DDI-CDI **KeyValueStructure** describes the structure of a key-value datastore — an organized collection of key-value data. Generated from the 2026-03 DDI-CDI model (`KeyValue` package).

The root validates any of six concrete classes:

- **`cdi:KeyValueStructure`** — the structure itself: identifier, datastructure components, component positions, foreign/primary keys, semantics, specialization role, and `cdi:isDefinedBy` linking to a RepresentedVariable.
- **`cdi:KeyValueDataStore`** — an organized collection of key-value data, structured by a `KeyValueStructure`.
- **`cdi:InstanceKey`** — the key of a key-value data instance.
- **`cdi:MainKeyMember`** — a member of the main key.
- **`cdi:ContextualComponent`** — a component supplying context to a key-value record.
- **`cdi:SyntheticIdComponent`** — a synthetic-identifier component.

The BB also carries the shared structural `$defs` these classes reference (`ComponentPosition`, `ForeignKey`, `PrimaryKey`, `KeyDefinition`, `ConceptSystem`, `Unit`, `UnitType`, `Universe`, etc.).
