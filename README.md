# Metadata Building Blocks Repository
Created by S.M. Richard and claude-code  2026-02-15

Core modular schema components following the [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) pattern for implementation of modular interoperable metadata for the [Cross-Domain Interoperability Framework (CDIF)](https://cdif.org). Each building block is a self-contained directory with a JSON Schema, JSON-LD context, metadata, and description. Building blocks compose into profiles that define complete metadata schemas for specific use cases.

This repository contains the **shared core building blocks** (schema.org properties, CDIF properties, PROV-O provenance, data quality, XAS spectroscopy, and DDI-CDI). Domain-specific building blocks have been refactored into separate repositories:

- **[ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)** — DDE (Deep-time Digital Earth) geoscience properties and profiles (7 BBs + 11 profiles)
- **[geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)** — ADA (IEDA Analytics & Data Archive) geochemistry properties and profiles (30 BBs + 36 profiles)
- **[ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)** — ECRR (EarthCube Resource Registry) properties and profiles (10 BBs + 11 profiles)

Domain-specific repos reference core building blocks in this repository via absolute URLs (`https://usgin.github.io/metadataBuildingBlocks/_sources/...`).

For more info see [the OGC Documentation](https://ogcincubator.github.io/bblocks-docs/).

## Schema Pipeline

The schema pipeline transforms modular YAML source schemas into JSON Forms-compatible Draft 7 schemas in two steps, plus an augmentation step for the bblocks-viewer:

```
schema.yaml → resolve_schema.py → resolvedSchema.json → convert_for_jsonforms.py → schema.json
                                                       → augment_register.py → register.json (adds resolvedSchema URLs)
```

### Step 1: Resolve (`resolve_schema.py`)

Recursively resolves all `$ref` references from modular YAML/JSON source schemas into one fully-inlined JSON Schema. Handles relative paths, fragment-only refs (`#/$defs/X`), cross-file fragments, URL refs, and both YAML/JSON extensions. Optionally flattens `allOf` entries.

```bash
# Resolve a profile by name (searches cdifProfiles/ subdirectories)
python tools/resolve_schema.py CDIFDiscovery

# Resolve all building blocks with external $refs
python tools/resolve_schema.py --all

# Resolve an arbitrary schema file
python tools/resolve_schema.py --file path/to/any/schema.yaml
```

**Requirements:** Python 3.6+ with `pyyaml` (`pip install pyyaml`)

### Step 2: Convert for JSON Forms (`convert_for_jsonforms.py`)

Reads `resolvedSchema.json` and converts to JSON Forms-compatible Draft 7:
- Converts `$schema` from Draft 2020-12 to Draft 7
- Simplifies `anyOf` patterns for form rendering
- Converts `contains` → `enum`, `const` → `default`
- Removes `not` constraints and relaxes `minItems`

```bash
# Convert all profiles
python tools/convert_for_jsonforms.py --all -v

# Convert a single profile
python tools/convert_for_jsonforms.py CDIFDiscovery -v
```

### Step 3: Augment register.json (`augment_register.py`)

Adds `resolvedSchema` URLs to `build/register.json` for each profile building block that has a `resolvedSchema.json` file. This enables the bblocks-viewer's "Resolved (JSON)" button to fetch and display the fully resolved schema (all `$ref` inlined, `allOf` flattened).

```bash
python tools/augment_register.py
```

The `generate-jsonforms` workflow runs this automatically after schema conversion.

## Profiles

CDIF profiles are in `_sources/profiles/cdifProfiles/`:

| Profile | Description |
|---|---|
| `CDIFDiscovery` | CDIF Discovery profile — general-purpose dataset metadata (allOf: cdifMandatory + cdifOptional) |
| `CDIFcomplete` | CDIF Complete profile — CDIFDiscovery + cdifProv + extended distribution (3 anyOf branches: DataDownload, archive, WebAPI) |
| `CDIFDataDescription` | CDIF Data Description profile |
| `CDIFxas` | CDIF XAS profile — CDIFcomplete + XAS-specific properties |

See [agents.md](agents.md) for the full building block structure, authoring rules, and composition hierarchy.

## Building Block Categories

| Category | Directory | Description |
|----------|-----------|-------------|
| schemaorgProperties | `_sources/schemaorgProperties/` | schema.org vocabulary building blocks (person, organization, identifier, definedTerm, instrument, etc.) |
| cdifProperties | `_sources/cdifProperties/` | CDIF-specific properties (mandatory, optional, provenance, tabular data, long data, etc.) |
| ddiProperties | `_sources/ddiProperties/` | DDI-CDI vocabulary building blocks |
| provProperties | `_sources/provProperties/` | PROV-O provenance (generatedBy, derivedFrom, provActivity) |
| qualityProperties | `_sources/qualityProperties/` | DQV data quality measures |
| xasProperties | `_sources/xasProperties/` | X-ray Absorption Spectroscopy domain properties |
| profiles | `_sources/profiles/cdifProfiles/` | CDIF profiles |

### ddiProperties

DDI-CDI vocabulary building blocks for communities using the DDI Cross-Domain Integration standard natively.

| Building Block | Description |
|----------------|-------------|
| `ddicdiProv` | DDI-CDI native provenance activity -- expresses workflows using `cdi:Activity`, `cdi:Step`, `cdi:ProcessingAgent`, and `cdi:Parameter`. Alternative to the schema.org/PROV-based `cdifProv` building block. Includes JSON Schema with `anyOf [inline-type, id-reference]` pattern for graph node links, SHACL validation shapes, and a soil chemistry analysis example as a multi-node `@graph` document. |

### schemaorgProperties

Schema.org vocabulary building blocks for reusable metadata components.

| Building Block | Description |
|----------------|-------------|
| `instrument` | Generic instrument or instrument system -- uses `schema:Thing` base type with optional `schema:Product` typing. Supports hierarchical instrument systems via `schema:hasPart` for sub-components. Instruments are nested within `prov:used` items via a `schema:instrument` sub-key (instruments are `prov:Entity` subclasses). Referenced by `cdifProv`, `provActivity`, and `xasInstrument`. |

### provProperties

PROV-O provenance building blocks.

| Building Block | Description |
|----------------|-------------|
| `generatedBy` | Base provenance activity -- minimal `prov:Activity` with `prov:used`. Extended by `cdifProv` and `provActivity`. |
| `provActivity` | PROV-O native provenance activity -- extends `generatedBy` with W3C PROV-O properties (`prov:wasAssociatedWith`, `prov:startedAtTime`, `prov:endedAtTime`, `prov:atLocation`, `prov:wasInformedBy`, `prov:generated`). Uses schema.org fallbacks only where PROV-O has no equivalent (name, description, methodology, status). Instruments nested in `prov:used` via `schema:instrument` sub-key. |
| `derivedFrom` | Provenance derivation -- `prov:wasDerivedFrom` linking. |

### Provenance Layering

The repository implements a three-tier provenance architecture:

| Tier | Building Block | Introduced At | Description |
|------|---------------|---------------|-------------|
| 1 (simple) | `generatedBy` (provProperties) | `cdifOptional` | Minimal `prov:Activity` — `prov:used` accepts only string names or `@id` references |
| 2 (extended) | `cdifProv` (cdifProperties) | `CDIFcomplete` | Extends `generatedBy` with schema.org Action properties (`schema:agent`, `schema:actionProcess`, `schema:object`, `schema:result`, temporal bounds, location). Requires `@type: ["schema:Action", "prov:Activity"]`. Instruments nested in `prov:used` via `schema:instrument` sub-key. |
| 3 (domain) | `xasGeneratedBy`, etc. | Domain-specific profiles | Extend `cdifProv` with domain-specific instrument types, agents, and additional properties (see [ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks), [geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)) |

### xasProperties

| Building Block | Description |
|----------------|-------------|
| `xasInstrument` | XAS instrument with `schema:hasPart` for hierarchical sub-components (refs generic instrument building block). |
| `xasGeneratedBy` | XAS analysis event — extends `cdifProv` with `xas:AnalysisEvent` typing, XAS facility location, sample object, XAS-specific instrument types, and XAS additional properties (edge_energy, calibration method, etc.). |
| `xasRequired` | XAS mandatory properties — `prov:wasGeneratedBy` items use `allOf` with `cdifProv` + NXsource/NXmonochromator instrument constraints via `schema:instrument` sub-key. |
| `xasOptional` | Same provenance structure as `xasRequired` — `cdifProv` activity with XAS instrument constraints. |

## Building Block Identifiers and Web Resolution

Each building block has a persistent HTTP URI under `https://w3id.org/cdif/bbr/metadata/`. The URI pattern is:

```
https://w3id.org/cdif/bbr/metadata/{category}/{name}
```

where `{category}` is one of `schemaorgProperties`, `cdifProperties`, `provProperties`, `qualityProperties`, `ddiProperties`, `xasProperties` and `{name}` is the building block directory name (e.g., `person`, `cdifProv`, `xasGeneratedBy`).

Examples:
- `https://w3id.org/cdif/bbr/metadata/schemaorgProperties/person`
- `https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifProv`
- `https://w3id.org/cdif/bbr/metadata/xasProperties/xasGeneratedBy`

The register root `https://w3id.org/cdif/bbr/metadata` resolves to the building blocks viewer home page.

All redirects use HTTP 303 (See Other).

### Content negotiation

A single building block URI serves different representations depending on the `Accept` header:

| Accept header | Returns |
|---|---|
| `text/html` (default) | Landing page in the building blocks viewer |
| `application/schema+json` | JSON Schema (JSON format) |
| `application/yaml` | JSON Schema (YAML format) |
| `text/turtle` | SHACL validation rules (Turtle) |
| `application/ld+json` | JSON-LD context |
| `application/json` | Full JSON documentation |

```bash
# Landing page (browser default)
curl -L https://w3id.org/cdif/bbr/metadata/schemaorgProperties/person

# JSON Schema
curl -L -H "Accept: application/schema+json" \
  https://w3id.org/cdif/bbr/metadata/schemaorgProperties/person

# SHACL rules
curl -L -H "Accept: text/turtle" \
  https://w3id.org/cdif/bbr/metadata/schemaorgProperties/person

# JSON-LD context
curl -L -H "Accept: application/ld+json" \
  https://w3id.org/cdif/bbr/metadata/schemaorgProperties/person
```

### Explicit sub-path resources

These resolve directly to the named resource regardless of `Accept` header:

| Sub-path | Returns |
|---|---|
| `.../{category}/{name}/schema` | JSON Schema (YAML; or JSON via `Accept: application/json`) |
| `.../{category}/{name}/resolved` | Resolved schema -- all `$ref` inlined (JSON) |
| `.../{category}/{name}/shacl` | SHACL validation rules (Turtle) |
| `.../{category}/{name}/context` | JSON-LD context |

```bash
curl -L https://w3id.org/cdif/bbr/metadata/schemaorgProperties/person/schema
curl -L https://w3id.org/cdif/bbr/metadata/schemaorgProperties/person/resolved
curl -L https://w3id.org/cdif/bbr/metadata/schemaorgProperties/person/shacl
curl -L https://w3id.org/cdif/bbr/metadata/schemaorgProperties/person/context
```

## License

This material is based upon work supported by the National Science Foundation (NSF) under awards 2012893, 2012748, and 2012593.
