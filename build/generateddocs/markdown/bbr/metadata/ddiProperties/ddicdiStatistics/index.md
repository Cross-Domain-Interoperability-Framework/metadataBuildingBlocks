
# DDI-CDI Statistics (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiStatistics` *v0.1*

Statistics related to an instance variable within a data set.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI **Statistics** covers summary and category statistics computed for an instance variable within a data set. Generated from the 2026-03 DDI-CDI model (`DataDescription` / `FormatDescription` packages).

The root validates any of three concrete classes:

- **`cdi:Statistics`** — a bundle of `cdi:Statistic` values for an instance variable, with `cdi:typeOfStatistic` (count, mean, median, …) and an optional `cdi:hasWeight` reference to the weighting `InstanceVariable`.
- **`cdi:CategoryStatistics`** — statistics for a specific `cdi:Category` of an instance variable; carries `cdi:appliesTo` (the `InstanceVariable`), `cdi:for` (the `Category`), and a `cdi:statistic` list.
- **`cdi:StatisticsCollection`** — groups summary and category statistics for an instance variable.

Supporting `$defs`: `cdi:Statistic` (the value object — `cdi:content`, `cdi:computationBase`, `cdi:isWeighted`, `cdi:typeOfNumericValue`) and `cdi:Category`.

This is the canonical `ddiProperties` counterpart to the CDIF schema.org `cdifStatistics` building block.

## Examples

### Statistics bundle for an instance variable
A cdi:Statistics node carrying two cdi:Statistic values (a weighted mean
and an unweighted valid-case count) for a sea-water-temperature instance
variable, with cdi:hasWeight referencing the weighting variable by @id.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:Statistics"],
  "@id": "ex:stats/seaWaterTemp/summary",
  "cdi:typeOfStatistic": {
    "@type": ["cdi:ControlledVocabularyEntry"],
    "cdi:entryValue": ["mean"]
  },
  "cdi:hasWeight": {
    "@id": "ex:var/sampleWeight"
  },
  "cdi:statistic": [
    {
      "@type": ["cdi:Statistic"],
      "cdi:content": 12.43,
      "cdi:computationBase": "ValidOnly",
      "cdi:isWeighted": true,
      "cdi:typeOfNumericValue": "double"
    },
    {
      "@type": ["cdi:Statistic"],
      "cdi:content": 1487,
      "cdi:computationBase": "ValidOnly",
      "cdi:isWeighted": false,
      "cdi:typeOfNumericValue": "decimal"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiStatistics/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:Statistics"
  ],
  "@id": "ex:stats/seaWaterTemp/summary",
  "cdi:typeOfStatistic": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "mean"
    ]
  },
  "cdi:hasWeight": {
    "@id": "ex:var/sampleWeight"
  },
  "cdi:statistic": [
    {
      "@type": [
        "cdi:Statistic"
      ],
      "cdi:content": 12.43,
      "cdi:computationBase": "ValidOnly",
      "cdi:isWeighted": true,
      "cdi:typeOfNumericValue": "double"
    },
    {
      "@type": [
        "cdi:Statistic"
      ],
      "cdi:content": 1487,
      "cdi:computationBase": "ValidOnly",
      "cdi:isWeighted": false,
      "cdi:typeOfNumericValue": "decimal"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/stats/seaWaterTemp/summary> a cdi:Statistics ;
    cdi:hasWeight <https://example.org/var/sampleWeight> ;
    cdi:statistic [ a cdi:Statistic ;
            cdi:computationBase "ValidOnly" ;
            cdi:content 1.243e+01 ;
            cdi:isWeighted true ;
            cdi:typeOfNumericValue "double" ],
        [ a cdi:Statistic ;
            cdi:computationBase "ValidOnly" ;
            cdi:content 1487 ;
            cdi:isWeighted false ;
            cdi:typeOfNumericValue "decimal" ] ;
    cdi:typeOfStatistic [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "mean" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Statistics
description: Statistics related to an instance variable within a data set.
anyOf:
- $ref: '#/$defs/Statistics'
- $ref: '#/$defs/CategoryStatistics'
- $ref: '#/$defs/StatisticsCollection'
$defs:
  Statistics:
    type: object
    description: Statistics related to an instance variable within a data set.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Statistics
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Statistics node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:statistic:
        type: array
        items:
          $ref: '#/$defs/Statistic'
        description: The value of the identified type of statistic. May be repeated
          to provide unweighted or weighted values and different computation bases.
      cdi:typeOfStatistic:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Type of summary statistics (e.g. count, mean, mode, median, etc.)
          or category statistics for the associated instance variable
      cdi:hasWeight:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiInstanceVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:has:
        anyOf:
        - $ref: '#/$defs/StatisticsCollection'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  CategoryStatistics:
    type: object
    description: Statistics related to a specific category of an instance variable
      within a data set.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:CategoryStatistics
        minItems: 1
      '@id':
        type: string
        description: Identifier for this CategoryStatistics node
      cdi:for:
        anyOf:
        - $ref: '#/$defs/Category'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:statistic:
        type: array
        items:
          $ref: '#/$defs/Statistic'
        description: The value of the identified type of statistic. May be repeated
          to provide unweighted or weighted values and different computation bases.
      cdi:typeOfStatistic:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Type of summary statistics (e.g. count, mean, mode, median, etc.)
          or category statistics for the associated instance variable
      cdi:hasWeight:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiInstanceVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:has:
        anyOf:
        - $ref: '#/$defs/StatisticsCollection'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  StatisticsCollection:
    type: object
    description: Collection of summary and category statistics for an instance variable
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:StatisticsCollection
        minItems: 1
      '@id':
        type: string
        description: Identifier for this StatisticsCollection node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:hasWeight:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiInstanceVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  Category:
    type: object
    description: Concept whose role is to define and measure a characteristic.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Category
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Category node
      cdi:descriptiveText:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: A short natural language account of the characteristics of the
          object.
      cdi:definition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Natural language statement conveying the meaning of a concept,
          differentiating it from other concepts. Supports the use of multiple languages
          and structured text. 'externalDefinition' can't be used if 'definition'
          is used.
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
      cdi:externalDefinition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        description: A reference to an external definition of a concept (that is,
          a concept which is described outside the content of the DDI-CDI metadata
          description). An example is a SKOS concept. The definition property is assumed
          to duplicate the external one referenced if externalDefinition is used.
          Other corresponding properties are assumed to be included unchanged if used.
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
      cdi:uses:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  Statistic:
    type: object
    description: The value of the statistic expressed as a decimal, float and/or double.
      Indicates whether it is weighted value and the computation base.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Statistic
        minItems: 1
      cdi:computationBase:
        type: string
        enum:
        - MissingOnly
        - Total
        - ValidOnly
        description: Defines the cases included in determining the statistic. The
          options are total = all cases, valid and missing (invalid); validOnly =
          Only valid values, missing (invalid) are not included in the calculation;
          missingOnly = Only missing (invalid) cases included in the calculation.
      cdi:content:
        type: number
        description: The value of the statistic expressed as a real number.
      cdi:isWeighted:
        type: boolean
        description: Set to True if the statistic is weighted.
      cdi:typeOfNumericValue:
        type: string
        description: Indicate the type of numeric value as decimal, float, double.
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiStatistics/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiStatistics/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiStatistics/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiStatistics`

