#!/usr/bin/env python3
"""Clean up a CDIF Implementation Guide markdown file.

What it does:
  - Normalizes class headings to ## (level 2) and property headings to ### (level 3)
    within "classes sections" (sections introduced by a # heading like
    "Dataset Properties added by ...", "Class Definitions", etc.)
  - Tightens blank lines between a heading and its first content (collapses
    multiple blank lines to one)
  - Generates a Table of Contents (# and ## levels only) right after the title
  - Sorts class blocks alphabetically within their parent classes-section,
    keeping a root Dataset class (Dataset / schema:Dataset / cdi:Dataset) first

What it does NOT do:
  - Touch property-level (###) ordering
  - Touch headings outside a classes-section (front-matter stays untouched)
  - Reflow paragraphs or rewrite prose

Class vs property heuristic: a heading is treated as a *property* if its body
contains a "Cardinality:" bullet. Otherwise, within a classes-section, a
level-2 or level-3 heading is treated as a *class*.

Usage:
    python tools/clean_ig.py path/to/ImplementationGuide.md
    python tools/clean_ig.py path/to/ImplementationGuide.md -o cleaned.md
    python tools/clean_ig.py path/to/ImplementationGuide.md --dry-run
"""
import argparse
import re
import sys
from pathlib import Path

# A heading whose body has a bullet starting with Cardinality / Required / Optional /
# Conditional / Content is treated as a property (these are the standard CDIF IG
# property-doc markers).
PROPERTY_BODY_RE = re.compile(
    r"^\s*[-*]\s*\*{0,2}(?:Cardinality|Required|Optional|Conditional|Content)\b",
    re.MULTILINE,
)

# A # heading whose title matches one of these starts a "classes-section":
# its ## children are classes, sortable alphabetically.
PROPERTIES_SECTION_PATTERNS = [
    re.compile(r"^(?:dataset\s+)?properties\s+added\s+by", re.IGNORECASE),
    re.compile(r"^class\s+definitions?$", re.IGNORECASE),
    re.compile(r"^(?:dataset\s+)?properties$", re.IGNORECASE),
    re.compile(r"^classes$", re.IGNORECASE),
    re.compile(r"^model$", re.IGNORECASE),
    re.compile(r"^object\s+definitions?$", re.IGNORECASE),
]

# Root Dataset names — kept first in alphabetical sort.
ROOT_DATASET_NAMES = {"Dataset", "schema:Dataset", "cdi:Dataset"}

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)(?:\s*\{#([^}]+)\})?\s*$")


FENCE_RE = re.compile(r"^(```|~~~)")


def parse_blocks(text):
    """Split markdown into heading blocks: list of dicts {level, title, anchor, body}.
    Lines inside fenced code blocks (``` or ~~~) are never treated as headings."""
    lines = text.splitlines(keepends=True)
    blocks = []
    preamble_lines = []
    current = None
    in_fence = False

    for line in lines:
        # Track fenced code blocks so bash/Python comments aren't mistaken for headings
        if FENCE_RE.match(line):
            in_fence = not in_fence

        m = None if in_fence else HEADING_RE.match(line)
        if m:
            if current is not None:
                blocks.append(current)
            elif preamble_lines:
                blocks.append({"level": 0, "title": None, "anchor": None, "body": preamble_lines})
                preamble_lines = []
            current = {
                "level": len(m.group(1)),
                "title": m.group(2).strip(),
                "anchor": m.group(3),
                "body": [],
            }
        else:
            if current is None:
                preamble_lines.append(line)
            else:
                current["body"].append(line)

    if current is not None:
        blocks.append(current)
    elif preamble_lines:
        blocks.append({"level": 0, "title": None, "anchor": None, "body": preamble_lines})

    return blocks


def is_classes_section(title):
    if not title:
        return False
    for pat in PROPERTIES_SECTION_PATTERNS:
        if pat.match(title):
            return True
    return False


def is_property(block):
    """A heading is a property if either:
    (a) its body has a property-doc marker (Cardinality/Required/Optional/...), or
    (b) its title looks like a property: starts with @, starts with lowercase,
        or has a prefix:local with lowercase local-name (e.g. cdi:value, schema:name).
    A title like schema:Dataset / cdi:InstanceVariable / dqv:QualityMeasurement
    (uppercase local-name) stays a class.
    """
    body_text = "".join(block["body"])
    if PROPERTY_BODY_RE.search(body_text):
        return True
    title = re.sub(r"\{#[^}]+\}", "", block.get("title") or "").strip()
    if not title:
        return False
    if title.startswith("@"):
        return True
    if ":" in title:
        local = title.split(":", 1)[1].lstrip()
        if local and local[0].islower():
            return True
        if local and local[0].isupper():
            return False
    if title[0].islower():
        return True
    return False


def slugify(text):
    """Approximate GitHub's anchor generation: lowercase, strip punctuation, spaces→hyphens."""
    s = re.sub(r"\{#[^}]+\}", "", text or "")
    s = s.lower()
    # Keep word chars, hyphens, spaces; strip everything else
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    return s


def tighten_body(body_lines, max_blank=1):
    """Strip leading blank lines; collapse runs of blank lines to at most max_blank."""
    i = 0
    while i < len(body_lines) and body_lines[i].strip() == "":
        i += 1
    body_lines = body_lines[i:]
    out = []
    blank_run = 0
    for line in body_lines:
        if line.strip() == "":
            blank_run += 1
            if blank_run <= max_blank:
                out.append(line)
        else:
            blank_run = 0
            out.append(line)
    # Strip trailing blanks
    while out and out[-1].strip() == "":
        out.pop()
    return out


def emit_block(block):
    if block["level"] == 0:
        return "".join(tighten_body(block["body"])) + "\n"
    hashes = "#" * block["level"]
    anchor = f" {{#{block['anchor']}}}" if block.get("anchor") else ""
    body = tighten_body(block["body"])
    text = f"{hashes} {block['title']}{anchor}\n"
    if body:
        text += "\n" + "".join(body)
        if not text.endswith("\n"):
            text += "\n"
    text += "\n"
    return text


def normalize_levels(blocks):
    """Within each classes-section: re-level class blocks to 2 and property blocks to 3."""
    in_classes = False
    for b in blocks:
        if b["level"] == 1:
            in_classes = is_classes_section(b["title"])
            continue
        if not in_classes:
            continue
        if b["level"] in (2, 3):
            b["level"] = 3 if is_property(b) else 2
    return blocks


def sort_classes(blocks):
    """Sort class blocks alphabetically within each classes-section, keeping
    root Dataset names first. Each class block + its trailing property blocks
    travel together."""
    out = []
    i = 0
    n = len(blocks)
    while i < n:
        b = blocks[i]
        out.append(b)
        if b["level"] == 1 and is_classes_section(b["title"]):
            # Collect all following blocks until next #-level heading
            section = []
            j = i + 1
            while j < n and blocks[j]["level"] != 1:
                section.append(blocks[j])
                j += 1

            # Group: each class block (##) + all its property blocks (###) until next ##
            groups = []
            current = None
            preamble_in_section = []
            for sb in section:
                if sb["level"] == 2:
                    if current is not None:
                        groups.append(current)
                    current = [sb]
                else:
                    if current is None:
                        preamble_in_section.append(sb)
                    else:
                        current.append(sb)
            if current is not None:
                groups.append(current)

            def key(g):
                title = re.sub(r"\{#[^}]+\}", "", g[0]["title"]).strip()
                is_root = title in ROOT_DATASET_NAMES
                return (0 if is_root else 1, title.lower())

            groups.sort(key=key)
            out.extend(preamble_in_section)
            for g in groups:
                out.extend(g)
            i = j
        else:
            i += 1
    return out


def generate_toc(blocks):
    """Generate TOC of # and ## headings. Skips the document title (first #),
    the TOC heading itself, and any existing top-level 'Table of contents'."""
    seen_title = False
    items = []
    for b in blocks:
        if b["level"] not in (1, 2):
            continue
        if b["title"] and b["title"].strip().lower() == "table of contents":
            continue
        if b["level"] == 1 and not seen_title:
            seen_title = True
            continue
        indent = "" if b["level"] == 1 else "  "
        anchor = b.get("anchor") or slugify(b["title"])
        items.append(f"{indent}- [{b['title']}](#{anchor})")
    if not items:
        return ""
    return "# Table of contents\n\n" + "\n".join(items) + "\n\n"


def clean(text):
    blocks = parse_blocks(text)
    # Strip any pre-existing top-level "Table of contents" sections
    blocks = [b for b in blocks
              if not (b["level"] == 1 and b["title"] and b["title"].strip().lower() == "table of contents")]
    blocks = normalize_levels(blocks)
    blocks = sort_classes(blocks)
    toc = generate_toc(blocks)

    # Emit. TOC goes immediately after the document title (first level-1 heading).
    parts = []
    title_emitted = False
    toc_emitted = False
    for b in blocks:
        parts.append(emit_block(b))
        if not title_emitted and b["level"] == 1:
            title_emitted = True
            if toc:
                parts.append(toc)
                toc_emitted = True
    # If we never saw a title (shouldn't happen), put TOC at the top.
    if not toc_emitted and toc:
        parts.insert(0, toc)

    return "".join(parts).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="Path to *.md file")
    ap.add_argument("-o", "--output", help="Output path (default: in-place)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print cleaned markdown to stdout instead of writing")
    args = ap.parse_args()

    p = Path(args.input)
    text = p.read_text(encoding="utf-8")
    cleaned = clean(text)

    if args.dry_run:
        sys.stdout.write(cleaned)
        return

    out = Path(args.output) if args.output else p
    out.write_text(cleaned, encoding="utf-8")
    print(f"Wrote {out} ({len(cleaned)} bytes)")


if __name__ == "__main__":
    main()
