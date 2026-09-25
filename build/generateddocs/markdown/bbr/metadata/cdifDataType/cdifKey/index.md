
# CDIF Key (Schema)

`cdif.bbr.metadata.cdifDataType.cdifKey` *v0.1*

Profile of ddi-cdi Key/PrimaryKey: a CDIF Key is the role of an ordered set of cdi:InstanceVariables (referenced via cdifInstanceVariable) that uniquely identify a data instance. Defines properties: @type, cdif:isComposedOf. Each cdif:ComponentPosition entry carries cdif:indexes (the InstanceVariable) and cdif:value (the integer position). Composes building block: cdifInstanceVariable (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF Key

A **CDIF Key** is the role of an ordered set of `cdi:InstanceVariable`s that uniquely identifies a data instance — typically the primary key of a tabular dataset, but the same shape covers any composite identifier role.

This is a CDIF profile of DDI-CDI's `Key` / `PrimaryKey` concept. Where the canonical DDI-CDI form composes a Key from `cdi:DataStructureComponent` nodes, the CDIF profile composes it from `cdi:InstanceVariable` nodes (referenced through the `cdifInstanceVariable` building block) so the Key references the actual measured variables rather than an intermediate component layer.

## Structure

- `@type` must contain `"cdif:Key"`.
- `cdif:isComposedOf` is an ordered array of one or more `cdi:ComponentPosition` entries.
- Each `cdi:ComponentPosition` carries:
  - `cdi:indexes` — an `@id`-only reference to the `cdi:InstanceVariable`, which is declared elsewhere in the document (normally in `schema:variableMeasured`);
  - `cdi:value` — an integer indicating the position of this component within the key, counting upward from `0` or `1`.

The `cdi:value` ordering matters for composite (multi-column) keys: it determines the canonical sort/lookup order so that `(year, country)` and `(country, year)` keys are distinguishable.

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
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:Key"],
  "cdif:isComposedOf": [
    {
      "@type": ["cdi:ComponentPosition"],
      "cdi:indexes": { "@id": "ex:var/sampleId" },
      "cdi:value": 1
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
      "cdif": "https://w3id.org/cdif/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifKey/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:Key"
  ],
  "cdif:isComposedOf": [
    {
      "@type": [
        "cdi:ComponentPosition"
      ],
      "cdi:indexes": {
        "@id": "ex:var/sampleId"
      },
      "cdi:value": 1
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a cdif:Key ;
    cdif:isComposedOf [ a cdi:ComponentPosition ;
            cdi:indexes <https://example.org/var/sampleId> ;
            cdi:value 1 ] .


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
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/"
  },
  "@type": [
    "cdif:Key"
  ],
  "@id": "ex:dataset/observations/key/primary",
  "cdif:isComposedOf": [
    {
      "@type": [
        "cdi:ComponentPosition"
      ],
      "@id": "ex:dataset/observations/key/primary/pos/1",
      "cdi:value": 1,
      "cdi:indexes": {
        "@id": "ex:var/year"
      }
    },
    {
      "@type": [
        "cdi:ComponentPosition"
      ],
      "@id": "ex:dataset/observations/key/primary/pos/2",
      "cdi:value": 2,
      "cdi:indexes": {
        "@id": "ex:var/countryCode"
      }
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
      "cdif": "https://w3id.org/cdif/",
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifKey/context.jsonld",
    {
      "schema": "http://schema.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:Key"
  ],
  "@id": "ex:dataset/observations/key/primary",
  "cdif:isComposedOf": [
    {
      "@type": [
        "cdi:ComponentPosition"
      ],
      "@id": "ex:dataset/observations/key/primary/pos/1",
      "cdi:value": 1,
      "cdi:indexes": {
        "@id": "ex:var/year"
      }
    },
    {
      "@type": [
        "cdi:ComponentPosition"
      ],
      "@id": "ex:dataset/observations/key/primary/pos/2",
      "cdi:value": 2,
      "cdi:indexes": {
        "@id": "ex:var/countryCode"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/dataset/observations/key/primary> a cdif:Key ;
    cdif:isComposedOf <https://example.org/dataset/observations/key/primary/pos/1>,
        <https://example.org/dataset/observations/key/primary/pos/2> .

<https://example.org/dataset/observations/key/primary/pos/1> a cdi:ComponentPosition ;
    cdi:indexes <https://example.org/var/year> ;
    cdi:value 1 .

<https://example.org/dataset/observations/key/primary/pos/2> a cdi:ComponentPosition ;
    cdi:indexes <https://example.org/var/countryCode> ;
    cdi:value 2 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Key
description: 'Profile of ddi-cdi Key/PrimaryKey: a CDIF Key is the role of an ordered
  set of cdi:InstanceVariables (referenced via cdifInstanceVariable) that uniquely
  identify a data instance. Each variable''s position in the key is recorded with
  an explicit cdi:ComponentPosition wrapper carrying cdi:indexes (the variable) and
  cdi:value (the integer position), matching the canonical DDI-CDI PrimaryKey structure
  in ddicdiDataStructure.'
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
    description: Ordered list of cdi:ComponentPosition wrappers. Each wrapper carries
      cdi:indexes (an @id-reference to a cdi:InstanceVariable declared elsewhere in
      the dataset) and cdi:value (the 1-based integer position in the key).
    items:
      type: object
      description: ComponentPosition wrapper indexing one variable's position in the
        key.
      properties:
        '@type':
          type: array
          items:
            type: string
          contains:
            const: cdi:ComponentPosition
          minItems: 1
        '@id':
          type: string
          description: Identifier for this ComponentPosition node.
        cdi:indexes:
          description: 'The variable this position indexes -- an @id-reference to
            one declared elsewhere in the document. At dataset level (cdif:hasPrimaryKey)
            that is a cdi:InstanceVariable in schema:variableMeasured; at data-structure
            level (cdif:has_PrimaryKey, cdif:has_ForeignKey) it is a cdi:RepresentedVariable
            in the structure. The value is a bare objectReference either way: a key
            names variables that are defined once and referenced from the key, so
            an inline variable here would be a second copy of a node that already
            exists.'
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
          x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/indexes
        cdi:value:
          type: integer
          minimum: 1
          default: 1
          description: 1-based position of this variable in the ordered key. Pinned
            to a minimum of 1 because a key that might be 0- or 1-based has ambiguous
            ordering, which defeats the purpose of recording a position at all --
            and because both structure-level key definitions already rejected 0, so
            the latitude this description used to advertise was never honoured anywhere.
          x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/value
      required:
      - '@type'
      - cdi:indexes
      - cdi:value
    minItems: 1
    x-jsonld-id: https://w3id.org/cdif/isComposedOf
required:
- '@type'
- cdif:isComposedOf
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  cdif: https://w3id.org/cdif/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifKey/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifKey/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifKey/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifKey`

