## Generic Instrument

Schema defining a generic instrument or instrument system, with optional sub-components via schema:hasPart. Based on schema.org Thing with Product typing.

### Defined properties

- **@type** — must include schema:Thing; may also include schema:Product or domain-specific types
- **@id** — identifier for the instrument
- **schema:name** — human-readable name for this instrument
- **schema:identifier** — formal identifier for this instrument
- **schema:description** — text description of this instrument
- **schema:alternateName** — alternate name, e.g. specific make/model
- **schema:additionalType** — domain-specific type URIs for this instrument
- **schema:additionalProperty** — domain-specific properties (detection limits, calibration info, etc.)
- **schema:hasPart** — sub-components of this instrument system

### Dependencies

- [identifier](../identifier/) — structured identifier pattern
- [additionalProperty](../additionalProperty/) — PropertyValue for extension properties
