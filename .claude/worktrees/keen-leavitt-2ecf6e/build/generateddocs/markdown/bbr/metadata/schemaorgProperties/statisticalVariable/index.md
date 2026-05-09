
# StatisticalVariable (Schema)

`cdif.bbr.metadata.schemaorgProperties.statisticalVariable` *v0.1*

Schema defining properties for schema.org/StatisticalVariable. Defines a variable that represents a statistical measure. Properties: @type, @id, schema:name, schema:description, schema:alternateName, schema:measurementTechnique, schema:statType, schema:measuredProperty. Uses building blocks: definedTerm (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Schema for schema.org/StatisticalVariable. Defines a variable that represents a statistical measure, such as median income or unemployment rate. Separated from PropertyValue-based variableMeasured to allow independent use in metadata records that describe statistical datasets.

## Examples

### Example Statistical Variable
Example statistical variable defining a median household income measure.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/"
  },
  "@id": "ex:statvar-median-income",
  "@type": [
    "schema:StatisticalVariable"
  ],
  "schema:name": "Median Household Income",
  "schema:description": "Median annual household income in US dollars, estimated from survey data.",
  "schema:statType": "Median",
  "schema:measuredProperty": {
    "@type": [
      "schema:Property"
    ],
    "schema:name": "household income"
  },
  "schema:measurementTechnique": "American Community Survey 5-year estimates"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/statisticalVariable/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:statvar-median-income",
  "@type": [
    "schema:StatisticalVariable"
  ],
  "schema:name": "Median Household Income",
  "schema:description": "Median annual household income in US dollars, estimated from survey data.",
  "schema:statType": "Median",
  "schema:measuredProperty": {
    "@type": [
      "schema:Property"
    ],
    "schema:name": "household income"
  },
  "schema:measurementTechnique": "American Community Survey 5-year estimates"
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:statvar-median-income a schema1:StatisticalVariable ;
    schema1:description "Median annual household income in US dollars, estimated from survey data." ;
    schema1:measuredProperty [ a schema1:Property ;
            schema1:name "household income" ] ;
    schema1:measurementTechnique "American Community Survey 5-year estimates" ;
    schema1:name "Median Household Income" ;
    schema1:statType "Median" .


```


### Complete statistical variable example.
StatisticalVariable instance exercising all properties: name, description,
alternateName, measuredProperty (with DefinedTerm name), statType
(DefinedTerm), and measurementTechnique (DefinedTerm).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/"
  },
  "@id": "ex:StatVarComplete_001",
  "@type": ["schema:StatisticalVariable"],
  "schema:name": "Annual Mean Surface Air Temperature",
  "schema:description": "Spatially averaged annual mean surface air temperature computed from hourly station observations within each grid cell, quality-controlled and homogenized",
  "schema:alternateName": ["Annual Mean SAT", "Mean Surface Temperature"],
  "schema:measuredProperty": {
    "@id": "https://www.wikidata.org/entity/Q11466",
    "@type": ["schema:Property"],
    "schema:name": {
      "@type": ["schema:DefinedTerm"],
      "schema:name": "Surface Air Temperature",
      "schema:termCode": "SAT",
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/P07/current/"
    }
  },
  "schema:statType": {
    "@type": ["schema:DefinedTerm"],
    "schema:name": "Arithmetic Mean",
    "schema:termCode": "mean",
    "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/S06/current/"
  },
  "schema:measurementTechnique": {
    "@type": ["schema:DefinedTerm"],
    "schema:name": "Automatic Weather Station",
    "schema:termCode": "AWS",
    "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/statisticalVariable/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:StatVarComplete_001",
  "@type": [
    "schema:StatisticalVariable"
  ],
  "schema:name": "Annual Mean Surface Air Temperature",
  "schema:description": "Spatially averaged annual mean surface air temperature computed from hourly station observations within each grid cell, quality-controlled and homogenized",
  "schema:alternateName": [
    "Annual Mean SAT",
    "Mean Surface Temperature"
  ],
  "schema:measuredProperty": {
    "@id": "https://www.wikidata.org/entity/Q11466",
    "@type": [
      "schema:Property"
    ],
    "schema:name": {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Surface Air Temperature",
      "schema:termCode": "SAT",
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/P07/current/"
    }
  },
  "schema:statType": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Arithmetic Mean",
    "schema:termCode": "mean",
    "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/S06/current/"
  },
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Automatic Weather Station",
    "schema:termCode": "AWS",
    "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/"
  }
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:StatVarComplete_001 a schema1:StatisticalVariable ;
    schema1:alternateName "Annual Mean SAT",
        "Mean Surface Temperature" ;
    schema1:description "Spatially averaged annual mean surface air temperature computed from hourly station observations within each grid cell, quality-controlled and homogenized" ;
    schema1:measuredProperty <https://www.wikidata.org/entity/Q11466> ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.nerc.ac.uk/collection/L05/current/" ;
            schema1:name "Automatic Weather Station" ;
            schema1:termCode "AWS" ] ;
    schema1:name "Annual Mean Surface Air Temperature" ;
    schema1:statType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.nerc.ac.uk/collection/S06/current/" ;
            schema1:name "Arithmetic Mean" ;
            schema1:termCode "mean" ] .

<https://www.wikidata.org/entity/Q11466> a schema1:Property ;
    schema1:name [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.nerc.ac.uk/collection/P07/current/" ;
            schema1:name "Surface Air Temperature" ;
            schema1:termCode "SAT" ] .


```

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
        type: array
        items:
          type: string
        contains:
          const: schema:Property
        minItems: 1
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

