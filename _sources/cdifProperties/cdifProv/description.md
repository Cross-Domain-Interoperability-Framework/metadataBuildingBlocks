## CDIF Provenance Activity

Extended provenance activity for CDIF metadata, adding schema.org Action properties (agents, methodology, temporal bounds, action chaining) to the base prov:Activity. Instruments are nested within prov:used items via schema:instrument sub-key.

### Defined properties

- **@type** — must include both schema:Action and prov:Activity
- **prov:used** — items used by the activity; can include instruments via schema:instrument sub-key
- **schema:name** — human-readable name for the activity
- **schema:description** — text description of what this activity did
- **schema:identifier** — formal identifier for this activity
- **schema:agent** — primary responsible agent for this activity
- **schema:participant** — other participants in this activity
- **schema:object** — input entity for this activity (for action chaining)
- **schema:result** — output entity produced by this activity (for action chaining)
- **schema:actionStatus** — status of this activity
- **schema:startTime** — ISO 8601 date-time when the activity started
- **schema:endTime** — ISO 8601 date-time when the activity ended
- **schema:location** — where the activity occurred
- **schema:actionProcess** — methodology or protocol for this activity
- **schema:error** — error description for failed activities
- **schema:additionalProperty** — domain-specific extension properties

### Dependencies

- [generatedBy](../../provProperties/generatedBy/) — base provenance activity
- [person](../../schemaorgProperties/person/) — person agent
- [organization](../../schemaorgProperties/organization/) — organization agent
- [agentInRole](../../schemaorgProperties/agentInRole/) — agent with qualified role
- [identifier](../../schemaorgProperties/identifier/) — structured identifier
- [instrument](../../schemaorgProperties/instrument/) — generic instrument
- [definedTerm](../../schemaorgProperties/definedTerm/) — controlled vocabulary term
- [labeledLink](../../schemaorgProperties/labeledLink/) — link with label and description
- [spatialExtent](../../schemaorgProperties/spatialExtent/) — spatial location
- [additionalProperty](../../schemaorgProperties/additionalProperty/) — PropertyValue for extension properties
