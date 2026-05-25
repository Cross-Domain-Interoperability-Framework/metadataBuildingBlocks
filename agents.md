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
│   │   ├── definedTermSet/          # schema:DefinedTermSet (controlled vocab / list of DefinedTerms)
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
│   │   ├── cdifPhysicalMapping/     # CDIF physical mapping — per-field physical representation of a variable in a distribution (cdif:index, cdif:format, cdif:physicalDataType, cdi:nullSequence, cdif:formats_InstanceVariable)
│   │   ├── cdifStatistics/          # CDIF Statistics / CategoryStatistics / StatisticsCollection — summary values for a dataset/variable; cdif:appliesTo links the variable, cdif:has_* are target-suffixed (cdi:has is polymorphic in DDI-CDI)
│   │   ├── cdifOpenApi/             # OpenAPI-aligned WebAPI distribution (alternative to schemaorgProperties/webAPI)
│   │   ├── cdifKey/                 # CDIF Key — ordered set of cdi:InstanceVariables (referenced via cdifInstanceVariable) that uniquely identify a data instance; CDIF profile of ddi-cdi Key/PrimaryKey
│   │   ├── cdifCodelist/            # CDIF Codelist — a skos:ConceptScheme constrained for CDIF use (resolvable @id; CdifCodelistConcept members require @id, skos:inScheme, skos:prefLabel, skos:notation; paired skos:narrower/skos:broader for hierarchy). Referenced by CDIFCodelistProfile and by cdifEnumerationDomain (cdif:references)
│   │   ├── cdifEnumerationDomain/   # CDIF Enumeration Domain — extension point that documents a codification as a cdif:EnumerationDomain; cdif:references accepts a cdifCodelist, a schema:DefinedTermSet, or an @id-only reference
│   │   ├── cdifValueDomain/         # CDIF Value Domain — cdi:SubstantiveValueDomain + cdi:SentinelValueDomain, with bounds, regex, takesValuesFrom (cdifEnumerationDomain), takesConceptsFrom (skos:Concept)
│   │   ├── cdifRepresentedVariable/ # CDIF RepresentedVariable — conceptual variable definition referenced by Data Structure components; carries name, definition, intended data type, unit-of-measure, takesSubstantiveValuesFrom / takesSentinelValuesFrom
│   │   ├── cdifDataStructure/       # CDIF DataStructure — root `anyOf` over cdi:DataStructure / cdi:DimensionalDataStructure / cdi:LongDataStructure / cdi:WideDataStructure; carries components, primary key, foreign keys, dimension groups. LongDataStructure enforces 1× IdentifierComponent / 1× VariableDescriptorComponent / 1× VariableValueComponent (+ 0..* Attribute) via Draft 2020-12 `contains` + `minContains`/`maxContains`.
│   │   ├── cdifDataStructureComponent/  # CDIF DataStructureComponent — component subclasses (cdi:IdentifierComponent, cdi:MeasureComponent, cdi:AttributeComponent, cdi:DimensionComponent, cdi:VariableValueComponent, cdi:VariableDescriptorComponent); `cdi:isDefinedBy` refs cdifRepresentedVariable (or cdifDescriptorVariable for the descriptor variant); `AttributeComponent.cdi:qualifies` carries the attribute-qualifies-measure relationship at component level.
│   │   ├── cdifDescriptorVariable/  # CDIF DescriptorVariable + DescriptorValueDomain — long-format pattern where a descriptor-column code maps to the RepresentedVariable it names; `cdif:takesValuesFrom` entries pair `cdif:value` (the code) with `cdif:isDefinedBy → cdi:RepresentedVariable`
│   │   └── cdifReference/           # CDIF Reference — typed external reference combining schema.org labeled-link surface (name, description, url) with DDI-CDI dt-Reference semantics and an optional `cdif:semantic` SKOS Concept role
│   ├── provProperties/              # W3C PROV provenance types
│   │   ├── generatedBy/             # prov:wasGeneratedBy (Activity)
│   │   ├── provActivity/            # PROV-O native activity (extends generatedBy)
│   │   └── derivedFrom/             # prov:wasDerivedFrom
│   ├── ddiProperties/               # DDI-CDI data description types (most generated from XMI via tools/uml_to_schema.py; reconciled with the 2026-03 DDI-CDI model)
│   │   ├── ddicdiActivity/          # DDI-CDI Activity (Process package)
│   │   ├── ddicdiAgent/             # DDI-CDI Agent (umbrella: refs 4 agent sub-BBs)
│   │   ├── ddicdiIndividual/        # DDI-CDI Individual (person)
│   │   ├── ddicdiMachine/           # DDI-CDI Machine (software/hardware)
│   │   ├── ddicdiOrganization/      # DDI-CDI Organization (group/institution)
│   │   ├── ddicdiProcessingAgent/   # DDI-CDI ProcessingAgent (orchestrates activities)
│   │   ├── ddicdiDataTypes/          # DDI-CDI structured data types (from DDICDILibrary/DataTypes; incl. CorrespondenceDefinition, StructureSpecification)
│   │   ├── ddicdiValueDomain/       # DDI-CDI ValueDomain (SubstantiveValueDomain + SentinelValueDomain)
│   │   ├── ddicdiEnumerationDomain/ # DDI-CDI EnumerationDomain (base for codifications)
│   │   ├── ddicdiCodeList/          # DDI-CDI CodeList (Code + CodePosition collections)
│   │   ├── ddicdiStatisticalClassification/  # DDI-CDI StatisticalClassification (with ClassificationItems and LevelStructure)
│   │   ├── ddicdiControlledVocabularyEntry/  # DDI-CDI ControlledVocabularyEntry (entry in an external vocabulary)
│   │   ├── ddicdiInstanceVariable/  # DDI-CDI InstanceVariable + RepresentedVariable property set (ConceptualVariable-level props excluded)
│   │   ├── ddicdiRepresentedVariable/  # DDI-CDI RepresentedVariable (variable definition with VD/CD ranges)
│   │   ├── ddicdiPresentationalVariable/  # DDI-CDI ReferenceVariable / DescriptorVariable (long-format presentational variables)
│   │   ├── ddicdiLogicalRecord/     # DDI-CDI LogicalRecord
│   │   ├── ddicdiLogicalRecordRepository/  # DDI-CDI LogicalRecordRepository — successor to the retired DataStore class (+ LogicalRecordRepositoryStructure, LogicalRecordRelationship, InstanceVariableMap)
│   │   ├── ddicdiPhysicalDataSet/   # DDI-CDI PhysicalDataSet subclasses (Wide/Long/Dimensional/Tabular/Structured DataSet)
│   │   ├── ddicdiPhysicalMapping/   # DDI-CDI PhysicalMapping / TextMapping / LocatorMapping — successor to the retired ValueMapping class
│   │   ├── ddicdiDataStructure/     # DDI-CDI DataStructure (Dimensional/Long/Wide variants + shared key structures)
│   │   ├── ddicdiDataStructureComponent/  # DDI-CDI DataStructureComponent subclasses
│   │   ├── ddicdiStatistics/        # DDI-CDI Statistics / CategoryStatistics / StatisticsCollection
│   │   ├── ddicdiKeyValueStructure/ # DDI-CDI KeyValue package (KeyValueStructure, KeyValueDataStore, InstanceKey, ...)
│   │   └── ddicdiCollections/       # DDI-CDI CollectionsPattern (Collection, List, Map, Member, Structure, ...)
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
│   │   ├── xasXdiTabularTextDataset/ # XDI tabular text dataset
│   │   ├── xasCore/             # XAS mandatory property group
│   │   └── xasOptional/             # XAS optional property group
│   └── profiles/                    # Top-level profiles that compose BBs
│       └── cdifProfiles/
│           ├── CDIFCodelistProfile/        # CDIF Codelist profile (thin allOf wrapper over the cdifCodelist BB)
│           ├── CDIFDiscoveryProfile/       # CDIF Discovery profile
│           ├── CDIFcompleteProfile/        # CDIF Complete profile (discovery + data description + provenance + archive)
│           ├── CDIFDataDescriptionProfile/ # CDIF Data Description profile (flat: InstanceVariables with cdif:role / cdi:qualifies; no component classes)
│           ├── CDIFDataStructureProfile/   # CDIF Data Structure profile (full DDI-CDI: cdifDataStructure + cdifDataStructureComponent + cdifRepresentedVariable + cdifValueDomain; distributions must carry cdi:isStructuredBy)
│           └── CDIFxasProfile/             # CDIF XAS profile
├── tools/
│   ├── resolve_schema.py            # Schema resolver (see below)
│   ├── uml_to_schema.py             # Generate a BB schema.yaml from a DDI-CDI XMI (canonical 2.5.1 or EA-native 1.1, auto-detected; see below)
│   ├── convert_for_jsonforms.py     # JSON Forms converter (see below)
│   ├── compare_schemas.py           # Schema comparison tool
│   ├── validate_instance.py         # Profile-aware validation tool
│   ├── validate_examples.py         # Validates all examples against resolved schemas (JSON Schema only)
│   ├── validate_shacl.py            # Standalone SHACL validation for a BB/profile (gathers rules transitively, expands JSON-LD, runs pyshacl)
│   ├── augment_register.py          # Adds resolvedSchema URLs to register.json
│   ├── regenerate_schema_json.py    # Regenerates *Schema.json files from schema.yaml sources
│   ├── test_redirects.py            # Tests w3id.org redirect rules for building block URIs
│   ├── update_conformsto_uris.py    # Updates conformsTo URIs in building block schemas
│   ├── audit_building_blocks.py     # Comprehensive BB repo audit (pluggable to any repo)
│   ├── audit_shacl_coverage.py      # Compares schema.yaml properties vs rules.shacl shapes
│   ├── audit_cdi_property_types.py  # Audits cdi:* properties in cdifProperties vs canonical DDI-CDI XMI
│   ├── audit_ddi_xmi_consistency.py # Audits ddiProperties BBs vs a DDI-CDI EA XMI export (missing/renamed classes, attr/assoc drift; --dump-class)
│   ├── audit_cdif_vs_ddi.py         # Audits cdi:* property value-types in cdifProperties vs ddiProperties BB definitions
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

## Namespace Conventions: `cdi:` vs `cdif:`

The `cdi:` prefix (`http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/`) is reserved for properties and classes defined in the canonical DDI-CDI 1.0 XMI model. The `cdif:` prefix (`https://cdif.org/0.1/`) is used for CDIF inventions, simplifications, or properties whose CDIF semantics diverge from the canonical XMI definition.

Audit rule: if a property in a `cdifProperties/` BB carries the `cdi:` prefix, the values it accepts must be type-compatible with the corresponding `ddiProperties/` definition. If CDIF needs to allow a value shape the XMI doesn't sanction (e.g. literal vs node, or a different target class), rename the property to `cdif:` so the divergence is namespace-visible. Run `tools/audit_cdif_vs_ddi.py` to check. Recent renames driven by this audit (May 2026):
- `cdi:fileSize` → `cdif:fileSize`, `cdi:fileSizeUofM` → `cdif:fileSizeUofM` (file metadata; not in XMI) — **later removed entirely** (May 2026): file size on a file distribution is `schema:contentSize` (now in the `dataDownload` BB); an action result has no fixed size.
- `cdi:role` → `cdif:role` (role-on-InstanceVariable; CDIF-only simplification)
- `cdi:content` retained inside `cdi:LanguageString` / `cdi:LabelForDisplay` (canonical use); migrated to `cdif:content` only outside those structured-string contexts
- `cdi:statistics` → `cdif:statistics`, `cdi:appliesTo` → `cdif:appliesTo`, `cdi:indexedBy` → `cdif:indexedBy` (CDIF additions, not in the canonical model)

Three further `cdif:` conventions established in the 2026-03-model reconciliation:
- **InternationalString / LabelForDisplay / ObjectName simplification.** Where a canonical DDI-CDI property is valued by one of those structured-string datatypes, the CDIF profile simplifies it to a plain `string` and renames the property to `cdif:`. Applied **repo-wide (2026-05): `cdi:name`/`cdi:displayLabel`/`cdi:definition`/`cdi:descriptiveText` → `cdif:*`** across cdifProperties + profiles (not just `cdi:Category` in `cdifStatistics`); examples were also flattened (structured `{@type:[cdi:ObjectName],cdi:name}` / LabelForDisplay / InternationalString objects → plain strings under the `cdif:*` keys). `cdi:regularExpression` on `ValueAndConceptDescription` was likewise simplified to a plain `string` (the `TypedString` $def was dropped from CDIF). The `TypedString → String` rule also lives in the DataStructure UML `datatypeSubstitutions`.
- **Polymorphic role-name disambiguation.** The DDI-CDI association role names `has`, `uses`, `isDefinedBy`, `isDescribedBy` are polymorphic (their valid target depends on the owning class). In `cdifProperties` they are split into target-suffixed `cdif:` keys — `cdif:has_DataStructureComponent`, `cdif:has_Concept`, `cdif:uses_Concept`, `cdif:isDefinedBy_RepresentedVariable`, `cdif:isDefinedBy_DescriptorVariable`, `cdif:isDefinedBy_Concept`, `cdif:isDescribedBy_StatisticsCollection`, etc. — so each JSON key has a single, unambiguous value type.
- **ControlledVocabularyEntry → skos:Concept normalization (union-type policy).** Canonical DDI-CDI `cdi:ControlledVocabularyEntry` and `cdi:PairedControlledVocabularyEntry` values are implemented as `skos:Concept` from the skosProperties building block. Concept-typed slots — including `cdi:typeOfStatistic` (in `cdifStatistics`) and `cdi:semantic` (on Data Structure components) — accept an `@id`-only reference into a known scheme, a structured `schema:DefinedTerm`, or a full inline `skos:Concept` node. Plain strings are **not** permitted, because vocabulary identity cannot be recovered from an unscoped string label. Where CDIF instead chooses a plain-string shortcut for a ControlledVocabularyEntry attribute (e.g. `cdif:encoding` on `cdifStructuredDataSet` = a bare charset string), that is a divergence and is therefore `cdif:`, not `cdi:`.
- **Enumerations stay `cdi:` with an `enum:` constraint.** A DDI-CDI enumeration (e.g. `TableDirectionValues`, `TextDirectionValues`, `TrimValues` on TabularTextDataSet) is type-faithful as a JSON `string` with an `enum:` listing the literal values, so it remains `cdi:` (matching the canonical `ddiProperties/ddicdiPhysicalDataSet`) — it is *not* a simplification. Verify `cdi:*` value types against the **1.1 canonical XMI** with `tools/audit_cdi_property_types.py` (note: that tool's hardcoded `XMI =` path is stale — repoint it at the current 1.1 XMI), cross-checking the generated `ddiProperties/ddicdi*` tree as the reference encoding.

## Data Description vs Data Structure profiles

CDIF carries two parallel ways to describe a dataset's variables:

- **CDIFDataDescriptionProfile** — flat: each `schema:variableMeasured` item is a `cdi:InstanceVariable` with `cdif:role` (UnitIdentifier / Measure / Attribute / Dimension / Descriptor / ReferenceVariable) and, for Attribute, `cdi:qualifies` pointing at the qualified InstanceVariable. Value-domain links (`cdi:takesSentinelValuesFrom` → `cdif:SentinelValueDomain`, `cdi:takesSubstantiveValuesFrom` → `cdif:SubstantiveValueDomain`) live **at the profile level** (added via `cdifDataDescription/schema.yaml`'s `allOf` on `schema:variableMeasured.items`), not on the base `cdifInstanceVariable` BB — this is the mechanism by which Discovery's plain `PropertyValue` and the Data-Description-level extended InstanceVariable diverge from the same base. Per-variable statistics: `cdif:isDescribedBy_StatisticsCollection`. Dataset-level: `cdif:hasPrimaryKey`, `cdif:statistics`. No component classes, no DataStructure node required.
- **CDIFDataStructureProfile** — full DDI-CDI: `schema:variableMeasured` items still carry InstanceVariables (for physical-column identity), but `cdif:role` is forbidden at this level (redundant — the component subclass on `cdi:isStructuredBy` encodes role). The structural commitments live on `cdi:isStructuredBy → cdi:DataStructure / cdi:DimensionalDataStructure / cdi:LongDataStructure / cdi:WideDataStructure`, which carries `cdi:has_DataStructureComponent` items (IdentifierComponent, MeasureComponent, AttributeComponent, DimensionComponent, VariableValueComponent, VariableDescriptorComponent), `cdi:has_PrimaryKey`, foreign keys, and dimension groups. RepresentedVariables and value domains hang off `cdi:isDefinedBy` on each component. The profile's `cdi:isStructuredBy` slots (distribution-level and `potentialAction.result`) reference the concrete variant `$defs` — `cdifDataStructure/schema.yaml#/$defs/{Dimensional,Wide,Long}DataStructure` — plus the abstract `#/$defs/DataStructure` (kept because the bare-`cdi:PhysicalDataSet` rule requires the abstract); the `cdifDataStructure` BB itself is unchanged.

### Physical dataset layout: PhysicalDataSet subclasses & mappings (Data Description)

A `cdi:PhysicalDataSet` is implemented as a `schema:DataDownload` distribution, optionally dual-typed as a DDI-CDI subclass. `cdifDataDescription` adds, via `if @type contains … then`:

- **`cdi:TabularTextDataSet`** → mixes in `cdifTabularTextDataSet` (delimited/fixed-width layout: `cdi:delimiter`, `cdi:hasHeader`, `cdi:headerRowCount`, `cdi:quoteCharacter`, `cdi:lineTerminator`, `cdi:tableDirection` / `cdi:textDirection` / `cdi:trim` as `string`+`enum`, …). Per-field mappings are `cdifTextMapping`.
- **`cdi:StructuredDataSet`** → mixes in `cdifStructuredDataSet` (XML/JSON; `cdif:encoding`). Fields are located with `cdifLocatorMapping` (`cdi:locator` = XPath/JSONPath) rather than a column index — enforced by the `cdifd:structuredDataSetLocatorMappingShape` SHACL rule (Violation) in `cdifDataDescription/rules.shacl`, because the JSON Schema keeps `cdif:hasPhysicalMapping` permissive.
- Every `schema:DataDownload` may carry `cdi:fingerprint` → `cdifDataFingerprint` (checksum/hash datatype) and `cdi:characterSet`.

`cdif:hasPhysicalMapping` items are `anyOf[cdifPhysicalMapping, cdifTextMapping, cdifLocatorMapping]`. **Mapping class split:** `cdifPhysicalMapping` is the serialization-agnostic base (`cdif:index`, `cdif:format`, `cdif:physicalDataType`, `cdi:numberPattern`, `cdi:scale`, null sequence, …); `cdifTextMapping` extends it with text specifics (`cdi:length`, decimal/digit separators, `cdif:displayLabel`); `cdifLocatorMapping` adds `cdi:locator` for structured documents. `cdifTabularTextDataSet` / `cdifStructuredDataSet` are typeless attribute mixins flagged `isTypeLibrary: true` (no examples — the `@type` token lives on the distribution). `cdifDataCube` (also a `cdi:StructuredDataSet`) uses the same `cdi:locator`.

### RepresentedVariable / InstanceVariable disambiguation (Data Structure profile)

In the Data Structure profile, the InstanceVariable in `schema:variableMeasured` is conceptually a pointer (via `cdif:uses`) into a richer RepresentedVariable that lives inside `cdi:isStructuredBy.cdi:has_DataStructureComponent.cdif:isDefinedBy_RepresentedVariable`. The RepresentedVariable carries the conceptual/represented-level properties; the InstanceVariable carries the physical-column identity.

To prevent the same property being declared in both places at this profile level, the Data Structure profile applies a **conditional SHACL rule per property** in `CDIFDataStructureProfile/rules.shacl` (six shapes: `NoDuplicateHasIntendedDataTypeShape`, `NoDuplicateDescribedUnitOfMeasureShape`, `NoDuplicateSimpleUnitOfMeasureShape`, `NoDuplicateTakesSentinelValuesFromShape`, `NoDuplicateTakesSubstantiveValuesFromShape`, `NoDuplicateQualifiesShape`):

> If the RepresentedVariable referenced by the InstanceVariable's `cdif:uses` already specifies property *P* (for `cdi:qualifies`: if the wrapping AttributeComponent specifies it), then *P* MUST NOT also be set on the InstanceVariable.

Simplification: JSON Schema and SHACL can't easily express "the InstanceVariable's value domain is a subset of the RepresentedVariable's" — so any duplication is forbidden rather than verifying subsetness. The JSON schema does NOT blanket-disallow these properties on the InstanceVariable; only the SHACL rules fire (and only when there is actually a RepresentedVariable to consult).

`CDIFDataStructureProfile/rules.shacl` also carries two **cross-reference integrity** shapes for RepresentedVariables referenced by a component (`cdif:isDefinedBy_RepresentedVariable`), both `sh:Violation` and both using `sh:targetObjectsOf cdif:isDefinedBy_RepresentedVariable`:

- `RepresentedVariableMustHaveStableIdShape` — the RV must be an IRI node (`sh:nodeKind sh:IRI`), i.e. have a stable `@id`, not an inline blank node.
- `RepresentedVariableMustBeInstantiatedShape` — the RV must be referenced by at least one `cdi:InstanceVariable` via `cdif:uses` (inverse-path qualified count).

These are coverage/identity constraints JSON Schema cannot express (they correlate sets of `@id`s across `schema:variableMeasured` and `cdi:isStructuredBy`), so they only run under SHACL — in CI, or locally via `tools/validate_shacl.py`, not in the JSON-Schema-only `validate_examples.py`.

### Value domains & descriptor components (2026-05)
A `cdifValueDomain` node (`cdif:SubstantiveValueDomain` | `cdif:SentinelValueDomain`) carries `cdif:takesValuesFrom` (→ `cdifEnumerationDomain`), `cdif:displayLabel`, `cdif:recommendedDataType`, and **`cdi:isDescribedBy` → `ValueAndConceptDescription`** (ranges, patterns, classification level, expressions; the `ValueAndConceptDescription` `$def` lives in `cdifValueDomain`). CDIF does **not** model the DDI-CDI conceptual side: there is no `cdi:takesConceptsFrom`, no `Substantive/SentinelConceptualDomain`, no `cdi:ConceptSystem` (and DDI-CDI `ReferenceVariable` collapses to a plain `cdifRepresentedVariable`). `cdifDescriptorVariable` (long-format descriptor) is minimal: `@id` + `cdif:name` + `cdif:hasValuesFrom` → `DescriptorValueDomain`. **`cdi:refersTo` on a `VariableDescriptorComponent` must point at a `cdi:VariableValueComponent`** — enforced by `cdifDataStructureComponent/rules.shacl` (`cdifVariableDescriptorComponentShape`, `sh:class cdi:VariableValueComponent`), since JSON Schema types it only as an `@id` reference.

### Conditional distribution typing rules (Data Structure profile)

Profile-level `if/then` constraints on `schema:distribution.items` (inline in the profile's `schema.yaml`, not via BB composition, because the resolver's `deep_merge` would drop them otherwise):

| `@type` includes... | `cdif:hasPhysicalMapping` | `cdi:isStructuredBy` |
|---|---|---|
| `cdi:TabularTextDataSet` or `cdi:StructuredDataSet` | **required** | any DataStructure variant |
| `cdi:PhysicalDataSet` (no subclass) | not required at this level | required on the distribution; abstract `cdi:DataStructure` only — Long/Dimensional/Wide forbidden (an `@id`-only reference also passes) |
| `schema:WebAPI` | not required on the distribution itself | **not required on the distribution**; required on each `schema:potentialAction.schema:result` (see below) |

The bare-`cdi:PhysicalDataSet` case is the "structure reuse" pattern: a dataset that points at a Data Structure node defining RepresentedVariables + components without committing to a specific physical file layout.

### WebAPI `schema:potentialAction.schema:result` physical realization

A `schema:WebAPI` distribution describes the *service*; the bytes it serves are
described by the action **result**, so physical-realization metadata lives on
`schema:distribution.items.schema:potentialAction.items.schema:result`, not on the
WebAPI distribution itself.

- **`potentialAction` is WebAPI-only.** It comes from the `webAPI` BB (on the
  `WebAPI` branch of cdifCore's `distribution.items.anyOf`). Do **not** add
  `potentialAction` at `distribution.items` level — that wrongly applies it to
  `DataDownload` too and duplicates the result.
- **The result base type is its own BB:** `schemaorgProperties/actionResult`
  (`@type` contains `schema:DataDownload`, `schema:name`, `schema:description`,
  `schema:encodingFormat`, `dcterms:conformsTo`). The `action` BB's `schema:result`
  `$ref`s it. Unlike a file `DataDownload`, the result has **no** `schema:contentUrl`
  / `schema:contentSize` — the response is generated per request, so its size
  depends on the request. (`cdif:fileSize` / `cdif:fileSizeUofM` were **removed**;
  file size on a file distribution is `schema:contentSize`.)
- **Data Description** adds the per-profile physical props to the result via an
  `if @type contains schema:WebAPI` branch in `cdifDataDescription`'s
  `schema:distribution.items.allOf` (a sibling `if @type contains
  schema:DataDownload` branch adds the same props at the DataDownload top level):
  `cdi:characterSet`, `cdif:hasPhysicalMapping` (whose `cdif:formats_InstanceVariable`
  references the **parent dataset's** `schema:variableMeasured` `@id`s — the API
  response is another physical realization of the same conceptual variables; do not
  redeclare InstanceVariables on the result). These props are scoped to the Data
  Description profile — they do **not** appear in Core or Discovery. (This BB-level
  `items.allOf` `if/then` survives composition — verified in the BB's resolvedSchema
  — because the profile composes it as a separate `allOf` member; contrast the Data
  Structure profile, which inlines its distribution `if/then` in the profile schema.)
- **Data Structure** result: `cdi:isStructuredBy`. MAY differ from sibling
  DataDownload distributions' `cdi:isStructuredBy` (e.g., the API may serve a
  long-format variant of a wide-format file download).

The same SHACL rules that target `cdi:TabularTextDataSet` / `cdi:StructuredDataSet` / `cdif:hasPhysicalMapping` apply unchanged because their targets are class-based or path-agnostic.

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
| CDIFDataStructureProfile | `core/1.0` + `data_description/1.0` + `data_structure/1.0` |
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

3. **Schema prefix must use `http`, not `https`**, with a trailing slash:
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

### Upstream tooling (OGC bblocks) and local reproduction

CI is a thin wrapper: `.github/workflows/process-bblocks.yml` calls the OGC reusable workflow `opengeospatial/bblocks-postprocess/.github/workflows/validate-and-process.yml@master` on push to `main`. It runs JSON Schema validation, JSON-LD uplift, and SHACL, then **auto-commits** `build/` + `register.json` (commits "Building blocks postprocessing" and "Generate JSON Forms schemas"). We pass `skip-pages: true` (the custom `deploy-viewer.yml` is the sole Pages deployer).

This postprocess — not the local Python tools — is the **authoritative** SHACL/uplift check. Reproduce it locally with Docker (no fork/CI needed):

```bash
# Full validate + build (writes build/, register.json)
docker run --pull=always --rm --workdir /workspace -v "$(pwd):/workspace" \
  ghcr.io/opengeospatial/bblocks-postprocess --clean true

# One block only
docker run ... ghcr.io/opengeospatial/bblocks-postprocess --clean true --filter <bblock-id>

# Preview the register in the viewer at http://localhost:9090
docker run --rm --pull=always -v "$(pwd):/register" -p 9090:9090 \
  ghcr.io/ogcincubator/bblocks-viewer
```

Per-example validation order in the postprocess: **1) JSON Schema → 2) JSON-LD uplift (JSON + `context.jsonld` → `.jsonld`/`.ttl`) → 3) SHACL.** `tools/validate_examples.py` covers only step 1; `tools/validate_shacl.py` approximates step 3 (it gathers rules from the `$ref` graph rather than the postprocessor's bundle, so confirm against the Docker run when it matters).

### OGC conventions vs. this repo

The generic OGC docs (<https://ogcincubator.github.io/bblocks-docs/all-bblocks-docs.md>) describe options we deliberately do or don't use:

| Generic OGC convention | This repo |
|---|---|
| SHACL in `shapes.ttl`, or `shaclShapes`/`shaclClosures` in `bblock.json` | **`rules.shacl`** auto-detected per dir; no `shaclShapes` field |
| `$ref: bblocks://{id}` | **relative paths** (`../cdifCore/schema.yaml`) |
| `x-jsonld-context` / `x-jsonld-prefixes` schema keywords | auto-detected **`context.jsonld`** + inline `@context` blocks (no `x-jsonld-*`) |
| SHACL inheritance via `isProfileOf` | schema **`allOf` composition** (profiles compose BBs; rules bundle by dependency) |

`bblock.json` allowed values: `status` ∈ {under-development, experimental, stable, superseded, retired, invalid, reserved, submitted}; `itemClass` ∈ {schema, datatype, path, parameter, header, cookie, response, api, model} (we use `schema`). `itemIdentifier` is auto-generated from the `_sources` path — never set it manually.

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

Generates a CDIF building-block `schema.yaml` (and, optionally, the surrounding `bblock.json` / `context.jsonld` / `rules.shacl` / `examples.yaml` skeletons) from a DDI-CDI / UCMIS class model. Used to bootstrap and refresh the `_sources/ddiProperties/ddicdi*` BBs.

**XMI format auto-detection.** `parse_xmi()` peeks at the XMI root and dispatches:
- **canonical XMI 2.5.1** (OMG namespaces, `uml:Model`, `packagedElement` / `ownedAttribute` / navigable-end association ends) → `_parse_canonical_xmi()`;
- **Enterprise Architect native XMI 1.1** (`xmi.version="1.1"`, `xmlns:UML="omg.org/UML1.3"`, `UML:Class` distinguished by `ea_stype` tagged value, top-level `UML:Generalization` / `UML:Association` with `UML:AssociationEnd` children) → `parse_ea_xmi()`.

Both parsers emit the same internal `Model` / `UmlClass` / `Property` structures, so everything downstream (def generation, inline-or-ref, multiplicity, generalization walk) is format-agnostic.

**Usage:**
```bash
# Single-class BB
python tools/uml_to_schema.py \
  --xmi C:/path/to/ddi-cdi_ea15.2026.March.xml \
  --class EnumerationDomain \
  --bb-name ddicdiEnumerationDomain \
  --out-dir _sources/ddiProperties/

# Multi-class BB (root anyOf over multiple concrete classes)
python tools/uml_to_schema.py \
  --xmi C:/path/to/ddi-cdi_ea15.2026.March.xml \
  --class DataStructure,DimensionalDataStructure,LongDataStructure,WideDataStructure \
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

**Source XMI:** DDI-CDI XMI exports live outside this repo at the user's working location. Two are in use:
- `C:/Users/smrTu/OneDrive/Documents/GithubC/CDIF/cdif-umlmodel/ddi-cdi_ea15.2026.March.xml` — Enterprise Architect native XMI 1.1 export of the 2026-03 DDI-CDI model (current source of truth).
- `C:/Users/smrTu/OneDrive/Documents/GithubC/CDIF/to-canonical-xmi/ddi-cdi_canonical-unique-names.xmi` — older canonical XMI 2.5.1 export.

Pull a fresh copy when the model updates; `uml_to_schema.py` auto-detects which format it is.

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

`process-bblocks.yml` (the "Validate and process Building Blocks" workflow) calls the OGC postprocessor reusable workflow with **`skip-pages: true`**, so the postprocessor validates, builds `build/`, and commits artifacts but does **not** deploy GitHub Pages. **`deploy-viewer.yml` is the sole Pages deployer.** (Previously both deployed Pages, which caused a ~30s window on every push where the custom pages — `bblocks-viewer.html`, the landing — 404'd, plus a cross-workflow Pages-deployment race; `skip-pages` removes both.)

`deploy-viewer.yml` builds and deploys the entire site:

1. **Runs `augment_register.py`** — injects `resolvedSchema` URLs into `build/register.json`
2. **Runs `tools/generate_custom_report.py`** — granular SHACL-severity `report.html`
3. **Generates `config.js`** — points `window.bblocksRegister` at the local register and sets `baseUrl: '/metadataBuildingBlocks/viewer/'` (the SPA router base)
4. **Generates `viewer/index.html`** — the SPA loader, loading JS/CSS assets from the CDIF-org fork `cross-domain-interoperability-framework.github.io/bblocks-viewer/`. Served at the **directory** path `/viewer/` so the Vue router base resolves to `/` (home). Carries a deep-link *restore* snippet.
5. **Generates `index.html`** — the custom landing page (two cards: JSON Schema viewer + UML model browser); copied to `404.html`, which carries a deep-link *redirect* snippet.
6. **Generates `bblocks-viewer.html`** — a redirect stub to `viewer/` so the pre-move URL still resolves.

**SPA deep links** (spa-github-pages technique): GitHub Pages serves the site `404.html` (the landing) for unknown paths, so a direct `/viewer/<route>` URL would never boot the SPA on its own. `404.html` redirects `/viewer/<route>` → `/viewer/?/<route>`; `viewer/index.html` rebuilds the route via `history.replaceState` before the app boots. Non-viewer 404s still render the landing.

**Trigger:** Runs after "Validate and process Building Blocks" completes successfully, or via `workflow_dispatch`.

**Workflow chain on push:**
```
push → "Validate and process Building Blocks" (postprocessor, skip-pages: true — no Pages deploy)
         ├──→ "Generate JSON Forms schemas" (convert + augment + commit build/)
         └──→ "Deploy custom bblocks-viewer" (sole Pages deployer: augment + report + config.js
                + viewer/index.html + index.html/404.html + bblocks-viewer.html → Pages)
```

**Custom validation report:** After augmenting the register, the workflow runs `tools/generate_custom_report.py` to replace the bblocks-postprocess `report.html` with a version that shows granular validation labels instead of binary PASS/FAIL. See [generate_custom_report.py](#generate_custom_reportpy) below for details.

**Key detail:** Both `generate-jsonforms` and `deploy-viewer` run `augment_register.py` independently. `generate-jsonforms` commits the augmented `register.json` to the repo (for future runs). `deploy-viewer` augments the checked-out copy before uploading to Pages (because it can't wait for the other workflow's commit).

**bblocks-viewer fork:** `Cross-Domain-Interoperability-Framework/bblocks-viewer` (forked from `smrgeoinfo/bblocks-viewer`, itself forked from upstream `ogcincubator/bblocks-viewer`). Its `gh-deploy.yml` builds the Vue app (`yarn build --base=https://<org>.github.io/<repo>/`) and deploys to `cross-domain-interoperability-framework.github.io/bblocks-viewer/`. The fork adds the "Resolved (JSON)" button to `JsonSchemaViewer.vue` and `resolvedSchema` to `COPY_PROPERTIES` in `bblock.service.js` — upstreamed via `ogcincubator/bblocks-viewer` PR #6.

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

## validate_shacl.py

Standalone, opt-in SHACL validation for a single building block or profile — complements `validate_examples.py` (which is JSON-Schema-only). It resolves the target by name or path, gathers the target's `rules.shacl` **plus every transitively-composed BB's** `rules.shacl` (by walking `schema.yaml` `$ref` links), expands each `example*.json` from JSON-LD to RDF (injecting the BB's `context.jsonld` when an example has no inline `@context`), and runs `pyshacl` (advanced mode, `allow_warnings=True`).

**Report-only by default (always exits 0)** so it can serve as a non-fatal "warnings" check; `--strict` exits non-zero on any `sh:Violation`. The JSON-Schema `validate_examples.py` remains the default gate.

**Usage:**
```bash
# Validate one profile's examples against its (transitively gathered) SHACL rules
python tools/validate_shacl.py CDIFDataStructureProfile

# List every result (warnings + info), not just violations
python tools/validate_shacl.py CDIFDataStructureProfile --verbose

# Fail the run on any sh:Violation
python tools/validate_shacl.py _sources/profiles/cdifProfiles/CDIFDataStructureProfile --strict
```

**CLI options:** `--verbose`/`-v` (list every result, not just violations), `--strict` (exit non-zero on violations).

**Requirements:** `pyshacl` (pulls in `rdflib`, which also provides the JSON-LD parser). Install with `pip install --user pyshacl`.

**Caveat:** it reimplements rule-bundling from the `_sources` `$ref` graph rather than the OGC `build/` bundle, so it can drift from what CI validates — verify against a CI run before treating it as authoritative.

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

## audit_cdi_property_types.py

Audits every `cdi:X` property used in `_sources/cdifProperties/*/schema.yaml` against the canonical DDI-CDI XMI. For each property, prints the XMI-declared owning class, target class, and multiplicity alongside the JSON Schema value shape allowed in each cdifProperties BB. Flags obvious mismatches (e.g. plain `type=string` where XMI says the target is a class).

Enforces the project's namespace hygiene rule: `cdi:` is reserved for properties defined in the canonical DDI-CDI XMI and used with value types compatible with the XMI definition. Anything CDIF invents, simplifies, or diverges from must use `cdif:` instead. Re-run after:
- adding a new cdifProperties BB that introduces `cdi:` keys
- updating the canonical DDI-CDI XMI
- broader schema refactors that change value shapes

**Usage:**
```bash
python tools/audit_cdi_property_types.py
```

**Output:** plain-text report on stdout, grouped by `cdi:X` property — XMI definitions on top, cdifProperties usages below, with `!! flag` lines on detected mismatches. Review manually; the mismatch heuristic is conservative (primitives vs objects, plain strings where classes are expected) and won't catch every divergence.

**Config:** the XMI path is hardcoded at the top of the script (`XMI = Path(r'C:/.../to-canonical-xmi/ddi-cdi_canonical-unique-names.xmi')`). Update if you keep the canonical XMI in a different location.

**Requirements:** Python 3.6+ with `pyyaml` (uses stdlib `xml.etree.ElementTree`).

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

Looks for sibling repos relative to this repo's parent directory. **Note:** this does NOT touch the published CDIF release profile repos (below) — it only distributes tool scripts to the usgin/dde/ecrr/geochem BB repos.

## Release profile repos & sync (downstream)

Four **published profile-spec repos** consume this one (GitHub org `Cross-Domain-Interoperability-Framework`): **core**, **discovery**, **datadescription**, **codelist**. Each holds `*StructuredSchema.json`, `*Rules.shacl`, `*ImplementationGuide.md` (+`.docx`), `*-frame.jsonld`, `examples/`, and a `FrameAndValidate.py`. The sync from this repo is **manual** (there is no automation for it):

- **StructuredSchema** ← `python tools/resolve_schema.py <Profile> --structured -o <release>/<file>StructuredSchema.json`. Profiles by name (`CDIFDiscoveryProfile`, `CDIFDataDescriptionProfile`, `CDIFCodelistProfile`); **Core via** `--file _sources/cdifProperties/cdifCore/schema.yaml`. The `-o` is required (otherwise it prints to stdout).
- **SHACL** — `coreRules.shacl` is a byte-copy of `cdifCore/rules.shacl`; the profile `*Rules.shacl` are **merged** from the ~15 composing BB `rules.shacl` (no merge script lives in those repos). Only re-sync when a `rules.shacl` actually changed.
- **Implementation guides** — hand-maintained `.md`; regenerate `.docx` with `pandoc <md> --reference-doc=<copy of prior .docx> -o <docx>`.
- **Examples** — validate with `python FrameAndValidate.py <ex> --validate --schema <S> --frame <F>` (frames the JSON-LD, array-wraps its `ARRAY_PROPERTIES`, then validates). Open-world, so unknown props pass.

Conventions that bit us (keep examples + schema consistent): `schema:contentSize` is a **string**; `cdif:fileSize`/`fileSizeUofM` are **removed**; a WebAPI action result is the **actionResult** BB (`name`/`description`/`encodingFormat`/`conformsTo`, no `contentUrl`/`contentSize`); an object-form **cdifReference** must include `dcat:Relationship` in `@type`; codelist `@context` is an **object**, `skos:notation` is a single **string** required on every `CdifCodelistConcept` (do not array-wrap it). The May/June 2026 re-sync lives on a `reviewRevision202606` branch in each repo.

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
