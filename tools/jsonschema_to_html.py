#!/usr/bin/env python3
"""Generate UML-style HTML model pages directly from a CDIF profile module's
JSON Schema (schema.yaml), no XMI / mapping config required.

Targets the property-bundle profile modules under
  _sources/profiles/cdifProfile/<name>/schema.yaml
where the schema is a JSON-LD shape: top-level `properties` plus `$defs`.

The emitted HTML is visually consistent with cdif-uml-model/ (it reuses the
same _static/style.css, written by the XMI-based pipeline). Layout per module:
  <out_dir>/<umlName>/index.html
  <out_dir>/<umlName>/Classes/<X>.html
  <out_dir>/<umlName>/DataTypes/<Y>.html

A "main class" is synthesized from the top-level schema; its name is derived
from `@type.contains.const` (e.g. 'skos:ConceptScheme' -> 'ConceptScheme') or
overridden via --class-name (use 'Dataset' for cdifDiscovery, etc., to match
the cdifCore Dataset that this module's properties are mixed into).

Each named `$defs` entry becomes its own class (or DataType if it has no @id
and looks value-typed).

Cross-file $refs (e.g. `../../../schemaorgProperties/definedTerm/schema.yaml`)
become cross-profile class references. If a _registry.json next to the output
dir maps a class name to an umlName, the property type cell links to that
profile's page; otherwise the type is rendered as a plain label with the
referenced filename in a tooltip.

USAGE:
  python tools/jsonschema_to_html.py cdifConceptScheme
  python tools/jsonschema_to_html.py cdifDiscovery --class-name Dataset
  python tools/jsonschema_to_html.py cdifDiscovery \
      --schema _sources/profiles/cdifProfile/cdifDiscovery/schema.yaml \
      --out-dir cdif-uml-model
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from html import escape as _h
from pathlib import Path
from typing import Optional

import yaml

REPO = Path(__file__).resolve().parent.parent
SOURCES = REPO / "_sources"
DEFAULT_OUT = REPO / "cdif-uml-model"

# Reuse the CSS the XMI-based pipeline writes to _static/style.css; we don't
# duplicate styling here. If _static/style.css is missing, we write a tiny
# fallback (the XMI pipeline will overwrite it on its next run).
_FALLBACK_CSS = """\
body { font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
       margin: 0; padding: 0; color: #222; background: #fafafa; }
header { background: #2c3e50; color: white; padding: 1rem 2rem; }
header h1 { margin: 0; font-size: 1.4rem; font-weight: 500; }
header a { color: white; text-decoration: none; }
nav.breadcrumb { font-size: 0.9rem; opacity: 0.85; margin-top: 0.3rem; }
nav.breadcrumb a { color: #cfe2f3; }
main { max-width: 1100px; margin: 2rem auto; padding: 0 2rem; }
h1.classname { font-size: 1.9rem; margin: 0 0 0.5rem 0; }
.fqn { color: #666; font-size: 0.9rem; margin-bottom: 1rem; font-family: monospace; }
h2 { font-size: 1.2rem; color: #2c3e50; border-bottom: 1px solid #ddd;
     padding-bottom: 0.3rem; margin-top: 2rem; }
.definition { background: white; padding: 1rem; border-left: 3px solid #2c3e50; }
.union-note { background: #fdf6e3; padding: 0.8rem 1rem; margin-top: 0.6rem;
              border-left: 3px solid #d4a017; }
table { width: 100%; border-collapse: collapse; background: white; }
th, td { padding: 0.6rem 0.8rem; text-align: left; border-bottom: 1px solid #eee;
         vertical-align: top; }
th { background: #f4f4f4; font-weight: 600; font-size: 0.9rem; color: #555; }
td.name { font-family: monospace; font-weight: 600; white-space: nowrap; }
td.type { font-family: monospace; color: #06c; }
td.mult { font-family: monospace; color: #999; white-space: nowrap; }
a.classlink { color: #06c; text-decoration: none; }
a.classlink:hover { text-decoration: underline; }
ul.classlist { list-style: none; padding: 0;
               display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
               gap: 0.5rem; }
ul.classlist li { background: white; padding: 0.6rem 0.8rem;
                  border: 1px solid #eee; border-radius: 4px; }
ul.classlist a { color: #06c; text-decoration: none; font-family: monospace;
                 font-weight: 600; }
.empty { color: #999; font-style: italic; }
"""


# ---------------------------------------------------------------------------
# Internal model
# ---------------------------------------------------------------------------

@dataclass
class Attribute:
    name: str
    type_label: str          # 'String' | 'Integer' | 'Real' | 'Boolean' | class name | union expression
    type_link: Optional[str] = None  # relative URL to the class page, or None
    cross_profile_ref: Optional[str] = None  # e.g. '../../OtherProfile/Classes/X.html'
    lower: int = 0
    upper: int = 1   # -1 means *
    doc: str = ""
    raw_property_name: str = ""  # e.g. 'schema:variableMeasured' for display


@dataclass
class Association:
    name: str
    target_class: str
    target_link: Optional[str] = None
    cross_profile_ref: Optional[str] = None
    lower: int = 0
    upper: int = -1
    doc: str = ""
    aggregation: Optional[str] = None  # 'composite', 'shared'


@dataclass
class ModelClass:
    name: str
    kind: str               # 'class' | 'datatype' | 'enumeration'
    doc: str = ""
    attributes: list[Attribute] = field(default_factory=list)
    associations: list[Association] = field(default_factory=list)
    is_main: bool = False   # the synthesized top-level class


# ---------------------------------------------------------------------------
# Schema parsing
# ---------------------------------------------------------------------------

PRIMITIVE_MAP = {
    "string": "String",
    "integer": "Integer",
    "number": "Real",
    "boolean": "Boolean",
    "null": "Null",
}


def _strip_prefix(prop_name: str) -> str:
    """schema:foo -> foo; @id -> identifier; @type -> type."""
    if prop_name == "@id":
        return "identifier"
    if prop_name == "@type":
        return "type"
    if prop_name == "@context":
        return "context"
    if ":" in prop_name:
        return prop_name.split(":", 1)[1]
    return prop_name


def _multiplicity_of(prop_schema: dict, required: bool) -> tuple[int, int]:
    """Return (lower, upper) for a JSON Schema property.
    upper = -1 means unbounded (*). lower = 0 unless `required`."""
    t = prop_schema.get("type")
    is_array = t == "array" or (isinstance(t, list) and "array" in t)
    if is_array:
        lo = prop_schema.get("minItems", 1 if required else 0)
        up = prop_schema.get("maxItems", -1)
        return (max(0, int(lo)), int(up) if up is not None and up != "*" else -1)
    return (1 if required else 0, 1)


def _doc_of(s: dict) -> str:
    return (s.get("description") or "").strip()


def _ref_to_name(ref: str) -> tuple[str, str]:
    """Given a $ref like '#/$defs/Foo' or '../../X/Y/schema.yaml' or
    '../../X/Y/schema.yaml#/$defs/Foo', return (kind, name) where kind is
    'local' or 'external' and name is the class name (last fragment piece for
    local; the basename of the parent dir for external schema.yaml).
    """
    if ref.startswith("#/$defs/"):
        return ("local", ref.split("/")[-1])
    if "#/$defs/" in ref:
        path, _, frag = ref.partition("#/$defs/")
        return ("external", frag.split("/")[-1])
    # ../../X/Y/schema.yaml -> use the parent dir (Y) as the class hint
    p = ref.split("#", 1)[0].rstrip("/")
    base = p.rsplit("/", 1)[-1]
    if base.endswith(".yaml") or base.endswith(".json"):
        # Use the directory name as the class hint
        parts = p.rsplit("/", 2)
        if len(parts) >= 2:
            base = parts[-2]
    # Drop leading lowercase prefix conventions: variableMeasured -> VariableMeasured
    return ("external", base[0].upper() + base[1:] if base else base)


# ---------------------------------------------------------------------------
# Type-label extraction
# ---------------------------------------------------------------------------

@dataclass
class TypeInfo:
    label: str               # display label, e.g. 'String', 'Concept', 'String | LanguageTaggedValue'
    targets: list[str] = field(default_factory=list)   # class names referenced
    external_targets: list[tuple[str, str]] = field(default_factory=list)
    # ^ list of (class_name, original_ref_path)


def _type_info(prop_schema: dict, _depth: int = 0) -> TypeInfo:
    """Reduce a JSON-schema property fragment to a single display label +
    list of class targets. Handles primitives, $ref, anyOf, oneOf, and the
    'type: array of X' wrapper."""
    if not isinstance(prop_schema, dict):
        return TypeInfo(label="any")

    # $ref direct
    if "$ref" in prop_schema:
        kind, name = _ref_to_name(prop_schema["$ref"])
        ti = TypeInfo(label=name)
        if kind == "local":
            ti.targets.append(name)
        else:
            ti.external_targets.append((name, prop_schema["$ref"]))
        return ti

    # anyOf / oneOf -> union label
    for k in ("anyOf", "oneOf"):
        if k in prop_schema and isinstance(prop_schema[k], list) and _depth < 4:
            parts = [_type_info(b, _depth + 1) for b in prop_schema[k]]
            labels = []
            seen = set()
            for p in parts:
                if p.label and p.label not in seen:
                    labels.append(p.label)
                    seen.add(p.label)
            ti = TypeInfo(label=" | ".join(labels) if labels else "any")
            for p in parts:
                ti.targets.extend(p.targets)
                ti.external_targets.extend(p.external_targets)
            return ti

    t = prop_schema.get("type")
    if isinstance(t, list):
        # Type union like ['string','number']
        labels = [PRIMITIVE_MAP.get(x, x) for x in t]
        return TypeInfo(label=" | ".join(labels))

    if t == "array":
        item_ti = _type_info(prop_schema.get("items", {}), _depth + 1)
        return TypeInfo(label=item_ti.label, targets=item_ti.targets,
                        external_targets=item_ti.external_targets)

    if isinstance(t, str):
        if t == "object":
            # Inline anonymous object; we just label as 'Object' (these are
            # typically references via @id sub-property, not full classes)
            if set(prop_schema.get("properties", {}).keys()) == {"@id"}:
                return TypeInfo(label="@id-ref")
            return TypeInfo(label="Object")
        return TypeInfo(label=PRIMITIVE_MAP.get(t, t))

    if "const" in prop_schema:
        return TypeInfo(label=f"const \"{prop_schema['const']}\"")

    return TypeInfo(label="any")


# ---------------------------------------------------------------------------
# Schema -> model
# ---------------------------------------------------------------------------

def _required_set(schema: dict) -> set[str]:
    return set(schema.get("required") or [])


def _build_class_from_object(name: str, obj_schema: dict, *, is_main: bool,
                              local_def_names: set[str]) -> ModelClass:
    """Build a ModelClass from a JSON Schema object fragment."""
    cls = ModelClass(name=name, kind="class", doc=_doc_of(obj_schema),
                     is_main=is_main)
    required = _required_set(obj_schema)
    for raw_name, prop in (obj_schema.get("properties") or {}).items():
        if raw_name in ("@context",):
            # @context is a JSON-LD plumbing slot; skip from UML
            continue
        ti = _type_info(prop)
        lo, up = _multiplicity_of(prop, raw_name in required)
        # Distinguish "association" (reference to a class in our model OR
        # external) vs "attribute" (primitive / string / object label).
        is_assoc = bool(ti.targets) or bool(ti.external_targets)
        clean_name = _strip_prefix(raw_name)
        if is_assoc:
            target = (ti.targets or [t for t, _ in ti.external_targets])[0]
            cls.associations.append(Association(
                name=clean_name,
                target_class=target,
                lower=lo, upper=up,
                doc=(prop.get("description") or "").strip(),
            ))
        else:
            cls.attributes.append(Attribute(
                name=clean_name,
                type_label=ti.label,
                lower=lo, upper=up,
                doc=(prop.get("description") or "").strip(),
                raw_property_name=raw_name,
            ))
    return cls


def _looks_value_typed(obj_schema: dict) -> bool:
    """A $def with @value/@language only, or no @id property, is treated as a
    UML DataType (no independent identity)."""
    props = set((obj_schema.get("properties") or {}).keys())
    if {"@value"} & props:
        return True
    if "@id" not in props and "identifier" not in props:
        # Heuristic: nested-value-object pattern
        return False
    return False


def _infer_main_class_name(schema: dict, override: Optional[str]) -> str:
    """Pick a name for the synthesized top-level class. Priority:
       1. CLI --class-name override
       2. @type 'contains.const' value, with the prefix stripped
       3. Schema title (sanitized)
       4. 'Root'."""
    if override:
        return override
    type_prop = (schema.get("properties") or {}).get("@type") or {}
    contains = type_prop.get("contains") or {}
    const = contains.get("const")
    if isinstance(const, str):
        return _strip_prefix(const)[0].upper() + _strip_prefix(const)[1:]
    title = (schema.get("title") or "").strip()
    if title:
        # Take the last word, drop spaces and 'CDIF' prefix words
        words = [w for w in re.split(r"\s+", title) if w and w.lower() != "cdif"]
        if words:
            return "".join(w[0].upper() + w[1:] for w in words)
    return "Root"


def build_model(schema: dict, main_class_name: str) -> list[ModelClass]:
    """Build a list of ModelClass from a parsed JSON schema."""
    defs = schema.get("$defs") or {}
    local_def_names = set(defs.keys())

    classes: list[ModelClass] = []
    # Main class from top-level
    main_cls = _build_class_from_object(main_class_name, schema, is_main=True,
                                        local_def_names=local_def_names)
    classes.append(main_cls)

    # $defs: each becomes a class (or DataType)
    for def_name, def_schema in defs.items():
        if not isinstance(def_schema, dict):
            continue
        cls = _build_class_from_object(def_name, def_schema, is_main=False,
                                       local_def_names=local_def_names)
        if _looks_value_typed(def_schema):
            cls.kind = "datatype"
        classes.append(cls)
    return classes


# ---------------------------------------------------------------------------
# PlantUML emission
# ---------------------------------------------------------------------------

# Match the colors used by the XMI-based pipeline so the two page sets look
# visually consistent.
_PUML_LOCAL_COLOR = "#FEFECE"   # classes owned by this module
_PUML_CROSS_COLOR = "#D6EAF8"   # classes defined in other profiles
_PUML_DATATYPE_COLOR = "#FAE5D3"  # datatypes / value objects

_PUML_HEADER = (
    "hide circle\n"
    "hide empty members\n"
    "skinparam shadowing false\n"
    "skinparam ArrowThickness 1.2\n"
    "skinparam class {\n"
    "  ArrowColor #404040\n"
    "  BorderColor #404040\n"
    "  FontSize 12\n"
    "}\n"
)


def _puml_class_decl(name: str, color: str, *, stereotype: str = "",
                     attributes: Optional[list["Attribute"]] = None) -> str:
    """Render a single PlantUML class block."""
    head = f'class "{name}" as {name}'
    if stereotype:
        head += f" <<{stereotype}>>"
    head += f" {color}"
    if not attributes:
        return head + "\n"
    body_lines = []
    for a in attributes:
        mult = _mult_str(a.lower, a.upper)
        body_lines.append(f"  +{a.name} : {a.type_label} {mult}")
    return head + " {\n" + "\n".join(body_lines) + "\n}\n"


def _puml_for_class(cls: "ModelClass", classes_by_name: dict[str, "ModelClass"],
                    cross_registry: dict[str, str], profile_name: str) -> str:
    """PlantUML source for a single-class detail diagram: the focal class
    plus every class it references via association (and via attribute when
    that attribute's type label happens to be another local class)."""
    lines = [f"@startuml", f"title {cls.name}", _PUML_HEADER]

    focal_color = _PUML_DATATYPE_COLOR if cls.kind == "datatype" else _PUML_LOCAL_COLOR
    lines.append(_puml_class_decl(
        cls.name, focal_color,
        stereotype="dataType" if cls.kind == "datatype" else "",
        attributes=cls.attributes,
    ))

    # Targets referenced by this class
    seen = {cls.name}
    edges = []
    for a in cls.associations:
        tgt = a.target_class
        if tgt and tgt not in seen:
            seen.add(tgt)
            if tgt in classes_by_name:
                tgt_cls = classes_by_name[tgt]
                color = (_PUML_DATATYPE_COLOR if tgt_cls.kind == "datatype"
                         else _PUML_LOCAL_COLOR)
                stereo = "dataType" if tgt_cls.kind == "datatype" else ""
            else:
                color = _PUML_CROSS_COLOR
                stereo = ""
            lines.append(_puml_class_decl(tgt, color, stereotype=stereo))
        upper = "*" if a.upper == -1 else str(a.upper)
        mult = f'"{a.lower}..{upper}"' if a.lower != a.upper else f'"{a.lower}"'
        arrow = "*--" if a.aggregation == "composite" else "-->"
        edges.append(f"{cls.name} {arrow} {mult} {tgt} : {a.name}")
    lines.extend(edges)
    lines.append("@enduml\n")
    return "\n".join(lines)


def _puml_overview(profile_name: str, classes: list["ModelClass"]) -> str:
    """PlantUML source for the module-level overview diagram."""
    by_name = {c.name: c for c in classes}
    lines = [f"@startuml", f"title {profile_name} — overview", _PUML_HEADER]

    for c in classes:
        color = _PUML_DATATYPE_COLOR if c.kind == "datatype" else _PUML_LOCAL_COLOR
        stereo = "dataType" if c.kind == "datatype" else ""
        lines.append(_puml_class_decl(c.name, color, stereotype=stereo))
    # Cross-profile targets referenced by any association — declare so the
    # arrow has a typed endpoint.
    cross_seen = set()
    for c in classes:
        for a in c.associations:
            tgt = a.target_class
            if tgt and tgt not in by_name and tgt not in cross_seen:
                cross_seen.add(tgt)
                lines.append(_puml_class_decl(tgt, _PUML_CROSS_COLOR))
    # Edges
    for c in classes:
        for a in c.associations:
            tgt = a.target_class
            if not tgt:
                continue
            upper = "*" if a.upper == -1 else str(a.upper)
            mult = f'"{a.lower}..{upper}"' if a.lower != a.upper else f'"{a.lower}"'
            arrow = "*--" if a.aggregation == "composite" else "-->"
            lines.append(f"{c.name} {arrow} {mult} {tgt} : {a.name}")
    lines.append("@enduml\n")
    return "\n".join(lines)


def _render_plantuml(pu_dir: Path, plantuml_jar: Path, java_exe: Path) -> int:
    """Run PlantUML on every .pu file under `pu_dir`, producing .svg siblings.
    Returns the number of SVGs produced. PlantUML occasionally exits non-zero
    on warnings even when every .pu rendered successfully, so we use the
    actual SVG count as the success signal and only log stderr if it's
    non-empty."""
    import subprocess
    pu_files = list(pu_dir.rglob("*.pu"))
    if not pu_files:
        return 0
    cmd = [str(java_exe), "-jar", str(plantuml_jar), "-tsvg",
           "-charset", "UTF-8",
           *[str(p) for p in pu_files]]
    result = subprocess.run(cmd, capture_output=True, text=True)
    n_svgs = sum(1 for p in pu_dir.rglob("*.svg"))
    if n_svgs < len(pu_files):
        sys.stderr.write(
            f"plantuml: rendered {n_svgs}/{len(pu_files)} .pu files; "
            f"stderr:\n{result.stderr[:1000]}\n"
        )
    return n_svgs


def _diagram_section(svg_filename: str) -> str:
    """HTML for the embedded SVG class diagram. Matches the markup the XMI
    pipeline emits so the same _static/diagram.js interactive behavior
    applies (zoom / pan / copy)."""
    return (
        '<h2>Diagram</h2>'
        f'<div class="diagram" data-diagram data-svg="{svg_filename}">'
        '<div class="diagram-viewport">'
        '<div class="diagram-stage">'
        f'<object data="{svg_filename}" type="image/svg+xml"></object>'
        '</div></div></div>'
    )


# ---------------------------------------------------------------------------
# HTML emission
# ---------------------------------------------------------------------------

def _mult_str(lo: int, up: int) -> str:
    upper = "*" if up == -1 else str(up)
    if lo == up:
        return f"[{lo}]"
    return f"[{lo}..{upper}]"


def _class_link(target: str, in_classes: set[str], in_datatypes: set[str],
                cross_registry: dict[str, str],
                profile_name: str) -> str:
    """Return an HTML link to a class. `target` may be a local class name,
    a class name in another profile (via cross_registry), or unknown."""
    # Local
    if target in in_classes:
        return f'<a class="classlink" href="../Classes/{target}.html">{_h(target)}</a>'
    if target in in_datatypes:
        return f'<a class="classlink" href="../DataTypes/{target}.html">{_h(target)}</a>'
    # Cross-profile
    if target in cross_registry:
        other = cross_registry[target]
        if other != profile_name:
            return (f'<a class="classlink" href="../../{other}/Classes/{target}.html" '
                    f'title="in {other}">{_h(target)} &#x2197;</a>')
    return _h(target)


def _shell(title: str, breadcrumb: list[tuple[str, str]], body: str,
           depth: int) -> str:
    """depth=0 root index, depth=1 profile index, depth=2 a class page."""
    prefix = "../" * depth
    crumbs = " &rsaquo; ".join(
        f'<a href="{prefix}{href}">{_h(label)}</a>' if href else _h(label)
        for label, href in breadcrumb
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{_h(title)}</title>
  <link rel="stylesheet" href="{prefix}_static/style.css">
</head>
<body>
<header>
  <h1><a href="{prefix}index.html">{_h(title)}</a></h1>
  <nav class="breadcrumb">{crumbs}</nav>
</header>
<main>{body}</main>
</body>
</html>
"""


def _attr_table(attrs: list[Attribute]) -> str:
    if not attrs:
        return '<p class="empty">No attributes.</p>'
    rows = []
    for a in attrs:
        rows.append(
            f'<tr><td class="name">{_h(a.name)}</td>'
            f'<td class="type">{_h(a.type_label)}</td>'
            f'<td class="mult">{_mult_str(a.lower, a.upper)}</td>'
            f'<td class="doc">{_h(a.doc)}</td></tr>'
        )
    return ('<table><thead><tr><th>Name</th><th>Type</th><th>Multiplicity</th>'
            '<th>Description</th></tr></thead><tbody>'
            + "".join(rows) + '</tbody></table>')


def _assoc_table(assocs: list[Association], in_classes: set[str],
                 in_datatypes: set[str], cross_registry: dict[str, str],
                 profile_name: str) -> str:
    if not assocs:
        return '<p class="empty">No associations.</p>'
    rows = []
    for a in assocs:
        tgt_html = _class_link(a.target_class, in_classes, in_datatypes,
                                cross_registry, profile_name)
        rows.append(
            f'<tr><td class="name">{_h(a.name)}</td>'
            f'<td class="type">{tgt_html}</td>'
            f'<td class="mult">{_mult_str(a.lower, a.upper)}</td>'
            f'<td class="doc">{_h(a.doc)}</td></tr>'
        )
    return ('<table><thead><tr><th>Role</th><th>Target</th>'
            '<th>Multiplicity</th><th>Description</th></tr></thead><tbody>'
            + "".join(rows) + '</tbody></table>')


def emit(out_root: Path, profile_name: str, classes: list[ModelClass],
         module_title: str, module_subtitle: str,
         cross_registry: Optional[dict[str, str]] = None,
         plantuml_jar: Optional[Path] = None,
         java_exe: Optional[Path] = None) -> None:
    cross_registry = cross_registry or {}
    profile_dir = out_root / profile_name
    (profile_dir / "Classes").mkdir(parents=True, exist_ok=True)
    (profile_dir / "DataTypes").mkdir(parents=True, exist_ok=True)

    # Ensure shared CSS exists (don't overwrite the XMI pipeline's richer copy
    # if it's already there; only write a minimal fallback if missing).
    static_dir = out_root / "_static"
    static_dir.mkdir(exist_ok=True)
    css_path = static_dir / "style.css"
    if not css_path.exists():
        css_path.write_text(_FALLBACK_CSS, encoding="utf-8")

    cls_by_kind = {"class": [], "datatype": [], "enumeration": []}
    for c in classes:
        cls_by_kind[c.kind].append(c)

    in_classes = {c.name for c in cls_by_kind["class"]}
    in_datatypes = {c.name for c in cls_by_kind["datatype"]
                    + cls_by_kind["enumeration"]}
    classes_by_name = {c.name: c for c in classes}

    # Sweep stale .pu/.svg in the per-class folders before regenerating, so
    # diagrams for classes that have been removed don't linger.
    for folder in ("Classes", "DataTypes"):
        for stale in (profile_dir / folder).iterdir() if (profile_dir / folder).exists() else ():
            if stale.is_file() and stale.suffix in {".pu", ".svg"}:
                stale.unlink()

    # Plant UML emission: write per-class .pu + overview.pu. If PlantUML jar +
    # Java are available, render to .svg in place. Diagram section is added
    # to HTML pages whenever the .svg exists on disk.
    diagram_available = {}  # class_name -> svg_filename (e.g. "Foo.svg")
    overview_svg = None
    if classes:
        for c in classes:
            folder = "Classes" if c.kind == "class" else "DataTypes"
            (profile_dir / folder / f"{c.name}.pu").write_text(
                _puml_for_class(c, classes_by_name, cross_registry, profile_name),
                encoding="utf-8",
            )
        (profile_dir / "index.pu").write_text(
            _puml_overview(profile_name, classes),
            encoding="utf-8",
        )

        if plantuml_jar and java_exe and plantuml_jar.exists() and java_exe.exists():
            n = _render_plantuml(profile_dir, plantuml_jar, java_exe)
            print(f"  Rendered {n} SVGs via {plantuml_jar.name}")
            for c in classes:
                folder = "Classes" if c.kind == "class" else "DataTypes"
                if (profile_dir / folder / f"{c.name}.svg").exists():
                    diagram_available[c.name] = f"{c.name}.svg"
            if (profile_dir / "index.svg").exists():
                overview_svg = "index.svg"

    # Per-class pages
    for c in classes:
        folder = "Classes" if c.kind == "class" else "DataTypes"
        stereotype = "" if c.kind == "class" else (
            f'<span class="stereotype">&laquo;{c.kind}&raquo;</span>'
        )
        diagram_html = (
            _diagram_section(diagram_available[c.name])
            if c.name in diagram_available else ""
        )
        body = (
            f'<h1 class="classname">{_h(c.name)}{stereotype}</h1>'
            f'<p class="fqn">{_h(profile_name)}::{folder}::{_h(c.name)}</p>'
            f'<h2>Definition</h2>'
            f'<div class="definition">{_h(c.doc) or "<em>(no description)</em>"}</div>'
            f'{diagram_html}'
            f'<h2>Attributes</h2>{_attr_table(c.attributes)}'
            f'<h2>Associations</h2>{_assoc_table(c.associations, in_classes, in_datatypes, cross_registry, profile_name)}'
        )
        breadcrumb = [
            ("Profiles", "../../index.html"),
            (profile_name, "../index.html"),
            (folder, f"../{folder}/index.html"),
            (c.name, ""),
        ]
        html = _shell(profile_name, breadcrumb, body, depth=2)
        (profile_dir / folder / f"{c.name}.html").write_text(html, encoding="utf-8")

    # Folder index pages (Classes and DataTypes)
    for folder, items in (("Classes", cls_by_kind["class"]),
                          ("DataTypes", cls_by_kind["datatype"]
                                        + cls_by_kind["enumeration"])):
        if not items:
            (profile_dir / folder / "index.html").write_text(
                _shell(profile_name,
                       [("Profiles", "../../index.html"),
                        (profile_name, "../index.html"),
                        (folder, "")],
                       f'<h1 class="classname">{_h(folder)}</h1>'
                       '<p class="empty">(none)</p>',
                       depth=2),
                encoding="utf-8")
            continue
        lis = "".join(
            f'<li><a href="{c.name}.html"><strong>{_h(c.name)}</strong></a></li>'
            for c in sorted(items, key=lambda x: x.name)
        )
        html = _shell(profile_name,
                      [("Profiles", "../../index.html"),
                       (profile_name, "../index.html"),
                       (folder, "")],
                      f'<h1 class="classname">{_h(folder)}</h1>'
                      f'<ul class="classlist">{lis}</ul>',
                      depth=2)
        (profile_dir / folder / "index.html").write_text(html, encoding="utf-8")

    # Profile index page
    cls_lis = "".join(
        f'<li><a href="Classes/{c.name}.html"><strong>{_h(c.name)}</strong></a></li>'
        for c in sorted(cls_by_kind["class"], key=lambda x: x.name)
    ) or '<li class="empty">(no classes)</li>'
    dt_lis = "".join(
        f'<li><a href="DataTypes/{c.name}.html"><strong>{_h(c.name)}</strong></a></li>'
        for c in sorted(cls_by_kind["datatype"] + cls_by_kind["enumeration"],
                        key=lambda x: x.name)
    ) or '<li class="empty">(none)</li>'
    overview_html = (
        f'<h2>Model overview</h2>'
        f'<div class="diagram" data-diagram data-svg="{overview_svg}">'
        f'<div class="diagram-viewport">'
        f'<div class="diagram-stage">'
        f'<object data="{overview_svg}" type="image/svg+xml"></object>'
        f'</div></div></div>'
    ) if overview_svg else ''
    body = (
        f'<h1 class="classname">{_h(module_title)}</h1>'
        f'<p>{_h(module_subtitle)}</p>'
        f'{overview_html}'
        f'<h2>Classes</h2><ul class="classlist">{cls_lis}</ul>'
        f'<h2>DataTypes &amp; Enumerations</h2><ul class="classlist">{dt_lis}</ul>'
    )
    html = _shell(profile_name,
                  [("Profiles", "../index.html"), (profile_name, "")],
                  body, depth=1)
    (profile_dir / "index.html").write_text(html, encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _resolve_schema_path(module: str) -> Path:
    p = Path(module)
    if p.is_file():
        return p.resolve()
    candidate = SOURCES / "profiles" / "cdifProfile" / module / "schema.yaml"
    if candidate.is_file():
        return candidate
    sys.exit(f"Could not find schema for module '{module}'. Tried: {candidate}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("module", help="Module name (e.g. cdifConceptScheme) "
                                    "or explicit schema.yaml path")
    ap.add_argument("--out-dir", default=str(DEFAULT_OUT),
                    help=f"Output root (default: {DEFAULT_OUT.relative_to(REPO)})")
    ap.add_argument("--uml-name", default=None,
                    help="Override the profile dir name (e.g. 'cdifDiscovery'). "
                         "Default: same as the module name argument.")
    ap.add_argument("--class-name", default=None,
                    help="Override the synthesized main class name. "
                         "Default: derived from @type.contains.const or title.")
    ap.add_argument("--plantuml-jar", default=str(REPO / "tools" / "plantuml.jar"),
                    help="Path to plantuml.jar (default: tools/plantuml.jar). "
                         "If the jar or Java is missing, .pu files are still "
                         "written but no SVGs are rendered and HTML omits the "
                         "Diagram section.")
    ap.add_argument("--java-exe",
                    default=r"C:\Program Files\Eclipse Adoptium\jdk-21.0.11.10-hotspot\bin\java.exe",
                    help="Java executable (default matches build-docs.ps1).")
    ap.add_argument("--no-diagrams", action="store_true",
                    help="Skip PlantUML emission entirely.")
    args = ap.parse_args()

    schema_path = _resolve_schema_path(args.module)
    schema = yaml.safe_load(schema_path.read_text(encoding="utf-8"))
    if not isinstance(schema, dict):
        sys.exit(f"Schema at {schema_path} is not a JSON object.")

    main_name = _infer_main_class_name(schema, args.class_name)
    classes = build_model(schema, main_name)

    profile_name = args.uml_name or Path(args.module).name.replace(".yaml", "")
    out_root = Path(args.out_dir).resolve()

    # Cross-profile registry, if any (written by the XMI pipeline).
    cross = {}
    reg = out_root / "_registry.json"
    if reg.exists():
        try:
            cross = json.loads(reg.read_text(encoding="utf-8"))
        except Exception:
            cross = {}

    title = schema.get("title") or profile_name
    subtitle = schema.get("description") or ""

    pj = Path(args.plantuml_jar) if (args.plantuml_jar and not args.no_diagrams) else None
    je = Path(args.java_exe) if (args.java_exe and not args.no_diagrams) else None

    emit(out_root, profile_name, classes, title, subtitle,
         cross_registry=cross, plantuml_jar=pj, java_exe=je)
    print(f"Wrote {profile_name}/ ({len(classes)} classes) under {out_root}")


if __name__ == "__main__":
    main()
