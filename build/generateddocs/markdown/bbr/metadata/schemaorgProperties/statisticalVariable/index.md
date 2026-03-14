
# StatisticalVariable (Schema)

`cdif.bbr.metadata.schemaorgProperties.statisticalVariable` *v0.1*

Schema defining properties for schema.org/StatisticalVariable. Defines a variable that represents a statistical measure. Properties: @type, @id, schema:name, schema:description, schema:alternateName, schema:measurementTechnique, schema:statType, schema:measuredProperty. Uses building blocks: definedTerm (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Schema for schema.org/StatisticalVariable. Defines a variable that represents a statistical measure, such as median income or unemployment rate. Separated from PropertyValue-based variableMeasured to allow independent use in metadata records that describe statistical datasets.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: A statistical variable description using schema.org/StatisticalVariable.
  Defines a variable that represents a statistical measure, such as median income
  or unemployment rate.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: schema:StatisticalVariable
    minItems: 1
  '@id':
    type: string
  schema:name:
    type: string
    description: string label for the statistical variable
  schema:description:
    type: string
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
        anyOf:
        - type: string
          const: schema:Property
        - type: array
          items:
            type: string
          contains:
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
- schema:name
- schema:measuredProperty
$defs:
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/statisticalVariable/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/statisticalVariable/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/statisticalVariable/context.jsonld)

## Sources

* [schema.org](https://schema.org/StatisticalVariable)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/statisticalVariable`

