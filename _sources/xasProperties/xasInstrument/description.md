## XAS Instrument properties

XAS-specific instrument definition requiring schema:Product + schema:Thing typing and Wikidata scientific instrument additionalType (wd:Q3099911). Supports hierarchical sub-components via schema:hasPart for beamline elements (source, monochromator, detector).

### Defined properties

- **@type** — must include both schema:Product and schema:Thing
- **schema:additionalType** — must include wd:Q3099911 (scientific instrument)
- **schema:name** — name of the instrument
- **schema:identifier** — identifier for the instrument (string or Identifier object)
- **schema:description** — description of the instrument
- **schema:additionalProperty** — domain-specific properties (varies by instrument type)
- **schema:hasPart** — sub-components of the instrument system

### Dependencies

- [identifier](../../schemaorgProperties/identifier/) — structured identifier pattern
- [additionalProperty](../../schemaorgProperties/additionalProperty/) — PropertyValue for extension properties
- [instrument](../../schemaorgProperties/instrument/) — base generic instrument schema
