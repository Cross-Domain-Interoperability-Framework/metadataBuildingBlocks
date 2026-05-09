# Long Data Structure

Describes data in **long (narrow) format**, where each row represents a single observation. A descriptor column identifies which variable the row measures, and a reference column holds the actual value. This contrasts with wide format (one row per entity with each variable in its own column) and data cube format (multi-dimensional arrays).

Uses DDI-CDI `LongStructureDataSet` type. The descriptor and reference variable roles are expressed via `cdi:role` on `cdi:InstanceVariable` entries in `schema:variableMeasured`, using the values `DescriptorComponent` and `ReferenceValueComponent`.

Optional CSVW and DDI-CDI physical properties may be provided when the long data is serialized as delimited text.
