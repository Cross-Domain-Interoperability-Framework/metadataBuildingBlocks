
# ODRL Rule (Schema)

`cdif.bbr.metadata.odrlProperties.odrlRule` *v0.1*

W3C ODRL 2.2 Rule: Permission (with duties), Prohibition (with remedies) or Duty (with consequences). Each rule has one action and may name its target asset or asset collection, output, assigner, assignee and constraints; target and parties may instead be given at policy level. Uses building blocks: odrlAction, odrlAsset, odrlParty, odrlConstraint (odrlProperties), objectReference (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ODRL Rule

W3C ODRL 2.2 Rule: Permission (with duties), Prohibition (with remedies) or Duty (with consequences). Each rule has one action and may name its target asset or asset collection, output, assigner, assignee and constraints; target and parties may instead be given at policy level.

Generic W3C ODRL; CDIF-specific rules belong in profile blocks such as [odrlOffer](../odrlOffer/).

### Dependencies

- [odrlAction](../odrlAction/)
- [odrlAsset](../odrlAsset/)
- [odrlParty](../odrlParty/)
- [odrlConstraint](../odrlConstraint/)
- [objectReference](../../cdifDataType/objectReference/)

## Examples

### ODRL Permission with a duty
Permission to distribute a dataset, with a duty to attribute; if the duty is not met, a consequence duty to compensate.
#### json
```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/"
  },
  "@type": [
    "odrl:Permission"
  ],
  "odrl:target": {
    "@id": "https://example.org/dataset/3936/distribution/csv"
  },
  "odrl:action": {
    "@id": "odrl:distribute"
  },
  "odrl:assignee": {
    "@id": "https://example.org/user/1"
  },
  "odrl:duty": [
    {
      "@type": [
        "odrl:Duty"
      ],
      "odrl:action": {
        "@id": "odrl:attribute"
      },
      "odrl:consequence": [
        {
          "@type": [
            "odrl:Duty"
          ],
          "odrl:action": {
            "@id": "odrl:compensate"
          }
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
      "odrl": "http://www.w3.org/ns/odrl/2/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlRule/context.jsonld",
    {
      "odrl": "http://www.w3.org/ns/odrl/2/"
    }
  ],
  "@type": [
    "odrl:Permission"
  ],
  "odrl:target": {
    "@id": "https://example.org/dataset/3936/distribution/csv"
  },
  "odrl:action": {
    "@id": "odrl:distribute"
  },
  "odrl:assignee": {
    "@id": "https://example.org/user/1"
  },
  "odrl:duty": [
    {
      "@type": [
        "odrl:Duty"
      ],
      "odrl:action": {
        "@id": "odrl:attribute"
      },
      "odrl:consequence": [
        {
          "@type": [
            "odrl:Duty"
          ],
          "odrl:action": {
            "@id": "odrl:compensate"
          }
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .

[] a odrl:Permission ;
    odrl:action odrl:distribute ;
    odrl:assignee <https://example.org/user/1> ;
    odrl:duty [ a odrl:Duty ;
            odrl:action odrl:attribute ;
            odrl:consequence [ a odrl:Duty ;
                    odrl:action odrl:compensate ] ] ;
    odrl:target <https://example.org/dataset/3936/distribution/csv> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ODRL Rule
description: 'An ODRL 2.2 Rule (https://www.w3.org/TR/odrl-model/#rule): a Permission
  (may do), a Prohibition (must not do) or a Duty (must do). Every rule has one action
  and may name its target asset, the parties (assigner, assignee) and constraints.
  Target and parties may instead be given once at policy level (odrlPolicy), so only
  the action is required here. A Permission may carry duties that must be fulfilled
  to exercise it, a Prohibition remedies owed if it is broken, and a Duty consequences
  owed if it is not fulfilled.'
type: object
properties:
  '@context':
    type: object
    description: JSON-LD namespace prefixes for ODRL properties.
    properties:
      odrl:
        const: http://www.w3.org/ns/odrl/2/
anyOf:
- $ref: '#/$defs/Permission'
- $ref: '#/$defs/Prohibition'
- $ref: '#/$defs/Duty'
$defs:
  Target:
    description: The asset, as a reference or an Asset or AssetCollection node.
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlAsset/schema.yaml
  PartyRef:
    description: A party, as a reference or a Party or PartyCollection node.
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlParty/schema.yaml
  Rule:
    type: object
    properties:
      '@id':
        type: string
        format: iri
      '@type':
        type: array
        items:
          type: string
      odrl:target:
        $ref: '#/$defs/Target'
        x-jsonld-id: http://www.w3.org/ns/odrl/2/target
      odrl:output:
        description: An asset created by exercising the action, e.g. the result of
          odrl:derive.
        $ref: '#/$defs/Target'
        x-jsonld-id: http://www.w3.org/ns/odrl/2/output
      odrl:action:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlAction/schema.yaml
        x-jsonld-id: http://www.w3.org/ns/odrl/2/action
      odrl:assigner:
        $ref: '#/$defs/PartyRef'
        x-jsonld-id: http://www.w3.org/ns/odrl/2/assigner
      odrl:assignee:
        $ref: '#/$defs/PartyRef'
        x-jsonld-id: http://www.w3.org/ns/odrl/2/assignee
      odrl:constraint:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlConstraint/schema.yaml
        x-jsonld-id: http://www.w3.org/ns/odrl/2/constraint
    required:
    - odrl:action
  Permission:
    allOf:
    - $ref: '#/$defs/Rule'
    - properties:
        '@type':
          contains:
            const: odrl:Permission
        odrl:duty:
          description: Duties that must be fulfilled before the permission can be
            exercised.
          type: array
          items:
            $ref: '#/$defs/Duty'
          x-jsonld-id: http://www.w3.org/ns/odrl/2/duty
  Prohibition:
    allOf:
    - $ref: '#/$defs/Rule'
    - properties:
        '@type':
          contains:
            const: odrl:Prohibition
        odrl:remedy:
          description: Duties owed if the prohibition is infringed.
          type: array
          items:
            $ref: '#/$defs/Duty'
          x-jsonld-id: http://www.w3.org/ns/odrl/2/remedy
  Duty:
    allOf:
    - $ref: '#/$defs/Rule'
    - properties:
        '@type':
          contains:
            const: odrl:Duty
        odrl:consequence:
          description: Further duties owed if this duty is not fulfilled.
          type: array
          items:
            $ref: '#/$defs/Duty'
          x-jsonld-id: http://www.w3.org/ns/odrl/2/consequence
x-jsonld-prefixes:
  odrl: http://www.w3.org/ns/odrl/2/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.odrlProperties.odrlRule
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-29'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlRule/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlRule/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlRule/context.jsonld)

## Sources

* [W3C ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [W3C ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/odrlProperties/odrlRule`

