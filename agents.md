# Agents Guide: OGC Building Blocks Repository

This document explains how to work with this repository — the building block structure, authoring rules, validation workflow, and the schema resolver tool.

## What This Repository Is

This repository contains modular schema components following the [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) pattern. Each building block is a self-contained directory with a JSON Schema, JSON-LD context, metadata, and description. Building blocks compose into profiles that define complete metadata schemas for specific use cases.

The repository is included as a git submodule in the [IEDA Data Submission Portal](https://github.com/smrgeoinfo/IEDADataSubmission) monorepo.

## Repository Structure

```
metadataBuildingBlocks/
├── _sources/                        # All building block sources
│   ├── schemaorgProperties/         # Core schema.org property types
│   │   ├── person/                  # schema:Person
│   │   ├── organization/            # schema:Organization
│   │   ├── identifier/              # schema:identifier (PropertyValue)
│   │   ├── definedTerm/             # schema:DefinedTerm
│   │   ├── additionalProperty/      # schema:PropertyValue for soft-typed properties
│   │   ├── variableMeasured/        # schema:variableMeasured (PropertyValue)
│   │   ├── spatialExtent/           # schema:Place (bounding box, facility/lab base)
│   │   ├── temporalExtent/          # schema:temporalCoverage
│   │   ├── dataDownload/            # schema:DataDownload
│   │   ├── labeledLink/             # schema:LinkRole
│   │   ├── funder/                  # schema:funder / schema:Grant
│   │   ├── webAPI/                  # schema:WebAPI
│   │   ├── action/                  # schema:Action
│   │   └── agentInRole/             # schema:Role wrapping Person/Org
│   ├── cdifProperties/              # CDIF-specific property types
│   │   ├── cdifCatalogRecord/       # dcat:CatalogRecord metadata-about-metadata
│   │   ├── cdifCore/           # CDIF core property group
│   │   ├── cdifDataDescription/      # CDIF data description constraints
│   │   ├── cdifProvActivity/         # CDIF provenance activity (extends generatedBy)
│   │   ├── cdifProvenance/          # CDIF provenance (prov:wasGeneratedBy wrapper)
│   │   ├── cdifTabularData/         # CDIF tabular data description
│   │   ├── cdifDataCube/            # CDIF data cube description
│   │   ├── cdifLongData/            # CDIF long data description
│   │   ├── cdifArchive/              # CDIF archive item (DataDownload with hasPart)
│   │   ├── cdifArchiveDistribution/ # CDIF archive distribution (schema:distribution wrapper)
│   │   └── cdifVariableMeasured/    # CDIF variable measured extension (cdi:InstanceVariable with cdi:qualifies)
│   ├── provProperties/              # W3C PROV provenance types
│   │   ├── generatedBy/             # prov:wasGeneratedBy (Activity)
│   │   ├── provActivity/            # PROV-O native activity (extends generatedBy)
│   │   └── derivedFrom/             # prov:wasDerivedFrom
│   ├── ddiProperties/               # DDI-CDI data description types
│   │   └── ddicdiProv/              # DDI-CDI native provenance activity
│   ├── qualityProperties/           # Data quality types
│   │   └── qualityMeasure/          # Quality measure definitions
│   ├── bioschemasProperties/         # Bioschemas vocabulary types
│   │   └── cdifBioschemasProperties/  # Lab protocols, samples, workflows
│   ├── xasProperties/               # X-ray Absorption Spectroscopy types
│   │   ├── xasSample/               # XAS sample (extends schema:Product)
│   │   ├── xasInstrument/           # XAS instrument (beamline, synchrotron)
│   │   ├── xasFacility/             # XAS facility (synchrotron source)
│   │   ├── xasGeneratedBy/          # XAS analysis event (extends cdifProvActivity)
│   │   ├── xasHDF5DataStructure/    # HDF5 data structure for XAS
│   │   ├── xasXdiTabularTextDataset/ # XDI tabular text dataset
│   │   ├── xasCore/             # XAS mandatory property group
│   │   └── xasOptional/             # XAS optional property group
│   └── profiles/                    # Top-level profiles that compose BBs
│       └── cdifProfiles/
│           ├── CDIFDiscoveryProfile/       # CDIF Discovery profile
│           ├── CDIFcompleteProfile/        # CDIF Complete profile (discovery + data description + provenance + archive)
│           ├── CDIFDataDescriptionProfile/ # CDIF Data Description profile
│           └── CDIFxasProfile/             # CDIF XAS profile
├── tools/
│   ├── resolve_schema.py            # Schema resolver (see below)
│   ├── convert_for_jsonforms.py     # JSON Forms converter (see below)
│   ├── compare_schemas.py           # Schema comparison tool
│   ├── validate_instance.py         # Profile-aware validation tool
│   ├── validate_examples.py         # Validates all examples against resolved schemas
│   ├── augment_register.py          # Adds resolvedSchema URLs to register.json
│   ├── regenerate_schema_json.py    # Regenerates schema.json files from resolvedSchema.json
│   ├── test_redirects.py            # Tests w3id.org redirect rules for building block URIs
│   ├── update_conformsto_uris.py    # Updates conformsTo URIs in building block schemas
│   ├── audit_building_blocks.py     # Comprehensive BB repo audit (pluggable to any repo)
│   ├── add_property_tree.py         # Adds propertyTree worksheets to Excel workbooks
│   ├── generate_property_tree2.py   # Generates propertyTree_2 worksheets from resolved schemas
│   └── cors_server.py               # CORS dev server for local testing
└── .github/workflows/               # Validation + JSON Forms generation + custom Pages deploy

Domain-specific building blocks (moved to separate repositories):
  ddeBuildingBlocks/     → DDEproperties/ + DDEProfiles/       (github.com/usgin/ddeBuildingBlocks)
  geochemBuildingBlocks/ → adaProperties/ + adaProfiles/       (github.com/usgin/geochemBuildingBlocks)  [formerly in this repo]
  ecrrBuildingBlocks/    → ecrrProperties/ + ecrrProfiles/     (github.com/usgin/ecrrBuildingBlocks)
```

## Building Block Composition

Profiles are defined as pure `allOf` compositions of building block `$ref`s, with no inline property definitions. All properties come from building block components.

Some building blocks define **item-level schemas** (e.g., a provenance activity object, an archive distribution item) rather than root-level dataset properties. Placing these directly in a profile's `allOf` would apply their constraints to the root object. **Wrapper building blocks** solve this by defining the root-level property (e.g., `prov:wasGeneratedBy`, `schema:distribution`) whose items reference the item-level building block.

| Wrapper BB | Root Property | Wraps |
|------------|--------------|-------|
| `cdifProvenance` | `prov:wasGeneratedBy` (array) | `cdifProvActivity` |
| `cdifArchiveDistribution` | `schema:distribution` (adds archive option) | `cdifArchive` |

## Distribution Composition Pattern

Building blocks that add properties to `schema:distribution` items must use partial property patches (no `type`, `anyOf`, `allOf`, or `$ref` at the distribution level) so the resolver's `deep_merge` merges them with cdifCore's `anyOf: [DataDownload, WebAPI]` rather than replacing it.

**Correct** — adds CDI properties without replacing base types:
```yaml
'schema:distribution':
    items:
      properties:
        'cdi:characterSet':
          type: string
```

**Wrong** — `type: array` triggers full replacement, losing DataDownload/WebAPI:
```yaml
'schema:distribution':
    type: array
    items:
      allOf:
        - type: object
          properties: ...
        - anyOf: [...]
```

## Building Block Conformance URIs

Building blocks that represent CDIF specification components declare required `dcterms:conformsTo` URIs in the metadata catalog record (`schema:subjectOf`). Each building block's `schema.yaml` adds a `contains` constraint on `schema:subjectOf` → `dcterms:conformsTo` requiring its specific URI. Corresponding SHACL shapes enforce the same constraint via `sh:hasValue`.

| Building Block | Conformance URI | SHACL Shape |
|---|---|---|
| `cdifCore` | `https://w3id.org/cdif/core/1.0` | `sh:hasValue` on existing `metadataProfileProperty` |
| `CDIFDiscoveryProfile` | `https://w3id.org/cdif/discovery/1.0` | `CDIFDiscoveryProfileConformsToShape` |
| `cdifDataDescription` | `https://w3id.org/cdif/data_description/1.0` | `CDIFDataDescriptionProfileConformsToShape` |
| `cdifArchiveDistribution` | `https://w3id.org/cdif/manifest/1.0` | *(no rules.shacl — JSON Schema only)* |
| `cdifProvenance` | `https://w3id.org/cdif/provenance/1.0` | *(no rules.shacl — JSON Schema only)* |
| `xasOptional` | `https://w3id.org/cdif/xasDiscovery/1.0` | `XasDiscoveryConformsToShape` |
| `xasCore` | `https://w3id.org/cdif/xasCore/1.0` | `XasCoreConformsToShape` |

**URI convention:** Conformance URIs must NOT have a trailing `/` character.

**Profile rollup:** When building blocks are composed into profiles via `allOf`, the `contains` constraints combine — the conformsTo array must include URIs for all constituent building blocks. For example:

| Profile | Required conformsTo URIs |
|---|---|
| CDIFDiscoveryProfile | `core/1.0` + `discovery/1.0` |
| CDIFDataDescriptionProfile | `core/1.0` + `discovery/1.0` + `data_description/1.0` |
| CDIFcompleteProfile | `core/1.0` + `discovery/1.0` + `data_description/1.0` + `manifest/1.0` + `provenance/1.0` |
| CDIFxasProfile | `core/1.0` + `discovery/1.0` + `xasDiscovery/1.0` + `xasCore/1.0` |

These conformance URIs are distinct from the OGC building block identifiers (`https://w3id.org/cdif/bbr/metadata/...`). Both may appear in a record's conformsTo array.

**JSON Schema pattern** (in each building block's `schema.yaml`):
```yaml
'schema:subjectOf':
  properties:
    'dcterms:conformsTo':
      type: array
      items:
        type: object
        properties:
          '@id':
            type: string
            description: uri for specifications that this metadata record conforms to
      minItems: 1
      contains:
        type: object
        properties:
          '@id':
            const: 'https://w3id.org/cdif/{component}/{version}/'
```

For `cdifCore` (which already defines `schema:subjectOf` with a `$ref` to CdifCatalogRecord), the constraint is wrapped in `allOf` to preserve the base schema.

## Building Block Structure

Each building block directory contains:

| File | Required | Purpose |
|---|---|---|
| `bblock.json` | Yes | Metadata: name, status, tags, version, links, sources |
| `schema.yaml` | Yes | JSON Schema with `$ref` cross-references to other BBs |
| `context.jsonld` | Yes | JSON-LD namespace prefix mappings |
| `description.md` | Yes | Human-readable description |
| `examples.yaml` | No | Example snippets with `ref:` pointing to example JSON files |

### `bblock.json` Required Fields

Every `bblock.json` must include all of these fields:

```json
{
  "$schema": "https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/refs/heads/master/ogc/bblocks/metadata-schema.yaml",
  "name": "Human-readable name",
  "abstract": "One-line description",
  "status": "under-development",
  "dateTimeAddition": "2026-01-01T00:00:00Z",
  "itemClass": "schema",
  "register": "ogc-building-block",
  "version": "0.1",
  "dateOfLastChange": "2026-01-01",
  "link": "https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks",
  "maturity": "development",
  "scope": "unstable",
  "tags": ["tag1", "tag2"],
  "sources": []
}
```

Missing `dateOfLastChange` or `link` will cause the validation workflow to fail.

### `schema.yaml` Cross-Reference Rules

Schemas reference other building blocks using relative `$ref` paths:

```yaml
$defs:
  Person:
    $ref: ../../schemaorgProperties/person/schema.yaml
  Identifier:
    $ref: ../../schemaorgProperties/identifier/schema.yaml
```

**Critical rules:**

1. **`@type` must always be an array of strings.** All building blocks use the array-only pattern with `contains: const:` to require specific types. Examples must also use array `@type` values (e.g. `["schema:Person"]`, not `"schema:Person"`).

   ```yaml
   # CORRECT
   '@type':
     type: array
     items:
       type: string
     contains:
       const: schema:Person
     minItems: 1

   # WRONG — do not use anyOf with string alternative
   '@type':
     anyOf:
     - type: string
       const: schema:Person
     - type: array
       ...
   ```

2. **Always reference `schema.yaml`, never standalone `.json` files.** The postprocess tool resolves `$ref` to GitHub Pages URLs. References to `.json` files cause 404 errors because only `schema.yaml` files are published to GitHub Pages.

   ```yaml
   # CORRECT
   $ref: ../../cdifProperties/cdifCatalogRecord/schema.yaml

   # WRONG — will cause 404 in validation
   $ref: ../../cdifProperties/cdifCatalogRecord/cdifCatalogRecordSchema.json
   ```

2. **Use correct relative paths.** Paths are relative to the current `schema.yaml` file. Building blocks in `xasProperties/` that reference `schemaorgProperties/` need `../../schemaorgProperties/...`, not `../...`.

3. **Reference `$defs` within another schema.yaml** using fragment syntax:
   ```yaml
   $ref: ../../schemaorgProperties/additionalProperty/schema.yaml#/$defs/propertyID_item
   ```

### `examples.yaml` Rules

1. **Provide minimal + complete examples.** Each building block and profile should have at least a minimal example (required properties only) and a complete example (exercising every property in the schema). Name them `example<Name>Minimal.json` and `example<Name>Complete.json`.

2. **`ref:` must match the actual filename** in the building block directory. Copy-paste errors referencing files from other BBs (e.g., `exampleWebAPI.json` in a non-webAPI BB) will cause validation failures.

2. **Schema prefix must use `http`, not `https`**, with a trailing slash:
   ```yaml
   # CORRECT
   prefixes:
     schema: http://schema.org/

   # WRONG
   prefixes:
     schema: https://schema.org
   ```

## Validation Workflow

A GitHub Actions workflow (`Validate and process Building Blocks`) runs on every push. It uses the `ogc/bblocks/postprocess` Docker container to:

1. Validate all `bblock.json` files have required fields
2. Resolve all `$ref` paths in `schema.yaml` files
3. Fetch resolved references from GitHub Pages URLs
4. Validate examples against their schemas
5. Generate annotated schemas and documentation

If the workflow fails, check the error log for:
- Missing `bblock.json` fields (especially `dateOfLastChange`, `link`)
- 404 errors fetching resolved `$ref` URLs (usually means a `.json` reference instead of `schema.yaml`)
- `FileNotFoundError` for example files (wrong `ref:` in `examples.yaml`)
- Date format errors (must be `YYYY-MM-DD`, not e.g. `2025-11=04`)

## Vocabulary Namespaces

| Prefix | URI | Used In |
|---|---|---|
| `schema` | `http://schema.org/` | Core metadata (name, description, identifier) — all BBs |
| `ada` | `https://ada.astromat.org/metadata/` | ADA-specific types and properties |
| `cdi` | `http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/` | Data structure descriptions |
| `prov` | `http://www.w3.org/ns/prov#` | Provenance (instruments, activities) |
| `nxs` | `http://purl.org/nexusformat/definitions/` | NeXus instrument/source classes |
| `csvw` | `http://www.w3.org/ns/csvw#` | Tabular data descriptions |
| `spdx` | `http://spdx.org/rdf/terms#` | File checksums |
| `dcterms` | `http://purl.org/dc/terms/` | Conformance declarations |
| `dcat` | `http://www.w3.org/ns/dcat#` | Catalog record typing (cdifCatalogRecord) |
| `geosparql` | `http://www.opengis.net/ont/geosparql#` | Spatial geometry types |
| `bios` | `https://bioschemas.org/` | Bioschemas lab protocols, samples, workflows |

## Domain-Specific Building Blocks (Moved)

The following building block categories have been refactored into separate repositories. See their respective `agents.md` files for detailed documentation:

- **ADA (geochemistry)**: [geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks) — 30 property BBs + 36 technique profiles
- **DDE (geoscience)**: [ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks) — 7 property BBs + 11 resource type profiles
- **ECRR (EarthCube)**: [ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks) — 10 property BBs + 11 resource type profiles

These repos reference core building blocks in this repository via absolute URLs (`https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/...`).

---

# Schema Tools

## Schema Pipeline

Three tools transform modular YAML source schemas into JSON Forms-compatible Draft 7 schemas and augment the bblocks-viewer register:

```
schema.yaml → resolve_schema.py → resolvedSchema.json → convert_for_jsonforms.py → schema.json
                                → <bbName>StructuredSchema.json (--structured)
                                → augment_register.py → register.json (adds resolvedSchema URLs)
```

## resolve_schema.py

Recursively resolves ALL `$ref` references from modular YAML/JSON source schemas into one fully-inlined JSON Schema. No external references remain in the output — all `$defs` are inlined and removed.

**$ref patterns handled:**
1. Relative path: `$ref: ../cdifCatalogRecord/schema.yaml`
2. Fragment-only: `$ref: '#/$defs/Identifier'`
3. Cross-file fragment: `$ref: ../cdifCatalogRecord/schema.yaml#/$defs/conformsTo_item`
4. Both YAML and JSON file extensions

**Structured mode (`--structured`):** Produces a compact `<bbName>StructuredSchema.json` that preserves building block structure via `$defs` and `$ref` links. For profiles, composing BBs are deep-merged into a single `properties` + `allOf`, while type schemas used >2 times appear as named `$defs`. Types used ≤2 times are inlined at usage sites. Typically 88–90% smaller than fully-resolved output.

**Usage:**
```bash
# Resolve a profile by name (searches _sources/profiles/cdifProfiles/{name}/)
python tools/resolve_schema.py CDIFDiscoveryProfile
python tools/resolve_schema.py CDIFcompleteProfile --flatten-allof

# Produce structured output with $defs preserved
python tools/resolve_schema.py CDIFDiscoveryProfile --structured
python tools/resolve_schema.py --all --structured

# Resolve an arbitrary schema file
python tools/resolve_schema.py --file path/to/any/schema.yaml

# Resolve all building blocks with external $refs
python tools/resolve_schema.py --all --flatten-allof
```

**CLI options:** `profile` (positional, profile name), `--file` (arbitrary schema path), `--all` (resolve all schemas with external refs), `-o`/`--output` (output file, default: stdout; ignored with --all), `--flatten-allof` (merge allOf entries into single objects), `--structured` (produce structured output with `$defs`, writes `<bbName>StructuredSchema.json`).

**Requirements:** Python 3.6+ with `pyyaml`

**Key implementation details:**
- `deep_merge` with `_is_complete_schema` heuristic: when merging `properties` dicts, overlay properties with `type`/`oneOf`/`anyOf`/`allOf`/`$ref` **replace** the base entirely; partial constraint patches (no composition keywords) are deep-merged
- Two-pass `$defs` resolution: pass 1 resolves external file refs with empty defs dict, pass 2 uses `_inline_unresolved_defs` to replace `$comment` placeholders left by forward cross-def fragment refs
- Circular reference detection via `seen` set (returns `$comment` placeholder)
- Strips metadata keys (`$id`, `x-jsonld-*`) from output

## convert_for_jsonforms.py

Reads `resolvedSchema.json` (from `_sources/profiles/cdifProfiles/{name}/`) and converts to JSON Forms-compatible Draft 7:
- Converts `$schema` from Draft 2020-12 to Draft 7
- Simplifies `anyOf` patterns for form rendering (single-item anyOf unwrapped, duplicate removal)
- Converts `contains` → `enum`, `const` → `default`
- Merges technique profile constraints into distribution `oneOf` branches
- Preserves `oneOf` in distribution (3 branches: single file, archive, WebAPI)
- Merges file-type `anyOf` (from `files/schema.yaml`) into flat hasPart item properties
- Removes `not` constraints and relaxes `minItems`

**Usage:**
```bash
python tools/convert_for_jsonforms.py CDIFDiscoveryProfile -v
python tools/convert_for_jsonforms.py --all -v
```

**Output:** `build/jsonforms/profiles/cdifProfiles/{name}/schema.json`

## augment_register.py

Adds `resolvedSchema` URLs to `build/register.json` for each profile building block. Scans bblock identifiers for `.profiles.{name}` patterns and checks whether `_sources/profiles/cdifProfiles/{name}/resolvedSchema.json` exists. If so, adds the GitHub Pages URL as `bblock.resolvedSchema`.

**Usage:**
```bash
python tools/augment_register.py
```

**Why:** The bblocks-viewer fork has a "Resolved (JSON)" button in the JSON Schema tab that fetches the resolved schema from this URL. The OGC postprocessor doesn't know about `resolvedSchema.json`, so this script injects the URLs after the postprocessor generates `register.json`.

**Workflow integration:** The `generate-jsonforms` workflow runs this after `convert_for_jsonforms.py` and stages `build/register.json` alongside `build/jsonforms/`. It is also run by `deploy-viewer.yml` before the Pages upload (see below).

## deploy-viewer.yml Workflow

The OGC postprocessor's reusable workflow deploys GitHub Pages with the upstream `ogcincubator/bblocks-viewer` and generates `config.js` in-memory (never committed). This means the deployed site uses the upstream viewer (which lacks the "Resolved (JSON)" button) and `register.json` without `resolvedSchema` URLs.

`deploy-viewer.yml` re-deploys Pages after the postprocessor, fixing both issues:

1. **Runs `augment_register.py`** — injects `resolvedSchema` URLs into `build/register.json`
2. **Generates `config.js`** — points `window.bblocksRegister` to the local register and sets `baseUrl` for SPA routing
3. **Generates `index.html`** — loads JS/CSS assets from `smrgeoinfo.github.io/bblocks-viewer/` (the fork) instead of the upstream viewer

**Trigger:** Runs after "Validate and process Building Blocks" completes successfully, or via `workflow_dispatch`.

**Workflow chain on push:**
```
push → "Validate and process Building Blocks" (OGC postprocessor)
         ├──→ "Generate JSON Forms schemas" (convert + augment + commit)
         └──→ "Deploy custom bblocks-viewer" (augment + config.js + index.html → Pages)
```

**Key detail:** Both `generate-jsonforms` and `deploy-viewer` run `augment_register.py` independently. `generate-jsonforms` commits the augmented `register.json` to the repo (for future runs). `deploy-viewer` augments the checked-out copy before uploading to Pages (because it can't wait for the other workflow's commit).

**bblocks-viewer fork:** `smrgeoinfo/bblocks-viewer` (forked from `ogcincubator/bblocks-viewer`). The fork's `gh-deploy.yml` workflow builds the Vue app and deploys to `smrgeoinfo.github.io/bblocks-viewer/`. The fork adds the "Resolved (JSON)" button to `JsonSchemaViewer.vue` and `resolvedSchema` to `COPY_PROPERTIES` in `bblock.service.js`.

## generate_property_table.py (in CDIF/Discovery repo)

Generates an Excel workbook (`<bbName>_properties.xlsx`) listing all properties from a building block or profile schema. For profiles, composing BB properties are merged into a single main worksheet; type schemas referenced via `$defs` get separate worksheets.

**Columns:** Field Name, Containing Class, CDIF Content Model (from crosswalk), Data Type(s), Cardinality, Enum/Const Values, Description.

**Type description logic:**
- Objects with a single `@id` property → `object reference`
- Objects with a single `@list` property (JSON-LD ordered list) → `list of <item types>`
- `anyOf`/`oneOf` unions → `Type1 | Type2 | ...`
- Arrays → `array of <item type>`

**Usage:**
```bash
# Generate property table for a building block
python generate_property_table.py path/to/_sources/cdifProperties/cdifCore/schema.yaml

# Generate property table for a profile
python generate_property_table.py path/to/_sources/profiles/cdifProfiles/CDIFDiscoveryProfile/schema.yaml
```

**Location:** `C:\Users\smrTu\OneDrive\Documents\GithubC\CDIF\Discovery\generate_property_table.py`

**Requirements:** `openpyxl`, `pyyaml`. Optionally uses `CDIF-metadata-crosswalks-merged.xlsx` for CDIF Content Model lookups.

## validate_examples.py

Validates all example JSON files against their resolved schemas. Uses `resolve_file()` from `resolve_schema.py` so `$defs`, cross-file `$ref`, and fragment references are handled correctly.

**Usage:**
```bash
# Validate all examples
python tools/validate_examples.py

# Verbose output (shows pass/fail for each)
python tools/validate_examples.py --verbose

# Filter to specific building blocks
python tools/validate_examples.py --filter spatialExtent
```

**CLI options:** `--verbose`/`-v` (show pass/fail for each example), `--filter`/`-f` (only validate paths containing this string).

**Requirements:** `pyyaml`, `jsonschema`

## audit_building_blocks.py

Comprehensive audit tool for any OGC Building Block repository. Scans a `_sources/` directory and runs 6 checks on each building block:

1. **File completeness** — required files (schema.yaml, bblock.json), optional files (description.md, context.jsonld, rules.shacl), examples, generated files
2. **schema.yaml vs *Schema.json** — structural consistency (ignoring expected $ref extension diffs)
3. **resolvedSchema.json freshness** — re-resolves and compares property keys
4. **Example validation** — validates example*.json against resolved schema (prefers existing resolvedSchema.json)
5. **SHACL completeness** — checks for NodeShape/PropertyShape definitions, property coverage
6. **Example coverage** — identifies schema properties not exercised by any example

**Usage:**
```bash
# Audit current repo
python tools/audit_building_blocks.py

# Audit another repo
python tools/audit_building_blocks.py /path/to/geochemBuildingBlocks/_sources

# Filter and verbose
python tools/audit_building_blocks.py --filter cdifCore -v

# JSON report
python tools/audit_building_blocks.py --json -o report.json
```

**Requirements:** `pyyaml`, `jsonschema`. Imports `resolve_schema.py` for re-resolution checks.

## generate_property_tree2.py

Generates `propertyTree_2` worksheets from resolved JSON Schemas. Walks the fully-resolved schema tree and produces a spreadsheet showing the complete property hierarchy following the CDIF property-tree convention.

**Worksheet layout:** Columns alternate between property and options. Column A holds the root object type (e.g., `schema:Dataset`, `skos:ConceptScheme`). Subsequent columns alternate property (odd) and options (even).

**Suffix conventions:**
| Suffix | Meaning |
|--------|---------|
| `-- string` | Literal string value |
| `-- string(uri)` | String with URI format |
| `-- string(date)` | String with date format |
| `-- boolean` / `-- number` | Literal boolean or number |
| `-- object reference` | JSON-LD `{@id: ...}` reference |
| `-- object` | Nested object (options column shows `@type` contains constraint) |
| `-- CHOICE` | `anyOf` with mixed types |
| `[brackets]` | Array cardinality (0..* or 1..*) |

**Recursion handling:** Types are expanded once per branch; revisiting a `@type` value in the same lineage stops expansion. Maximum nesting depth is 6 levels.

**Usage:**
```bash
# Generate for all profiles (Codelist, Discovery, DataDescription)
python tools/generate_property_tree2.py --profile all

# Generate for a single profile
python tools/generate_property_tree2.py --profile discovery
python tools/generate_property_tree2.py --profile codelist
python tools/generate_property_tree2.py --profile datadescription
```

For existing workbooks, adds `propertyTree_2` as a new sheet (preserving all existing sheets). For new workbooks (e.g., CDIFCodelistProfile), creates a new `.xlsx` file.

**Requirements:** `openpyxl`, `pyyaml`

## Verification

```bash
# Verify all schemas resolve without errors
python tools/resolve_schema.py --all --flatten-allof

# Verify all examples validate against their schemas
python tools/validate_examples.py --verbose

# Full audit
python tools/audit_building_blocks.py -v
```

## License

This material is based upon work supported by the National Science Foundation (NSF) under awards 2012893, 2012748, and 2012593.
