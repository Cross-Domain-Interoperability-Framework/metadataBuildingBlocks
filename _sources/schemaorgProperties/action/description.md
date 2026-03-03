## Action properties

Defines an action (operation) that can be invoked via HTTP using the schema.org Action pattern. Specifies endpoint URL template, result encoding format, and query parameter documentation.

### Defined properties

- **@type** — the type of action (schema:Action or subtypes like SearchAction, CreateAction, UpdateAction, etc.)
- **schema:name** — text label for the action
- **schema:target** — request target location and syntax (schema:EntryPoint with urlTemplate, httpMethod, contentType)
- **schema:result** — serialization scheme and encoding format for API responses (schema:DataDownload with encodingFormat)
- **schema:object** — specification of the information model for the target resource (schema:DataFeed with variableMeasured)
- **schema:query-input** — explanations of URL template parameters (array of schema:PropertyValueSpecification with valueName, valueRequired, valuePattern)

### Dependencies

- [variableMeasured](../variableMeasured/) — variable descriptions for data feed objects
