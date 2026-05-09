## CDIF Data Description Metadata Profile

Profile for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) data description profile. Composes cdifCore with discovery properties and data description extensions.

### Composition

- **cdifCore** -- all required and optional core metadata properties
- **Discovery properties** -- measurement technique, variables measured, spatial/temporal coverage, quality measurements
- **Data description extensions**:
  - `schema:variableMeasured` items at this level require `cdi:InstanceVariable` typing and `cdi:physicalDataType`
  - `schema:distribution` items may include `cdi:characterSet`, `cdi:fileSize`, `cdi:fileSizeUofM`

### Conformance

Metadata conforming to this profile declares conformance to `cdif/core/1.0/`, `cdif/discovery/1.0/`, and `cdif/data_description/1.0/`.
