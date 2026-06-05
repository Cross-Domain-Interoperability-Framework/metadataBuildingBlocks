
# Action result properties (Schema)

`cdif.bbr.metadata.schemaorgProperties.actionResult` *v0.1*

Schema defining the result of a schema:Action on a schema:WebAPI distribution - the serialization/format of the data the service returns. Typed as schema:DataDownload but without contentUrl/contentSize (the response is generated per request). Defines properties: @type, schema:name, schema:description, schema:encodingFormat, dcterms:conformsTo.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Action result
description: The result of a schema:Action invoked on a schema:WebAPI distribution
  - documents the serialization/format of the data the service returns. Typed as schema:DataDownload
  but, unlike a file distribution, an action result has no contentUrl/contentSize
  because the response is generated per request (its size depends on the request).
  Profiles may extend this result; e.g. the CDIF Data Description profile adds cdif:hasPhysicalMapping
  and cdi:characterSet.
type: object
properties:
  '@type':
    type: array
    description: Type of result object. Typically schema:DataDownload, but may include
      additional types.
    items:
      type: string
    contains:
      const: schema:DataDownload
    minItems: 1
  schema:name:
    type: string
    description: text label for the result/response format.
    x-jsonld-id: http://schema.org/name
  schema:description:
    type: string
    description: description of the result/response representation.
    x-jsonld-id: http://schema.org/description
  schema:encodingFormat:
    type: array
    description: MIME type(s) of the response serialization.
    items:
      type: string
    x-jsonld-id: http://schema.org/encodingFormat
  dcterms:conformsTo:
    type: array
    description: identifier(s) for a standard or specification the response conforms
      to.
    items:
      type: object
      properties:
        '@id':
          type: string
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
x-jsonld-prefixes:
  schema: http://schema.org/
  dcterms: http://purl.org/dc/terms/
  cdif: https://w3id.org/cdif/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/actionResult/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/actionResult/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "cdif": "https://w3id.org/cdif/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/actionResult/context.jsonld)

## Sources

* [schema.org](https://schema.org/DataDownload)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/actionResult`

