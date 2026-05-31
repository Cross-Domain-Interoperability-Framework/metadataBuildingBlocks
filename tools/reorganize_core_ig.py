#!/usr/bin/env python3
"""One-off reorganizer: rearrange profile-core IG sections to match the TOC.

The current CDIFCoreImplementationGuide.md was alphabetized by clean_ig.py.
The user has hand-edited the Table of Contents to show the desired logical
grouping (Notes on schema.org / Namespaces / Base Class / Required / Optional
/ Other Classes / Data types). This script:

  1. Preserves the title block + intro + Table of contents verbatim
     (everything before the first '# Model' heading).
  2. Parses the rest of the file into top-level blocks (# or ##).
  3. Promotes 5 category headings from ## to # (Base Class DataSet,
     Required Properties from cdif Core profile, Optional Dataset properties,
     Other Classes used for CDIF Core, Data types used for CDIF Core).
  4. Re-emits all blocks in the order specified by TARGET_STRUCTURE below,
     with classes placed under their parent category.

Renames: "Dataset/dcat:CatalogRecord" -> "dcat:CatalogRecord" per the TOC.
"""
import re
import sys
from pathlib import Path

FILE = Path(r'C:\GithubC\CDIF\profile-core\CDIFCoreImplementationGuide.md')

# Target structure: list of (level, source_title, output_title)
# level: 1 for #, 2 for ##
# source_title: the heading text in the existing document (None for category
#   stubs that have no body to carry over)
# output_title: what to emit (allows renaming)
TARGET = [
    (1, "Model", "Model"),

    (1, "Notes on schema.org implementation", "Notes on schema.org implementation"),
    (2, "JSON-LD @type", "JSON-LD @type"),
    (2, "Object reference", "Object reference"),
    (2, "Repeating values", "Repeating values"),
    (2, "Namespace prefixes and JSON validation.", "Namespace prefixes and JSON validation."),
    (2, "Use of dcat:CatalogRecord", "Use of dcat:CatalogRecord"),
    (2, "Polymorphism of PropertyValue", "Polymorphism of PropertyValue"),

    (1, "Namespaces", "Namespaces"),

    (1, "Base Class DataSet", "Base Class DataSet"),

    (1, "Required Properties from cdif Core profile", "Required Properties from cdif Core profile"),
    (2, "Action", "Action"),

    (1, "Optional Dataset properties", "Optional Dataset properties"),

    (1, "Other Classes used for CDIF Core", "Other Classes used for CDIF Core"),
    (2, "Data Download", "Data Download"),
    (2, "DataCatalog", "DataCatalog"),
    (2, "MonetaryGrant", "MonetaryGrant"),
    (2, "Organization", "Organization"),
    (2, "Person", "Person"),
    (2, "PropertyValueSpecification", "PropertyValueSpecification"),
    (2, "Web API", "Web API"),

    (1, "Data types used for CDIF Core", "Data types used for CDIF Core"),
    (2, "ContactPoint", "ContactPoint"),
    (2, "Contributor", "Contributor"),
    (2, "Dataset/dcat:CatalogRecord", "dcat:CatalogRecord"),
    (2, "Defined Term", "Defined Term"),
    (2, "EntryPoint", "EntryPoint"),
    (2, "Labeled Link", "Labeled Link"),
    (2, "LinkRole", "LinkRole"),
    (2, "PropertyValue-(identifier)", "PropertyValue-(identifier)"),
    (2, "spdx:Checksum", "spdx:Checksum"),
]


def main():
    text = FILE.read_text(encoding='utf-8')
    lines = text.splitlines(keepends=True)

    # Find the line where the structural content begins — the first '# Model'
    model_idx = None
    for i, l in enumerate(lines):
        if l.rstrip() == '# Model':
            model_idx = i
            break
    if model_idx is None:
        print("ERROR: '# Model' not found", file=sys.stderr)
        sys.exit(1)

    header = lines[:model_idx]  # title + intro + TOC, preserved verbatim
    body = lines[model_idx:]

    # Parse body into blocks. A block boundary is a line starting with # or ##
    # (one or two hashes followed by space). Heading level = number of hashes.
    heading_re = re.compile(r'^(#{1,2}) (.+?)\s*$')
    blocks = {}  # title -> (level, body_lines_without_heading)
    current_title = None
    current_level = None
    current_body = []

    def flush():
        nonlocal current_body
        if current_title is not None:
            if current_title in blocks:
                print(f"WARN: duplicate heading: {current_title}", file=sys.stderr)
            blocks[current_title] = (current_level, current_body)

    for line in body:
        m = heading_re.match(line)
        if m:
            flush()
            current_level = len(m.group(1))
            current_title = m.group(2).strip()
            current_body = []
        else:
            current_body.append(line)
    flush()

    # Emit new document
    out = list(header)
    if not out or out[-1].rstrip() != '':
        out.append('\n')

    missing = []
    used = set()
    for level, src, dst in TARGET:
        if src not in blocks:
            missing.append(src)
            continue
        used.add(src)
        _src_level, body_lines = blocks[src]
        hashes = '#' * level
        out.append(f'{hashes} {dst}\n')
        # Trim leading blank lines from body (so heading isn't followed by
        # extra blanks beyond a single one)
        while body_lines and body_lines[0].strip() == '':
            body_lines = body_lines[1:]
        if body_lines:
            out.append('\n')
            out.extend(body_lines)
        # Ensure a blank line between sections
        if out and out[-1].rstrip() != '':
            out.append('\n')

    # Check for blocks present in source but not in TARGET (would be dropped)
    unused = [t for t in blocks if t not in used]

    if missing:
        print(f"MISSING in source (target wanted them): {missing}", file=sys.stderr)
    if unused:
        print(f"UNUSED in target (would be dropped): {unused}", file=sys.stderr)

    if missing or unused:
        print("\nABORTING due to mismatches — no file written.", file=sys.stderr)
        sys.exit(1)

    new_text = ''.join(out)
    # Collapse runs of more than 2 blank lines down to 2 (one blank separator)
    new_text = re.sub(r'\n{3,}', '\n\n', new_text)
    FILE.write_text(new_text, encoding='utf-8')
    print(f"Wrote {FILE} ({len(new_text)} bytes, {new_text.count(chr(10))} lines)")


if __name__ == '__main__':
    main()
