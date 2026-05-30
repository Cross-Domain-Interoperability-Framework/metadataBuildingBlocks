#!/usr/bin/env python3
"""Generate a draft CDIF Implementation Guide markdown from a resolved JSON Schema.

Output mirrors the property-by-property style of the existing IGs (header +
per-class section + per-property cardinality/content/description). Intended
as a starting point for hand-editing; descriptions are extracted verbatim
from the schema's `description` fields.

Usage:
    python tools/generate_ig_draft.py <profile-name> <schema-path> [-o out.md]

Example:
    python tools/generate_ig_draft.py cdifManifest \\
        ../profile-manifest/cdifManifestStructuredSchema.json \\
        -o ../profile-manifest/CDIFManifestImplementationGuide.md
"""
import argparse
import json
import re
from pathlib import Path


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def content_type(prop: dict) -> str:
    """Best-effort content-type description for a property."""
    if "$ref" in prop:
        return f"[object reference]({prop['$ref']})"
    if "enum" in prop:
        opts = " | ".join(f'`"{v}"`' for v in prop["enum"])
        return f"string ({opts})"
    if "anyOf" in prop or "oneOf" in prop:
        return "one of: " + ", ".join(content_type(opt) for opt in (prop.get("anyOf") or prop.get("oneOf")))
    t = prop.get("type")
    if t == "array":
        items = prop.get("items", {})
        return f"array of {content_type(items)}" if items else "array"
    if t == "object":
        return "object"
    if isinstance(t, list):
        return " or ".join(t)
    if t:
        return t
    return "—"


def cardinality(name: str, required_list: list) -> str:
    return "Required" if name in (required_list or []) else "Optional"


def emit_property(name: str, prop: dict, required: list, level: int = 3) -> list[str]:
    out = [f"{'#' * level} {name}", ""]
    out.append(f"- **Cardinality:** {cardinality(name, required)}")
    out.append(f"- **Content:** {content_type(prop)}")
    desc = (prop.get("description") or "").strip()
    if desc:
        # Collapse multi-line descriptions into a single paragraph
        desc = re.sub(r"\s+", " ", desc)
        out.append(f"- **Description:** {desc}")
    out.append("")
    return out


def emit_class(name: str, schema: dict) -> list[str]:
    out = [f"## {name} {{#sec-{slug(name)}}}", ""]
    if (desc := (schema.get("description") or "").strip()):
        desc = re.sub(r"\s+", " ", desc)
        out.append(desc)
        out.append("")
    props = schema.get("properties", {})
    required = schema.get("required", []) or []
    for pname, pschema in props.items():
        out.extend(emit_property(pname, pschema, required))
    return out


def emit_header(profile_name: str, schema_filename: str, shacl_filename: str,
                source_path: str, conformance_uri: str, profile_title: str) -> list[str]:
    return [
        f"# {profile_title} Profile — Implementation Guide",
        "",
        "> **Draft.** This guide was auto-generated from the StructuredSchema. "
        "Edit freely — descriptions, ordering, and the introductory prose should be "
        "curated by hand.",
        "",
        "# Purpose and scope",
        "",
        f"The **{profile_title} profile module** (`{profile_name}`) — see the source "
        f"register description for the module's purpose. *(Replace this stub paragraph "
        f"with a hand-written purpose statement.)*",
        "",
        "# Conformance",
        "",
        f"A resource conforms to the {profile_title} profile when its catalog record "
        "declares conformance to the profile identifier. The catalog record is carried "
        "on `schema:subjectOf` as a `dcat:CatalogRecord`:",
        "",
        "```json",
        '"schema:subjectOf": {',
        '  "@type": ["schema:CreativeWork", "dcat:CatalogRecord"],',
        '  "dcterms:conformsTo": [',
        f'    "{conformance_uri}"',
        "  ]",
        "}",
        "```",
        "",
        "Other properties added in this profile are optional; conformance requires only "
        "that the constraints in the JSON Schema and SHACL rules are satisfied.",
        "",
        "## Validation",
        "",
        "Two validators ship with this repository:",
        f"- **JSON Schema** — `{schema_filename}` (Draft 2020-12), generated from the source register.",
        f"- **SHACL** — `{shacl_filename}`, a self-contained shapes graph merged from every "
        "composing building block plus the profile-level shapes.",
        "",
        "```bash",
        "python FrameAndValidate.py examples/<file>.json --validate \\",
        f"  --schema {schema_filename} --frame <frame.jsonld>",
        "```",
        "",
        "Validation is **open-world**: properties not described by the profile are allowed.",
        "",
        "# Provenance of the artifacts",
        "",
        "The schema and SHACL files are generated from the canonical source register, "
        "[metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks):",
        "",
        f"- `{schema_filename}` ← `tools/resolve_schema.py {profile_name}`",
        f"- `{shacl_filename}` ← `tools/validate_shacl.py {profile_name} --emit-shapes`",
        "",
        f"Source profile directory: `{source_path}`.",
        "",
    ]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("profile_name", help="Short profile id, e.g. cdifManifest")
    ap.add_argument("schema_path", help="Path to <Name>StructuredSchema.json")
    ap.add_argument("--title", required=True, help="Human title, e.g. 'CDIF Manifest'")
    ap.add_argument("--shacl", required=True, help="Filename of the SHACL file, e.g. manifestRules.shacl")
    ap.add_argument("--source", required=True, help="Source dir, e.g. _sources/profiles/cdifProfile/cdifManifest/")
    ap.add_argument("--conformsTo", required=True, help="Profile conformance URI, e.g. https://w3id.org/cdif/manifest/1.0")
    ap.add_argument("-o", "--output", help="Output markdown file (default: stdout)")
    args = ap.parse_args()

    schema_path = Path(args.schema_path)
    schema = json.loads(schema_path.read_text(encoding="utf-8"))

    lines = []
    lines.extend(emit_header(args.profile_name, schema_path.name, args.shacl,
                             args.source, args.conformsTo, args.title))

    # Root-level properties (under the top-level "Dataset" class)
    if schema.get("properties"):
        lines.append(f"# Dataset Properties added by the {args.title} Profile")
        lines.append("")
        lines.extend(emit_class("schema:Dataset", schema))

    # $defs (sub-classes)
    if defs := schema.get("$defs"):
        lines.append("# Class Definitions")
        lines.append("")
        for cls_name, cls_schema in defs.items():
            if cls_name.startswith("$"):
                continue
            lines.extend(emit_class(cls_name, cls_schema))

    out = "\n".join(lines).rstrip() + "\n"

    if args.output:
        Path(args.output).write_text(out, encoding="utf-8")
        print(f"Wrote {Path(args.output)} ({len(out)} bytes)")
    else:
        print(out)


if __name__ == "__main__":
    main()
