# Metadata Building Blocks Repository
Created by S.M. Richard and claude-code  2026-02-15

Core modular schema components following the [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) pattern for implementation of modular interoperable metadata for the [Cross-Domain Interoperability Framework (CDIF)](https://cdif.org). Each building block is a self-contained directory with a JSON Schema, JSON-LD context, metadata, and description. Building blocks compose into profiles that define complete metadata schemas for specific use cases.

This repository contains the **shared core building blocks** (schema.org properties, CDIF properties, PROV-O provenance, data quality, XAS spectroscopy, and DDI-CDI). Domain-specific building blocks have been refactored into separate repositories:

- **[ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)** — DDE (Deep-time Digital Earth) geoscience properties and profiles (7 BBs + 11 profiles)
- **[geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)** — ADA (IEDA Analytics & Data Archive) geochemistry properties and profiles (30 BBs + 36 profiles)
- **[ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)** — ECRR (EarthCube Resource Registry) properties and profiles (10 BBs + 11 profiles)

Domain-specific repos reference core building blocks in this repository via absolute URLs (`https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/...`).

For more info see [the OGC Documentation](https://ogcincubator.github.io/bblocks-docs/).

## Schema Pipeline

The schema pipeline transforms modular YAML source schemas into JSON Forms-compatible Draft 7 schemas in two steps, plus an augmentation step for the bblocks-viewer:

```
schema.yaml → resolve_schema.py → resolvedSchema.json → convert_for_jsonforms.py → schema.json
                                → <bbName>StructuredSchema.json (--structured)
                                → augment_register.py → register.json (adds resolvedSchema URLs)
```

### Step 1: Resolve (`resolve_schema.py`)

Recursively resolves all `$ref` references from modular YAML/JSON source schemas into one fully-inlined JSON Schema. Handles relative paths, fragment-only refs (`#/$defs/X`), cross-file fragments, URL refs, and both YAML/JSON extensions. Optionally flattens `allOf` entries.

The `--structured` flag produces a compact alternative output (`<bbName>StructuredSchema.json`) that preserves building block structure via `$defs` and `$ref` links instead of fully inlining everything. For profiles, composing BBs are deep-merged into a single `properties` + `allOf`, while frequently-used type schemas (Person, Identifier, Organization, etc.) appear as named `$defs` with `$ref` links at usage sites. Types used ≤2 times are inlined. This typically reduces output size by 88–90% compared to fully-resolved schemas.

```bash
# Resolve a profile by name (searches cdifProfiles/ subdirectories)
python tools/resolve_schema.py CDIFDiscoveryProfile

# Produce structured output with $defs
python tools/resolve_schema.py CDIFDiscoveryProfile --structured

# Resolve all building blocks with external $refs
python tools/resolve_schema.py --all
python tools/resolve_schema.py --all --structured

# Resolve an arbitrary schema file
python tools/resolve_schema.py --file path/to/any/schema.yaml
```

**Requirements:** Python 3.6+ with `pyyaml` (`pip install pyyaml`)

### Validate Examples (`validate_examples.py`)

Validates all example JSON files against their resolved schemas. Uses `resolve_schema.py`'s resolver for proper `$defs` and cross-file `$ref` handling.

```bash
# Validate all examples
python tools/validate_examples.py

# Verbose output (shows pass/fail for each)
python tools/validate_examples.py --verbose

# Filter to specific building blocks
python tools/validate_examples.py --filter person
```

**Requirements:** Python 3.6+ with `pyyaml`, `jsonschema` (`pip install pyyaml jsonschema`)

### Audit Building Blocks (`audit_building_blocks.py`)

Comprehensive audit tool for any OGC Building Block repository. Checks file completeness, schema consistency, example validation, SHACL completeness, and property coverage.

```bash
# Audit current repo
python tools/audit_building_blocks.py -v

# Audit another repo (e.g. geochemBuildingBlocks)
python tools/audit_building_blocks.py /path/to/_sources -v

# JSON report
python tools/audit_building_blocks.py --json -o report.json
```

**Requirements:** Python 3.6+ with `pyyaml`, `jsonschema`

### Generate Property Tree (`generate_property_tree2.py`)

Generates `propertyTree_2` worksheets from resolved JSON Schemas. Walks the fully-resolved schema tree and produces an Excel worksheet showing the complete property hierarchy — root object type, then alternating property/options columns with type suffixes (`-- string`, `-- object`, `-- CHOICE`, `[brackets]` for arrays, etc.). Handles recursion by expanding each `@type` once per branch.

```bash
# Generate for all profiles (Codelist, Discovery, DataDescription)
python tools/generate_property_tree2.py --profile all

# Generate for a single profile
python tools/generate_property_tree2.py --profile discovery
```

**Requirements:** Python 3.6+ with `openpyxl`, `pyyaml`

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
python tools/convert_for_jsonforms.py CDIFDiscoveryProfile -v
```

### Step 3: Augment register.json (`augment_register.py`)

Adds `resolvedSchema` URLs to `build/register.json` for each profile building block that has a `resolvedSchema.json` file. This enables the bblocks-viewer's "Resolved (JSON)" button to fetch and display the fully resolved schema (all `$ref` inlined, `allOf` flattened).

```bash
python tools/augment_register.py
```

The `generate-jsonforms` workflow runs this automatically after schema conversion.

### Custom Validation Report (`generate_custom_report.py`)

Replaces the OGC bblocks-postprocess `report.html` with a version that shows granular validation labels instead of binary PASS/FAIL. Parses SHACL severity levels (Violation, Warning, Info) from the report data and displays them as separate badges.

- **JSON Schema Fail** (red) if JSON Schema validation fails
- **SHACL: N Violation, N Warning, N Info** with color-coded severity
- SHACL Warnings and Info do not cause a building block to be marked as failed

```bash
python tools/generate_custom_report.py
```

The `deploy-viewer` workflow runs this automatically after `augment_register.py`.

## Examples

Each building block and profile includes example JSON-LD instances:
- **Minimal** (`*Minimal.json`) — only required properties, simplest valid record
- **Complete** (`*Complete.json`) — exercises every property allowed by the schema

Validate examples with:
```bash
python tools/validate_examples.py --verbose
python tools/validate_examples.py --filter CDIFDiscovery --verbose
```

## Profiles

CDIF profiles are in `_sources/profiles/cdifProfiles/`:

| Profile | Description |
|---|---|
| `CDIFDiscoveryProfile` | CDIF Discovery profile (allOf: cdifCore + discovery properties) |
| `CDIFDataDescriptionProfile` | CDIF Data Description profile (allOf: cdifCore + cdifDataDescription + discovery properties) |
| `CDIFcompleteProfile` | CDIF Complete profile (allOf: cdifCore + cdifDataDescription + cdifArchiveDistribution + cdifProvenance + discovery properties) |
| `CDIFxasProfile` | CDIF XAS profile (allOf: cdifCore + xasOptional + xasCore + discovery properties) |

See [agents.md](agents.md) for the full building block structure, authoring rules, and composition hierarchy.

### Wrapper Building Blocks

Some building blocks define *item-level* schemas (e.g., a single provenance activity, or a single archive distribution item) rather than root-level dataset properties. These cannot be placed directly in a profile's `allOf` because their constraints would apply to the root dataset object instead of to items within a property array.

**Wrapper building blocks** solve this by defining a root-level property whose items reference the item-level building block. This keeps profiles as pure `allOf` compositions of building block refs, with no inline property definitions.

| Wrapper | Root Property | Item Building Block |
|---------|--------------|---------------------|
| `cdifProvenance` | `prov:wasGeneratedBy` (array) | `cdifProvActivity` |
| `cdifArchiveDistribution` | `schema:distribution` (array, adds archive option) | `cdifArchive` |

For example, `cdifProvActivity` defines the schema for a single provenance Activity object. The `cdifProvenance` wrapper defines `prov:wasGeneratedBy` as an array of `cdifProvActivity` items, making it composable at the profile level. Similarly, `cdifArchive` defines the schema for a single archive DataDownload item (with `schema:hasPart` component files), and `cdifArchiveDistribution` adds it as a valid `schema:distribution` item type alongside the DataDownload and WebAPI options already provided by `cdifCore`.

## Building Block Categories

| Category | Directory | Description |
|----------|-----------|-------------|
| schemaorgProperties | `_sources/schemaorgProperties/` | schema.org vocabulary building blocks (person, organization, identifier, definedTerm, instrument, etc.) |
| cdifProperties | `_sources/cdifProperties/` | CDIF-specific properties (core, optional, provenance, tabular data, long data, etc.) |
| ddiProperties | `_sources/ddiProperties/` | DDI-CDI vocabulary building blocks |
| provProperties | `_sources/provProperties/` | PROV-O provenance (generatedBy, derivedFrom, provActivity) |
| qualityProperties | `_sources/qualityProperties/` | DQV data quality measures |
| xasProperties | `_sources/xasProperties/` | X-ray Absorption Spectroscopy domain properties |
| bioschemasProperties | `_sources/bioschemasProperties/` | Bioschemas vocabulary building blocks (lab protocols, samples, computational workflows) |
| profiles | `_sources/profiles/cdifProfiles/` | CDIF profiles |

### ddiProperties

DDI-CDI vocabulary building blocks for communities using the DDI Cross-Domain Integration standard natively. Generated from the DDI-CDI 1.0 Enterprise Architect UML model with all structured data types resolved to base types.

| Building Block | Description |
|----------------|-------------|
| `ddicdiActivity` | DDI-CDI Activity class (DDICDILibrary/Classes/Process) -- describes tasks using `cdi:Activity`, `cdi:Step`, and `cdi:Parameter`. Includes `cdi:definition` (InternationalString), `cdi:start`/`cdi:end` (timestamps), `cdi:hasInternal` (ControlLogic), `cdi:entityUsed`/`cdi:entityProduced` (References), and `cdi:has_Step` with `cdi:script` (CommandCode). SHACL shapes for Activity and Step. |
| `ddicdiDataTypes` | Shared DDI-CDI data types used across Agent building blocks: identifiers (`cdi:Identifier`, `cdi:NonDdiIdentifier`, `cdi:IRDI`), names (`cdi:ObjectName`, `cdi:IndividualName`, `cdi:OrganizationName`), contact information (`cdi:ContactInformation`, `cdi:Address`, `cdi:Email`, `cdi:Telephone`, `cdi:WebLink`), references (`cdi:Reference`, `cdi:ControlledVocabularyEntry`), strings (`cdi:InternationalString`, `cdi:LanguageString`), and other types (`cdi:DateRange`, `cdi:CombinedDate`, `cdi:PrivateImage`, `cdi:CatalogDetails`, `cdi:AccessLocation`). |
| `ddicdiIndividual` | DDI-CDI Individual agent (person) with `cdi:individualName` (IndividualName), `cdi:contactInformation`, and identification. Refs `ddicdiDataTypes` for shared data types. |
| `ddicdiMachine` | DDI-CDI Machine agent (software/hardware) with `cdi:accessLocation`, `cdi:function`, `cdi:machineInterface`, and `cdi:typeOfMachine`. Refs `ddicdiDataTypes` for shared data types. |
| `ddicdiOrganization` | DDI-CDI Organization agent (group/institution) with `cdi:organizationName` (OrganizationName), `cdi:contactInformation`, and identification. Refs `ddicdiDataTypes` for shared data types. |
| `ddicdiProcessingAgent` | DDI-CDI ProcessingAgent that orchestrates activities via `cdi:performs` and `cdi:operatesOn` (ProductionEnvironment references). Refs `ddicdiDataTypes` for shared data types. |
| `ddicdiAgent` | Umbrella building block composing the 4 agent subtypes (`ddicdiIndividual`, `ddicdiMachine`, `ddicdiOrganization`, `ddicdiProcessingAgent`) via `anyOf`. Supports single node, unwrapped `@graph` array, and full JSON-LD document formats. |
| `ddicdiValueDomain` | DDI-CDI ValueDomain (DDICDILibrary/Classes/Representations) -- unified building block covering both `cdi:SubstantiveValueDomain` (subject-matter values) and `cdi:SentinelValueDomain` (processing/missing-value codes like SAS `.R`, SPSS `999`). Includes `cdi:isDescribedBy` (ValueAndConceptDescription with min/max bounds, regex, classification level), `cdi:takesValuesFrom` (EnumerationDomain), and `cdi:platformType` (sentinel only). |

### schemaorgProperties

Schema.org vocabulary building blocks for reusable metadata components.

| Building Block | Description |
|----------------|-------------|
| `instrument` | Generic instrument or instrument system -- uses `schema:Thing` base type with optional `schema:Product` typing. Supports hierarchical instrument systems via `schema:hasPart` for sub-components. Instruments are nested within `prov:used` items via a `schema:instrument` sub-key (instruments are `prov:Entity` subclasses). Referenced by `cdifProvActivity`, `provActivity`, and `xasInstrument`. |

### provProperties

PROV-O provenance building blocks.

| Building Block | Description |
|----------------|-------------|
| `generatedBy` | Base provenance activity -- minimal `prov:Activity` with `prov:used`. Extended by `cdifProvActivity` and `provActivity`. |
| `provActivity` | PROV-O native provenance activity -- extends `generatedBy` with W3C PROV-O properties (`prov:wasAssociatedWith`, `prov:startedAtTime`, `prov:endedAtTime`, `prov:atLocation`, `prov:wasInformedBy`, `prov:generated`). Uses schema.org fallbacks only where PROV-O has no equivalent (name, description, methodology, status). Instruments nested in `prov:used` via `schema:instrument` sub-key. |
| `derivedFrom` | Provenance derivation -- `prov:wasDerivedFrom` linking. |

### Provenance Layering

The repository implements a three-tier provenance architecture:

| Tier | Building Block | Introduced At | Description |
|------|---------------|---------------|-------------|
| 1 (simple) | `generatedBy` (provProperties) | `cdifCore` | Minimal `prov:Activity` — `prov:used` accepts only string names or `@id` references |
| 2 (extended) | `cdifProvActivity` (cdifProperties) | `CDIFcompleteProfile` (via `cdifProvenance`) | Extends `generatedBy` with schema.org Action properties (`schema:agent`, `schema:actionProcess`, `schema:object`, `schema:result`, temporal bounds, location). Requires `@type: ["schema:Action", "prov:Activity"]`. Instruments nested in `prov:used` via `schema:instrument` sub-key. The `cdifProvenance` building block wraps `cdifProvActivity` items in the `prov:wasGeneratedBy` root property. |
| 3 (domain) | `xasGeneratedBy`, etc. | Domain-specific profiles | Extend `cdifProvActivity` with domain-specific instrument types, agents, and additional properties (see [ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks), [geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)) |

### xasProperties

| Building Block | Description |
|----------------|-------------|
| `xasInstrument` | XAS instrument with `schema:hasPart` for hierarchical sub-components (refs generic instrument building block). |
| `xasGeneratedBy` | XAS analysis event — extends `cdifProvActivity` with `xas:AnalysisEvent` typing, XAS facility location, sample object, XAS-specific instrument types, and XAS additional properties (edge_energy, calibration method, etc.). |
| `xasCore` | XAS mandatory properties — `prov:wasGeneratedBy` items use `allOf` with `cdifProvActivity` + NXsource/NXmonochromator instrument constraints via `schema:instrument` sub-key. |
| `xasOptional` | Same provenance structure as `xasCore` — `cdifProvActivity` activity with XAS instrument constraints. |

## Building Block Conformance URIs

Each building block that represents a CDIF specification component declares a required `dcterms:conformsTo` URI in the metadata catalog record (`schema:subjectOf`). This constraint ensures that metadata records explicitly identify which specification components they implement.

| Building Block | Conformance URI |
|---|---|
| `cdifCore` | `https://w3id.org/cdif/core/1.0/` |
| `CDIFDiscoveryProfile` | `https://w3id.org/cdif/discovery/1.0/` |
| `cdifDataDescription` | `https://w3id.org/cdif/dataDescription/1.0/` |
| `cdifArchiveDistribution` | `https://w3id.org/cdif/manifest/1.0/` |
| `cdifProvenance` | `https://w3id.org/cdif/provenance/1.0/` |
| `xasOptional` | `https://w3id.org/cdif/xasDiscovery/1.0/` |
| `xasCore` | `https://w3id.org/cdif/xasCore/1.0/` |

### How it works

Each building block's `schema.yaml` adds a `contains` constraint on `schema:subjectOf` → `dcterms:conformsTo` requiring its specific URI. When building blocks are composed into profiles via `allOf`, these constraints roll up automatically — the conformsTo array must include URIs for **all** constituent building blocks.

For example, the **CDIFDiscoveryProfile** profile (cdifCore + discovery properties) requires conformsTo to contain both `w3id.org/cdif/core/1.0/` and `w3id.org/cdif/discovery/1.0/`.

These conformance URIs are distinct from the OGC building block identifiers (e.g., `https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore`), which identify the building block artifacts themselves. Both may appear in a record's conformsTo array.

Corresponding SHACL shapes enforce the same constraints via `sh:hasValue` on `dcterms:conformsTo`.

## Building Block Identifiers and Web Resolution

Each building block has a persistent HTTP URI under `https://w3id.org/cdif/bbr/metadata/`. The URI pattern is:

```
https://w3id.org/cdif/bbr/metadata/{category}/{name}
```

where `{category}` is one of `schemaorgProperties`, `cdifProperties`, `provProperties`, `qualityProperties`, `ddiProperties`, `xasProperties` and `{name}` is the building block directory name (e.g., `person`, `cdifProvActivity`, `xasGeneratedBy`).

Examples:
- `https://w3id.org/cdif/bbr/metadata/schemaorgProperties/person`
- `https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifProvActivity`
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
