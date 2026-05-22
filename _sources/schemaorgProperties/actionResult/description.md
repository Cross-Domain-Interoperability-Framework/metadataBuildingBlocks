# Action result

The result of a `schema:Action` invoked on a `schema:WebAPI` distribution. It documents
the serialization/format of the data the service returns — the encoding format(s) and any
specification the response conforms to — and is typed as `schema:DataDownload`.

Unlike a file-based `schema:DataDownload` distribution, an action result has **no**
`schema:contentUrl` or `schema:contentSize`: the response is generated per request, so its
size depends on the request rather than being a fixed property of a stored file.

Properties: `@type` (contains `schema:DataDownload`), `schema:name`, `schema:description`,
`schema:encodingFormat`, `dcterms:conformsTo`.

Profiles may extend the result. The CDIF Data Description profile, for example, adds the
per-field physical mappings (`cdif:hasPhysicalMapping`) and `cdi:characterSet` so that an
API response can be described as a physical realization of the dataset's variables, the same
way a `schema:DataDownload` distribution is.
