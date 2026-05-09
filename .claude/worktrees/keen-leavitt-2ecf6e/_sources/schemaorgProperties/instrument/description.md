## Instrument Description

Schema for describing laboratory instruments and instrument systems. Combines instrument identity, ownership, manufacturer/model, commissioning lifecycle, hierarchical sub-components, and domain-specific properties.

### Defined properties

- **@context** - JSON-LD context (requires schema prefix)
- **@id** - persistent identifier URI for this instrument record
- **@type** - must include schema:Product and schema:Thing
- **schema:additionalType** - domain-specific type classifications (e.g. wd:Q3099911 for scientific instrument)
- **schema:name** - human-readable name (min 3 characters)
- **schema:description** - text description of purpose and capabilities
- **schema:alternateName** - alternate names (make/model, abbreviation)
- **schema:identifier** - formal identifiers (PIDINST, serial number, inventory number)
- **schema:url** - landing page URL
- **schema:manufacturer** - organization that manufactured the instrument
- **schema:model** - product model (name, identifier)
- **schema:category** - instrument type from controlled vocabulary
- **schema:owner** - organization that owns the instrument
- **schema:contributor** - agents in roles (operator, custodian, PI — use schema:owner for ownership)
- **schema:additionalProperty** - instrument-specific properties (measured variables, detection limits, calibration, etc.)
- **schema:validFrom** / **schema:validThrough** - commissioned/decommissioned dates
- **schema:hasPart** - sub-components of the instrument system
- **schema:relatedLink** - links to manuals, datasheets, calibration records
- **schema:subjectOf** - catalog record metadata

### Dependencies

- [identifier](../identifier/) - structured identifier pattern
- [organization](../organization/) - organization schema
- [person](../person/) - person schema
- [definedTerm](../definedTerm/) - controlled vocabulary term
- [agentInRole](../agentInRole/) - agent with qualified role
- [additionalProperty](../additionalProperty/) - PropertyValue for extension properties
- [labeledLink](../labeledLink/) - typed link to related resource
