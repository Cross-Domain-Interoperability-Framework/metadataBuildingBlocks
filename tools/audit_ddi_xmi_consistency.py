#!/usr/bin/env python3
"""Audit _sources/ddiProperties building blocks against an Enterprise Architect
XMI 1.1 export of the DDI-CDI UML model.

Parses the EA-native XMI (UML:Class / UML:Attribute / UML:Association /
UML:Generalization), then for every ddiProperties BB:
  - discovers which DDI-CDI classes the BB claims to model (the `cdi:X` values
    that appear as `@type` `const`s, plus the BB-name fallback);
  - gathers the XMI-expected member set for each class (own attributes + own
    navigable association roles + everything inherited through generalization);
  - compares against the property keys actually present in the BB schema.yaml;
  - reports XMI-only (missing from BB), BB-only (extra / renamed), and
    multiplicity/type notes.

Name matching is best-effort: `cdi:` / `cdif:` prefixes are stripped, the
generator's `has_<Target>` / `<role>_<Target>` association-key convention is
folded, and comparison is case-insensitive. Treat the output as a review aid,
not a hard pass/fail.

Usage:
  python tools/audit_ddi_xmi_consistency.py --xmi <path-to-ea-xmi> [--bb NAME] [--verbose]
"""
import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DDI_DIR = REPO / "_sources" / "ddiProperties"

UML = "omg.org/UML1.3"


def _tag(elem):
    return elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag


def _tagged_values(elem):
    """Collect UML:TaggedValue tag->value pairs that are direct children of the
    element's UML:ModelElement.taggedValue block."""
    out = {}
    for child in elem:
        if _tag(child) == "ModelElement.taggedValue":
            for tv in child:
                if _tag(tv) == "TaggedValue":
                    out[tv.get("tag")] = tv.get("value")
    return out


def parse_xmi(xmi_path):
    """Return (classes, id2name).

    classes: name -> {
        'id', 'stereotype', 'package', 'doc',
        'attrs': [ {name,type,lower,upper,ordered} ],
        'parents': [name,...],
        'roles': [ {role, target, mult, navigable, aggregation, src} ],
    }
    """
    tree = ET.parse(xmi_path)
    root = tree.getroot()

    id2name = {}
    classes = {}
    class_elems = {}  # id -> element

    # ---- pass 1: classes + attributes -------------------------------------
    for elem in root.iter():
        if _tag(elem) != "Class":
            continue
        cid = elem.get("xmi.id")
        name = elem.get("name")
        if not cid or not name:
            continue
        id2name[cid] = name
        tv = _tagged_values(elem)
        attrs = []
        for feat in elem:
            if _tag(feat) != "Classifier.feature":
                continue
            for a in feat:
                if _tag(a) != "Attribute":
                    continue
                atv = _tagged_values(a)
                attrs.append({
                    "name": a.get("name"),
                    "type": atv.get("type", ""),
                    "lower": atv.get("lowerBound", ""),
                    "upper": atv.get("upperBound", ""),
                    "ordered": atv.get("ordered", "0") == "1",
                })
        rec = {
            "id": cid,
            "stereotype": tv.get("ea_stype", ""),
            "package": tv.get("package_name", ""),
            "doc": (tv.get("documentation", "") or "").split("\n")[0][:120],
            "attrs": attrs,
            "parents": [],
            "roles": [],
        }
        # a name can be reused (e.g. RDF mirror package); keep the first
        # non-Deleted, prefer Class stereotype over DataType only on collision
        if name not in classes:
            classes[name] = rec
            class_elems[cid] = elem
        else:
            # collision: prefer the one that actually has attributes/feature
            if attrs and not classes[name]["attrs"]:
                classes[name] = rec
                class_elems[cid] = elem

    # ---- pass 2: generalizations ------------------------------------------
    for elem in root.iter():
        if _tag(elem) != "Generalization":
            continue
        sub = elem.get("subtype")
        sup = elem.get("supertype")
        sub_name = id2name.get(sub)
        sup_name = id2name.get(sup)
        if sub_name and sup_name and sub_name in classes:
            classes[sub_name]["parents"].append(sup_name)

    # ---- pass 3: associations ---------------------------------------------
    for elem in root.iter():
        if _tag(elem) != "Association":
            continue
        tv = _tagged_values(elem)
        if tv.get("ea_type") not in (None, "Association", "Aggregation"):
            # skip trace/dependency/abstraction connectors
            continue
        role = elem.get("name") or tv.get("mt") or ""
        s_name = tv.get("ea_sourceName")
        t_name = tv.get("ea_targetName")
        lb = tv.get("lb", "")  # source-side multiplicity
        rb = tv.get("rb", "")  # target-side multiplicity
        ends = []
        for conn in elem:
            if _tag(conn) != "Association.connection":
                continue
            for ae in conn:
                if _tag(ae) != "AssociationEnd":
                    continue
                aetv = _tagged_values(ae)
                ends.append({
                    "type": ae.get("type"),
                    "mult": ae.get("multiplicity", ""),
                    "navigable": ae.get("isNavigable") == "true",
                    "aggregation": ae.get("aggregation", "none"),
                    "end": aetv.get("ea_end", ""),
                })
        if len(ends) != 2:
            continue
        src = next((e for e in ends if e["end"] == "source"), ends[0])
        tgt = next((e for e in ends if e["end"] == "target"), ends[1])
        # navigable source->target : the SOURCE class gets a role pointing at target
        if tgt["navigable"] and s_name in classes:
            classes[s_name]["roles"].append({
                "role": role,
                "target": t_name or id2name.get(tgt["type"], "?"),
                "mult": tgt["mult"] or rb,
                "aggregation": tgt["aggregation"],
                "src": s_name,
            })
        if src["navigable"] and t_name in classes:
            classes[t_name]["roles"].append({
                "role": role,
                "target": s_name or id2name.get(src["type"], "?"),
                "mult": src["mult"] or lb,
                "aggregation": src["aggregation"],
                "src": t_name,
            })

    # dedupe roles per class (EA can emit an association more than once)
    for c in classes.values():
        seen = set()
        uniq = []
        for r in c["roles"]:
            k = (r["role"], r["target"])
            if k in seen:
                continue
            seen.add(k)
            uniq.append(r)
        c["roles"] = uniq

    return classes, id2name


def inherited_members(cls_name, classes, _seen=None):
    """Return (attrs, roles) accumulated through the generalization chain."""
    if _seen is None:
        _seen = set()
    if cls_name in _seen or cls_name not in classes:
        return [], []
    _seen.add(cls_name)
    c = classes[cls_name]
    attrs = list(c["attrs"])
    roles = list(c["roles"])
    for p in c["parents"]:
        pa, pr = inherited_members(p, classes, _seen)
        attrs += pa
        roles += pr
    return attrs, roles


# ---- BB side --------------------------------------------------------------
def bb_claimed_classes(schema_text, bb_name):
    """Class names a BB models: every `const: 'cdi:X'` (or cdif:) found, plus a
    fallback derived from the BB directory name."""
    names = set()
    for m in re.finditer(r"""const:\s*['"]?(?:cdi|cdif):([A-Za-z0-9_]+)['"]?""", schema_text):
        names.add(m.group(1))
    if not names and bb_name.startswith("ddicdi"):
        names.add(bb_name[len("ddicdi"):])
    return names


def bb_property_keys(schema_text):
    """All `cdi:` / `cdif:` property keys that appear as YAML mapping keys."""
    keys = set()
    for m in re.finditer(r"""^\s*['"]?((?:cdi|cdif):[A-Za-z0-9_]+)['"]?\s*:""", schema_text, re.M):
        keys.add(m.group(1))
    return keys


def norm(name):
    """Normalize a member name for fuzzy matching."""
    n = name.split(":")[-1]
    n = re.sub(r"^(has|isComposedOf|uses|in|for)_", "", n)  # generator prefixes
    return n.lower().replace("_", "")


def xmi_member_names(cls_name, classes):
    attrs, roles = inherited_members(cls_name, classes)
    out = {}  # norm -> display
    for a in attrs:
        out[norm(a["name"])] = ("attr", a)
    for r in roles:
        # association keys in BBs are often role or has_<Target>
        key = r["role"] or ("has_" + r["target"])
        out[norm(key)] = ("role", r)
        out.setdefault(norm("has_" + r["target"]), ("role", r))
        out.setdefault(norm(r["target"]), ("role", r))
    return attrs, roles, out


def dump_classes(classes, names):
    """Print a full member listing for the named classes (own + inherited)."""
    for name in names:
        if name not in classes:
            print(f"## {name}  !! NOT FOUND in XMI")
            # offer near matches
            near = [c for c in classes if name.lower() in c.lower() or c.lower() in name.lower()]
            if near:
                print(f"   near: {', '.join(sorted(near))}")
            print()
            continue
        c = classes[name]
        print(f"## {name}   (package={c['package']}, stereotype={c['stereotype']})")
        if c["parents"]:
            print(f"   parents: {', '.join(c['parents'])}")
        if c["doc"]:
            print(f"   doc: {c['doc']}")
        attrs, roles = inherited_members(name, classes)
        own_attr = {a["name"] for a in c["attrs"]}
        own_role = {(r["role"], r["target"]) for r in c["roles"]}
        for a in attrs:
            tag = "" if a["name"] in own_attr else "  (inherited)"
            print(f"   - attr  {a['name']} : {a['type']} [{a['lower']}..{a['upper']}]"
                  f"{' {ordered}' if a['ordered'] else ''}{tag}")
        for r in roles:
            tag = "" if (r["role"], r["target"]) in own_role else "  (inherited)"
            agg = f" «{r['aggregation']}»" if r["aggregation"] not in ("none", "") else ""
            print(f"   - role  {r['role']} -> {r['target']} [{r['mult']}]{agg}{tag}")
        print()


def audit():
    ap = argparse.ArgumentParser()
    ap.add_argument("--xmi", required=True)
    ap.add_argument("--bb", help="audit only this BB (dir name)")
    ap.add_argument("--dump-class", help="comma-separated class names to dump (skips the BB audit)")
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()

    classes, id2name = parse_xmi(args.xmi)
    print(f"Parsed XMI: {len(classes)} uniquely-named classes/datatypes\n")

    if args.dump_class:
        dump_classes(classes, [n.strip() for n in args.dump_class.split(",")])
        return

    bbs = sorted(p for p in DDI_DIR.iterdir() if p.is_dir())
    if args.bb:
        bbs = [p for p in bbs if p.name == args.bb]

    total_missing = total_extra = total_unknown = 0

    for bb in bbs:
        schema = bb / "schema.yaml"
        if not schema.exists():
            print(f"## {bb.name}\n  !! no schema.yaml\n")
            continue
        text = schema.read_text(encoding="utf-8")
        claimed = bb_claimed_classes(text, bb.name)
        prop_keys = bb_property_keys(text)
        bb_norm = {norm(k): k for k in prop_keys}

        print(f"## {bb.name}")
        print(f"   models: {', '.join(sorted(claimed)) or '(none detected)'}")

        unknown = [c for c in sorted(claimed) if c not in classes]
        if unknown:
            total_unknown += len(unknown)
            print(f"   !! NOT FOUND in XMI: {', '.join(unknown)}")

        # union of expected members across all claimed (known) classes
        expected = {}  # norm -> (kind, obj, owner_class)
        for c in sorted(claimed):
            if c not in classes:
                continue
            attrs, roles, members = xmi_member_names(c, classes)
            for nm, (kind, obj) in members.items():
                expected.setdefault(nm, (kind, obj, c))

        # known intentional CDIF omissions — not real discrepancies
        INTENTIONAL = {"catalogdetails"}
        missing_attr, missing_role = [], []
        for nm, (kind, obj, owner) in sorted(expected.items()):
            if nm in bb_norm or nm in INTENTIONAL:
                continue
            if kind == "attr":
                missing_attr.append(
                    f"      - {obj['name']} : {obj['type']} [{obj['lower']}..{obj['upper']}]  (from {owner})")
            else:
                missing_role.append(
                    f"      - {obj['role']} -> {obj['target']} [{obj['mult']}]  (from {owner})")
        if missing_attr:
            total_missing += len(missing_attr)
            print(f"   MISSING attributes ({len(missing_attr)}):")
            print("\n".join(missing_attr))
        if missing_role:
            total_missing += len(missing_role)
            print(f"   MISSING association roles ({len(missing_role)}):")
            print("\n".join(missing_role))

        # BB-only keys (extra / renamed / CDIF additions)
        extra = []
        for nm, key in sorted(bb_norm.items()):
            if nm in expected:
                continue
            extra.append(f"      - {key}")
        if extra:
            total_extra += len(extra)
            print(f"   BB-only keys ({len(extra)}) — renamed, CDIF-added, or structural:")
            print("\n".join(extra))

        if args.verbose and not missing and not extra and not unknown:
            print("   OK — members align")
        print()

    print("=" * 70)
    print(f"Totals: {total_missing} XMI members missing from BBs, "
          f"{total_extra} BB-only keys, {total_unknown} classes not found in XMI")


if __name__ == "__main__":
    audit()
