
# CDIF Provenance (Schema)

`cdif.bbr.metadata.cdifProperties.cdifProvenance` *v0.1*

Defines the prov:wasGeneratedBy property for CDIF metadata records. Wraps the cdifProvActivity building block as an array of provenance activities describing how the resource was generated.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Provenance

Defines the `prov:wasGeneratedBy` property for CDIF metadata records. This building block wraps the cdifProvActivity building block as an array of provenance activities.

### Defined properties

- **prov:wasGeneratedBy** - array of provenance activities describing how the described resource was generated

### Dependencies

- [cdifProvActivity](../cdifProvActivity/) - extended provenance activity with schema.org Action properties

## Examples

### Example CDIF Provenance record
Example dataset with provenance activity describing how the resource was generated.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "ex": "https://example.org/"
  },
  "@id": "ex:dataset_with_provenance_001",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Processed Seismic Survey Data",
  "schema:identifier": "https://doi.org/10.1234/seismic-2025",
  "schema:url": "https://example.org/datasets/seismic-2025",
  "schema:dateModified": "2025-06-15",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:metadata_provenance_001",
    "schema:about": {
      "@id": "ex:dataset_with_provenance_001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/provenance/1.0/"
      }
    ]
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:name": "Seismic data processing",
      "schema:description": "Raw seismic traces were processed using standard reflection seismology workflow including deconvolution, stacking, and migration.",
      "schema:agent": {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Garcia, Maria",
        "schema:identifier": "https://orcid.org/0000-0003-1234-5678",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "m.garcia@example.org"
        }
      },
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "SeisUnix",
            "schema:version": "44R27",
            "schema:url": "https://wiki.seismic-unix.org/",
            "schema:category": [
              {
                "@type": [
                  "schema:DefinedTerm"
                ],
                "schema:name": "Seismic processing software",
                "schema:termCode": "seismic-processing"
              }
            ]
          }
        }
      ],
      "schema:startTime": "2025-01-10T00:00:00Z",
      "schema:endTime": "2025-03-20T00:00:00Z",
      "schema:actionStatus": "schema:CompletedActionStatus"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvenance/context.jsonld",
    {
      "schema": "http://schema.org/",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:dataset_with_provenance_001",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Processed Seismic Survey Data",
  "schema:identifier": "https://doi.org/10.1234/seismic-2025",
  "schema:url": "https://example.org/datasets/seismic-2025",
  "schema:dateModified": "2025-06-15",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:metadata_provenance_001",
    "schema:about": {
      "@id": "ex:dataset_with_provenance_001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/provenance/1.0/"
      }
    ]
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:name": "Seismic data processing",
      "schema:description": "Raw seismic traces were processed using standard reflection seismology workflow including deconvolution, stacking, and migration.",
      "schema:agent": {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Garcia, Maria",
        "schema:identifier": "https://orcid.org/0000-0003-1234-5678",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "m.garcia@example.org"
        }
      },
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "SeisUnix",
            "schema:version": "44R27",
            "schema:url": "https://wiki.seismic-unix.org/",
            "schema:category": [
              {
                "@type": [
                  "schema:DefinedTerm"
                ],
                "schema:name": "Seismic processing software",
                "schema:termCode": "seismic-processing"
              }
            ]
          }
        }
      ],
      "schema:startTime": "2025-01-10T00:00:00Z",
      "schema:endTime": "2025-03-20T00:00:00Z",
      "schema:actionStatus": "schema:CompletedActionStatus"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .

ex:dataset_with_provenance_001 a schema1:Dataset ;
    schema1:dateModified "2025-06-15" ;
    schema1:identifier "https://doi.org/10.1234/seismic-2025" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:name "Processed Seismic Survey Data" ;
    schema1:subjectOf ex:metadata_provenance_001 ;
    schema1:url "https://example.org/datasets/seismic-2025" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:actionStatus "schema:CompletedActionStatus" ;
            schema1:agent [ a schema1:Person ;
                    schema1:contactPoint [ a schema1:ContactPoint ;
                            schema1:email "m.garcia@example.org" ] ;
                    schema1:identifier "https://orcid.org/0000-0003-1234-5678" ;
                    schema1:name "Garcia, Maria" ] ;
            schema1:description "Raw seismic traces were processed using standard reflection seismology workflow including deconvolution, stacking, and migration." ;
            schema1:endTime "2025-03-20T00:00:00Z" ;
            schema1:name "Seismic data processing" ;
            schema1:startTime "2025-01-10T00:00:00Z" ;
            prov:used [ schema1:instrument [ a schema1:SoftwareApplication ;
                            schema1:category [ a schema1:DefinedTerm ;
                                    schema1:name "Seismic processing software" ;
                                    schema1:termCode "seismic-processing" ] ;
                            schema1:name "SeisUnix" ;
                            schema1:url "https://wiki.seismic-unix.org/" ;
                            schema1:version "44R27" ] ] ] .

ex:metadata_provenance_001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/provenance/1.0/> ;
    schema1:about ex:dataset_with_provenance_001 ;
    schema1:additionalType "dcat:CatalogRecord" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Provenance
description: Building block that defines the prov:wasGeneratedBy property for CDIF
  metadata records. Wraps the cdifProvActivity building block as an array of provenance
  activities that describe how the described resource was generated.
type: object
properties:
  schema:subjectOf:
    properties:
      dcterms:conformsTo:
        type: array
        items:
          type: object
          properties:
            '@id':
              type: string
              description: uri for specifications that this metadata record conforms
                to
        minItems: 1
        contains:
          type: object
          properties:
            '@id':
              const: https://w3id.org/cdif/provenance/1.0/
  prov:wasGeneratedBy:
    description: Provenance activities describing how the resource was generated,
      including agents, instruments, methodology, temporal bounds, and action chaining.
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvActivity/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvenance/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvenance/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvenance/context.jsonld)

## Sources

* [W3C PROV-O](https://www.w3.org/TR/prov-o/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifProvenance`

