#!/usr/bin/env python3
"""
Profile-aware validation for ADA/CDIF JSON-LD metadata instances.

Reads dcterms:conformsTo from a metadata file, maps the profile URI to a
resolved JSON Schema, and validates the instance against it.

Profile URI convention:
    ada:profile/{profileName}   →  expands to
    https://ada.astromat.org/metadata/profile/{profileName}

Usage:
    # Validate a single file (profile auto-detected from conformsTo)
    python tools/validate_instance.py example.json

    # Validate a directory of files
    python tools/validate_instance.py --dir /path/to/metadata/

    # Show only a summary table
    python tools/validate_instance.py --dir /path/to/metadata/ --summary

    # Explicit profile override (skip conformsTo detection)
    python tools/validate_instance.py example.json --profile adaEMPA

    # Fallback to termCode when conformsTo has no recognized profile
    python tools/validate_instance.py --dir /path/to/metadata/ --termcode-fallback

    # Use a different schema root
    python tools/validate_instance.py example.json --schema-root /other/bblocks/
"""

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Optional

try:
    import jsonschema
except ImportError:
    sys.exit("jsonschema package is required: pip install jsonschema")

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILES_DIR = REPO_ROOT / "_sources" / "profiles"

# All known profiles and their resolved schema locations
KNOWN_PROFILES = [
    "adaProduct", "adaEMPA", "adaXRD", "adaICPMS", "adaVNMIR",
    "adaAIVA", "adaAMS", "adaARGT", "adaDSC", "adaEAIRMS",
    "adaFTICRMS", "adaGCMS", "adaGPYC", "adaIC", "adaICPOES",
    "adaL2MS", "adaLAF", "adaLCMS", "adaLIT", "adaNGNSMS",
    "adaNanoIR", "adaNanoSIMS", "adaPSFD", "adaQRIS", "adaRAMAN",
    "adaRITOFNGMS", "adaSEM", "adaSIMS", "adaSLS", "adaSVRUEC",
    "adaTEM", "adaToFSIMS", "adaUVFM", "adaVLM", "adaXANES", "adaXCT",
    "CDIFDiscoveryProfile", "CDIFxasProfile",
]

# Namespace prefix → expanded base URI
ADA_PROFILE_PREFIX = "ada:profile/"
ADA_PROFILE_EXPANDED_PREFIX = "https://ada.astromat.org/metadata/profile/"
CDIF_PROFILE_PREFIX = "cdif:profile_"

# Map profile URIs (both prefixed and expanded) → profile name
PROFILE_URI_MAP = {}
for _name in KNOWN_PROFILES:
    if _name.startswith("ada") or _name.startswith("CDIF"):
        PROFILE_URI_MAP[f"{ADA_PROFILE_PREFIX}{_name}"] = _name
        PROFILE_URI_MAP[f"{ADA_PROFILE_EXPANDED_PREFIX}{_name}"] = _name
# CDIF discovery URI
PROFILE_URI_MAP["https://w3id.org/cdif/profiles/discovery"] = "CDIFDiscoveryProfile"

# termCode → profile mapping (for --termcode-fallback)
TERMCODE_TO_PROFILE = {
    "AIVA": "adaAIVA",
    "AMS": "adaAMS",
    "ARGT": "adaARGT",
    "DSC": "adaDSC",
    "EA-IRMS": "adaEAIRMS",
    "EMPA": "adaEMPA",
    "FIB-SEM": "adaSEM",
    "FTICR-MS": "adaFTICRMS",
    "GC-MS": "adaGCMS",
    "GPYC": "adaGPYC",
    "HR-ICP-MS": "adaICPMS",
    "IC": "adaIC",
    "ICP-OES": "adaICPOES",
    "LAF": "adaLAF",
    "LC-MS": "adaLCMS",
    "LIT": "adaLIT",
    "MC-ICP-MS": "adaICPMS",
    "NanoIR": "adaNanoIR",
    "NanoSIMS": "adaNanoSIMS",
    "NG-NS-MS": "adaNGNSMS",
    "PSFD": "adaPSFD",
    "Q-ICP-MS": "adaICPMS",
    "QRIS": "adaQRIS",
    "RAMAN": "adaRAMAN",
    "RI-TOF-NGMS": "adaRITOFNGMS",
    "SEM": "adaSEM",
    "SIMS": "adaSIMS",
    "SLS": "adaSLS",
    "SV-RUEC": "adaSVRUEC",
    "TEM": "adaTEM",
    "ToF-SIMS": "adaToFSIMS",
    "uL2MS": "adaL2MS",
    "UVFM": "adaUVFM",
    "VLM": "adaVLM",
    "VLMBasemap": "adaVLM",
    "VNMIR": "adaVNMIR",
    "XANES": "adaXANES",
    "XCT": "adaXCT",
    "XRD": "adaXRD",
}
DEFAULT_PROFILE = "adaProduct"


# ---------------------------------------------------------------------------
# Schema registry
# ---------------------------------------------------------------------------

class SchemaRegistry:
    """Caches loaded resolvedSchema.json files."""

    def __init__(self, schema_root: Path):
        self.schema_root = schema_root / "_sources" / "profiles"
        self._cache: dict[str, dict] = {}

    def _find_schema_path(self, profile_name: str) -> Path:
        """Search subdirectories for the profile's resolvedSchema.json."""
        for subdir in self.schema_root.iterdir():
            if subdir.is_dir():
                candidate = subdir / profile_name / "resolvedSchema.json"
                if candidate.exists():
                    return candidate
        # Legacy flat layout fallback
        return self.schema_root / profile_name / "resolvedSchema.json"

    def get(self, profile_name: str) -> Optional[dict]:
        if profile_name in self._cache:
            return self._cache[profile_name]
        path = self._find_schema_path(profile_name)
        if not path.exists():
            return None
        with open(path, "r", encoding="utf-8") as f:
            schema = json.load(f)
        self._cache[profile_name] = schema
        return schema

    def schema_path(self, profile_name: str) -> Path:
        return self._find_schema_path(profile_name)


# ---------------------------------------------------------------------------
# Profile detection
# ---------------------------------------------------------------------------

def extract_profile_from_conformsto(data: dict) -> Optional[str]:
    """Extract the most specific ADA/CDIF profile from dcterms:conformsTo."""
    subject_of = data.get("schema:subjectOf", {})
    conforms_to = subject_of.get("dcterms:conformsTo", [])
    if not isinstance(conforms_to, list):
        conforms_to = [conforms_to]

    found_profiles = []
    for entry in conforms_to:
        uri = entry.get("@id", "") if isinstance(entry, dict) else str(entry)
        profile = PROFILE_URI_MAP.get(uri)
        if profile and profile != "CDIFDiscoveryProfile":
            # Prefer technique-specific over CDIFDiscovery (which is a base)
            found_profiles.append(profile)

    if found_profiles:
        return found_profiles[0]
    return None


def extract_profile_from_termcode(data: dict) -> str:
    """Extract profile from schema:measurementTechnique.schema:termCode."""
    mt = data.get("schema:measurementTechnique", {})
    if isinstance(mt, list):
        for item in mt:
            if isinstance(item, dict):
                tc = item.get("schema:termCode", "")
                profile = TERMCODE_TO_PROFILE.get(tc)
                if profile:
                    return profile
        return DEFAULT_PROFILE
    term_code = mt.get("schema:termCode", "")
    return TERMCODE_TO_PROFILE.get(term_code, DEFAULT_PROFILE)


def detect_profile(data: dict, *, termcode_fallback: bool = False) -> tuple[str, str]:
    """
    Detect the profile for an instance.

    Returns (profile_name, source) where source is one of:
        "conformsTo", "termCode", "default"
    """
    profile = extract_profile_from_conformsto(data)
    if profile:
        return profile, "conformsTo"

    if termcode_fallback:
        profile = extract_profile_from_termcode(data)
        source = "termCode" if profile != DEFAULT_PROFILE else "default"
        return profile, source

    return DEFAULT_PROFILE, "default"


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_instance(data: dict, schema: dict) -> list[jsonschema.ValidationError]:
    """Validate data against schema, returning all errors."""
    validator_cls = jsonschema.Draft202012Validator
    validator = validator_cls(schema)
    return sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))


def format_error(err: jsonschema.ValidationError, index: int) -> str:
    """Format a single validation error for display."""
    path = ".".join(str(p) for p in err.absolute_path) or "(root)"
    lines = [f"  {index}. {path}"]
    lines.append(f"     Rule: {err.validator}")
    msg = err.message
    if len(msg) > 200:
        msg = msg[:200] + "..."
    lines.append(f"     {msg}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File processing
# ---------------------------------------------------------------------------

def process_file(
    filepath: Path,
    registry: SchemaRegistry,
    *,
    profile_override: Optional[str] = None,
    termcode_fallback: bool = False,
    verbose: bool = True,
) -> dict:
    """
    Validate a single file. Returns a result dict:
        {file, profile, source, status, errors, error_count}
    """
    result = {
        "file": filepath.name,
        "filepath": filepath,
        "profile": None,
        "source": None,
        "status": "ERROR",
        "errors": [],
        "error_count": 0,
    }

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as exc:
        result["errors"] = [str(exc)]
        if verbose:
            print(f"\nValidating: {filepath.name}")
            print(f"  ERROR: Could not load file: {exc}")
        return result

    # Determine profile
    if profile_override:
        profile, source = profile_override, "override"
    else:
        profile, source = detect_profile(data, termcode_fallback=termcode_fallback)

    result["profile"] = profile
    result["source"] = source

    # BB-level schema fallback: if no profile was detected, check for a
    # resolvedSchema.json in the same directory as the instance file.
    schema = None
    if source == "default":
        local_schema = filepath.parent / "resolvedSchema.json"
        if local_schema.exists():
            profile = filepath.parent.name
            source = "local"
            result["profile"] = profile
            result["source"] = source
            with open(local_schema, "r", encoding="utf-8") as f:
                schema = json.load(f)

    # Load schema from registry if not already loaded locally
    if schema is None:
        schema = registry.get(profile)
    if schema is None:
        result["errors"] = [f"Schema not found: {registry.schema_path(profile)}"]
        if verbose:
            print(f"\nValidating: {filepath.name}")
            print(f"  Profile: {profile} (from {source})")
            print(f"  ERROR: Schema not found at {registry.schema_path(profile)}")
        return result

    # Validate
    errors = validate_instance(data, schema)
    result["error_count"] = len(errors)
    result["errors"] = errors

    if errors:
        result["status"] = "FAIL"
    else:
        result["status"] = "PASS"

    if verbose:
        print(f"\nValidating: {filepath.name}")
        print(f"  Profile: {profile} (from {source})")
        if source == "local":
            print(f"  Schema:  {filepath.parent / 'resolvedSchema.json'}")
        else:
            print(f"  Schema:  _sources/profiles/{profile}/resolvedSchema.json")
        if errors:
            print(f"  Result:  FAIL ({len(errors)} error{'s' if len(errors) != 1 else ''})")
            print()
            print("  Errors:")
            for i, err in enumerate(errors[:20], 1):
                print(format_error(err, i))
            if len(errors) > 20:
                print(f"\n  ... and {len(errors) - 20} more errors")
        else:
            print("  Result:  PASS")

    return result


def print_summary(results: list[dict]) -> None:
    """Print a summary table of validation results."""
    total = len(results)
    pass_count = sum(1 for r in results if r["status"] == "PASS")
    fail_count = sum(1 for r in results if r["status"] == "FAIL")
    error_count = sum(1 for r in results if r["status"] == "ERROR")

    print("\nProfile-Aware Validation Report")
    print("=" * 40)
    print(f"Total: {total}  |  PASS: {pass_count}  |  FAIL: {fail_count}  |  ERROR: {error_count}")

    # Group by profile
    by_profile: dict[str, list[dict]] = defaultdict(list)
    for r in results:
        by_profile[r["profile"] or "UNKNOWN"].append(r)

    print("\nBy profile:")
    for profile in sorted(by_profile.keys()):
        pres = by_profile[profile]
        p = sum(1 for r in pres if r["status"] == "PASS")
        f = sum(1 for r in pres if r["status"] == "FAIL")
        e = sum(1 for r in pres if r["status"] == "ERROR")
        count_label = f"{len(pres)} file{'s' if len(pres) != 1 else ''}"
        print(f"  {profile:<14s} {count_label:<10s} {p} pass  {f} fail  {e} error")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Profile-aware validation for ADA/CDIF JSON-LD metadata."
    )
    parser.add_argument(
        "file", nargs="?",
        help="Path to a single JSON-LD metadata file to validate."
    )
    parser.add_argument(
        "--dir", "-d",
        help="Directory of JSON-LD metadata files to validate (batch mode)."
    )
    parser.add_argument(
        "--profile", "-p",
        help="Override: validate against this profile regardless of conformsTo."
    )
    parser.add_argument(
        "--termcode-fallback", action="store_true",
        help="Fall back to termCode-based profile detection if conformsTo "
             "has no recognized profile."
    )
    parser.add_argument(
        "--summary", "-s", action="store_true",
        help="Show only a summary table (batch mode)."
    )
    parser.add_argument(
        "--schema-root",
        help="Root directory for building blocks (default: auto-detect from tool location)."
    )

    args = parser.parse_args()

    if not args.file and not args.dir:
        parser.error("Provide either a file path or --dir for batch mode.")

    schema_root = Path(args.schema_root) if args.schema_root else REPO_ROOT
    registry = SchemaRegistry(schema_root)

    # Collect files
    files: list[Path] = []
    if args.file:
        files.append(Path(args.file))
    if args.dir:
        dirpath = Path(args.dir)
        if not dirpath.is_dir():
            sys.exit(f"Not a directory: {dirpath}")
        SKIP_NAMES = {"bblock.json", "resolvedSchema.json"}
        files.extend(
            f for f in sorted(dirpath.glob("*.json"))
            if f.name not in SKIP_NAMES and not f.name.endswith("Schema.json")
        )

    if not files:
        sys.exit("No JSON files found.")

    # Process
    verbose = not args.summary
    results = []
    for fp in files:
        result = process_file(
            fp, registry,
            profile_override=args.profile,
            termcode_fallback=args.termcode_fallback,
            verbose=verbose,
        )
        results.append(result)

    if args.summary or len(files) > 1:
        print_summary(results)

    # Exit code: 0 if all pass, 1 if any fail/error
    if any(r["status"] != "PASS" for r in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
