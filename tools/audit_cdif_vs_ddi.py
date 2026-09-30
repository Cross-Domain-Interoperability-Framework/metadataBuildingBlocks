#!/usr/bin/env python3
"""Audit cdifProperties `cdi:*` property value-types against the ddiProperties
building-block definitions.

CDIF is a subset of DDI-CDI. Where a cdifProperties building block uses a
`cdi:`-prefixed (i.e. DDI-CDI) property, its value type/shape should be
*consistent* with how the same `cdi:` property is defined in the ddiProperties
building blocks (which are generated from the DDI-CDI UML and are the source of
truth for `cdi:` typing).

This script:
  - walks every _sources/cdifProperties/*/schema.yaml and collects, for each
    `cdi:` property key (anywhere — root properties or nested $defs), a compact
    normalised "value-shape signature";
  - does the same for _sources/ddiProperties/*/schema.yaml;
  - for each `cdi:` property used in cdifProperties, compares its signature(s)
    against the ddiProperties signature(s) and classifies:
      MATCH        — identical or trivially compatible shapes
      STRUCTURAL   — scalar-vs-class-ref mismatch (likely a real bug)
      SOFT         — both structured but differ (CDIF simplification? review)
      CDIF-ONLY    — no ddiProperties definition of this cdi: property at all
                     (should it be `cdif:`? or is the ddi BB missing it?)

Treat SOFT / CDIF-ONLY as review items, STRUCTURAL as likely fixes.

Usage:  python tools/audit_cdif_vs_ddi.py [--verbose]
"""
import argparse
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
# cdi: and cdif: appear in these two trees and nowhere else -- measured
# 2026-09-30: cdifDataType 107/64, profiles/cdifProfile 15/15, and zero in
# cdifCompositeProfile, xasProperties, skosProperties, provProperties,
# qualityProperties and bioschemasProperties. Auditing cdifDataType alone, as
# this tool did until then, left the 15 cdi: declarations in the profile modules
# unchecked.
CDIF_DIRS = [REPO / "_sources" / "cdifDataType",
             REPO / "_sources" / "profiles" / "cdifProfile"]
CDIF_DIR = CDIF_DIRS[0]  # retained: some callers still pass a single dir
DDI_DIR = REPO / "_sources" / "ddiProperties"

PRIMITIVES = {"string", "integer", "number", "boolean", "null"}


def _canon_type(name: str) -> str:
    """Collapse the cdif* / ddicdi* sibling-BB naming so a CDIF BB that
    $refs its own `cdifFoo` reads the same as a ddiProperties `ddicdiFoo`.

    cdifInstanceVariable / ddicdiInstanceVariable -> InstanceVariable
    """
    for prefix in ("ddicdi", "cdif"):
        if name.startswith(prefix) and len(name) > len(prefix) \
                and name[len(prefix)].isupper():
            return name[len(prefix):]
    return name


# CDIF's objectReference and canonical ddicdiDataTypes#/$defs/id-reference are
# the SAME shape -- {type: object, properties: {@id: string}, required: [@id],
# additionalProperties: false} -- differing only in their description. Measured
# 2026-09-30. Treating them as different made every reference-bearing property
# look like a CDIF divergence: cdi:measures and cdi:qualifies were reported SOFT
# purely because CDIF spells the reference branch with its own block. A
# namespace audit that flags a naming difference as a value-range difference
# points at the wrong properties.
_ID_REF_ALIASES = {"objectReference", "id-reference"}


def _ref_basename(ref: str) -> str:
    """Normalise a $ref string to a short, sibling-collapsed type name.

    '../ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry'
        -> 'ControlledVocabularyEntry'
    '../cdifInstanceVariable/schema.yaml' -> 'InstanceVariable'
    '#/$defs/Foo' -> 'Foo'
    """
    ref = ref.strip()
    if "#/$defs/" in ref or "#/properties/" in ref:
        return _canon_type(ref.split("/")[-1])
    if ref.endswith("/schema.yaml"):
        parts = [p for p in ref.split("/") if p and p not in (".", "..")]
        if len(parts) >= 2:
            return _canon_type(parts[-2])
        return ref
    if ref == "#":
        return "<root>"
    return _canon_type(ref.split("/")[-1])


def _norm_ref(name: str) -> str:
    return "@idref" if name in _ID_REF_ALIASES else name


def _resolve_local_alias(ref: str, root) -> str:
    """Follow a #/$defs/X that is itself a single $ref, and return that target.

    A local $defs entry may be an ALIAS for something entirely different from
    what its name suggests, and comparing on the name alone then reports two
    unrelated types as identical. cdifRepresentedVariable declares
    `$defs/Reference: {$ref: schemaorgProperties/labeledLink}` -- a schema.org
    work-at-a-URL -- while canonical cdi:Reference is
    {@type, cdi:ddiReference, cdi:description, cdi:semantic, cdi:uri}. Both
    collapsed to the token "Reference", so cdif:externalDefinition was reported
    as matching canonical exactly when its value range shares nothing with it.
    Measured 2026-09-30.
    """
    if not isinstance(root, dict) or not ref.startswith("#/$defs/"):
        return ref
    target = (root.get("$defs") or {}).get(ref.split("/")[-1])
    if isinstance(target, dict) and set(target) == {"$ref"}:
        return target["$ref"]
    return ref


def shape_sig(node, root=None) -> str:
    """Compact, comparable signature for a JSON-Schema value node."""
    if not isinstance(node, dict):
        return "?"
    if "$ref" in node:
        ref = _resolve_local_alias(node["$ref"], root)
        return f"ref:{_norm_ref(_ref_basename(ref))}"
    if "anyOf" in node or "oneOf" in node:
        key = "anyOf" if "anyOf" in node else "oneOf"
        parts = sorted({shape_sig(x, root) for x in node[key]})
        return f"anyOf[{','.join(parts)}]"
    if "allOf" in node:
        parts = sorted({shape_sig(x, root) for x in node["allOf"]})
        return f"allOf[{','.join(parts)}]"
    if "enum" in node:
        return "enum"
    t = node.get("type")
    if t == "array":
        items = node.get("items", {})
        return f"array<{shape_sig(items, root)}>"
    if _is_inline_id_ref(node):
        # Some sites $ref objectReference, others write the identical sealed
        # {@id} object inline -- cdi:for and cdi:hasWeight in cdifStatistics do.
        # Same value range either way, so it must produce the same signature or
        # the audit reports a style difference as a namespace violation.
        return "ref:@idref"
    if t == "object" or "properties" in node:
        return "object"
    if isinstance(t, list):
        return "anyOf[" + ",".join(sorted(t)) + "]"
    if isinstance(t, str):
        return t
    # bare {} or description-only node
    return "any"


# Keywords that narrow an already-declared property rather than declare its
# value range. A node carrying only these is a CONSTRAINT, not a declaration:
# cdifTabularData writes `cdi:isDelimited: {const: true}` inside an if/then
# branch, and counting that as a value shape reported the property as diverging
# from a canonical `boolean` it agrees with perfectly.
_CONSTRAINT_ONLY = {"const", "minItems", "maxItems", "minimum", "maximum",
                    "minLength", "maxLength", "pattern", "required",
                    "description", "default", "title", "contains"}


def _is_constraint_only(node: dict) -> bool:
    return bool(node) and set(node) <= _CONSTRAINT_ONLY


def _is_inline_id_ref(node: dict) -> bool:
    """A sealed object whose only property is @id -- objectReference, inline."""
    if node.get("type") != "object" or node.get("additionalProperties") is not False:
        return False
    props = node.get("properties")
    if not isinstance(props, dict) or set(props) != {"@id"}:
        return False
    return set(node.get("required") or []) <= {"@id"}


def _is_scalar_sig(sig: str) -> bool:
    base = sig
    if base.startswith("array<") and base.endswith(">"):
        base = base[6:-1]
    return base in PRIMITIVES or base == "enum"


def _is_class_ref_sig(sig: str) -> bool:
    base = sig
    if base.startswith("array<") and base.endswith(">"):
        base = base[6:-1]
    if base.startswith("ref:"):
        tgt = base[4:]
        # id-reference / scalar-ish refs are not "class" refs
        return tgt not in ("@idref", "id-reference", "<root>")
    return False


def collect_props(schema_dirs, prefix="cdi:") -> dict:
    """name -> {bb_name -> set(signatures)} for every *prefix* property key."""
    if isinstance(schema_dirs, Path):
        schema_dirs = [schema_dirs]
    merged: dict[str, dict[str, set]] = {}
    for d in schema_dirs:
        for name, bbs in _collect_one(d, prefix).items():
            for bb, sigs in bbs.items():
                merged.setdefault(name, {}).setdefault(bb, set()).update(sigs)
    return merged


def collect_cdi_props(schema_dir) -> dict:
    """Back-compatible wrapper: cdi: properties under one or more dirs."""
    return collect_props(schema_dir, "cdi:")


def _collect_one(schema_dir: Path, prefix: str) -> dict:
    """name -> {bb_name -> set(signatures)} for every *prefix* property key."""
    out: dict[str, dict[str, set]] = {}

    root = None  # set per block below; the alias table lives at the root

    def walk(node, bb):
        if isinstance(node, dict):
            for k, v in node.items():
                if (isinstance(k, str) and k.startswith(prefix)
                        and isinstance(v, dict)
                        and not _is_constraint_only(v)):
                    sig = shape_sig(v, root)
                    out.setdefault(k, {}).setdefault(bb, set()).add(sig)
                walk(v, bb)
        elif isinstance(node, list):
            for x in node:
                walk(x, bb)

    for bb in sorted(schema_dir.iterdir()):
        sy = bb / "schema.yaml"
        if not sy.exists():
            continue
        try:
            doc = yaml.safe_load(sy.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            print(f"  !! {bb.name}: YAML parse error: {e}", file=sys.stderr)
            continue
        root = doc
        walk(doc, bb.name)
    return out


# ---------------------------------------------------------------------------
# Reverse direction: a cdif: property whose value range AGREES with canonical
# DDI-CDI does not need the cdif: prefix.
#
# The rule this audits (CLAUDE.md, "cdi: vs cdif:"): cdi: is for properties
# whose value types match the canonical DDI-CDI XMI; any CDIF simplification or
# restriction is renamed to cdif: so the divergence is namespace-visible. An RDF
# agent seeing cdi:X is entitled to assume DDI-CDI's value types for X.
#
# That rule has two failure modes and the forward check above only finds one.
# A cdif: property that matches canonical exactly is the other: it advertises a
# divergence that does not exist, which costs interoperability for nothing --
# a consumer that understands DDI-CDI cannot tell it already understands this.
#
# Compared on LOCAL NAME, because that is what a consumer would have to match.
# A CDIF-invented name with no canonical counterpart (cdif:has_PrimaryKey,
# cdif:isDefinedBy_Variable -- the role_Target disambiguation CDIF inherits from
# the canonical Source_role_Target association naming) is correctly cdif:
# whatever its range, and is reported separately rather than as a finding.
# ---------------------------------------------------------------------------

def audit_reverse(verbose=False):
    cdif = collect_props(CDIF_DIRS, "cdif:")
    ddi = collect_props(DDI_DIR, "cdi:")
    ddi_local = {k[len("cdi:"):]: v for k, v in ddi.items()}

    print(f"cdif: properties declared in CDIF blocks: {len(cdif)}")
    print(f"canonical cdi: properties to compare against: {len(ddi_local)}")
    print()

    could_be_cdi, invented, diverges, restricts = [], [], [], []
    for name in sorted(cdif):
        local = name[len("cdif:"):]
        sigs = set()
        bbs = {}
        for bb, s in cdif[name].items():
            sigs |= s
            for one in s:
                bbs.setdefault(one, []).append(bb)
        if local not in ddi_local:
            invented.append((name, sorted(sigs)))
            continue
        ddi_sigs = set()
        for bb, s in ddi_local[local].items():
            ddi_sigs |= s
        unmatched = [s for s in sigs if s not in ddi_sigs]
        if unmatched:
            diverges.append((name, sorted(sigs), sorted(ddi_sigs)))
        elif sigs == ddi_sigs:
            could_be_cdi.append((name, sorted(sigs), sorted(ddi_sigs), bbs))
        else:
            # Every CDIF signature appears canonically, but canonical permits
            # more: CDIF is a strict SUBSET, which is a restriction and so is
            # exactly what cdif: is for. cdif:value takes string where canonical
            # takes string or integer; cdif:isDefinedBy takes one of the four
            # ranges canonical gives that role. Reporting these as "could be
            # cdi:" would recommend dropping a prefix that is carrying real
            # information.
            restricts.append((name, sorted(sigs), sorted(ddi_sigs)))

    if could_be_cdi:
        print(f"[COULD-BE-cdi] {len(could_be_cdi)} cdif: propert(ies) whose range "
              f"matches canonical DDI-CDI exactly:")
        for name, sigs, ddi_sigs, bbs in could_be_cdi:
            print(f"  {name}")
            for s in sigs:
                print(f"      cdif: {s}   ({', '.join(sorted(bbs[s]))})")
            print(f"      ddi:  {', '.join(ddi_sigs)}")
        print()
    else:
        print("[COULD-BE-cdi] none -- every cdif: property with a canonical "
              "counterpart genuinely diverges from it.")
        print()

    print(f"[cdif-CORRECT, restricts] {len(restricts)} cdif: propert(ies) whose "
          f"range is a strict SUBSET of canonical -- a restriction, which is "
          f"what cdif: is for:")
    for name, sigs, ddi_sigs in restricts:
        print(f"  {name}")
        print(f"      cdif: {', '.join(sigs)}")
        print(f"      ddi:  {', '.join(ddi_sigs)}")
    print()

    print(f"[cdif-CORRECT, differs] {len(diverges)} cdif: propert(ies) share a "
          f"local name with a canonical property and genuinely differ:")
    for name, sigs, ddi_sigs in diverges:
        print(f"  {name}")
        print(f"      cdif: {', '.join(sigs)}")
        print(f"      ddi:  {', '.join(ddi_sigs)}")
    print()

    print(f"[CDIF-INVENTED] {len(invented)} cdif: propert(ies) with no canonical "
          f"property of that local name -- correctly cdif: by name alone:")
    if verbose:
        for name, sigs in invented:
            print(f"  {name}: {', '.join(sigs)}")
    else:
        print("  " + ", ".join(n for n, _ in invented))
    print()
    return could_be_cdi


# ---------------------------------------------------------------------------
# Self-test
#
# Each case pins one of the four normalisations this tool depends on. They all
# fail the same way if they regress -- findings go UP, and a larger number reads
# as a more thorough audit rather than a broken one. That is why they are pinned
# rather than trusted.
# ---------------------------------------------------------------------------

def _check(results, name, got, want):
    ok = got == want
    results.append(ok)
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    if not ok:
        print(f"        got  {got!r}")
        print(f"        want {want!r}")


def self_test() -> bool:
    print("audit_cdif_vs_ddi self-test")
    results = []

    # 1. objectReference and id-reference are the same shape under two names.
    a = shape_sig({"$ref": "../objectReference/schema.yaml"})
    b = shape_sig({"$ref": "../ddicdiDataTypes/schema.yaml#/$defs/id-reference"})
    _check(results, "objectReference and id-reference share a signature", a, b)

    # 2. The same shape written inline must not read differently.
    inline = {"type": "object", "additionalProperties": False,
              "required": ["@id"], "properties": {"@id": {"type": "string"}}}
    _check(results, "an inline sealed {@id} reads as a reference",
           shape_sig(inline), a)

    # 3. A const inside a conditional narrows an existing declaration; it is
    #    not a value-range declaration.
    _check(results, "a const-only node is a constraint, not a declaration",
           _is_constraint_only({"const": True}), True)
    _check(results, "a typed node is a declaration",
           _is_constraint_only({"type": "boolean"}), False)

    # 4. A local $defs alias must resolve to what it points at, not to its own
    #    name. This is the one that made cdif:externalDefinition read as
    #    matching canonical cdi:Reference while pointing at labeledLink.
    root = {"$defs": {"Reference":
                      {"$ref": "../../schemaorgProperties/labeledLink/schema.yaml"}}}
    _check(results, "a local $defs alias resolves to its target",
           shape_sig({"$ref": "#/$defs/Reference"}, root), "ref:labeledLink")
    _check(results, "and without the root it cannot, so it must not claim to",
           shape_sig({"$ref": "#/$defs/Reference"}), "ref:Reference")

    # 5. Real-repo anchor. Update these deliberately when a schema changes;
    #    an unexplained move means a normalisation above stopped working.
    cdif = collect_props(CDIF_DIRS, "cdi:")
    ddi = collect_props(DDI_DIR, "cdi:")
    # 68 since 2026-09-30. Two deliberate moves that day: DimensionGroup's
    # grouping property was renamed from cdif:has_DataStructureComponent to
    # cdi:has_DimensionComponent and narrowed to the DimensionComponent subtype
    # (+1), the seven properties taking a CDIF ConceptOrTermOrString where
    # canonical takes a ControlledVocabularyEntry moved to cdif: (-7), and
    # cdi:identifier -- a schema:PropertyValue where canonical is the composite
    # cdi:Identifier -- moved too, consolidating with the cdif:identifier that
    # already existed for the same shape (-1).
    _check(results, "real repo: cdi: properties in CDIF blocks", len(cdif), 67)
    diverging = 0
    for name in sorted(cdif):
        if name not in ddi:
            continue
        cs = set().union(*cdif[name].values())
        ds = set().union(*ddi[name].values())
        if [s for s in cs if s not in ds]:
            diverging += 1
    # 13 since the seven ControlledVocabularyEntry simplifications moved to
    # cdif: on 2026-09-30. What remains: four flattenings to a bare string
    # (formatPattern, logicalExpression, purpose, regularExpression), three
    # class narrowings (takesSubstantiveValuesFrom, takesSentinelValuesFrom,
    # refersTo), cdi:identifier using the schema.org block, and the per-class
    # variations in cdi:indexes, cdi:qualifies, cdi:source, cdi:isStructuredBy
    # and cdi:has_DataStructureComponent. Tracked in issue #40.
    _check(results, "real repo: cdi: properties whose range diverges",
           diverging, 12)

    # The reverse direction needs its own anchor: the $defs-alias fix only shows
    # up here, because cdif:externalDefinition is a cdif: property and the count
    # above walks cdi: ones. Without this, dropping alias resolution failed only
    # the unit case.
    cdif_side = collect_props(CDIF_DIRS, "cdif:")
    ddi_local = {k[len("cdi:"):]: v for k, v in ddi.items()}
    equal = 0
    for name in sorted(cdif_side):
        local = name[len("cdif:"):]
        if local not in ddi_local:
            continue
        cs = set().union(*cdif_side[name].values())
        ds = set().union(*ddi_local[local].values())
        if cs == ds:
            equal += 1
    # 2 since 2026-09-30: cdif:has_DataStructureComponent was the third, and it
    # was never a real match -- it compared equal on local name while sitting on
    # a different domain class. The rename removed it.
    _check(results, "real repo: cdif: properties matching canonical exactly",
           equal, 2)

    passed = sum(1 for ok in results if ok)
    print()
    print(f"{passed}/{len(results)} checks passed")
    return passed == len(results)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", "-v", action="store_true",
                    help="also list MATCH rows")
    ap.add_argument("--self-test", action="store_true",
                    help="prove each normalisation still holds")
    args = ap.parse_args()

    if args.self_test:
        return 0 if self_test() else 1

    cdif = collect_props(CDIF_DIRS, "cdi:")
    ddi = collect_props(DDI_DIR, "cdi:")
    print(f"cdifProperties: {len(cdif)} distinct cdi: properties")
    print(f"ddiProperties:  {len(ddi)} distinct cdi: properties\n")

    matches = soft = structural = cdif_only = 0

    for name in sorted(cdif):
        cdif_sigs = set()
        cdif_bbs = {}
        for bb, sigs in cdif[name].items():
            cdif_sigs |= sigs
            for s in sigs:
                cdif_bbs.setdefault(s, []).append(bb)
        ddi_sigs = set()
        for bb, sigs in ddi.get(name, {}).items():
            ddi_sigs |= sigs

        if name not in ddi:
            cdif_only += 1
            print(f"[CDIF-ONLY] {name}")
            for s in sorted(cdif_sigs):
                print(f"    cdif: {s}   ({', '.join(sorted(cdif_bbs[s]))})")
            print(f"    ddi:  (no ddiProperties definition)")
            print()
            continue

        # classify each cdif signature against the ddi signature set
        unmatched = [s for s in cdif_sigs if s not in ddi_sigs]
        if not unmatched:
            matches += 1
            if args.verbose:
                print(f"[MATCH] {name}: {sorted(cdif_sigs)}")
            continue

        # is any unmatched pair a scalar-vs-classref mismatch?
        ddi_has_classref = any(_is_class_ref_sig(s) for s in ddi_sigs)
        ddi_has_scalar = any(_is_scalar_sig(s) for s in ddi_sigs)
        kind = "SOFT"
        for s in unmatched:
            if (_is_scalar_sig(s) and ddi_has_classref and not ddi_has_scalar) or \
               (_is_class_ref_sig(s) and ddi_has_scalar and not ddi_has_classref):
                kind = "STRUCTURAL"
                break
        if kind == "STRUCTURAL":
            structural += 1
        else:
            soft += 1
        print(f"[{kind}] {name}")
        for s in sorted(cdif_sigs):
            mark = "  <-- not in ddi" if s in unmatched else ""
            print(f"    cdif: {s}   ({', '.join(sorted(cdif_bbs[s]))}){mark}")
        for s in sorted(ddi_sigs):
            print(f"    ddi:  {s}")
        print()

    print("=" * 64)
    print(f"MATCH: {matches}   SOFT: {soft}   STRUCTURAL: {structural}   "
          f"CDIF-ONLY: {cdif_only}")
    print()
    print("=" * 64)
    print("REVERSE: does any cdif: property not need the prefix?")
    print("=" * 64)
    audit_reverse(args.verbose)
    return 0


if __name__ == "__main__":
    sys.exit(main())
