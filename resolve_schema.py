#!/usr/bin/env python3
"""
JSON Schema Reference Resolver for OGC Building Blocks

This program reads a building block JSON schema and generates a complete
standalone schema by resolving all external $ref references recursively.
All definitions are flattened to a single top-level $defs section.

With the --inline-single-use flag, definitions that are only referenced once
are inlined directly into the schema, while definitions used multiple times
remain in the $defs section. This produces a more compact, readable schema
similar to hand-authored schemas.

Usage:
    python resolve_schema.py <input_schema_path> [output_path]

Examples:
    python resolve_schema.py _sources/profiles/CDIFDiscovery/CDIFDiscoverySchema.json
    python resolve_schema.py _sources/cdifProperties/cdifCore/cdifCoreSchema.json output.json
    python resolve_schema.py schema.json -o output.json --inline-single-use
"""

import json
import os
import sys
import copy
import argparse
from pathlib import Path
from urllib.parse import urldefrag
from typing import Any, Dict, Set, Optional, Tuple

import yaml


class SchemaResolver:
    """Resolves all $ref references in a JSON Schema to produce a standalone schema."""

    def __init__(self, verbose: bool = False, inline_single_use: bool = False):
        """
        Initialize the resolver.

        Args:
            verbose: If True, print progress information
            inline_single_use: If True, inline definitions that are only referenced once
        """
        self.verbose = verbose
        self.inline_single_use = inline_single_use
        self.schema_cache: Dict[str, dict] = {}  # Cache loaded schemas by absolute path
        self.global_defs: Dict[str, dict] = {}  # All flattened definitions
        self.processing_stack: Set[str] = set()  # Track schemas being processed (cycle detection)
        # Maps absolute file path (optionally with fragment) -> global def name
        self.file_to_def_name: Dict[str, str] = {}
        self.warnings: list = []

    def log(self, message: str) -> None:
        """Print a message if verbose mode is enabled."""
        if self.verbose:
            print(message, file=sys.stderr)

    def warn(self, message: str) -> None:
        """Record a warning message."""
        self.warnings.append(message)
        if self.verbose:
            print(f"WARNING: {message}", file=sys.stderr)

    def load_schema(self, schema_path: Path) -> dict:
        """
        Load a JSON schema from file, using cache if available.

        Args:
            schema_path: Absolute path to the schema file

        Returns:
            The loaded schema as a dictionary
        """
        path_str = str(schema_path)
        if path_str not in self.schema_cache:
            self.log(f"Loading: {schema_path}")
            with open(schema_path, 'r', encoding='utf-8') as f:
                suffix = schema_path.suffix.lower()
                if suffix in ('.yaml', '.yml'):
                    self.schema_cache[path_str] = yaml.safe_load(f)
                else:
                    self.schema_cache[path_str] = json.load(f)
        return copy.deepcopy(self.schema_cache[path_str])

    def resolve_path(self, ref_path: str, current_dir: Path) -> Path:
        """
        Resolve a relative reference path to an absolute path.

        Args:
            ref_path: The reference path (may be relative)
            current_dir: The directory of the current schema file

        Returns:
            Absolute path to the referenced file
        """
        resolved = (current_dir / ref_path).resolve()
        return resolved

    def parse_ref(self, ref: str) -> Tuple[str, Optional[str]]:
        """
        Parse a $ref into file path and fragment components.

        Args:
            ref: The $ref value (e.g., "../file.json#/$defs/Name")

        Returns:
            Tuple of (file_path, fragment) where fragment may be None
        """
        url, fragment = urldefrag(ref)
        return url, fragment if fragment else None

    def resolve_fragment(self, schema: dict, fragment: str) -> dict:
        """
        Resolve a JSON pointer fragment within a schema.

        Args:
            schema: The schema to resolve within
            fragment: JSON pointer (e.g., "/$defs/Name")

        Returns:
            The resolved sub-schema
        """
        if not fragment:
            return schema

        # Remove leading slash and split
        parts = fragment.lstrip('/').split('/')
        current = schema

        for part in parts:
            # Handle array indices
            if isinstance(current, list):
                current = current[int(part)]
            else:
                current = current[part]

        return current

    def get_schema_base_name(self, schema_path: Path) -> str:
        """
        Extract base name from schema path.

        Uses the parent directory name when the filename is generic (e.g.,
        "schema.yaml"), since building blocks all use that convention.

        Args:
            schema_path: Path to schema file

        Returns:
            Base name (e.g., "Person" from "personSchema.json",
            "VariableMeasured" from "variableMeasured/schema.yaml")
        """
        filename = schema_path.stem
        if filename.endswith('Schema'):
            name = filename[:-6]
        elif filename.lower() == 'schema':
            # Generic filename — use parent directory name instead
            name = schema_path.parent.name
        else:
            name = filename
        # Capitalize first letter for consistency
        return name[0].upper() + name[1:] if name else name

    def generate_unique_name(self, base_name: str) -> str:
        """
        Generate a unique definition name, handling collisions.

        Args:
            base_name: The desired name

        Returns:
            A unique name not already in global_defs
        """
        name = base_name
        counter = 2

        while name in self.global_defs:
            name = f"{base_name}_{counter}"
            counter += 1

        return name

    def get_or_create_def_for_file(self, schema_path: Path, fragment: Optional[str] = None) -> str:
        """
        Get or create a global definition for a file (or fragment thereof).

        Args:
            schema_path: Absolute path to the schema file
            fragment: Optional fragment pointer

        Returns:
            The name of the global definition
        """
        cache_key = f"{schema_path}#{fragment or ''}"

        # Check if we already have a definition for this file
        if cache_key in self.file_to_def_name:
            return self.file_to_def_name[cache_key]

        # Generate a name for this schema
        if fragment:
            frag_parts = fragment.lstrip('/').split('/')
            if len(frag_parts) >= 2 and frag_parts[0] == '$defs':
                base_name = frag_parts[1]
            else:
                base_name = self.get_schema_base_name(schema_path)
        else:
            base_name = self.get_schema_base_name(schema_path)

        def_name = self.generate_unique_name(base_name)
        self.file_to_def_name[cache_key] = def_name

        # Process and store the definition
        if cache_key not in self.processing_stack:
            self.processing_stack.add(cache_key)
            try:
                schema = self.load_schema(schema_path)

                if fragment:
                    schema = self.resolve_fragment(schema, fragment)

                # Process the schema recursively, passing the source file
                # so internal #/$defs/ refs can be resolved against it
                processed = self.process_schema(schema, schema_path.parent,
                                                source_file=schema_path)

                # Remove nested $defs - they've been flattened
                if isinstance(processed, dict):
                    processed.pop('$defs', None)

                self.global_defs[def_name] = processed

            finally:
                self.processing_stack.discard(cache_key)

        return def_name

    def process_schema(self, schema: Any, current_dir: Path,
                       source_file: Optional[Path] = None) -> Any:
        """
        Recursively process a schema, resolving all external references.

        Args:
            schema: The schema to process
            current_dir: Current directory for resolving relative paths
            source_file: The file this schema was loaded from (used to resolve
                internal #/$defs/ refs within external files)

        Returns:
            Processed schema with external references converted to local $defs references
        """
        if isinstance(schema, dict):
            # Handle $ref
            if '$ref' in schema:
                ref = schema['$ref']
                file_path, fragment = self.parse_ref(ref)

                if file_path:
                    # External reference
                    abs_path = self.resolve_path(file_path, current_dir)
                    def_name = self.get_or_create_def_for_file(abs_path, fragment)
                    # Keep any other properties alongside $ref (though rare)
                    if len(schema) == 1:
                        return {"$ref": f"#/$defs/{def_name}"}
                    else:
                        result = {k: v for k, v in schema.items() if k != '$ref'}
                        result["$ref"] = f"#/$defs/{def_name}"
                        return result
                else:
                    # Internal reference (#/$defs/X)
                    # If we're processing an external file, resolve internal
                    # $defs refs against that source file so transitive defs
                    # get promoted to global scope
                    if source_file and fragment and fragment.startswith('/$defs/'):
                        def_name = self.get_or_create_def_for_file(
                            source_file, fragment)
                        if len(schema) == 1:
                            return {"$ref": f"#/$defs/{def_name}"}
                        else:
                            result = {k: v for k, v in schema.items()
                                      if k != '$ref'}
                            result["$ref"] = f"#/$defs/{def_name}"
                            return result
                    return schema

            # Check for malformed schemas that use "$defs" where "$ref" was intended
            # This handles typos like {"$defs": "path/to/file.json"}
            if '$defs' in schema and isinstance(schema['$defs'], str):
                # This looks like a typo - "$defs" used instead of "$ref"
                self.warn(f"Found '$defs' with string value (likely should be '$ref'): {schema['$defs']}")
                ref = schema['$defs']
                file_path, fragment = self.parse_ref(ref)
                if file_path:
                    abs_path = self.resolve_path(file_path, current_dir)
                    def_name = self.get_or_create_def_for_file(abs_path, fragment)
                    result = {k: v for k, v in schema.items() if k != '$defs'}
                    result["$ref"] = f"#/$defs/{def_name}"
                    return result

            # Process $defs - each def becomes a global definition
            result = {}
            if '$defs' in schema and isinstance(schema['$defs'], dict):
                for local_name, local_def in schema['$defs'].items():
                    if isinstance(local_def, dict) and '$ref' in local_def and len(local_def) == 1:
                        # This def is a reference to external schema
                        ref = local_def['$ref']
                        file_path, fragment = self.parse_ref(ref)
                        if file_path:
                            abs_path = self.resolve_path(file_path, current_dir)
                            # Get or create a def and map local name to it
                            global_def_name = self.get_or_create_def_for_file(abs_path, fragment)
                            # Create an alias if the local name differs
                            if local_name != global_def_name:
                                self.global_defs[local_name] = {"$ref": f"#/$defs/{global_def_name}"}
                        else:
                            # Internal reference in $defs - just process it
                            processed_def = self.process_schema(local_def, current_dir, source_file=source_file)
                            if local_name not in self.global_defs:
                                self.global_defs[local_name] = processed_def
                    elif isinstance(local_def, dict) and '$defs' in local_def and isinstance(local_def['$defs'], str):
                        # Handle malformed def: {"$defs": "path/to/file"} instead of {"$ref": ...}
                        self.warn(f"Found '$defs' with string value in definition '{local_name}' (likely should be '$ref'): {local_def['$defs']}")
                        ref = local_def['$defs']
                        file_path, fragment = self.parse_ref(ref)
                        if file_path:
                            abs_path = self.resolve_path(file_path, current_dir)
                            global_def_name = self.get_or_create_def_for_file(abs_path, fragment)
                            if local_name != global_def_name:
                                self.global_defs[local_name] = {"$ref": f"#/$defs/{global_def_name}"}
                    else:
                        # Inline definition
                        processed_def = self.process_schema(local_def, current_dir, source_file=source_file)
                        if isinstance(processed_def, dict):
                            processed_def.pop('$defs', None)
                        if local_name not in self.global_defs:
                            self.global_defs[local_name] = processed_def

            # Process all other keys
            for key, value in schema.items():
                if key == '$defs':
                    continue  # Already processed
                result[key] = self.process_schema(value, current_dir, source_file=source_file)

            return result

        elif isinstance(schema, list):
            return [self.process_schema(item, current_dir, source_file=source_file) for item in schema]

        else:
            return schema

    def resolve(self, schema_path: str) -> dict:
        """
        Resolve all references in a schema file and produce a standalone schema.

        Args:
            schema_path: Path to the root schema file

        Returns:
            Complete standalone schema with no external references
        """
        root_path = Path(schema_path).resolve()
        self.log(f"Resolving schema: {root_path}")

        # Load and process the root schema
        root_schema = self.load_schema(root_path)
        result = self.process_schema(root_schema, root_path.parent)

        # Add global $defs to result (if not already present)
        if self.global_defs:
            if '$defs' not in result:
                result['$defs'] = {}
            for name, definition in self.global_defs.items():
                if name not in result['$defs']:
                    result['$defs'][name] = definition

        # Optionally inline single-use definitions
        if self.inline_single_use:
            result = self.optimize_inlining(result)

        return result

    def count_refs(self, schema: Any, counts: Dict[str, int]) -> None:
        """
        Count references to each $def in the schema.

        Args:
            schema: The schema to scan
            counts: Dictionary to update with reference counts
        """
        if isinstance(schema, dict):
            if '$ref' in schema:
                ref = schema['$ref']
                if ref.startswith('#/$defs/'):
                    def_name = ref[8:]  # Remove '#/$defs/' prefix
                    counts[def_name] = counts.get(def_name, 0) + 1
            for key, value in schema.items():
                if key != '$defs':  # Don't count references within $defs itself
                    self.count_refs(value, counts)
        elif isinstance(schema, list):
            for item in schema:
                self.count_refs(item, counts)

    def count_refs_in_defs(self, defs: Dict[str, Any], counts: Dict[str, int]) -> None:
        """
        Count references within $defs to other $defs.

        Args:
            defs: The $defs dictionary
            counts: Dictionary to update with reference counts
        """
        for def_name, definition in defs.items():
            self.count_refs(definition, counts)

    def inline_refs(self, schema: Any, defs: Dict[str, Any], single_use: Set[str]) -> Any:
        """
        Replace single-use $ref with inlined definitions.

        Args:
            schema: The schema to process
            defs: The $defs dictionary
            single_use: Set of definition names that are only used once

        Returns:
            Schema with single-use refs inlined
        """
        if isinstance(schema, dict):
            if '$ref' in schema and len(schema) == 1:
                ref = schema['$ref']
                if ref.startswith('#/$defs/'):
                    def_name = ref[8:]
                    if def_name in single_use and def_name in defs:
                        # Inline this definition
                        inlined = copy.deepcopy(defs[def_name])
                        # Recursively inline within the inlined definition
                        return self.inline_refs(inlined, defs, single_use)
            # Process all values in the dict
            result = {}
            for key, value in schema.items():
                if key == '$defs':
                    # Filter out single-use defs
                    result[key] = {
                        k: self.inline_refs(v, defs, single_use)
                        for k, v in value.items()
                        if k not in single_use
                    }
                    # Remove $defs entirely if empty
                    if not result[key]:
                        del result[key]
                else:
                    result[key] = self.inline_refs(value, defs, single_use)
            return result
        elif isinstance(schema, list):
            return [self.inline_refs(item, defs, single_use) for item in schema]
        else:
            return schema

    def optimize_inlining(self, schema: dict) -> dict:
        """
        Inline definitions that are only referenced once.

        Args:
            schema: The resolved schema with all definitions in $defs

        Returns:
            Optimized schema with single-use definitions inlined
        """
        if '$defs' not in schema:
            return schema

        defs = schema['$defs']

        # Count references in main schema (excluding $defs section)
        counts: Dict[str, int] = {}
        for key, value in schema.items():
            if key != '$defs':
                self.count_refs(value, counts)

        # Also count references within $defs to other $defs
        self.count_refs_in_defs(defs, counts)

        # Find definitions used only once
        single_use = {name for name, count in counts.items() if count == 1}

        # Also include defs that are never referenced (count == 0 or not in counts)
        # These might be aliases or unused - include them for inlining too
        for def_name in defs:
            if def_name not in counts:
                single_use.add(def_name)

        self.log(f"Single-use definitions to inline: {single_use}")
        self.log(f"Multi-use definitions to keep: {set(defs.keys()) - single_use}")

        # Inline single-use definitions
        result = self.inline_refs(schema, defs, single_use)

        return result


def main():
    parser = argparse.ArgumentParser(
        description='Resolve JSON Schema references to produce a standalone schema',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python resolve_schema.py _sources/profiles/CDIFDiscovery/CDIFDiscoverySchema.json
    python resolve_schema.py _sources/cdifProperties/cdifCore/cdifCoreSchema.json -o output.json
    python resolve_schema.py _sources/cdifProperties/cdifOptional/cdifOptionalSchema.json -v
        """
    )

    parser.add_argument(
        'input_schema',
        help='Path to the input JSON schema file'
    )

    parser.add_argument(
        '-o', '--output',
        help='Output file path (default: prints to stdout)'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Print progress information'
    )

    parser.add_argument(
        '--indent',
        type=int,
        default=2,
        help='JSON indentation level (default: 2)'
    )

    parser.add_argument(
        '--inline-single-use',
        action='store_true',
        help='Inline definitions that are only referenced once (produces more compact schema)'
    )

    args = parser.parse_args()

    # Check if input file exists
    if not os.path.isfile(args.input_schema):
        print(f"Error: Input file not found: {args.input_schema}", file=sys.stderr)
        sys.exit(1)

    # Create resolver and process
    resolver = SchemaResolver(verbose=args.verbose, inline_single_use=args.inline_single_use)

    try:
        result = resolver.resolve(args.input_schema)

        # Print warnings at the end
        if resolver.warnings:
            print("\n--- WARNINGS ---", file=sys.stderr)
            for warning in resolver.warnings:
                print(f"  - {warning}", file=sys.stderr)
            print("----------------\n", file=sys.stderr)

        # Output the result
        output_json = json.dumps(result, indent=args.indent, ensure_ascii=False)

        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output_json)
            if args.verbose:
                print(f"Output written to: {args.output}", file=sys.stderr)
        else:
            print(output_json)

    except FileNotFoundError as e:
        print(f"Error: Referenced file not found: {e}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in schema file: {e}", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Invalid YAML in schema file: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Missing key in schema: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
