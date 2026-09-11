#!/usr/bin/env python3
"""Generate a negative test case by mutating a block's own valid example.

A `tests/<prop>-fail.json` is only worth anything if the document is valid
EXCEPT for the thing it is named after. Hand-written cases in this repo were
not: 29 of 34 failed on an incidental `@type: ... is not of type 'array'` and
would have failed identically with the named rule deleted.

Starting from an example that already validates guarantees the opposite. Mutate
exactly one property and the only error left is the one the case is about.

Two mutations, in order of preference:
  drop    remove a required property -> "'<prop>' is a required property"
  retype  give a property a value of the wrong JSON type -> error AT that path

    python tools/generate_fail_cases.py <block-dir>              # list candidates
    python tools/generate_fail_cases.py <block-dir> --write      # write them
    python tools/generate_fail_cases.py <block-dir> --write --only schema:name
"""
import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent


def valid_example(block: Path):
    """The block's first example that validates -- the base for any mutation."""
    schema = json.loads((block / "resolvedSchema.json").read_text(encoding="utf-8"))
    v = Draft202012Validator(schema)
    for ex in sorted(block.glob("example*.json")):
        doc = json.loads(ex.read_text(encoding="utf-8"))
        if not list(v.iter_errors(doc)):
            return schema, ex, doc
    return schema, None, None


def errors(schema, doc):
    out = []
    for e in Draft202012Validator(schema).iter_errors(doc):
        out.append(("/".join(str(p) for p in e.absolute_path) or "(root)", e.message))
    return out


WRONG = {"object": 42, "array": 42, "string": 42, "number": "not-a-number",
         "integer": "not-an-integer", "boolean": "not-a-boolean"}


def candidates(schema, doc):
    """(property, mutation, mutated-doc) for each single-property mutation."""
    out = []
    required = schema.get("required", []) or []
    for prop in required:
        if prop in doc and not prop.startswith("@"):
            d = json.loads(json.dumps(doc)); d.pop(prop)
            out.append((prop, "drop", d))
    props = (schema.get("properties") or {})
    for prop, spec in props.items():
        if prop.startswith("@") or prop not in doc or prop in required:
            continue
        t = spec.get("type")
        t = t[0] if isinstance(t, list) and t else t
        if t in WRONG:
            d = json.loads(json.dumps(doc)); d[prop] = WRONG[t]
            out.append((prop, f"retype({t})", d))

    if out:
        return out

    # Empirical fallback. An anyOf-rooted block (spatialExtent is Box | Line |
    # Point | PlaceName) has no root `required` and no root `properties`, so the
    # schema-driven paths above find nothing. Mutate keys the example actually
    # carries and keep whichever mutation the validator rejects; caller still
    # checks the error is about that property and is the only one.
    for prop in [k for k in doc if not k.startswith("@")]:
        for label, value in (("drop", None), ("retype(number)", 42),
                             ("retype(string)", "not-valid"), ("retype(object)", {})):
            d = json.loads(json.dumps(doc))
            if label == "drop":
                d.pop(prop)
            else:
                d[prop] = value
            out.append((prop, label, d))
    return out


def slug(prop: str) -> str:
    return prop.split(":")[-1]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("block")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--only", help="only this property")
    ap.add_argument("--max", type=int, default=3, help="cases to write (default 3)")
    args = ap.parse_args()

    block = (ROOT / args.block).resolve()
    schema, ex, doc = valid_example(block)
    if doc is None:
        print(f"  SKIP {args.block}: no example validates, so no clean base to mutate")
        return 0
    print(f"  base: {ex.name}")

    # Best mutation per property. Rank matters: an error whose PATH names the
    # property proves that constraint fired, while an anyOf failure reported at
    # (root) prints the whole instance, so every token "matches" and nothing is
    # proved. test_fail_cases.py discounts the latter, so generating one would
    # produce a case its own checker rejects.
    best = {}
    for prop, how, mutated in candidates(schema, doc):
        if args.only and prop != args.only:
            continue
        errs = errors(schema, mutated)
        if not errs:
            continue
        want = slug(prop).lower()
        by_path = [e for e in errs if want in e[0].lower()]
        by_msg = [e for e in errs
                  if not e[1].lstrip().startswith("{")
                  and "is not valid under any of the given schemas" not in e[1]
                  and want in e[1].lower()]
        if by_path:
            rank, hit = 0, by_path[0]
        elif by_msg:
            rank, hit = 1, by_msg[0]
        else:
            continue
        key = (rank, len(errs))
        if prop not in best or key < best[prop][0]:
            best[prop] = (key, how, mutated, hit, len(errs))

    written = 0
    for prop, (_, how, mutated, hit, nerr) in sorted(best.items(), key=lambda kv: kv[1][0]):
        errs_n = nerr
        name = f"{slug(prop)}-fail.json"
        print(f"    {name:<30} {how:<14} {errs_n} error(s); evidence: "
              f"{hit[0]}: {hit[1][:58]}")
        if args.write:
            t = block / "tests"; t.mkdir(exist_ok=True)
            (t / name).write_text(json.dumps(mutated, indent=2) + "\n", encoding="utf-8")
            written += 1
            if written >= args.max:
                break
    if args.write:
        print(f"  wrote {written} case(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
