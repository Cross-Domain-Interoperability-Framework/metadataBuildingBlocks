
# Quality annotation properties (Schema)

`cdif.bbr.metadata.qualityProperties.qualityAnnotation` *v0.1*

Schema defining properties for a narrative or categorical data quality annotation associated with a resource -- a compliance statement, a rating, or a quality certificate, as distinct from a quantitative quality measurement. Defines properties: @type, oa:hasBody, oa:motivatedBy, oa:hasTarget. Uses building blocks: definedTerm (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Quality annotation properties

Defines a set of properties for attaching a **quality annotation** to a resource in the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.

A quality annotation is a *narrative or categorical* quality statement — a standards-compliance note, a rating, or a quality certificate — as distinct from a `dqv:QualityMeasurement`, which reports a *quantitative* value against a named metric. Use a quality **measure** when there is a metric and a measured result (e.g. positional accuracy = 4.2 m); use a quality **annotation** when the quality assertion is a statement or a categorical outcome that does not reduce to a metric/value pair (e.g. "compliant with ISO 19115", or a certification level).

`dqv:QualityAnnotation` is a subclass of the [Web Annotation](https://www.w3.org/TR/annotation-model/) `oa:Annotation`, so this building block follows the DQV pattern rather than inventing new terms:

- **`oa:hasBody`** *(required)* — the content of the annotation: a free-text statement, a `schema:DefinedTerm` for a categorical outcome (a certification level, a pass/fail rating from a controlled vocabulary), or an `@id` reference to a separate body resource.
- **`oa:motivatedBy`** *(recommended)* — why the annotation was made. For quality annotations this is normally the DQV instance `dqv:qualityAssessment`; any motivation IRI or Defined Term is accepted.
- **`oa:hasTarget`** *(optional)* — the resource the annotation is about. When omitted, the annotation is about the resource that carries it (typically the `schema:Dataset`).

The annotation is attached to the described resource with `dqv:hasQualityAnnotation`.

### Relationship to DDI Codebook

DDI Codebook 2.5 `stdyInfo/qualityStatement` maps here: `standardsCompliance/complianceDescription` and `otherQualityStatement` become the `oa:hasBody` of a quality annotation, while `standardsCompliance/standard/standardName` — a machine-actionable claim of conformance to a named standard — is better expressed as `dcterms:conformsTo` on the dataset than as a free-text annotation.

## Examples

### Standards-compliance quality annotation.
A narrative quality annotation asserting that the dataset's metadata conform to ISO 19115.
The compliance statement is the annotation body; the motivation is dqv:qualityAssessment.
#### json
```json
{
  "@type": [
    "dqv:QualityAnnotation"
  ],
  "schema:name": "ISO 19115 compliance statement",
  "oa:motivatedBy": {
    "@id": "dqv:qualityAssessment"
  },
  "oa:hasBody": "Metadata for this dataset were prepared and validated against ISO 19115-1:2014. All mandatory elements are populated and the record passed the national profile conformance check on 2024-03-11.",
  "oa:hasTarget": {
    "@id": "https://example.org/dataset/soil-chem-2024"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "dqv": "http://www.w3.org/ns/dqv#",
      "oa": "http://www.w3.org/ns/oa#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityAnnotation/context.jsonld"
  ],
  "@type": [
    "dqv:QualityAnnotation"
  ],
  "schema:name": "ISO 19115 compliance statement",
  "oa:motivatedBy": {
    "@id": "dqv:qualityAssessment"
  },
  "oa:hasBody": "Metadata for this dataset were prepared and validated against ISO 19115-1:2014. All mandatory elements are populated and the record passed the national profile conformance check on 2024-03-11.",
  "oa:hasTarget": {
    "@id": "https://example.org/dataset/soil-chem-2024"
  }
}
```

#### ttl
```ttl
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix schema1: <http://schema.org/> .

[] a dqv:QualityAnnotation ;
    schema1:name "ISO 19115 compliance statement" ;
    oa:hasBody "Metadata for this dataset were prepared and validated against ISO 19115-1:2014. All mandatory elements are populated and the record passed the national profile conformance check on 2024-03-11." ;
    oa:hasTarget <https://example.org/dataset/soil-chem-2024> ;
    oa:motivatedBy dqv:qualityAssessment .


```


### Quality annotation carrying a categorical rating.
A quality annotation whose body is a schema:DefinedTerm rather than free text — here an Open
Data certification level from a controlled vocabulary, the categorical counterpart of the
narrative statement above.
#### json
```json
{
  "@type": [
    "dqv:QualityAnnotation"
  ],
  "schema:name": "Open Data certification",
  "oa:motivatedBy": {
    "@id": "dqv:qualityAssessment"
  },
  "oa:hasBody": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Silver",
    "schema:termCode": "silver",
    "schema:inDefinedTermSet": "https://certificates.theodi.org/en/about/badges"
  },
  "oa:hasTarget": {
    "@id": "https://example.org/dataset/soil-chem-2024"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "dqv": "http://www.w3.org/ns/dqv#",
      "oa": "http://www.w3.org/ns/oa#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityAnnotation/context.jsonld"
  ],
  "@type": [
    "dqv:QualityAnnotation"
  ],
  "schema:name": "Open Data certification",
  "oa:motivatedBy": {
    "@id": "dqv:qualityAssessment"
  },
  "oa:hasBody": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Silver",
    "schema:termCode": "silver",
    "schema:inDefinedTermSet": "https://certificates.theodi.org/en/about/badges"
  },
  "oa:hasTarget": {
    "@id": "https://example.org/dataset/soil-chem-2024"
  }
}
```

#### ttl
```ttl
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix schema1: <http://schema.org/> .

[] a dqv:QualityAnnotation ;
    schema1:name "Open Data certification" ;
    oa:hasBody [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://certificates.theodi.org/en/about/badges" ;
            schema1:name "Silver" ;
            schema1:termCode "silver" ] ;
    oa:hasTarget <https://example.org/dataset/soil-chem-2024> ;
    oa:motivatedBy dqv:qualityAssessment .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: definitions for a quality annotation property
description: A dqv:QualityAnnotation (a subclass of oa:Annotation) attaches a narrative
  or categorical quality statement -- a standards-compliance note, a rating, or a
  quality certificate -- to a resource. Unlike a dqv:QualityMeasurement it does not
  report a measured value against a named metric; the assertion lives in the annotation
  body.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: dqv:QualityAnnotation
    minItems: 1
  oa:hasBody:
    description: the content of the quality annotation -- a free-text statement, a
      categorical outcome as a Defined Term (e.g. a certification level or a pass/fail
      rating), or a reference to a separate body resource
    anyOf:
    - type: string
    - $ref: '#/$defs/DefinedTerm'
    - type: object
      required:
      - '@id'
      additionalProperties: false
      properties:
        '@id':
          type: string
          description: a resolvable reference to the annotation body
    x-jsonld-id: http://www.w3.org/ns/oa#hasBody
  oa:motivatedBy:
    description: why the annotation was made; for quality annotations this is normally
      the instance dqv:qualityAssessment, but any motivation IRI or Defined Term is
      allowed
    anyOf:
    - type: string
    - type: object
      required:
      - '@id'
      additionalProperties: false
      properties:
        '@id':
          type: string
          description: a resolvable reference to an oa:Motivation
    - $ref: '#/$defs/DefinedTerm'
    x-jsonld-id: http://www.w3.org/ns/oa#motivatedBy
  oa:hasTarget:
    description: the resource the annotation is about; if omitted, the annotation
      is about the resource that carries it (e.g. the Dataset)
    type: object
    required:
    - '@id'
    additionalProperties: false
    properties:
      '@id':
        type: string
        description: a resolvable reference to the annotated resource
    x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
  schema:name:
    type: string
    description: optional short human-readable label for the annotation
    x-jsonld-id: http://schema.org/name
required:
- oa:hasBody
$defs:
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  dqv: http://www.w3.org/ns/dqv#
  oa: http://www.w3.org/ns/oa#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityAnnotation/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityAnnotation/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "oa": "http://www.w3.org/ns/oa#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityAnnotation/context.jsonld)

## Sources

* [Data Quality Vocabulary (DQV) -- Quality Annotation](https://www.w3.org/TR/vocab-dqv/#dqv:QualityAnnotation)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/qualityProperties/qualityAnnotation`

