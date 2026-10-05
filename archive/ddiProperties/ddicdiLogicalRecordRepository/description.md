DDI-CDI **LogicalRecordRepository** models a managed collection of logical records held together as a repository — a delimited file, fixed-record-length file, relational database, and so on. It is the successor to the DDI-CDI 1.0 `DataStore` class: the 2026-03 DDI-CDI model renamed `DataStore` to `LogicalRecordRepository` and moved it into the `FormatDescription` package.

The root `cdi:LogicalRecordRepository` carries `cdi:has_LogicalRecord` (members from the `ddicdiLogicalRecord` BB) and characterization properties `cdi:repositoryType` (renamed from `DataStore.dataStoreType`), `cdi:characterSet`, `cdi:recordCount`, `cdi:aboutMissing`, `cdi:allowsDuplicates`, `cdi:name`, `cdi:purpose`, and `cdi:isDefinedBy`.

## Changes from DDI-CDI 1.0 `DataStore`

- `DataStore` → `LogicalRecordRepository`; `dataStoreType` → `repositoryType`.
- `has_LogicalRecordPosition` is dropped — `LogicalRecordPosition` was deleted from the model.
- `has_RecordRelation` is replaced by the `LogicalRecordRelationship` `$def` — `RecordRelation` was deleted and its capability moved into `LogicalRecordRelationship`.
- `CorrespondenceDefinition` is now a canonical DDI-CDI structured datatype and lives in the `ddicdiDataTypes` BB.

## `$defs`

- **`LogicalRecordRepositoryStructure`** — describes the topology and mathematical properties (`cdi:specification` → `StructureSpecification`: reflexive / symmetric / transitive; `cdi:totality`: Partial / Total) of a repository, and the `LogicalRecordRelationship`s that compose it.
- **`LogicalRecordRelationship`** — successor to `RecordRelation`. Pairs source and target `LogicalRecord`s (`cdi:hasSource` / `cdi:hasTarget`) and carries the `InstanceVariableMap`s that define how their instance variables correspond.
- **`InstanceVariableMap`** — a key/value relationship between equivalent instance variables of two logical records. Carries a required `cdi:correspondence` (`CorrespondenceDefinition`), a required `cdi:comparison` (`ComparisonOperator`), and a required `cdi:setValue`, plus `cdi:hasSource` / `cdi:hasTarget` instance-variable references. The three required members follow the `[1..1]` multiplicities in the 2026-03 DDI-CDI model.
