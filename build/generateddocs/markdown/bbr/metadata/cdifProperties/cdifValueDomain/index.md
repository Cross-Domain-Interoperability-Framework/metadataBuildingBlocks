
# CDIF Value Domain (Schema)

`cdif.bbr.metadata.cdifProperties.cdifValueDomain` *v0.1*

CDIF profile of the DDI-CDI ValueDomain. A single node is either a cdif:SubstantiveValueDomain (subject-matter values) or a cdif:SentinelValueDomain (processing/missing-value codes). Each carries cdif:takesValuesFrom (refs cdifEnumerationDomain), cdif:displayLabel, and an array cdif:recommendedDataType of xsd: type tokens; at least one of takesValuesFrom or recommendedDataType is required.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF Value Domain

A **CDIF Value Domain** describes the set of values a variable may take — either *substantive* (subject-matter values of interest) or *sentinel* (processing or missing-value codes like SAS `.R`, SPSS `999`, "not applicable", etc.).

This is a CDIF profile of the DDI-CDI `ValueDomain` family. A single node is **one of**:

- `cdif:SubstantiveValueDomain` — the real values a variable measures.
- `cdif:SentinelValueDomain` — codes that flag missing, refused, not-applicable, or otherwise non-substantive observations.

The schema discriminates the two via `@type` (a `oneOf` over the two `$defs`).

## Structure

Each subclass carries the same shape:

| Property | Type | Notes |
|---|---|---|
| `@type` | array | Must contain `cdif:SubstantiveValueDomain` or `cdif:SentinelValueDomain` |
| `@id` | string | Optional IRI for the domain node |
| `cdif:takesValuesFrom` | anyOf | Inline [cdifEnumerationDomain](../cdifEnumerationDomain/) or `{@id}` reference |
| `cdif:displayLabel` | string | Short human-readable label (multilingual via repeat) |
| `cdif:recommendedDataType` | array | One or more `xsd:` type tokens (e.g. `xsd:decimal`, `xsd:date`) drawn from the enum in `$defs/xsdDataType` |

`@type` is required, plus **at least one of** `cdif:takesValuesFrom` or `cdif:recommendedDataType` — a value domain that pins neither an enumeration nor a recommended data type is not informative.

## Relationship to other BBs

- **[cdifEnumerationDomain](../cdifEnumerationDomain/)** — `cdif:takesValuesFrom` refs this BB when the value set is a controlled vocabulary, codelist, or classification.
- **[cdifInstanceVariable](../cdifInstanceVariable/)** — references a CDIF Value Domain to describe permissible values for the variable.
- **[ddicdiValueDomain](../../ddiProperties/ddicdiValueDomain/)** — the native DDI-CDI version (covers ValueAndConceptDescription, conceptual domain pointers, platformType). This CDIF profile is intentionally slimmer.

## Notes

- Where DDI-CDI uses `cdi:ValueAndConceptDescription` for value/concept description, CDIF uses `skos:Concept` (via [skosConcept](../../skosProperties/skosConcept/)) as the general pattern. This BB does not yet expose a description pointer; add `cdif:isDescribedBy` → `skosConcept` if/when needed.
- The `xsdDataType` enum is the same fixed list used elsewhere in CDIF for advertising recommended XML Schema datatypes.

## Examples

### Minimal CDIF Value Domain
A bare cdif:SubstantiveValueDomain that recommends a single xsd:nonNegativeInteger
data type for an age-in-years variable. Schema requires @type plus at least one of
cdif:takesValuesFrom or cdif:recommendedDataType; this example satisfies the latter.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdif": "https://cdif.org/0.1/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:SubstantiveValueDomain"],
  "@id": "ex:vd/age-years",
  "cdif:recommendedDataType": ["xsd:nonNegativeInteger"]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdif": "https://cdif.org/0.1/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifValueDomain/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdif": "https://cdif.org/0.1/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:SubstantiveValueDomain"
  ],
  "@id": "ex:vd/age-years",
  "cdif:recommendedDataType": [
    "xsd:nonNegativeInteger"
  ]
}
```

#### ttl
```ttl
@prefix cdif: <https://cdif.org/0.1/> .

<https://example.org/vd/age-years> a cdif:SubstantiveValueDomain ;
    cdif:recommendedDataType "xsd:nonNegativeInteger" .


```


### Complete CDIF Value Domain
A cdif:SubstantiveValueDomain for ISO 3166-1 alpha-2 country codes — exercises
every property: cdif:takesValuesFrom (inline cdifEnumerationDomain),
cdif:displayLabel, and cdif:recommendedDataType (two xsd: types).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:SubstantiveValueDomain"],
  "@id": "ex:vd/country-iso3166",
  "cdif:displayLabel": "ISO 3166-1 alpha-2 country code",
  "cdif:takesValuesFrom": {
    "@type": ["cdif:EnumerationDomain"],
    "@id": "ex:enum-domain/iso3166",
    "schema:name": "ISO 3166-1 alpha-2 country codes",
    "schema:inDefinedTermSet": {
      "@id": "https://www.iso.org/obp/ui/#iso:pub:PUB500001"
    }
  },
  "cdif:recommendedDataType": ["xsd:string", "xsd:token"]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifValueDomain/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:SubstantiveValueDomain"
  ],
  "@id": "ex:vd/country-iso3166",
  "cdif:displayLabel": "ISO 3166-1 alpha-2 country code",
  "cdif:takesValuesFrom": {
    "@type": [
      "cdif:EnumerationDomain"
    ],
    "@id": "ex:enum-domain/iso3166",
    "schema:name": "ISO 3166-1 alpha-2 country codes",
    "schema:inDefinedTermSet": {
      "@id": "https://www.iso.org/obp/ui/#iso:pub:PUB500001"
    }
  },
  "cdif:recommendedDataType": [
    "xsd:string",
    "xsd:token"
  ]
}
```

#### ttl
```ttl
@prefix cdif: <https://cdif.org/0.1/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/vd/country-iso3166> a cdif:SubstantiveValueDomain ;
    cdif:displayLabel "ISO 3166-1 alpha-2 country code" ;
    cdif:recommendedDataType "xsd:string",
        "xsd:token" ;
    cdif:takesValuesFrom <https://example.org/enum-domain/iso3166> .

<https://example.org/enum-domain/iso3166> a cdif:EnumerationDomain ;
    schema1:inDefinedTermSet <https://www.iso.org/obp/ui/#iso:pub:PUB500001> ;
    schema1:name "ISO 3166-1 alpha-2 country codes" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Value Domain
description: "Value domain for substantive or sentinel values for a variable. Typically
  a description and/or enumeration of allowed values of interest. CDIF profile of
  the DDI-CDI ValueDomain \u2014 a single node is either a cdif:SubstantiveValueDomain
  (subject-matter values) or a cdif:SentinelValueDomain (processing/missing-value
  codes)."
oneOf:
- $ref: '#/$defs/SubstantiveValueDomain'
- $ref: '#/$defs/SentinelValueDomain'
$defs:
  SubstantiveValueDomain:
    type: object
    description: Value domain for a substantive conceptual domain. Typically a description
      and/or enumeration of allowed values of interest.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdif:SubstantiveValueDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this SubstantiveValueDomain node
      cdif:takesValuesFrom:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifEnumerationDomain/schema.yaml
        - type: object
          description: JSON-LD @id reference to a node defined elsewhere in the graph
          properties:
            '@id':
              type: string
              description: IRI or blank node identifier of the referenced node
          required:
          - '@id'
      cdif:displayLabel:
        type: string
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
      cdif:recommendedDataType:
        type: array
        description: The data types that are recommended for use with this domain.
        items:
          $ref: '#/$defs/xsdDataType'
        minItems: 1
    required:
    - '@type'
    anyOf:
    - required:
      - cdif:takesValuesFrom
    - required:
      - cdif:recommendedDataType
  SentinelValueDomain:
    type: object
    description: Value domain for a sentinel conceptual domain.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdif:SentinelValueDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this SentinelValueDomain node
      cdif:takesValuesFrom:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifEnumerationDomain/schema.yaml
        - type: object
          description: JSON-LD @id reference to a node defined elsewhere in the graph
          properties:
            '@id':
              type: string
              description: IRI or blank node identifier of the referenced node
          required:
          - '@id'
      cdif:displayLabel:
        type: string
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
      cdif:recommendedDataType:
        type: array
        description: The data types that are recommended for use with this domain.
        items:
          $ref: '#/$defs/xsdDataType'
        minItems: 1
    required:
    - '@type'
    anyOf:
    - required:
      - cdif:takesValuesFrom
    - required:
      - cdif:recommendedDataType
  xsdDataType:
    type: string
    enum:
    - xsd:anyURI
    - xsd:base64Binary
    - xsd:boolean
    - xsd:byte
    - xsd:date
    - xsd:dateTime
    - xsd:decimal
    - xsd:double
    - xsd:float
    - xsd:gDay
    - xsd:gMonth
    - xsd:gMonthDay
    - xsd:gYear
    - xsd:gYearMonth
    - xsd:hexBinary
    - xsd:int
    - xsd:integer
    - xsd:language
    - xsd:long
    - xsd:Name
    - xsd:NCName
    - xsd:NMTOKEN
    - xsd:negativeInteger
    - xsd:nonNegativeInteger
    - xsd:nonPositiveInteger
    - xsd:normalizedString
    - xsd:positiveInteger
    - xsd:short
    - xsd:string
    - xsd:time
    - xsd:token
    - xsd:unsignedByte
    - xsd:unsignedInt
    - xsd:unsignedLong
    - xsd:unsignedShort
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  cdif: https://cdif.org/0.1/
  skos: http://www.w3.org/2004/02/skos/core#
  xsd: http://www.w3.org/2001/XMLSchema#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifValueDomain/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifValueDomain/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifValueDomain/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifValueDomain`

