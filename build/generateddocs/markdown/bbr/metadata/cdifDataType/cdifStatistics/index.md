
# CDIF Statistics (Schema)

`cdif.bbr.metadata.cdifDataType.cdifStatistics` *v0.1*

Profile of DDI-CDI Statistics, StatisticsCollection, Statistic, CategoryStatistics, and Category. A Statistics node bundles one or more Statistic value objects (mean, count, median, etc.) optionally weighted by an InstanceVariable and optionally broken down by Category via CategoryStatistics. A StatisticsCollection groups multiple Statistics nodes and records the InstanceVariables they index. Composes building block: cdifInstanceVariable (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF Statistics

CDIF profile of the DDI-CDI **Statistics**, **CategoryStatistics**, and **StatisticsCollection** classes (2026-03 model). Used to attach computed summary values (counts, means, quantiles, etc.) to a dataset, a variable, or a category of values within a variable.

## CDIF divergences from canonical DDI-CDI

- Properties valued by `InternationalString` / `LabelForDisplay` / `ObjectName` in DDI-CDI are simplified to plain strings and carried under the `cdif:` namespace — here, on `cdi:Category`: `cdif:name`, `cdif:descriptiveText`, `cdif:definition`, `cdif:displayLabel`.
- The polymorphic `cdi:has` association is split into target-specific keys: `cdif:has_CategoryStatistics` (on `Statistics`) and `cdif:has_Statistics` (on `StatisticsCollection`).
- `cdif:appliesTo` and `cdif:indexedBy` are CDIF additions — they link statistics to the `InstanceVariable`(s) they describe and are **not** present in the canonical DDI-CDI model.

## Classes

### `cdi:Statistic` (dataType)

A single computed value. A value object — no identity, always appears inline inside a `cdi:statistic` array. Properties:

- `cdi:computationBase` — the cases included in the computation: `Total` (all cases), `ValidOnly` (valid values only), `MissingOnly` (invalid cases only).
- `cdi:content` — the numeric value of the statistic.
- `cdi:isWeighted` — `true` when the value was computed using a weighting variable; default `false`.
- `cdi:typeOfNumericValue` — the numeric type of `cdi:content` — `decimal`, `float`, or `double`.

### `cdi:Statistics`

A named bundle of one or more `cdi:Statistic` value objects for an instance variable. Properties:

- `@id` — optional identifier.
- `@type` — must contain `cdi:Statistics`.
- `cdi:typeOfStatistic` — the kind of statistic (mean, median, count, …) for the whole bundle.
- `cdi:statistic` — ordered array of one or more inline `Statistic` objects (required).
- `cdi:hasWeight` — `cdi:InstanceVariable` whose values were used as weights (inline or `@id`-ref).
- `cdif:appliesTo` — CDIF addition: the `InstanceVariable`(s) this bundle summarizes.
- `cdif:has_CategoryStatistics` — array of `CategoryStatistics` entries for per-category breakdowns.

### `cdi:CategoryStatistics`

Statistics for a specific `cdi:Category` of an instance variable.

- `cdi:for` — the `Category` (inline or `@id`-ref) (required).
- `cdi:typeOfStatistic` — the kind of statistic.
- `cdi:statistic` — per-category `Statistic` value objects (required).
- `cdi:hasWeight` — the weighting `InstanceVariable`.

### `cdi:StatisticsCollection`

Groups multiple `Statistics` nodes for an instance variable. Properties:

- `@id` — optional identifier.
- `@type` — must contain `cdi:StatisticsCollection`.
- `cdif:has_Statistics` — array of one or more `Statistics` nodes (inline or `@id`-ref) (required).
- `cdif:indexedBy` — CDIF addition: the `InstanceVariable`(s) the contained statistics index — the collection-level coordinate space.
- `cdi:hasWeight` — the weighting `InstanceVariable`.

### `cdi:Category`

Minimal Category shape used as a `CategoryStatistics` target, carrying the `cdif:`-namespaced simplified string properties (`cdif:name`, `cdif:descriptiveText`, `cdif:definition`, `cdif:displayLabel`). Full category modelling lives in `cdifEnumerationDomain` / SKOS Concept.

## Usage

The root of this building block validates **any of** a `Statistics`, `CategoryStatistics`, or `StatisticsCollection` node (via `anyOf`). External building blocks compose individual `$defs` (e.g. `cdifStatistics/schema.yaml#/$defs/Statistics`) when only one shape is needed.

## Examples

### Minimal CDIF Statistics
Smallest valid cdi:Statistics node — one cdi:typeOfStatistic ("count") and
one cdi:statistic value object carrying cdi:computationBase + cdi:content.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/",
    "schema": "http://schema.org/"
  },
  "@type": [
    "cdi:Statistics"
  ],
  "cdi:typeOfStatistic": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Count",
    "schema:termCode": "count",
    "schema:inDefinedTermSet": "https://ddialliance.org/vocab/statistic-types"
  },
  "cdi:statistic": [
    {
      "cdi:computationBase": "Total",
      "cdi:content": 1500
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifStatistics/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/",
      "schema": "http://schema.org/"
    }
  ],
  "@type": [
    "cdi:Statistics"
  ],
  "cdi:typeOfStatistic": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Count",
    "schema:termCode": "count",
    "schema:inDefinedTermSet": "https://ddialliance.org/vocab/statistic-types"
  },
  "cdi:statistic": [
    {
      "cdi:computationBase": "Total",
      "cdi:content": 1500
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a cdi:Statistics ;
    cdi:statistic [ cdi:computationBase "Total" ;
            cdi:content 1500 ] ;
    cdi:typeOfStatistic [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://ddialliance.org/vocab/statistic-types" ;
            schema1:name "Count" ;
            schema1:termCode "count" ] .


```


### Statistics with weighting and per-category breakdown
A cdi:Statistics bundle for a temperature variable: typeOfStatistic = mean,
cdif:appliesTo links the variable, cdi:hasWeight references the weighting
variable, two cdi:statistic value variants (weighted ValidOnly + unweighted
Total), and cdif:has_CategoryStatistics carrying surface / deep breakdowns.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "ex": "https://example.org/"
  },
  "@id": "ex:stats/temperature-mean",
  "@type": [
    "cdi:Statistics"
  ],
  "cdi:typeOfStatistic": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "arithmetic mean",
    "schema:identifier": "https://example.org/vocab/stat-types/mean",
    "schema:inDefinedTermSet": "https://example.org/vocab/stat-types"
  },
  "cdif:appliesTo": [
    {
      "@id": "ex:var-temperature"
    }
  ],
  "cdi:hasWeight": {
    "@id": "ex:var-sample-weight"
  },
  "cdi:statistic": [
    {
      "cdi:computationBase": "ValidOnly",
      "cdi:content": 12.43,
      "cdi:typeOfNumericValue": "double",
      "cdi:isWeighted": true
    },
    {
      "cdi:computationBase": "Total",
      "cdi:content": 12.1,
      "cdi:typeOfNumericValue": "double",
      "cdi:isWeighted": false
    }
  ],
  "cdif:has_CategoryStatistics": [
    {
      "@type": [
        "cdi:CategoryStatistics"
      ],
      "cdi:typeOfStatistic": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Mean",
        "schema:termCode": "mean",
        "schema:inDefinedTermSet": "https://ddialliance.org/vocab/statistic-types"
      },
      "cdi:for": {
        "@type": [
          "cdi:Category"
        ],
        "@id": "ex:category/surface",
        "cdif:descriptiveText": "Surface samples (depth < 10 m)"
      },
      "cdi:statistic": [
        {
          "cdi:computationBase": "ValidOnly",
          "cdi:content": 15.81,
          "cdi:isWeighted": true
        }
      ]
    },
    {
      "@type": [
        "cdi:CategoryStatistics"
      ],
      "cdi:typeOfStatistic": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Mean",
        "schema:termCode": "mean",
        "schema:inDefinedTermSet": "https://ddialliance.org/vocab/statistic-types"
      },
      "cdi:for": {
        "@id": "ex:category/deep"
      },
      "cdi:statistic": [
        {
          "cdi:computationBase": "ValidOnly",
          "cdi:content": 10.07,
          "cdi:isWeighted": true
        }
      ]
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
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifStatistics/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:stats/temperature-mean",
  "@type": [
    "cdi:Statistics"
  ],
  "cdi:typeOfStatistic": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "arithmetic mean",
    "schema:identifier": "https://example.org/vocab/stat-types/mean",
    "schema:inDefinedTermSet": "https://example.org/vocab/stat-types"
  },
  "cdif:appliesTo": [
    {
      "@id": "ex:var-temperature"
    }
  ],
  "cdi:hasWeight": {
    "@id": "ex:var-sample-weight"
  },
  "cdi:statistic": [
    {
      "cdi:computationBase": "ValidOnly",
      "cdi:content": 12.43,
      "cdi:typeOfNumericValue": "double",
      "cdi:isWeighted": true
    },
    {
      "cdi:computationBase": "Total",
      "cdi:content": 12.1,
      "cdi:typeOfNumericValue": "double",
      "cdi:isWeighted": false
    }
  ],
  "cdif:has_CategoryStatistics": [
    {
      "@type": [
        "cdi:CategoryStatistics"
      ],
      "cdi:typeOfStatistic": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Mean",
        "schema:termCode": "mean",
        "schema:inDefinedTermSet": "https://ddialliance.org/vocab/statistic-types"
      },
      "cdi:for": {
        "@type": [
          "cdi:Category"
        ],
        "@id": "ex:category/surface",
        "cdif:descriptiveText": "Surface samples (depth < 10 m)"
      },
      "cdi:statistic": [
        {
          "cdi:computationBase": "ValidOnly",
          "cdi:content": 15.81,
          "cdi:isWeighted": true
        }
      ]
    },
    {
      "@type": [
        "cdi:CategoryStatistics"
      ],
      "cdi:typeOfStatistic": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Mean",
        "schema:termCode": "mean",
        "schema:inDefinedTermSet": "https://ddialliance.org/vocab/statistic-types"
      },
      "cdi:for": {
        "@id": "ex:category/deep"
      },
      "cdi:statistic": [
        {
          "cdi:computationBase": "ValidOnly",
          "cdi:content": 10.07,
          "cdi:isWeighted": true
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/stats/temperature-mean> a cdi:Statistics ;
    cdi:hasWeight ex:var-sample-weight ;
    cdi:statistic [ cdi:computationBase "ValidOnly" ;
            cdi:content 1.243e+01 ;
            cdi:isWeighted true ;
            cdi:typeOfNumericValue "double" ],
        [ cdi:computationBase "Total" ;
            cdi:content 1.21e+01 ;
            cdi:isWeighted false ;
            cdi:typeOfNumericValue "double" ] ;
    cdi:typeOfStatistic [ a schema1:DefinedTerm ;
            schema1:identifier "https://example.org/vocab/stat-types/mean" ;
            schema1:inDefinedTermSet "https://example.org/vocab/stat-types" ;
            schema1:name "arithmetic mean" ] ;
    cdif:appliesTo ex:var-temperature ;
    cdif:has_CategoryStatistics [ a cdi:CategoryStatistics ;
            cdi:for <https://example.org/category/deep> ;
            cdi:statistic [ cdi:computationBase "ValidOnly" ;
                    cdi:content 1.007e+01 ;
                    cdi:isWeighted true ] ;
            cdi:typeOfStatistic [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "https://ddialliance.org/vocab/statistic-types" ;
                    schema1:name "Mean" ;
                    schema1:termCode "mean" ] ],
        [ a cdi:CategoryStatistics ;
            cdi:for <https://example.org/category/surface> ;
            cdi:statistic [ cdi:computationBase "ValidOnly" ;
                    cdi:content 1.581e+01 ;
                    cdi:isWeighted true ] ;
            cdi:typeOfStatistic [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "https://ddialliance.org/vocab/statistic-types" ;
                    schema1:name "Mean" ;
                    schema1:termCode "mean" ] ] .

<https://example.org/category/surface> a cdi:Category ;
    cdif:descriptiveText "Surface samples (depth < 10 m)" .


```


### CDIF StatisticsCollection
A cdi:StatisticsCollection grouping two Statistics nodes (one per indexed
variable). cdif:indexedBy names the collection-level coordinate space;
cdif:has_Statistics carries the member Statistics nodes.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "ex": "https://example.org/"
  },
  "@id": "ex:stats/dataset-summary",
  "@type": ["cdi:StatisticsCollection"],
  "cdif:indexedBy": [
    { "@id": "ex:var-temperature" },
    { "@id": "ex:var-salinity" }
  ],
  "cdif:has_Statistics": [
    {
      "@id": "ex:stats/temperature-mean",
      "@type": ["cdi:Statistics"],
      "cdi:typeOfStatistic": "mean",
      "cdif:appliesTo": [
        { "@id": "ex:var-temperature" }
      ],
      "cdi:statistic": [
        {
          "cdi:computationBase": "Total",
          "cdi:content": 12.43
        }
      ]
    },
    {
      "@id": "ex:stats/salinity-mean",
      "@type": ["cdi:Statistics"],
      "cdi:typeOfStatistic": "mean",
      "cdif:appliesTo": [
        { "@id": "ex:var-salinity" }
      ],
      "cdi:statistic": [
        {
          "cdi:computationBase": "Total",
          "cdi:content": 34.21
        }
      ]
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifStatistics/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:stats/dataset-summary",
  "@type": [
    "cdi:StatisticsCollection"
  ],
  "cdif:indexedBy": [
    {
      "@id": "ex:var-temperature"
    },
    {
      "@id": "ex:var-salinity"
    }
  ],
  "cdif:has_Statistics": [
    {
      "@id": "ex:stats/temperature-mean",
      "@type": [
        "cdi:Statistics"
      ],
      "cdi:typeOfStatistic": "mean",
      "cdif:appliesTo": [
        {
          "@id": "ex:var-temperature"
        }
      ],
      "cdi:statistic": [
        {
          "cdi:computationBase": "Total",
          "cdi:content": 12.43
        }
      ]
    },
    {
      "@id": "ex:stats/salinity-mean",
      "@type": [
        "cdi:Statistics"
      ],
      "cdi:typeOfStatistic": "mean",
      "cdif:appliesTo": [
        {
          "@id": "ex:var-salinity"
        }
      ],
      "cdi:statistic": [
        {
          "cdi:computationBase": "Total",
          "cdi:content": 34.21
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix ex: <https://example.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/stats/dataset-summary> a cdi:StatisticsCollection ;
    cdif:has_Statistics <https://example.org/stats/salinity-mean>,
        <https://example.org/stats/temperature-mean> ;
    cdif:indexedBy ex:var-salinity,
        ex:var-temperature .

<https://example.org/stats/salinity-mean> a cdi:Statistics ;
    cdi:statistic [ cdi:computationBase "Total" ;
            cdi:content 3.421e+01 ] ;
    cdi:typeOfStatistic "mean" ;
    cdif:appliesTo ex:var-salinity .

<https://example.org/stats/temperature-mean> a cdi:Statistics ;
    cdi:statistic [ cdi:computationBase "Total" ;
            cdi:content 1.243e+01 ] ;
    cdi:typeOfStatistic "mean" ;
    cdif:appliesTo ex:var-temperature .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Statistics
description: 'CDIF profile of the DDI-CDI Statistics / CategoryStatistics / StatisticsCollection
  classes (2026-03 model). A Statistics node carries one or more Statistic value objects;
  CategoryStatistics carries per-category results; a StatisticsCollection groups Statistics
  nodes. The root validates any of the three. CDIF divergences from canonical DDI-CDI:
  properties valued by InternationalString / LabelForDisplay / ObjectName are simplified
  to plain strings and carried under the cdif: namespace (cdif:name, cdif:descriptiveText,
  cdif:definition, cdif:displayLabel); the polymorphic cdi:has association is split
  into target-specific cdif:has_* keys; cdif:appliesTo and cdif:indexedBy are CDIF
  additions (not present in the canonical model) that link statistics to the InstanceVariable(s)
  they describe.'
type: object
anyOf:
- $ref: '#/$defs/Statistics'
- $ref: '#/$defs/CategoryStatistics'
- $ref: '#/$defs/StatisticsCollection'
$defs:
  Statistic:
    title: Statistic
    description: "DDI-CDI Statistic dataType \u2014 a single computed value (mean,
      count, median, etc.). A value object with no identity; appears inline inside
      a cdi:statistic array."
    type: object
    properties:
      cdi:computationBase:
        type: string
        enum:
        - MissingOnly
        - Total
        - ValidOnly
        description: "The cases included in determining the statistic \u2014 Total
          (all cases, valid and missing), ValidOnly (valid values only), MissingOnly
          (invalid cases only)."
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/computationBase
      cdi:content:
        type: number
        description: The value of the statistic expressed as a real number.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/content
      cdi:isWeighted:
        type: boolean
        default: false
        description: True if the statistic was computed using a weighting variable.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isWeighted
      cdi:typeOfNumericValue:
        type: string
        description: "The type of numeric value carried in cdi:content \u2014 decimal,
          float, or double."
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/typeOfNumericValue
  Statistics:
    title: Statistics
    description: A named bundle of one or more Statistic value objects for an instance
      variable, optionally weighted, optionally broken down by Category.
    type: object
    properties:
      '@id':
        type: string
        description: Identifier for this Statistics node.
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Statistics
        minItems: 1
      cdi:typeOfStatistic:
        description: "Controlled-vocabulary entry naming the kind of statistic \u2014
          e.g. mean, median, count, sum, stdDev."
        $ref: '#/$defs/SkosConcept'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/typeOfStatistic
      cdi:statistic:
        type: array
        description: "Ordered list of Statistic value objects carried by this bundle.
          Order is significant \u2014 consumers MAY rely on array position."
        items:
          $ref: '#/$defs/Statistic'
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/statistic
      cdi:hasWeight:
        description: The InstanceVariable whose values were used as weights when computing
          the Statistic entries (inline cdifInstanceVariable node or an @id-reference).
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/schema.yaml
        - type: object
          properties:
            '@id':
              type: string
          required:
          - '@id'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasWeight
      cdif:appliesTo:
        type: array
        description: "CDIF addition (not in canonical DDI-CDI): the InstanceVariable(s)
          this Statistics bundle summarizes \u2014 the per-bundle \"what these numbers
          describe\" link. When a Statistics node sits inside a StatisticsCollection
          that indexes more than one variable, cdif:appliesTo disambiguates which
          variable each bundle describes."
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/schema.yaml
          - type: object
            properties:
              '@id':
                type: string
            required:
            - '@id'
        minItems: 1
        x-jsonld-id: https://cdif.org/0.1/appliesTo
      cdif:has_CategoryStatistics:
        type: array
        description: 'CategoryStatistics entries breaking this Statistics bundle down
          by Category. cdif: namespaced and target-suffixed because the DDI-CDI cdi:has
          association is polymorphic.'
        items:
          $ref: '#/$defs/CategoryStatistics'
        x-jsonld-id: https://cdif.org/0.1/has_CategoryStatistics
    required:
    - '@type'
    - cdi:statistic
  CategoryStatistics:
    title: CategoryStatistics
    description: Statistics for a specific Category of an instance variable within
      a data set.
    type: object
    properties:
      '@id':
        type: string
        description: Identifier for this CategoryStatistics node.
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:CategoryStatistics
        minItems: 1
      cdi:for:
        description: The Category this CategoryStatistics is for (inline Category
          node or an @id-reference).
        anyOf:
        - $ref: '#/$defs/Category'
        - type: object
          properties:
            '@id':
              type: string
          required:
          - '@id'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/for
      cdi:typeOfStatistic:
        description: Controlled-vocabulary entry naming the kind of statistic.
        $ref: '#/$defs/SkosConcept'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/typeOfStatistic
      cdi:statistic:
        type: array
        description: Per-category Statistic value objects.
        items:
          $ref: '#/$defs/Statistic'
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/statistic
      cdi:hasWeight:
        description: The InstanceVariable whose values were used as weights (inline
          cdifInstanceVariable node or an @id-reference).
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/schema.yaml
        - type: object
          properties:
            '@id':
              type: string
          required:
          - '@id'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasWeight
    required:
    - '@type'
    - cdi:for
    - cdi:statistic
  StatisticsCollection:
    title: StatisticsCollection
    description: Groups one or more Statistics nodes for an instance variable. A typical
      use is a dataset-level collection holding row-count / mean / stddev Statistics
      for each measured variable.
    type: object
    properties:
      '@id':
        type: string
        description: Identifier for this StatisticsCollection node.
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:StatisticsCollection
        minItems: 1
      cdi:hasWeight:
        description: The InstanceVariable whose values were used as weights (inline
          cdifInstanceVariable node or an @id-reference).
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/schema.yaml
        - type: object
          properties:
            '@id':
              type: string
          required:
          - '@id'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasWeight
      cdif:has_Statistics:
        type: array
        description: 'Statistics nodes carried by this collection (inline or @id-ref).
          cdif: namespaced and target-suffixed because the DDI-CDI cdi:has association
          is polymorphic.'
        items:
          anyOf:
          - $ref: '#/$defs/Statistics'
          - type: object
            properties:
              '@id':
                type: string
            required:
            - '@id'
        minItems: 1
        x-jsonld-id: https://cdif.org/0.1/has_Statistics
      cdif:indexedBy:
        type: array
        description: "CDIF addition (not in canonical DDI-CDI): the InstanceVariable(s)
          the contained Statistics index \u2014 the collection-level coordinate space."
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/schema.yaml
          - type: object
            properties:
              '@id':
                type: string
            required:
            - '@id'
        minItems: 1
        x-jsonld-id: https://cdif.org/0.1/indexedBy
    required:
    - '@type'
    - cdif:has_Statistics
  Category:
    title: Category
    description: 'Minimal Category shape used as a CategoryStatistics target. CDIF
      simplifies the DDI-CDI InternationalString / LabelForDisplay / ObjectName valued
      properties to plain strings carried under the cdif: namespace. A full CDIF treatment
      of categories lives in cdifEnumerationDomain / SKOS Concept.'
    type: object
    properties:
      '@id':
        type: string
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Category
        minItems: 1
      cdif:name:
        type: array
        items:
          type: string
        description: Human-understandable name(s). CDIF-simplified from DDI-CDI Category.name
          (ObjectName) to plain strings.
        x-jsonld-id: https://cdif.org/0.1/name
      cdif:descriptiveText:
        type: string
        description: Short natural-language account of the category. CDIF-simplified
          from DDI-CDI Category.descriptiveText (InternationalString).
        x-jsonld-id: https://cdif.org/0.1/descriptiveText
      cdif:definition:
        type: string
        description: Natural-language definition of the category. CDIF-simplified
          from DDI-CDI Category.definition (InternationalString).
        x-jsonld-id: https://cdif.org/0.1/definition
      cdif:displayLabel:
        type: array
        items:
          type: string
        description: Human-readable display label(s). CDIF-simplified from DDI-CDI
          Category.displayLabel (LabelForDisplay).
        x-jsonld-id: https://cdif.org/0.1/displayLabel
  SkosConcept:
    title: SKOS Concept (CDIF vocabulary-bound term reference)
    description: "Vocabulary-bound term reference. CDIF policy implements the DDI-CDI
      ControlledVocabularyEntry / PairedControlledVocabularyEntry concept as a skos:Concept
      from the skosProperties building block. Under the union-type-policy a Concept
      value MUST be a controlled-vocabulary term \u2014 either an @id-only reference
      into a known scheme, a structured schema:DefinedTerm, or a full inline skos:Concept
      node. Plain strings are NOT permitted because vocabulary identity cannot be
      recovered from an unscoped string label."
    anyOf:
    - type: object
      properties:
        '@id':
          type: string
      required:
      - '@id'
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  cdif: https://cdif.org/0.1/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifStatistics/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifStatistics/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "spdx": "http://spdx.org/rdf/terms#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifStatistics/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifStatistics`

