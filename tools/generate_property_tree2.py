#!/usr/bin/env python3
"""
Generate propertyTree_2 worksheets from resolved JSON Schemas.

Walks a resolved schema and produces a spreadsheet tree following the CDIF
property-tree convention:

    col 0: root object type
    col 1: property (depth 0)
    col 2: options  (depth 0)
    col 3: property (depth 1)
    col 4: options  (depth 1)
    ...

Suffix conventions:
    -- string               literal string
    -- string(uri)          string with URI format
    -- string(date)         string with date format
    -- boolean              boolean
    -- number               number
    -- object reference     JSON-LD {@id: ...} reference
    -- object               nested object
    -- CHOICE               anyOf with mixed types
    [...]                   square brackets = array (0..* or 1..*)
"""

import io
import json
import os
import sys
import argparse
from pathlib import Path

import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill

MAX_DEPTH = 6
MAX_COLS = 2 + 2 * MAX_DEPTH  # object col + depth levels * 2


# ── helpers ──────────────────────────────────────────────────────────────

def get_type_contains(schema):
    """Return the @type contains value, if any."""
    tp = schema.get("properties", {}).get("@type", {})
    c = tp.get("contains", {})
    return c.get("const")


def is_id_only_object(schema):
    """True if this object schema is just {@id: string}."""
    if schema.get("type") != "object":
        return False
    props = set(schema.get("properties", {}).keys())
    return props <= {"@id"}


def is_lang_tagged_pattern(any_of):
    """Detect the string-or-language-tagged-value pattern."""
    has_string = False
    has_lang = False
    for item in any_of:
        if item.get("type") == "string":
            has_string = True
        elif item.get("type") == "object":
            pkeys = set(item.get("properties", {}).keys())
            if "@value" in pkeys and "@language" in pkeys:
                has_lang = True
        elif item.get("type") == "array":
            sub = item.get("items", {})
            if sub.get("type") == "object":
                pkeys = set(sub.get("properties", {}).keys())
                if "@value" in pkeys and "@language" in pkeys:
                    has_lang = True
            for s in sub.get("anyOf", []):
                if s.get("type") == "object":
                    pkeys = set(s.get("properties", {}).keys())
                    if "@value" in pkeys and "@language" in pkeys:
                        has_lang = True
    return has_string and has_lang


# Internal $defs of the schema currently being walked, for deref().
_DEFS = {}


def deref(schema, _seen=None):
    """Resolve an internal #/$defs/<name> $ref, preserving sibling keywords.

    resolve_schema.py resolves EXTERNAL refs into $defs but leaves the internal ones
    in place -- recursive types are left as cycles by design -- so a composite's
    resolvedSchema.json is full of {"$ref": "#/$defs/Identifier"}. Every function here
    keys on "type", which such a node does not carry, so before this existed they all
    classified as "unknown" (inside an anyOf) or fell through to the bare-name fallback.
    Measured 2026-11-12: 50 unknown cells in CoreDiscovery alone, and schema:identifier
    printing as an unexpanded CHOICE of unknown/string.

    A $ref chain is followed to its end. A cycle, or a name not in $defs, yields the
    sibling keywords alone: a cyclic type cannot be expanded into a finite tree, and
    the caller's own visited_types guard is what stops the recursive ones.
    """
    if not isinstance(schema, dict):
        return schema
    seen = set() if _seen is None else _seen
    while True:
        ref = schema.get("$ref")
        if not isinstance(ref, str) or not ref.startswith("#/$defs/"):
            return schema
        name = ref[len("#/$defs/"):]
        target = _DEFS.get(name)
        if name in seen or not isinstance(target, dict):
            return {k: v for k, v in schema.items() if k != "$ref"}
        seen.add(name)
        # Siblings win: a $ref's own description is more specific than the target's.
        schema = {**target, **{k: v for k, v in schema.items() if k != "$ref"}}


def merge_allof(schema, _depth=0):
    """Shallow-merge an allOf into one schema for display.

    allOf means every member applies, so the useful rendering for a property tree is
    the union of what the members contribute. The members here are a mix: object
    schemas carrying properties, pure constraint refinements carrying none
    (required / contains / if-then), and sometimes one member carrying the union that
    actually defines the value -- cdifComplete's schema:distribution is
    allOf[anyOf[...], required, required]. Measured 2026-11-12: 18 such properties
    across the six composites, schema:distribution, schema:variableMeasured,
    prov:wasGeneratedBy, dcterms:conformsTo and schema:measurementTechnique among
    them, every one printing as a bare name with no type and no children because
    emit_property had no allOf case and fell through to its fallback.

    This is a DISPLAY merge, not validation semantics: the first member to supply a
    keyword wins, and no attempt is made to intersect two unions. resolve_schema.py
    owns real allOf composition.
    """
    members = schema.get("allOf")
    if not members or _depth >= MAX_DEPTH:
        return schema

    merged = {k: v for k, v in schema.items() if k != "allOf"}
    props = dict(merged.get("properties", {}))
    required = list(merged.get("required", []))

    for member in members:
        member = deref(member)
        if "allOf" in member:
            member = merge_allof(member, _depth + 1)
        props.update(member.get("properties", {}))
        required.extend(r for r in member.get("required", [])
                        if r not in required)
        for key in ("type", "contains", "anyOf", "oneOf", "enum", "const",
                    "format", "items"):
            if key not in merged and key in member:
                merged[key] = member[key]

    if props:
        merged["properties"] = props
        merged.setdefault("type", "object")
    if required:
        merged["required"] = required
    return merged


def resolve_node(schema):
    """deref an internal $ref, then flatten an allOf -- the two shapes the walker
    cannot read directly. Applied wherever a schema node is about to be classified."""
    return merge_allof(deref(schema))


def expand_union(any_of, _depth=0):
    """Deref each member and splice nested anyOf/oneOf unions into one flat list.

    anyOf[anyOf[A, B], C] is the same set of permitted values as anyOf[A, B, C], and
    the shared $defs here nest exactly that way: cdifConceptOrTermOrString wraps
    cdifConceptOrTerm's own union, so once deref() resolved it the member arrived as
    {anyOf, title, description} with no "type" -- which classify_anyof had no case for,
    leaving 31 of the original 50 unknown cells in CoreDiscovery after derefing alone.

    Members are deduplicated: flattening can surface the same branch twice (a string
    arm present in both the inner and outer union), which would otherwise print as two
    identical option rows. Depth is bounded in case a union ever nests cyclically.
    """
    out = []
    for item in any_of:
        item = resolve_node(item)
        nested = item.get("anyOf", item.get("oneOf"))
        if (nested and item.get("type") is None and "enum" not in item
                and _depth < MAX_DEPTH):
            out.extend(expand_union(nested, _depth + 1))
        else:
            out.append(item)

    seen, unique = set(), []
    for item in out:
        key = json.dumps(item, sort_keys=True, default=str)
        if key not in seen:
            seen.add(key)
            unique.append(item)
    return unique


def classify_anyof(any_of):
    """Return a list of (kind, schema[, type_contains]) tuples."""
    options = []
    for item in any_of:
        t = item.get("type")
        if t == "string":
            if "enum" in item:
                options.append(("enum", item))
            else:
                fmt = item.get("format", "")
                options.append(("string", item))
        elif t in ("number", "integer"):
            options.append(("number", item))
        elif t == "boolean":
            options.append(("boolean", item))
        elif t == "array":
            options.append(("array", item))
        elif t == "object":
            if is_id_only_object(item):
                options.append(("object_reference", item))
            else:
                tc = get_type_contains(item)
                if tc:
                    options.append(("typed_object", item, tc))
                else:
                    options.append(("object", item))
        elif "enum" in item:
            options.append(("enum", item))
        else:
            options.append(("unknown", item))
    return options


def make_row():
    return [None] * MAX_COLS


def string_suffix(schema):
    fmt = schema.get("format", "")
    if fmt in ("uri", "iri", "uri-reference", "iri-reference"):
        return "string(uri)"
    if fmt == "date":
        return "string(date)"
    if fmt == "date-time":
        return "string(date-time)"
    return "string"


# ── main tree walker ─────────────────────────────────────────────────────

def emit_property(prop_name, prop_schema, depth, rows, visited_types):
    """Emit row(s) for one property."""
    if depth > MAX_DEPTH:
        return
    prop_col = 1 + 2 * depth
    opts_col = 2 + 2 * depth
    if prop_col >= MAX_COLS:
        return

    # Resolve before anything reads "type": a property may itself be a bare $ref
    # or an allOf composition.
    prop_schema = resolve_node(prop_schema)

    is_array = prop_schema.get("type") == "array"

    # ── @context ──
    if prop_name == "@context":
        row = make_row()
        row[prop_col] = "@context -- standard context"
        rows.append(row)
        return

    # ── @id ──
    if prop_name == "@id":
        row = make_row()
        row[prop_col] = "@id -- string(uri)"
        rows.append(row)
        return

    # ── @type ──
    if prop_name == "@type":
        contains = None
        c = prop_schema.get("contains", {})
        contains = c.get("const")
        row = make_row()
        if contains:
            row[prop_col] = f"@type -- [string](contains {contains})"
        else:
            row[prop_col] = "@type -- [string]"
        rows.append(row)
        return

    # ── effective schema (unwrap array) ──
    effective = resolve_node(prop_schema.get("items", {})) if is_array else prop_schema

    # ── type as array (e.g. ["string", "number"]) → CHOICE ──
    ptype = effective.get("type")
    if isinstance(ptype, list):
        bracket = "[CHOICE]" if is_array else "CHOICE"
        row = make_row()
        row[prop_col] = f"{prop_name} -- {bracket}"
        rows.append(row)
        # opts_col can be one past the last column when prop_col is the last one;
        # every other emitter guards this, and only deeper expansion made it
        # reachable here (IndexError at depth 6, 2026-11-12).
        if opts_col < MAX_COLS:
            for t in ptype:
                r = make_row()
                r[opts_col] = t
                rows.append(r)
        return

    # ── anyOf / oneOf ──
    any_of = effective.get("anyOf", effective.get("oneOf"))
    if any_of:
        any_of = expand_union(any_of)
    # If anyOf items are only constraint refinements (e.g. different 'required'
    # sets) and the schema already has a concrete 'type', skip the anyOf and
    # treat as the base type.
    if any_of and all(set(item.keys()) <= {"required", "if", "then", "else",
                                            "not", "description"}
                      for item in any_of):
        any_of = None

    if any_of:
        # language-tagged pattern → treat as simple string
        if is_lang_tagged_pattern(any_of):
            sfx = "[string]" if is_array else "string"
            row = make_row()
            row[prop_col] = f"{prop_name} -- {sfx}"
            rows.append(row)
            return

        options = classify_anyof(any_of)
        kind_set = set(o[0] for o in options)

        # all-string → simple string
        if kind_set <= {"string"}:
            sfx = "[string]" if is_array else "string"
            row = make_row()
            row[prop_col] = f"{prop_name} -- {sfx}"
            rows.append(row)
            return

        # all object-reference → simple ref
        if kind_set <= {"object_reference"}:
            sfx = "[object reference]" if is_array else "object reference"
            row = make_row()
            row[prop_col] = f"{prop_name} -- {sfx}"
            rows.append(row)
            return

        # genuine CHOICE
        bracket = "[CHOICE]" if is_array else "CHOICE"
        row = make_row()
        row[prop_col] = f"{prop_name} -- {bracket}"
        rows.append(row)

        for opt in options:
            emit_choice_option(opt, opts_col, depth, rows, visited_types)
        return

    # ── simple types ──
    ptype = effective.get("type")

    if ptype == "string":
        sfx = string_suffix(effective)
        if is_array:
            sfx = f"[{sfx}]"
        row = make_row()
        row[prop_col] = f"{prop_name} -- {sfx}"
        rows.append(row)
        return

    if ptype == "boolean":
        sfx = "[boolean]" if is_array else "boolean"
        row = make_row()
        row[prop_col] = f"{prop_name} -- {sfx}"
        rows.append(row)
        return

    if ptype in ("number", "integer"):
        sfx = "[number]" if is_array else "number"
        row = make_row()
        row[prop_col] = f"{prop_name} -- {sfx}"
        rows.append(row)
        return

    if "enum" in effective:
        vals = ", ".join(f'"{v}"' for v in effective["enum"])
        sfx = f"[enum]" if is_array else "enum"
        row = make_row()
        row[prop_col] = f"{prop_name} -- {sfx} -- {vals}"
        rows.append(row)
        return

    if ptype == "object":
        emit_object_property(prop_name, effective, is_array, depth, rows, visited_types)
        return

    # ── const ──
    if "const" in effective:
        row = make_row()
        row[prop_col] = f'{prop_name} -- const("{effective["const"]}")'
        rows.append(row)
        return

    # fallback
    row = make_row()
    row[prop_col] = f"{prop_name}"
    rows.append(row)


def emit_object_property(prop_name, schema, is_array, depth, rows, visited_types):
    """Emit rows for a property whose value is an object."""
    prop_col = 1 + 2 * depth
    opts_col = 2 + 2 * depth

    if is_id_only_object(schema):
        sfx = "[object reference]" if is_array else "object reference"
        row = make_row()
        row[prop_col] = f"{prop_name} -- {sfx}"
        rows.append(row)
        return

    tc = get_type_contains(schema)
    sfx = "[object]" if is_array else "object"

    row = make_row()
    row[prop_col] = f"{prop_name} -- {sfx}"
    if tc and opts_col < MAX_COLS:
        row[opts_col] = f"@type -- [string](contains {tc})"
    rows.append(row)

    # recursion guard
    if tc and tc in visited_types:
        return
    new_visited = visited_types | ({tc} if tc else set())

    # emit child properties
    if depth + 1 <= MAX_DEPTH:
        child_props = {k: v for k, v in schema.get("properties", {}).items()
                       if k != "@type"}
        for cname, cschema in child_props.items():
            emit_property(cname, cschema, depth + 1, rows, new_visited)


def emit_choice_option(opt, opts_col, depth, rows, visited_types):
    """Emit one option within a CHOICE."""
    if opts_col >= MAX_COLS:
        return

    kind = opt[0]
    item = opt[1]

    if kind == "string":
        fmt = item.get("format", "")
        label = f"string({fmt})" if fmt else "string"
        row = make_row()
        row[opts_col] = label
        rows.append(row)

    elif kind == "number":
        row = make_row()
        row[opts_col] = "number"
        rows.append(row)

    elif kind == "boolean":
        row = make_row()
        row[opts_col] = "boolean"
        rows.append(row)

    elif kind == "object_reference":
        row = make_row()
        row[opts_col] = "object reference"
        rows.append(row)

    elif kind == "enum":
        vals = ", ".join(f'"{v}"' for v in item.get("enum", []))
        row = make_row()
        row[opts_col] = f"enum -- {vals}"
        rows.append(row)

    elif kind == "typed_object":
        tc = opt[2]
        row = make_row()
        row[opts_col] = f"@type -- [string](contains {tc})"
        rows.append(row)

        if tc in visited_types:
            return
        new_visited = visited_types | {tc}

        if depth + 1 <= MAX_DEPTH:
            child_props = {k: v for k, v in item.get("properties", {}).items()
                           if k != "@type"}
            for cname, cschema in child_props.items():
                emit_property(cname, cschema, depth + 1, rows, new_visited)

    elif kind == "object":
        # untyped object — show its properties
        row = make_row()
        row[opts_col] = "object"
        rows.append(row)

        if depth + 1 <= MAX_DEPTH:
            child_props = {k: v for k, v in item.get("properties", {}).items()
                           if k != "@type"}
            for cname, cschema in child_props.items():
                emit_property(cname, cschema, depth + 1, rows, visited_types)

    elif kind == "array":
        # array option — language tagged etc; just show "array"
        row = make_row()
        row[opts_col] = "array"
        rows.append(row)

    else:
        row = make_row()
        row[opts_col] = str(kind)
        rows.append(row)


# ── top-level entry ──────────────────────────────────────────────────────

def generate_property_tree(resolved_schema_path):
    """Generate the full property tree rows from a resolved schema."""
    with open(resolved_schema_path, encoding="utf-8") as f:
        schema = json.load(f)

    global _DEFS
    _DEFS = schema.get("$defs", {}) or {}

    # determine root type
    tc = get_type_contains(schema)
    root_label = tc if tc else "root"

    # header
    header = make_row()
    for i in range(0, MAX_COLS, 2):
        if i == 0:
            header[i] = "object"
        else:
            header[i] = "options"
    for i in range(1, MAX_COLS, 2):
        header[i] = "property"

    rows = [header]

    # root object row
    root_row = make_row()
    root_row[0] = root_label
    rows.append(root_row)

    # walk all properties
    props = schema.get("properties", {})
    for pname, pschema in props.items():
        emit_property(pname, pschema, 0, rows, set())

    return rows


def write_worksheet(ws, rows):
    """Write rows to an openpyxl worksheet with formatting."""
    header_font = Font(bold=True)
    header_fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2",
                              fill_type="solid")
    wrap = Alignment(wrap_text=True, vertical="top")

    for r_idx, row_data in enumerate(rows, start=1):
        for c_idx, val in enumerate(row_data, start=1):
            cell = ws.cell(row=r_idx, column=c_idx, value=val)
            cell.alignment = wrap
            if r_idx == 1:
                cell.font = header_font
                cell.fill = header_fill

    # auto-width (rough estimate)
    for col_cells in ws.columns:
        max_len = 0
        col_letter = col_cells[0].column_letter
        for cell in col_cells:
            if cell.value:
                max_len = max(max_len, len(str(cell.value)))
        ws.column_dimensions[col_letter].width = min(max_len + 2, 60)


# ── CLI ──────────────────────────────────────────────────────────────────

def add_sheet_to_existing(xlsx_path, sheet_name, rows):
    """Add a worksheet to an existing xlsx file, replacing any sheet of that name."""
    # Read into memory rather than copying to a temp file: openpyxl keeps the source
    # archive open past wb.close(), so on Windows os.remove() of that copy raised
    # WinError 32 -- after wb.save() had already written the destination, leaving the
    # workbook modified and the run aborted partway through the target list.
    with open(xlsx_path, "rb") as f:
        buf = io.BytesIO(f.read())
    wb = openpyxl.load_workbook(buf)
    if sheet_name in wb.sheetnames:
        del wb[sheet_name]
    ws = wb.create_sheet(sheet_name)
    write_worksheet(ws, rows)
    wb.save(xlsx_path)
    wb.close()
    print(f"  Added '{sheet_name}' to {xlsx_path}")


def create_new_workbook(xlsx_path, sheet_name, rows):
    """Create a new xlsx file with one worksheet."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = sheet_name
    write_worksheet(ws, rows)
    wb.save(xlsx_path)
    wb.close()
    print(f"  Created {xlsx_path} with sheet '{sheet_name}'")


def discover_targets(composites_dir, selected="all"):
    """Composite profiles to generate for, derived from the tree rather than hardcoded.

    Every directory under cdifCompositeProfile that holds a resolvedSchema.json is a
    target. The workbook is found by globbing *_properties.xlsx in that directory --
    never by assuming <dirname>_properties.xlsx, because the two that exist are named
    CDIFDiscovery_properties.xlsx and CDIFDataDescriptionProfile_properties.xlsx. A
    name-derived path would miss them and create a duplicate alongside, leaving the
    real propertyTree_2 sheet stale. That is how this tool broke in 3c2f5291b9.
    """
    composites_dir = Path(composites_dir)
    if not composites_dir.is_dir():
        raise SystemExit(f"no composite profile directory at {composites_dir}")

    targets, skipped = [], []
    for d in sorted(p for p in composites_dir.iterdir() if p.is_dir()):
        if selected not in ("all", d.name):
            continue
        if not (d / "resolvedSchema.json").exists():
            skipped.append(d.name)
            continue
        books = sorted(d.glob("*_properties.xlsx"))
        if len(books) > 1:
            raise SystemExit(
                f"{d.name}: {len(books)} candidate workbooks "
                f"({', '.join(b.name for b in books)}) -- name one explicitly")
        targets.append({
            "name": d.name,
            "resolved": d / "resolvedSchema.json",
            "xlsx": books[0] if books else d / f"{d.name}_properties.xlsx",
            "existing": bool(books),
        })

    for name in skipped:
        print(f"  skipping {name}: no resolvedSchema.json")
    return targets


def main():
    parser = argparse.ArgumentParser(
        description="Generate propertyTree_2 worksheets from resolved schemas")
    # Deliberately no choices=: the valid values are the composite directory names,
    # and a hardcoded list is what went stale across two reorgs.
    parser.add_argument("--profile", default="all",
                        help="composite profile directory name, or 'all' (default)")
    args = parser.parse_args()

    base = Path(__file__).resolve().parent.parent
    composites_dir = base / "_sources" / "profiles" / "cdifCompositeProfile"

    targets = discover_targets(composites_dir, args.profile)
    if not targets:
        available = sorted(p.name for p in composites_dir.iterdir()
                           if (p / "resolvedSchema.json").exists())
        raise SystemExit(
            f"no composite profile matched --profile {args.profile!r}; "
            f"available: {', '.join(available)}")

    for t in targets:
        print(f"Generating propertyTree_2 for {t['name']}...")
        rows = generate_property_tree(t["resolved"])
        print(f"  {len(rows)} rows generated")

        if t["existing"]:
            add_sheet_to_existing(str(t["xlsx"]), "propertyTree_2", rows)
        else:
            create_new_workbook(str(t["xlsx"]), "propertyTree_2", rows)


if __name__ == "__main__":
    main()
