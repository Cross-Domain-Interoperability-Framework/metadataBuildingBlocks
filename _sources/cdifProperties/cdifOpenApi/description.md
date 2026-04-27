## CDIF OpenAPI WebAPI distribution

Documents a WebAPI distribution of a resource using property structure aligned with the [OpenAPI Specification](https://spec.openapis.org/oas/3.1) (OAS 3.1). Reuses CDIF schema.org-based WebAPI properties for the API-level metadata (service type, terms of service, documentation link) and adds OpenAPI-aligned Operation, Parameter, RequestBody, and Response structure under an `oas:` namespace.

This BB is an alternative to [`schemaorgProperties/webAPI`](../../schemaorgProperties/webAPI/): use it when the CDIF metadata record should inline OpenAPI-style operation parameters, request bodies, and response media-type schemas (e.g. for self-describing distributions where no external OpenAPI document is available, or where the catalog should expose enough OAS detail for client tools to invoke the API directly).

### Defined properties

- **@type** — must include `schema:WebAPI`
- **schema:name** — API title (OAS `info.title`)
- **schema:description** — API description (OAS `info.description`)
- **schema:serviceType** — kind of service (string, IRI, or `schema:DefinedTerm`); the service-type identifier is expected to identify versions and so subsumes OAS `info.version`
- **schema:termsOfService** — access privileges required to use the API; maps OAS `info.termsOfService`
- **schema:documentation** — link to a machine-actionable service description, typically the canonical OpenAPI document
- **spdx:license** — SPDX license identifier expression for the API itself, per OAS License Object. Use `schema:license` at the parent resource level for licensing of the data.
- **schema:potentialAction[]** — operations the API exposes (one per OAS path × HTTP method). Each is a `schema:Action` (or subtype) with:
  - `schema:name` — operation identifier (OAS `operationId`)
  - `schema:description` — operation description
  - `schema:target` — `schema:EntryPoint` carrying:
    - `schema:urlTemplate` — full URL template (RFC 6570) for the endpoint (OAS server URL + path)
    - `schema:httpMethod` — HTTP method (default `GET`)
    - `oas:parameters[]` — parameter definitions (OAS Parameter Object): `oas:name`, `oas:in`, `oas:description`, `oas:required`, `oas:schema`
    - `oas:requestBody` — request body for write methods (OAS Request Body Object): `schema:description`, `oas:required`, `oas:content[]`
    - `oas:response[]` — response definitions (OAS Response Object): `oas:code`, `schema:description`, `oas:content[]`

### OpenAPI mapping notes

- OAS `info.title`, `info.description` map to `schema:name`, `schema:description` at the WebAPI level.
- OAS `info.version` is folded into `schema:serviceType` when the service-type identifier captures version (e.g. `geochem-api/v2`); otherwise add a version property at the resource level.
- OAS `Server.url` is folded into each operation's `schema:urlTemplate`. Use one CDIF WebAPI distribution per server.
- OAS `paths.{path}.{method}` becomes one `schema:potentialAction` entry; the relative path is concatenated with the server URL into `schema:urlTemplate`.
- OAS `License Object` maps to `spdx:license` when an SPDX expression is available; otherwise express via `LabeledLink` or use `schema:license` at the resource level.
- OAS Responses Object is a map keyed by HTTP code; this BB represents it as an array, with each item carrying `oas:code` explicitly. `oas:code` defaults to `"200"`.
- OAS Media Type maps similarly: an array where each item carries `schema:encodingFormat` (the MIME type) instead of using the media type as a JSON key.
- For complex payload schemas (request bodies, responses), the `oas:schema` element supports a basic `oas:type`/`oas:format`/`oas:pattern`/`oas:enum` shape and an `oas:$ref` URL pointing to an external JSON Schema or XML Schema document. For tabular outputs, the referenced schema may align with `cdifVariableMeasured` InstanceVariable definitions.

### Dependencies

- [labeledLink](../../schemaorgProperties/labeledLink/) — link with label and description
- [definedTerm](../../schemaorgProperties/definedTerm/) — controlled vocabulary term for service type
