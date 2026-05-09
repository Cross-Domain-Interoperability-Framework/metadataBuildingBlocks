#!/usr/bin/env python3
"""
Convert resolved OGC Building Block schemas to JSON Forms-compatible Draft 7.

Reads from:  _sources/profiles/{profile}/resolvedSchema.json  (resolve_schema.py output)
Writes to:   build/jsonforms/profiles/{profile}/schema.json

Conversion rules:
  1. Strip $id, x-jsonld-* metadata keys
  2. $schema → Draft 7
  3. Simplify anyOf patterns for form rendering
  4. const arrays → default values
  5. contains constraints → enum on items
  6. Remove 'not' constraints
  7. Flatten leftover allOf entries
  8. Remove minItems constraints

The input schemas are already fully resolved (no $ref, no $defs).

Usage:
    python tools/convert_for_jsonforms.py --all
    python tools/convert_for_jsonforms.py --profile CDIFDiscoveryProfile
    python tools/convert_for_jsonforms.py --profile CDIFxasProfile --verbose
"""

import argparse
import copy
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
RESOLVED_DIR = REPO_ROOT / "_sources" / "profiles"
OUTPUT_DIR = REPO_ROOT / "build" / "jsonforms" / "profiles"
SOURCES_DIR = REPO_ROOT / "_sources" / "jsonforms" / "profiles"

# Subdirectory mapping for profile categories
_PROFILE_SUBDIR = {
    "CDIF": "cdifProfiles",
}


def _profile_subdir(name: str) -> str:
    """Return the subdirectory name for a profile (adaProfiles or cdifProfiles)."""
    for prefix, subdir in _PROFILE_SUBDIR.items():
        if name.startswith(prefix):
            return subdir
    return ""


def _find_resolved_schema(name: str) -> Path:
    """Find the resolvedSchema.json for a profile, searching subdirectories."""
    subdir = _profile_subdir(name)
    if subdir:
        candidate = RESOLVED_DIR / subdir / name / "resolvedSchema.json"
        if candidate.exists():
            return candidate
    # Fallback: search all subdirectories
    for child in RESOLVED_DIR.iterdir():
        if child.is_dir():
            candidate = child / name / "resolvedSchema.json"
            if candidate.exists():
                return candidate
    # Legacy flat layout fallback
    return RESOLVED_DIR / name / "resolvedSchema.json"


def _find_sources_dir(name: str) -> Path:
    """Find the jsonforms sources directory for a profile."""
    subdir = _profile_subdir(name)
    if subdir:
        candidate = SOURCES_DIR / subdir / name
        if candidate.is_dir():
            return candidate
    # Fallback: search all subdirectories
    for child in SOURCES_DIR.iterdir():
        if child.is_dir():
            candidate = child / name
            if candidate.is_dir():
                return candidate
    # Legacy flat layout fallback
    return SOURCES_DIR / name

CDIF_PROFILES = ["CDIFDiscoveryProfile", "CDIFxasProfile"]
ALL_PROFILES = CDIF_PROFILES


# Keys to strip from schemas (metadata, not useful for forms)
STRIP_KEYS = {"$id", "x-jsonld-prefixes", "x-jsonld-context", "x-jsonld-extra-terms"}


def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


# ---------------------------------------------------------------------------
# Inline $ref and merge allOf
# ---------------------------------------------------------------------------

def inline_refs_and_merge_allof(schema: dict) -> dict:
    """
    Resolve all $ref pointers (to local $defs) and merge top-level allOf
    entries into a single flat schema.  This produces a structure identical
    to the old fully-inlined resolved schemas, so downstream simplification
    passes work correctly without allOf/enum conflicts.
    """
    defs = schema.get("$defs", {})

    def _resolve(node: Any) -> Any:
        """Recursively inline $ref → $defs pointers."""
        if isinstance(node, dict):
            if "$ref" in node:
                ref = node["$ref"]
                if ref.startswith("#/$defs/"):
                    def_name = ref[len("#/$defs/"):]
                    if def_name in defs:
                        resolved_def = _resolve(copy.deepcopy(defs[def_name]))
                        if len(node) == 1:
                            return resolved_def
                        # Merge sibling keys into the resolved def
                        if isinstance(resolved_def, dict):
                            extra = {k: _resolve(v) for k, v in node.items() if k != "$ref"}
                            merged = {**resolved_def, **extra}
                            return merged
                        return resolved_def
                return {k: _resolve(v) for k, v in node.items() if k != "$ref"} if len(node) > 1 else node
            return {k: _resolve(v) for k, v in node.items()}
        elif isinstance(node, list):
            return [_resolve(item) for item in node]
        return node

    resolved = _resolve(schema)
    resolved.pop("$defs", None)

    # Merge top-level allOf entries into a single flat object
    if "allOf" in resolved:
        resolved = _merge_allof_entries(resolved)

    return resolved


def _merge_allof_entries(schema: dict) -> dict:
    """
    Merge allOf entries by combining their properties, required lists,
    and other keywords into the parent object.  For conflicting property
    definitions (e.g. @type with different items.enum), merge enum lists.
    """
    if "allOf" not in schema:
        return schema

    entries = schema.pop("allOf")
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        # Merge properties
        for pk, pv in entry.get("properties", {}).items():
            existing = schema.get("properties", {}).get(pk)
            if existing is not None:
                schema["properties"][pk] = _deep_merge_with_enum_union(existing, pv)
            else:
                schema.setdefault("properties", {})[pk] = pv
        # Merge required
        for req in entry.get("required", []):
            schema.setdefault("required", [])
            if req not in schema["required"]:
                schema["required"].append(req)
        # Merge other keys (type, description, etc.) — entry wins only if
        # the parent doesn't already have a value
        for k, v in entry.items():
            if k in ("properties", "required", "allOf"):
                continue
            if k not in schema:
                schema[k] = v
        # Recurse into nested allOf
        if "allOf" in entry:
            nested = copy.deepcopy(entry)
            nested = _merge_allof_entries(nested)
            for pk, pv in nested.get("properties", {}).items():
                existing = schema.get("properties", {}).get(pk)
                if existing is not None:
                    schema["properties"][pk] = _deep_merge_with_enum_union(existing, pv)
                else:
                    schema.setdefault("properties", {})[pk] = pv

    return schema


def _deep_merge_with_enum_union(base: Any, overlay: Any) -> Any:
    """
    Recursive dict merge that takes the *union* of enum lists instead
    of letting overlay overwrite.
    """
    if not isinstance(base, dict) or not isinstance(overlay, dict):
        return copy.deepcopy(overlay)

    result = copy.deepcopy(base)
    for k, v in overlay.items():
        if k == "enum" and k in result:
            # Union of enum lists, preserving order
            combined = list(result[k])
            for val in v:
                if val not in combined:
                    combined.append(val)
            result[k] = combined
        elif k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = _deep_merge_with_enum_union(result[k], v)
        else:
            result[k] = copy.deepcopy(v)
    return result


# ---------------------------------------------------------------------------
# Core conversion helpers
# ---------------------------------------------------------------------------

def strip_metadata_keys(schema: Any, is_root: bool = True) -> Any:
    """Recursively remove metadata keys like $id, x-jsonld-*. Also strip $schema from nested objects."""
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            if k in STRIP_KEYS:
                continue
            if k.startswith("x-jsonld"):
                continue
            # Strip $schema from nested objects (keep only at root)
            if k == "$schema" and not is_root:
                continue
            result[k] = strip_metadata_keys(v, is_root=False)
        return result
    elif isinstance(schema, list):
        return [strip_metadata_keys(item, is_root=False) for item in schema]
    return schema


def convert_draft_version(schema: dict) -> dict:
    """Change $schema to Draft 7."""
    if "$schema" in schema:
        schema["$schema"] = "http://json-schema.org/draft-07/schema#"
    return schema


def simplify_const_to_default(schema: Any) -> Any:
    """
    Convert const values to default values for form pre-population.
    const arrays like {"const": ["schema:Dataset", "schema:Product"]} become
    {"default": ["schema:Dataset", "schema:Product"]}.
    const strings remain as default strings.
    Also handles the pattern where const is used alongside type.
    """
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            result[k] = simplify_const_to_default(v)

        # If const is present, convert to default and remove const
        if "const" in result:
            const_val = result.pop("const")
            if "default" not in result:
                result["default"] = const_val
            # Add type if not present
            if "type" not in result:
                if isinstance(const_val, list):
                    result["type"] = "array"
                elif isinstance(const_val, str):
                    result["type"] = "string"

        return result
    elif isinstance(schema, list):
        return [simplify_const_to_default(item) for item in schema]
    return schema


def simplify_contains_to_enum(schema: Any) -> Any:
    """
    Convert contains constraints to enum on items.
    {type: array, items: {type: string}, contains: {const: "X"}}
    ->  {type: array, items: {type: string, enum: ["X"]}}

    {type: array, items: {type: string}, contains: {enum: [...]}}
    ->  {type: array, items: {type: string, enum: [...]}}

    Also handles allOf with multiple contains.
    """
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            result[k] = simplify_contains_to_enum(v)

        # Strip contains from non-array types (invalid placement)
        if "contains" in result and result.get("type") != "array":
            result.pop("contains")

        if "contains" in result and result.get("type") == "array":
            contains = result.pop("contains")
            if "const" in contains:
                enum_vals = [contains["const"]]
            elif "enum" in contains:
                enum_vals = contains["enum"]
            else:
                enum_vals = None

            if enum_vals is not None:
                if "items" not in result:
                    result["items"] = {"type": "string"}
                if isinstance(result["items"], dict):
                    result["items"]["enum"] = enum_vals

        # Handle allOf with contains patterns (e.g., @type requiring multiple values)
        if "allOf" in result and result.get("type") == "array":
            new_allof = []
            collected_enums = []
            for item in result["allOf"]:
                if isinstance(item, dict) and "contains" in item:
                    contains = item["contains"]
                    if "const" in contains:
                        collected_enums.append(contains["const"])
                    elif "enum" in contains:
                        collected_enums.extend(contains["enum"])
                else:
                    new_allof.append(item)

            if collected_enums:
                # Set as default values for the array
                if "default" not in result:
                    result["default"] = collected_enums
                if "items" not in result:
                    result["items"] = {"type": "string"}
                if isinstance(result["items"], dict):
                    result["items"]["enum"] = collected_enums

            if new_allof:
                result["allOf"] = new_allof
            else:
                result.pop("allOf", None)

        return result
    elif isinstance(schema, list):
        return [simplify_contains_to_enum(item) for item in schema]
    return schema


# ---------------------------------------------------------------------------
# anyOf simplification helpers
# ---------------------------------------------------------------------------

def simplify_anyof_license_items(items_schema: dict) -> dict:
    """Simplify schema:license items anyOf to CreativeWork object."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:CreativeWork",
            },
            "schema:name": {"type": "string"},
            "schema:description": {"type": "string"},
            "schema:url": {"type": "string"},
        },
    }


def simplify_anyof_contributor_items(items_schema: dict) -> dict:
    """Simplify schema:contributor items anyOf to Person with optional role."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:Person",
            },
            "schema:name": {"type": "string"},
            "schema:identifier": {
                "type": "string",
                "description": "ORCID or other identifier",
            },
            "schema:affiliation": {
                "type": "object",
                "properties": {
                    "schema:name": {"type": "string"},
                },
            },
            "schema:roleName": {
                "type": "string",
                "description": "Role of the contributor",
            },
        },
        "required": ["schema:name"],
    }


def simplify_anyof_funder(funder_schema: dict) -> dict:
    """Simplify funder anyOf to inline Organization object."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:Organization",
            },
            "schema:name": {"type": "string"},
        },
        "required": ["schema:name"],
    }


def simplify_anyof_creator_items(items_schema: dict) -> dict:
    """Simplify schema:creator @list items anyOf Person/Org to Person with selector."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:Person",
                "enum": ["schema:Person", "schema:Organization"],
            },
            "schema:name": {"type": "string"},
            "schema:alternateName": {"type": "string"},
            "schema:identifier": {
                "type": "string",
                "description": "ORCID or other identifier",
            },
            "schema:affiliation": {
                "type": "object",
                "properties": {
                    "schema:name": {"type": "string"},
                },
            },
            "schema:description": {"type": "string"},
        },
        "required": ["@type", "schema:name"],
    }


def simplify_anyof_maintainer(schema: dict) -> dict:
    """Simplify schema:maintainer anyOf to Person object."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:Person",
                "enum": ["schema:Person", "schema:Organization"],
            },
            "schema:name": {"type": "string"},
        },
        "required": ["schema:name"],
    }


def simplify_anyof_provider_items(schema: dict) -> dict:
    """Simplify distribution provider items anyOf to Organization."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:Organization",
            },
            "schema:name": {"type": "string"},
        },
        "required": ["schema:name"],
    }


def simplify_anyof_measurement_technique(schema: dict) -> dict:
    """Simplify variableMeasured measurementTechnique anyOf."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:DefinedTerm",
            },
            "schema:name": {"type": "string"},
        },
        "required": ["schema:name"],
    }


def simplify_anyof_unit_code(schema: dict) -> dict:
    """Simplify unitCode anyOf to string."""
    return {"type": "string"}


def simplify_anyof_property_id_items(schema: dict) -> dict:
    """Simplify propertyID items anyOf to DefinedTerm."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:DefinedTerm",
            },
            "schema:name": {"type": "string"},
            "schema:identifier": {"type": "string"},
            "schema:inDefinedTermSet": {"type": "string"},
            "schema:termCode": {"type": "string"},
        },
    }


def simplify_anyof_cdi_uses_items(schema: dict) -> dict:
    """Simplify cdi:uses items anyOf to DefinedTerm."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:DefinedTerm",
            },
            "schema:name": {"type": "string"},
        },
    }


def simplify_anyof_conditions_of_access_items(schema: dict) -> dict:
    """Simplify schema:conditionsOfAccess items anyOf to LabeledLink (CreativeWork)."""
    return {
        "type": "object",
        "description": "Access condition — provide a label and optional URL",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:CreativeWork",
            },
            "schema:name": {
                "type": "string",
                "description": "Short label for the access condition",
            },
            "schema:description": {
                "type": "string",
                "description": "Detailed description of the condition",
            },
            "schema:url": {
                "type": "string",
                "format": "uri",
                "description": "URL to a document describing the access condition",
            },
        },
        "required": ["schema:name"],
    }


def simplify_anyof_publisher(schema: dict) -> dict:
    """Simplify schema:publisher anyOf to Organization."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:Organization",
                "enum": ["schema:Person", "schema:Organization"],
            },
            "schema:name": {"type": "string"},
            "schema:identifier": {
                "type": "string",
                "description": "Identifier (e.g. ROR, ORCID)",
            },
        },
        "required": ["schema:name"],
    }


def simplify_anyof_spatial_coverage_items(schema: dict) -> dict:
    """Simplify schema:spatialCoverage items to a place object."""
    return {
        "type": "object",
        "description": "Spatial extent of the dataset",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:Place",
            },
            "schema:name": {
                "type": "string",
                "description": "Place name",
            },
            "schema:geo": {
                "type": "object",
                "properties": {
                    "@type": {
                        "type": "string",
                        "default": "schema:GeoShape",
                    },
                    "schema:box": {
                        "type": "string",
                        "description": "Bounding box as 'south west north east'",
                    },
                },
            },
        },
    }


def simplify_anyof_temporal_coverage_items(schema: dict) -> dict:
    """Replace temporalCoverage items anyOf with a simple string."""
    return {
        "type": "string",
        "description": "ISO 8601 date, date range (e.g. 2020-01/2020-12), or text description",
    }


def simplify_anyof_keywords_items(schema: dict) -> dict:
    """Simplify schema:keywords items anyOf to string."""
    return {"type": "string"}


def simplify_anyof_publishing_principles_items(schema: dict) -> dict:
    """Simplify schema:publishingPrinciples items anyOf to string."""
    return {"type": "string", "description": "Publishing principle statement or URL"}


def simplify_anyof_additional_type_items(schema: dict) -> dict:
    """Simplify schema:additionalType items anyOf to string."""
    return {"type": "string", "description": "Additional type URI or label"}


def simplify_anyof_distribution_items_cdif(schema: dict) -> dict:
    """
    Replace CDIF distribution items anyOf with a single flat object containing
    all fields from DataDownload and WebAPI, plus any additional properties
    from the anyOf branches (e.g. fileDetail, schema:hasPart from Files).
    The @type field indicates which type.
    """
    merged_props = {
        "@type": {
            "type": "array",
            "items": {"type": "string", "enum": ["schema:DataDownload", "schema:WebAPI"]},
            "default": ["schema:DataDownload"],
        },
        "schema:name": {"type": "string", "description": "Name of this distribution"},
        "schema:description": {"type": "string"},
        "schema:contentUrl": {
            "type": "string",
            "format": "uri",
            "description": "Download URL for the file (DataDownload)",
        },
        "schema:encodingFormat": {
            "type": "array",
            "items": {"type": "string"},
            "description": "MIME type(s) (DataDownload)",
        },
        "spdx:checksum": {
            "type": "object",
            "properties": {
                "spdx:algorithm": {"type": "string"},
                "spdx:checksumValue": {"type": "string"},
            },
        },
        "schema:serviceType": {
            "type": "string",
            "description": "Type of service, e.g. OGC:WMS, OPeNDAP (WebAPI)",
        },
        "schema:documentation": {
            "type": "string",
            "format": "uri",
            "description": "URL to API documentation (WebAPI)",
        },
    }

    # Merge properties from anyOf branches (e.g. fileDetail, schema:hasPart
    # from the inlined Files schema in technique profile distributions).
    # Branches may contain allOf (e.g. allOf: [Files, {@type override}])
    # that hasn't been flattened yet — flatten each branch first.
    for branch in schema.get("anyOf", []):
        if not isinstance(branch, dict):
            continue
        flat = _merge_allof_entries(copy.deepcopy(branch)) if "allOf" in branch else branch
        for pk, pv in flat.get("properties", {}).items():
            if pk in merged_props:
                if pk == "@type":
                    merged_props[pk] = _merge_type_enums(merged_props[pk], pv)
                else:
                    merged_props[pk] = _deep_merge_dict(merged_props[pk], pv)
            else:
                merged_props[pk] = copy.deepcopy(pv)

    return {
        "type": "object",
        "description": "Distribution — Data Download or Web API",
        "properties": merged_props,
    }


def simplify_anyof_same_as_items(schema: dict) -> dict:
    """Simplify schema:sameAs items anyOf to string."""
    return {"type": "string", "description": "Alternate identifier or URL"}


# ---------------------------------------------------------------------------
# Distribution simplification — preserve oneOf structure
# ---------------------------------------------------------------------------

def simplify_distribution_items(items_schema: dict) -> dict:
    """
    Flatten distribution items oneOf into a single merged object.

    The resolved schema has oneOf with 3 branches (single file, archive,
    WebAPI).  JSON Forms cannot add new array items when items uses oneOf,
    because it cannot determine which variant to instantiate.  Since the
    UISchema already handles switching between Data Download and WebAPI via
    the ``_distributionType`` virtual field (injected at serve time), we
    merge all branches into a single flat object with all properties.

    For technique profiles the resolved schema may also have top-level
    ``properties`` alongside ``oneOf`` (technique constraints).  These are
    merged in as well.
    """
    result = copy.deepcopy(items_schema)

    if "oneOf" not in result:
        return result

    branches = result.pop("oneOf")
    extra_props = result.pop("properties", {})

    # Start with an empty merged object
    merged = {"type": "object", "properties": {}}

    # Merge each oneOf branch's properties (flatten allOf within branches first)
    for branch in branches:
        if not isinstance(branch, dict):
            continue
        flat = _merge_allof_entries(copy.deepcopy(branch)) if "allOf" in branch else branch
        for pk, pv in flat.get("properties", {}).items():
            if pk in merged["properties"]:
                if pk == "@type":
                    # Special handling: combine enum values from all branches
                    merged["properties"][pk] = _merge_type_enums(
                        merged["properties"][pk], pv
                    )
                else:
                    # Deep merge if both exist
                    merged["properties"][pk] = _deep_merge_dict(
                        merged["properties"][pk], pv
                    )
            else:
                merged["properties"][pk] = copy.deepcopy(pv)

    # Merge technique-specific extra properties
    for pk, pv in extra_props.items():
        if pk in merged["properties"]:
            merged["properties"][pk] = _deep_merge_dict(
                merged["properties"][pk], pv
            )
        else:
            merged["properties"][pk] = copy.deepcopy(pv)

    return merged


def _deep_merge_dict(base: dict, overlay: dict) -> dict:
    """Simple recursive dict merge (overlay wins on conflicts)."""
    result = copy.deepcopy(base)
    for k, v in overlay.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = _deep_merge_dict(result[k], v)
        else:
            result[k] = copy.deepcopy(v)
    return result


def _merge_type_enums(existing: dict, new: dict) -> dict:
    """Merge @type schemas by combining their items.enum lists."""
    result = copy.deepcopy(existing)
    new = copy.deepcopy(new)

    # Collect enum values from both sides
    existing_enums = []
    new_enums = []

    if isinstance(result.get("items"), dict) and "enum" in result["items"]:
        existing_enums = result["items"]["enum"]
    if isinstance(new.get("items"), dict) and "enum" in new["items"]:
        new_enums = new["items"]["enum"]

    # Combine and deduplicate while preserving order
    combined = list(existing_enums)
    for val in new_enums:
        if val not in combined:
            combined.append(val)

    if combined:
        if "items" not in result:
            result["items"] = {"type": "string"}
        if isinstance(result["items"], dict):
            result["items"]["enum"] = combined

    return result


# ---------------------------------------------------------------------------
# File-type anyOf simplification (hasPart item level)
# ---------------------------------------------------------------------------

def _is_file_type_anyof(anyof: list) -> bool:
    """Return True if the anyOf list contains file-type branches (image, tabular, etc.).

    Detected by checking whether any branch defines a ``componentType`` property,
    which is the hallmark of file-type schemas with hasPart.
    """
    if not isinstance(anyof, list) or len(anyof) < 2:
        return False
    return any(
        isinstance(branch, dict)
        and "componentType" in branch.get("properties", {})
        for branch in anyof
    )


def simplify_file_detail_anyof(schema: dict) -> dict:
    """
    Flatten file-type anyOf into a single merged object.

    JSON Forms cannot render anyOf discriminators, so we merge all file-type
    branches (image, tabular, dataCube, etc.) into one flat object.  The
    UISchema uses MIME-type-based SHOW rules to display only the relevant
    fields for the selected file type.

    The anyOf appears at the hasPart item level (merged from files/schema.yaml).
    The caller extracts it and merges the result's properties back into the
    parent object.

    - All properties across all branches are merged (skip @type — inferred
      from MIME type at save time)
    - componentType enums are collected from all branches and merged into a
      single flat enum list
    """
    if "anyOf" not in schema:
        return schema

    merged_props: dict = {}
    all_ct_enums: list = []
    all_ct_detail_props: dict = {}

    for option in schema.get("anyOf", []):
        if not isinstance(option, dict):
            continue
        for pk, pv in option.get("properties", {}).items():
            if pk == "@type":
                # Skip — fileDetail @type is inferred from MIME type on save
                continue
            if pk == "componentType":
                _collect_component_type_info(pv, all_ct_enums, all_ct_detail_props)
                continue
            if pk not in merged_props:
                merged_props[pk] = copy.deepcopy(pv)
            else:
                # Deep merge if both exist
                merged_props[pk] = _deep_merge_dict(merged_props[pk], pv)

    # Build merged componentType with flat enum + detail properties
    if all_ct_enums:
        # Deduplicate while preserving order
        seen = set()
        unique_enums = []
        for e in all_ct_enums:
            if e not in seen:
                seen.add(e)
                unique_enums.append(e)
        ct_props = {
            "@type": {
                "type": "string",
                "enum": unique_enums,
            },
        }
        ct_props.update(all_ct_detail_props)
        merged_props["componentType"] = {
            "type": "object",
            "properties": ct_props,
        }

    return {"type": "object", "properties": merged_props}


def _collect_component_type_info(ct_schema: dict, enums: list, detail_props: dict) -> None:
    """Recursively collect @type enum values AND detail properties from componentType.

    In addition to gathering enum values for the flat componentType dropdown,
    this collects all non-@type properties from each anyOf branch (these are
    technique-specific detail properties like detector, beamsplitter, etc.).
    """
    if not isinstance(ct_schema, dict):
        return

    # Direct object with properties.@type.enum
    props = ct_schema.get("properties", {})
    at_type = props.get("@type", {})
    if isinstance(at_type, dict):
        if "enum" in at_type:
            enums.extend(at_type["enum"])
        if "default" in at_type and isinstance(at_type["default"], str):
            enums.append(at_type["default"])

    # Collect non-@type properties from detail schemas
    for pk, pv in props.items():
        if pk != "@type" and pk not in detail_props:
            detail_props[pk] = copy.deepcopy(pv)

    # Recurse into anyOf branches
    for branch in ct_schema.get("anyOf", []):
        _collect_component_type_info(branch, enums, detail_props)

    # Recurse into @type.anyOf (deeply nested EMPA pattern)
    if isinstance(at_type, dict) and "anyOf" in at_type:
        for sub in at_type["anyOf"]:
            if isinstance(sub, dict) and "default" in sub:
                enums.append(sub["default"])
            if isinstance(sub, dict) and "enum" in sub:
                enums.extend(sub["enum"])


# ---------------------------------------------------------------------------
# Main anyOf simplification walker
# ---------------------------------------------------------------------------

def apply_anyof_simplifications(schema: Any, path: str = "") -> Any:
    """
    Walk the schema and apply anyOf simplifications at known locations.
    Uses the property path to identify which simplification to apply.
    """
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            current_path = f"{path}/{k}" if path else k

            # schema:identifier anyOf -> simplify (anywhere in schema)
            if k == "schema:identifier" and isinstance(v, dict) and "anyOf" in v:
                desc = v.get("description", "Identifier")
                result[k] = {"type": "string", "description": desc}
                continue

            # schema:license items anyOf
            if k == "items" and path.endswith("schema:license") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_license_items(v)
                continue

            # schema:contributor items anyOf
            if k == "items" and path.endswith("schema:contributor") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_contributor_items(v)
                continue

            # funder anyOf (in funding items or schema:funder)
            if k in ("funder", "schema:funder") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_funder(v)
                continue

            # schema:creator @list items anyOf
            if k == "items" and path.endswith("@list") and "schema:creator" in path and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_creator_items(v)
                continue

            # schema:maintainer anyOf in subjectOf
            if k == "schema:maintainer" and "schema:subjectOf" in path and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_maintainer(v)
                continue

            # schema:provider items anyOf in distribution
            if k == "items" and path.endswith("schema:provider") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_provider_items(v)
                continue

            # variableMeasured schema:measurementTechnique anyOf
            if k == "schema:measurementTechnique" and "schema:variableMeasured" in path and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_measurement_technique(v)
                continue

            # variableMeasured schema:unitCode anyOf
            if k == "schema:unitCode" and "schema:variableMeasured" in path and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_unit_code(v)
                continue

            # variableMeasured schema:propertyID items anyOf
            if k == "items" and path.endswith("schema:propertyID") and "schema:variableMeasured" in path and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_property_id_items(v)
                continue

            # variableMeasured cdi:uses items anyOf
            if k == "items" and path.endswith("cdi:uses") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_cdi_uses_items(v)
                continue

            # variableMeasured schema:identifier anyOf (nested in variable)
            if k == "schema:identifier" and "schema:variableMeasured" in path and isinstance(v, dict) and "anyOf" in v:
                result[k] = {"type": "string", "description": "Variable identifier"}
                continue

            # @type anyOf patterns (e.g., Organization types)
            if k == "@type" and isinstance(v, dict) and "anyOf" in v:
                first_anyof = v["anyOf"][0] if v["anyOf"] else {}
                if "const" in first_anyof:
                    result[k] = {
                        "type": "array" if isinstance(first_anyof["const"], list) else "string",
                        "default": first_anyof["const"],
                    }
                else:
                    result[k] = apply_anyof_simplifications(v, current_path)
                continue

            # distribution items oneOf -> preserve structure
            # After structural simplification, continue recursion into branches
            if k == "items" and path.endswith("schema:distribution") and isinstance(v, dict) and "oneOf" in v:
                simplified = simplify_distribution_items(v)
                result[k] = apply_anyof_simplifications(simplified, current_path)
                continue

            # distribution items anyOf -> simplified (CDIF: DataDownload/WebAPI)
            # Preserve extra properties from technique overlays (e.g. fileDetail)
            if k == "items" and path.endswith("schema:distribution") and isinstance(v, dict) and "anyOf" in v:
                simplified = simplify_anyof_distribution_items_cdif(v)
                extra_props = v.get("properties", {})
                if extra_props:
                    simplified.setdefault("properties", {})
                    for pk, pv in extra_props.items():
                        if pk not in simplified["properties"]:
                            simplified["properties"][pk] = copy.deepcopy(pv)
                result[k] = apply_anyof_simplifications(simplified, current_path)
                continue

            # schema:conditionsOfAccess items anyOf
            if k == "items" and path.endswith("schema:conditionsOfAccess") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_conditions_of_access_items(v)
                continue

            # schema:publisher anyOf (not an array, direct anyOf)
            if k == "schema:publisher" and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_publisher(v)
                continue

            # schema:spatialCoverage items
            if k == "items" and path.endswith("schema:spatialCoverage") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_spatial_coverage_items(v)
                continue

            # schema:temporalCoverage items
            if k == "items" and path.endswith("schema:temporalCoverage") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_temporal_coverage_items(v)
                continue

            # schema:keywords items anyOf
            if k == "items" and path.endswith("schema:keywords") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_keywords_items(v)
                continue

            # schema:publishingPrinciples items anyOf
            if k == "items" and path.endswith("schema:publishingPrinciples") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_publishing_principles_items(v)
                continue

            # schema:additionalType items anyOf
            if k == "items" and path.endswith("schema:additionalType") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_additional_type_items(v)
                continue

            # schema:sameAs items anyOf
            if k == "items" and path.endswith("schema:sameAs") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_same_as_items(v)
                continue

            # schema:geo anyOf (GeoShape vs GeoCoordinates) -> simplify to GeoShape
            if k == "schema:geo" and isinstance(v, dict) and "anyOf" in v:
                result[k] = {
                    "type": "object",
                    "description": v.get("description", "Geographic extent"),
                    "properties": {
                        "@type": {"type": "string", "default": "schema:GeoShape"},
                        "schema:box": {
                            "type": "string",
                            "description": "Bounding box as 'south west north east'",
                        },
                    },
                }
                continue

            # schema:linkRelationship anyOf (DefinedTerm or string) -> simplify to string
            if k == "schema:linkRelationship" and isinstance(v, dict) and "anyOf" in v:
                result[k] = {"type": "string", "description": "How the linked resource is related"}
                continue

            # schema:name items anyOf in spatialCoverage (place names: DefinedTerm or string)
            if k == "items" and path.endswith("schema:name") and "schema:spatialCoverage" in path and isinstance(v, dict) and "anyOf" in v:
                result[k] = {"type": "string"}
                continue

            # schema:serviceType anyOf (string or DefinedTerm) -> simplify to string
            if k == "schema:serviceType" and isinstance(v, dict) and "anyOf" in v:
                result[k] = {
                    "type": "string",
                    "description": v.get("description", "Type of service"),
                }
                continue

            # schema:documentation oneOf (string or LabeledLink) -> simplify to string
            if k == "schema:documentation" and isinstance(v, dict) and "oneOf" in v:
                result[k] = {
                    "type": "string",
                    "description": v.get("description", "URL to API documentation"),
                }
                continue

            # schema:termsOfService oneOf (string or LabeledLink) -> simplify to string
            if k == "schema:termsOfService" and isinstance(v, dict) and "oneOf" in v:
                result[k] = {
                    "type": "string",
                    "description": v.get("description", "Terms of service"),
                }
                continue

            result[k] = apply_anyof_simplifications(v, current_path)

        # Post-processing: merge file-type anyOf into properties.
        # After files/schema.yaml restructuring, file-type branches (image,
        # tabular, etc.) appear as a root-level anyOf on hasPart items instead
        # of under a "fileDetail" property.  Detect this pattern and merge.
        if "anyOf" in result and "properties" in result and _is_file_type_anyof(result["anyOf"]):
            simplified = simplify_file_detail_anyof({"anyOf": result.pop("anyOf")})
            for pk, pv in simplified.get("properties", {}).items():
                if pk in result["properties"]:
                    result["properties"][pk] = _deep_merge_dict(result["properties"][pk], pv)
                else:
                    result["properties"][pk] = pv

        return result
    elif isinstance(schema, list):
        return [apply_anyof_simplifications(item, path) for item in schema]
    return schema


# ---------------------------------------------------------------------------
# Remaining cleanup passes
# ---------------------------------------------------------------------------

def remove_not_constraints(schema: Any) -> Any:
    """Remove 'not' constraints (e.g., not contains) that confuse form renderers."""
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            if k == "not":
                continue
            result[k] = remove_not_constraints(v)
        return result
    elif isinstance(schema, list):
        return [remove_not_constraints(item) for item in schema]
    return schema


def flatten_remaining_allof(schema: Any) -> Any:
    """
    Flatten leftover allOf entries that remain after merging.
    - Entries with 'properties' are merged into the parent (deep merge).
    - Simple entries with only 'required' are merged into the parent.
    - Entries with 'anyOf' containing conditional-required rules are dropped
      (JSON Forms doesn't support conditional required).
    Applied recursively so it catches allOf inside items, properties, etc.
    """
    if isinstance(schema, dict):
        # Recurse first so nested allOf in properties/items are handled
        result = {}
        for k, v in schema.items():
            result[k] = flatten_remaining_allof(v)

        # Now flatten allOf in the current object
        if "allOf" in result:
            all_of = result.pop("allOf")
            for entry in all_of:
                if not isinstance(entry, dict):
                    continue
                keys = set(entry.keys())
                if not keys:
                    continue
                if keys == {"anyOf"}:
                    # Distinguish file-type anyOf (branches have properties
                    # including componentType — image/tabular/dataCube/document
                    # file-type branches) from conditional-required patterns
                    # (branches only have required).
                    branches = entry["anyOf"]
                    if _is_file_type_anyof(branches):
                        # File-type anyOf — flatten into parent properties
                        # now, since apply_anyof_simplifications already ran.
                        simplified = simplify_file_detail_anyof({"anyOf": branches})
                        for pk, pv in simplified.get("properties", {}).items():
                            existing = result.get("properties", {}).get(pk)
                            if existing is not None:
                                result["properties"][pk] = _deep_merge_dict(existing, pv)
                            else:
                                result.setdefault("properties", {})[pk] = copy.deepcopy(pv)
                    # else: conditional required — drop for form friendliness
                    continue
                # Merge properties from the allOf entry into the parent
                for pk, pv in entry.get("properties", {}).items():
                    existing = result.get("properties", {}).get(pk)
                    if existing is not None:
                        result["properties"][pk] = _deep_merge_dict(existing, pv)
                    else:
                        result.setdefault("properties", {})[pk] = copy.deepcopy(pv)
                # Merge required
                for req in entry.get("required", []):
                    result.setdefault("required", [])
                    if req not in result["required"]:
                        result["required"].append(req)
                # Merge other scalar keys (type, description, title, etc.)
                for ek, ev in entry.items():
                    if ek in ("properties", "required", "allOf"):
                        continue
                    if ek not in result:
                        result[ek] = ev
        return result
    elif isinstance(schema, list):
        return [flatten_remaining_allof(item) for item in schema]
    return schema


def relax_min_items(schema: Any) -> Any:
    """Remove or relax minItems constraints that prevent empty arrays in forms."""
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            if k == "minItems":
                continue  # Remove minItems from all arrays for form friendliness
            result[k] = relax_min_items(v)
        return result
    elif isinstance(schema, list):
        return [relax_min_items(item) for item in schema]
    return schema


# ---------------------------------------------------------------------------
# additionalType enum → oneOf (human-readable dropdown labels)
# ---------------------------------------------------------------------------

def _id_to_label(val: str) -> str:
    """Generate label: strip namespace prefix and split camelCase into words."""
    name = val.split(":", 1)[1] if ":" in val else val
    # Insert space before each uppercase letter that follows a lowercase letter
    return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", name)


def _convert_at_enum_to_oneof(at_schema: dict) -> None:
    """Flatten additionalType from array to string with oneOf labels.

    CzForm's oneOf dropdown renderer requires ``oneOf`` at the schema level
    (not nested inside ``items``).  So we promote the enum values to top-level
    ``oneOf`` with ``const``+``title`` pairs, change ``type`` to ``"string"``,
    and drop ``items``.  The frontend unwraps/wraps the array ↔ string value.
    """
    items = at_schema.get("items")
    # Try items.enum first (legacy behavior)
    enum_vals = items.get("enum") if isinstance(items, dict) else None
    # Fallback: contains.enum
    if not enum_vals:
        contains = at_schema.get("contains")
        if isinstance(contains, dict):
            enum_vals = contains.get("enum")
    if not enum_vals or not isinstance(enum_vals, list):
        return

    one_of = []
    for val in enum_vals:
        label = _id_to_label(val)
        one_of.append({"const": val, "title": label})

    # Flatten: array with items → string with oneOf
    at_schema["type"] = "string"
    at_schema["oneOf"] = one_of
    at_schema.pop("items", None)
    at_schema.pop("contains", None)
    at_schema.pop("default", None)


def convert_additional_type_to_oneof(schema: Any) -> Any:
    """Recursively find schema:additionalType properties and convert
    items.enum to items.oneOf with human-readable labels."""
    if isinstance(schema, dict):
        props = schema.get("properties")
        if isinstance(props, dict) and "schema:additionalType" in props:
            at = props["schema:additionalType"]
            if isinstance(at, dict):
                _convert_at_enum_to_oneof(at)

        # Recurse into all dict values
        for v in schema.values():
            convert_additional_type_to_oneof(v)
    elif isinstance(schema, list):
        for item in schema:
            convert_additional_type_to_oneof(item)
    return schema


# ---------------------------------------------------------------------------
# Main conversion pipeline
# ---------------------------------------------------------------------------

def convert_profile_schema(
    profile_name: str,
    verbose: bool = False,
) -> dict:
    """
    Convert a single profile's resolvedSchema.json to JSON Forms Draft 7.

    Input:  _sources/profiles/{profile}/resolvedSchema.json
    Output: Fully simplified schema with no $ref, no $defs, Draft 7 compatible.
    """
    schema_path = _find_resolved_schema(profile_name)

    if not schema_path.exists():
        print(f"ERROR: Schema not found: {schema_path}", file=sys.stderr)
        sys.exit(1)

    if verbose:
        print(f"Converting {profile_name} from {schema_path}...", file=sys.stderr)

    schema = load_json(schema_path)

    # Pipeline: apply all transformations in order.
    # First, inline all $ref pointers and merge allOf entries into a flat
    # schema.  This must happen before other passes so that enum values from
    # base building blocks and profile overrides are unioned correctly.
    schema = inline_refs_and_merge_allof(schema)

    # Note: simplify_contains_to_enum must run BEFORE simplify_const_to_default,
    # because const_to_default converts {const: X} -> {default: X}, which would
    # prevent contains_to_enum from extracting the value.
    schema = strip_metadata_keys(schema)
    schema = convert_draft_version(schema)
    schema = apply_anyof_simplifications(schema, "")
    schema = simplify_contains_to_enum(schema)
    schema = simplify_const_to_default(schema)
    schema = remove_not_constraints(schema)
    schema = flatten_remaining_allof(schema)
    schema = relax_min_items(schema)
    schema = convert_additional_type_to_oneof(schema)

    # Strip enum from top-level @type items — the pick list values are provided
    # via uischema suggestion option to avoid JSON Forms scope resolution issues
    if "properties" in schema and "@type" in schema["properties"]:
        at_type = schema["properties"]["@type"]
        if "items" in at_type and isinstance(at_type["items"], dict):
            at_type["items"].pop("enum", None)

    return schema


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Convert resolved schemas to JSON Forms Draft 7 format",
    )
    parser.add_argument(
        "--profile",
        help="Convert a single profile (e.g., CDIFDiscoveryProfile)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Convert all profiles",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print progress information",
    )
    args = parser.parse_args()

    if not args.all and not args.profile:
        parser.error("Specify --all or --profile <name>")

    profiles = ALL_PROFILES if args.all else [args.profile]

    for profile in profiles:
        schema = convert_profile_schema(profile, args.verbose)
        subdir = _profile_subdir(profile)
        output_path = OUTPUT_DIR / subdir / profile / "schema.json" if subdir else OUTPUT_DIR / profile / "schema.json"
        save_json(schema, output_path)
        if args.verbose:
            print(f"  -> {output_path}", file=sys.stderr)

        # Copy uischema.json and defaults.json from _sources/ to build/
        src_dir = _find_sources_dir(profile)
        for static_file in ("uischema.json", "defaults.json"):
            src = src_dir / static_file
            dst = output_path.parent / static_file
            if src.exists():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(str(src), str(dst))
                if args.verbose:
                    print(f"  -> {dst} (copied from _sources)", file=sys.stderr)
            elif args.verbose:
                print(f"  WARNING: {src} not found", file=sys.stderr)

    print(f"Converted {len(profiles)} profile(s) to {OUTPUT_DIR}", file=sys.stderr)


if __name__ == "__main__":
    main()
