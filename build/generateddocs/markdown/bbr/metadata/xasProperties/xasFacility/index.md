
# XAS Facility (Schema)

`cdif.bbr.metadata.xasProperties.xasFacility` *v1.0*

Schema defining properties for documenting the facility (a schema:Place typed xas:facility, e.g. a synchrotron/storage-ring facility) where X-ray absorption spectroscopy (XAS) data is acquired. Defines properties: @type, schema:additionalType, schema:identifier, schema:name, schema:additionalProperty. Uses building blocks: additionalProperty (schemaorgProperties), identifier (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Stable

## Description

## Facility properties

Defines a set of properties for describing a facility at which X-ray absorption spectroscopy (XAS) data is acquired (a `schema:Place` typed `xas:Facility`, e.g. a synchrotron or storage-ring facility). A schema.org implementation for the CDIF XAS profile.
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
    "xas": "https://w3id.org/cdif/xas/"
  },
  "@id": "ex:xasfacility_37yht",
  "@type": [
    "schema:Place"
  ],
  "schema:additionalType": [
    {
      "@id": "xas:facility"
    }
  ],
  "schema:identifier": "https://ror.org/aps",
  "schema:name": "APS",
  "schema:additionalProperty": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:facilityenergy"
        }
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
        {
          "@id": "xas:facilitycurrent"
        }
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
        {
          "@id": "xas:xraysourcetype"
        }
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
      "xas": "https://w3id.org/cdif/xas/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasFacility/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "xas": "https://w3id.org/cdif/xas/"
    }
  ],
  "@id": "ex:xasfacility_37yht",
  "@type": [
    "schema:Place"
  ],
  "schema:additionalType": [
    {
      "@id": "xas:facility"
    }
  ],
  "schema:identifier": "https://ror.org/aps",
  "schema:name": "APS",
  "schema:additionalProperty": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:facilityenergy"
        }
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
        {
          "@id": "xas:facilitycurrent"
        }
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
        {
          "@id": "xas:xraysourcetype"
        }
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
@prefix xas: <https://w3id.org/cdif/xas/> .

ex:xasfacility_37yht a schema1:Place ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Facility current" ;
            schema1:propertyID xas:facilitycurrent ;
            schema1:unitText "Amps" ;
            schema1:value "120" ],
        [ a schema1:PropertyValue ;
            schema1:name "X-ray Source" ;
            schema1:propertyID xas:xraysourcetype ;
            schema1:value "APS bending magnet" ],
        [ a schema1:PropertyValue ;
            schema1:name "Facility energy" ;
            schema1:propertyID xas:facilityenergy ;
            schema1:unitText "GeV" ;
            schema1:value "7.00" ] ;
    schema1:additionalType xas:facility ;
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
      anyOf:
      - type: string
      - type: object
        additionalProperties: false
        required:
        - '@id'
        properties:
          '@id':
            type: string
    contains:
      type: object
      additionalProperties: false
      required:
      - '@id'
      properties:
        '@id':
          const: xas:facility
    minItems: 1
    x-jsonld-id: http://schema.org/additionalType
  schema:identifier:
    anyOf:
    - type: string
    - $ref: '#/$defs/Identifier'
    x-jsonld-id: http://schema.org/identifier
  schema:name:
    type: string
    x-jsonld-id: http://schema.org/name
  schema:additionalProperty:
    type: array
    items:
      $ref: '#/$defs/AdditionalProperty'
    x-jsonld-id: http://schema.org/additionalProperty
required:
- '@type'
- schema:additionalType
- schema:name
$defs:
  AdditionalProperty:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
  Identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  xas: https://w3id.org/cdif/xas/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasFacility/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasFacility/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "xas": "https://w3id.org/cdif/xas/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasFacility/context.jsonld)

## Sources

* [CDIF-4-XAS OSCARS Project](https://doi.org/10.5281/zenodo.17421917)
* [NeXus NXsource base class](https://manual.nexusformat.org/classes/base_classes/NXsource.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/xasProperties/xasFacility`

