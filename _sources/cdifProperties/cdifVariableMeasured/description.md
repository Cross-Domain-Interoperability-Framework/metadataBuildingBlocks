## CDIF Variable Measured properties

Extends the base [variableMeasured](../../schemaorgProperties/variableMeasured/) building block with DDI-CDI InstanceVariable properties for richer variable descriptions in CDIF integration profiles.

### Defined properties

- **@type** — must include schema:PropertyValue and cdi:InstanceVariable
- **cdi:identifier** — identifier for this variable
- **cdi:physicalDataType** — physical data type concept (string, URI reference, or DefinedTerm)
- **cdi:intendedDataType** — intended data type for values (recommended: XML Schema datatypes)
- **cdi:role** — role of variable in data structure (MeasureComponent, AttributeComponent, DimensionComponent, DescriptorComponent, ReferenceValueComponent)
- **cdi:describedUnitOfMeasure** — structured unit of measure from controlled vocabulary (DefinedTerm)
- **cdi:simpleUnitOfMeasure** — simple unit of measure (string, URI reference, or DefinedTerm)
- **cdi:uses** — concepts that this variable measures or represents
- **cdi:name** — name of variable in DDI-CDI model
- **cdi:displayLabel** — human-readable label for display purposes

### Dependencies

- [variableMeasured](../../schemaorgProperties/variableMeasured/) — base variable measured properties
- [definedTerm](../../schemaorgProperties/definedTerm/) — controlled vocabulary term
