
# Optional Fields for XAS data (Schema)

`cdif.bbr.metadata.xasProperties.xasOptional` *v0.1*

Optional XAS metadata extending CDIF mandatory with cdifProvActivity-based provenance. Includes XAS subject descriptors, instrument wrappers, XDI-conformant distribution, measurement technique DefinedTerms, and element/edge keywords. Defines properties: schema:subjectOf, prov:wasGeneratedBy, schema:distribution, schema:measurementTechnique, schema:keywords. Uses building blocks: cdifCore (cdifProperties), cdifProvActivity (cdifProperties), definedTerm (schemaorgProperties), additionalProperty (schemaorgProperties), dataDownload (schemaorgProperties), xasSample (xasProperties), cdifCatalogRecord (cdifProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Optional Fields for XAS data

Extends CDIF mandatory metadata with optional XAS-specific properties. Composes cdifCore with cdifProvActivity-based provenance (via xasGeneratedBy pattern), XAS subject descriptors, data distribution with XDI conformance, measurement technique DefinedTerms, and element/edge keywords.

### Key properties

- **schema:subjectOf** — XAS subject descriptors (element, edge)
- **prov:wasGeneratedBy** — cdifProvActivity activity extended with XAS instrument wrappers (source, monochromator with d-spacing/reflection), sample object, and facility
- **schema:distribution** — data download with XDI specification conformance
- **schema:measurementTechnique** — DefinedTerms for XAS technique and measurement mode
- **schema:keywords** — DefinedTerms for absorption edge (XDI dictionary) and target element (SWEET ontology)

## Examples

### Example XAS optional metadata with beamline instrument, measurement technique, and sample.
XAS dataset with NXsource and NXmonochromator instrument components, XAS measurement technique keywords, and sample description.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "prov": "http://www.w3.org/ns/prov#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:xasOptionalExample_001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "XAS measurement of Fe K-edge in magnetite sample",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://doi.org",
    "schema:value": "10.12345/xas-optional-test",
    "schema:url": "https://doi.org/10.12345/xas-optional-test"
  },
  "schema:dateModified": "2026-01-15",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:distribution": [
    {
      "@id": "ex:dist_xdi_001",
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataset"
      ],
      "schema:name": "XDI data file for Fe K-edge magnetite",
      "schema:contentUrl": "https://example.org/data/fe_magnetite_kedge_01.xdi",
      "schema:encodingFormat": [
        "text/plain"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md"
        }
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6"
      }
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:meta_xasOpt_001",
    "schema:about": {
      "@id": "ex:xasOptionalExample_001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/xasDiscovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/xasProperties/xasOptional"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFxas"
      }
    ],
    "schema:maintainer": {
      "@id": "ex:person_jdoe",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Doe, Jane",
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "jane.doe@example.org"
      }
    },
    "schema:sdDatePublished": "2026-01-20T10:00:00Z"
  },
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing",
              "schema:Product"
            ],
            "schema:name": "APS Sector 20-BM beamline instrument",
            "schema:category": [
              {
                "@type": [
                  "schema:DefinedTerm"
                ],
                "schema:name": "X-ray absorption spectroscopy beamline",
                "schema:termCode": "XAS-beamline"
              }
            ],
            "schema:hasPart": [
              {
                "@type": [
                  "schema:Thing",
                  "schema:Product"
                ],
                "schema:additionalType": "nxs:BaseClass/NXsource",
                "schema:name": "APS Undulator A",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXsource/type"
                    ],
                    "schema:name": "x-ray source type",
                    "schema:value": "Synchrotron X-ray Source"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXsource/probe"
                    ],
                    "schema:name": "Probe",
                    "schema:value": "x-ray"
                  }
                ]
              },
              {
                "@type": [
                  "schema:Thing",
                  "schema:Product"
                ],
                "schema:additionalType": "nxs:BaseClass/NXmonochromator",
                "schema:name": "Si 311",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/d_spacing"
                    ],
                    "schema:name": "d-spacing",
                    "schema:value": "1.63747",
                    "schema:unitText": "Angstrom"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/type"
                    ],
                    "schema:name": "crystal type",
                    "schema:value": "channel-cut"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/reflection"
                    ],
                    "schema:name": "reflection plane (hkl)",
                    "schema:value": "3,1,1"
                  }
                ]
              }
            ]
          }
        }
      ],
      "schema:object": {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "MaterialSample",
          "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
        ],
        "schema:name": "Magnetite powder",
        "schema:identifier": "igsn:10.60471/mag-001",
        "schema:description": "Synthetic magnetite powder, 99.5% purity",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "xas:stoichiometry"
            ],
            "schema:name": "Stoichiometry",
            "schema:value": "Fe3O4"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "xas:samplePreparation"
            ],
            "schema:name": "sample preparation method",
            "schema:value": "ground and pressed into pellet with BN diluent"
          }
        ]
      }
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "X-Ray Absorption Spectroscopy",
      "schema:termCode": "XAS",
      "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01196",
      "schema:inDefinedTermSet": "http://purl.org/pan-science/PaNET/PaNET.owl"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Transmission",
      "schema:identifier": "xas:transmissionMode",
      "schema:inDefinedTermSet": "nxs:Field/NXxas/ENTRY/DATA/mode"
    }
  ],
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "K-edge",
      "schema:identifier": "xas:K-edge",
      "schema:termCode": "K",
      "schema:inDefinedTermSet": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Iron",
      "schema:identifier": "http://sweetontology.net/matrElement/Iron",
      "schema:termCode": "Fe",
      "schema:inDefinedTermSet": "http://sweetontology.net/matrElement"
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
      "prov": "http://www.w3.org/ns/prov#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "xas": "https://xas.org/dictionary/",
      "dcat": "http://www.w3.org/ns/dcat#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasOptional/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "spdx": "http://spdx.org/rdf/terms#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "prov": "http://www.w3.org/ns/prov#",
      "xas": "https://xas.org/dictionary/",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:xasOptionalExample_001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "XAS measurement of Fe K-edge in magnetite sample",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://doi.org",
    "schema:value": "10.12345/xas-optional-test",
    "schema:url": "https://doi.org/10.12345/xas-optional-test"
  },
  "schema:dateModified": "2026-01-15",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:distribution": [
    {
      "@id": "ex:dist_xdi_001",
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataset"
      ],
      "schema:name": "XDI data file for Fe K-edge magnetite",
      "schema:contentUrl": "https://example.org/data/fe_magnetite_kedge_01.xdi",
      "schema:encodingFormat": [
        "text/plain"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md"
        }
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6"
      }
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:meta_xasOpt_001",
    "schema:about": {
      "@id": "ex:xasOptionalExample_001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/xasDiscovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/xasProperties/xasOptional"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFxas"
      }
    ],
    "schema:maintainer": {
      "@id": "ex:person_jdoe",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Doe, Jane",
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "jane.doe@example.org"
      }
    },
    "schema:sdDatePublished": "2026-01-20T10:00:00Z"
  },
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing",
              "schema:Product"
            ],
            "schema:name": "APS Sector 20-BM beamline instrument",
            "schema:category": [
              {
                "@type": [
                  "schema:DefinedTerm"
                ],
                "schema:name": "X-ray absorption spectroscopy beamline",
                "schema:termCode": "XAS-beamline"
              }
            ],
            "schema:hasPart": [
              {
                "@type": [
                  "schema:Thing",
                  "schema:Product"
                ],
                "schema:additionalType": "nxs:BaseClass/NXsource",
                "schema:name": "APS Undulator A",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXsource/type"
                    ],
                    "schema:name": "x-ray source type",
                    "schema:value": "Synchrotron X-ray Source"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXsource/probe"
                    ],
                    "schema:name": "Probe",
                    "schema:value": "x-ray"
                  }
                ]
              },
              {
                "@type": [
                  "schema:Thing",
                  "schema:Product"
                ],
                "schema:additionalType": "nxs:BaseClass/NXmonochromator",
                "schema:name": "Si 311",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/d_spacing"
                    ],
                    "schema:name": "d-spacing",
                    "schema:value": "1.63747",
                    "schema:unitText": "Angstrom"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/type"
                    ],
                    "schema:name": "crystal type",
                    "schema:value": "channel-cut"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/reflection"
                    ],
                    "schema:name": "reflection plane (hkl)",
                    "schema:value": "3,1,1"
                  }
                ]
              }
            ]
          }
        }
      ],
      "schema:object": {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "MaterialSample",
          "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
        ],
        "schema:name": "Magnetite powder",
        "schema:identifier": "igsn:10.60471/mag-001",
        "schema:description": "Synthetic magnetite powder, 99.5% purity",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "xas:stoichiometry"
            ],
            "schema:name": "Stoichiometry",
            "schema:value": "Fe3O4"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "xas:samplePreparation"
            ],
            "schema:name": "sample preparation method",
            "schema:value": "ground and pressed into pellet with BN diluent"
          }
        ]
      }
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "X-Ray Absorption Spectroscopy",
      "schema:termCode": "XAS",
      "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01196",
      "schema:inDefinedTermSet": "http://purl.org/pan-science/PaNET/PaNET.owl"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Transmission",
      "schema:identifier": "xas:transmissionMode",
      "schema:inDefinedTermSet": "nxs:Field/NXxas/ENTRY/DATA/mode"
    }
  ],
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "K-edge",
      "schema:identifier": "xas:K-edge",
      "schema:termCode": "K",
      "schema:inDefinedTermSet": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Iron",
      "schema:identifier": "http://sweetontology.net/matrElement/Iron",
      "schema:termCode": "Fe",
      "schema:inDefinedTermSet": "http://sweetontology.net/matrElement"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .

ex:dist_xdi_001 a cdi:PhysicalDataset,
        schema1:DataDownload ;
    dcterms:conformsTo <https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md> ;
    schema1:contentUrl "https://example.org/data/fe_magnetite_kedge_01.xdi" ;
    schema1:encodingFormat "text/plain" ;
    schema1:name "XDI data file for Fe K-edge magnetite" ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "SHA256" ;
            spdx:checksumValue "a1b2c3d4e5f6" ] .

ex:meta_xasOpt_001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFxas>,
        <https://w3id.org/cdif/bbr/metadata/xasProperties/xasOptional>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/>,
        <https://w3id.org/cdif/xasDiscovery/1.0/> ;
    schema1:about ex:xasOptionalExample_001 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:maintainer ex:person_jdoe ;
    schema1:sdDatePublished "2026-01-20T10:00:00Z" .

ex:person_jdoe a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "jane.doe@example.org" ] ;
    schema1:name "Doe, Jane" .

ex:xasOptionalExample_001 a schema1:Dataset,
        schema1:Product ;
    schema1:dateModified "2026-01-15" ;
    schema1:distribution ex:dist_xdi_001 ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://doi.org" ;
            schema1:url "https://doi.org/10.12345/xas-optional-test" ;
            schema1:value "10.12345/xas-optional-test" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier "http://sweetontology.net/matrElement/Iron" ;
            schema1:inDefinedTermSet "http://sweetontology.net/matrElement" ;
            schema1:name "Iron" ;
            schema1:termCode "Fe" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "xas:K-edge" ;
            schema1:inDefinedTermSet "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md" ;
            schema1:name "K-edge" ;
            schema1:termCode "K" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "xas:transmissionMode" ;
            schema1:inDefinedTermSet "nxs:Field/NXxas/ENTRY/DATA/mode" ;
            schema1:name "Transmission" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "http://purl.org/pan-science/PaNET/PaNET01196" ;
            schema1:inDefinedTermSet "http://purl.org/pan-science/PaNET/PaNET.owl" ;
            schema1:name "X-Ray Absorption Spectroscopy" ;
            schema1:termCode "XAS" ] ;
    schema1:name "XAS measurement of Fe K-edge in magnetite sample" ;
    schema1:subjectOf ex:meta_xasOpt_001 ;
    prov:wasGeneratedBy [ schema1:object [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "Stoichiometry" ;
                            schema1:propertyID "xas:stoichiometry" ;
                            schema1:value "Fe3O4" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "sample preparation method" ;
                            schema1:propertyID "xas:samplePreparation" ;
                            schema1:value "ground and pressed into pellet with BN diluent" ] ;
                    schema1:additionalType "MaterialSample",
                        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample" ;
                    schema1:description "Synthetic magnetite powder, 99.5% purity" ;
                    schema1:identifier "igsn:10.60471/mag-001" ;
                    schema1:name "Magnetite powder" ] ;
            prov:used [ schema1:instrument [ a schema1:Product,
                                schema1:Thing ;
                            schema1:category [ a schema1:DefinedTerm ;
                                    schema1:name "X-ray absorption spectroscopy beamline" ;
                                    schema1:termCode "XAS-beamline" ] ;
                            schema1:hasPart [ a schema1:Product,
                                        schema1:Thing ;
                                    schema1:additionalProperty [ a schema1:PropertyValue ;
                                            schema1:name "crystal type" ;
                                            schema1:propertyID "nxs:Field/NXcrystal/type" ;
                                            schema1:value "channel-cut" ],
                                        [ a schema1:PropertyValue ;
                                            schema1:name "d-spacing" ;
                                            schema1:propertyID "nxs:Field/NXcrystal/d_spacing" ;
                                            schema1:unitText "Angstrom" ;
                                            schema1:value "1.63747" ],
                                        [ a schema1:PropertyValue ;
                                            schema1:name "reflection plane (hkl)" ;
                                            schema1:propertyID "nxs:Field/NXcrystal/reflection" ;
                                            schema1:value "3,1,1" ] ;
                                    schema1:additionalType "nxs:BaseClass/NXmonochromator" ;
                                    schema1:name "Si 311" ],
                                [ a schema1:Product,
                                        schema1:Thing ;
                                    schema1:additionalProperty [ a schema1:PropertyValue ;
                                            schema1:name "x-ray source type" ;
                                            schema1:propertyID "nxs:Field/NXsource/type" ;
                                            schema1:value "Synchrotron X-ray Source" ],
                                        [ a schema1:PropertyValue ;
                                            schema1:name "Probe" ;
                                            schema1:propertyID "nxs:Field/NXsource/probe" ;
                                            schema1:value "x-ray" ] ;
                                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                                    schema1:name "APS Undulator A" ] ;
                            schema1:name "APS Sector 20-BM beamline instrument" ] ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: '#/$defs/CdifMandatory'
- type: object
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
                const: https://w3id.org/cdif/xasDiscovery/1.0/
    prov:wasGeneratedBy:
      type: array
      items:
        allOf:
        - $ref: '#/$defs/CdifProvActivity'
        - type: object
          properties:
            prov:used:
              type: array
              description: Array of used entities. Must contain an instrument wrapper
                with schema:hasPart sub-components. The x-ray source type and probe,
                and monochromator properties type, d-spacing and reflection plane
                are required.
              contains:
                type: object
                required:
                - schema:instrument
                properties:
                  schema:instrument:
                    type: object
                    properties:
                      schema:hasPart:
                        type: array
                        minItems: 2
                        allOf:
                        - contains:
                            type: object
                            properties:
                              '@type':
                                type: array
                                items:
                                  type: string
                                minItems: 2
                                allOf:
                                - contains:
                                    const: schema:Thing
                                - contains:
                                    const: schema:Product
                              schema:additionalType:
                                const: nxs:BaseClass/NXsource
                              schema:additionalProperty:
                                type: array
                                minItems: 2
                                items:
                                  $ref: '#/$defs/AdditionalProperty'
                                allOf:
                                - contains:
                                    type: object
                                    properties:
                                      schema:propertyID:
                                        type: array
                                        contains:
                                          const: nxs:Field/NXsource/type
                                      schema:value:
                                        type: string
                                    required:
                                    - schema:propertyID
                                    - schema:value
                                - contains:
                                    type: object
                                    properties:
                                      schema:propertyID:
                                        type: array
                                        contains:
                                          const: nxs:Field/NXsource/probe
                                      schema:name:
                                        const: Probe
                                      schema:value:
                                        type: string
                                    required:
                                    - schema:name
                                    - schema:propertyID
                                    - schema:value
                            required:
                            - '@type'
                            - schema:additionalType
                            - schema:additionalProperty
                        - contains:
                            type: object
                            properties:
                              '@type':
                                type: array
                                items:
                                  type: string
                                minItems: 2
                                allOf:
                                - contains:
                                    const: schema:Thing
                                - contains:
                                    const: schema:Product
                              schema:additionalType:
                                const: nxs:BaseClass/NXmonochromator
                              schema:name:
                                type: string
                              schema:additionalProperty:
                                description: Require additional properties for monochromator,
                                  requires d-space, crystal type, reflection plane.
                                type: array
                                minItems: 3
                                items:
                                  $ref: '#/$defs/AdditionalProperty'
                                contains:
                                  type: object
                                  properties:
                                    schema:propertyID:
                                      type: array
                                      contains:
                                        const: nxs:Field/NXcrystal/type
                                    schema:value:
                                      type: string
                                  required:
                                  - schema:value
                                  - schema:propertyID
                                allOf:
                                - contains:
                                    type: object
                                    properties:
                                      schema:propertyID:
                                        type: array
                                        contains:
                                          const: nxs:Field/NXcrystal/d_spacing
                                      schema:value:
                                        type: string
                                      schema:unitText:
                                        type: string
                                    required:
                                    - schema:propertyID
                                    - schema:value
                                    - schema:unitText
                                - contains:
                                    type: object
                                    properties:
                                      schema:propertyID:
                                        type: array
                                        contains:
                                          const: nxs:Field/NXcrystal/reflection
                                      schema:value:
                                        type: string
                                    required:
                                    - schema:value
                                    - schema:propertyID
                            required:
                            - '@type'
                            - schema:additionalType
                            - schema:additionalProperty
                    required:
                    - schema:hasPart
            schema:object:
              $ref: '#/$defs/XasSample'
    schema:distribution:
      type: array
      items:
        $ref: '#/$defs/DataDownload'
      contains:
        type: object
        properties:
          '@type':
            type: array
            items:
              type: string
            minItems: 2
            allOf:
            - contains:
                const: schema:DataDownload
            - contains:
                enum:
                - cdi:PhysicalDataset
                - cdi:TabularTextDataSet
                - cdi:StructuredDataSet
          dcterms:conformsTo:
            type: array
            contains:
              type: object
              properties:
                '@id':
                  const: https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md
              required:
              - '@id'
        required:
        - '@type'
        - dcterms:conformsTo
    schema:measurementTechnique:
      type: array
      description: 'Require DefinedTerms for both: absorption edge (XDI dict) and
        target element (SWEET).'
      minItems: 2
      items:
        $ref: '#/$defs/DefinedTerm'
      allOf:
      - contains:
          type: object
          properties:
            schema:name:
              const: X-Ray Absorption Spectroscopy
            schema:termCode:
              const: XAS
            schema:identifier:
              const: http://purl.org/pan-science/PaNET/PaNET01196
            schema:inDefinedTermSet:
              const: http://purl.org/pan-science/PaNET/PaNET.owl
          required:
          - schema:name
          - schema:termCode
          - schema:identifier
          - schema:inDefinedTermSet
      - contains:
          type: object
          properties:
            schema:name:
              type: string
            schema:inDefinedTermSet:
              const: nxs:Field/NXxas/ENTRY/DATA/mode
          required:
          - schema:name
          - schema:inDefinedTermSet
    schema:keywords:
      type: array
      description: extends base CDIF keyword schema to require defined terms for the
        absorption edge and the target element for the analysis
      minItems: 2
      items:
        type: object
        properties:
          '@type':
            type: array
            items:
              type: string
            contains:
              const: schema:DefinedTerm
            minItems: 1
          schema:name:
            type: string
          schema:identifier:
            type: string
          schema:inDefinedTermSet:
            type: string
            description: need to include this to tag what the keyword is about; we're
              using the keywords as soft-typed properties
        required:
        - '@type'
        - schema:name
        - schema:inDefinedTermSet
        additionalProperties: true
      allOf:
      - contains:
          type: object
          properties:
            schema:inDefinedTermSet:
              const: https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md
          required:
          - schema:inDefinedTermSet
      - contains:
          type: object
          properties:
            schema:inDefinedTermSet:
              const: http://sweetontology.net/matrElement
          required:
          - schema:inDefinedTermSet
$defs:
  CdifMandatory:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCore/schema.yaml
  CdifProvActivity:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvActivity/schema.yaml
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  AdditionalProperty:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
  DataDownload:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.yaml
  XasSample:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasSample/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasOptional/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasOptional/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasOptional/context.jsonld)

## Sources

* [CDIF-4-XAS OSCARS Project](https://doi.org/10.5281/zenodo.17421917)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/xasProperties/xasOptional`

