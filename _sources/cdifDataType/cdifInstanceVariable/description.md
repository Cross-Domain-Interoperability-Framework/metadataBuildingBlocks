## CDIF Instance Variable

Profile of `cdi:InstanceVariable` / `schema:PropertyValue` for use as a member of a `schema:variableMeasured` array. Composes the base [variableMeasured](../../schemaorgProperties/variableMeasured/) building block with the DDI-CDI properties of `InstanceVariable` and its `RepresentedVariable` superclass.

The BB accepts three shapes interchangeably:

1. a single CDIF Instance Variable node;
2. an unwrapped array of such nodes (OGC pipeline `@graph` form);
3. a full JSON-LD document with `@context` and `@graph`.

### Property scope

The schema carries **all `InstanceVariable`-own and `RepresentedVariable`-own properties** from the DDI-CDI class hierarchy (`ConceptualVariable → RepresentedVariable → InstanceVariable`). Properties inherited from `ConceptualVariable` and above (`descriptiveText`, `unitOfMeasureKind`, `definition`, `displayLabel`, `name`, `measures`, `takesSentinel/SubstantiveConceptsFrom`, `uses`-as-Concept, …) are **not** included — the conceptual layer is described separately.

**InstanceVariable-own:**

- **@type** — must include `cdi:InstanceVariable` (and, as a `schema:PropertyValue`, that type too)
- **cdif:physicalDataType** — physical data type concept (string, URI reference, or DefinedTerm)
- **cdif:role** — role in a data structure (`UnitIdentifier`, `Measure`, `Attribute`, `Dimension`, `Descriptor`, `ReferenceVariable`)
- **cdi:function** — immutable characteristic (geographic designator, weight, temporal designation, …)
- **cdi:platformType** — application / technical system context the variable was realized in
- **cdi:source** — provenance reference
- **cdif:isDescribedBy_StatisticsCollection** — the `StatisticsCollection` of summary / category statistics for this variable (target-suffixed: `isDescribedBy` is polymorphic in DDI-CDI)

**RepresentedVariable-own:**

- **cdi:hasIntendedDataType** — intended data type, independent of physical representation
- **cdi:describedUnitOfMeasure** — unit of measure as a controlled-vocabulary entry
- **cdif:simpleUnitOfMeasure** — unit of measure as a plain string / URI / DefinedTerm
- **cdi:takesSentinelValuesFrom** — sentinel (missing / not-applicable) value domain(s) — `cdifValueDomain`
- **cdi:takesSubstantiveValuesFrom** — substantive value domain — `cdifValueDomain`

**CDIF extensions:**

- **cdif:uses** — concepts (or, under the Data Structure profile, the `RepresentedVariable`) that this variable represents
- **cdi:qualifies** — `@id` reference to another instance variable; used when `cdif:role` is `Attribute`

### Data Structure profile constraint

When a dataset's distribution carries `cdi:isStructuredBy` (CDIF **Data Structure** profile), the `RepresentedVariable`-own properties above live on the referenced `RepresentedVariable` and are reached from the InstanceVariable via `cdif:uses` — they must **not** be duplicated on the InstanceVariable. The Data Structure profile disallows them on `schema:variableMeasured` items for that reason. In the plain **Data Description** profile (no `cdi:isStructuredBy`), they may be carried directly on the InstanceVariable.

### Dependencies

- [variableMeasured](../../schemaorgProperties/variableMeasured/) — base variable measured properties
- [cdifValueDomain](../cdifValueDomain/) — substantive / sentinel value domains
- [cdifStatistics](../cdifStatistics/) — `StatisticsCollection` target of `cdif:isDescribedBy_StatisticsCollection`
- [definedTerm](../../schemaorgProperties/definedTerm/) — controlled vocabulary term
