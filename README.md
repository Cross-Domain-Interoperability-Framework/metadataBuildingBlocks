# Metadata Building Blocks Repository
Created by S.M. Richard and claude-code  2026-02-15

Core modular schema components following the [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) pattern for implementation of modular interoperable metadata for the [Cross-Domain Interoperability Framework (CDIF)](https://cdif.org). Each building block is a self-contained directory with a JSON Schema, JSON-LD context, metadata, and description. Building blocks compose into profiles that define complete metadata schemas for specific use cases.

This repository contains the **shared core building blocks** (schema.org properties, CDIF properties, PROV-O provenance, SKOS vocabulary, Bioschemas, data quality, XAS spectroscopy, and DDI-CDI). Domain-specific building blocks have been refactored into separate repositories:

- **[ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)** — DDE (Deep-time Digital Earth) geoscience properties and profiles (7 BBs + 11 profiles)
- **[geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)** — ADA (IEDA Analytics & Data Archive) geochemistry properties and profiles (30 BBs + 36 profiles)
- **[ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)** — ECRR (EarthCube Resource Registry) properties and profiles (10 BBs + 11 profiles)

Domain-specific repos reference core building blocks in this repository via absolute URLs (`https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/...`).

For more info see [the OGC Documentation](https://ogcincubator.github.io/bblocks-docs/).

## Schema Pipeline

The schema pipeline transforms modular YAML source schemas into JSON Forms-compatible Draft 7 schemas in two steps, plus an augmentation step for the bblocks-viewer:

```
schema.yaml → resolve_schema.py → resolvedSchema.json → convert_for_jsonforms.py → schema.json
                                → augment_register.py → register.json (adds resolvedSchema URLs)
```

### Step 1: Resolve (`resolve_schema.py`)

Resolves all external `$ref` references from modular YAML/JSON source schemas into a single standalone JSON Schema and writes it to `resolvedSchema.json` next to each `schema.yaml`. Output is in **structured form**: composing BBs are deep-merged into `properties` + `allOf`, frequently-used type schemas (Person, Identifier, Organization, etc.) appear as named `$defs` with internal `$ref`s, and recursive types stay as `$ref` cycles. Types used ≤2 times are inlined at usage sites. The structured output is recursion-safe and typically 88–90% smaller than the older fully-inlined form. Handles relative paths, fragment-only refs (`#/$defs/X`), cross-file fragments, URL refs (including transitive relative refs within fetched files), and both YAML/JSON extensions.

```bash
# Resolve a profile by name (searches cdifProfiles/ subdirectories)
python tools/resolve_schema.py CDIFDiscoveryProfile

# Resolve all building blocks with external $refs (writes each BB's resolvedSchema.json)
python tools/resolve_schema.py --all

# Resolve an arbitrary schema file
python tools/resolve_schema.py --file path/to/any/schema.yaml -o resolvedSchema.json
```

The legacy `--structured` flag is accepted but ignored — structured form is the only output mode.

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
python tools/convert_for_jsonforms.py CDIFDiscoveryProfile -v
```

### Step 3: Augment register.json (`augment_register.py`)

Adds `resolvedSchema` URLs to `build/register.json` for each profile building block that has a `resolvedSchema.json` file. This enables the bblocks-viewer's "Resolved (JSON)" button to fetch and display the standalone resolved schema (structured form — external `$ref`s resolved into `$defs` + internal `$ref`s; recursive types stay as `$ref` cycles).

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

## Other Tools

### UML → Schema Generator (`uml_to_schema.py`)

Generates a CDIF building-block `schema.yaml` (plus `bblock.json`/`context.jsonld`/`rules.shacl`/`examples.yaml` skeletons) from a DDI-CDI / UCMIS class model. Used to bootstrap and refresh the `_sources/ddiProperties/ddicdi*` BBs. The XMI format is **auto-detected**: both the canonical XMI 2.5.1 (OMG namespaces, `uml:Model`) and the Enterprise Architect native XMI 1.1 export (`xmlns:UML="omg.org/UML1.3"`) are supported — both parsers emit the same internal model so the rest of the generator is format-agnostic.

Generated schemas follow the project's conventions: Node-only root (no single/array/`@graph` wrapper); class-typed properties default to inline-or-ref with sibling-BB lookup before local inline; UCMIS overload of duplicate role names merged via flat `anyOf`; multiplicity → array-only when upper is `*`; UML generalization walked with subclass-shadows-parent.

```bash
python tools/uml_to_schema.py \
  --xmi C:/path/to/ddi-cdi_ea15.2026.March.xml \
  --class EnumerationDomain \
  --bb-name ddicdiEnumerationDomain \
  --out-dir _sources/ddiProperties/
```

See `agents.md` for full CLI options and convention details.

**Requirements:** Python 3.10+ with `pyyaml`

### DDI-CDI Consistency Audits

- **`audit_ddi_xmi_consistency.py`** — checks the `_sources/ddiProperties` BBs against a DDI-CDI EA XMI export: flags classes a BB references that are no longer in the model, attributes/associations added or dropped, and (with `--dump-class`) prints a class's full member set. `python tools/audit_ddi_xmi_consistency.py --xmi <xmi> [--bb NAME] [--dump-class A,B]`
- **`audit_cdif_vs_ddi.py`** — checks that every `cdi:`-prefixed property in `_sources/cdifProperties` has a value-type shape consistent with the corresponding `_sources/ddiProperties` definition; classifies MATCH / SOFT / STRUCTURAL / CDIF-ONLY.

### Validate Examples (`validate_examples.py`)

Validates all example JSON files against their resolved schemas. Uses `schema_resolver.py`'s `SchemaResolver` for proper `$defs` and cross-file `$ref` handling, with fallback to `tools/resolve_schema.py` for schemas with circular references.

```bash
python tools/validate_examples.py --verbose
python tools/validate_examples.py --filter person
```

**Requirements:** Python 3.6+ with `pyyaml`, `jsonschema`

### Validate with SHACL (`validate_shacl.py`)

Optional, standalone SHACL validation for one building block or profile (the JSON-Schema `validate_examples.py` stays the default gate). Gathers the target's `rules.shacl` plus every transitively-composed BB's rules, expands the target's examples from JSON-LD to RDF, and runs `pyshacl`. Report-only by default; `--strict` fails on `sh:Violation`. Catches cross-reference constraints JSON Schema can't (e.g. "every RepresentedVariable used by a component must be instantiated by an InstanceVariable").

```bash
python tools/validate_shacl.py CDIFDataStructureProfile
python tools/validate_shacl.py CDIFDataStructureProfile --verbose
python tools/validate_shacl.py CDIFDataStructureProfile --strict
```

**Requirements:** `pyshacl` (pulls in `rdflib`) — `pip install --user pyshacl`

### Audit Building Blocks (`audit_building_blocks.py`)

Comprehensive audit tool for any OGC Building Block repository. Checks file completeness, schema consistency, example validation, SHACL completeness, and property coverage.

```bash
python tools/audit_building_blocks.py -v
python tools/audit_building_blocks.py /path/to/_sources -v
python tools/audit_building_blocks.py --json -o report.json
```

**Requirements:** Python 3.6+ with `pyyaml`, `jsonschema`

### Generate Property Tree (`generate_property_tree2.py`)

Generates `propertyTree_2` worksheets from resolved JSON Schemas showing complete property hierarchy with type suffixes and array cardinality.

```bash
python tools/generate_property_tree2.py --profile all
python tools/generate_property_tree2.py --profile discovery
```

**Requirements:** Python 3.6+ with `openpyxl`, `pyyaml`

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
| `CDIFCodelistProfile` | CDIF Codelist profile (allOf: cdifCodelist) — thin wrapper over the `cdifCodelist` building block (a `skos:ConceptScheme` constrained for CDIF codelist use) |
| `CDIFDiscoveryProfile` | CDIF Discovery profile (allOf: cdifCore + discovery properties) |
| `CDIFDataDescriptionProfile` | CDIF Data Description profile (allOf: cdifCore + cdifDataDescription + discovery properties). Flat: InstanceVariables with `cdif:role`, `cdi:qualifies`, value-domain links (`cdi:takesSentinelValuesFrom` → `cdif:SentinelValueDomain`, `cdi:takesSubstantiveValuesFrom` → `cdif:SubstantiveValueDomain`; value domains carry `cdi:isDescribedBy` → `ValueAndConceptDescription`), and `cdif:isDescribedBy_StatisticsCollection`. Dataset-level extensions: `cdif:hasPrimaryKey` (ordered `cdi:ComponentPosition` wrappers around InstanceVariables), `cdif:statistics`. WebAPI distributions: the action result (`schema:potentialAction.schema:result`, the `actionResult` BB — no `contentUrl`/`contentSize`) carries the per-profile physical-realization properties (`cdif:hasPhysicalMapping`, `cdi:characterSet`) added via an `if @type contains schema:WebAPI` branch; a sibling `DataDownload` gets the same props at top level. No component classes. |
| `CDIFDataStructureProfile` | CDIF Data Structure profile (allOf: cdifCore + cdifDataDescription + cdifDataStructure + cdifDataStructureComponent + cdifRepresentedVariable + cdifValueDomain). Adds full DDI-CDI structural complexity: component subclasses (Identifier / Measure / Attribute / Dimension / VariableValue / VariableDescriptor), DataStructure variants (Dimensional / Long / Wide), RepresentedVariables, value domains, and DescriptorVariable for long-format data. Distributions carry `cdi:isStructuredBy` (conditionally required: at distribution level when `@type` contains `cdi:PhysicalDataSet`; on each `schema:potentialAction.schema:result` when `@type` contains `schema:WebAPI` — the WebAPI distribution describes the service, the result describes the bytes, and its `cdi:isStructuredBy` MAY differ from sibling distributions). InstanceVariables in this profile MUST NOT duplicate represented-variable-level properties (`cdi:hasIntendedDataType`, `cdi:describedUnitOfMeasure`, `cdif:simpleUnitOfMeasure`, `cdi:takesSentinelValuesFrom`, `cdi:takesSubstantiveValuesFrom`, `cdi:qualifies`) when the RepresentedVariable they `cdif:uses` already specifies them — enforced by conditional SHACL rules in `CDIFDataStructureProfile/rules.shacl` (the JSON-Schema-can't-express-subset simplification: any duplication is forbidden). |
| `CDIFcompleteProfile` | CDIF Complete profile (allOf: cdifCore + cdifDataDescription + cdifArchiveDistribution + cdifProvenance + discovery properties) |
| `CDIFxasProfile` | CDIF XAS profile (allOf: cdifCore + xasOptional + xasCore + discovery properties) |

See [agents.md](agents.md) for the full building block structure, authoring rules, and composition hierarchy.

### Published release repos (downstream)

Four separate repos publish the release form of these profiles for implementers — `core`, `discovery`, `datadescription`, and `codelist` (GitHub org `Cross-Domain-Interoperability-Framework`). Each carries a `*StructuredSchema.json` (generated here via `resolve_schema.py <Profile> --structured`), a merged `*Rules.shacl`, an implementation guide (`.md`/`.docx`), JSON-LD frame, and validated examples. They are **manually synced** from this repo (no automation) — see [agents.md](agents.md) §"Release profile repos & sync".

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
| cdifProperties | `_sources/cdifProperties/` | CDIF-specific properties (core, provenance, tabular/long data, OpenAPI-aligned WebAPI, plus the DDI-CDI structural family: `cdifInstanceVariable`, `cdifKey`, `cdifCodelist`, `cdifEnumerationDomain`, `cdifValueDomain`, `cdifRepresentedVariable`, `cdifDataStructure`, `cdifDataStructureComponent`, `cdifDescriptorVariable`, `cdifPhysicalMapping`, `cdifTextMapping`, `cdifLocatorMapping`, `cdifTabularTextDataSet`, `cdifStructuredDataSet`, `cdifDataFingerprint`, `cdifStatistics`) |
| ddiProperties | `_sources/ddiProperties/` | DDI-CDI vocabulary building blocks |
| provProperties | `_sources/provProperties/` | PROV-O provenance (generatedBy, derivedFrom, provActivity) |
| skosProperties | `_sources/skosProperties/` | W3C SKOS vocabulary building blocks (ConceptScheme, Concept, Collection) |
| qualityProperties | `_sources/qualityProperties/` | DQV data quality measures |
| xasProperties | `_sources/xasProperties/` | X-ray Absorption Spectroscopy domain properties |
| bioschemasProperties | `_sources/bioschemasProperties/` | Bioschemas vocabulary building blocks (lab protocols, samples, computational workflows) |
| profiles | `_sources/profiles/cdifProfiles/` | CDIF profiles |

### ddiProperties

DDI-CDI vocabulary building blocks for communities using the DDI Cross-Domain Integration standard natively. Most are **generated from a DDI-CDI XMI export** of the Enterprise Architect UML model via `tools/uml_to_schema.py`, which auto-detects the canonical XMI 2.5.1 and the EA-native XMI 1.1 formats (see `agents.md` for details). The set was reconciled against the 2026-03 DDI-CDI model: `ddicdiDataStore` was retired in favour of `ddicdiLogicalRecordRepository`, `ddicdiPhysicalSegmentLayout` in favour of `ddicdiPhysicalMapping`, and `ddicdiStatistics` / `ddicdiKeyValueStructure` / `ddicdiCollections` were added. The table below is representative, not exhaustive.

Each BB's `schema.yaml` validates a single Node (or, for multi-class BBs, an `anyOf` of Node `$defs`); profile schemas wrap nodes for `@graph` JSON-LD documents. Class-typed properties default to inline-or-ref (`anyOf [class def, id-reference]`), where the class def comes from another BB if one owns that class, otherwise inlined locally.

| Building Block | Description |
|----------------|-------------|
| `ddicdiActivity` | DDI-CDI Activity class (DDICDILibrary/Classes/Process) -- describes tasks using `cdi:Activity`, `cdi:Step`, and `cdi:Parameter`. Includes `cdi:definition` (InternationalString), `cdi:start`/`cdi:end` (timestamps), `cdi:hasInternal` (ControlLogic), `cdi:entityUsed`/`cdi:entityProduced` (References), and `cdi:has_Step` with `cdi:script` (CommandCode). SHACL shapes for Activity and Step. |
| `ddicdiDataTypes` | Shared DDI-CDI data types used across BBs: identifiers (`cdi:Identifier`, `cdi:NonDdiIdentifier`, `cdi:IRDI`), names (`cdi:ObjectName`, `cdi:IndividualName`, `cdi:OrganizationName`), contact information (`cdi:ContactInformation`, `cdi:Address`, `cdi:Email`, `cdi:Telephone`, `cdi:WebLink`), references (`cdi:Reference`, `cdi:ControlledVocabularyEntry`, `cdi:PairedControlledVocabularyEntry`), strings (`cdi:InternationalString`, `cdi:LanguageString`), and others (`cdi:DateRange`, `cdi:CombinedDate`, `cdi:PrivateImage`, `cdi:CatalogDetails`, `cdi:AccessLocation`). |
| `ddicdiIndividual` | DDI-CDI Individual agent (person) with `cdi:individualName` (IndividualName), `cdi:contactInformation`, and identification. Refs `ddicdiDataTypes` for shared data types. |
| `ddicdiMachine` | DDI-CDI Machine agent (software/hardware) with `cdi:accessLocation`, `cdi:function`, `cdi:machineInterface`, and `cdi:typeOfMachine`. Refs `ddicdiDataTypes` for shared data types. |
| `ddicdiOrganization` | DDI-CDI Organization agent (group/institution) with `cdi:organizationName` (OrganizationName), `cdi:contactInformation`, and identification. Refs `ddicdiDataTypes` for shared data types. |
| `ddicdiProcessingAgent` | DDI-CDI ProcessingAgent that orchestrates activities via `cdi:performs` and `cdi:operatesOn` (ProductionEnvironment references). Refs `ddicdiDataTypes` for shared data types. |
| `ddicdiAgent` | Umbrella building block composing the 4 agent subtypes (`ddicdiIndividual`, `ddicdiMachine`, `ddicdiOrganization`, `ddicdiProcessingAgent`) via root `anyOf` of `$ref` to each sub-BB. |
| `ddicdiValueDomain` | DDI-CDI ValueDomain (DDICDILibrary/Classes/Representations) -- multi-root BB covering both `cdi:SubstantiveValueDomain` (subject-matter values) and `cdi:SentinelValueDomain` (processing/missing-value codes like SAS `.R`, SPSS `999`). Includes `cdi:isDescribedBy` (ValueAndConceptDescription with min/max bounds, regex, classification level), `cdi:takesValuesFrom` (refs `ddicdiEnumerationDomain`), `cdi:takesConceptsFrom` (Substantive/SentinelConceptualDomain), and `cdi:platformType` (sentinel only). |
| `ddicdiEnumerationDomain` | DDI-CDI EnumerationDomain — base class acting as an extension point so all codifications (codelist, statistical classification, etc.) are usable as enumerated value domains. Refs LevelStructure, CategorySet, Concept. |
| `ddicdiCodeList` | DDI-CDI CodeList (extends EnumerationDomain) — collection of `cdi:Code`s with their `cdi:CodePosition`s. Both targets reachable via `cdi:has` (merged `anyOf`). |
| `ddicdiStatisticalClassification` | DDI-CDI StatisticalClassification (extends EnumerationDomain) — full classification with `cdi:has` reaching ClassificationItem / ClassificationItemPosition / LevelStructure, plus `cdi:isMaintainedBy` (refs `ddicdiOrganization`), `cdi:isIndexedBy` (ClassificationIndex), and self-references for variant/successor/predecessor lineage. |
| `ddicdiControlledVocabularyEntry` | DDI-CDI ControlledVocabularyEntry — entry from an externally maintained controlled vocabulary. 5 properties: `cdi:entryReference`, `cdi:entryValue`, `cdi:name`, `cdi:valueForOther`, `cdi:vocabulary`. Same shape as the inlined `dt-ControlledVocabularyEntry` `$def` in `ddicdiDataTypes`. |
| `ddicdiDataStructure` | DDI-CDI DataStructure — multi-root BB covering DataStructure plus the four leaf subclasses (`Dimensional`, `KeyValue`, `Long`, `Wide`). Inherits component properties from DataStructureComponent: `cdi:has → ForeignKey` (1..*), `cdi:identifier`, `cdi:isDefinedBy → RepresentedVariable` (refs `ddicdiRepresentedVariable`), `cdi:semantic`, `cdi:specialization`. |
| `ddicdiDataStructureComponent` | DDI-CDI DataStructureComponent subclasses (IdentifierComponent, MeasureComponent, AttributeComponent, DimensionComponent, VariableValueComponent, VariableDescriptorComponent). |
| `ddicdiRepresentedVariable` | DDI-CDI RepresentedVariable — variable definition with `cdi:takesSubstantiveValuesFrom` / `cdi:takesSentinelValuesFrom` (refs `ddicdiValueDomain`), conceptual domains, unit-of-measure, and intended data type. Pulled out as its own BB to break the DataStructure → RepresentedVariable → ValueDomain transitive cascade. |
| `ddicdiInstanceVariable` | DDI-CDI InstanceVariable plus the RepresentedVariable property set (ConceptualVariable-level properties excluded). |
| `ddicdiPresentationalVariable` | DDI-CDI ReferenceVariable / DescriptorVariable — long-format presentational variables. |
| `ddicdiLogicalRecord` | DDI-CDI LogicalRecord. |
| `ddicdiLogicalRecordRepository` | DDI-CDI LogicalRecordRepository — successor to the retired `DataStore` class (renamed and relocated to the FormatDescription package in the 2026-03 model). `$defs` for LogicalRecordRepositoryStructure, LogicalRecordRelationship (successor to RecordRelation), and InstanceVariableMap. |
| `ddicdiPhysicalDataSet` | DDI-CDI PhysicalDataSet subclasses (Wide / Long / Dimensional / Tabular / Structured DataSet). |
| `ddicdiPhysicalMapping` | DDI-CDI PhysicalMapping — successor to the retired `ValueMapping` class; describes how an InstanceVariable's values are physically represented. Root validates `cdi:PhysicalMapping` / `cdi:TextMapping` / `cdi:LocatorMapping`; `$def` for PhysicalMappingPosition. |
| `ddicdiStatistics` | DDI-CDI Statistics / CategoryStatistics / StatisticsCollection — summary and per-category statistics for an instance variable. |
| `ddicdiKeyValueStructure` | DDI-CDI KeyValueStructure family (KeyValue package): KeyValueStructure, KeyValueDataStore, InstanceKey, MainKeyMember, ContextualComponent, SyntheticIdComponent. |
| `ddicdiCollections` | DDI-CDI CollectionsPattern: the generic Collection / List / Map / Member / MemberRelationship / Position / Structure / Comparison machinery. |

### skosProperties

W3C SKOS vocabulary building blocks for controlled vocabulary and codelist representation.

| Building Block | Description |
|----------------|-------------|
| `skosConceptScheme` | SKOS ConceptScheme with `skos:hasTopConcept`, prefLabel, and nested concepts. Base for `CDIFCodelistProfile`. |
| `skosConcept` | SKOS Concept with prefLabel, notations, broader/narrower/related hierarchical relations, cross-scheme mapping properties, and documentary notes. Defines `$defs`: ConceptRef, LanguageTaggedValue. |
| `skosCollection` | SKOS Collection and OrderedCollection. Collection groups concepts via `skos:member`; OrderedCollection preserves ordering via JSON-LD `@list`. References `skosConcept` for concept items. |

### schemaorgProperties

Schema.org vocabulary building blocks for reusable metadata components.

| Building Block | Description |
|----------------|-------------|
| `instrument` | Generic instrument or instrument system -- uses `schema:Thing` base type with optional `schema:Product` typing. Supports hierarchical instrument systems via `schema:hasPart` for sub-components. Instruments are nested within `prov:used` items via a `schema:instrument` sub-key (instruments are `prov:Entity` subclasses). Referenced by `cdifProvActivity`, `provActivity`, and `xasInstrument`. |
| `statisticalVariable` | `schema:StatisticalVariable` — a variable representing a statistical measure. Properties: `@type`, `@id`, `schema:name`, `schema:description`, `schema:measurementTechnique`, `schema:statType`, `schema:measuredProperty`. Uses `definedTerm` building block. |
| `actionResult` | The `schema:result` of a `schema:Action` on a WebAPI distribution — the format/serialization of the data the service returns. Typed `schema:DataDownload` but with **no** `schema:contentUrl`/`schema:contentSize` (the response is generated per request). Properties: `@type`, `schema:name`, `schema:description`, `schema:encodingFormat`, `dcterms:conformsTo`. Referenced by the `action` BB's `schema:result`. |

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
| `xasSample` | Material sample that is the `schema:mainEntity` of an XAS analysis (extends `schema:Product`). |
| `xasInstrument` | XAS instrument with `schema:hasPart` for hierarchical sub-components (refs generic instrument building block). |
| `xasFacility` | XAS facility (synchrotron source / beamline host). |
| `xasGeneratedBy` | XAS analysis event — extends `cdifProvActivity` with `xas:AnalysisEvent` typing, XAS facility location, sample object, XAS-specific instrument types, and XAS additional properties (edge_energy, calibration method, etc.). |
| `xasXdiTabularTextDataset` | XDI data structure description — fixed-width tabular text dataset for XAS experiment results. |
| `xasCore` | XAS mandatory properties — `prov:wasGeneratedBy` items use `allOf` with `cdifProvActivity` + NXsource/NXmonochromator instrument constraints via `schema:instrument` sub-key. |
| `xasOptional` | Same provenance structure as `xasCore` — `cdifProvActivity` activity with XAS instrument constraints. |

## Building Block Conformance URIs

Each building block that represents a CDIF specification component declares a required `dcterms:conformsTo` URI in the metadata catalog record (`schema:subjectOf`). When building blocks are composed into profiles via `allOf`, these constraints roll up automatically — the conformsTo array must include URIs for **all** constituent building blocks. Corresponding SHACL shapes enforce the same constraints via `sh:hasValue` on `dcterms:conformsTo`.

See [agents.md → Building Block Conformance URIs](agents.md#building-block-conformance-uris) for the canonical table of URIs, the per-profile rollup, the URI convention (no trailing slash), and the JSON Schema / SHACL patterns used to enforce them.

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
