
# CDIF Access (Schema)

`cdif.bbr.metadata.profiles.cdifProfile.cdifAccess` *v0.1*

Profile module for machine-actionable access and usage conditions expressed as ODRL Offer policies. Requires that the metadata record declare conformance to https://w3id.org/cdif/access/1.1 and carry at least one policy: inline or by {@id} reference as odrl:hasPolicy on a schema:distribution item, or as an {@id} reference in schema:conditionsOfAccess on the Dataset (only a reference there, because cdifCore's item shapes do not admit an inline Offer). Draft: the conformance URI and the cdifa1 action vocabulary are not yet minted. Uses building blocks: odrlOffer (odrlProperties), objectReference (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Access

Profile module for machine-actionable access and usage conditions, expressed as [ODRL Offer](../../../odrlProperties/odrlOffer/) policies. A conforming record declares `https://w3id.org/cdif/access/1.1` and carries at least one policy:

- as `odrl:hasPolicy` on a `schema:distribution` item, inline or by `{@id}` reference (preferred: distributions of one dataset can differ in their conditions), or
- as an `{@id}` reference in `schema:conditionsOfAccess` on the Dataset. Only a reference fits there, because cdifCore's item shapes for that property do not admit an inline Offer.

Draft. Open questions are listed in the schema descriptions and in [odrlOffer](../../../odrlProperties/odrlOffer/).

### Dependencies

- [odrlOffer](../../../odrlProperties/odrlOffer/) - the ODRL Offer policy
- [objectReference](../../../cdifDataType/objectReference/) - `{@id}` references

## Examples

### CDIF Access record
Dataset with one CSV distribution carrying an inline ODRL Offer as
odrl:hasPolicy, and the same Offer referenced by uid from
schema:conditionsOfAccess alongside a prose statement. The Offer follows
the CDIF Access spreadsheet: a download permission with an assent access
condition, a data-destruction obligation and a prohibition. Illustrative
values only.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "ex": "https://example.org/",
    "cdifa1": "https://w3id.org/cdif/access/profile1/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  },
  "@type": [
    "schema:Dataset"
  ],
  "@id": "ex:dataset/3936",
  "schema:name": "Example restricted-access survey dataset",
  "schema:conditionsOfAccess": [
    "Users located in the UK may download the data after assenting to the End User Licence.",
    {
      "@id": "https://example.org/odrloffer/13adb49c-f641-4ac7-aa90-18651cc211ce"
    }
  ],
  "schema:subjectOf": {
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/access/1.1"
      }
    ]
  },
  "schema:distribution": [
    {
      "@id": "ex:dataset/3936/distribution/csv",
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Survey responses (CSV)",
      "schema:contentUrl": "https://example.org/data/3936/responses.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "odrl:hasPolicy": [
        {
          "@type": [
            "odrl:Offer"
          ],
          "@id": "https://example.org/odrloffer/13adb49c-f641-4ac7-aa90-18651cc211ce",
          "odrl:profile": {
            "@id": "https://w3id.org/cdif/access/profile1/cdifa1.ttl"
          },
          "odrl:assigner": {
            "@id": "https://example.org/repository"
          },
          "odrl:permission": [
            {
              "odrl:target": {
                "@id": "https://example.org/dataset/3936/distribution/csv"
              },
              "odrl:action": {
                "@id": "cdifa1:download"
              },
              "odrl:constraint": [
                {
                  "@type": [
                    "odrl:Constraint"
                  ],
                  "odrl:leftOperand": {
                    "@id": "odrl:spatial"
                  },
                  "odrl:operator": {
                    "@id": "odrl:eq"
                  },
                  "odrl:rightOperand": {
                    "@id": "http://publications.europa.eu/resource/authority/country/GBR"
                  }
                }
              ],
              "odrl:duty": [
                {
                  "odrl:action": {
                    "@id": "cdifa1:assent"
                  },
                  "odrl:constraint": [
                    {
                      "@type": [
                        "odrl:Constraint"
                      ],
                      "odrl:leftOperand": {
                        "@id": "odrl:event"
                      },
                      "odrl:operator": {
                        "@id": "odrl:lt"
                      },
                      "odrl:rightOperand": {
                        "@id": "odrl:policyUsage"
                      }
                    }
                  ]
                }
              ]
            }
          ],
          "odrl:obligation": [
            {
              "odrl:target": {
                "@id": "https://example.org/dataset/3936/distribution/csv"
              },
              "odrl:action": {
                "@id": "cdifa1:datadestruction"
              }
            }
          ],
          "odrl:prohibition": [
            {
              "odrl:target": {
                "@id": "https://example.org/dataset/3936/distribution/csv"
              },
              "odrl:action": {
                "@id": "cdifa1:shareTRECredentials"
              }
            }
          ]
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
      "dcterms": "http://purl.org/dc/terms/",
      "odrl": "http://www.w3.org/ns/odrl/2/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifAccess/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "odrl": "http://www.w3.org/ns/odrl/2/",
      "ex": "https://example.org/",
      "cdifa1": "https://w3id.org/cdif/access/profile1/",
      "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    }
  ],
  "@type": [
    "schema:Dataset"
  ],
  "@id": "ex:dataset/3936",
  "schema:name": "Example restricted-access survey dataset",
  "schema:conditionsOfAccess": [
    "Users located in the UK may download the data after assenting to the End User Licence.",
    {
      "@id": "https://example.org/odrloffer/13adb49c-f641-4ac7-aa90-18651cc211ce"
    }
  ],
  "schema:subjectOf": {
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/access/1.1"
      }
    ]
  },
  "schema:distribution": [
    {
      "@id": "ex:dataset/3936/distribution/csv",
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Survey responses (CSV)",
      "schema:contentUrl": "https://example.org/data/3936/responses.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "odrl:hasPolicy": [
        {
          "@type": [
            "odrl:Offer"
          ],
          "@id": "https://example.org/odrloffer/13adb49c-f641-4ac7-aa90-18651cc211ce",
          "odrl:profile": {
            "@id": "https://w3id.org/cdif/access/profile1/cdifa1.ttl"
          },
          "odrl:assigner": {
            "@id": "https://example.org/repository"
          },
          "odrl:permission": [
            {
              "odrl:target": {
                "@id": "https://example.org/dataset/3936/distribution/csv"
              },
              "odrl:action": {
                "@id": "cdifa1:download"
              },
              "odrl:constraint": [
                {
                  "@type": [
                    "odrl:Constraint"
                  ],
                  "odrl:leftOperand": {
                    "@id": "odrl:spatial"
                  },
                  "odrl:operator": {
                    "@id": "odrl:eq"
                  },
                  "odrl:rightOperand": {
                    "@id": "http://publications.europa.eu/resource/authority/country/GBR"
                  }
                }
              ],
              "odrl:duty": [
                {
                  "odrl:action": {
                    "@id": "cdifa1:assent"
                  },
                  "odrl:constraint": [
                    {
                      "@type": [
                        "odrl:Constraint"
                      ],
                      "odrl:leftOperand": {
                        "@id": "odrl:event"
                      },
                      "odrl:operator": {
                        "@id": "odrl:lt"
                      },
                      "odrl:rightOperand": {
                        "@id": "odrl:policyUsage"
                      }
                    }
                  ]
                }
              ]
            }
          ],
          "odrl:obligation": [
            {
              "odrl:target": {
                "@id": "https://example.org/dataset/3936/distribution/csv"
              },
              "odrl:action": {
                "@id": "cdifa1:datadestruction"
              }
            }
          ],
          "odrl:prohibition": [
            {
              "odrl:target": {
                "@id": "https://example.org/dataset/3936/distribution/csv"
              },
              "odrl:action": {
                "@id": "cdifa1:shareTRECredentials"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix cdifa1: <https://w3id.org/cdif/access/profile1/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/dataset/3936> a schema1:Dataset ;
    schema1:conditionsOfAccess <https://example.org/odrloffer/13adb49c-f641-4ac7-aa90-18651cc211ce>,
        "Users located in the UK may download the data after assenting to the End User Licence." ;
    schema1:distribution <https://example.org/dataset/3936/distribution/csv> ;
    schema1:name "Example restricted-access survey dataset" ;
    schema1:subjectOf [ dcterms:conformsTo <https://w3id.org/cdif/access/1.1> ] .

<https://example.org/odrloffer/13adb49c-f641-4ac7-aa90-18651cc211ce> a odrl:Offer ;
    odrl:assigner ex:repository ;
    odrl:obligation [ odrl:action cdifa1:datadestruction ;
            odrl:target <https://example.org/dataset/3936/distribution/csv> ] ;
    odrl:permission [ odrl:action cdifa1:download ;
            odrl:constraint [ a odrl:Constraint ;
                    odrl:leftOperand odrl:spatial ;
                    odrl:operator odrl:eq ;
                    odrl:rightOperand <http://publications.europa.eu/resource/authority/country/GBR> ] ;
            odrl:duty [ odrl:action cdifa1:assent ;
                    odrl:constraint [ a odrl:Constraint ;
                            odrl:leftOperand odrl:event ;
                            odrl:operator odrl:lt ;
                            odrl:rightOperand odrl:policyUsage ] ] ;
            odrl:target <https://example.org/dataset/3936/distribution/csv> ] ;
    odrl:profile cdifa1:cdifa1.ttl ;
    odrl:prohibition [ odrl:action cdifa1:shareTRECredentials ;
            odrl:target <https://example.org/dataset/3936/distribution/csv> ] .

<https://example.org/dataset/3936/distribution/csv> a schema1:DataDownload ;
    schema1:contentUrl "https://example.org/data/3936/responses.csv" ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "Survey responses (CSV)" ;
    odrl:hasPolicy <https://example.org/odrloffer/13adb49c-f641-4ac7-aa90-18651cc211ce> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Access
description: "Profile module for machine-actionable access and usage conditions, expressed
  as ODRL Offer policies (odrlProperties/odrlOffer). Marks the catalog record as conformant
  to the CDIF access spec and requires at least one policy, attached in either of
  two places:\n- on a schema:distribution item, as odrl:hasPolicy: the preferred place,\n
  \ because distributions of one dataset can carry different conditions\n  (cdifbook
  data_access, \"Connecting CDIF and ODRL\"). The Offer may be\n  inline or an {@id}
  reference.\n\n- on the Dataset, as an {@id} reference in schema:conditionsOfAccess
  to\n  a policy published elsewhere. Only a reference: cdifCore types the\n  items
  of that property as string, {@id} or a CreativeWork link, and an\n  inline Offer
  matches none of them, so it would fail any composite that\n  includes cdifCore.\n\nThis
  module adds constraints only; it does not change cdifCore's schema:distribution
  anyOf [DataDownload, WebAPI]. Draft; OPEN QUESTIONS are marked \"OPEN:\"."
type: object
properties:
  '@context':
    type: object
    description: Additional JSON-LD namespace prefixes for access properties.
    properties:
      odrl:
        const: http://www.w3.org/ns/odrl/2/
      cdifa1:
        const: https://w3id.org/cdif/access/profile1/
      rdf:
        const: http://www.w3.org/1999/02/22-rdf-syntax-ns#
      xsd:
        const: http://www.w3.org/2001/XMLSchema#
  schema:subjectOf:
    properties:
      dcterms:conformsTo:
        description: 'OPEN: https://w3id.org/cdif/access/1.1 is not minted. 1.1 follows
          the other CDIF modules; a new profile might start at 1.0 instead.'
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        minItems: 1
        contains:
          type: object
          required:
          - '@id'
          additionalProperties: false
          properties:
            '@id':
              const: https://w3id.org/cdif/access/1.1
  schema:conditionsOfAccess:
    description: Item shape comes from cdifCore. In a CDIF Access record, an {@id}
      item here should be the uid of an ODRL Offer; JSON Schema cannot tell that reference
      from any other (a SHACL rule would have to).
  schema:distribution:
    type: array
    items:
      properties:
        odrl:hasPolicy:
          description: 'ODRL policies governing access to and use of this distribution.
            OPEN: the book argues against dataset-level policies, so odrl:hasPolicy
            is not declared on the Dataset; confirm.'
          type: array
          minItems: 1
          items:
            anyOf:
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
            - $ref: '#/$defs/odrlOffer'
anyOf:
- required:
  - schema:distribution
  properties:
    schema:distribution:
      contains:
        type: object
        required:
        - odrl:hasPolicy
- required:
  - schema:conditionsOfAccess
  properties:
    schema:conditionsOfAccess:
      contains:
        type: object
        required:
        - '@id'
$defs:
  odrlOffer:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlOffer/schema.yaml
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.profiles.cdifProfile.cdifAccess
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-28'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifAccess/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifAccess/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "cdifa1": "https://w3id.org/cdif/access/profile1/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifAccess/context.jsonld)

## Sources

* [W3C ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifProfile/cdifAccess`

