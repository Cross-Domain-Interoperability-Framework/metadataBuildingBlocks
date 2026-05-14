## CDIF Data Description Metadata Profile

Profile for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) data description profile. Composes cdifCore with discovery properties and data description extensions.

### Composition

- **cdifCore** -- all required and optional core metadata properties
- **Discovery properties** -- measurement technique, variables measured, spatial/temporal coverage, quality measurements
- **Data description extensions**:
  - `schema:variableMeasured` items at this level require `cdi:InstanceVariable` typing and `cdif:physicalDataType`
  - `schema:distribution` items may include `cdi:characterSet`, `cdif:fileSize`, `cdif:fileSizeUofM`
  - `cdif:hasPrimaryKey` points at a `cdif:Key` node (via the `cdifKey` building block)
  - `cdif:statistics` carries one or more `cdi:Statistics` bundles or a `cdi:StatisticsCollection` (via the `cdifStatistics` building block)

### Conformance

Metadata conforming to this profile declares conformance to `cdif/core/1.0/`, `cdif/discovery/1.0/`, and `cdif/data_description/1.0/`.
