# USGIN Metadata Building Blocks Repository
Created by S.M. Richard and claude-code  2026-02-15


Modular schema components following the [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) pattern for the [IEDA Data Submission Portal](https://github.com/smrgeoinfo/IEDADataSubmission) and for implementation of modular inteoperable metadata for the [Cross-Domain Interoperability Framework (CDIF)](https://cdif.org). Each building block is a self-contained directory with a JSON Schema, JSON-LD context, metadata, and description. Building blocks compose into profiles that define complete metadata schemas for specific use cases.

For more info see [the OGC Documentation](https://ogcincubator.github.io/bblocks-docs/).

## Schema Pipeline

The schema pipeline transforms modular YAML source schemas into JSON Forms-compatible Draft 7 schemas in two steps, plus an augmentation step for the bblocks-viewer:

```
schema.yaml → resolve_schema.py → resolvedSchema.json → convert_for_jsonforms.py → schema.json
                                                       → augment_register.py → register.json (adds resolvedSchema URLs)
```

### Step 1: Resolve (`resolve_schema.py`)

Recursively resolves all `$ref` references from modular YAML/JSON source schemas into one fully-inlined JSON Schema. Handles relative paths, fragment-only refs (`#/$defs/X`), cross-file fragments, and both YAML/JSON extensions. Optionally flattens `allOf` entries.

```bash
# Resolve a profile by name (searches adaProfiles/ and cdifProfiles/ subdirectories)
python tools/resolve_schema.py adaProduct

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
- Merges technique profile constraints into distribution branches
- Preserves `oneOf` in distribution (3 branches: single file, archive, WebAPI)
- Merges file-type `anyOf` (from `files/schema.yaml`) into flat hasPart item properties
- Removes `not` constraints and relaxes `minItems`

```bash
# Convert all profiles
python tools/convert_for_jsonforms.py --all -v

# Convert a single profile
python tools/convert_for_jsonforms.py adaEMPA -v
```

### Step 3: Augment register.json (`augment_register.py`)

Adds `resolvedSchema` URLs to `build/register.json` for each profile building block that has a `resolvedSchema.json` file. This enables the bblocks-viewer's "Resolved (JSON)" button to fetch and display the fully resolved schema (all `$ref` inlined, `allOf` flattened).

```bash
python tools/augment_register.py
```

The `generate-jsonforms` workflow runs this automatically after schema conversion.

## Profiles (62 total)

Profiles are organized into subdirectories: `_sources/profiles/adaProfiles/` (36 ADA profiles), `_sources/profiles/cdifProfiles/` (4 CDIF profiles), `_sources/profiles/DDEProfiles/` (11 DDE profiles), and `_sources/profiles/ecrrProfiles/` (11 ECRR profiles).

| Profile | Description |
|---|---|
| `adaProduct` | Base ADA product metadata — distribution has 3 `oneOf` branches (single file, archive, WebAPI) |
| `adaEMPA` | Electron Microprobe Analysis — constrains component types to EMPA-valid file types |
| `adaXRD` | X-ray Diffraction — constrains to XRD-valid component and file types |
| `adaICPMS` | ICP Mass Spectrometry — constrains to ICP-MS-valid component and file types (HR/Q/MC) |
| `adaVNMIR` | Very-Near Mid-IR / FTIR — constrains to VNMIR-valid component and file types |
| `CDIFDiscovery` | CDIF Discovery profile — general-purpose dataset metadata |
| `DDEDiscovery` | DDE Geoscience Discovery profile (base) — extends CDIF Discovery with DDE resource types, topic/acquisition keywords, and browse graphics |
| `DDEDataset` | DDE Dataset — dataset, dataCatalog, geographicDataset, nonGeographicDataset |
| `DDECollection` | DDE Collection — aggregate, collection, series, learningResource, guide (requires hasPart) |
| `DDEDocument` | DDE Document — document, article, thesis, book, poster, webPage |
| `DDEImage` | DDE Image — image, map, photograph, explanatoryFigure (includes ddeImagery) |
| `DDEService` | DDE Service — repository, service, webAPI (includes ddeServiceInfo) |
| `DDESoftware` | DDE Software — software |
| `DDEEvent` | DDE Event — initiative, fieldSession (requires temporalCoverage) |
| `DDEFunctionalResource` | DDE Functional Resource — application, webApplication, model (requires implementationSoftware link) |
| `DDESemanticResource` | DDE Semantic Resource — semanticResource, definedTermSet |
| `DDEAudioVisualProduct` | DDE AudioVisual Product — movie, sound |
| 31 more | Generated by `tools/generate_profiles.py`: adaAIVA, adaAMS, adaARGT, adaDSC, adaEAIRMS, adaFTICRMS, adaGCMS, adaGPYC, adaIC, adaICPOES, adaL2MS, adaLAF, adaLCMS, adaLIT, adaNGNSMS, adaNanoIR, adaNanoSIMS, adaPSFD, adaQRIS, adaRAMAN, adaRITOFNGMS, adaSEM, adaSIMS, adaSLS, adaSVRUEC, adaTEM, adaToFSIMS, adaUVFM, adaVLM, adaXANES, adaXCT |
| `ECRRDataset` | ECRR Dataset — extends CDIFcomplete + ecrrBase + ecrrAssessment with ECRR-unique properties inline |
| `ECRRService` | ECRR Service Instance — ecrrBase + ecrrCommon + ecrrAssessment + ecrrService |
| `ECRRSoftware` | ECRR Software — ecrrBase + ecrrCommon + ecrrAssessment + ecrrSoftware |
| `ECRRSpecification` | ECRR Specification — ecrrBase + ecrrCommon + ecrrAssessment + ecrrSpecification |
| `ECRRCatalog` | ECRR Catalog/Registry — ecrrBase + ecrrCommon + ecrrAssessment + ecrrCatalog |
| `ECRRCollection` | ECRR Bundled Object — ecrrBase + ecrrCommon + ecrrAssessment + ecrrCollection |
| `ECRRSemanticResource` | ECRR Semantic Resource — ecrrBase + ecrrCommon + ecrrAssessment + ecrrSemanticResource |
| `ECRRUseCase` | ECRR Use Case — ecrrBase + ecrrCommon + ecrrAssessment (base-only) |
| `ECRRInterface` | ECRR Interface/API — ecrrBase + ecrrCommon + ecrrAssessment (base-only) |
| `ECRRInterchangeFormat` | ECRR Interchange Format — ecrrBase + ecrrCommon + ecrrAssessment (base-only) |
| `ECRRPlatform` | ECRR Platform — ecrrBase + ecrrCommon + ecrrAssessment (base-only) |

Run `python tools/generate_profiles.py --list` to see all generated ADA profiles with their termcodes and detail building block info.

See [agents.md](agents.md) for the full building block structure, authoring rules, and composition hierarchy.

## Building Block Categories

| Category | Directory | Description |
|----------|-----------|-------------|
| schemaorgProperties | `_sources/schemaorgProperties/` | schema.org vocabulary building blocks (person, organization, identifier, definedTerm, instrument, etc.) |
| cdifProperties | `_sources/cdifProperties/` | CDIF-specific properties (mandatory, optional, provenance, tabular data, long data, etc.) |
| ddiProperties | `_sources/ddiProperties/` | DDI-CDI vocabulary building blocks |
| provProperties | `_sources/provProperties/` | PROV-O provenance (generatedBy, derivedFrom) |
| qualityProperties | `_sources/qualityProperties/` | DQV data quality measures |
| adaProperties | `_sources/adaProperties/` | ADA (IEDA Analytics & Data Archive) domain properties |
| xasProperties | `_sources/xasProperties/` | X-ray Absorption Spectroscopy domain properties |
| DDEproperties | `_sources/DDEproperties/` | DDE (Deep-time Digital Earth) geoscience metadata properties (7 BBs: subject, resourceType, required, optional, imagery, serviceInfo, geographicDataset) |
| ecrrProperties | `_sources/ecrrProperties/` | ECRR (EarthCube Resource Registry) resource type properties (base, common, assessment, type-specific) |
| profiles | `_sources/profiles/` | Composed profiles (ADA technique, CDIF discovery, DDE resource type, ECRR resource type) |

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
| 3 (domain) | `ddeImagery`, `xasGeneratedBy`, etc. | Domain-specific profiles | Extend `cdifProv` with domain-specific instrument types, agents, and additional properties |

Domain-specific building blocks (`ddeImagery`, `xasOptional`, `xasRequired`) import `cdifProv` directly, so they can be used in profiles that don't include `CDIFcomplete`.

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

where `{category}` is one of `schemaorgProperties`, `cdifProperties`, `adaProperties`, `provProperties`, `qualityProperties`, `ddiProperties`, `xasProperties`, `DDEproperties`, `ecrrProperties` and `{name}` is the building block directory name (e.g., `person`, `cdifProv`, `xasGeneratedBy`).

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
| `…/{category}/{name}/schema` | JSON Schema (YAML; or JSON via `Accept: application/json`) |
| `…/{category}/{name}/resolved` | Resolved schema — all `$ref` inlined (JSON) |
| `…/{category}/{name}/shacl` | SHACL validation rules (Turtle) |
| `…/{category}/{name}/context` | JSON-LD context |

```bash
curl -L https://w3id.org/cdif/bbr/metadata/schemaorgProperties/person/schema
curl -L https://w3id.org/cdif/bbr/metadata/schemaorgProperties/person/resolved
curl -L https://w3id.org/cdif/bbr/metadata/schemaorgProperties/person/shacl
curl -L https://w3id.org/cdif/bbr/metadata/schemaorgProperties/person/context
```

## License

This material is based upon work supported by the National Science Foundation (NSF) under awards 2012893, 2012748, and 2012593.
