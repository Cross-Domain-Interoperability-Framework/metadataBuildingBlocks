#!/usr/bin/env python3
"""
Validate all example JSON files against their resolved schemas.

Uses resolve_schema.py's resolver to fully inline $ref references before
validation, so $defs and cross-file references are handled correctly.

Usage:
    python tools/validate_examples.py           # validate all examples
    python tools/validate_examples.py --verbose  # show pass/fail for each
    python tools/validate_examples.py --filter person  # only matching paths
"""

import argparse
import json
import sys
import yaml
from pathlib import Path

# Import the root resolver (handles transitive internal $defs refs correctly)
_repo_root = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, _repo_root)
from resolve_schema import SchemaResolver

# Fallback: tools/resolve_schema.py (handles recursive schemas better)
import importlib.util
_tools_spec = importlib.util.spec_from_file_location(
    "tools_resolve_schema",
    str(Path(__file__).resolve().parent / "resolve_schema.py"))
_tools_resolver = importlib.util.module_from_spec(_tools_spec)
_tools_spec.loader.exec_module(_tools_resolver)
_fallback_resolve_file = _tools_resolver.resolve_file
_fallback_strip = _tools_resolver.strip_metadata_keys

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = REPO_ROOT / "_sources"


def find_example_schema_pairs():
    """Find all (example.json, schema.yaml) pairs in the sources tree."""
    pairs = []
    for example_path in sorted(SOURCES_DIR.rglob("example*.json")):
        schema_path = example_path.parent / "schema.yaml"
        if schema_path.exists():
            pairs.append((example_path, schema_path))
    return pairs


def resolve_for_validation(schema_path: Path) -> dict:
    """Resolve a schema file into a fully-inlined JSON Schema dict.

    Uses the root SchemaResolver (correct transitive $defs handling).
    Falls back to tools/resolve_schema.py for schemas with circular refs.
    """
    try:
        resolver = SchemaResolver(verbose=False, inline_single_use=False)
        resolved = resolver.resolve(str(schema_path.resolve()))
        resolved.pop("$schema", None)
        return resolved
    except RecursionError:
        resolved = _fallback_resolve_file(schema_path.resolve(), set())
        _fallback_strip(resolved)
        resolved.pop("$schema", None)
        return resolved


def validate_example(example_path: Path, schema: dict):
    """Validate a JSON example against a resolved schema. Returns list of error strings."""
    with open(example_path) as f:
        instance = json.load(f)

    validator = Draft202012Validator(schema)
    errors = []
    for error in validator.iter_errors(instance):
        path = "/".join(str(p) for p in error.absolute_path) or "(root)"
        errors.append(f"  {path}: {error.message[:200]}")
    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate all example JSON files against their schemas.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show pass/fail for each example")
    parser.add_argument("--filter", "-f", type=str, default="", help="Only validate paths containing this string")
    args = parser.parse_args()

    pairs = find_example_schema_pairs()
    if args.filter:
        pairs = [(e, s) for e, s in pairs if args.filter.lower() in str(e).lower()]

    passed = 0
    failed = 0
    errored = 0
    failures = []

    for example_path, schema_path in pairs:
        rel = example_path.relative_to(REPO_ROOT)
        try:
            schema = resolve_for_validation(schema_path)
            try:
                errors = validate_example(example_path, schema)
            except RecursionError:
                # Root resolver may produce circular $ref that jsonschema
                # can't handle; fall back to tools resolver which inlines fully
                resolved = _fallback_resolve_file(schema_path.resolve(), set())
                _fallback_strip(resolved)
                resolved.pop("$schema", None)
                errors = validate_example(example_path, resolved)
            if errors:
                failed += 1
                failures.append((rel, errors))
                if args.verbose:
                    print(f"FAIL {rel}")
                    for e in errors[:5]:
                        print(e)
            else:
                passed += 1
                if args.verbose:
                    print(f"PASS {rel}")
        except Exception as ex:
            errored += 1
            failures.append((rel, [f"  {type(ex).__name__}: {str(ex)[:200]}"]))
            if args.verbose:
                print(f"ERROR {rel}: {type(ex).__name__}: {str(ex)[:150]}")

    print(f"\n{'='*60}")
    print(f"Results: {passed} passed, {failed} failed, {errored} errors (of {len(pairs)} total)")
    print(f"{'='*60}")

    if failures:
        print("\nFailures:")
        for rel, errors in failures:
            print(f"\n{rel}:")
            for e in errors[:5]:
                print(e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
