
# CDIF Key (Schema)

`cdif.bbr.metadata.cdifProperties.cdifKey` *v0.1*

Profile of ddi-cdi Key/PrimaryKey: a CDIF Key is the role of an ordered set of cdi:InstanceVariables (referenced via cdifInstanceVariable) that uniquely identify a data instance. Defines properties: @type, cdif:isComposedOf. Each cdif:ComponentPosition entry carries cdif:indexes (the InstanceVariable) and cdif:value (the integer position). Composes building block: cdifInstanceVariable (cdifProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF Key

A **CDIF Key** is the role of an ordered set of `cdi:InstanceVariable`s that uniquely identifies a data instance — typically the primary key of a tabular dataset, but the same shape covers any composite identifier role.

This is a CDIF profile of DDI-CDI's `Key` / `PrimaryKey` concept. Where the canonical DDI-CDI form composes a Key from `cdi:DataStructureComponent` nodes, the CDIF profile composes it from `cdi:InstanceVariable` nodes (referenced through the `cdifInstanceVariable` building block) so the Key references the actual measured variables rather than an intermediate component layer.

## Structure

- `@type` must contain `"cdif:Key"`.
- `cdif:isComposedOf` is an ordered array of one or more `cdif:ComponentPosition` entries.
- Each `cdif:ComponentPosition` carries:
  - `cdif:indexes` — the `cdi:InstanceVariable` (inline `cdifInstanceVariable` node, or an `@id`-only reference);
  - `cdif:value` — an integer indicating the position of this component within the key, counting upward from `0` or `1`.

The `cdif:value` ordering matters for composite (multi-column) keys: it determines the canonical sort/lookup order so that `(year, country)` and `(country, year)` keys are distinguishable.

## Examples

### Minimal CDIF Key
Single-component key referencing one cdi:InstanceVariable by @id only.
This is the smallest valid cdif:Key — schema requires @type=cdif:Key,
a non-empty cdif:isComposedOf array, and each entry carrying
@type=cdif:ComponentPosition + cdif:indexes + cdif:value.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:Key"],
  "cdif:isComposedOf": [
    { "@id": "ex:var/sampleId" }
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifKey/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:Key"
  ],
  "cdif:isComposedOf": [
    {
      "@id": "ex:var/sampleId"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdif: <https://cdif.org/0.1/> .

[] a cdif:Key ;
    cdif:isComposedOf <https://example.org/var/sampleId> .


```


### Complete CDIF Key
Composite (two-column) key with a fully-described inline cdifInstanceVariable
node for the first component and an @id-only reference for the second.
Demonstrates the inline-or-ref pattern, cdif:value ordering, and use of
every property the schema permits including @id on the Key itself.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:Key"],
  "@id": "ex:dataset/observations/key/primary",
  "cdif:isComposedOf": [
    {
      "@id": "ex:var/year",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:name": "year",
      "schema:alternateName": ["Observation year"],
      "schema:description": "Calendar year in which the observation was recorded.",
      "schema:propertyID": ["ex:concept/calendarYear"],
      "schema:unitText": "year",
      "cdi:identifier": "ex:var/year",
      "cdi:physicalDataType": ["xsd:gYear"],
      "cdi:simpleUnitOfMeasure": "year",
      "cdi:name": "year",
      "cdi:displayLabel": "Observation year",
      "cdi:role": "Dimension"
    },
    { "@id": "ex:var/countryCode" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifKey/context.jsonld",
    {
      "schema": "http://schema.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:Key"
  ],
  "@id": "ex:dataset/observations/key/primary",
  "cdif:isComposedOf": [
    {
      "@id": "ex:var/year",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:name": "year",
      "schema:alternateName": [
        "Observation year"
      ],
      "schema:description": "Calendar year in which the observation was recorded.",
      "schema:propertyID": [
        "ex:concept/calendarYear"
      ],
      "schema:unitText": "year",
      "cdi:identifier": "ex:var/year",
      "cdi:physicalDataType": [
        "xsd:gYear"
      ],
      "cdi:simpleUnitOfMeasure": "year",
      "cdi:name": "year",
      "cdi:displayLabel": "Observation year",
      "cdi:role": "Dimension"
    },
    {
      "@id": "ex:var/countryCode"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/dataset/observations/key/primary> a cdif:Key ;
    cdif:isComposedOf <https://example.org/var/countryCode>,
        <https://example.org/var/year> .

<https://example.org/var/year> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "Observation year" ;
    cdi:identifier "ex:var/year" ;
    cdi:name "year" ;
    cdi:physicalDataType "xsd:gYear" ;
    cdi:role "Dimension" ;
    cdi:simpleUnitOfMeasure "year" ;
    schema1:alternateName "Observation year" ;
    schema1:description "Calendar year in which the observation was recorded." ;
    schema1:name "year" ;
    schema1:propertyID "ex:concept/calendarYear" ;
    schema1:unitText "year" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Key
description: 'Profile of ddi-cdi Key/PrimaryKey: a CDIF Key is the role of an ordered
  set of cdi:InstanceVariables (referenced via cdifInstanceVariable) that uniquely
  identify a data instance. Array order of cdif:isComposedOf items is the position;
  no intermediate ComponentPosition wrapper.'
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: cdif:Key
    minItems: 1
  '@id':
    type: string
    description: Identifier for this Key node.
  cdif:isComposedOf:
    type: array
    description: Ordered list of cdi:InstanceVariables (inline cdifInstanceVariable
      or @id-reference to one declared elsewhere in the dataset). Position is implicit
      in array order.
    items:
      anyOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifInstanceVariable/schema.yaml
      - type: object
        description: object reference via URI or URI fragment to a variable declared
          in the same document
        properties:
          '@id':
            type: string
        required:
        - '@id'
    minItems: 1
required:
- '@type'
- cdif:isComposedOf
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  cdif: https://cdif.org/0.1/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifKey/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifKey/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "prov": "http://www.w3.org/ns/prov#",
    "cdif": "https://cdif.org/0.1/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifKey/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifKey`

