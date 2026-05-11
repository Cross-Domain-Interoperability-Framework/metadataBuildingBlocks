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
│   │   ├── statisticalVariable/     # schema:StatisticalVariable
│   │   ├── spatialExtent/           # schema:Place (bounding box, facility/lab base)
│   │   ├── temporalExtent/          # schema:temporalCoverage
│   │   ├── dataDownload/            # schema:DataDownload
│   │   ├── labeledLink/             # schema:LinkRole
│   │   ├── monetaryGrant/            # schema:MonetaryGrant (funding acknowledgement)
│   │   ├── webAPI/                  # schema:WebAPI
│   │   ├── action/                  # schema:Action
│   │   ├── agentInRole/             # schema:Role wrapping Person/Org
│   │   └── instrument/              # schema:Thing/Product instrument
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
│   │   ├── cdifInstanceVariable/    # CDIF Instance Variable: profile of cdi:InstanceVariable / schema:PropertyValue for schema:variableMeasured items (with cdi:role / cdi:qualifies). Renamed 2026-05 from cdifVariableMeasured.
│   │   ├── cdifPhysicalMapping/     # CDIF physical mapping (cdi:PhysicalSegmentLayout serialization metadata)
│   │   ├── cdifOpenApi/             # OpenAPI-aligned WebAPI distribution (alternative to schemaorgProperties/webAPI)
│   │   ├── cdifKey/                 # CDIF Key — ordered set of cdi:InstanceVariables (referenced via cdifInstanceVariable) that uniquely identify a data instance; CDIF profile of ddi-cdi Key/PrimaryKey
│   │   └── cdifEnumerationDomain/   # CDIF Enumeration Domain — extension point that documents any codification (skos:ConceptScheme, schema:DefinedTermSet, or @id-only reference) as a cdif:EnumerationDomain
│   ├── provProperties/              # W3C PROV provenance types
│   │   ├── generatedBy/             # prov:wasGeneratedBy (Activity)
│   │   ├── provActivity/            # PROV-O native activity (extends generatedBy)
│   │   └── derivedFrom/             # prov:wasDerivedFrom
│   ├── ddiProperties/               # DDI-CDI data description types (most generated from XMI via tools/uml_to_schema.py)
│   │   ├── ddicdiActivity/          # DDI-CDI Activity (Process package)
│   │   ├── ddicdiAgent/             # DDI-CDI Agent (umbrella: refs 4 agent sub-BBs)
│   │   ├── ddicdiIndividual/        # DDI-CDI Individual (person)
│   │   ├── ddicdiMachine/           # DDI-CDI Machine (software/hardware)
│   │   ├── ddicdiOrganization/      # DDI-CDI Organization (group/institution)
│   │   ├── ddicdiProcessingAgent/   # DDI-CDI ProcessingAgent (orchestrates activities)
│   │   ├── ddicdiDataTypes/          # DDI-CDI structured data types (from DDICDILibrary/DataTypes)
│   │   ├── ddicdiValueDomain/       # DDI-CDI ValueDomain (SubstantiveValueDomain + SentinelValueDomain)
│   │   ├── ddicdiEnumerationDomain/ # DDI-CDI EnumerationDomain (base for codifications)
│   │   ├── ddicdiCodeList/          # DDI-CDI CodeList (Code + CodePosition collections)
│   │   ├── ddicdiStatisticalClassification/  # DDI-CDI StatisticalClassification (with ClassificationItems and LevelStructure)
│   │   ├── ddicdiControlledVocabularyEntry/  # DDI-CDI ControlledVocabularyEntry (entry in an external vocabulary)
│   │   ├── ddicdiDataStructure/     # DDI-CDI DataStructure (Dimensional/KeyValue/Long/Wide variants)
│   │   └── ddicdiRepresentedVariable/  # DDI-CDI RepresentedVariable (variable definition with VD/CD ranges)
│   ├── skosProperties/               # W3C SKOS vocabulary types
│   │   ├── skosConceptScheme/       # skos:ConceptScheme
│   │   ├── skosConcept/            # skos:Concept
│   │   └── skosCollection/          # skos:Collection / skos:OrderedCollection
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
│           ├── CDIFCodelistProfile/        # CDIF Codelist profile (SKOS ConceptScheme validation)
│           ├── CDIFDiscoveryProfile/       # CDIF Discovery profile
│           ├── CDIFcompleteProfile/        # CDIF Complete profile (discovery + data description + provenance + archive)
│           ├── CDIFDataDescriptionProfile/ # CDIF Data Description profile
│           └── CDIFxasProfile/             # CDIF XAS profile
├── tools/
│   ├── resolve_schema.py            # Schema resolver (see below)
│   ├── uml_to_schema.py             # Generate a BB schema.yaml from canonical UML 2.5 / XMI 2.5.1 (see below)
│   ├── convert_for_jsonforms.py     # JSON Forms converter (see below)
│   ├── compare_schemas.py           # Schema comparison tool
│   ├── validate_instance.py         # Profile-aware validation tool
│   ├── validate_examples.py         # Validates all examples against resolved schemas
│   ├── augment_register.py          # Adds resolvedSchema URLs to register.json
│   ├── regenerate_schema_json.py    # Regenerates *Schema.json files from schema.yaml sources
│   ├── test_redirects.py            # Tests w3id.org redirect rules for building block URIs
│   ├── update_conformsto_uris.py    # Updates conformsTo URIs in building block schemas
│   ├── audit_building_blocks.py     # Comprehensive BB repo audit (pluggable to any repo)
│   ├── audit_shacl_coverage.py      # Compares schema.yaml properties vs rules.shacl shapes
│   ├── generate_custom_report.py    # Custom validation report with SHACL severity breakdown
│   ├── add_property_tree.py         # Adds propertyTree worksheets to Excel workbooks
│   ├── generate_property_tree2.py   # Generates propertyTree_2 worksheets from resolved schemas
│   ├── generate_pv_comparison.py    # Generates Word doc comparing PropertyValue implementations across BBs
│   ├── sync_resolve_schema.py       # Syncs shared tool scripts to domain BB repos
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

## BB Root Convention: Node-only schemas, no `@graph` wrapper

A building block's `schema.yaml` validates a **single Node** (or, for multi-class BBs, an `anyOf` of Node `$defs`). It does NOT include the {single | array | `{@context, @graph}`} wrapper trio at root. The wrapping responsibility belongs to **profiles** that compose BBs — they decide whether the document is a single Node, an unwrapped array, or a `@graph`-style JSON-LD document.

Single-class root:
```yaml
type: object
properties:
  "@type":
    type: array
    items: { type: string }
    contains: { const: "cdi:EnumerationDomain" }
    minItems: 1
  ...
required: [ "@type" ]
$defs:
  ...helpers (only types not already a BB on their own)...
```

Multi-class root (e.g. `ddicdiValueDomain`):
```yaml
anyOf:
  - $ref: '#/$defs/SubstantiveValueDomain'
  - $ref: '#/$defs/SentinelValueDomain'
$defs:
  SubstantiveValueDomain:
    ...
  SentinelValueDomain:
    ...
```

Examples should use single-Node form. The historical wrapper pattern (with `anyOf` over single/array/@graph branches) was removed in favor of this cleaner shape; `tools/uml_to_schema.py` and the resolver both follow it.

## Class Targets: inline-or-ref by default

For any property whose UML type is a class (a node, not a literal/datatype), the generated schema emits the JSON-LD embed-or-link pattern:

```yaml
"cdi:isMaintainedBy":
  anyOf:
    - $ref: ../ddicdiOrganization/schema.yaml   # external BB if one exists
    - $ref: ../ddicdiDataTypes/schema.yaml#/$defs/id-reference
```

Resolution order for the first `$ref`:
1. Another BB in this repo whose root class matches the target — `$ref` to that BB's `schema.yaml`.
2. Otherwise inline the class as a local `$def`.

The second `$ref` (to `id-reference`) lets a JSON-LD document carry just `{"@id": "..."}` instead of the full inline node.

**Principle:** local `$defs` are only for classes not already owned by another BB. As more classes get pulled out into their own BBs, more property targets resolve through the external-`$ref` path.

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
| CDIFCodelistProfile | *(no conformsTo constraints — uses SKOS ConceptScheme, not dataset metadata)* |
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
            const: 'https://w3id.org/cdif/{component}/{version}'
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

**Auto-generated files** (do not edit manually — regenerate with the tools below):

| File | Generated By | Purpose |
|---|---|---|
| `*Schema.json` | `regenerate_schema_json.py` | JSON copy of `schema.yaml` with `$ref` paths rewritten to `.json` extensions |
| `resolvedSchema.json` | `resolve_schema.py --all` | Standalone JSON Schema in structured form (`$defs` + internal `$ref`); single resolved-form artifact |

For profiles, generated files use the full profile directory name (e.g., `CDIFDiscoveryProfileSchema.json`).

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

3. **Use correct relative paths.** Paths are relative to the current `schema.yaml` file. Building blocks in `xasProperties/` that reference `schemaorgProperties/` need `../../schemaorgProperties/...`, not `../...`.

4. **Reference `$defs` within another schema.yaml** using fragment syntax:
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
| `spdx` | `http://spdx.org/rdf/terms#` | File checksums; SPDX license identifiers (cdifOpenApi) |
| `oas` | `https://spec.openapis.org/oas/3.1#` | OpenAPI 3.1 Operation/Parameter/RequestBody/Response (cdifOpenApi) |
| `dcterms` | `http://purl.org/dc/terms/` | Conformance declarations |
| `dcat` | `http://www.w3.org/ns/dcat#` | Catalog record typing (cdifCatalogRecord) |
| `geosparql` | `http://www.opengis.net/ont/geosparql#` | Spatial geometry types |
| `skos` | `http://www.w3.org/2004/02/skos/core#` | SKOS vocabulary (ConceptScheme, Concept, Collection) |
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
                                → augment_register.py → register.json (adds resolvedSchema URLs)
```

## resolve_schema.py

Resolves all external `$ref` references from modular YAML/JSON source schemas into a single standalone JSON Schema in **structured form** — composing BBs are deep-merged into `properties` + `allOf`, type schemas used >2 times become named `$defs` with internal `$ref`s, and recursive types stay as `$ref` cycles (the canonical JSON Schema way). Output is written to `resolvedSchema.json` next to each `schema.yaml`. Typically 88–90% smaller than the older fully-inlined form, and recursion-safe.

**$ref patterns handled:**
1. Relative path: `$ref: ../cdifCatalogRecord/schema.yaml`
2. Fragment-only: `$ref: '#/$defs/Identifier'`
3. Cross-file fragment: `$ref: ../cdifCatalogRecord/schema.yaml#/$defs/conformsTo_item`
4. Both YAML and JSON file extensions

**Usage:**
```bash
# Resolve a profile by name (searches _sources/profiles/cdifProfiles/{name}/)
python tools/resolve_schema.py CDIFDiscoveryProfile

# Resolve an arbitrary schema file
python tools/resolve_schema.py --file path/to/any/schema.yaml -o resolvedSchema.json

# Resolve all building blocks with external $refs (writes each BB's resolvedSchema.json)
python tools/resolve_schema.py --all
```

**CLI options:** `profile` (positional, profile name), `--file` (arbitrary schema path), `--all` (resolve all schemas with external refs, writes resolvedSchema.json per BB), `-o`/`--output` (output file for single-target runs; default: stdout). The legacy `--structured` flag is accepted but ignored — structured form is the only output mode.

**Requirements:** Python 3.6+ with `pyyaml`

**Key implementation details (tools/resolve_schema.py):**
- `deep_merge` with `_is_complete_schema` heuristic: when merging `properties` dicts, overlay properties with `type`/`oneOf`/`anyOf`/`allOf`/`$ref` **replace** the base entirely; partial constraint patches (no composition keywords) are deep-merged
- Two-pass `$defs` resolution: pass 1 resolves external file refs with empty defs dict, pass 2 uses `_inline_unresolved_defs` to replace `$comment` placeholders left by forward cross-def fragment refs. `_inline_unresolved_defs` also handles direct `$ref: '#/$defs/X'` nodes encountered during placeholder resolution with the same cycle protection (`resolving` set), so self-recursive root-class refs (e.g. `cdi:isVariantOf` → StatisticalClassification on a StatisticalClassification BB) don't blow up.
- **Cycle handling:** local fragment refs to inline `$defs` are promoted to top-level `$defs` of the structured output (with disambiguated names if there's a collision with BB-level promotions); cross-file fragment refs to inline `$defs` are also promoted instead of falling through to whole-file resolution. `_resolve_promoted_defs` resolves each promoted entry, iterating until the promotion set is stable. Cycles are expressed as `$ref: #/$defs/<name>` — the canonical JSON Schema way to handle recursion. `inline_low_use_defs` collapses non-cyclic, low-use defs back inline; `_is_in_cycle` (graph-reachability check via `_has_ref_to`) excludes cyclic defs to avoid producing dangling self-refs.
- Strips metadata keys (`$id`, `x-jsonld-*`) from output
- **URL ref resolution with transitive fetch**: URL `$ref`s (e.g. to GitHub Pages) are fetched and cached in a directory tree mirroring the URL structure (`host/path/...`). When a fetched file contains relative `$ref`s to sibling files, the resolver reconstructs the URL from the cache path and fetches on demand (`_fetch_relative_in_cache`). This enables full resolution of cross-repo building block references without requiring local clones.
- **Draft 2020-12 `$ref` siblings:** when a `$ref` carries sibling keywords (e.g. `description`), they merge into the `$ref` node directly rather than being wrapped in `allOf [{$ref}, {siblings}]`. Draft 2020-12 evaluates sibling keywords alongside the referenced schema, so the allOf wrap is unnecessary and the merged shape is more compact and metaschema-clean.
- **`merge_profile_structured` keys handling:** top-level keys other than `properties`/`allOf`/identity (e.g. `required`, `contains`) on a composing BB become `allOf` constraint entries on the merged result rather than being inserted into the merged `properties` dict. Multiple BBs' `required` lists therefore compose by intersection (each is its own constraint) instead of clobbering each other or polluting `properties`.

**Key implementation details (schema_resolver.py):**
- Flattens all `$defs` to a single global scope; `--inline-single-use` inlines defs referenced only once
- Tracks `source_file` through `process_schema()` so that internal `#/$defs/X` refs within externally-referenced files are resolved against the source file and promoted to global scope (fixes transitive internal ref resolution)
- Collapses alias `$defs` (e.g. `DefinedTerm_2: {$ref: "#/$defs/DefinedTerm"}`) that arise when multiple building blocks each declare a local `$defs` entry pointing to the same external schema — rewrites all references to point directly to the canonical def and removes the aliases
- Cycle detection via `processing_stack` set

## uml_to_schema.py

Generates a CDIF building-block `schema.yaml` (and, optionally, the surrounding `bblock.json` / `context.jsonld` / `rules.shacl` / `examples.yaml` skeletons) from a canonical UML 2.5 / XMI 2.5.1 export of a DDI-CDI / UCMIS class model. Used to bootstrap and refresh the `_sources/ddiProperties/ddicdi*` BBs.

**Usage:**
```bash
# Single-class BB
python tools/uml_to_schema.py \
  --xmi C:/path/to/ddi-cdi_canonical-unique-names.xmi \
  --class EnumerationDomain \
  --bb-name ddicdiEnumerationDomain \
  --out-dir _sources/ddiProperties/

# Multi-class BB (root anyOf over multiple concrete classes)
python tools/uml_to_schema.py \
  --xmi C:/path/to/ddi-cdi_canonical-unique-names.xmi \
  --class DataStructure,DimensionalDataStructure,KeyValueStructure,LongDataStructure,WideDataStructure \
  --bb-name ddicdiDataStructure \
  --out-dir _sources/ddiProperties/

# Just the schema.yaml, skip bblock.json/context.jsonld/rules.shacl/examples.yaml stubs
python tools/uml_to_schema.py ... --schema-only
```

**Encoded conventions:**
- Walks UML generalization (subclass shadows parent on name collision); collects own + inherited attributes.
- Multiplicity: `0..1` / `1..1` → single value; `*` upper → array-only with `minItems` if `lower>=1`.
- `uml:DataType` targets → `$ref` to `../ddicdiDataTypes/schema.yaml#/$defs/<Name>` if the name is in that BB's `$defs`, else inlined locally.
- `uml:Class` targets → inline-or-ref by default (`anyOf [class def, id-reference]`); class def comes from a sibling BB whose root is that class, else inlined locally. `--reference X,Y` forces id-ref-only; `--inline X,Y` forces inline-only.
- `uml:Enumeration` → `enum` literal list.
- Multi-class BB root: `anyOf` over local `$defs/<Class>` entries; each class gets its own Node `$def`.
- Role-name recovery for unnamed canonical-XMI association ends from the `<Source>_<role>_<Target>` association id pattern.
- Duplicate role-name properties (UCMIS overload, e.g. `CodeList.has → Code` AND `CodeList.has → CodePosition`) are merged via flat `anyOf` of distinct targets plus a single `id-reference` fallback.
- Sibling-BB lookup recognizes three root shapes: single-class `@type.contains.const`; multi-class `@type.anyOf` of `contains.const` branches; multi-root `anyOf` of `$ref` to local `$defs`. Also derives a class name from the BB directory name (`ddicdi<ClassName>`) so abstract parents like `ValueDomain` whose subclasses share a BB resolve to that BB.

**Source XMI:** the DDI-CDI canonical XMI lives outside this repo at the user's working location (e.g. `C:/Users/smrTu/Downloads/ddi-cdi_canonical-unique-names.xmi`). Pull a fresh copy from the DDI Alliance distribution when the model updates.

**Requirements:** Python 3.10+ with `pyyaml`.

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

**Custom validation report:** After augmenting the register, the workflow runs `tools/generate_custom_report.py` to replace the bblocks-postprocess `report.html` with a version that shows granular validation labels instead of binary PASS/FAIL. See [generate_custom_report.py](#generate_custom_reportpy) below for details.

**Key detail:** Both `generate-jsonforms` and `deploy-viewer` run `augment_register.py` independently. `generate-jsonforms` commits the augmented `register.json` to the repo (for future runs). `deploy-viewer` augments the checked-out copy before uploading to Pages (because it can't wait for the other workflow's commit).

**bblocks-viewer fork:** `smrgeoinfo/bblocks-viewer` (forked from `ogcincubator/bblocks-viewer`). The fork's `gh-deploy.yml` workflow builds the Vue app and deploys to `smrgeoinfo.github.io/bblocks-viewer/`. The fork adds the "Resolved (JSON)" button to `JsonSchemaViewer.vue` and `resolvedSchema` to `COPY_PROPERTIES` in `bblock.service.js`.

## generate_custom_report.py

Reads `build/tests/report.json` (generated by the OGC bblocks-postprocess pipeline) and generates a custom `build/tests/report.html` with granular validation labels instead of binary PASS/FAIL.

**Labels:**
- **Passed** (green) — JSON Schema passes, no SHACL issues
- **JSON Schema Fail** (red) — JSON Schema validation failed
- **SHACL: N Violation, N Warning, N Info** — SHACL issues with severity counts, colored by highest severity (red for Violation, yellow for Warning, blue for Info)
- Both JSON Schema and SHACL badges appear if both have issues
- `requireFail` test resources show "Passed (expected fail)" as before

**Pass criteria at building block level:** JSON Schema passes AND no SHACL Violations. SHACL Warnings and Info are displayed but do not cause failure. This is explained in a note at the top of the report.

**Usage:**
```bash
python tools/generate_custom_report.py
python tools/generate_custom_report.py --input build/tests/report.json --output build/tests/report.html
```

**How it works:** Parses the SHACL Turtle graphs embedded in each `report.json` entry (the `graph` field contains the full `sh:ValidationReport` RDF), extracts `sh:resultSeverity` values, and counts them per severity level. The original bblocks-postprocess treats all SHACL non-conformance as failure (`sh:conforms false` → `isError: true`), regardless of whether the results are Violations, Warnings, or Info.

**Workflow integration:** Called by `deploy-viewer.yml` after `augment_register.py`, overwriting the bblocks-postprocess `report.html` before the Pages upload. The original `report.json` is preserved unchanged.

**Requirements:** Python 3.6+ (no additional dependencies — uses only `json`, `re`, `html`, `os`, `argparse`, `collections`)

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

Validates all example JSON files against their resolved schemas. Uses `schema_resolver.py`'s `SchemaResolver` class for resolution, which correctly handles transitive internal `$defs` references within externally-referenced schemas. Falls back to the `tools/resolve_schema.py` inline resolver for schemas with circular `$ref` patterns that cause recursion errors in jsonschema validation.

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

**Requirements:** `pyyaml`, `jsonschema`. Imports `schema_resolver.py` for re-resolution checks.

## audit_shacl_coverage.py

Compares schema.yaml properties against rules.shacl shapes for all building blocks. Reports missing shapes, severity mismatches, and extra SHACL shapes. Processes leaf BBs first (no external `$ref`), then composites, then profiles.

```bash
# Default: show required/anyOf gaps and severity mismatches
python tools/audit_shacl_coverage.py

# Verbose: also show optional property gaps and extra SHACL shapes
python tools/audit_shacl_coverage.py --verbose
```

**Known limitations:** The SHACL parser is regex-based and produces false positives for:
- Named property references (`cdifd:nameProperty` etc.) — can't follow the reference
- `sh:or` constructs (anyOf patterns for person/org/definedTerm)
- Nested property shapes within NodeShapes

Always manually verify MISSING_REQUIRED findings before acting on them.

**Requirements:** `pyyaml`

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

## sync_resolve_schema.py

Syncs shared tool scripts (`resolve_schema.py`, `regenerate_schema_json.py`) from this canonical repo to all domain building block repositories (ddeBuildingBlocks, geochemBuildingBlocks, ecrrBuildingBlocks).

**Usage:**
```bash
# Dry-run (show what would be copied)
python tools/sync_resolve_schema.py

# Actually copy the files
python tools/sync_resolve_schema.py --apply
```

Looks for sibling repos relative to this repo's parent directory.

## generate_pv_comparison.py

Generates a Word document (`PropertyValue_Comparison.docx`) comparing `schema:PropertyValue` implementations across building blocks. Shows how different BBs use PropertyValue as a property type, with a comparison table.

**Usage:**
```bash
python tools/generate_pv_comparison.py
```

**Requirements:** `python-docx`

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
