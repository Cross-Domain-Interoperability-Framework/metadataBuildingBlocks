
# XAS Core metadata properties (Schema)

`cdif.bbr.metadata.xasProperties.xasCore` *v1.0*

Required XAS metadata constraints layered on cdifCore (composed once by the xasDocument profile). Requires schema:Dataset in @type (schema:Product optional -- no root-level property depends on it), a required prov:wasGeneratedBy analysis activity whose prov:used carries the instrument wrapper (NXsource + NXmonochromator sub-components with required type/probe/d_spacing/reflection), an XDI-conformant schema:distribution, required XAS measurementTechnique DefinedTerms, required element/edge keywords, and the schema:object material sample. Defines properties: @type, schema:subjectOf, prov:wasGeneratedBy, schema:distribution, schema:measurementTechnique, schema:keywords. Uses building blocks: cdifProvActivity (cdifDataType), definedTerm (schemaorgProperties), additionalProperty (schemaorgProperties), dataDownload (schemaorgProperties), xasSample (xasProperties).

[*Status*](http://www.opengis.net/def/status): Stable

## Description

## Required Fields for XAS data

Extends CDIF mandatory metadata with required XAS-specific properties. Same structure as xasOptional but adds `@type` constraints (requires `schema:Dataset`; `schema:Product` optional) and stricter cardinality requirements on instrument components, measurement techniques, and keywords.

### Key requirements

- **@type** — must include `schema:Dataset`; `schema:Product` is optional (no root-level property depends on it)
- **schema:subjectOf** — XAS subject descriptors (element, edge)
- **prov:wasGeneratedBy** — cdifProvActivity activity requiring XAS instruments with NXsource (type, probe) and NXmonochromator (type, d_spacing, reflection) components, plus sample object
- **schema:distribution** — requires at least one DataDownload typed as `cdi:PhysicalDataSet` conforming to the XDI specification
- **schema:measurementTechnique** — requires DefinedTerms for XAS (PaNET) and measurement mode (NXxas)
- **schema:keywords** — requires DefinedTerms from both the XDI dictionary (absorption edge) and SWEET ontology (target element)

## Examples

### Example XAS core metadata with required items.
XAS core properties: instrument components, XDI distribution, measurement techniques, keywords.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "xas": "https://w3id.org/cdif/xas/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:xas-dataset-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "Se K-edge XANES of Na2SeO4 reference compound",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://doi.org"
    },
    "schema:value": "10.12345/xas.2024.001",
    "schema:url": "http://example.com/resource?foo=bar#fragment"
  },
  "schema:dateModified": "2025-06-15",
  "schema:conditionsOfAccess": [
    "Public access, no restrictions"
  ],
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:url": "http://example.com/resource?foo=bar#fragment",
  "schema:distribution": [
    {
      "@id": "lMtIx",
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "XDI data file",
      "schema:contentUrl": "http://example.com/resource/35uj46j",
      "schema:encodingFormat": [
        "application/x-xdi"
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
        "spdx:algorithm": "SHA-256",
        "spdx:checksumValue": "a1b2c3d4e5f6..."
      },
      "schema:provider": [
        {
          "@id": "https://ror.org/04qxsr837",
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Advanced Photon Source",
          "schema:url": "https://www.aps.anl.gov"
        }
      ]
    },
    {
      "@id": "RNdlTIf",
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Processed spectrum CSV",
      "schema:contentUrl": "http://example.com/resource/34h5ykl",
      "schema:encodingFormat": [
        "text/csv",
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "MD5",
        "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e"
      },
      "schema:provider": [
        {
          "@id": "https://ror.org/04qxsr837",
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Advanced Photon Source",
          "schema:url": "https://www.aps.anl.gov"
        }
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "urn:uuid:xas-required-catalog-record",
    "schema:about": {
      "@id": "ex:xas-dataset-001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/xasCore/1.0"
      }
    ],
    "schema:maintainer": {
      "@id": "nKwywfsuBh",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Cataloger, Example Data",
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "cataloger@example.org"
      }
    },
    "schema:sdDatePublished": "2025-08-15T06:45:40Z",
    "schema:includedInDataCatalog": {
      "@id": "nbUunSyw",
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "XAS Data Library",
      "schema:url": "http://example.com/resource?foo=bar#fragment"
    }
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "schema:Action",
        "prov:Activity"
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "@type": [
                "schema:Thing",
                "schema:Product",
                "prov:Entity"
              ],
              "schema:additionalType": [
                {
                  "@id": "xas:beamline"
                },
                {
                  "@id": "wd:Q3099911"
                }
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
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "@type": [
                "schema:Thing",
                "schema:Product",
                "prov:Entity"
              ],
              "schema:additionalType": [
                {
                  "@id": "xas:source"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "APS bending magnet source",
              "schema:additionalProperty": [
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:xraysourcetype"
                    }
                  ],
                  "schema:name": "x-ray source",
                  "schema:value": "Synchrotron X-ray Source"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:probe"
                    }
                  ],
                  "schema:name": "Probe",
                  "schema:value": "x-ray"
                }
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "@type": [
                "schema:Thing",
                "schema:Product",
                "prov:Entity"
              ],
              "schema:additionalType": [
                {
                  "@id": "xas:xraymonochromator"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "Si 111",
              "schema:additionalProperty": [
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:dspacing"
                    }
                  ],
                  "schema:name": "d-spacing",
                  "schema:value": "3.13550",
                  "schema:unitText": "Angstrom"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:monochromatortype"
                    }
                  ],
                  "schema:name": "crystal type",
                  "schema:value": "Si(111)"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:reflectionplane"
                    }
                  ],
                  "schema:name": "reflection plane (hkl)",
                  "schema:value": "1,1,1"
                }
              ]
            }
          ]
        }
      ],
      "schema:object": {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "MaterialSample",
          {
            "@id": "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          }
        ],
        "schema:name": "Na2SeO4",
        "schema:identifier": "igsn:10.6620/se-selenate-001",
        "schema:description": "Sodium selenate reference compound, powder",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "https://w3id.org/cdif/xas/samplepreparation"
              }
            ],
            "schema:name": "sample preparation method",
            "schema:value": "powder on tape, 6 layers"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplechemicalcomposition"
              }
            ],
            "schema:name": "Stoichiometry",
            "schema:value": "Na2SeO4"
          }
        ]
      },
      "schema:additionalType": [
        {
          "@id": "xas:analysisevent"
        }
      ]
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
      "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01188",
      "schema:inDefinedTermSet": "nxs:Field/NXxas/ENTRY/DATA/mode"
    }
  ],
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "K-edge",
      "schema:identifier": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md#K",
      "schema:termCode": "K",
      "schema:inDefinedTermSet": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md",
      "schema:about": "element.edge"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Selenium",
      "schema:identifier": "http://sweetontology.net/matrElement/Selenium",
      "schema:termCode": "Se",
      "schema:inDefinedTermSet": "http://sweetontology.net/matrElement",
      "schema:about": "element.symbol"
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
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "nxs": "https://manual.nexusformat.org/classes/",
      "xas": "https://w3id.org/cdif/xas/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasCore/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "spdx": "http://spdx.org/rdf/terms#",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "xas": "https://w3id.org/cdif/xas/",
      "nxs": "https://manual.nexusformat.org/classes/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:xas-dataset-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "Se K-edge XANES of Na2SeO4 reference compound",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://doi.org"
    },
    "schema:value": "10.12345/xas.2024.001",
    "schema:url": "http://example.com/resource?foo=bar#fragment"
  },
  "schema:dateModified": "2025-06-15",
  "schema:conditionsOfAccess": [
    "Public access, no restrictions"
  ],
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:url": "http://example.com/resource?foo=bar#fragment",
  "schema:distribution": [
    {
      "@id": "lMtIx",
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "XDI data file",
      "schema:contentUrl": "http://example.com/resource/35uj46j",
      "schema:encodingFormat": [
        "application/x-xdi"
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
        "spdx:algorithm": "SHA-256",
        "spdx:checksumValue": "a1b2c3d4e5f6..."
      },
      "schema:provider": [
        {
          "@id": "https://ror.org/04qxsr837",
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Advanced Photon Source",
          "schema:url": "https://www.aps.anl.gov"
        }
      ]
    },
    {
      "@id": "RNdlTIf",
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Processed spectrum CSV",
      "schema:contentUrl": "http://example.com/resource/34h5ykl",
      "schema:encodingFormat": [
        "text/csv",
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "MD5",
        "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e"
      },
      "schema:provider": [
        {
          "@id": "https://ror.org/04qxsr837",
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Advanced Photon Source",
          "schema:url": "https://www.aps.anl.gov"
        }
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "urn:uuid:xas-required-catalog-record",
    "schema:about": {
      "@id": "ex:xas-dataset-001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/xasCore/1.0"
      }
    ],
    "schema:maintainer": {
      "@id": "nKwywfsuBh",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Cataloger, Example Data",
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "cataloger@example.org"
      }
    },
    "schema:sdDatePublished": "2025-08-15T06:45:40Z",
    "schema:includedInDataCatalog": {
      "@id": "nbUunSyw",
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "XAS Data Library",
      "schema:url": "http://example.com/resource?foo=bar#fragment"
    }
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "schema:Action",
        "prov:Activity"
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "@type": [
                "schema:Thing",
                "schema:Product",
                "prov:Entity"
              ],
              "schema:additionalType": [
                {
                  "@id": "xas:beamline"
                },
                {
                  "@id": "wd:Q3099911"
                }
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
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "@type": [
                "schema:Thing",
                "schema:Product",
                "prov:Entity"
              ],
              "schema:additionalType": [
                {
                  "@id": "xas:source"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "APS bending magnet source",
              "schema:additionalProperty": [
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:xraysourcetype"
                    }
                  ],
                  "schema:name": "x-ray source",
                  "schema:value": "Synchrotron X-ray Source"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:probe"
                    }
                  ],
                  "schema:name": "Probe",
                  "schema:value": "x-ray"
                }
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "@type": [
                "schema:Thing",
                "schema:Product",
                "prov:Entity"
              ],
              "schema:additionalType": [
                {
                  "@id": "xas:xraymonochromator"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "Si 111",
              "schema:additionalProperty": [
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:dspacing"
                    }
                  ],
                  "schema:name": "d-spacing",
                  "schema:value": "3.13550",
                  "schema:unitText": "Angstrom"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:monochromatortype"
                    }
                  ],
                  "schema:name": "crystal type",
                  "schema:value": "Si(111)"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:reflectionplane"
                    }
                  ],
                  "schema:name": "reflection plane (hkl)",
                  "schema:value": "1,1,1"
                }
              ]
            }
          ]
        }
      ],
      "schema:object": {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "MaterialSample",
          {
            "@id": "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          }
        ],
        "schema:name": "Na2SeO4",
        "schema:identifier": "igsn:10.6620/se-selenate-001",
        "schema:description": "Sodium selenate reference compound, powder",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "https://w3id.org/cdif/xas/samplepreparation"
              }
            ],
            "schema:name": "sample preparation method",
            "schema:value": "powder on tape, 6 layers"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplechemicalcomposition"
              }
            ],
            "schema:name": "Stoichiometry",
            "schema:value": "Na2SeO4"
          }
        ]
      },
      "schema:additionalType": [
        {
          "@id": "xas:analysisevent"
        }
      ]
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
      "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01188",
      "schema:inDefinedTermSet": "nxs:Field/NXxas/ENTRY/DATA/mode"
    }
  ],
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "K-edge",
      "schema:identifier": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md#K",
      "schema:termCode": "K",
      "schema:inDefinedTermSet": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md",
      "schema:about": "element.edge"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Selenium",
      "schema:identifier": "http://sweetontology.net/matrElement/Selenium",
      "schema:termCode": "Se",
      "schema:inDefinedTermSet": "http://sweetontology.net/matrElement",
      "schema:about": "element.symbol"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xas: <https://w3id.org/cdif/xas/> .

<file:///github/workspace/RNdlTIf> a schema1:DataDownload ;
    dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
    schema1:contentUrl "http://example.com/resource/34h5ykl" ;
    schema1:encodingFormat "application/zip",
        "text/csv" ;
    schema1:name "Processed spectrum CSV" ;
    schema1:provider <https://ror.org/04qxsr837> ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "MD5" ;
            spdx:checksumValue "d41d8cd98f00b204e9800998ecf8427e" ] .

<file:///github/workspace/lMtIx> a cdi:PhysicalDataSet,
        schema1:DataDownload ;
    dcterms:conformsTo <https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md> ;
    schema1:contentUrl "http://example.com/resource/35uj46j" ;
    schema1:encodingFormat "application/x-xdi" ;
    schema1:name "XDI data file" ;
    schema1:provider <https://ror.org/04qxsr837> ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "SHA-256" ;
            spdx:checksumValue "a1b2c3d4e5f6..." ] .

<file:///github/workspace/nKwywfsuBh> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "cataloger@example.org" ] ;
    schema1:name "Cataloger, Example Data" .

<file:///github/workspace/nbUunSyw> a schema1:DataCatalog ;
    schema1:name "XAS Data Library" ;
    schema1:url "http://example.com/resource?foo=bar#fragment" .

ex:xas-dataset-001 a schema1:Dataset,
        schema1:Product ;
    schema1:conditionsOfAccess "Public access, no restrictions" ;
    schema1:dateModified "2025-06-15" ;
    schema1:distribution <file:///github/workspace/RNdlTIf>,
        <file:///github/workspace/lMtIx> ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID <https://doi.org> ;
            schema1:url "http://example.com/resource?foo=bar#fragment" ;
            schema1:value "10.12345/xas.2024.001" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:about "element.edge" ;
            schema1:identifier "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md#K" ;
            schema1:inDefinedTermSet "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md" ;
            schema1:name "K-edge" ;
            schema1:termCode "K" ],
        [ a schema1:DefinedTerm ;
            schema1:about "element.symbol" ;
            schema1:identifier "http://sweetontology.net/matrElement/Selenium" ;
            schema1:inDefinedTermSet "http://sweetontology.net/matrElement" ;
            schema1:name "Selenium" ;
            schema1:termCode "Se" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "http://purl.org/pan-science/PaNET/PaNET01188" ;
            schema1:inDefinedTermSet "nxs:Field/NXxas/ENTRY/DATA/mode" ;
            schema1:name "Transmission" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "http://purl.org/pan-science/PaNET/PaNET01196" ;
            schema1:inDefinedTermSet "http://purl.org/pan-science/PaNET/PaNET.owl" ;
            schema1:name "X-Ray Absorption Spectroscopy" ;
            schema1:termCode "XAS" ] ;
    schema1:name "Se K-edge XANES of Na2SeO4 reference compound" ;
    schema1:subjectOf <urn:uuid:xas-required-catalog-record> ;
    schema1:url "http://example.com/resource?foo=bar#fragment" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:additionalType xas:analysisevent ;
            schema1:object [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "sample preparation method" ;
                            schema1:propertyID xas:samplepreparation ;
                            schema1:value "powder on tape, 6 layers" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Stoichiometry" ;
                            schema1:propertyID xas:samplechemicalcomposition ;
                            schema1:value "Na2SeO4" ] ;
                    schema1:additionalType <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample>,
                        "MaterialSample" ;
                    schema1:description "Sodium selenate reference compound, powder" ;
                    schema1:identifier "igsn:10.6620/se-selenate-001" ;
                    schema1:name "Na2SeO4" ] ;
            prov:used [ schema1:instrument [ a schema1:Product,
                                schema1:Thing,
                                prov:Entity ;
                            schema1:additionalType xas:beamline,
                                wd:Q3099911 ;
                            schema1:category [ a schema1:DefinedTerm ;
                                    schema1:name "X-ray absorption spectroscopy beamline" ;
                                    schema1:termCode "XAS-beamline" ] ;
                            schema1:name "APS Sector 20-BM beamline instrument" ] ],
                [ schema1:instrument [ a schema1:Product,
                                schema1:Thing,
                                prov:Entity ;
                            schema1:additionalProperty [ a schema1:PropertyValue ;
                                    schema1:name "crystal type" ;
                                    schema1:propertyID xas:monochromatortype ;
                                    schema1:value "Si(111)" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "reflection plane (hkl)" ;
                                    schema1:propertyID xas:reflectionplane ;
                                    schema1:value "1,1,1" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "d-spacing" ;
                                    schema1:propertyID xas:dspacing ;
                                    schema1:unitText "Angstrom" ;
                                    schema1:value "3.13550" ] ;
                            schema1:additionalType xas:xraymonochromator,
                                wd:Q3099911 ;
                            schema1:name "Si 111" ] ],
                [ schema1:instrument [ a schema1:Product,
                                schema1:Thing,
                                prov:Entity ;
                            schema1:additionalProperty [ a schema1:PropertyValue ;
                                    schema1:name "Probe" ;
                                    schema1:propertyID xas:probe ;
                                    schema1:value "x-ray" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "x-ray source" ;
                                    schema1:propertyID xas:xraysourcetype ;
                                    schema1:value "Synchrotron X-ray Source" ] ;
                            schema1:additionalType xas:source,
                                wd:Q3099911 ;
                            schema1:name "APS bending magnet source" ] ] ] .

<urn:uuid:xas-required-catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/discovery/1.1>,
        <https://w3id.org/cdif/xasCore/1.0> ;
    schema1:about ex:xas-dataset-001 ;
    schema1:additionalType dcat:CatalogRecord ;
    schema1:includedInDataCatalog <file:///github/workspace/nbUunSyw> ;
    schema1:maintainer <file:///github/workspace/nKwywfsuBh> ;
    schema1:sdDatePublished "2025-08-15T06:45:40Z" .

<https://ror.org/04qxsr837> a schema1:Organization ;
    schema1:name "Advanced Photon Source" ;
    schema1:url "https://www.aps.anl.gov" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: XAS Core (required) metadata constraints
description: Required XAS constraints layered on cdifCore (composed once by the xasDocument
  profile; this module does NOT re-embed cdifCore). Enforces dual @type (Dataset+Product),
  a prov:wasGeneratedBy analysis activity whose prov:used carries the NXsource+NXmonochromator
  instrument wrapper, an XDI-conformant distribution, required XAS measurementTechnique
  DefinedTerms, required element/edge keywords, and the schema:object material sample.
type: object
properties:
  '@type':
    description: Dataset @type MUST include schema:Dataset. schema:Product MAY also
      be included (to treat the dataset as a data product) but is not required; no
      root-level property depends on the Product type.
    type: array
    items:
      type: string
      enum:
      - schema:Dataset
      - schema:Product
    minItems: 1
    contains:
      const: schema:Dataset
  schema:subjectOf:
    properties:
      dcterms:conformsTo:
        type: array
        items:
          type: object
          required:
          - '@id'
          additionalProperties: false
          properties:
            '@id':
              type: string
              description: uri for specifications that this metadata record conforms
                to
        minItems: 1
        contains:
          type: object
          required:
          - '@id'
          additionalProperties: false
          properties:
            '@id':
              const: https://w3id.org/cdif/xasCore/1.0
        x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-id: http://schema.org/subjectOf
  prov:wasGeneratedBy:
    type: array
    items:
      allOf:
      - $ref: '#/$defs/CdifProvActivity'
      - type: object
        properties:
          prov:used:
            type: array
            description: Array of instrument-wrapper entries used by the analysis.
              Under the peer prov:used model each instrument (source, beamline, monochromator,
              monitor, ...) is its own top-level wrapper differentiated by schema:instrument.schema:additionalType.
              An x-ray source (with type and probe properties) and a monochromator
              (with crystal type, d_spacing, and reflection plane properties) are
              required here; xas:beamline and the monochromator d_spacing schema:value
              are additionally required by xasGeneratedBy.
            allOf:
            - description: Must contain a peer wrapper whose schema:instrument is
                classified as xas:source and carries schema:additionalProperty entries
                for xas:xraysourcetype and xas:probe (each with a schema:value; the
                probe entry is also named "Probe").
              contains:
                type: object
                required:
                - schema:instrument
                properties:
                  schema:instrument:
                    type: array
                    contains:
                      type: object
                      required:
                      - schema:additionalType
                      - schema:additionalProperty
                      properties:
                        schema:additionalType:
                          anyOf:
                          - type: object
                            additionalProperties: false
                            required:
                            - '@id'
                            properties:
                              '@id':
                                const: xas:source
                          - type: array
                            contains:
                              type: object
                              additionalProperties: false
                              required:
                              - '@id'
                              properties:
                                '@id':
                                  const: xas:source
                        schema:additionalProperty:
                          type: array
                          minItems: 2
                          items:
                            $ref: '#/$defs/AdditionalProperty'
                          allOf:
                          - contains:
                              type: object
                              required:
                              - schema:propertyID
                              - schema:value
                              properties:
                                schema:propertyID:
                                  type: array
                                  contains:
                                    type: object
                                    additionalProperties: false
                                    required:
                                    - '@id'
                                    properties:
                                      '@id':
                                        const: xas:xraysourcetype
                                schema:value:
                                  type: string
                          - contains:
                              type: object
                              required:
                              - schema:name
                              - schema:propertyID
                              - schema:value
                              properties:
                                schema:propertyID:
                                  type: array
                                  contains:
                                    type: object
                                    additionalProperties: false
                                    required:
                                    - '@id'
                                    properties:
                                      '@id':
                                        const: xas:probe
                                schema:name:
                                  const: Probe
                                schema:value:
                                  type: string
            - description: Must contain a peer wrapper whose schema:instrument is
                classified as xas:xraymonochromator, has a schema:name, and carries
                schema:additionalProperty entries for xas:monochromatortype, xas:dspacing
                (with value + unitText), and xas:reflectionplane.
              contains:
                type: object
                required:
                - schema:instrument
                properties:
                  schema:instrument:
                    type: array
                    contains:
                      type: object
                      required:
                      - schema:additionalType
                      - schema:name
                      - schema:additionalProperty
                      properties:
                        schema:additionalType:
                          anyOf:
                          - type: object
                            additionalProperties: false
                            required:
                            - '@id'
                            properties:
                              '@id':
                                const: xas:xraymonochromator
                          - type: array
                            contains:
                              type: object
                              additionalProperties: false
                              required:
                              - '@id'
                              properties:
                                '@id':
                                  const: xas:xraymonochromator
                        schema:name:
                          type: string
                        schema:additionalProperty:
                          description: Require crystal type, d_spacing (with unitText),
                            and reflection plane properties.
                          type: array
                          minItems: 3
                          items:
                            $ref: '#/$defs/AdditionalProperty'
                          allOf:
                          - contains:
                              type: object
                              required:
                              - schema:propertyID
                              - schema:value
                              properties:
                                schema:propertyID:
                                  type: array
                                  contains:
                                    type: object
                                    additionalProperties: false
                                    required:
                                    - '@id'
                                    properties:
                                      '@id':
                                        const: xas:monochromatortype
                                schema:value:
                                  type: string
                          - contains:
                              type: object
                              required:
                              - schema:propertyID
                              - schema:value
                              - schema:unitText
                              properties:
                                schema:propertyID:
                                  type: array
                                  contains:
                                    type: object
                                    additionalProperties: false
                                    required:
                                    - '@id'
                                    properties:
                                      '@id':
                                        const: xas:dspacing
                                schema:value:
                                  type: string
                                schema:unitText:
                                  type: string
                          - contains:
                              type: object
                              required:
                              - schema:propertyID
                              - schema:value
                              properties:
                                schema:propertyID:
                                  type: array
                                  contains:
                                    type: object
                                    additionalProperties: false
                                    required:
                                    - '@id'
                                    properties:
                                      '@id':
                                        const: xas:reflectionplane
                                schema:value:
                                  type: string
            x-jsonld-id: http://www.w3.org/ns/prov#used
          schema:object:
            $ref: '#/$defs/XasSample'
            x-jsonld-id: http://schema.org/object
    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
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
              - cdi:PhysicalDataSet
              - cdi:TabularTextDataSet
              - cdi:StructuredDataSet
        dcterms:conformsTo:
          type: array
          description: The distribution must declare the format specification its
            bytes follow. XDI and NeXus are the two serializations of XAS data in
            scope, so either satisfies this. The '@type' constraint above is already
            format-neutral (tabular text or structured binary); requiring the XDI
            specification here contradicted it and made a conforming NeXus/HDF5 distribution
            impossible to describe.
          contains:
            type: object
            additionalProperties: false
            properties:
              '@id':
                anyOf:
                - description: The XDI specification.
                  const: https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md
                - description: 'A NeXus application definition, compact form, as emitted
                    with the nxs: prefix bound to https://manual.nexusformat.org/classes/.'
                  type: string
                  pattern: ^nxs:applications/NX[A-Za-z0-9_]+\.html$
                - description: A NeXus application definition, full form.
                  type: string
                  pattern: ^https://manual\.nexusformat\.org/classes/applications/NX[A-Za-z0-9_]+\.html$
            required:
            - '@id'
          x-jsonld-id: http://purl.org/dc/terms/conformsTo
      required:
      - '@type'
      - dcterms:conformsTo
    x-jsonld-id: http://schema.org/distribution
  schema:measurementTechnique:
    type: array
    description: 'Require DefinedTerms for both: absorption edge (XDI dict) and target
      element (SWEET).'
    minItems: 2
    items:
      $ref: '#/$defs/DefinedTerm'
    contains:
      type: object
      properties:
        schema:name:
          const: X-Ray Absorption Spectroscopy
          x-jsonld-id: http://schema.org/name
        schema:termCode:
          const: XAS
          x-jsonld-id: http://schema.org/termCode
        schema:identifier:
          const: http://purl.org/pan-science/PaNET/PaNET01196
          x-jsonld-id: http://schema.org/identifier
        schema:inDefinedTermSet:
          const: http://purl.org/pan-science/PaNET/PaNET.owl
          x-jsonld-id: http://schema.org/inDefinedTermSet
      required:
      - schema:name
      - schema:termCode
      - schema:identifier
      - schema:inDefinedTermSet
    allOf:
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
    x-jsonld-id: http://schema.org/measurementTechnique
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
          x-jsonld-id: http://schema.org/name
        schema:identifier:
          type: string
          x-jsonld-id: http://schema.org/identifier
        schema:inDefinedTermSet:
          type: string
          description: need to include this to tag what the keyword is about; we're
            using the keywords as soft-typed properties
          x-jsonld-id: http://schema.org/inDefinedTermSet
      required:
      - '@type'
      - schema:name
      - schema:inDefinedTermSet
      additionalProperties: true
    contains:
      description: The XDI-dictionary keyword identifying the absorption edge; tagged
        with schema:about "element.edge" to mark its role.
      type: object
      properties:
        schema:inDefinedTermSet:
          const: https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md
          x-jsonld-id: http://schema.org/inDefinedTermSet
        schema:about:
          const: element.edge
          x-jsonld-id: http://schema.org/about
      required:
      - schema:inDefinedTermSet
      - schema:about
    allOf:
    - contains:
        description: The SWEET matrElement keyword identifying the target element;
          tagged with schema:about "element.symbol" to mark its role.
        type: object
        properties:
          schema:inDefinedTermSet:
            const: http://sweetontology.net/matrElement
          schema:about:
            const: element.symbol
        required:
        - schema:inDefinedTermSet
        - schema:about
    x-jsonld-id: http://schema.org/keywords
  schema:variableMeasured:
    description: XAS variableMeasured items. Each item's schema:propertyID SHOULD
      reference one of the XDI canonical variable concept URIs (XDI-CDIF-Mapping.xlsx
      rows 71-89); any other propertyID string is also permitted (propertyID_item
      arm).
    type: array
    items:
      properties:
        schema:propertyID:
          type: array
          minItems: 1
          items:
            anyOf:
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml#/$defs/propertyID_item
            - enum:
              - xas:monochromatorenergy
              - xas:monochromatorangle
              - xas:incidentintensity
              - xas:transmittedintensity
              - xas:fluorescenceintensity
              - xas:referenceintensity
              - xas:absorptioncoefficient
              - xas:fluorescenceabsorptioncoefficient
              - xas:referenceabsorptioncoefficient
              - xas:normalizedtransmissionabsorptioncoefficient
              - xas:normalizedfluorescenceabsorptioncoefficient
              - xas:normalizedreferenceabsorptioncoefficient
              - xas:wavenumber
              - xas:exafsfunction
              - xas:filteredchimagnitude
              - xas:filteredchiphase
              - xas:filteredchireal
              - xas:filteredchiimaginary
              - xas:radialdistance
          x-jsonld-id: http://schema.org/propertyID
    x-jsonld-id: http://schema.org/variableMeasured
$defs:
  CdifProvActivity:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasGeneratedBy/schema.yaml
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
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  dcat: http://www.w3.org/ns/dcat#
  dcterms: http://purl.org/dc/terms/
  nxs: https://manual.nexusformat.org/classes/
  prov: http://www.w3.org/ns/prov#
  spdx: http://spdx.org/rdf/terms#
  xas: https://w3id.org/cdif/xas/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasCore/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasCore/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "dcterms": "http://purl.org/dc/terms/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "xas": "cdif:xas/",
    "wd": "https://www.wikidata.org/entity/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasCore/context.jsonld)

## Sources

* [CDIF-4-XAS OSCARS Project](https://doi.org/10.5281/zenodo.17421917)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/xasProperties/xasCore`

