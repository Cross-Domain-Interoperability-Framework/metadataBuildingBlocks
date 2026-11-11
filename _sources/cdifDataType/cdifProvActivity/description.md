## CDIF Provenance Activity

Extended provenance activity for CDIF metadata, adding schema.org Action properties (agents, methodology, temporal bounds, action chaining) to the base prov:Activity. What the activity used is recorded with schema:instrument (instruments, software and reagents, each told apart by a Wikidata kind term in schema:additionalType) and schema:object (inputs). An activity must have at least one of schema:instrument, schema:object or schema:actionProcess. The plan it followed is the {@id} form of schema:actionProcess; an inline HowTo records the procedure as performed and links the plan with schema:isBasedOn.

### Defined properties

- **@type** — must include both schema:Action and prov:Activity
- **schema:instrument** — instruments, software and reagents used: an {@id} reference, or a description in place whose schema:additionalType carries one of Q3099911 (instrument), Q7397 (software) or Q2356542 (reagent)
- **prov:used** — not used by this profile; accepted only in the core shape (strings and @id references)
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
