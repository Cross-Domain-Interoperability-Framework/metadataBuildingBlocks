#!/usr/bin/env python3
"""
Generate a CDIF building-block schema.yaml from a canonical UML 2.5 / XMI 2.5.1
export of a DDI-CDI / UCMIS-style class model.

Inputs:
  --xmi PATH                    canonical XMI file (UML 2.5.1 / XMI 2.5.1)
  --class A[,B,...]             one or more classes to use as BB roots
  --bb-name DDICDIThing         building block directory name
  --out-dir DIR                 parent directory for the new BB folder

Conventions encoded (see tools/uml_to_schema.md for details):
  - JSON-LD root: anyOf [single node, array of nodes, {@context, @graph}].
  - @type required, validated via array `contains` const "cdi:<ClassName>".
  - @id is always optional on every node.
  - UML attributes typed by uml:DataType (UCMIS dt-*) expand inline as $defs,
    OR are emitted as $ref to a sibling shared-types BB if the type name is
    found there (default: ../ddicdiDataTypes/schema.yaml).
  - UML attributes typed by uml:Class become {$ref: "#/$defs/id-reference"},
    unless the target class is one of --inline=ClassA,ClassB or the user
    explicitly passes --reference for a class that would otherwise be inlined.
  - UML attributes typed by uml:Enumeration emit `enum: [literal, ...]`.
  - Multiplicity:
      lower>=1, upper==1 → required + single value.
      lower==0, upper==1 → optional + single value.
      upper=='*'         → array-only (`type: array, items: {...}`,
                                       minItems if lower>=1).
  - Generalizations are walked: inherited attributes are merged into the
    child node (child overrides parent on name collision).
  - The Node $def name is the class's UML name. Docs are taken from the
    "Definition" section of the class's ownedComment (cleaned).
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
import textwrap
from collections import OrderedDict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Optional
from xml.etree import ElementTree as ET

import yaml

NS = {
    "uml": "http://www.omg.org/spec/UML/20131001",
    "xmi": "http://www.omg.org/spec/XMI/20131001",
}
XMI_ID = f"{{{NS['xmi']}}}id"
XMI_IDREF = f"{{{NS['xmi']}}}idref"
XMI_TYPE = f"{{{NS['xmi']}}}type"
XMI_HREF = "href"

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = REPO_ROOT / "_sources"

# ---------------------------------------------------------------------------
# Model classes
# ---------------------------------------------------------------------------

@dataclass
class Property:
    id: str
    name: str
    type_id: Optional[str]      # idref to a Class/DataType/Enum in this XMI
    primitive: Optional[str]    # 'String', 'Integer', 'Boolean', 'Real', etc.
    lower: int                  # 0 or positive; default 1 (UML default)
    upper: int                  # -1 sentinel for *
    doc: Optional[str]
    is_assoc_end: bool          # True if <association> ref present
    aggregation: Optional[str]  # 'composite', 'shared', or None


@dataclass
class UmlClass:
    id: str
    name: str
    package: str
    doc: Optional[str]
    is_abstract: bool
    parents: list[str]          # generalization superClass ids
    properties: list[Property]
    kind: str = "class"         # 'class' | 'datatype' | 'enumeration'
    literals: list[str] = field(default_factory=list)


@dataclass
class Model:
    elements: dict[str, UmlClass]      # id -> element
    name_to_id: dict[str, list[str]]   # name -> [ids] (multiple if dupes)


# ---------------------------------------------------------------------------
# XMI parsing
# ---------------------------------------------------------------------------

PRIMITIVE_FRAGMENTS = {
    "String": "string",
    "Integer": "integer",
    "Boolean": "boolean",
    "Real": "number",
    "UnlimitedNatural": "integer",
}


def _text(elem: ET.Element, child: str) -> Optional[str]:
    e = elem.find(child)
    if e is not None and e.text is not None:
        return e.text.strip()
    return None


def _local_doc(elem: ET.Element) -> Optional[str]:
    comment = elem.find("ownedComment")
    if comment is None:
        return None
    body = comment.find("body")
    if body is None or body.text is None:
        return None
    return body.text


def _parse_int_value(elem: Optional[ET.Element], default: int) -> int:
    if elem is None:
        return default
    v = elem.find("value")
    raw = v.text.strip() if (v is not None and v.text) else ""
    if raw == "*":
        return -1
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _parse_property(elem: ET.Element, owner_name: str = "") -> Property:
    pid = elem.get(XMI_ID, "")
    name = _text(elem, "name") or ""
    type_id = None
    primitive = None
    type_el = elem.find("type")
    if type_el is not None:
        if XMI_IDREF in type_el.attrib:
            type_id = type_el.get(XMI_IDREF)
        elif XMI_HREF in type_el.attrib:
            href = type_el.get(XMI_HREF, "")
            frag = href.split("#", 1)[-1]
            primitive = PRIMITIVE_FRAGMENTS.get(frag, None)
            if primitive is None:
                primitive = "string"  # unknown primitive → string fallback
    lower = _parse_int_value(elem.find("lowerValue"), 1)
    upper = _parse_int_value(elem.find("upperValue"), 1)
    doc = _local_doc(elem)
    assoc_el = elem.find("association")
    is_assoc = assoc_el is not None
    aggregation = elem.get("aggregation")

    # Recover a role name when the navigable end has no <name>: the assoc id
    # ends with `<Owner>_<role>_<Target>` (where role may contain underscores).
    # The id may be prefixed with a path using dots and/or dashes — match the
    # owner_role_target tail anchored at end-of-string.
    if not name and is_assoc and owner_name:
        assoc_id = assoc_el.get(XMI_IDREF, "") if assoc_el is not None else ""
        m = re.search(rf"(?:^|[.\-_]){re.escape(owner_name)}_(.+)_([A-Za-z][\w]*)$", assoc_id)
        if m:
            name = m.group(1)

    return Property(
        id=pid, name=name, type_id=type_id, primitive=primitive,
        lower=lower, upper=upper, doc=doc,
        is_assoc_end=is_assoc, aggregation=aggregation,
    )


def _parse_class(elem: ET.Element, package: str, kind: str) -> UmlClass:
    cid = elem.get(XMI_ID, "")
    name = _text(elem, "name") or cid
    is_abstract = elem.get("isAbstract", "false") == "true"
    doc = _local_doc(elem)
    parents = []
    for gen in elem.findall("generalization"):
        # `general` may be either an attribute on <generalization> or a child
        # element <general xmi:idref="..."/>; canonical XMI 2.5.1 uses the
        # child form.
        sup = gen.get("general")
        if not sup:
            child = gen.find("general")
            if child is not None:
                sup = child.get(XMI_IDREF)
        if sup:
            parents.append(sup)
    props: list[Property] = []
    owner_name = _text(elem, "name") or ""
    for attr in elem.findall("ownedAttribute"):
        props.append(_parse_property(attr, owner_name=owner_name))
    literals: list[str] = []
    if kind == "enumeration":
        for lit in elem.findall("ownedLiteral"):
            n = _text(lit, "name") or lit.get(XMI_ID, "")
            literals.append(n)
    return UmlClass(
        id=cid, name=name, package=package, doc=doc,
        is_abstract=is_abstract, parents=parents, properties=props,
        kind=kind, literals=literals,
    )


def _walk_packages(root: ET.Element, model: Model, current_path: list[str]):
    for child in list(root):
        ctype = child.get(XMI_TYPE, "")
        if ctype == "uml:Package":
            pname = _text(child, "name") or child.get(XMI_ID, "")
            _walk_packages(child, model, current_path + [pname])
            continue
        kind = None
        if ctype == "uml:Class":
            kind = "class"
        elif ctype == "uml:DataType":
            kind = "datatype"
        elif ctype == "uml:Enumeration":
            kind = "enumeration"
        if kind:
            cls = _parse_class(child, ".".join(current_path), kind)
            if cls.id in model.elements:
                # Duplicate id (shouldn't happen in canonical XMI); keep first.
                continue
            model.elements[cls.id] = cls
            model.name_to_id.setdefault(cls.name, []).append(cls.id)


def parse_xmi(path: Path) -> Model:
    tree = ET.parse(path)
    root = tree.getroot()
    # XMI root is <xmi:XMI>; the model lives in <uml:Model> inside.
    uml_model = root.find("uml:Model", NS)
    if uml_model is None:
        # Some exports omit the namespace prefix on Model.
        for child in root:
            if child.tag.endswith("Model"):
                uml_model = child
                break
    if uml_model is None:
        raise SystemExit("Could not find <uml:Model> in XMI")
    model = Model(elements={}, name_to_id={})
    _walk_packages(uml_model, model, [_text(uml_model, "name") or "Model"])
    return model


# ---------------------------------------------------------------------------
# Doc cleaning
# ---------------------------------------------------------------------------

_SECTION_RE = re.compile(
    r"^(Definition|Examples?|Explanatory notes?)\s*\n=+\s*\n",
    re.MULTILINE,
)


def clean_definition(doc: Optional[str]) -> Optional[str]:
    """Extract the "Definition" section from a UCMIS-style ownedComment body.

    UCMIS comments are formatted as:
        Definition
        ==========
        <text>

        Examples
        ========
        ...

    Return only the Definition body (collapsed whitespace). If no recognizable
    section markers are present, return the whole body trimmed.
    """
    if not doc:
        return None
    # Normalize whitespace and split on section headers
    parts = _SECTION_RE.split(doc.strip())
    # _SECTION_RE.split returns: [pre, header1, body1, header2, body2, ...]
    if len(parts) >= 3:
        # Walk pairs (header, body) and pick "Definition"
        for i in range(1, len(parts) - 1, 2):
            if parts[i].lower().startswith("definition"):
                body = parts[i + 1].strip()
                return _normalize_whitespace(body)
        # No Definition header: take first non-empty body
        for i in range(2, len(parts), 2):
            if parts[i].strip():
                return _normalize_whitespace(parts[i].strip())
    return _normalize_whitespace(doc.strip())


def _normalize_whitespace(s: str) -> str:
    # Collapse runs of whitespace; preserve paragraph breaks
    paragraphs = re.split(r"\n\s*\n", s)
    cleaned = [re.sub(r"\s+", " ", p).strip() for p in paragraphs]
    return "\n\n".join(p for p in cleaned if p)


# ---------------------------------------------------------------------------
# Schema construction
# ---------------------------------------------------------------------------

@dataclass
class BuildContext:
    model: Model
    prefix: str                       # e.g. "cdi"
    shared_bb_relpath: str            # e.g. "../ddicdiDataTypes/schema.yaml"
    shared_defs: set[str]             # names available in the shared BB
    inline_class_names: set[str]      # uml:Class names to inline (no id-ref fallback)
    inline_or_ref_class_names: set[str]  # explicit inline-OR-id-reference (now also default)
    reference_class_names: set[str]   # uml:Class names to force as id-reference only
    exclude_class_names: set[str]     # uml:Class / uml:DataType names to drop entirely (any property typed by one of these is omitted; the type's $def is not registered)
    exclude_property_specs: set[str]  # `ClassName.propertyName` pairs to drop. Use when an inherited UML property is conceptually wrong on a specific subclass (e.g. DataStructure.isDefinedBy belongs on DataStructureComponent subclasses, not on DataStructure variants).
    inline_datatypes: bool            # if True, never $ref shared bb; inline all
    strict_required: bool             # if True, emit `required` per UML lower>=1
    external_class_refs: dict[str, str]  # ClassName -> $ref target if defined in another BB
    local_defs: dict[str, dict]       # name -> $def schema fragment
    expanding: set[str]               # currently-being-expanded type names (cycle guard)


def collect_inherited_properties(class_id: str, model: Model) -> list[Property]:
    """Walk parent chain leaf-first. Within a single class, all properties are
    kept (UCMIS overloads role names — e.g. CodeList has two `cdi:has`
    associations to different targets). Across inheritance, a subclass that
    redefines a name shadows ancestors of that name."""
    result: list[Property] = []
    visited: set[str] = set()
    shadowed: set[str] = set()  # names defined at a more specific level

    def visit(cid: str):
        if cid in visited or cid not in model.elements:
            return
        visited.add(cid)
        cls = model.elements[cid]
        for prop in cls.properties:
            if prop.name and prop.name in shadowed:
                continue
            result.append(prop)
        # Names defined here shadow same-named props on ancestors
        shadowed.update(p.name for p in cls.properties if p.name)
        for parent_id in cls.parents:
            visit(parent_id)

    visit(class_id)
    return result


def _qname(prefix: str, local: str) -> str:
    return f"{prefix}:{local}"


def _ref_to_shared(ctx: BuildContext, def_name: str) -> dict:
    return {"$ref": f"{ctx.shared_bb_relpath}#/$defs/{def_name}"}


def _ref_to_local(def_name: str) -> dict:
    return {"$ref": f"#/$defs/{def_name}"}


def _id_reference_schema(ctx: BuildContext) -> dict:
    if "id-reference" in ctx.shared_defs and not ctx.inline_datatypes:
        return _ref_to_shared(ctx, "id-reference")
    if "id-reference" not in ctx.local_defs:
        ctx.local_defs["id-reference"] = {
            "type": "object",
            "description": "JSON-LD @id reference to a node defined elsewhere",
            "properties": {
                "@id": {"type": "string"},
            },
            "required": ["@id"],
        }
    return _ref_to_local("id-reference")


def _group_to_schema(group: list[Property], ctx: BuildContext) -> Optional[dict]:
    """Render N UML properties that share a role name as a single JSON-Schema
    fragment. For len==1 this is just `property_to_schema`. For len>1 the
    target type schemas are combined into a flat `anyOf`, and multiplicity is
    union-ed (lower = min, upper = max with `*` dominating)."""
    if len(group) == 1:
        return property_to_schema(group[0], ctx)
    inner_options: list[dict] = []
    for p in group:
        opt = _resolve_property_type(p, ctx)
        if opt is None:
            continue
        # Flatten nested anyOf: a class target now resolves to
        # `{anyOf: [target, id-ref]}`, so when N such options are merged into
        # the outer anyOf we want one flat list rather than anyOf-of-anyOf.
        sub_options = opt["anyOf"] if (set(opt.keys()) == {"anyOf"}) else [opt]
        for sub in sub_options:
            if sub not in inner_options:
                inner_options.append(sub)
    if not inner_options:
        return None
    inner = {"anyOf": inner_options} if len(inner_options) > 1 else inner_options[0]
    combined_lower = min(p.lower for p in group)
    uppers = [p.upper for p in group]
    combined_upper = -1 if -1 in uppers else max(uppers)
    synthetic = Property(
        id=group[0].id, name=group[0].name,
        type_id=None, primitive=None,
        lower=combined_lower, upper=combined_upper,
        doc=None, is_assoc_end=False, aggregation=None,
    )
    out = _wrap_multiplicity(inner, synthetic)
    # Combine docs from each property; dedup while preserving first-seen order.
    docs: list[str] = []
    for p in group:
        if not p.doc:
            continue
        d = clean_definition(p.doc)
        if d and d not in docs:
            docs.append(d)
    if docs:
        out = dict(out)
        out["description"] = "\n\n".join(docs)
    return out


def _target_type_name(prop: Property, ctx: BuildContext) -> Optional[str]:
    """Return the simple class/datatype/enum name of a property's target,
    or None for primitives / unresolvable targets / excluded targets."""
    if prop.primitive or not prop.type_id:
        return None
    target = ctx.model.elements.get(prop.type_id)
    if target is None:
        return None
    if target.name in ctx.exclude_class_names:
        return None
    return target.name


def _has_distinct_named_targets(group: list[Property], ctx: BuildContext) -> bool:
    """True when the group has at least two properties resolving to distinct
    named targets (class / datatype / enum). Used to decide whether to
    disambiguate same-named UML associations by suffixing the target class —
    UCMIS / DDI-CDI re-use bare role names like `has` / `uses` for several
    distinct targets within a single class, and emitting them as one anyOf
    key strips type information from the JSON-LD tree."""
    seen: set[str] = set()
    for prop in group:
        n = _target_type_name(prop, ctx)
        if n is None:
            continue
        seen.add(n)
        if len(seen) >= 2:
            return True
    return False


def _build_properties_dict(
    prop_list: list[Property], ctx: BuildContext,
    owner_class_name: Optional[str] = None,
) -> tuple[OrderedDict, list[str]]:
    """Group UML properties by role name, then build the JSON Schema
    `properties` dict and the matching `required` list. When N>1 properties
    share a role name and target distinct classes, emit one key per target
    suffixed with `_<TargetName>` so each remains unambiguous in the JSON
    tree (the source class is implicit from position).

    `owner_class_name` is the name of the class/datatype whose properties
    are being emitted; used to honour `--exclude-property
    ClassName.propertyName` exclusions (e.g. drop an inherited property
    from a specific subclass)."""
    groups: OrderedDict[str, list[Property]] = OrderedDict()
    for prop in prop_list:
        if not prop.name:
            print(f"WARN: skipping unnamed property id={prop.id}", file=sys.stderr)
            continue
        groups.setdefault(prop.name, []).append(prop)
    properties: OrderedDict = OrderedDict()
    required: list[str] = []
    for name, group in groups.items():
        if owner_class_name and f"{owner_class_name}.{name}" in ctx.exclude_property_specs:
            continue  # excluded for this owner
        if len(group) > 1 and _has_distinct_named_targets(group, ctx):
            # Disambiguate by suffixing each property with its target class.
            # Properties to the same target are merged into a shared anyOf at
            # the same suffixed key.
            by_target: OrderedDict[str, list[Property]] = OrderedDict()
            for prop in group:
                tn = _target_type_name(prop, ctx)
                if tn is None:
                    print(
                        f"WARN: cannot suffix '{name}' for prop id={prop.id} "
                        "(primitive or excluded target); dropping",
                        file=sys.stderr,
                    )
                    continue
                by_target.setdefault(tn, []).append(prop)
            for tn, sub_group in by_target.items():
                sub = _group_to_schema(sub_group, ctx)
                if sub is None:
                    continue
                key = _qname(ctx.prefix, f"{name}_{tn}")
                properties[key] = sub
                if ctx.strict_required and any(p.lower >= 1 for p in sub_group):
                    required.append(key)
        else:
            sub = _group_to_schema(group, ctx)
            if sub is None:
                continue
            key = _qname(ctx.prefix, name)
            properties[key] = sub
            if ctx.strict_required and any(p.lower >= 1 for p in group):
                required.append(key)
    return properties, required


def datatype_to_def(dt: UmlClass, ctx: BuildContext) -> dict:
    """Build a $def schema body for a uml:DataType."""
    schema: dict[str, Any] = {"type": "object"}
    if dt.doc:
        schema["description"] = clean_definition(dt.doc) or dt.doc.strip()
    props: OrderedDict = OrderedDict()
    props["@type"] = {
        "type": "array",
        "items": {"type": "string"},
        "contains": {"const": _qname(ctx.prefix, dt.name)},
        "minItems": 1,
    }
    extra, required = _build_properties_dict(
        collect_inherited_properties(dt.id, ctx.model), ctx,
        owner_class_name=dt.name,
    )
    props.update(extra)
    schema["properties"] = props
    if required:
        schema["required"] = required
    return schema


def class_to_node_def(cls: UmlClass, ctx: BuildContext) -> dict:
    """Build a $def schema body for a uml:Class (a JSON-LD node)."""
    schema: dict[str, Any] = {"type": "object"}
    if cls.doc:
        schema["description"] = clean_definition(cls.doc) or cls.doc.strip()
    props: OrderedDict = OrderedDict()
    required: list[str] = ["@type"]
    props["@type"] = {
        "type": "array",
        "items": {"type": "string"},
        "contains": {"const": _qname(ctx.prefix, cls.name)},
        "minItems": 1,
    }
    props["@id"] = {
        "type": "string",
        "description": f"Identifier for this {cls.name} node",
    }
    extra, extra_req = _build_properties_dict(
        collect_inherited_properties(cls.id, ctx.model), ctx,
        owner_class_name=cls.name,
    )
    props.update(extra)
    required.extend(extra_req)
    schema["properties"] = props
    if required:
        schema["required"] = required
    return schema


def _wrap_multiplicity(inner: dict, prop: Property) -> dict:
    """Apply UML multiplicity to a JSON Schema fragment.

    upper==1   → return inner unchanged.
    upper==-1  → wrap in array (array-only convention; minItems if lower>=1).
    upper>1    → array with maxItems.
    """
    if prop.upper == 1:
        return inner
    array_schema: dict[str, Any] = {"type": "array", "items": inner}
    if prop.lower >= 1:
        array_schema["minItems"] = prop.lower
    if prop.upper > 1:
        array_schema["maxItems"] = prop.upper
    return array_schema


def property_to_schema(prop: Property, ctx: BuildContext) -> Optional[dict]:
    """Render one UML property as a JSON Schema fragment, including
    multiplicity wrapping and an optional `description`."""
    if not prop.name:
        # Anonymous association end where role name couldn't be recovered;
        # skip rather than emit a malformed `cdi:` key.
        print(f"WARN: skipping unnamed property id={prop.id}", file=sys.stderr)
        return None
    inner = _resolve_property_type(prop, ctx)
    if inner is None:
        return None
    out = _wrap_multiplicity(inner, prop)
    desc = clean_definition(prop.doc) if prop.doc else None
    if desc:
        # Prefer the description on the outer (multiplicity) wrapper if array,
        # else inline it on the inner.
        out = dict(out)  # copy so we don't mutate $ref dicts shared across props
        out["description"] = desc
    return out


def _resolve_property_type(prop: Property, ctx: BuildContext) -> Optional[dict]:
    if prop.primitive:
        return {"type": prop.primitive}
    if not prop.type_id:
        return {"type": "string"}  # unknown type → permissive string
    target = ctx.model.elements.get(prop.type_id)
    if target is None:
        # Type id not present in this XMI (could be cross-package ref).
        return {"type": "string"}

    if target.name in ctx.exclude_class_names:
        # Caller drops this property entirely (also prevents the target's $def
        # from being registered, since _resolve_class_target / _resolve_datatype_ref
        # are never reached).
        return None

    if target.kind == "enumeration":
        # Emit literal-list enum
        return {"type": "string", "enum": list(target.literals)}

    if target.kind == "datatype":
        return _resolve_datatype_ref(target, ctx)

    # uml:Class:
    if target.name in ctx.reference_class_names:
        return _id_reference_schema(ctx)
    if target.name in ctx.inline_class_names:
        # Force inline-only (no id-reference fallback). Useful for true
        # compositions where linking by @id doesn't make sense.
        return _resolve_class_target(target, ctx)
    # Default: inline-or-ref. Prefer a $ref to whichever other BB already
    # defines this class; if no other BB has it, inline locally. Either way,
    # also accept a plain id-reference (the JSON-LD embed-or-link pattern).
    return {
        "anyOf": [
            _resolve_class_target(target, ctx),
            _id_reference_schema(ctx),
        ],
    }


def _resolve_class_target(cls: UmlClass, ctx: BuildContext) -> dict:
    """Resolve a uml:Class target to a $ref. Prefers an external BB that
    already defines the class (so we don't duplicate definitions across BBs);
    falls back to inlining locally."""
    ext = ctx.external_class_refs.get(cls.name)
    if ext:
        return {"$ref": ext}
    return _inline_class_ref(cls, ctx)


def _resolve_datatype_ref(dt: UmlClass, ctx: BuildContext) -> dict:
    """Return a schema fragment that references this dt-type, either via
    shared-BB $ref or by inlining (and registering) a local $def."""
    if not ctx.inline_datatypes and dt.name in ctx.shared_defs:
        return _ref_to_shared(ctx, dt.name)
    # Inline: ensure local $def exists
    if dt.name not in ctx.local_defs:
        if dt.name in ctx.expanding:
            # Cycle: rely on the in-progress $def already being registered or
            # mark a placeholder that will be filled when the outer call returns.
            ctx.local_defs[dt.name] = {
                "type": "object",
                "$comment": f"cycle stub for {dt.name}",
            }
        else:
            ctx.expanding.add(dt.name)
            ctx.local_defs[dt.name] = datatype_to_def(dt, ctx)
            ctx.expanding.discard(dt.name)
    return _ref_to_local(dt.name)


def _inline_class_ref(cls: UmlClass, ctx: BuildContext) -> dict:
    """Inline a uml:Class as a local $def (used for compositions)."""
    if cls.name not in ctx.local_defs:
        if cls.name in ctx.expanding:
            return _ref_to_local(cls.name)
        ctx.expanding.add(cls.name)
        ctx.local_defs[cls.name] = class_to_node_def(cls, ctx)
        ctx.expanding.discard(cls.name)
    return _ref_to_local(cls.name)


# ---------------------------------------------------------------------------
# Top-level schema assembly
# ---------------------------------------------------------------------------

def build_root_schema(
    classes: list[UmlClass],
    ctx: BuildContext,
    title: str,
    description: Optional[str],
) -> dict:
    """Emit a BB schema.yaml whose root *is* the Node definition (single root)
    or an `anyOf` of Node $refs (multiple roots). The wrapper pattern that
    accepts single/array/@graph forms is intentionally omitted — that wrapping
    is applied by profile schemas that compose this BB."""
    # Build per-class node defs (registers them in ctx.local_defs)
    node_def_names: list[str] = []
    for cls in classes:
        if cls.name not in ctx.local_defs:
            ctx.expanding.add(cls.name)
            ctx.local_defs[cls.name] = class_to_node_def(cls, ctx)
            ctx.expanding.discard(cls.name)
        node_def_names.append(cls.name)

    root: dict[str, Any] = OrderedDict()
    root["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    root["title"] = title
    if description:
        root["description"] = description

    if len(node_def_names) == 1:
        # Single root: promote the class def to the schema root. Drop the
        # class-level `description` since the root carries one already.
        node = copy.deepcopy(ctx.local_defs[node_def_names[0]])
        node.pop("description", None)
        for k, v in node.items():
            root[k] = v
    else:
        # Multiple roots: $ref each at the root via anyOf, classes live in $defs.
        root["anyOf"] = [_ref_to_local(n) for n in node_def_names]

    # Detect self-references to a single-root class: if the root class is
    # referenced by `#/$defs/<name>` from anywhere (its own properties or a
    # helper $def), keep that root class in $defs so the ref resolves.
    self_referenced_roots: set[str] = set()
    if len(node_def_names) == 1:
        only_root = node_def_names[0]
        target = f"#/$defs/{only_root}"
        def _has_ref(o: Any) -> bool:
            if isinstance(o, dict):
                if o.get("$ref") == target:
                    return True
                return any(_has_ref(v) for v in o.values())
            if isinstance(o, list):
                return any(_has_ref(v) for v in o)
            return False
        scan_targets = [v for k, v in root.items() if k != "$defs"]
        scan_targets.extend(v for k, v in ctx.local_defs.items() if k != only_root)
        if any(_has_ref(t) for t in scan_targets):
            self_referenced_roots.add(only_root)

    # $defs holds helpers (and, for the multi-root case, the root classes too).
    helper_keys = sorted(k for k in ctx.local_defs if k not in node_def_names)
    defs = OrderedDict()
    if len(node_def_names) > 1:
        for n in node_def_names:
            defs[n] = ctx.local_defs[n]
    else:
        for n in node_def_names:
            if n in self_referenced_roots:
                defs[n] = ctx.local_defs[n]
    for k in helper_keys:
        defs[k] = ctx.local_defs[k]
    if defs:
        root["$defs"] = defs
    return root


# ---------------------------------------------------------------------------
# YAML emit (block style, quoted JSON-LD/prefixed keys, folded descriptions)
# ---------------------------------------------------------------------------

class _BBYamlDumper(yaml.SafeDumper):
    pass


def _str_representer(dumper, data: str):
    style = None
    if "\n" in data:
        style = "|"
    elif len(data) > 80:
        style = ">"
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


def _ordered_dict_representer(dumper, data):
    return dumper.represent_dict(data.items())


_BBYamlDumper.add_representer(str, _str_representer)
_BBYamlDumper.add_representer(OrderedDict, _ordered_dict_representer)


def _quote_special_keys(obj: Any) -> Any:
    """JSON-LD keys (@type, @id, @graph) and prefixed keys (cdi:foo) need to be
    quoted in YAML. PyYAML quotes strings that *contain* `:` automatically when
    used as values, but as mapping keys it sometimes emits them unquoted. We
    side-step that by ensuring every key is a plain str — the str representer
    above promotes any string with `:` or `@` to single-quoted form.
    """
    return obj  # placeholder — handled at representer level below


_IDENT_RE = re.compile(r"^[\w@$#./:-]+$")


def _key_representer_safer(dumper, data: str):
    # Heuristic: distinguish structural identifiers (keys, $refs, CURIEs,
    # JSON-Pointers, URIs without spaces) from prose. Identifiers go single-
    # quoted so YAML-significant chars (`@`, `:`, `#`, `$`) are unambiguous;
    # prose with whitespace gets folded for readability.
    style = None
    if not data:
        style = "'"
    elif _IDENT_RE.match(data) and (
        data.startswith(("@", "$", "#", "/")) or ":" in data or "#" in data
    ):
        style = "'"
    elif "\n" in data:
        style = "|"
    elif len(data) > 80:
        style = ">"
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


# Override default str representer with the key-aware one. This is fine because
# our schemas don't have legitimate long-string *values* that need different
# treatment; we want keys quoted and we'll re-fold long descriptions manually.
_BBYamlDumper.add_representer(str, _key_representer_safer)


def emit_yaml(schema: dict, out_path: Path):
    text = yaml.dump(
        schema,
        Dumper=_BBYamlDumper,
        sort_keys=False,
        default_flow_style=False,
        width=88,
        allow_unicode=True,
        indent=2,
    )
    out_path.write_text(text, encoding="utf-8")


# ---------------------------------------------------------------------------
# Companion files
# ---------------------------------------------------------------------------

def emit_companions(out_dir: Path, bb_name: str, title: str, abstract: str,
                    class_names: list[str], prefix: str, prefix_iri: str,
                    today: str):
    bblock = OrderedDict([
        ("$schema", "metaschema.yaml"),
        ("name", title),
        ("abstract", abstract),
        ("status", "under-development"),
        ("dateTimeAddition", f"{today}T00:00:00Z"),
        ("itemClass", "schema"),
        ("register", "cdif-building-block-register"),
        ("version", "0.1"),
        ("dateOfLastChange", today),
        ("link", "https://github.com/usgin/metadataBuildingBlocks"),
        ("maturity", "draft"),
        ("scope", "unstable"),
        ("tags", ["CDIF", "DDI-CDI"] + class_names),
        ("sources", [
            {
                "title": "DDI-CDI 1.0 Specification",
                "link": "https://ddialliance.org/Specification/DDI-CDI/1.0/",
            }
        ]),
    ])
    (out_dir / "bblock.json").write_text(
        json.dumps(bblock, indent=2) + "\n", encoding="utf-8")

    context = {"@context": {prefix: prefix_iri}}
    (out_dir / "context.jsonld").write_text(
        json.dumps(context, indent=2) + "\n", encoding="utf-8")

    shacl = textwrap.dedent(f"""\
        # SHACL rules skeleton for {title}.
        # TODO: author NodeShape and PropertyShape constraints from the UML model.

        @prefix sh:   <http://www.w3.org/ns/shacl#> .
        @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
        @prefix {prefix}:  <{prefix_iri}> .
        @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        """)
    (out_dir / "rules.shacl").write_text(shacl, encoding="utf-8")

    examples = [
        {
            "title": f"Minimal {class_names[0]}",
            "content": "TODO: replace with a JSON-LD example.",
        }
    ]
    (out_dir / "examples.yaml").write_text(
        yaml.safe_dump(examples, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# Shared-types discovery
# ---------------------------------------------------------------------------

def discover_shared_defs(shared_yaml_path: Path) -> set[str]:
    if not shared_yaml_path.exists():
        return set()
    with open(shared_yaml_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        return set()
    defs = data.get("$defs") or {}
    return set(defs.keys())


def _extract_root_class_names(doc: dict, prefix: str) -> list[str]:
    """Extract the class name(s) owned by a BB whose root *is* the Node.
    Three shapes recognized:
      1) Single-class:    properties.@type.contains.const = "<prefix>:<Class>".
      2) Multi-class @type: properties.@type.anyOf is a list of
         {contains: {const: "<prefix>:<Class>"}}.
      3) Multi-root anyOf at schema root: anyOf of $refs to local $defs,
         each $def carrying a single-class @type contains.const.
    Returns the class names (without prefix). Empty list if no root class
    detected (e.g. umbrella BBs like ddicdiAgent that only dispatch via
    external $refs).
    """
    names: list[str] = []
    plen = len(prefix) + 1

    def _const_to_name(const) -> Optional[str]:
        if isinstance(const, str) and const.startswith(prefix + ":"):
            return const[plen:]
        return None

    props = doc.get("properties")
    if isinstance(props, dict):
        type_prop = props.get("@type")
        if isinstance(type_prop, dict):
            contains = type_prop.get("contains")
            if isinstance(contains, dict):
                n = _const_to_name(contains.get("const"))
                if n:
                    names.append(n)
            for branch in type_prop.get("anyOf") or []:
                if isinstance(branch, dict):
                    sub = branch.get("contains")
                    if isinstance(sub, dict):
                        n = _const_to_name(sub.get("const"))
                        if n and n not in names:
                            names.append(n)

    if not names:
        # Multi-root anyOf at top: each branch is {$ref: '#/$defs/X'}.
        for branch in doc.get("anyOf") or []:
            if not isinstance(branch, dict):
                continue
            ref = branch.get("$ref")
            if not isinstance(ref, str) or not ref.startswith("#/$defs/"):
                continue
            def_name = ref[len("#/$defs/"):]
            sub = (doc.get("$defs") or {}).get(def_name)
            if isinstance(sub, dict):
                sub_props = sub.get("properties")
                if isinstance(sub_props, dict):
                    sub_type = sub_props.get("@type")
                    if isinstance(sub_type, dict):
                        contains = sub_type.get("contains")
                        if isinstance(contains, dict):
                            n = _const_to_name(contains.get("const"))
                            if n and n not in names:
                                names.append(n)
    return names


def discover_external_class_refs(
    out_bb_dir: Path, sources_dir: Path, prefix: str,
) -> dict[str, str]:
    """Walk every other schema.yaml under sources_dir and return a map of
    {ClassName: $ref-target} pointing to the BB that "owns" each class.
    A class is owned by a BB only when it is that BB's *root* class — i.e.,
    the schema's properties['@type'].contains.const is "<prefix>:<ClassName>".
    $defs entries are intentionally NOT registered: they can be private
    inlinings rather than canonical homes, and registering them introduces
    order-dependence between BBs. The $ref-target is a relative path from
    `out_bb_dir`.

    When a class name appears as a root in multiple BBs (e.g. when the same
    UML class has been cloned into a parallel directory like ddiProperties
    vs ddiCDIFProperties), prefer the BB whose parent directory matches
    out_bb_dir's parent — i.e. don't leak a cross-package reference."""
    import os
    out_resolved = out_bb_dir.resolve()
    out_parent = out_resolved.parent
    # Collect candidates per class as (rel_path, same_parent) tuples,
    # then pick the same-parent one if available; otherwise the first.
    candidates: dict[str, list[tuple[str, bool]]] = {}
    for schema_path in sorted(sources_dir.rglob("schema.yaml")):
        bb_dir = schema_path.parent.resolve()
        if bb_dir == out_resolved:
            continue
        try:
            with open(schema_path, encoding="utf-8") as f:
                doc = yaml.safe_load(f)
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        root_classes = _extract_root_class_names(doc, prefix)
        # Also derive a class name from the BB directory name (project
        # convention: ddicdi<ClassName>; also kebab `ddi-cdif-<kebab-name>`).
        # This catches abstract parents like `ValueDomain` whose concrete
        # subclasses are roots of the same BB, and umbrella BBs like
        # `ddi-cdif-agent` whose root is anyOf of sibling-BB $refs.
        bb_dir_name = bb_dir.name
        kebab_prefixes = ("ddi-cdif-",)
        camel_prefixes = ("ddicdi", "cdif", "skos", "dcat", "schema", "prov", "xas")
        derived: Optional[str] = None
        for prefix_name in kebab_prefixes:
            if bb_dir_name.startswith(prefix_name) and len(bb_dir_name) > len(prefix_name):
                tail = bb_dir_name[len(prefix_name):]
                derived = "".join(p[:1].upper() + p[1:] for p in tail.split("-") if p)
                break
        if derived is None:
            for prefix_name in camel_prefixes:
                if bb_dir_name.startswith(prefix_name) and len(bb_dir_name) > len(prefix_name):
                    tail = bb_dir_name[len(prefix_name):]
                    if tail[:1].isupper():
                        derived = tail
                    break
        if derived and derived not in root_classes:
            root_classes.append(derived)
        if not root_classes:
            continue
        try:
            rel = os.path.relpath(bb_dir, out_resolved).replace(os.sep, "/")
        except ValueError:
            continue
        is_same_parent = bb_dir.parent == out_parent
        for root_class in root_classes:
            candidates.setdefault(root_class, []).append((rel, is_same_parent))

    registry: dict[str, str] = {}
    for cls, opts in candidates.items():
        same = [o for o in opts if o[1]]
        chosen = same[0] if same else opts[0]
        registry[cls] = f"{chosen[0]}/schema.yaml"
    return registry


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _today_iso() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).date().isoformat()


def _split_csv(s: Optional[str]) -> list[str]:
    return [x.strip() for x in s.split(",")] if s else []


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description="Generate a CDIF building-block schema.yaml from canonical XMI.",
    )
    ap.add_argument("--xmi", type=Path, required=True,
                    help="Path to canonical XMI 2.5.1 file.")
    ap.add_argument("--class", dest="classes", required=True,
                    help="Comma-separated list of root class names.")
    ap.add_argument("--bb-name", required=True,
                    help="Building-block directory name (e.g. ddicdiValueDomain).")
    ap.add_argument("--out-dir", type=Path, required=True,
                    help="Parent directory; the BB folder will be created/replaced inside.")
    ap.add_argument("--title", default=None,
                    help="Human-readable BB title (default: derived from --bb-name).")
    ap.add_argument("--description", default=None,
                    help="BB-level description (default: extracted from first class docstring).")
    ap.add_argument("--prefix", default="cdi",
                    help="JSON-LD prefix label (default: cdi).")
    ap.add_argument("--prefix-iri",
                    default="http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
                    help="IRI for the prefix.")
    ap.add_argument("--shared-bb",
                    default="../ddicdiDataTypes/schema.yaml",
                    help="Relative path to shared-types BB schema.yaml "
                         "(default: ../ddicdiDataTypes/schema.yaml).")
    ap.add_argument("--inline", default="",
                    help="Comma-separated uml:Class names to inline as compositions.")
    ap.add_argument("--inline-or-ref", default="",
                    help="Comma-separated names that may be either an inlined object "
                         "or an @id reference (emitted as anyOf).")
    ap.add_argument("--reference", default="",
                    help="Comma-separated names to force as id-reference (overrides --inline).")
    ap.add_argument("--exclude-class", default="",
                    help="Comma-separated uml:Class / uml:DataType names to drop entirely. "
                         "Properties typed by an excluded class are omitted; the type's $def "
                         "is not emitted. Use for classes the project intentionally won't "
                         "implement (e.g. CatalogDetails).")
    ap.add_argument("--exclude-property", default="",
                    help="Comma-separated `ClassName.propertyName` pairs to drop. "
                         "Use when an inherited UML property is conceptually wrong on a "
                         "specific subclass (e.g. DataStructure.isDefinedBy belongs on "
                         "DataStructureComponent subclasses, not on the DataStructure variants).")
    ap.add_argument("--inline-datatypes", action="store_true",
                    help="Inline all dt-types locally instead of $ref-ing the shared BB.")
    ap.add_argument("--schema-only", action="store_true",
                    help="Only emit schema.yaml; skip bblock.json/context.jsonld/rules.shacl/examples.yaml.")
    ap.add_argument("--strict-required", action="store_true",
                    help="Emit `required` for every property with UML lower>=1. "
                         "Default is project-style: only @type required.")
    args = ap.parse_args(argv)

    model = parse_xmi(args.xmi)
    print(f"Parsed XMI: {len(model.elements)} elements", file=sys.stderr)

    # Resolve class names → ids
    class_names = _split_csv(args.classes)
    classes: list[UmlClass] = []
    for name in class_names:
        ids = model.name_to_id.get(name, [])
        if not ids:
            print(f"ERROR: class '{name}' not found in XMI", file=sys.stderr)
            return 2
        if len(ids) > 1:
            print(f"WARN: '{name}' is ambiguous ({len(ids)} elements); using first",
                  file=sys.stderr)
        cls = model.elements[ids[0]]
        if cls.kind != "class":
            print(f"WARN: '{name}' is a {cls.kind}, not a uml:Class; emitting anyway",
                  file=sys.stderr)
        classes.append(cls)

    # Compute shared-defs registry from the sibling BB.
    # Try (1) relative to the output BB dir (the textually-correct lookup),
    # then (2) fall back to the canonical _sources/ddiProperties tree so the
    # script also works when --out-dir is a scratch directory.
    bb_out_dir = args.out_dir / args.bb_name
    bb_out_dir.mkdir(parents=True, exist_ok=True)
    shared_yaml_abs = (bb_out_dir / args.shared_bb).resolve()
    shared_defs = discover_shared_defs(shared_yaml_abs)
    if not shared_defs:
        # Fallback: resolve the relative path from a hypothetical sibling under
        # _sources/ddiProperties/<bb_name>.
        fallback = (SOURCES_DIR / "ddiProperties" / args.bb_name / args.shared_bb).resolve()
        shared_defs = discover_shared_defs(fallback)
        if shared_defs:
            print(f"INFO: shared $defs discovered via fallback: {fallback}",
                  file=sys.stderr)
    if not shared_defs and not args.inline_datatypes:
        print(f"WARN: no shared $defs discovered at {shared_yaml_abs}; "
              "set --inline-datatypes if intentional.", file=sys.stderr)

    # Build a registry of class names defined in OTHER BBs so we can $ref
    # out instead of duplicating definitions. Falls back to local inline if
    # no external definition is found.
    external_class_refs = discover_external_class_refs(
        out_bb_dir=bb_out_dir, sources_dir=SOURCES_DIR, prefix=args.prefix,
    )
    # The current BB's own root classes win over any external registration
    # (e.g. a cloned parallel BB). Without this, an inter-class reference
    # like Descriptor.hasValueFrom -> DescriptorValueDomain would resolve to
    # a parallel-package BB instead of the local $def.
    own_root_names = {c.name for c in classes}
    for own in own_root_names:
        external_class_refs.pop(own, None)
    if external_class_refs:
        print(f"INFO: discovered {len(external_class_refs)} class definitions "
              f"in sibling BBs", file=sys.stderr)

    ctx = BuildContext(
        model=model,
        prefix=args.prefix,
        shared_bb_relpath=args.shared_bb,
        shared_defs=shared_defs,
        inline_class_names=set(_split_csv(args.inline)),
        inline_or_ref_class_names=set(_split_csv(args.inline_or_ref)),
        reference_class_names=set(_split_csv(args.reference)),
        exclude_class_names=set(_split_csv(args.exclude_class)),
        exclude_property_specs=set(_split_csv(args.exclude_property)),
        inline_datatypes=args.inline_datatypes,
        strict_required=args.strict_required,
        external_class_refs=external_class_refs,
        local_defs=OrderedDict(),
        expanding=set(),
    )

    # Title and description
    if args.title:
        title = args.title
    else:
        title = " ".join(_humanize(args.bb_name).split())
    if args.description:
        description = args.description
    else:
        description = clean_definition(classes[0].doc)

    schema = build_root_schema(classes, ctx, title, description)

    schema_path = bb_out_dir / "schema.yaml"
    emit_yaml(schema, schema_path)
    print(f"Wrote {schema_path}", file=sys.stderr)

    if not args.schema_only:
        abstract = (description or "").strip().replace("\n\n", " ")
        if not abstract:
            abstract = f"Building block for {', '.join(class_names)}."
        emit_companions(
            out_dir=bb_out_dir,
            bb_name=args.bb_name,
            title=title,
            abstract=abstract,
            class_names=class_names,
            prefix=args.prefix,
            prefix_iri=args.prefix_iri,
            today=_today_iso(),
        )
        print(f"Wrote bblock.json, context.jsonld, rules.shacl, examples.yaml",
              file=sys.stderr)

    return 0


def _humanize(name: str) -> str:
    """ddicdiValueDomain → DDI-CDI Value Domain."""
    if name.lower().startswith("ddicdi"):
        rest = name[6:]
        return "DDI-CDI " + re.sub(r"(?<=[a-z])(?=[A-Z])", " ", rest)
    return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", name)


if __name__ == "__main__":
    sys.exit(main())
