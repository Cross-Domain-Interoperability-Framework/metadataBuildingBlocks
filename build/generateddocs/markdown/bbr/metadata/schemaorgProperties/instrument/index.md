
# Instrument (Schema)

`cdif.bbr.metadata.schemaorgProperties.instrument` *v0.1*

Schema defining a generic instrument or instrument system, with optional sub-components via schema:hasPart. Based on schema.org Thing with Product typing. Defines properties: @type, @id, schema:name, schema:identifier, schema:description, schema:alternateName, schema:additionalType, schema:additionalProperty, schema:hasPart. Uses building blocks: identifier (schemaorgProperties), additionalProperty (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Generic Instrument

Schema defining a generic instrument or instrument system, with optional sub-components via schema:hasPart. Based on schema.org Thing with Product typing.

### Defined properties

- **@type** — must include schema:Thing; may also include schema:Product or domain-specific types
- **@id** — identifier for the instrument
- **schema:name** — human-readable name for this instrument
- **schema:identifier** — formal identifier for this instrument
- **schema:description** — text description of this instrument
- **schema:alternateName** — alternate name, e.g. specific make/model
- **schema:additionalType** — domain-specific type URIs for this instrument
- **schema:additionalProperty** — domain-specific properties (detection limits, calibration info, etc.)
- **schema:hasPart** — sub-components of this instrument system

### Dependencies

- [identifier](../identifier/) — structured identifier pattern
- [additionalProperty](../additionalProperty/) — PropertyValue for extension properties

## Examples

### Example generic instrument with sub-components.
ICP-MS analytical system demonstrating the generic instrument building block
with schema:hasPart sub-components (autosampler, spray chamber). Uses
schema:Thing + schema:Product typing, schema:alternateName for specific
make/model, and schema:additionalProperty for detection limits.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/"
    },
    "@id": "ex:instrument-icpms-system",
    "@type": ["schema:Thing", "schema:Product"],
    "schema:name": "ICP-MS Analytical System",
    "schema:alternateName": "Thermo Fisher iCAP RQ ICP-MS with autosampler",
    "schema:description": "Inductively Coupled Plasma Mass Spectrometry system for trace element analysis of geological samples.",
    "schema:additionalProperty": [
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": ["detectionLimit"],
            "schema:name": "Typical Detection Limit",
            "schema:value": "0.01 mg/kg for trace elements"
        }
    ],
    "schema:hasPart": [
        {
            "@type": ["schema:Thing", "schema:Product"],
            "schema:name": "ESI SC-4DX autosampler",
            "schema:description": "Automated sample introduction system with 240-position tray"
        },
        {
            "@type": ["schema:Thing", "schema:Product"],
            "schema:name": "PFA spray chamber",
            "schema:description": "Perfluoroalkoxy spray chamber for sample aerosol generation"
        }
    ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:instrument-icpms-system",
  "@type": [
    "schema:Thing",
    "schema:Product"
  ],
  "schema:name": "ICP-MS Analytical System",
  "schema:alternateName": "Thermo Fisher iCAP RQ ICP-MS with autosampler",
  "schema:description": "Inductively Coupled Plasma Mass Spectrometry system for trace element analysis of geological samples.",
  "schema:additionalProperty": [
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "detectionLimit"
      ],
      "schema:name": "Typical Detection Limit",
      "schema:value": "0.01 mg/kg for trace elements"
    }
  ],
  "schema:hasPart": [
    {
      "@type": [
        "schema:Thing",
        "schema:Product"
      ],
      "schema:name": "ESI SC-4DX autosampler",
      "schema:description": "Automated sample introduction system with 240-position tray"
    },
    {
      "@type": [
        "schema:Thing",
        "schema:Product"
      ],
      "schema:name": "PFA spray chamber",
      "schema:description": "Perfluoroalkoxy spray chamber for sample aerosol generation"
    }
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:instrument-icpms-system a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Typical Detection Limit" ;
            schema1:propertyID "detectionLimit" ;
            schema1:value "0.01 mg/kg for trace elements" ] ;
    schema1:alternateName "Thermo Fisher iCAP RQ ICP-MS with autosampler" ;
    schema1:description "Inductively Coupled Plasma Mass Spectrometry system for trace element analysis of geological samples." ;
    schema1:hasPart [ a schema1:Product,
                schema1:Thing ;
            schema1:description "Automated sample introduction system with 240-position tray" ;
            schema1:name "ESI SC-4DX autosampler" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:description "Perfluoroalkoxy spray chamber for sample aerosol generation" ;
            schema1:name "PFA spray chamber" ] ;
    schema1:name "ICP-MS Analytical System" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Generic Instrument
description: A generic instrument or instrument system. Uses schema:Thing as base
  type with optional schema:Product typing. Supports hierarchical instrument systems
  via schema:hasPart for sub-components.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    minItems: 1
    contains:
      const: schema:Thing
    description: Must include schema:Thing. May also include schema:Product or domain-specific
      types.
  '@id':
    type: string
  schema:name:
    type: string
    description: Human-readable name for this instrument
  schema:identifier:
    description: Formal identifier for this instrument
    anyOf:
    - type: string
    - $ref: '#/$defs/Identifier'
  schema:description:
    type: string
    description: Text description of this instrument
  schema:alternateName:
    type: string
    description: Alternate name, e.g. specific make/model
  schema:additionalType:
    description: Domain-specific type URIs for this instrument
    anyOf:
    - type: string
    - type: array
      items:
        type: string
  schema:additionalProperty:
    type: array
    description: Domain-specific properties (detection limits, calibration info, etc.)
    items:
      $ref: '#/$defs/AdditionalProperty'
  schema:hasPart:
    type: array
    description: Sub-components of this instrument system. Use @id references or inline
      instrument objects.
    items:
      anyOf:
      - $ref: '#/$defs/InstrumentRef'
      - type: object
        properties:
          '@id':
            type: string
            description: reference to a sub-component defined elsewhere
required:
- schema:name
allOf:
- required:
  - '@type'
$defs:
  Identifier:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
  AdditionalProperty:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
  InstrumentRef:
    type: object
    description: Inline sub-component instrument (non-recursive single level)
    properties:
      '@type':
        type: array
        items:
          type: string
        minItems: 1
        contains:
          const: schema:Thing
      '@id':
        type: string
      schema:name:
        type: string
      schema:identifier:
        anyOf:
        - type: string
        - $ref: '#/$defs/Identifier'
      schema:description:
        type: string
      schema:alternateName:
        type: string
      schema:additionalType:
        anyOf:
        - type: string
        - type: array
          items:
            type: string
      schema:additionalProperty:
        type: array
        items:
          $ref: '#/$defs/AdditionalProperty'
    required:
    - schema:name
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/context.jsonld)

## Sources

* [schema.org Thing](https://schema.org/Thing)
* [schema.org instrument property](https://schema.org/instrument)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/instrument`

