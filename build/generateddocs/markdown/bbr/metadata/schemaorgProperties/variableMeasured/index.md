
# VariableMeasured (Schema)

`cdif.bbr.metadata.schemaorgProperties.variableMeasured` *v0.1*

Schema defining propertis for schema.org varialbleMeasured as defined for CDIF discovery. Implemented as schema.org/PropertyValue. Defines properties: @type, @id, schema:name, schema:description, schema:alternateName, schema:propertyID, schema:measurementTechnique, schema:unitText, schema:unitCode, schema:minValue, schema:maxValue, schema:url. Uses building blocks: definedTerm (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Variable Measured properties

Schema.org PropertyValue for describing variables in a dataset. Used as values for schema:variableMeasured in the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.

### Defined properties

- **@type** — must include schema:PropertyValue
- **@id** — identifier for this variable
- **schema:name** — string label expected to be associated with the variable in dataset serialization
- **schema:description** — text description of the variable
- **schema:alternateName** — human intelligible names for the variable
- **schema:propertyID** — identifier or name for the property concept being quantified (string, URI reference, or DefinedTerm)
- **schema:measurementTechnique** — text description of measurement method (string, URI reference, or DefinedTerm)
- **schema:unitText** — string identifying unit of measurement
- **schema:unitCode** — HTTP URI identifying unit of measure from vocabulary (recommends QUDT)
- **schema:minValue** — minimum numeric value in dataset
- **schema:maxValue** — maximum numeric value in dataset
- **schema:url** — URL to resource useful for interpreting the variable

### Dependencies

- [definedTerm](../definedTerm/) — controlled vocabulary term for propertyID, measurementTechnique, and unitCode

## Examples

### Variable Measured.
Implementation of Schema.org PropertyValue as value for variableMeasured property.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@type": ["schema:PropertyValue"],
    "@id": "ex:variableMeasured_346",
    "schema:name": "example variable measured",
    "schema:description": "Air temperature measured at 2 meters above ground level",
    "schema:propertyID": [
        {
            "@id": "ex:definedTerm_zZc",
            "@type": "schema:DefinedTerm",
            "schema:name": "Temperature",
            "schema:identifier": {
                "@id": "ex:tempTerm_246u",
                "@type": "schema:PropertyValue",
                "schema:propertyID": "https://qudt.org/vocab/quantitykind/Temperature",
                "schema:url": "https://qudt.org/vocab/quantitykind/Temperature"
            },
            "schema:inDefinedTermSet": "http://ogc.org/defs",
            "schema:termCode": "T"
        }
    ],
    "schema:measurementTechnique": "thermometer",
    "schema:unitText": "deg C",
    "schema:unitCode": "C",
    "schema:minValue": 0,
    "schema:maxValue": 200
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@type": [
    "schema:PropertyValue"
  ],
  "@id": "ex:variableMeasured_346",
  "schema:name": "example variable measured",
  "schema:description": "Air temperature measured at 2 meters above ground level",
  "schema:propertyID": [
    {
      "@id": "ex:definedTerm_zZc",
      "@type": "schema:DefinedTerm",
      "schema:name": "Temperature",
      "schema:identifier": {
        "@id": "ex:tempTerm_246u",
        "@type": "schema:PropertyValue",
        "schema:propertyID": "https://qudt.org/vocab/quantitykind/Temperature",
        "schema:url": "https://qudt.org/vocab/quantitykind/Temperature"
      },
      "schema:inDefinedTermSet": "http://ogc.org/defs",
      "schema:termCode": "T"
    }
  ],
  "schema:measurementTechnique": "thermometer",
  "schema:unitText": "deg C",
  "schema:unitCode": "C",
  "schema:minValue": 0,
  "schema:maxValue": 200
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:variableMeasured_346 a schema1:PropertyValue ;
    schema1:description "Air temperature measured at 2 meters above ground level" ;
    schema1:maxValue 200 ;
    schema1:measurementTechnique "thermometer" ;
    schema1:minValue 0 ;
    schema1:name "example variable measured" ;
    schema1:propertyID ex:definedTerm_zZc ;
    schema1:unitCode "C" ;
    schema1:unitText "deg C" .

ex:definedTerm_zZc a schema1:DefinedTerm ;
    schema1:identifier ex:tempTerm_246u ;
    schema1:inDefinedTermSet "http://ogc.org/defs" ;
    schema1:name "Temperature" ;
    schema1:termCode "T" .

ex:tempTerm_246u a schema1:PropertyValue ;
    schema1:propertyID "https://qudt.org/vocab/quantitykind/Temperature" ;
    schema1:url "https://qudt.org/vocab/quantitykind/Temperature" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: CDIF schema.org implementation of variableMeasured
type: object
properties:
  '@id':
    type: string
  schema:name:
    type: string
    description: string label associated with the variable in the dataset serialization
  schema:description:
    type: string
    default: missing
  schema:alternateName:
    type: array
    items:
      type: string
      description: human intelligible name for variable that conveys semantics
  schema:measurementTechnique:
    anyOf:
    - type: string
    - type: object
      properties:
        '@id':
          type: string
          description: reference to a skos concept
    - $ref: '#/$defs/DefinedTerm'
    description: Text description or URI identifying the measurement method.
required:
- schema:name
oneOf:
- type: object
  properties:
    '@type':
      type: array
      items:
        type: string
      contains:
        const: schema:PropertyValue
      minItems: 1
    schema:propertyID:
      type: array
      items:
        anyOf:
        - type: string
        - type: object
          properties:
            '@id':
              type: string
        - $ref: '#/$defs/DefinedTerm'
      description: identifier or name for the property concept
    schema:unitText:
      type: string
      description: unit of measurement as text
    schema:unitCode:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
      - $ref: '#/$defs/DefinedTerm'
      description: URI or code identifying the unit of measure
    schema:minValue:
      type: number
      description: minimum numeric value in the dataset
    schema:maxValue:
      type: number
      description: maximum numeric value in the dataset
    schema:url:
      type: string
      format: uri
      description: link to a web page useful for interpreting the variable
  required:
  - '@type'
- type: object
  properties:
    '@type':
      type: array
      items:
        type: string
      contains:
        const: schema:StatisticalVariable
      minItems: 1
    schema:statType:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
      - $ref: '#/$defs/DefinedTerm'
    schema:measuredProperty:
      type: object
      properties:
        '@id':
          type: string
          description: reference to a skos concept for the property
        '@type':
          type: string
          const: schema:Property
        schema:name:
          anyOf:
          - type: string
          - type: object
            properties:
              '@id':
                type: string
          - $ref: '#/$defs/DefinedTerm'
  required:
  - '@type'
  - schema:measuredProperty
$defs:
  DefinedTerm:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/context.jsonld)

## Sources

* [schema.org](https://schema.org/variableMeasured)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/variableMeasured`

