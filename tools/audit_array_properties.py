#!/usr/bin/env python3
"""Which array-typed properties are missing from FrameAndValidate's restore lists?

JSON-LD compaction flattens any single-valued array. A property declared
``type: array`` in a schema therefore fails that schema the moment a document
carries exactly ONE value -- unless FrameAndValidate.py restores it, from
ARRAY_PROPERTIES (every document) or STRUCTURE_ARRAY_KEYS (bare-structure
documents only).

Those lists are hand-maintained, and until 2026-10-01 nothing compared them
against the schemas. Two entries were missing and both were found by accident:
cdif:has_ForeignKey, when profile-datastructure's foreign-key example was
assumed to be bad content, and cdi:has_DataStructureComponent, which meant a
data structure with exactly one component could not validate. This tool is the
check that was absent.

Three buckets, because the lists are keyed on property NAME ALONE:

  MISSING   array-typed at every declaring site, absent from both lists.
            Safe to add: there is no scalar site for a wrapper to break.
  CONFLICT  array in some schemas, scalar in others. Adding these by name WOULD
            break their scalar sites -- they need parent_key / type_list keying
            instead (see schema:identifier on an instrument vs on a Person).
            Reported for visibility, never as something to add.
  LISTED    already restored.

Usage:
    python tools/audit_array_properties.py                 # report
    python tools/audit_array_properties.py --strict        # exit 1 if MISSING
    python tools/audit_array_properties.py --self-test     # prove the checks fire
"""
import argparse
import ast
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SOURCES = REPO / "_sources"
# The normative copy. A release repo's copy is generated and may lag.
FRAME_AND_VALIDATE = REPO.parent / "validation" / "tools" / "FrameAndValidate.py"

LIST_NAMES = ("ARRAY_PROPERTIES", "STRUCTURE_ARRAY_KEYS")

# Two spellings, two patterns, and the difference is not cosmetic. A multi-line
# list closes with "]" in COLUMN 0, so the closer must be anchored there: a
# non-greedy ".*?" followed by an unanchored "]" stops at the first bracket that
# happens to end a line, and ARRAY_PROPERTIES' own comments contain "[type]".
# That produced an unclosed "[" and a SyntaxError out of literal_eval.
LIST_RE_MULTILINE = r"^{}\s*=\s*(\[.*?^\])"
LIST_RE_ONELINE = r"^{}\s*=\s*(\([^\n]*\))\s*$"


def restore_lists(path=None):
    """Union of the lists that wrap a single value back into an array.

    Both spellings matter: ARRAY_PROPERTIES is a multi-line list and
    STRUCTURE_ARRAY_KEYS a single-line tuple, and a regex written for one
    silently misses the other -- which it did on the first pass of this sweep,
    reporting cdif:semantic as missing when it was handled.
    """
    path = Path(path or FRAME_AND_VALIDATE)
    text = path.read_text(encoding="utf-8")
    out = set()
    for name in LIST_NAMES:
        values = extract_list(text, name)
        if values is None:
            print("::warning::%s not found in %s" % (name, path), file=sys.stderr)
            continue
        out |= set(values)
    return out


def extract_list(text, name):
    """The literal value of a module-level list/tuple, or None.

    Raises if a pattern matches but the text does not evaluate -- a partial
    match is a broken pattern, not an absent list, and silently skipping it
    would make every entry look unrestored.
    """
    m = re.search(LIST_RE_MULTILINE.format(name), text, re.S | re.M)
    if not m:
        m = re.search(LIST_RE_ONELINE.format(name), text, re.M)
    if not m:
        return None
    return ast.literal_eval(m.group(1))


def classify(defn):
    """'array', 'scalar', 'mixed' or 'ref' for one property definition."""
    if not isinstance(defn, dict):
        return "scalar"
    if defn.get("type") == "array":
        return "array"
    branches = []
    for kw in ("anyOf", "oneOf"):
        for b in defn.get(kw) or []:
            if isinstance(b, dict):
                branches.append("array" if b.get("type") == "array" else "scalar")
    if branches:
        return "mixed" if "scalar" in branches and "array" in branches else branches[0]
    if "$ref" in defn and "type" not in defn:
        return "ref"
    return "scalar"


def walk(node, out, where):
    """Record every `properties` entry as name -> kind -> [locations]."""
    if isinstance(node, dict):
        props = node.get("properties")
        if isinstance(props, dict):
            for name, defn in props.items():
                if not name.startswith("@"):
                    out[name][classify(defn)].append(where)
        for v in node.values():
            walk(v, out, where)
    elif isinstance(node, list):
        for v in node:
            walk(v, out, where)


def survey(sources=None):
    sources = Path(sources or SOURCES)
    props = defaultdict(lambda: defaultdict(list))
    files = [f for f in sorted(sources.glob("**/schema.yaml"))
             if "archive" not in f.parts]
    for f in files:
        try:
            doc = yaml.safe_load(f.read_text(encoding="utf-8"))
        except Exception as e:
            print("::warning::unreadable %s: %s" % (f, e), file=sys.stderr)
            continue
        walk(doc, props, str(f.relative_to(sources)).replace("\\", "/"))
    return props, len(files)


def buckets(props, listed):
    missing, conflict = [], []
    for name, kinds in sorted(props.items()):
        if name in listed:
            continue
        if not (kinds.get("array") or kinds.get("mixed")):
            continue
        scalar = kinds.get("scalar", []) + kinds.get("ref", []) + kinds.get("mixed", [])
        row = (name, len(kinds.get("array", [])), len(scalar))
        (conflict if scalar else missing).append(row)
    return missing, conflict


SELF_TESTS = [
    ("array everywhere -> MISSING", {"a": {"array": ["x", "y"]}}, "missing", set()),
    ("scalar everywhere -> ignored", {"a": {"scalar": ["x"]}}, None, set()),
    ("array + scalar -> CONFLICT", {"a": {"array": ["x"], "scalar": ["y"]}}, "conflict", set()),
    ("array + $ref -> CONFLICT", {"a": {"array": ["x"], "ref": ["y"]}}, "conflict", set()),
    ("anyOf both -> CONFLICT", {"a": {"mixed": ["x"]}}, "conflict", set()),
    ("listed -> ignored", {"a": {"array": ["x"]}}, None, {"a"}),
]

CLASSIFY_TESTS = [
    ({"type": "array"}, "array"),
    ({"type": "string"}, "scalar"),
    ({"$ref": "x"}, "ref"),
    ({"anyOf": [{"type": "array"}, {"type": "string"}]}, "mixed"),
]


def self_test():
    """Prove each bucket decision fires, so a silent misclassification shows up."""
    fails = 0
    for label, props, want, listed in SELF_TESTS:
        miss, conf = buckets(props, listed)
        got = "missing" if miss else ("conflict" if conf else None)
        ok = got == want
        fails += not ok
        print("  %s %s: got %r, want %r" % ("ok  " if ok else "FAIL", label, got, want))

    for defn, want in CLASSIFY_TESTS:
        got = classify(defn)
        ok = got == want
        fails += not ok
        print("  %s classify(%s) -> %r, want %r"
              % ("ok  " if ok else "FAIL", defn, got, want))

    # Both list spellings must parse out of the real file, or the audit
    # under-reports by calling a handled property missing.
    if FRAME_AND_VALIDATE.exists():
        text = FRAME_AND_VALIDATE.read_text(encoding="utf-8")
        for name in LIST_NAMES:
            # Must EVALUATE, not merely match. Checking re.search alone passed
            # while literal_eval raised SyntaxError on a partial match -- a test
            # that reported success for a function that could not run at all.
            try:
                values = extract_list(text, name)
                ok = bool(values)
                detail = "%d entries" % len(values) if values else "empty/absent"
            except Exception as e:
                ok, detail = False, "%s: %s" % (type(e).__name__, e)
            fails += not ok
            print("  %s %s evaluates out of the normative source (%s)"
                  % ("ok  " if ok else "FAIL", name, detail))
    else:
        print("  skip  %s not present" % FRAME_AND_VALIDATE)

    print("\n%s: %d failing check(s)" % ("PASS" if not fails else "FAIL", fails))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any array-typed property is unrestored")
    ap.add_argument("--self-test", action="store_true",
                    help="prove the bucket checks still fire, then exit")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    if not FRAME_AND_VALIDATE.exists():
        print("::error::normative source not found: %s" % FRAME_AND_VALIDATE)
        return 1

    listed = restore_lists()
    props, nfiles = survey()
    missing, conflict = buckets(props, listed)

    print("schema.yaml scanned      : %d" % nfiles)
    print("distinct properties      : %d" % len(props))
    print("restored (both lists)    : %d" % len(listed))
    print()
    print("=== MISSING -- array-typed everywhere, unrestored (%d) ===" % len(missing))
    for name, na, _ in missing:
        print("  %-52s %d array site(s)" % (name, na))
    if not missing:
        print("  (none)")
    print()
    print("=== CONFLICT -- needs parent_key/type_list, NOT a name entry (%d) ==="
          % len(conflict))
    for name, na, ns in conflict:
        print("  %-52s %d array / %d scalar" % (name, na, ns))
    print()
    if missing and args.strict:
        print("::error::%d array-typed propert(ies) are not restored; a document "
              "carrying exactly one value will fail its own schema" % len(missing))
        return 1
    print("OK: every array-typed property is restored." if not missing
          else "Report only (--strict to fail).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
