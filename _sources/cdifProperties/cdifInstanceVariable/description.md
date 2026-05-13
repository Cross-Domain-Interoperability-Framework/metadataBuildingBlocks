## CDIF Instance Variable

Profile of `cdi:InstanceVariable` / `schema:PropertyValue` for use as a member of a `schema:variableMeasured` array. Extends the base [variableMeasured](../../schemaorgProperties/variableMeasured/) and [ddi-cdif-instance-variable](../../ddiCDIFProperties/ddi-cdif-instance-variable/) building blocks with the DDI-CDI properties most commonly needed for variable description in CDIF integration profiles.

The BB accepts three shapes interchangeably:

1. a single CDIF Instance Variable node;
2. an unwrapped array of such nodes (OGC pipeline `@graph` form);
3. a full JSON-LD document with `@context` and `@graph`.

### Defined properties

- **@type** — must include `schema:PropertyValue` and `cdi:InstanceVariable`
- **cdi:identifier** — identifier for this variable
- **cdif:physicalDataType** — physical data type concept (string, URI reference, or DefinedTerm)
- **cdi:intendedDataType** — intended data type for values (recommended: XML Schema datatypes)
- **cdi:role** — role of variable in data structure (`UnitIdentifier`, `Measure`, `Attribute`, `Dimension`, `Descriptor`, `ReferenceVariable`)
- **cdi:describedUnitOfMeasure** — structured unit of measure from controlled vocabulary (DefinedTerm)
- **cdif:simpleUnitOfMeasure** — simple unit of measure (string, URI reference, or DefinedTerm)
- **cdif:uses** — concepts that this variable measures or represents
- **cdi:qualifies** — `@id` reference to another instance variable in the same dataset; required when `cdi:role` is `Attribute`
- **cdi:name** — name of variable in DDI-CDI model
- **cdi:displayLabel** — human-readable label for display purposes

### Dependencies

- [variableMeasured](../../schemaorgProperties/variableMeasured/) — base variable measured properties
- [ddi-cdif-instance-variable](../../ddiCDIFProperties/ddi-cdif-instance-variable/) — full DDI-CDI InstanceVariable shape
- [definedTerm](../../schemaorgProperties/definedTerm/) — controlled vocabulary term
