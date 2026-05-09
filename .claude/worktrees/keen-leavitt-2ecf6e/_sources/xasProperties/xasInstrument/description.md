## XAS Instrument

Extends the [instrument](../../schemaorgProperties/instrument/) building block with the required Wikidata scientific instrument classification (`wd:Q3099911` in `schema:additionalType`). All other properties (manufacturer, model, sub-components, etc.) are inherited from the base instrument description.

### Additional constraints

- **schema:additionalType** — must include `wd:Q3099911` (Wikidata scientific instrument)

### Dependencies

- [instrument](../../schemaorgProperties/instrument/) — base instrument description (all properties inherited)
