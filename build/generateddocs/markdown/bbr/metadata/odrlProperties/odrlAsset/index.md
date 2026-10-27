
# ODRL Asset (Schema)

`cdif.bbr.metadata.odrlProperties.odrlAsset` *v0.1*

W3C ODRL 2.2 Asset (the resource a rule applies to, identified by IRI, optionally odrl:partOf collections) or AssetCollection (a group of assets, identified by @id, or by odrl:source narrowed with odrl:refinement). In CDIF the asset is normally a distribution or data service. Uses building blocks: odrlConstraint (odrlProperties), objectReference (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ODRL Asset

W3C ODRL 2.2 Asset (the resource a rule applies to, identified by IRI, optionally odrl:partOf collections) or AssetCollection (a group of assets, identified by @id, or by odrl:source narrowed with odrl:refinement). In CDIF the asset is normally a distribution or data service.

Generic W3C ODRL; CDIF-specific rules belong in profile blocks such as [odrlOffer](../odrlOffer/).

### Dependencies

- [odrlConstraint](../odrlConstraint/)
- [objectReference](../../cdifDataType/objectReference/)

## Examples

### ODRL refined AssetCollection
The distributions of a dataset, refined to those in CSV format.
#### json
```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/"
  },
  "@type": [
    "odrl:AssetCollection"
  ],
  "odrl:source": {
    "@id": "https://example.org/dataset/3936/distributions"
  },
  "odrl:refinement": [
    {
      "@type": [
        "odrl:Constraint"
      ],
      "odrl:leftOperand": {
        "@id": "odrl:fileFormat"
      },
      "odrl:operator": {
        "@id": "odrl:eq"
      },
      "odrl:rightOperand": "text/csv"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "odrl": "http://www.w3.org/ns/odrl/2/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlAsset/context.jsonld",
    {
      "odrl": "http://www.w3.org/ns/odrl/2/"
    }
  ],
  "@type": [
    "odrl:AssetCollection"
  ],
  "odrl:source": {
    "@id": "https://example.org/dataset/3936/distributions"
  },
  "odrl:refinement": [
    {
      "@type": [
        "odrl:Constraint"
      ],
      "odrl:leftOperand": {
        "@id": "odrl:fileFormat"
      },
      "odrl:operator": {
        "@id": "odrl:eq"
      },
      "odrl:rightOperand": "text/csv"
    }
  ]
}
```

#### ttl
```ttl
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .

[] a odrl:AssetCollection ;
    odrl:refinement [ a odrl:Constraint ;
            odrl:leftOperand odrl:fileFormat ;
            odrl:operator odrl:eq ;
            odrl:rightOperand "text/csv" ] ;
    odrl:source <https://example.org/dataset/3936/distributions> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ODRL Asset
description: 'An ODRL 2.2 Asset (https://www.w3.org/TR/odrl-model/#asset) or AssetCollection
  (https://www.w3.org/TR/odrl-model/#asset-collection): the resource a rule applies
  to. In CDIF this is normally a distribution or data service, identified by its IRI.
  An AssetCollection groups assets: either the collection itself, identified by @id,
  or a subset of one, where odrl:source names the collection and odrl:refinement narrows
  it (e.g. the CSV distributions of a dataset).'
type: object
properties:
  '@context':
    type: object
    description: JSON-LD namespace prefixes for ODRL properties.
    properties:
      odrl:
        const: http://www.w3.org/ns/odrl/2/
anyOf:
- $ref: '#/$defs/Asset'
- $ref: '#/$defs/AssetCollection'
$defs:
  Asset:
    type: object
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: odrl:Asset
      '@id':
        type: string
        format: iri
      odrl:partOf:
        description: AssetCollections this asset is a member of.
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        x-jsonld-id: http://www.w3.org/ns/odrl/2/partOf
    required:
    - '@type'
    - '@id'
  AssetCollection:
    description: Per ODRL, a refined collection is identified through odrl:source,
      so odrl:refinement requires odrl:source.
    type: object
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: odrl:AssetCollection
      '@id':
        type: string
        format: iri
      odrl:source:
        description: The collection this one is drawn from.
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        x-jsonld-id: http://www.w3.org/ns/odrl/2/source
      odrl:refinement:
        description: Constraints selecting the members of odrl:source that belong
          to this collection.
        type: array
        minItems: 1
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlConstraint/schema.yaml
        x-jsonld-id: http://www.w3.org/ns/odrl/2/refinement
    required:
    - '@type'
    anyOf:
    - required:
      - '@id'
    - required:
      - odrl:source
    dependentRequired:
      odrl:refinement:
      - odrl:source
x-jsonld-prefixes:
  odrl: http://www.w3.org/ns/odrl/2/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.odrlProperties.odrlAsset
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-27'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlAsset/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlAsset/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlAsset/context.jsonld)

## Sources

* [W3C ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [W3C ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/odrlProperties/odrlAsset`

