#!/usr/bin/env python3
"""Comprehensive audit tool for OGC Building Block repositories.

Scans a _sources/ directory and checks each building block for:
  1. File completeness (schema.yaml, bblock.json, examples, etc.)
  2. schema.yaml vs *Schema.json consistency
  3. resolvedSchema.json freshness (re-resolve and compare)
  4. Example validation against resolved schemas
  5. SHACL rules completeness relative to schema properties
  6. Example coverage of schema properties

Designed to work with any building block repository that follows the
OGC Building Blocks directory pattern.

Usage:
    python audit_building_blocks.py [_sources_dir] [options]

    # Audit current repo
    python audit_building_blocks.py

    # Audit specific repo
    python audit_building_blocks.py /path/to/repo/_sources

    # Filter to specific building blocks
    python audit_building_blocks.py --filter cdifCore

    # Output JSON report
    python audit_building_blocks.py --json -o report.json
"""

import argparse
import json
import sys
import os
import copy
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

try:
    from jsonschema import Draft202012Validator
except ImportError:
    Draft202012Validator = None

# ---------------------------------------------------------------------------
# Add tools/ to path so we can import resolve_schema
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

try:
    from resolve_schema import resolve_file, strip_metadata_keys
except ImportError:
    resolve_file = None
    strip_metadata_keys = None


# ---------------------------------------------------------------------------
# Building block discovery
# ---------------------------------------------------------------------------

REQUIRED_FILES = ["schema.yaml", "bblock.json"]
EXPECTED_FILES = ["description.md", "context.jsonld", "rules.shacl"]
GENERATED_FILES = ["resolvedSchema.json"]  # checked for freshness

# Directories to skip
SKIP_DIRS = {"tests", "assets", "build", ".git", "node_modules", "__pycache__"}


def discover_building_blocks(sources_dir):
    """Find all building block directories under sources_dir.

    A building block directory contains at least schema.yaml.
    Returns list of (category, name, path) tuples sorted by path.
    """
    bbs = []
    for schema_path in sorted(sources_dir.rglob("schema.yaml")):
        bb_dir = schema_path.parent
        # Skip nested dirs (tests/, assets/, etc.)
        if any(part in SKIP_DIRS for part in bb_dir.parts):
            continue
        # Derive category and name from path relative to sources_dir
        rel = bb_dir.relative_to(sources_dir)
        parts = rel.parts
        if len(parts) >= 2:
            category = parts[0]
            name = parts[-1]
        elif len(parts) == 1:
            category = ""
            name = parts[0]
        else:
            continue
        bbs.append((category, name, bb_dir))
    return bbs


# ---------------------------------------------------------------------------
# Check 1: File completeness
# ---------------------------------------------------------------------------

def check_files(bb_dir, name):
    """Check for required, expected, and generated files."""
    issues = []
    info = []

    for f in REQUIRED_FILES:
        if not (bb_dir / f).exists():
            issues.append(f"MISSING required file: {f}")

    for f in EXPECTED_FILES:
        if not (bb_dir / f).exists():
            info.append(f"Missing optional file: {f}")

    # Check for examples
    examples = list(bb_dir.glob("example*.json"))
    if not examples:
        # Check examples.yaml for inline examples
        if (bb_dir / "examples.yaml").exists():
            info.append("Has examples.yaml but no standalone example*.json files")
        else:
            issues.append("No example files found (example*.json or examples.yaml)")
    else:
        info.append(f"Found {len(examples)} example file(s)")

    # Check for generated schema files
    for f in GENERATED_FILES:
        if not (bb_dir / f).exists():
            issues.append(f"MISSING generated file: {f}")

    # Check for *Schema.json
    schema_jsons = list(bb_dir.glob("*Schema.json"))
    if not schema_jsons:
        issues.append("MISSING *Schema.json (run regenerate_schema_json.py)")

    return issues, info


# ---------------------------------------------------------------------------
# Check 2: schema.yaml vs *Schema.json consistency
# ---------------------------------------------------------------------------

def load_yaml(path):
    """Load YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path):
    """Load JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_ref(ref_str):
    """Normalize $ref for comparison.

    The *Schema.json files rewrite refs from 'dir/schema.yaml' to
    'dir/dirNameSchema.json', so we normalize to just the directory path.
    Fragment-only refs (#/$defs/X) and URL refs are compared as-is.
    """
    if not ref_str:
        return ref_str
    if ref_str.startswith("#") or ref_str.startswith("http"):
        return ref_str
    # Strip the filename, keep just the directory path
    import posixpath
    return posixpath.dirname(ref_str)


def compare_schemas(yaml_schema, json_schema, path=""):
    """Compare YAML source schema with generated JSON schema.

    Returns list of difference descriptions. Ignores $ref extension
    differences (.yaml vs .json).
    """
    diffs = []
    if type(yaml_schema) != type(json_schema):
        diffs.append(f"{path}: type mismatch: {type(yaml_schema).__name__} vs {type(json_schema).__name__}")
        return diffs

    if isinstance(yaml_schema, dict):
        yaml_keys = set(yaml_schema.keys())
        json_keys = set(json_schema.keys())

        for k in yaml_keys - json_keys:
            diffs.append(f"{path}.{k}: missing from JSON schema")
        for k in json_keys - yaml_keys:
            diffs.append(f"{path}.{k}: extra in JSON schema")

        for k in yaml_keys & json_keys:
            if k == "$ref":
                # $ref extension differences (.yaml vs .json) are expected
                if normalize_ref(yaml_schema[k]) != normalize_ref(json_schema[k]):
                    diffs.append(f"{path}.$ref: {yaml_schema[k]} vs {json_schema[k]}")
            elif k == "$schema":
                # $schema differences are OK
                pass
            else:
                diffs.extend(compare_schemas(yaml_schema[k], json_schema[k], f"{path}.{k}"))

    elif isinstance(yaml_schema, list):
        if len(yaml_schema) != len(json_schema):
            diffs.append(f"{path}: array length {len(yaml_schema)} vs {len(json_schema)}")
        else:
            for i, (a, b) in enumerate(zip(yaml_schema, json_schema)):
                diffs.extend(compare_schemas(a, b, f"{path}[{i}]"))

    else:
        if yaml_schema != json_schema:
            diffs.append(f"{path}: value {yaml_schema!r} vs {json_schema!r}")

    return diffs


def check_schema_json_consistency(bb_dir, name):
    """Compare schema.yaml with *Schema.json."""
    issues = []
    schema_yaml_path = bb_dir / "schema.yaml"
    if not schema_yaml_path.exists():
        return issues

    yaml_data = load_yaml(schema_yaml_path)

    # Find *Schema.json
    schema_jsons = list(bb_dir.glob("*Schema.json"))
    # Exclude resolved and structured
    schema_jsons = [p for p in schema_jsons
                    if "resolved" not in p.name.lower()
                    and "structured" not in p.name.lower()]
    if not schema_jsons:
        return issues

    json_data = load_json(schema_jsons[0])
    diffs = compare_schemas(yaml_data, json_data)
    for d in diffs[:5]:  # limit to first 5
        issues.append(f"schema.yaml vs {schema_jsons[0].name}: {d}")
    if len(diffs) > 5:
        issues.append(f"  ... and {len(diffs) - 5} more differences")

    return issues


# ---------------------------------------------------------------------------
# Check 3: resolvedSchema.json freshness
# ---------------------------------------------------------------------------

def check_resolved_schema(bb_dir, name):
    """Re-resolve schema.yaml and compare with existing resolvedSchema.json."""
    issues = []
    resolved_path = bb_dir / "resolvedSchema.json"
    schema_path = bb_dir / "schema.yaml"

    if not schema_path.exists() or not resolved_path.exists():
        return issues

    if resolve_file is None:
        issues.append("Cannot check resolvedSchema freshness (resolve_schema not importable)")
        return issues

    try:
        fresh = resolve_file(schema_path.resolve(), set())
        if strip_metadata_keys:
            fresh = strip_metadata_keys(fresh)
        existing = load_json(resolved_path)

        # Compare top-level property keys as a quick freshness check
        fresh_props = set(fresh.get("properties", {}).keys())
        existing_props = set(existing.get("properties", {}).keys())

        missing = fresh_props - existing_props
        extra = existing_props - fresh_props

        if missing:
            issues.append(f"resolvedSchema.json STALE — missing properties: {', '.join(sorted(missing))}")
        if extra:
            issues.append(f"resolvedSchema.json STALE — extra properties: {', '.join(sorted(extra))}")

    except Exception as e:
        issues.append(f"resolvedSchema.json check error: {e}")

    return issues


# ---------------------------------------------------------------------------
# Check 4: Example validation
# ---------------------------------------------------------------------------

def check_example_validation(bb_dir, name):
    """Validate all example*.json against resolved schema."""
    issues = []
    info = []

    if Draft202012Validator is None:
        issues.append("Cannot validate examples (jsonschema not installed)")
        return issues, info

    schema_path = bb_dir / "schema.yaml"
    if not schema_path.exists():
        return issues, info

    examples = sorted(bb_dir.glob("example*.json"))
    if not examples:
        return issues, info

    # Prefer existing resolvedSchema.json (CI-generated, handles allOf correctly)
    # Fall back to re-resolving from source
    resolved_path = bb_dir / "resolvedSchema.json"
    resolved = None
    if resolved_path.exists():
        try:
            resolved = load_json(resolved_path)
        except Exception:
            pass

    if resolved is None:
        if resolve_file is None:
            issues.append("Cannot validate examples (no resolvedSchema.json and resolve_schema not importable)")
            return issues, info
        try:
            resolved = resolve_file(schema_path.resolve(), set())
            if strip_metadata_keys:
                resolved = strip_metadata_keys(resolved)
        except Exception as e:
            issues.append(f"Schema resolution failed: {e}")
            return issues, info

    validator = Draft202012Validator(resolved)

    for ex_path in examples:
        try:
            example = load_json(ex_path)
        except Exception as e:
            issues.append(f"{ex_path.name}: JSON parse error: {e}")
            continue

        errors = list(validator.iter_errors(example))
        if errors:
            for err in errors[:3]:
                path_str = "/".join(str(p) for p in err.absolute_path) if err.absolute_path else "(root)"
                issues.append(f"{ex_path.name}: {path_str}: {err.message[:120]}")
            if len(errors) > 3:
                issues.append(f"{ex_path.name}: ... and {len(errors) - 3} more errors")
        else:
            info.append(f"{ex_path.name}: PASS")

    return issues, info


# ---------------------------------------------------------------------------
# Check 5: SHACL completeness relative to schema
# ---------------------------------------------------------------------------

def extract_schema_properties(schema, prefix=""):
    """Extract property paths from a JSON schema."""
    props = set()
    if not isinstance(schema, dict):
        return props

    for key, val in schema.get("properties", {}).items():
        if key.startswith("@"):
            continue
        full = f"{prefix}{key}" if not prefix else f"{prefix}.{key}"
        props.add(full)
        if isinstance(val, dict):
            props |= extract_schema_properties(val, full)

    # Walk allOf, anyOf, oneOf
    for keyword in ("allOf", "anyOf", "oneOf"):
        for item in schema.get(keyword, []):
            props |= extract_schema_properties(item, prefix)

    # Walk items
    items = schema.get("items", {})
    if isinstance(items, dict):
        props |= extract_schema_properties(items, prefix)

    return props


def check_shacl_completeness(bb_dir, name):
    """Check if SHACL rules exist and cover key schema properties."""
    issues = []
    info = []

    shacl_path = bb_dir / "rules.shacl"
    schema_path = bb_dir / "schema.yaml"

    if not schema_path.exists():
        return issues, info

    if not shacl_path.exists():
        # Not all BBs need SHACL
        info.append("No rules.shacl file")
        return issues, info

    try:
        shacl_text = shacl_path.read_text(encoding="utf-8")
    except Exception as e:
        issues.append(f"Cannot read rules.shacl: {e}")
        return issues, info

    # Extract schema properties
    try:
        schema = load_yaml(schema_path)
        schema_props = extract_schema_properties(schema)
    except Exception:
        schema_props = set()

    # Check for sh:NodeShape definitions
    if "sh:NodeShape" not in shacl_text:
        issues.append("rules.shacl has no sh:NodeShape definitions")
    else:
        # Count shapes
        shape_count = shacl_text.count("sh:NodeShape")
        prop_shape_count = shacl_text.count("sh:PropertyShape")
        info.append(f"SHACL: {shape_count} NodeShape(s), {prop_shape_count} PropertyShape(s)")

    # Check which schema properties are referenced in SHACL
    # Simple heuristic: look for property path URIs in the SHACL text
    covered = set()
    uncovered = set()
    for prop in schema_props:
        # Normalize: schema:name → schema:name
        local_name = prop.split(".")[-1]  # innermost property
        if ":" in local_name:
            prefix, local = local_name.split(":", 1)
            # Check if the property appears in SHACL
            if local in shacl_text or local_name in shacl_text:
                covered.add(prop)
            else:
                uncovered.add(prop)

    if covered:
        info.append(f"SHACL covers {len(covered)}/{len(covered) + len(uncovered)} schema properties")

    return issues, info


# ---------------------------------------------------------------------------
# Check 6: Example property coverage
# ---------------------------------------------------------------------------

def extract_example_properties(data, prefix=""):
    """Extract property paths used in an example JSON."""
    props = set()
    if isinstance(data, dict):
        for key, val in data.items():
            if key.startswith("@"):
                continue
            full = f"{prefix}{key}" if not prefix else f"{prefix}.{key}"
            props.add(full)
            if isinstance(val, dict):
                props |= extract_example_properties(val, full)
            elif isinstance(val, list):
                for item in val:
                    props |= extract_example_properties(item, full)
    return props


def check_example_coverage(bb_dir, name):
    """Check whether examples exercise all schema properties."""
    issues = []
    info = []

    schema_path = bb_dir / "schema.yaml"
    if not schema_path.exists():
        return issues, info

    try:
        schema = load_yaml(schema_path)
        schema_props = extract_schema_properties(schema)
    except Exception:
        return issues, info

    # Collect all properties used across all examples
    all_example_props = set()
    examples = sorted(bb_dir.glob("example*.json"))
    for ex_path in examples:
        try:
            data = load_json(ex_path)
            all_example_props |= extract_example_properties(data)
        except Exception:
            continue

    if not examples:
        return issues, info

    # Find schema properties not exercised by any example
    # Only check top-level domain properties (schema:X, prov:X, etc.)
    domain_props = {p for p in schema_props if ":" in p.split(".")[-1]}
    exercised = set()
    for sp in domain_props:
        leaf = sp.split(".")[-1]
        if any(leaf in ep for ep in all_example_props):
            exercised.add(sp)

    missing = domain_props - exercised
    if missing and len(missing) <= 10:
        for m in sorted(missing):
            info.append(f"Property not exercised in examples: {m}")
    elif missing:
        info.append(f"{len(missing)} schema properties not exercised in examples")

    if exercised:
        info.append(f"Examples cover {len(exercised)}/{len(domain_props)} domain properties")

    return issues, info


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

class AuditResult:
    def __init__(self, category, name, bb_dir):
        self.category = category
        self.name = name
        self.bb_dir = str(bb_dir)
        self.issues = []
        self.info = []
        self.status = "PASS"

    def add_issues(self, issues):
        self.issues.extend(issues)
        if issues:
            self.status = "FAIL"

    def add_info(self, info):
        self.info.extend(info)

    def to_dict(self):
        return {
            "category": self.category,
            "name": self.name,
            "status": self.status,
            "issues": self.issues,
            "info": self.info,
        }


def print_report(results, verbose=False):
    """Print human-readable audit report."""
    total = len(results)
    passed = sum(1 for r in results if r.status == "PASS")
    failed = total - passed

    print(f"\n{'=' * 70}")
    print(f"Building Block Audit Report")
    print(f"{'=' * 70}")

    # Group by category
    by_category = defaultdict(list)
    for r in results:
        by_category[r.category].append(r)

    for category in sorted(by_category.keys()):
        cat_results = by_category[category]
        cat_pass = sum(1 for r in cat_results if r.status == "PASS")
        print(f"\n--- {category or '(root)'} ({cat_pass}/{len(cat_results)} pass) ---")

        for r in cat_results:
            marker = "PASS" if r.status == "PASS" else "FAIL"
            print(f"  [{marker}] {r.name}")

            if r.issues:
                for issue in r.issues:
                    print(f"    ERROR: {issue}")

            if verbose and r.info:
                for info in r.info:
                    print(f"    info: {info}")

    print(f"\n{'=' * 70}")
    print(f"Summary: {passed} passed, {failed} failed (of {total} building blocks)")
    print(f"{'=' * 70}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def audit_building_block(category, name, bb_dir, checks=None):
    """Run all audit checks on a single building block."""
    result = AuditResult(category, name, bb_dir)

    # Check 1: File completeness
    if not checks or "files" in checks:
        issues, info = check_files(bb_dir, name)
        result.add_issues(issues)
        result.add_info(info)

    # Check 2: schema.yaml vs *Schema.json
    if not checks or "schema-json" in checks:
        issues = check_schema_json_consistency(bb_dir, name)
        result.add_issues(issues)

    # Check 3: resolvedSchema freshness
    if not checks or "resolved" in checks:
        issues = check_resolved_schema(bb_dir, name)
        result.add_issues(issues)

    # Check 4: Example validation
    if not checks or "examples" in checks:
        issues, info = check_example_validation(bb_dir, name)
        result.add_issues(issues)
        result.add_info(info)

    # Check 5: SHACL completeness
    if not checks or "shacl" in checks:
        issues, info = check_shacl_completeness(bb_dir, name)
        result.add_issues(issues)
        result.add_info(info)

    # Check 6: Example coverage
    if not checks or "coverage" in checks:
        issues, info = check_example_coverage(bb_dir, name)
        result.add_issues(issues)
        result.add_info(info)

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Comprehensive audit of OGC Building Block repositories"
    )
    parser.add_argument(
        "sources_dir",
        nargs="?",
        default=None,
        help="Path to _sources/ directory (default: auto-detect)"
    )
    parser.add_argument(
        "--filter", "-f",
        type=str,
        default=None,
        help="Only audit BBs whose name contains this string"
    )
    parser.add_argument(
        "--checks", "-c",
        type=str,
        default=None,
        help="Comma-separated list of checks to run: files,schema-json,resolved,examples,shacl,coverage"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show info messages in addition to errors"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output report as JSON"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        help="Output file (default: stdout)"
    )
    args = parser.parse_args()

    # Find sources directory
    if args.sources_dir:
        sources_dir = Path(args.sources_dir)
    else:
        # Auto-detect: look for _sources/ relative to CWD or script
        candidates = [
            Path.cwd() / "_sources",
            SCRIPT_DIR.parent / "_sources",
        ]
        sources_dir = None
        for c in candidates:
            if c.is_dir():
                sources_dir = c
                break
        if sources_dir is None:
            print("ERROR: Cannot find _sources/ directory. Provide path as argument.",
                  file=sys.stderr)
            sys.exit(1)

    print(f"Auditing: {sources_dir}")

    # Parse checks
    checks = None
    if args.checks:
        checks = set(args.checks.split(","))

    # Discover building blocks
    bbs = discover_building_blocks(sources_dir)
    if args.filter:
        bbs = [(c, n, p) for c, n, p in bbs if args.filter.lower() in n.lower()]

    print(f"Found {len(bbs)} building blocks\n")

    # Run audit
    results = []
    for category, name, bb_dir in bbs:
        result = audit_building_block(category, name, bb_dir, checks)
        results.append(result)
        # Progress indicator
        marker = "." if result.status == "PASS" else "F"
        print(marker, end="", flush=True)
    print()

    # Output
    if args.json_output:
        report = {
            "sources_dir": str(sources_dir),
            "total": len(results),
            "passed": sum(1 for r in results if r.status == "PASS"),
            "failed": sum(1 for r in results if r.status == "FAIL"),
            "results": [r.to_dict() for r in results],
        }
        output = json.dumps(report, indent=2)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"\nJSON report written to {args.output}")
        else:
            print(output)
    else:
        print_report(results, verbose=args.verbose)


if __name__ == "__main__":
    main()
