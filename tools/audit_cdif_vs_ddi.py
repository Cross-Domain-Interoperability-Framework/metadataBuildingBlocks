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
CDIF_DIR = REPO / "_sources" / "cdifProperties"
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


def shape_sig(node) -> str:
    """Compact, comparable signature for a JSON-Schema value node."""
    if not isinstance(node, dict):
        return "?"
    if "$ref" in node:
        return f"ref:{_ref_basename(node['$ref'])}"
    if "anyOf" in node or "oneOf" in node:
        key = "anyOf" if "anyOf" in node else "oneOf"
        parts = sorted({shape_sig(x) for x in node[key]})
        return f"anyOf[{','.join(parts)}]"
    if "allOf" in node:
        parts = sorted({shape_sig(x) for x in node["allOf"]})
        return f"allOf[{','.join(parts)}]"
    if "enum" in node:
        return "enum"
    t = node.get("type")
    if t == "array":
        items = node.get("items", {})
        return f"array<{shape_sig(items)}>"
    if t == "object" or "properties" in node:
        return "object"
    if isinstance(t, list):
        return "anyOf[" + ",".join(sorted(t)) + "]"
    if isinstance(t, str):
        return t
    # bare {} or description-only node
    return "any"


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
        return tgt not in ("id-reference", "<root>")
    return False


def collect_cdi_props(schema_dir: Path) -> dict:
    """name -> {bb_name -> set(signatures)} for every cdi: property key."""
    out: dict[str, dict[str, set]] = {}

    def walk(node, bb):
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(k, str) and k.startswith("cdi:") and isinstance(v, dict):
                    sig = shape_sig(v)
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
        walk(doc, bb.name)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", "-v", action="store_true",
                    help="also list MATCH rows")
    args = ap.parse_args()

    cdif = collect_cdi_props(CDIF_DIR)
    ddi = collect_cdi_props(DDI_DIR)
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
