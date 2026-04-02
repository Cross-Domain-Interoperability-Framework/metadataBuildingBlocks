
# WebAPI properties (Schema)

`cdif.bbr.metadata.xasProperties.xasFacility` *v0.1*

Schema defining properties for documenting a WebAPI used as a resource distribution option. Defines properties: @id, @type, schema:additionalType, schema:identifier, schema:name, schema:additionalProperty. Uses building blocks: additionalProperty (schemaorgProperties), identifier (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Facility properties

Defines a set of properties for use describing a Faciliy at wich X-ray absorption (XAS) data is acquired. A schema.org implementation for the CDIF XAS profile
## Examples

### Example X-ray absorption facility
Example documentation for x-ray absorption facility, based on schema.org Place
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "xas": "https://xas.org/dictionary/"
  },
  "@id": "ex:xasfacility_37yht",
  "@type": [
    "schema:Place"
  ],
  "schema:additionalType": [
    "xas:Facility"
  ],
  "schema:identifier": "https://ror.org/aps",
  "schema:name": "APS",
  "schema:additionalProperty": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "xas:energy"
      ],
      "schema:name": "Facility energy",
      "schema:value": "7.00",
      "schema:unitText": "GeV"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "xas:current"
      ],
      "schema:name": "Facility current",
      "schema:value": "120",
      "schema:unitText": "Amps"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "xas:xray_source"
      ],
      "schema:name": "X-ray Source",
      "schema:value": "APS bending magnet"
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
      "xas": "https://xas.org/dictionary/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasFacility/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "xas": "https://xas.org/dictionary/"
    }
  ],
  "@id": "ex:xasfacility_37yht",
  "@type": [
    "schema:Place"
  ],
  "schema:additionalType": [
    "xas:Facility"
  ],
  "schema:identifier": "https://ror.org/aps",
  "schema:name": "APS",
  "schema:additionalProperty": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "xas:energy"
      ],
      "schema:name": "Facility energy",
      "schema:value": "7.00",
      "schema:unitText": "GeV"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "xas:current"
      ],
      "schema:name": "Facility current",
      "schema:value": "120",
      "schema:unitText": "Amps"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "xas:xray_source"
      ],
      "schema:name": "X-ray Source",
      "schema:value": "APS bending magnet"
    }
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:xasfacility_37yht a schema1:Place ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "X-ray Source" ;
            schema1:propertyID "xas:xray_source" ;
            schema1:value "APS bending magnet" ],
        [ a schema1:PropertyValue ;
            schema1:name "Facility energy" ;
            schema1:propertyID "xas:energy" ;
            schema1:unitText "GeV" ;
            schema1:value "7.00" ],
        [ a schema1:PropertyValue ;
            schema1:name "Facility current" ;
            schema1:propertyID "xas:current" ;
            schema1:unitText "Amps" ;
            schema1:value "120" ] ;
    schema1:additionalType "xas:Facility" ;
    schema1:identifier "https://ror.org/aps" ;
    schema1:name "APS" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: definitions a Facility location, type schema:Place
type: object
properties:
  '@id':
    type: string
  '@type':
    type: array
    items:
      type: string
    contains:
      const: schema:Place
    minItems: 1
  schema:additionalType:
    type: array
    items:
      type: string
    contains:
      const: xas:Facility
    minItems: 1
  schema:identifier:
    anyOf:
    - type: string
    - $ref: '#/$defs/Identifier'
  schema:name:
    type: string
  schema:additionalProperty:
    type: array
    items:
      $ref: '#/$defs/AdditionalProperty'
required:
- '@type'
- schema:additionalType
- schema:name
$defs:
  AdditionalProperty:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
  Identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
x-jsonld-extra-terms:
  schema: http://schema.org
x-jsonld-prefixes:
  xas: https://xas.org/dictionary/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasFacility/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasFacility/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasFacility/context.jsonld)

## Sources

* [schema.org](https://schema.org/Action)
* [schema.org issue 62](https://github.com/schemaorg/suggestions-questions-brainstorming/issues/62)
* [schema.org discussion on Action](https://schema.org/docs/actions.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/xasProperties/xasFacility`

