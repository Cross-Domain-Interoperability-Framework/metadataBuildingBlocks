## WebAPI properties

Documents a web service API endpoint using the schema.org WebAPI pattern. Specifies service type, terms of service, machine-readable documentation, and potential actions.

### Defined properties

- **@type** — must include schema:WebAPI
- **schema:serviceType** — kind of service (string, DefinedTerm, or resolvable identifier)
- **schema:termsOfService** — description of access privileges required (string or cdif:Reference)
- **schema:documentation** — machine-actionable description of the service (e.g. OpenAPI, OGC Capabilities documents)
- **schema:potentialAction** — actions that can be invoked via the API

### Dependencies

- [labeledLink](../labeledLink/) — a resolvable URL with an optional name and
  description, plus the optional DCAT relation surface (`dcat:hadRole`,
  `dcterms:relation`). Absorbed the former `cdifDataType/cdifReference` block on
  2026-09-23; the old link here pointed at `cdifProperties/`, a directory that has
  not existed for some time.
- [definedTerm](../definedTerm/) — controlled vocabulary term for service type
- [action](../action/) — action definitions for potentialAction
