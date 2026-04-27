
# CDIF OpenAPI WebAPI distribution (Schema)

`cdif.bbr.metadata.cdifProperties.cdifOpenApi` *v0.1*

Schema for documenting a WebAPI distribution of a resource using property structure aligned with the OpenAPI Specification (OAS 3.1). Reuses CDIF schema.org WebAPI properties (schema:serviceType, schema:termsOfService, schema:documentation, schema:potentialAction) and adds OpenAPI-aligned Operation, Parameter, RequestBody, and Response structure under an 'oas:' namespace. Defines properties: @type, schema:name, schema:description, schema:serviceType, schema:termsOfService, schema:documentation, spdx:license, schema:potentialAction. Uses building blocks: labeledLink (schemaorgProperties), definedTerm (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### OpenAPI-aligned WebAPI distribution example.
Example of a CDIF WebAPI distribution described with OpenAPI-aligned operation,
parameter, requestBody, and response structure under the oas namespace. Includes
a GET search operation with query parameters and multiple response media types,
and a POST create operation with a request body.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "oas": "https://spec.openapis.org/oas/3.1#",
    "spdx": "http://spdx.org/rdf/terms#",
    "ex": "https://example.org/",
    "dcterms": "http://purl.org/dc/terms/"
  },
  "@id": "ex:openApiWebAPI_001",
  "@type": ["schema:WebAPI"],
  "schema:name": "Geochemistry Data Service",
  "schema:description": "OpenAPI 3.1 service providing search and submission over a global geochemical reference database with major and trace element data from 50,000+ samples.",
  "schema:serviceType": {
    "@type": ["schema:DefinedTerm"],
    "schema:name": "Geochemistry Query API v2",
    "schema:termCode": "geochem-api/v2",
    "schema:inDefinedTermSet": "https://geochem.example.org/serviceType/"
  },
  "schema:termsOfService": {
    "@type": ["schema:CreativeWork"],
    "schema:name": "Data Portal Terms of Use",
    "schema:description": "Open access with CC-BY 4.0 attribution requirement; rate limited to 1000 requests per hour.",
    "schema:url": "https://geochem.example.org/terms-of-use"
  },
  "schema:documentation": {
    "@type": ["schema:CreativeWork"],
    "schema:name": "Geochemistry Data Service OpenAPI 3.1 specification",
    "schema:url": "https://geochem.example.org/api/v2/openapi.json"
  },
  "spdx:license": "CC-BY-4.0",
  "schema:potentialAction": [
    {
      "@id": "ex:op_searchAnalyses",
      "@type": ["schema:SearchAction"],
      "schema:name": "searchAnalyses",
      "schema:description": "Search geochemical analyses by element, bounding box, and time range; returns tabular results.",
      "schema:target": {
        "@type": ["schema:EntryPoint"],
        "schema:urlTemplate": "https://geochem.example.org/api/v2/analyses?element={element}&bbox={bbox}&start={start}&end={end}&format={format}",
        "schema:httpMethod": ["GET"],
        "oas:parameters": [
          {
            "@id": "ex:param_element",
            "oas:name": "element",
            "oas:in": "query",
            "oas:description": "Chemical element symbol(s) to query (comma-separated, e.g. Fe,Mg,Si).",
            "oas:required": true,
            "oas:schema": {
              "oas:type": "string",
              "oas:pattern": "^[A-Z][a-z]?(,[A-Z][a-z]?)*$"
            }
          },
          {
            "@id": "ex:param_bbox",
            "oas:name": "bbox",
            "oas:in": "query",
            "oas:description": "Bounding box filter as west,south,east,north in WGS84 decimal degrees.",
            "oas:required": false,
            "oas:schema": {
              "oas:type": "string",
              "oas:pattern": "^-?\\d+\\.?\\d*,-?\\d+\\.?\\d*,-?\\d+\\.?\\d*,-?\\d+\\.?\\d*$"
            }
          },
          {
            "@id": "ex:param_start",
            "oas:name": "start",
            "oas:in": "query",
            "oas:description": "Start of time interval for analyses (ISO 8601).",
            "oas:required": false,
            "oas:schema": {
              "oas:type": "string",
              "oas:format": "date-time"
            }
          },
          {
            "@id": "ex:param_end",
            "oas:name": "end",
            "oas:in": "query",
            "oas:description": "End of time interval for analyses (ISO 8601).",
            "oas:required": false,
            "oas:schema": {
              "oas:type": "string",
              "oas:format": "date-time"
            }
          },
          {
            "@id": "ex:param_format",
            "oas:name": "format",
            "oas:in": "query",
            "oas:description": "Output format for results.",
            "oas:required": false,
            "oas:schema": {
              "oas:type": "string",
              "oas:enum": ["json", "csv"]
            }
          }
        ],
        "oas:response": [
          {
            "oas:code": "200",
            "schema:description": "Tabular geochemical analysis results matching the query.",
            "oas:content": [
              {
                "schema:encodingFormat": "application/json",
                "oas:schema": {
                  "oas:type": "object",
                  "oas:$ref": "https://geochem.example.org/api/v2/schemas/analysisResult.json"
                }
              },
              {
                "schema:encodingFormat": "text/csv",
                "oas:schema": {
                  "oas:type": "string",
                  "oas:$ref": "https://geochem.example.org/api/v2/schemas/analysisResult.csv-frictionless.json"
                }
              }
            ]
          },
          {
            "oas:code": "400",
            "schema:description": "Invalid query parameter (e.g. malformed bbox).",
            "oas:content": [
              {
                "schema:encodingFormat": "application/json",
                "oas:schema": {
                  "oas:type": "object"
                }
              }
            ]
          }
        ]
      }
    },
    {
      "@id": "ex:op_submitAnalysis",
      "@type": ["schema:CreateAction"],
      "schema:name": "submitAnalysis",
      "schema:description": "Submit a new geochemical analysis record. Requires authentication.",
      "schema:target": {
        "@type": ["schema:EntryPoint"],
        "schema:urlTemplate": "https://geochem.example.org/api/v2/analyses",
        "schema:httpMethod": ["POST"],
        "oas:requestBody": {
          "schema:description": "Analysis record conforming to the analysisSubmission schema.",
          "oas:required": true,
          "oas:content": [
            {
              "schema:encodingFormat": "application/json",
              "oas:schema": {
                "oas:type": "object",
                "oas:$ref": "https://geochem.example.org/api/v2/schemas/analysisSubmission.json"
              }
            }
          ]
        },
        "oas:response": [
          {
            "oas:code": "201",
            "schema:description": "Analysis accepted; response payload contains the assigned identifier.",
            "oas:content": [
              {
                "schema:encodingFormat": "application/json",
                "oas:schema": {
                  "oas:type": "object"
                }
              }
            ]
          },
          {
            "oas:code": "401",
            "schema:description": "Authentication required.",
            "oas:content": [
              {
                "schema:encodingFormat": "application/json",
                "oas:schema": {
                  "oas:type": "object"
                }
              }
            ]
          }
        ]
      }
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "oas": "https://spec.openapis.org/oas/3.1#",
      "spdx": "http://spdx.org/rdf/terms#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifOpenApi/context.jsonld",
    {
      "schema": "http://schema.org/",
      "oas": "https://spec.openapis.org/oas/3.1#",
      "spdx": "http://spdx.org/rdf/terms#",
      "ex": "https://example.org/",
      "dcterms": "http://purl.org/dc/terms/"
    }
  ],
  "@id": "ex:openApiWebAPI_001",
  "@type": [
    "schema:WebAPI"
  ],
  "schema:name": "Geochemistry Data Service",
  "schema:description": "OpenAPI 3.1 service providing search and submission over a global geochemical reference database with major and trace element data from 50,000+ samples.",
  "schema:serviceType": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Geochemistry Query API v2",
    "schema:termCode": "geochem-api/v2",
    "schema:inDefinedTermSet": "https://geochem.example.org/serviceType/"
  },
  "schema:termsOfService": {
    "@type": [
      "schema:CreativeWork"
    ],
    "schema:name": "Data Portal Terms of Use",
    "schema:description": "Open access with CC-BY 4.0 attribution requirement; rate limited to 1000 requests per hour.",
    "schema:url": "https://geochem.example.org/terms-of-use"
  },
  "schema:documentation": {
    "@type": [
      "schema:CreativeWork"
    ],
    "schema:name": "Geochemistry Data Service OpenAPI 3.1 specification",
    "schema:url": "https://geochem.example.org/api/v2/openapi.json"
  },
  "spdx:license": "CC-BY-4.0",
  "schema:potentialAction": [
    {
      "@id": "ex:op_searchAnalyses",
      "@type": [
        "schema:SearchAction"
      ],
      "schema:name": "searchAnalyses",
      "schema:description": "Search geochemical analyses by element, bounding box, and time range; returns tabular results.",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:urlTemplate": "https://geochem.example.org/api/v2/analyses?element={element}&bbox={bbox}&start={start}&end={end}&format={format}",
        "schema:httpMethod": [
          "GET"
        ],
        "oas:parameters": [
          {
            "@id": "ex:param_element",
            "oas:name": "element",
            "oas:in": "query",
            "oas:description": "Chemical element symbol(s) to query (comma-separated, e.g. Fe,Mg,Si).",
            "oas:required": true,
            "oas:schema": {
              "oas:type": "string",
              "oas:pattern": "^[A-Z][a-z]?(,[A-Z][a-z]?)*$"
            }
          },
          {
            "@id": "ex:param_bbox",
            "oas:name": "bbox",
            "oas:in": "query",
            "oas:description": "Bounding box filter as west,south,east,north in WGS84 decimal degrees.",
            "oas:required": false,
            "oas:schema": {
              "oas:type": "string",
              "oas:pattern": "^-?\\d+\\.?\\d*,-?\\d+\\.?\\d*,-?\\d+\\.?\\d*,-?\\d+\\.?\\d*$"
            }
          },
          {
            "@id": "ex:param_start",
            "oas:name": "start",
            "oas:in": "query",
            "oas:description": "Start of time interval for analyses (ISO 8601).",
            "oas:required": false,
            "oas:schema": {
              "oas:type": "string",
              "oas:format": "date-time"
            }
          },
          {
            "@id": "ex:param_end",
            "oas:name": "end",
            "oas:in": "query",
            "oas:description": "End of time interval for analyses (ISO 8601).",
            "oas:required": false,
            "oas:schema": {
              "oas:type": "string",
              "oas:format": "date-time"
            }
          },
          {
            "@id": "ex:param_format",
            "oas:name": "format",
            "oas:in": "query",
            "oas:description": "Output format for results.",
            "oas:required": false,
            "oas:schema": {
              "oas:type": "string",
              "oas:enum": [
                "json",
                "csv"
              ]
            }
          }
        ],
        "oas:response": [
          {
            "oas:code": "200",
            "schema:description": "Tabular geochemical analysis results matching the query.",
            "oas:content": [
              {
                "schema:encodingFormat": "application/json",
                "oas:schema": {
                  "oas:type": "object",
                  "oas:$ref": "https://geochem.example.org/api/v2/schemas/analysisResult.json"
                }
              },
              {
                "schema:encodingFormat": "text/csv",
                "oas:schema": {
                  "oas:type": "string",
                  "oas:$ref": "https://geochem.example.org/api/v2/schemas/analysisResult.csv-frictionless.json"
                }
              }
            ]
          },
          {
            "oas:code": "400",
            "schema:description": "Invalid query parameter (e.g. malformed bbox).",
            "oas:content": [
              {
                "schema:encodingFormat": "application/json",
                "oas:schema": {
                  "oas:type": "object"
                }
              }
            ]
          }
        ]
      }
    },
    {
      "@id": "ex:op_submitAnalysis",
      "@type": [
        "schema:CreateAction"
      ],
      "schema:name": "submitAnalysis",
      "schema:description": "Submit a new geochemical analysis record. Requires authentication.",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:urlTemplate": "https://geochem.example.org/api/v2/analyses",
        "schema:httpMethod": [
          "POST"
        ],
        "oas:requestBody": {
          "schema:description": "Analysis record conforming to the analysisSubmission schema.",
          "oas:required": true,
          "oas:content": [
            {
              "schema:encodingFormat": "application/json",
              "oas:schema": {
                "oas:type": "object",
                "oas:$ref": "https://geochem.example.org/api/v2/schemas/analysisSubmission.json"
              }
            }
          ]
        },
        "oas:response": [
          {
            "oas:code": "201",
            "schema:description": "Analysis accepted; response payload contains the assigned identifier.",
            "oas:content": [
              {
                "schema:encodingFormat": "application/json",
                "oas:schema": {
                  "oas:type": "object"
                }
              }
            ]
          },
          {
            "oas:code": "401",
            "schema:description": "Authentication required.",
            "oas:content": [
              {
                "schema:encodingFormat": "application/json",
                "oas:schema": {
                  "oas:type": "object"
                }
              }
            ]
          }
        ]
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix ns1: <https://spec.openapis.org/oas/3.1#$> .
@prefix oas: <https://spec.openapis.org/oas/3.1#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:openApiWebAPI_001 a schema1:WebAPI ;
    schema1:description "OpenAPI 3.1 service providing search and submission over a global geochemical reference database with major and trace element data from 50,000+ samples." ;
    schema1:documentation [ a schema1:CreativeWork ;
            schema1:name "Geochemistry Data Service OpenAPI 3.1 specification" ;
            schema1:url "https://geochem.example.org/api/v2/openapi.json" ] ;
    schema1:name "Geochemistry Data Service" ;
    schema1:potentialAction ex:op_searchAnalyses,
        ex:op_submitAnalysis ;
    schema1:serviceType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://geochem.example.org/serviceType/" ;
            schema1:name "Geochemistry Query API v2" ;
            schema1:termCode "geochem-api/v2" ] ;
    schema1:termsOfService [ a schema1:CreativeWork ;
            schema1:description "Open access with CC-BY 4.0 attribution requirement; rate limited to 1000 requests per hour." ;
            schema1:name "Data Portal Terms of Use" ;
            schema1:url "https://geochem.example.org/terms-of-use" ] ;
    spdx:license "CC-BY-4.0" .

ex:op_searchAnalyses a schema1:SearchAction ;
    schema1:description "Search geochemical analyses by element, bounding box, and time range; returns tabular results." ;
    schema1:name "searchAnalyses" ;
    schema1:target [ a schema1:EntryPoint ;
            schema1:httpMethod "GET" ;
            schema1:urlTemplate "https://geochem.example.org/api/v2/analyses?element={element}&bbox={bbox}&start={start}&end={end}&format={format}" ;
            oas:parameters ex:param_bbox,
                ex:param_element,
                ex:param_end,
                ex:param_format,
                ex:param_start ;
            oas:response [ schema1:description "Invalid query parameter (e.g. malformed bbox)." ;
                    oas:code "400" ;
                    oas:content [ schema1:encodingFormat "application/json" ;
                            oas:schema [ oas:type "object" ] ] ],
                [ schema1:description "Tabular geochemical analysis results matching the query." ;
                    oas:code "200" ;
                    oas:content [ schema1:encodingFormat "application/json" ;
                            oas:schema [ ns1:ref "https://geochem.example.org/api/v2/schemas/analysisResult.json" ;
                                    oas:type "object" ] ],
                        [ schema1:encodingFormat "text/csv" ;
                            oas:schema [ ns1:ref "https://geochem.example.org/api/v2/schemas/analysisResult.csv-frictionless.json" ;
                                    oas:type "string" ] ] ] ] .

ex:op_submitAnalysis a schema1:CreateAction ;
    schema1:description "Submit a new geochemical analysis record. Requires authentication." ;
    schema1:name "submitAnalysis" ;
    schema1:target [ a schema1:EntryPoint ;
            schema1:httpMethod "POST" ;
            schema1:urlTemplate "https://geochem.example.org/api/v2/analyses" ;
            oas:requestBody [ schema1:description "Analysis record conforming to the analysisSubmission schema." ;
                    oas:content [ schema1:encodingFormat "application/json" ;
                            oas:schema [ ns1:ref "https://geochem.example.org/api/v2/schemas/analysisSubmission.json" ;
                                    oas:type "object" ] ] ;
                    oas:required true ] ;
            oas:response [ schema1:description "Analysis accepted; response payload contains the assigned identifier." ;
                    oas:code "201" ;
                    oas:content [ schema1:encodingFormat "application/json" ;
                            oas:schema [ oas:type "object" ] ] ],
                [ schema1:description "Authentication required." ;
                    oas:code "401" ;
                    oas:content [ schema1:encodingFormat "application/json" ;
                            oas:schema [ oas:type "object" ] ] ] ] .

ex:param_bbox oas:description "Bounding box filter as west,south,east,north in WGS84 decimal degrees." ;
    oas:in "query" ;
    oas:name "bbox" ;
    oas:required false ;
    oas:schema [ oas:pattern "^-?\\d+\\.?\\d*,-?\\d+\\.?\\d*,-?\\d+\\.?\\d*,-?\\d+\\.?\\d*$" ;
            oas:type "string" ] .

ex:param_element oas:description "Chemical element symbol(s) to query (comma-separated, e.g. Fe,Mg,Si)." ;
    oas:in "query" ;
    oas:name "element" ;
    oas:required true ;
    oas:schema [ oas:pattern "^[A-Z][a-z]?(,[A-Z][a-z]?)*$" ;
            oas:type "string" ] .

ex:param_end oas:description "End of time interval for analyses (ISO 8601)." ;
    oas:in "query" ;
    oas:name "end" ;
    oas:required false ;
    oas:schema [ oas:format "date-time" ;
            oas:type "string" ] .

ex:param_format oas:description "Output format for results." ;
    oas:in "query" ;
    oas:name "format" ;
    oas:required false ;
    oas:schema [ oas:enum "csv",
                "json" ;
            oas:type "string" ] .

ex:param_start oas:description "Start of time interval for analyses (ISO 8601)." ;
    oas:in "query" ;
    oas:name "start" ;
    oas:required false ;
    oas:schema [ oas:format "date-time" ;
            oas:type "string" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF OpenAPI-aligned WebAPI distribution
description: Documents a WebAPI distribution of a resource using property structure
  aligned with OpenAPI Specification 3.1. Reuses CDIF schema.org-based WebAPI metadata
  (serviceType, termsOfService, documentation) and adds OpenAPI-aligned Operation,
  Parameter, RequestBody, and Response structure under an oas namespace. Use as an
  alternative to schemaorgProperties/webAPI when the metadata record should inline
  OpenAPI-style operation, parameter, and response detail.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: schema:WebAPI
    minItems: 1
  schema:name:
    type: string
    description: title of the API. Maps OpenAPI info.title.
  schema:description:
    type: string
    description: description of the API. Maps OpenAPI info.description. May use CommonMark.
  schema:serviceType:
    description: identifier for the kind of service, expected to identify the service
      type and version. For interoperability, ideally a resolvable identifier; otherwise
      a string from a vocabulary shared between provider and consumer. Subsumes OpenAPI
      info.version when the service-type identifier includes versioning.
    anyOf:
    - type: string
    - $ref: '#/$defs/DefinedTerm'
  schema:termsOfService:
    description: Description of access privileges required to use the API (e.g. registration,
      licensing, payments). Maps OpenAPI info.termsOfService. Note that access constraints
      applying to all distributions of the resource should be specified at the resource
      level.
    oneOf:
    - type: string
    - $ref: '#/$defs/LabeledLink'
  schema:documentation:
    description: a document that provides a machine-actionable description of this
      service instance, typically the canonical OpenAPI document. Even when this BB
      inlines OAS detail, schema:documentation may still link to an authoritative
      OAS source.
    oneOf:
    - type: string
    - $ref: '#/$defs/LabeledLink'
  spdx:license:
    description: SPDX license identifier expression for the API itself, per OpenAPI
      License Object. Use schema:license at the resource (parent) level for licensing
      of the data. If only a URL identifier is available rather than an SPDX id, encode
      as a LabeledLink.
    oneOf:
    - type: string
    - $ref: '#/$defs/LabeledLink'
  schema:potentialAction:
    type: array
    description: operations exposed by the API. Each entry corresponds to an OpenAPI
      Operation Object (one path + HTTP method).
    minItems: 1
    items:
      $ref: '#/$defs/Operation'
required:
- '@type'
- schema:serviceType
- schema:termsOfService
- schema:potentialAction
$defs:
  Operation:
    type: object
    description: an OpenAPI-aligned operation. Corresponds to one OpenAPI Operation
      Object; the path component of OAS Path Item is folded into schema:target/schema:urlTemplate
      together with the server URL.
    properties:
      '@id':
        type: string
      '@type':
        type: array
        items:
          type: string
        contains:
          enum:
          - schema:Action
          - schema:AssessAction
          - schema:ConsumeAction
          - schema:ControlAction
          - schema:CreateAction
          - schema:DeleteAction
          - schema:FindAction
          - schema:InteractAction
          - schema:MoveAction
          - schema:PlayAction
          - schema:SearchAction
          - schema:TransferAction
          - schema:UpdateAction
        minItems: 1
        default:
        - schema:Action
      schema:name:
        type: string
        description: identifier for the operation. Maps OpenAPI operationId.
      schema:description:
        type: string
        description: description of the operation. Maps OpenAPI Operation.description.
      schema:target:
        $ref: '#/$defs/EntryPoint'
    required:
    - schema:name
    - schema:target
  EntryPoint:
    type: object
    description: endpoint URL template, HTTP method, and the OpenAPI-shaped parameters,
      request body, and responses for the operation.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:EntryPoint
        minItems: 1
        default:
        - schema:EntryPoint
      schema:urlTemplate:
        type: string
        description: full URL template (RFC 6570) for invoking the operation; concatenation
          of the OpenAPI server URL and the path. Parameters are enclosed in curly
          braces {..} and MUST be documented in oas:parameters.
      schema:httpMethod:
        type: array
        description: HTTP method for the operation. Default GET.
        items:
          type: string
          enum:
          - GET
          - PUT
          - POST
          - PATCH
          - DELETE
          - HEAD
          - OPTIONS
          - TRACE
          - QUERY
        default:
        - GET
      oas:parameters:
        type: array
        description: query, path, header, or cookie parameters accepted by the operation.
          Maps OpenAPI Parameter Object.
        items:
          $ref: '#/$defs/Parameter'
      oas:requestBody:
        description: request body for the operation (typically POST/PUT/PATCH). Maps
          OpenAPI Request Body Object.
        $ref: '#/$defs/RequestBody'
      oas:response:
        type: array
        description: possible responses returned by the operation. Maps OpenAPI Responses
          Object; each item carries an explicit oas:code rather than using the HTTP
          code as a map key.
        minItems: 1
        items:
          $ref: '#/$defs/Response'
    required:
    - schema:urlTemplate
    - oas:response
  Parameter:
    type: object
    description: an OpenAPI Parameter Object; describes a single parameter of an operation.
    properties:
      '@id':
        type: string
      oas:name:
        type: string
        description: name of the parameter (case-sensitive). For path parameters,
          MUST match a {template} expression in schema:urlTemplate.
      oas:in:
        type: string
        enum:
        - query
        - querystring
        - path
        - header
        - cookie
        description: location of the parameter.
      oas:description:
        type: string
        description: description of the parameter, including serialization or semantic
          notes.
      oas:required:
        type: boolean
        default: false
        description: whether the parameter is mandatory. MUST be true if oas:in is
          "path".
      oas:schema:
        description: schema describing the parameter value type, format, and any pattern.
        $ref: '#/$defs/Schema'
    required:
    - oas:name
    - oas:in
  RequestBody:
    type: object
    description: an OpenAPI Request Body Object; describes the body of a write request.
    properties:
      schema:description:
        type: string
      oas:required:
        type: boolean
        default: false
      oas:content:
        type: array
        description: representations the request body may take. Maps OpenAPI Request
          Body content map; each item carries its own schema:encodingFormat instead
          of using media type as a map key.
        minItems: 1
        items:
          $ref: '#/$defs/MediaType'
    required:
    - oas:content
  Response:
    type: object
    description: an OpenAPI Response Object describing one response from an operation.
    properties:
      oas:code:
        type: string
        description: HTTP status code (e.g. "200", "404", "303") this response describes.
          Default "200".
        default: '200'
      schema:description:
        type: string
        description: description of the response.
      oas:content:
        type: array
        description: representations the response payload may take. Maps OpenAPI Response
          content map; each item carries its own schema:encodingFormat instead of
          using media type as a map key.
        minItems: 1
        items:
          $ref: '#/$defs/MediaType'
    required:
    - schema:description
    - oas:content
  MediaType:
    type: object
    description: an OpenAPI Media Type Object; describes the structure of one media-type
      representation in a request body or response.
    properties:
      schema:encodingFormat:
        type: string
        description: registered MIME type for this representation (e.g. application/json,
          text/csv). Replaces OpenAPI's media-type map key.
      oas:schema:
        description: schema describing the structure of the payload. May reference
          an external JSON Schema or XML Schema document via oas:$ref. For tabular
          outputs, the referenced schema may align with InstanceVariable definitions
          in cdifVariableMeasured.
        $ref: '#/$defs/Schema'
    required:
    - schema:encodingFormat
  Schema:
    type: object
    description: a minimal OpenAPI Schema Object. The full OAS Schema Object is a
      superset of JSON Schema 2020-12; this BB requires only a basic type/format/pattern/enum/$ref
      shape sufficient to describe parameter and response payload types in CDIF metadata.
      For richer schemas, use oas:$ref to point at an external schema document.
    properties:
      oas:type:
        type: string
        enum:
        - string
        - number
        - integer
        - boolean
        - array
        - object
        default: string
      oas:format:
        type: string
        description: optional format hint (e.g. "int32", "date-time", "uri", "decimal").
      oas:pattern:
        type: string
        description: regular expression the value must match (string types).
      oas:enum:
        type: array
        description: enumeration of permitted values.
        items: {}
      oas:$ref:
        type: string
        format: uri
        description: reference to an external JSON Schema or XML Schema document describing
          a complex payload structure.
  LabeledLink:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  oas: https://spec.openapis.org/oas/3.1#
  spdx: http://spdx.org/rdf/terms#
  dcterms: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifOpenApi/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifOpenApi/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "oas": "https://spec.openapis.org/oas/3.1#",
    "spdx": "http://spdx.org/rdf/terms#",
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifOpenApi/context.jsonld)

## Sources

* [OpenAPI Specification 3.1 schema](https://spec.openapis.org/oas/3.0/schema/2024-10-18.html)
* [schema.org WebAPI](https://schema.org/WebAPI)
* [schema.org Action discussion](https://schema.org/docs/actions.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifOpenApi`

