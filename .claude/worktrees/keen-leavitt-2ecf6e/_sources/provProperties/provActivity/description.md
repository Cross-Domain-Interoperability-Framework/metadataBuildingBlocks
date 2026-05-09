## PROV-O Provenance Activity

PROV-O native provenance activity for CDIF metadata. Extends the minimal [generatedBy](../generatedBy/) with W3C PROV-O vocabulary for comprehensive provenance (used, generated, wasAssociatedWith, wasInformedBy, temporal bounds, location) with schema.org fallbacks for name, description, methodology, and status. Instruments are nested in prov:used via schema:instrument sub-key.

### Defined properties

- **@type** — must include prov:Activity
- **schema:name** — human-readable name for the activity
- **schema:description** — text description of what this activity did
- **prov:generated** — entities produced by this activity
- **prov:wasAssociatedWith** — agents responsible for this activity
- **prov:wasInformedBy** — other activities that communicated information to this one
- **prov:startedAtTime** — ISO 8601 date-time when the activity started
- **prov:endedAtTime** — ISO 8601 date-time when the activity ended
- **prov:atLocation** — location where the activity occurred
- **prov:wasStartedBy** — entity that triggered the start of this activity
- **prov:wasEndedBy** — entity that triggered the end of this activity
- **schema:actionStatus** — status of this activity (Completed, Active, Potential, Failed)
- **schema:actionProcess** — methodology or protocol for this activity
- **schema:error** — error description for failed activities

### Dependencies

- [generatedBy](../generatedBy/) — base provenance activity
- [person](../../schemaorgProperties/person/) — person agent
- [organization](../../schemaorgProperties/organization/) — organization agent
- [agentInRole](../../schemaorgProperties/agentInRole/) — agent with qualified role
- [instrument](../../schemaorgProperties/instrument/) — generic instrument
- [definedTerm](../../schemaorgProperties/definedTerm/) — controlled vocabulary term
- [labeledLink](../../schemaorgProperties/labeledLink/) — link with label and description
- [spatialExtent](../../schemaorgProperties/spatialExtent/) — spatial location
