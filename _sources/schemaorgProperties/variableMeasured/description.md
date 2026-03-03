## Variable Measured properties

Schema.org PropertyValue for describing variables in a dataset. Used as values for schema:variableMeasured in the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.

### Defined properties

- **@type** — must include schema:PropertyValue
- **@id** — identifier for this variable
- **schema:name** — string label expected to be associated with the variable in dataset serialization
- **schema:description** — text description of the variable
- **schema:alternateName** — human intelligible names for the variable
- **schema:propertyID** — identifier or name for the property concept being quantified (string, URI reference, or DefinedTerm)
- **schema:measurementTechnique** — text description of measurement method (string, URI reference, or DefinedTerm)
- **schema:unitText** — string identifying unit of measurement
- **schema:unitCode** — HTTP URI identifying unit of measure from vocabulary (recommends QUDT)
- **schema:minValue** — minimum numeric value in dataset
- **schema:maxValue** — maximum numeric value in dataset
- **schema:url** — URL to resource useful for interpreting the variable

### Dependencies

- [definedTerm](../definedTerm/) — controlled vocabulary term for propertyID, measurementTechnique, and unitCode
