## WebAPI properties

Documents a web service API endpoint using the schema.org WebAPI pattern. Specifies service type, terms of service, machine-readable documentation, and potential actions.

### Defined properties

- **@type** — must include schema:WebAPI
- **schema:serviceType** — kind of service (string, DefinedTerm, or resolvable identifier)
- **schema:termsOfService** — description of access privileges required (string or LabeledLink)
- **schema:documentation** — machine-actionable description of the service (e.g. OpenAPI, OGC Capabilities documents)
- **schema:potentialAction** — actions that can be invoked via the API

### Dependencies

- [labeledLink](../labeledLink/) — link with label and description
- [definedTerm](../definedTerm/) — controlled vocabulary term for service type
- [action](../action/) — action definitions for potentialAction
