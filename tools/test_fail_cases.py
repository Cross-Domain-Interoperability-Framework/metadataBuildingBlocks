#!/usr/bin/env python3
"""Do the `tests/*-fail.json` cases actually fail?

The OGC building-block layout puts negative test cases in a `tests/` directory
beside each block. A file named `<thing>-fail.json` asserts "this document must
NOT validate". Nothing in this repo has been checking that claim, and a negative
test that quietly passes is worse than no test: it reports coverage it does not
have. That is the same failure this repo keeps meeting -- a rule that stops
working looks exactly like a rule that passes -- pointed at the tests instead of
at the rules.

For every `tests/*-fail.json` this validates the document against its OWN
block's `resolvedSchema.json` and reports:

    DEAD          the document validates cleanly -- the test asserts nothing
    MISDIRECTED   it fails, but on something other than the constraint its name
                  claims, so it would fail identically with that rule deleted
    ok            it fails, and an error actually concerns the named constraint

It also flags a case that is byte-identical to one in another block. Those are
copies, and a copy usually exercises a constraint the receiving block does not
have -- an `affiliation-fail.json` in `spatialExtent` tests nothing about
spatial extents even if it happens to fail for some unrelated reason.

    python tools/test_fail_cases.py             # report
    python tools/test_fail_cases.py --strict    # exit 1 if any case is DEAD
    python tools/test_fail_cases.py --coverage  # also list blocks with no tests
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

SOURCES = Path(__file__).resolve().parent.parent / "_sources"


def all_errors(schema: dict, doc: dict):
    """Every validation error as (path, message)."""
    out = []
    for e in Draft202012Validator(schema).iter_errors(doc):
        where = "/".join(str(p) for p in e.absolute_path) or "(root)"
        out.append((where, e.message))
    return out


def _norm(s: str) -> str:
    return "".join(ch for ch in s.lower() if ch.isalnum())


def mentions_subject(errors, subject: str) -> bool:
    """Does any error actually concern the constraint the filename names?

    Failing is not enough. `affiliation-fail.json` that is rejected because
    @type is a string rather than an array would fail identically with the
    affiliation rule deleted -- it asserts nothing about affiliation. A
    negative case has to fail FOR ITS OWN REASON to be worth anything.
    """
    want = _norm(subject)
    for path, msg in errors:
        # An error on @type is never evidence: every block types @type as an
        # array, so a string there rejects the document whatever else is wrong,
        # and it false-matches whenever the subject is also a type name.
        if path.endswith("@type"):
            continue
        # The PATH is strong evidence -- an error at schema:identifier for
        # identifier-fail.json means that constraint is what fired.
        if want in _norm(path):
            return True
        # The MESSAGE is weak evidence: an anyOf/oneOf failure prints the whole
        # instance, so every token in the document appears in it.
        if msg.lstrip().startswith("{") or "is not valid under any of the given schemas" in msg:
            continue
        if "is not of type 'array'" in msg:
            continue
        if want in _norm(msg):
            return True
    return False


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true", help="exit 1 if any -fail.json validates")
    ap.add_argument("--coverage", action="store_true", help="also list blocks with no tests/")
    args = ap.parse_args()

    cases = sorted(SOURCES.glob("**/tests/*-fail.json"))
    if not cases:
        # Zero cases is not a pass. Say so rather than printing a clean result.
        print("::error::no tests/*-fail.json found at all -- has the layout changed?")
        return 1

    digests = {}
    for c in cases:
        digests.setdefault(hashlib.md5(c.read_bytes()).hexdigest(), []).append(c)

    dead, copied, ok = [], [], 0
    print(f"{'block':<52}{'case':<26}result")
    print("-" * 104)
    for c in cases:
        block = c.parent.parent
        schema_path = block / "resolvedSchema.json"
        label = str(block.relative_to(SOURCES)).replace("\\", "/")
        if not schema_path.exists():
            print(f"{label:<52}{c.name:<26}SKIP  no resolvedSchema.json")
            continue
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        try:
            doc = json.loads(c.read_text(encoding="utf-8"))
        except ValueError as e:
            print(f"{label:<52}{c.name:<26}SKIP  not JSON: {e}")
            continue

        errors = all_errors(schema, doc)
        subject = c.name[:-len("-fail.json")]
        dup = [p for p in digests[hashlib.md5(c.read_bytes()).hexdigest()] if p != c]
        note = f"  [copy of {len(dup)} other block(s)]" if dup else ""
        if dup:
            copied.append(c)
        if not errors:
            dead.append((label, c.name, "validates cleanly"))
            print(f"{label:<52}{c.name:<26}DEAD  validates cleanly{note}")
        elif not mentions_subject(errors, subject):
            first = f"{errors[0][0]}: {errors[0][1][:60]}"
            dead.append((label, c.name, f"fails only on '{first}'"))
            print(f"{label:<52}{c.name:<26}MISDIRECTED  no error mentions "
                  f"'{subject}'; first is {first}{note}")
        else:
            ok += 1
            hit = next(f"{p}: {m[:60]}" for p, m in errors
                       if _norm(subject) in _norm(p) or _norm(subject) in _norm(m))
            print(f"{label:<52}{c.name:<26}ok    {hit}{note}")

    print()
    print(f"{ok} of {len(cases)} negative cases fail for the reason they name; "
          f"{len(dead)} do not; {len(copied)} are byte-identical copies of a case in "
          f"another block.")

    if args.coverage:
        blocks = {p.parent for p in SOURCES.glob("**/schema.yaml")}
        untested = sorted(b for b in blocks if not (b / "tests").is_dir())
        print(f"\n{len(untested)} of {len(blocks)} blocks have no tests/ directory:")
        for b in untested[:20]:
            print(f"    {str(b.relative_to(SOURCES)).replace(chr(92), '/')}")
        if len(untested) > 20:
            print(f"    ... and {len(untested) - 20} more")

    if dead:
        print()
        print(f"::error::{len(dead)} negative test case(s) assert nothing about the "
              f"constraint they name.")
        for label, name, why in dead:
            print(f"    {label}/tests/{name}: {why}")
    return 1 if (dead and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
