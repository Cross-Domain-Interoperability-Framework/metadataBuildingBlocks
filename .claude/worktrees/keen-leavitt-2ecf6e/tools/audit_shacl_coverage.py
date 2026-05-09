#!/usr/bin/env python3
"""
Audit SHACL coverage against JSON Schema for all building blocks.

For each building block, compares properties defined in schema.yaml with
sh:PropertyShape paths in rules.shacl. Reports missing shapes, extra shapes,
and severity mismatches.

Processes leaf BBs first (no external $ref), then composites, then profiles.

Usage:
    python tools/audit_shacl_coverage.py [--verbose]
"""

import yaml
import re
import sys
from pathlib import Path

BB_ROOT = Path(__file__).resolve().parent.parent / "_sources"


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def extract_schema_properties(schema, depth=0):
    """Extract property paths from a schema.yaml, skipping $ref'd externals."""
    props = {}
    if not isinstance(schema, dict):
        return props

    for key, val in schema.get("properties", {}).items():
        if key.startswith("@"):
            continue  # skip @context, @id, @type
        props[key] = {
            "required": False,
            "type": val.get("type") if isinstance(val, dict) else None,
            "description": (val.get("description", "") or "")[:80] if isinstance(val, dict) else "",
        }

    # Check required
    for req in schema.get("required", []):
        if req in props:
            props[req]["required"] = True

    # Check allOf for additional required/anyOf constraints
    for entry in schema.get("allOf", []):
        if isinstance(entry, dict):
            for req in entry.get("required", []):
                if req in props:
                    props[req]["required"] = True
            # anyOf with required
            for ao in entry.get("anyOf", []):
                if isinstance(ao, dict):
                    for req in ao.get("required", []):
                        if req in props:
                            props[req]["required"] = "anyOf"

    return props


def extract_shacl_paths(shacl_text):
    """Extract sh:path values and their severity from SHACL Turtle text."""
    shapes = {}

    # Find property shape blocks
    # Pattern: cdifd:someName ... sh:path schema:something ...
    # This is a rough parser — looks for sh:path and sh:severity in nearby context

    # Split into shape blocks (separated by blank lines or .)
    blocks = re.split(r'\n\s*\.\s*\n', shacl_text)

    for block in blocks:
        # Find sh:path
        path_matches = re.findall(
            r'sh:path\s+(?:\[\s*sh:alternativePath\s*\(\s*(.*?)\s*\)\s*\]|(\S+))',
            block, re.DOTALL
        )

        severity = "Violation"  # default
        if "sh:severity sh:Warning" in block:
            severity = "Warning"
        elif "sh:severity sh:Info" in block:
            severity = "Info"

        min_count = None
        mc = re.search(r'sh:minCount\s+(\d+)', block)
        if mc:
            min_count = int(mc.group(1))

        for alt_paths, single_path in path_matches:
            if alt_paths:
                # alternativePath — extract individual paths
                paths = re.findall(r'(\w+:\w+)', alt_paths)
                for p in paths:
                    shapes[p] = {"severity": severity, "minCount": min_count,
                                 "alternativeWith": paths}
            elif single_path and ':' in single_path and not single_path.startswith('sh:'):
                shapes[single_path] = {"severity": severity, "minCount": min_count}

    return shapes


def has_external_refs(schema):
    """Check if schema has external $ref (../)."""
    text = yaml.dump(schema) if isinstance(schema, dict) else str(schema)
    return "../" in text


def audit_building_block(bb_dir, verbose=False):
    """Audit a single building block. Returns (name, issues)."""
    name = bb_dir.name
    schema_path = bb_dir / "schema.yaml"
    shacl_path = bb_dir / "rules.shacl"

    if not schema_path.exists():
        return name, []

    issues = []
    schema = load_yaml(schema_path)
    schema_props = extract_schema_properties(schema)

    if not shacl_path.exists():
        if schema_props:
            issues.append(("MISSING", "No rules.shacl file but schema has properties"))
        return name, issues

    shacl_text = shacl_path.read_text(encoding="utf-8")
    shacl_shapes = extract_shacl_paths(shacl_text)

    # Compare
    for prop, info in schema_props.items():
        if prop in shacl_shapes:
            shacl = shacl_shapes[prop]
            # Check severity consistency
            if info["required"] is True and shacl["severity"] == "Warning":
                issues.append(("SEVERITY", f"{prop}: required in schema but Warning in SHACL"))
            elif info["required"] is False and shacl["severity"] == "Violation" and shacl.get("minCount"):
                issues.append(("SEVERITY", f"{prop}: optional in schema but Violation with minCount in SHACL"))
        else:
            # Check if it's in an alternativePath
            in_alt = any(
                prop in (s.get("alternativeWith") or [])
                for s in shacl_shapes.values()
            )
            if not in_alt:
                if info["required"] is True:
                    issues.append(("MISSING_REQUIRED", f"{prop}: required in schema, no SHACL shape"))
                elif info["required"] == "anyOf":
                    issues.append(("MISSING_ANYOF", f"{prop}: part of anyOf requirement in schema, no SHACL shape"))
                elif verbose:
                    issues.append(("MISSING_OPTIONAL", f"{prop}: optional in schema, no SHACL shape"))

    # Check for SHACL shapes with no corresponding schema property
    for path, info in shacl_shapes.items():
        # Normalize: shacl might use schema:X but schema.yaml uses 'schema:X'
        if path not in schema_props:
            # Check alternativePaths
            alt = info.get("alternativeWith")
            if alt and any(p in schema_props for p in alt):
                continue
            if verbose:
                issues.append(("EXTRA_SHACL", f"{path}: SHACL shape exists but not in schema properties"))

    return name, issues


def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    # Collect all BB dirs
    bb_dirs = []
    for category in ["schemaorgProperties", "provProperties", "qualityProperties",
                      "cdifProperties", "skosProperties"]:
        cat_dir = BB_ROOT / category
        if cat_dir.exists():
            for d in sorted(cat_dir.iterdir()):
                if d.is_dir() and (d / "schema.yaml").exists():
                    bb_dirs.append(d)

    # Sort: leaves first, then composites
    leaves = []
    composites = []
    for d in bb_dirs:
        schema = load_yaml(d / "schema.yaml")
        if has_external_refs(schema):
            composites.append(d)
        else:
            leaves.append(d)

    # Profiles
    profiles = []
    profile_dir = BB_ROOT / "profiles" / "cdifProfiles"
    if profile_dir.exists():
        for d in sorted(profile_dir.iterdir()):
            if d.is_dir() and (d / "schema.yaml").exists():
                profiles.append(d)

    total_issues = 0

    for label, dirs in [("LEAF BUILDING BLOCKS", leaves),
                        ("COMPOSITE BUILDING BLOCKS", composites),
                        ("PROFILES", profiles)]:
        print(f"\n{'='*70}")
        print(f"  {label}")
        print(f"{'='*70}")

        for d in dirs:
            name, issues = audit_building_block(d, verbose=verbose)
            if issues:
                # Filter: only show MISSING_REQUIRED, MISSING_ANYOF, SEVERITY, MISSING by default
                shown = [i for i in issues
                         if verbose or i[0] in ("MISSING_REQUIRED", "MISSING_ANYOF",
                                                 "SEVERITY", "MISSING")]
                if shown:
                    print(f"\n  {name}:")
                    for itype, msg in shown:
                        print(f"    [{itype}] {msg}")
                    total_issues += len(shown)
                else:
                    print(f"  {name}: OK")
            else:
                print(f"  {name}: OK")

    print(f"\n{'='*70}")
    print(f"Total issues: {total_issues}")
    if not verbose:
        print("(Run with --verbose to see optional property gaps and extra SHACL shapes)")


if __name__ == "__main__":
    main()
