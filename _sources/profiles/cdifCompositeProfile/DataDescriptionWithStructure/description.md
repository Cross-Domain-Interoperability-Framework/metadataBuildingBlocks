# CDIF Data Structure profile

The **CDIF Data Structure profile** extends the [Data Description profile](../CDIFDataDescriptionProfile/) with full DDI-CDI structural complexity. Use this profile when the catalog record must commit to *how* the data is organized — which variables play which role, what the keys are, what value domains constrain measurements — not just *which* variables are measured.

## What it adds beyond Data Description

- **Component subclasses.** [cdifDataStructureComponent](../../../cdifProperties/cdifDataStructureComponent/) defines `cdi:IdentifierComponent`, `cdi:MeasureComponent`, `cdi:AttributeComponent`, `cdi:DimensionComponent`, `cdi:VariableValueComponent`, and `cdi:VariableDescriptorComponent` as Node classes — the structural counterparts to the role values carried directly on InstanceVariables in the Data Description profile.
- **Polymorphic DataStructure root.** [cdifDataStructure](../../../cdifProperties/cdifDataStructure/) carries `cdi:DataStructure`, `cdi:DimensionalDataStructure`, `cdi:LongDataStructure`, and `cdi:WideDataStructure`, plus shared structural types (`cdi:DimensionGroup`, `cdi:ForeignKey`, `cdi:ForeignKeyComponent`, `cdif:PrimaryKey`, `cdi:PrimaryKeyComponent`).
- **Represented variables and value domains.** [cdifRepresentedVariable](../../../cdifProperties/cdifRepresentedVariable/) and [cdifValueDomain](../../../cdifProperties/cdifValueDomain/) provide the conceptual variable definitions and substantive/sentinel value domains referenced from components.
- **Descriptor variable.** [cdifDescriptorVariable](../../../cdifProperties/cdifDescriptorVariable/) defines the `cdi:DescriptorVariable` + `cdi:DescriptorValueDomain` pattern that maps descriptor-column codes to the RepresentedVariables they name (long-format datasets).
- **Distribution is structured.** Every `schema:distribution` item must carry `cdi:isStructuredBy` pointing at a Data Structure node (Data Description allows it but does not require it).
- **InstanceVariable role / qualifies redundancy forbidden.** `cdif:role` and `cdi:qualifies` on items in `schema:variableMeasured` are not allowed at this profile level — the component class type on `cdi:isStructuredBy` already encodes the role, and `AttributeComponent.cdi:qualifies` encodes the qualifies relation.
- **Summary statistics.** `cdif:statistics` (inherited from Data Description via [cdifStatistics](../../../cdifProperties/cdifStatistics/)) carries one or more `cdi:Statistics` bundles or a `cdi:StatisticsCollection` describing computed summary values for the dataset's variables.

## Distribution typing rules

How a `schema:distribution` item is typed determines what else it must carry. The two rules below are enforced at the profile level (`schema:distribution.items.allOf` with `if/then`):

| `@type` includes... | `cdif:hasPhysicalMapping` | `cdi:isStructuredBy` |
|---|---|---|
| `cdi:TabularTextDataSet` or `cdi:StructuredDataSet` | **required** | any DataStructure variant (Long / Dimensional / Wide / abstract) |
| `cdi:PhysicalDataSet` only (no subclass) | not required | must be the abstract `cdi:DataStructure` variant (or `@id`-only reference) — Long / Dimensional / Wide subclasses are forbidden because they imply a specific physical realization |

The bare-`cdi:PhysicalDataSet` case is the "structure reuse" pattern: a dataset that points at a Data Structure node (defining RepresentedVariables + components) without committing to a specific physical file layout. Use this when the same conceptual structure is shared by multiple physical realizations, or when the physical layout is documented externally.

## Conformance

This profile composes [cdifCore](../../../cdifProperties/cdifCore/) and [cdifDataDescription](../../../cdifProperties/cdifDataDescription/), so a conforming record must carry `dcterms:conformsTo` URIs for all three:

- `https://w3id.org/cdif/core/1.0`
- `https://w3id.org/cdif/data_description/1.0`
- `https://w3id.org/cdif/data_structure/1.0`

## When to use which profile

| Want to publish... | Use profile |
|---|---|
| Catalog record with `schema:variableMeasured` and roles, no structure commitment | [Data Description](../CDIFDataDescriptionProfile/) |
| Wide table with simple measures | [Data Description](../CDIFDataDescriptionProfile/) |
| Long-format data (descriptor + reference columns) | **CDIF Data Structure** |
| Dimensional / cube data | **CDIF Data Structure** |
| Anything where consumers need keys + components + value domains | **CDIF Data Structure** |
