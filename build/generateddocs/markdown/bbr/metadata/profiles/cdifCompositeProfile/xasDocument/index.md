
# CDIF XAS document profile (Schema)

`cdif.bbr.metadata.profiles.cdifCompositeProfile.xasDocument` *v1.0*

Document-level CDIF profile for X-ray Absorption Spectroscopy datasets: composes cdifCore + cdifDiscovery + cdifDataDescription + cdifDataStructure with xasCore (mandatory) + xasOptional (recommended). Conformance URI https://w3id.org/cdif/xasDocument/1.0.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF XAS document profile

Document-level CDIF profile for X-ray Absorption Spectroscopy datasets.

## Composition

| Component | Role | Conformance URI |
|-----------|------|-----------------|
| cdifCore | dataset discovery mandatory content | `https://w3id.org/cdif/core/1.1` |
| cdifDiscovery | dataset discovery optional content | `https://w3id.org/cdif/discovery/1.1` |
| cdifDataDescription | measured variables and their semantics | `https://w3id.org/cdif/data_description/1.1` |
| cdifDataStructure | physical / logical / tabular data structure | `https://w3id.org/cdif/data_structure/1.1` |
| xasCore | XAS-mandatory instrument + sample metadata | `https://w3id.org/cdif/xasCore/1.0` |
| xasOptional | XAS-recommended metadata (calibration, edge, etc.) | `https://w3id.org/cdif/xasOptional/1.0` |

## Conformance URI

`https://w3id.org/cdif/xasDocument/1.0`

## Release

Release artifacts (resolved schema, aggregated SHACL, implementation guide,
frame, examples) are built into the `cdifxasRelease` branch of the
[XAS-CDIF](https://github.com/smrgeoinfo/XAS-CDIF) repository.

## Examples

### Example CDIF XAS test record.
Example CDIF XAS metadata, not real values.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "time": "http://www.w3.org/2006/time#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://w3id.org/cdif/xas/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "prov": "http://www.w3.org/ns/prov#",
    "csvw": "http://www.w3.org/ns/csvw#",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "xas:487y54",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "X-ray absorption spectra for K edge, Iron metal, XDI CDIF example",
  "schema:description": "Example metadata including all properties in the CDIF XAS profile",
  "schema:identifier": "https://doi.org/10.9999/aqweropjh",
  "schema:dateModified": "2025-06-22",
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "Facility",
      "schema:contributor": {
        "@type": [
          "schema:Organization"
        ],
        "@id": "https://ror.org/aps",
        "schema:name": "Argonne Synchotron"
      }
    },
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "dataCollector",
      "schema:contributor": {
        "@id": "https://orcid.org/3547ulkj"
      }
    },
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "principleInvestigator",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "@id": "https://orcid.org/35735ul",
        "schema:name": "Scienceguy, Biggus",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "missing@email.org"
        },
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "@id": "https://ror.org/lejkthoj",
          "schema:name": "Big Science Institute"
        }
      }
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://orcid.org/3547ulkj",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Collectus, Poindexter",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "missing@email.org"
        }
      }
    ]
  },
  "schema:license": [
    "https://creativecommons.org/publicdomain/zero/1.0/"
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "Se_Na2SeO4_rt_01 XDI data file",
      "schema:contentUrl": "https://github.com/XraySpectroscopy/XASDataLibrary/blob/master/data/Se/Se_Na2SeO4_rt_01.xdi",
      "schema:description": "Distribution = PhysicalDataSet text file conformant with XDI specification",
      "schema:contentSize": "30 kb",
      "schema:encodingFormat": [
        "text/plain"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md"
        }
      ],
      "cdi:allowsDuplicates": false,
      "cdi:isStructuredBy": {
        "@type": [
          "cdi:WideDataStructure"
        ],
        "cdi:has_DataStructureComponent": [
          {
            "@type": [
              "cdi:IdentifierComponent"
            ],
            "cdif:isDefinedBy_RepresentedVariable": {
              "@id": "xas:monochromatorenergy",
              "cdif:name": [
                "monochromator energy"
              ]
            },
            "cdi:isDefinedBy_InstanceVariable": {
              "@id": "xas:monochromatorenergy"
            },
            "cdi:has": {
              "@type": [
                "cdi:ValueMapping"
              ],
              "cdi:hasIndex": 1,
              "cdi:length": 12
            }
          },
          {
            "@type": [
              "cdi:MeasureComponent"
            ],
            "cdi:isDefinedBy_InstanceVariable": {
              "@id": "xas:incidentintensity"
            },
            "cdi:has": {
              "@type": [
                "cdi:ValueMapping"
              ],
              "cdi:hasIndex": 3,
              "cdi:length": 13
            }
          },
          {
            "@type": [
              "cdi:MeasureComponent"
            ],
            "cdi:isDefinedBy_InstanceVariable": {
              "@id": "xas:transmittedintensity"
            },
            "cdi:has": {
              "@type": [
                "cdi:ValueMapping"
              ],
              "cdi:hasIndex": 2,
              "cdi:length": 12
            }
          }
        ],
        "cdi:allowsDuplicates": false,
        "cdi:arrayBase": 1,
        "cdi:commentPrefix": "#",
        "cdi:hasHeader": true,
        "cdi:headerRowCount": 27,
        "cdi:skipInitialSpace": true,
        "cdi:isDelimited": false,
        "cdi:isFixedWidth": true
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
      "schema:identifier": "missing",
      "schema:inDefinedTermSet": "nxs:Field/NXxas/ENTRY/DATA/mode"
    }
  ],
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "K-edge",
      "schema:identifier": "missing",
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
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "schema:Action",
        "prov:Activity"
      ],
      "schema:identifier": "20241111_DSC_NU_OREX-803224-0_1",
      "schema:startTime": "2008-04-10T21:58:50",
      "schema:endTime": "2008-04-10T22:14:37",
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
                  "@id": "xas:source"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "source, made up for this example",
              "schema:identifier": [
                "should have a registry with URIs"
              ],
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
                  "@id": "xas:beamline"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "13-BM-D",
              "schema:identifier": [
                "should have a registry with URIs"
              ],
              "schema:additionalProperty": [
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:collimation"
                    }
                  ],
                  "schema:name": "collimation technique",
                  "schema:value": "none"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:focusing"
                    }
                  ],
                  "schema:name": "focusing",
                  "schema:value": "???"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:harmonicrejection"
                    }
                  ],
                  "schema:name": "harmonic_rejection",
                  "schema:value": "Rh-coated mirror, detuned"
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
                      "@id": "xas:monochromatorchemicalformula"
                    }
                  ],
                  "schema:name": "chemical formula",
                  "schema:value": "Si"
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
                  "schema:value": "missing"
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
                  "@id": "xas:xraymonitor"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "x-ray intensity monitor",
              "schema:additionalProperty": [
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:monitormode"
                    }
                  ],
                  "schema:name": "monitor mode",
                  "schema:value": "monitor"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:monitorpreset"
                    }
                  ],
                  "schema:name": "monitor preset",
                  "schema:value": "N.A."
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:detectori0"
                    }
                  ],
                  "schema:name": "detector mode i0",
                  "schema:alternateName": "incident flux measurement method",
                  "schema:value": "10cm  N2"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:detectorit"
                    }
                  ],
                  "schema:name": "detector mode it",
                  "schema:alternateName": "transmitted flux measurement method",
                  "schema:value": "10cm  N2"
                }
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:pressure"
            }
          ],
          "schema:name": "experiment environment-pressure",
          "schema:description": "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential",
          "schema:value": "3567",
          "schema:unitText": "KPa"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:edgeenergy"
            }
          ],
          "schema:name": "Absorption edge",
          "schema:value": "12658.0",
          "schema:unitText": "eV"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:calibrationmethod"
            }
          ],
          "schema:name": "calibration method",
          "schema:value": "description of calibration procedure",
          "schema:url": "http://protocols.io/link/to/calibrationMethod"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:experimentdocumentation"
            }
          ],
          "schema:name": "Instrument configuration",
          "schema:value": "description of instrument configuration",
          "schema:url": "http://protocols.io/link/to/calibrationMethod"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:installedoptions"
            }
          ],
          "schema:name": "Installed Options",
          "schema:value": "Description of extra equipment installed on the base instrument(?)"
        }
      ],
      "schema:location": {
        "@id": "ex:xasfacility_37yht",
        "@type": [
          "schema:Place"
        ],
        "schema:additionalType": [
          {
            "@id": "xas:facility"
          }
        ],
        "schema:identifier": "https://ror.org/aps",
        "schema:name": "APS",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:facilityenergy"
              }
            ],
            "schema:name": "Facility energy",
            "schema:value": "7.00",
            "schema:unitText": "GeV"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:facilitycurrent"
              }
            ],
            "schema:name": "Facility current",
            "schema:value": "120",
            "schema:unitText": "Amps"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:xraysourcetype"
              }
            ],
            "schema:name": "X-ray Source",
            "schema:value": "APS bending magnet"
          }
        ]
      },
      "schema:object": {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "MaterialSample",
          {
            "@id": "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          }
        ],
        "schema:name": "Na2SeO4",
        "schema:identifier": "igsn:10.6620/357lkj",
        "schema:description": "physical properties of sample: ph, eh, volume, porosity, density, concentration, resistivity, viscosity, crystal structure, opacity from xdi list...",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:porosity"
              }
            ],
            "schema:name": "Porosity",
            "schema:value": "27",
            "schema:unitText": "percent"
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
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplepreparation"
              }
            ],
            "schema:name": "samaple preparation method",
            "schema:value": "powder on tape, 6 layers"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplemass"
              }
            ],
            "schema:name": "sample mass",
            "schema:value": "10",
            "schema:unitText": "mg"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:pointgroup"
              }
            ],
            "schema:name": "crystallographic point group",
            "schema:value": "mm2"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:sampleunitcell"
              }
            ],
            "schema:name": "Crystal unit cell dimensions",
            "schema:value": "cubic; Z = 4; a = 5.46; V = 162.77"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:parentsample"
              }
            ],
            "schema:name": "parent sample identifier",
            "schema:value": "igsn:10.3476/342573"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplematerial"
              }
            ],
            "schema:name": "material state",
            "schema:value": "solid metal foil"
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
  "schema:variableMeasured": [
    {
      "@id": "xas:monochromatorenergy",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:name": "energy",
      "schema:alternateName": [
        "Monochromator energy"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
      "schema:propertyID": [
        {
          "@id": "xas:monochromatorenergy"
        }
      ],
      "schema:unitText": "eV",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:simpleUnitOfMeasure": "eV",
      "cdi:uses": "xas:monochromatorenergy",
      "cdi:name": "energy",
      "cdi:displayLabel": "monochromator energy"
    },
    {
      "@id": "xas:incidentintensity",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:name": "i0 monitory intensity",
      "schema:alternateName": [
        "Monitor intensity"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description)",
      "schema:propertyID": [
        {
          "@id": "xas:incidentintensity"
        }
      ],
      "schema:unitText": "counts",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:uses": "xas:incidentintensity",
      "cdi:name": "i0",
      "cdi:displayLabel": "monitor intensity"
    },
    {
      "@id": "xas:transmittedintensity",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
      "schema:propertyID": [
        {
          "@id": "xas:transmittedintensity"
        }
      ],
      "schema:unitText": "counts",
      "schema:name": "itrans",
      "schema:alternateName": [
        "transmission intensity"
      ],
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:uses": "xas:transmittedintensity",
      "cdi:name": "itrans",
      "cdi:displayLabel": "transmission intensity"
    }
  ],
  "cdi:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "cdi:linkRelationship": "projectProposal",
      "cdi:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "cdi:encodingType": "text/html",
        "cdi:name": "name of the proposal",
        "cdi:url": "https://example.org/locatorForProposalText",
        "cdi:identifier": "identifier for proposal, could used text or schema:PropertyValue pattern"
      }
    }
  ],
  "schema:subjectOf": {
    "@id": "xas:ja51-pz63",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "schema:dateModified": "2025-08-26",
    "schema:creator": [
      {
        "@id": "https://ada.org/person/3479",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Richard, Stephen M.",
        "schema:identifier": "https://orcid.org/0000-0002-7933-2154",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "smrTucson@email.org"
        }
      }
    ],
    "schema:about": {
      "@id": "xas:485749"
    },
    "schema:description": "metadata about documentation for se_na2so4",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/xasOptional/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/xasCore/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_structure/1.1"
      }
    ],
    "schema:sdDatePublished": "2025-08-26",
    "schema:maintainer": {
      "@id": "https://ada.org/person/3479",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Richard, Stephen M."
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/xasDocument/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "spdx": "http://spdx.org/rdf/terms#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "time": "http://www.w3.org/2006/time#",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "xas": "https://w3id.org/cdif/xas/",
      "nxs": "https://manual.nexusformat.org/classes/",
      "prov": "http://www.w3.org/ns/prov#",
      "csvw": "http://www.w3.org/ns/csvw#",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "xas:487y54",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "X-ray absorption spectra for K edge, Iron metal, XDI CDIF example",
  "schema:description": "Example metadata including all properties in the CDIF XAS profile",
  "schema:identifier": "https://doi.org/10.9999/aqweropjh",
  "schema:dateModified": "2025-06-22",
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "Facility",
      "schema:contributor": {
        "@type": [
          "schema:Organization"
        ],
        "@id": "https://ror.org/aps",
        "schema:name": "Argonne Synchotron"
      }
    },
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "dataCollector",
      "schema:contributor": {
        "@id": "https://orcid.org/3547ulkj"
      }
    },
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "principleInvestigator",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "@id": "https://orcid.org/35735ul",
        "schema:name": "Scienceguy, Biggus",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "missing@email.org"
        },
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "@id": "https://ror.org/lejkthoj",
          "schema:name": "Big Science Institute"
        }
      }
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://orcid.org/3547ulkj",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Collectus, Poindexter",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "missing@email.org"
        }
      }
    ]
  },
  "schema:license": [
    "https://creativecommons.org/publicdomain/zero/1.0/"
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "Se_Na2SeO4_rt_01 XDI data file",
      "schema:contentUrl": "https://github.com/XraySpectroscopy/XASDataLibrary/blob/master/data/Se/Se_Na2SeO4_rt_01.xdi",
      "schema:description": "Distribution = PhysicalDataSet text file conformant with XDI specification",
      "schema:contentSize": "30 kb",
      "schema:encodingFormat": [
        "text/plain"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md"
        }
      ],
      "cdi:allowsDuplicates": false,
      "cdi:isStructuredBy": {
        "@type": [
          "cdi:WideDataStructure"
        ],
        "cdi:has_DataStructureComponent": [
          {
            "@type": [
              "cdi:IdentifierComponent"
            ],
            "cdif:isDefinedBy_RepresentedVariable": {
              "@id": "xas:monochromatorenergy",
              "cdif:name": [
                "monochromator energy"
              ]
            },
            "cdi:isDefinedBy_InstanceVariable": {
              "@id": "xas:monochromatorenergy"
            },
            "cdi:has": {
              "@type": [
                "cdi:ValueMapping"
              ],
              "cdi:hasIndex": 1,
              "cdi:length": 12
            }
          },
          {
            "@type": [
              "cdi:MeasureComponent"
            ],
            "cdi:isDefinedBy_InstanceVariable": {
              "@id": "xas:incidentintensity"
            },
            "cdi:has": {
              "@type": [
                "cdi:ValueMapping"
              ],
              "cdi:hasIndex": 3,
              "cdi:length": 13
            }
          },
          {
            "@type": [
              "cdi:MeasureComponent"
            ],
            "cdi:isDefinedBy_InstanceVariable": {
              "@id": "xas:transmittedintensity"
            },
            "cdi:has": {
              "@type": [
                "cdi:ValueMapping"
              ],
              "cdi:hasIndex": 2,
              "cdi:length": 12
            }
          }
        ],
        "cdi:allowsDuplicates": false,
        "cdi:arrayBase": 1,
        "cdi:commentPrefix": "#",
        "cdi:hasHeader": true,
        "cdi:headerRowCount": 27,
        "cdi:skipInitialSpace": true,
        "cdi:isDelimited": false,
        "cdi:isFixedWidth": true
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
      "schema:identifier": "missing",
      "schema:inDefinedTermSet": "nxs:Field/NXxas/ENTRY/DATA/mode"
    }
  ],
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "K-edge",
      "schema:identifier": "missing",
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
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "schema:Action",
        "prov:Activity"
      ],
      "schema:identifier": "20241111_DSC_NU_OREX-803224-0_1",
      "schema:startTime": "2008-04-10T21:58:50",
      "schema:endTime": "2008-04-10T22:14:37",
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
                  "@id": "xas:source"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "source, made up for this example",
              "schema:identifier": [
                "should have a registry with URIs"
              ],
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
                  "@id": "xas:beamline"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "13-BM-D",
              "schema:identifier": [
                "should have a registry with URIs"
              ],
              "schema:additionalProperty": [
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:collimation"
                    }
                  ],
                  "schema:name": "collimation technique",
                  "schema:value": "none"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:focusing"
                    }
                  ],
                  "schema:name": "focusing",
                  "schema:value": "???"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:harmonicrejection"
                    }
                  ],
                  "schema:name": "harmonic_rejection",
                  "schema:value": "Rh-coated mirror, detuned"
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
                      "@id": "xas:monochromatorchemicalformula"
                    }
                  ],
                  "schema:name": "chemical formula",
                  "schema:value": "Si"
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
                  "schema:value": "missing"
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
                  "@id": "xas:xraymonitor"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "x-ray intensity monitor",
              "schema:additionalProperty": [
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:monitormode"
                    }
                  ],
                  "schema:name": "monitor mode",
                  "schema:value": "monitor"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:monitorpreset"
                    }
                  ],
                  "schema:name": "monitor preset",
                  "schema:value": "N.A."
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:detectori0"
                    }
                  ],
                  "schema:name": "detector mode i0",
                  "schema:alternateName": "incident flux measurement method",
                  "schema:value": "10cm  N2"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:detectorit"
                    }
                  ],
                  "schema:name": "detector mode it",
                  "schema:alternateName": "transmitted flux measurement method",
                  "schema:value": "10cm  N2"
                }
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:pressure"
            }
          ],
          "schema:name": "experiment environment-pressure",
          "schema:description": "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential",
          "schema:value": "3567",
          "schema:unitText": "KPa"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:edgeenergy"
            }
          ],
          "schema:name": "Absorption edge",
          "schema:value": "12658.0",
          "schema:unitText": "eV"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:calibrationmethod"
            }
          ],
          "schema:name": "calibration method",
          "schema:value": "description of calibration procedure",
          "schema:url": "http://protocols.io/link/to/calibrationMethod"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:experimentdocumentation"
            }
          ],
          "schema:name": "Instrument configuration",
          "schema:value": "description of instrument configuration",
          "schema:url": "http://protocols.io/link/to/calibrationMethod"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:installedoptions"
            }
          ],
          "schema:name": "Installed Options",
          "schema:value": "Description of extra equipment installed on the base instrument(?)"
        }
      ],
      "schema:location": {
        "@id": "ex:xasfacility_37yht",
        "@type": [
          "schema:Place"
        ],
        "schema:additionalType": [
          {
            "@id": "xas:facility"
          }
        ],
        "schema:identifier": "https://ror.org/aps",
        "schema:name": "APS",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:facilityenergy"
              }
            ],
            "schema:name": "Facility energy",
            "schema:value": "7.00",
            "schema:unitText": "GeV"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:facilitycurrent"
              }
            ],
            "schema:name": "Facility current",
            "schema:value": "120",
            "schema:unitText": "Amps"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:xraysourcetype"
              }
            ],
            "schema:name": "X-ray Source",
            "schema:value": "APS bending magnet"
          }
        ]
      },
      "schema:object": {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "MaterialSample",
          {
            "@id": "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          }
        ],
        "schema:name": "Na2SeO4",
        "schema:identifier": "igsn:10.6620/357lkj",
        "schema:description": "physical properties of sample: ph, eh, volume, porosity, density, concentration, resistivity, viscosity, crystal structure, opacity from xdi list...",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:porosity"
              }
            ],
            "schema:name": "Porosity",
            "schema:value": "27",
            "schema:unitText": "percent"
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
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplepreparation"
              }
            ],
            "schema:name": "samaple preparation method",
            "schema:value": "powder on tape, 6 layers"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplemass"
              }
            ],
            "schema:name": "sample mass",
            "schema:value": "10",
            "schema:unitText": "mg"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:pointgroup"
              }
            ],
            "schema:name": "crystallographic point group",
            "schema:value": "mm2"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:sampleunitcell"
              }
            ],
            "schema:name": "Crystal unit cell dimensions",
            "schema:value": "cubic; Z = 4; a = 5.46; V = 162.77"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:parentsample"
              }
            ],
            "schema:name": "parent sample identifier",
            "schema:value": "igsn:10.3476/342573"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplematerial"
              }
            ],
            "schema:name": "material state",
            "schema:value": "solid metal foil"
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
  "schema:variableMeasured": [
    {
      "@id": "xas:monochromatorenergy",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:name": "energy",
      "schema:alternateName": [
        "Monochromator energy"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
      "schema:propertyID": [
        {
          "@id": "xas:monochromatorenergy"
        }
      ],
      "schema:unitText": "eV",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:simpleUnitOfMeasure": "eV",
      "cdi:uses": "xas:monochromatorenergy",
      "cdi:name": "energy",
      "cdi:displayLabel": "monochromator energy"
    },
    {
      "@id": "xas:incidentintensity",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:name": "i0 monitory intensity",
      "schema:alternateName": [
        "Monitor intensity"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description)",
      "schema:propertyID": [
        {
          "@id": "xas:incidentintensity"
        }
      ],
      "schema:unitText": "counts",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:uses": "xas:incidentintensity",
      "cdi:name": "i0",
      "cdi:displayLabel": "monitor intensity"
    },
    {
      "@id": "xas:transmittedintensity",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
      "schema:propertyID": [
        {
          "@id": "xas:transmittedintensity"
        }
      ],
      "schema:unitText": "counts",
      "schema:name": "itrans",
      "schema:alternateName": [
        "transmission intensity"
      ],
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:uses": "xas:transmittedintensity",
      "cdi:name": "itrans",
      "cdi:displayLabel": "transmission intensity"
    }
  ],
  "cdi:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "cdi:linkRelationship": "projectProposal",
      "cdi:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "cdi:encodingType": "text/html",
        "cdi:name": "name of the proposal",
        "cdi:url": "https://example.org/locatorForProposalText",
        "cdi:identifier": "identifier for proposal, could used text or schema:PropertyValue pattern"
      }
    }
  ],
  "schema:subjectOf": {
    "@id": "xas:ja51-pz63",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "schema:dateModified": "2025-08-26",
    "schema:creator": [
      {
        "@id": "https://ada.org/person/3479",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Richard, Stephen M.",
        "schema:identifier": "https://orcid.org/0000-0002-7933-2154",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "smrTucson@email.org"
        }
      }
    ],
    "schema:about": {
      "@id": "xas:485749"
    },
    "schema:description": "metadata about documentation for se_na2so4",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/xasOptional/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/xasCore/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_structure/1.1"
      }
    ],
    "schema:sdDatePublished": "2025-08-26",
    "schema:maintainer": {
      "@id": "https://ada.org/person/3479",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Richard, Stephen M."
    }
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xas: <https://w3id.org/cdif/xas/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

xas:487y54 a schema1:Dataset,
        schema1:Product ;
    cdi:relatedLink [ a schema1:LinkRole ;
            cdi:linkRelationship "projectProposal" ;
            cdi:target [ a schema1:EntryPoint ;
                    cdi:encodingType "text/html" ;
                    cdi:identifier "identifier for proposal, could used text or schema:PropertyValue pattern" ;
                    cdi:name "name of the proposal" ;
                    cdi:url "https://example.org/locatorForProposalText" ] ] ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor <https://orcid.org/3547ulkj> ;
            schema1:roleName "dataCollector" ],
        [ a schema1:Role ;
            schema1:contributor <https://orcid.org/35735ul> ;
            schema1:roleName "principleInvestigator" ],
        [ a schema1:Role ;
            schema1:contributor <https://ror.org/aps> ;
            schema1:roleName "Facility" ] ;
    schema1:creator ( <https://orcid.org/3547ulkj> ) ;
    schema1:dateModified "2025-06-22" ;
    schema1:description "Example metadata including all properties in the CDIF XAS profile" ;
    schema1:distribution [ a cdi:PhysicalDataSet,
                schema1:DataDownload ;
            cdi:allowsDuplicates false ;
            cdi:isStructuredBy [ a cdi:WideDataStructure ;
                    cdi:allowsDuplicates false ;
                    cdi:arrayBase 1 ;
                    cdi:commentPrefix "#" ;
                    cdi:hasHeader true ;
                    cdi:has_DataStructureComponent [ a cdi:MeasureComponent ;
                            cdi:has [ a cdi:ValueMapping ;
                                    cdi:hasIndex 2 ;
                                    cdi:length 12 ] ;
                            cdi:isDefinedBy_InstanceVariable xas:transmittedintensity ],
                        [ a cdi:IdentifierComponent ;
                            cdi:has [ a cdi:ValueMapping ;
                                    cdi:hasIndex 1 ;
                                    cdi:length 12 ] ;
                            cdi:isDefinedBy_InstanceVariable xas:monochromatorenergy ;
                            cdif:isDefinedBy_RepresentedVariable xas:monochromatorenergy ],
                        [ a cdi:MeasureComponent ;
                            cdi:has [ a cdi:ValueMapping ;
                                    cdi:hasIndex 3 ;
                                    cdi:length 13 ] ;
                            cdi:isDefinedBy_InstanceVariable xas:incidentintensity ] ;
                    cdi:headerRowCount 27 ;
                    cdi:isDelimited false ;
                    cdi:isFixedWidth true ;
                    cdi:skipInitialSpace true ] ;
            dcterms:conformsTo <https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md> ;
            schema1:contentSize "30 kb" ;
            schema1:contentUrl "https://github.com/XraySpectroscopy/XASDataLibrary/blob/master/data/Se/Se_Na2SeO4_rt_01.xdi" ;
            schema1:description "Distribution = PhysicalDataSet text file conformant with XDI specification" ;
            schema1:encodingFormat "text/plain" ;
            schema1:name "Se_Na2SeO4_rt_01 XDI data file" ] ;
    schema1:identifier "https://doi.org/10.9999/aqweropjh" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:about "element.symbol" ;
            schema1:identifier "http://sweetontology.net/matrElement/Selenium" ;
            schema1:inDefinedTermSet "http://sweetontology.net/matrElement" ;
            schema1:name "Selenium" ;
            schema1:termCode "Se" ],
        [ a schema1:DefinedTerm ;
            schema1:about "element.edge" ;
            schema1:identifier "missing" ;
            schema1:inDefinedTermSet "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md" ;
            schema1:name "K-edge" ;
            schema1:termCode "K" ] ;
    schema1:license "https://creativecommons.org/publicdomain/zero/1.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "http://purl.org/pan-science/PaNET/PaNET01196" ;
            schema1:inDefinedTermSet "http://purl.org/pan-science/PaNET/PaNET.owl" ;
            schema1:name "X-Ray Absorption Spectroscopy" ;
            schema1:termCode "XAS" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "missing" ;
            schema1:inDefinedTermSet "nxs:Field/NXxas/ENTRY/DATA/mode" ;
            schema1:name "Transmission" ] ;
    schema1:name "X-ray absorption spectra for K edge, Iron metal, XDI CDIF example" ;
    schema1:subjectOf xas:ja51-pz63 ;
    schema1:variableMeasured xas:incidentintensity,
        xas:monochromatorenergy,
        xas:transmittedintensity ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:additionalProperty [ a schema1:PropertyValue ;
                    schema1:name "calibration method" ;
                    schema1:propertyID xas:calibrationmethod ;
                    schema1:url "http://protocols.io/link/to/calibrationMethod" ;
                    schema1:value "description of calibration procedure" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Absorption edge" ;
                    schema1:propertyID xas:edgeenergy ;
                    schema1:unitText "eV" ;
                    schema1:value "12658.0" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Installed Options" ;
                    schema1:propertyID xas:installedoptions ;
                    schema1:value "Description of extra equipment installed on the base instrument(?)" ],
                [ a schema1:PropertyValue ;
                    schema1:description "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential" ;
                    schema1:name "experiment environment-pressure" ;
                    schema1:propertyID xas:pressure ;
                    schema1:unitText "KPa" ;
                    schema1:value "3567" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Instrument configuration" ;
                    schema1:propertyID xas:experimentdocumentation ;
                    schema1:url "http://protocols.io/link/to/calibrationMethod" ;
                    schema1:value "description of instrument configuration" ] ;
            schema1:additionalType xas:analysisevent ;
            schema1:endTime "2008-04-10T22:14:37" ;
            schema1:identifier "20241111_DSC_NU_OREX-803224-0_1" ;
            schema1:location ex:xasfacility_37yht ;
            schema1:object [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "Stoichiometry" ;
                            schema1:propertyID xas:samplechemicalcomposition ;
                            schema1:value "Na2SeO4" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "sample mass" ;
                            schema1:propertyID xas:samplemass ;
                            schema1:unitText "mg" ;
                            schema1:value "10" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "crystallographic point group" ;
                            schema1:propertyID xas:pointgroup ;
                            schema1:value "mm2" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "samaple preparation method" ;
                            schema1:propertyID xas:samplepreparation ;
                            schema1:value "powder on tape, 6 layers" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Crystal unit cell dimensions" ;
                            schema1:propertyID xas:sampleunitcell ;
                            schema1:value "cubic; Z = 4; a = 5.46; V = 162.77" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "material state" ;
                            schema1:propertyID xas:samplematerial ;
                            schema1:value "solid metal foil" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Porosity" ;
                            schema1:propertyID xas:porosity ;
                            schema1:unitText "percent" ;
                            schema1:value "27" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "parent sample identifier" ;
                            schema1:propertyID xas:parentsample ;
                            schema1:value "igsn:10.3476/342573" ] ;
                    schema1:additionalType <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample>,
                        "MaterialSample" ;
                    schema1:description "physical properties of sample: ph, eh, volume, porosity, density, concentration, resistivity, viscosity, crystal structure, opacity from xdi list..." ;
                    schema1:identifier "igsn:10.6620/357lkj" ;
                    schema1:name "Na2SeO4" ] ;
            schema1:startTime "2008-04-10T21:58:50" ;
            prov:used [ schema1:instrument [ a schema1:Product,
                                schema1:Thing,
                                prov:Entity ;
                            schema1:additionalProperty [ a schema1:PropertyValue ;
                                    schema1:name "monitor preset" ;
                                    schema1:propertyID xas:monitorpreset ;
                                    schema1:value "N.A." ],
                                [ a schema1:PropertyValue ;
                                    schema1:alternateName "transmitted flux measurement method" ;
                                    schema1:name "detector mode it" ;
                                    schema1:propertyID xas:detectorit ;
                                    schema1:value "10cm  N2" ],
                                [ a schema1:PropertyValue ;
                                    schema1:alternateName "incident flux measurement method" ;
                                    schema1:name "detector mode i0" ;
                                    schema1:propertyID xas:detectori0 ;
                                    schema1:value "10cm  N2" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "monitor mode" ;
                                    schema1:propertyID xas:monitormode ;
                                    schema1:value "monitor" ] ;
                            schema1:additionalType xas:xraymonitor,
                                wd:Q3099911 ;
                            schema1:name "x-ray intensity monitor" ] ],
                [ schema1:instrument [ a schema1:Product,
                                schema1:Thing,
                                prov:Entity ;
                            schema1:additionalProperty [ a schema1:PropertyValue ;
                                    schema1:name "harmonic_rejection" ;
                                    schema1:propertyID xas:harmonicrejection ;
                                    schema1:value "Rh-coated mirror, detuned" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "focusing" ;
                                    schema1:propertyID xas:focusing ;
                                    schema1:value "???" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "collimation technique" ;
                                    schema1:propertyID xas:collimation ;
                                    schema1:value "none" ] ;
                            schema1:additionalType xas:beamline,
                                wd:Q3099911 ;
                            schema1:identifier "should have a registry with URIs" ;
                            schema1:name "13-BM-D" ] ],
                [ schema1:instrument [ a schema1:Product,
                                schema1:Thing,
                                prov:Entity ;
                            schema1:additionalProperty [ a schema1:PropertyValue ;
                                    schema1:name "reflection plane (hkl)" ;
                                    schema1:propertyID xas:reflectionplane ;
                                    schema1:value "1,1,1" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "chemical formula" ;
                                    schema1:propertyID xas:monochromatorchemicalformula ;
                                    schema1:value "Si" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "d-spacing" ;
                                    schema1:propertyID xas:dspacing ;
                                    schema1:unitText "Angstrom" ;
                                    schema1:value "3.13550" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "crystal type" ;
                                    schema1:propertyID xas:monochromatortype ;
                                    schema1:value "missing" ] ;
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
                            schema1:identifier "should have a registry with URIs" ;
                            schema1:name "source, made up for this example" ] ] ] .

ex:xasfacility_37yht a schema1:Place ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "X-ray Source" ;
            schema1:propertyID xas:xraysourcetype ;
            schema1:value "APS bending magnet" ],
        [ a schema1:PropertyValue ;
            schema1:name "Facility energy" ;
            schema1:propertyID xas:facilityenergy ;
            schema1:unitText "GeV" ;
            schema1:value "7.00" ],
        [ a schema1:PropertyValue ;
            schema1:name "Facility current" ;
            schema1:propertyID xas:facilitycurrent ;
            schema1:unitText "Amps" ;
            schema1:value "120" ] ;
    schema1:additionalType xas:facility ;
    schema1:identifier "https://ror.org/aps" ;
    schema1:name "APS" .

<https://orcid.org/35735ul> a schema1:Person ;
    schema1:affiliation <https://ror.org/lejkthoj> ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "missing@email.org" ] ;
    schema1:name "Scienceguy, Biggus" .

<https://ror.org/aps> a schema1:Organization ;
    schema1:name "Argonne Synchotron" .

<https://ror.org/lejkthoj> a schema1:Organization ;
    schema1:name "Big Science Institute" .

xas:ja51-pz63 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/data_description/1.1>,
        <https://w3id.org/cdif/data_structure/1.1>,
        <https://w3id.org/cdif/discovery/1.1>,
        <https://w3id.org/cdif/xasCore/1.0>,
        <https://w3id.org/cdif/xasOptional/1.0> ;
    schema1:about xas:485749 ;
    schema1:additionalType dcat:CatalogRecord ;
    schema1:creator <https://ada.org/person/3479> ;
    schema1:dateModified "2025-08-26" ;
    schema1:description "metadata about documentation for se_na2so4" ;
    schema1:maintainer <https://ada.org/person/3479> ;
    schema1:sdDatePublished "2025-08-26" .

<https://ada.org/person/3479> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "smrTucson@email.org" ] ;
    schema1:identifier "https://orcid.org/0000-0002-7933-2154" ;
    schema1:name "Richard, Stephen M." .

<https://orcid.org/3547ulkj> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "missing@email.org" ] ;
    schema1:name "Collectus, Poindexter" .

xas:incidentintensity a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "monitor intensity" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "i0" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:uses "xas:incidentintensity" ;
    schema1:alternateName "Monitor intensity" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description)" ;
    schema1:name "i0 monitory intensity" ;
    schema1:propertyID xas:incidentintensity ;
    schema1:unitText "counts" .

xas:transmittedintensity a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "transmission intensity" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "itrans" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:uses "xas:transmittedintensity" ;
    schema1:alternateName "transmission intensity" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description" ;
    schema1:name "itrans" ;
    schema1:propertyID xas:transmittedintensity ;
    schema1:unitText "counts" .

xas:monochromatorenergy a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "monochromator energy" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "energy" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:simpleUnitOfMeasure "eV" ;
    cdi:uses "xas:monochromatorenergy" ;
    schema1:alternateName "Monochromator energy" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description" ;
    schema1:name "energy" ;
    schema1:propertyID xas:monochromatorenergy ;
    schema1:unitText "eV" ;
    cdif:name "monochromator energy" .


```


### Actual data CDIF XAS record.
Metadata for an example XAS dataset.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "time": "http://www.w3.org/2006/time#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "csvw": "http://www.w3.org/ns/csvw#",
    "xas": "https://w3id.org/cdif/xas/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "prov": "http://www.w3.org/ns/prov#",
    "dcat": "http://www.w3.org/ns/dcat#",
    "cdif": "https://cdif.org/profiles/",
    "ex": "https://example.org/",
    "igsn": "https://igsn.org/"
  },
  "@id": "xas:487y54123",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "X-ray absorption spectra for K edge, Iron metal, XDI CDIF example",
  "schema:description": "Example metadata including all properties in the CDIF XAS profile",
  "schema:identifier": "https://doi.org/10.9999/aqweropjh",
  "schema:dateModified": "2025-06-22",
  "schema:datePublished": "2025-06-22",
  "schema:creator": {
    "@list": [
      {
        "@id": "https://orcid.org/3547ulkj",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Collectus, Poindexter",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "missing@email.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "Facility",
      "schema:contributor": {
        "@type": [
          "schema:Organization"
        ],
        "@id": "https://ror.org/aps",
        "schema:name": "Argonne Synchotron"
      }
    },
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "dataCollector",
      "schema:contributor": {
        "@id": "https://orcid.org/3547ulkj"
      }
    },
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "principleInvestigator",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "@id": "https://orcid.org/35735ul",
        "schema:name": "Scienceguy, Biggus",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "missing@email.org"
        },
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "@id": "https://ror.org/lejkthoj",
          "schema:name": "Big Science Institute"
        }
      }
    }
  ],
  "schema:license": [
    "https://creativecommons.org/publicdomain/zero/1.0/"
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:TabularTextDataSet"
      ],
      "schema:name": "XDI data file for Se K-edge XAS",
      "schema:contentUrl": "https://github.com/XraySpectroscopy/XASDataLibrary/blob/master/data/Se/Se_Na2SeO4_rt_01.xdi",
      "schema:description": "Fixed-width text file conformant with XDI specification. Contains three data columns: monochromator energy (eV), transmitted intensity (counts), and incident intensity (counts). 27-line header with comment prefix '#'.",
      "schema:encodingFormat": [
        "text/plain"
      ],
      "cdi:isFixedWidth": true,
      "dcterms:conformsTo": [
        {
          "@id": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md"
        }
      ],
      "cdif:hasPhysicalMapping": [
        {
          "cdif:index": 0,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "xas:monochromatorenergy"
          }
        },
        {
          "cdif:index": 1,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "xas:transmittedintensity"
          }
        },
        {
          "cdif:index": 2,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "xas:incidentintensity"
          }
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
      "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01196",
      "schema:termCode": "XAS",
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
      "schema:identifier": "missing",
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
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "schema:Action",
        "prov:Activity"
      ],
      "schema:additionalType": [
        {
          "@id": "xas:analysisevent"
        }
      ],
      "schema:identifier": "20241111_DSC_NU_OREX-803224-0_1",
      "schema:startTime": "2008-04-10T21:58:50",
      "schema:endTime": "2008-04-10T22:14:37",
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
                  "@id": "xas:source"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "source, made up for this example",
              "schema:identifier": [
                "should have a registry with URIs"
              ],
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
                  "@id": "xas:beamline"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "13-BM-D",
              "schema:identifier": [
                "should have a registry with URIs"
              ],
              "schema:additionalProperty": [
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:collimation"
                    }
                  ],
                  "schema:name": "collimation technique",
                  "schema:value": "none"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:focusing"
                    }
                  ],
                  "schema:name": "focusing",
                  "schema:value": "???"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:harmonicrejection"
                    }
                  ],
                  "schema:name": "harmonic_rejection",
                  "schema:value": "Rh-coated mirror, detuned"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:detectortype"
                    }
                  ],
                  "schema:name": "detector",
                  "schema:value": "Vortex ME4 silicon drift detector"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:energyrange"
                    }
                  ],
                  "schema:name": "energy range",
                  "schema:value": "4.5 - 27",
                  "schema:unitText": "keV"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:energyresolution"
                    }
                  ],
                  "schema:name": "energy resolution",
                  "schema:value": "1e-4",
                  "schema:description": "delta_E/E"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:flux"
                    }
                  ],
                  "schema:name": "photon flux",
                  "schema:value": "1e11",
                  "schema:unitText": "photons/s"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:scanmode"
                    }
                  ],
                  "schema:name": "scan mode",
                  "schema:value": "step"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:spotsize"
                    }
                  ],
                  "schema:name": "beam spot size",
                  "schema:value": "500 x 500",
                  "schema:unitText": "um"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:website"
                    }
                  ],
                  "schema:name": "beamline website",
                  "schema:value": "https://www.aps.anl.gov/Beamlines/Directory/13-BM-D"
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
                      "@id": "xas:monochromatorchemicalformula"
                    }
                  ],
                  "schema:name": "chemical formula",
                  "schema:value": "Si"
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
                  "schema:value": "missing"
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
                  "@id": "xas:xraymonitor"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "x-ray intensity monitor",
              "schema:additionalProperty": [
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:monitormode"
                    }
                  ],
                  "schema:name": "monitor mode",
                  "schema:value": "monitor"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:monitorpreset"
                    }
                  ],
                  "schema:name": "monitor preset",
                  "schema:value": "N.A."
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:detectori0"
                    }
                  ],
                  "schema:name": "detector mode i0",
                  "schema:alternateName": [
                    "incident flux measurement method"
                  ],
                  "schema:value": "10cm  N2"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:detectorit"
                    }
                  ],
                  "schema:name": "detector mode it",
                  "schema:alternateName": [
                    "transmitted flux measurement method"
                  ],
                  "schema:value": "10cm  N2"
                }
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:pressure"
            }
          ],
          "schema:name": "experiment environment-pressure",
          "schema:description": "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential",
          "schema:value": 3567,
          "schema:unitText": "KPa"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:edgeenergy"
            }
          ],
          "schema:name": "Absorption edge",
          "schema:value": "12658.0",
          "schema:unitText": "eV"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:calibrationmethod"
            }
          ],
          "schema:name": "calibration method",
          "schema:value": "description of calibration procedure",
          "schema:url": "http://protocols.io/link/to/calibrationMethod"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:experimentdocumentation"
            }
          ],
          "schema:name": "Instrument configuration",
          "schema:value": "description of instrument configuration",
          "schema:url": "http://protocols.io/link/to/calibrationMethod"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:installedoptions"
            }
          ],
          "schema:name": "Installed Options",
          "schema:value": "Description of extra equipment installed on the base instrument(?)"
        }
      ],
      "schema:location": {
        "@id": "ex:xasfacility_37yht",
        "@type": [
          "schema:Place"
        ],
        "schema:additionalType": [
          {
            "@id": "xas:facility"
          }
        ],
        "schema:identifier": "https://ror.org/aps",
        "schema:name": "APS",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:facilityenergy"
              }
            ],
            "schema:name": "Facility energy",
            "schema:value": "7.00",
            "schema:unitText": "GeV"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:facilitycurrent"
              }
            ],
            "schema:name": "Facility current",
            "schema:value": "120",
            "schema:unitText": "Amps"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:xraysourcetype"
              }
            ],
            "schema:name": "X-ray Source",
            "schema:value": "APS bending magnet"
          }
        ]
      },
      "schema:object": {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "MaterialSample",
          {
            "@id": "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          }
        ],
        "schema:name": "Na2SeO4",
        "schema:identifier": "igsn:10.6620/357lkj",
        "schema:description": "physical properties of sample: ph, eh, volume, porosity, density, concentration, resistivity, viscosity, crystal structure, opacity from xdi list...",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:porosity"
              }
            ],
            "schema:name": "Porosity",
            "schema:value": 27,
            "schema:unitText": "percent"
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
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplepreparation"
              }
            ],
            "schema:name": "samaple preparation method",
            "schema:value": "powder on tape, 6 layers"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplemass"
              }
            ],
            "schema:name": "sample mass",
            "schema:value": "10",
            "schema:unitText": "mg"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:pointgroup"
              }
            ],
            "schema:name": "crystallographic point group",
            "schema:value": "mm2"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:sampleunitcell"
              }
            ],
            "schema:name": "Crystal unit cell dimensions",
            "schema:value": "cubic; Z = 4; a = 5.46; V = 162.77"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:parentsample"
              }
            ],
            "schema:name": "parent sample identifier",
            "schema:value": "igsn:10.3476/342573"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplematerial"
              }
            ],
            "schema:name": "material state",
            "schema:value": "solid metal foil"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:concentration"
              }
            ],
            "schema:name": "concentration",
            "schema:value": "0.05",
            "schema:unitText": "mol/L"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplecrystalstructure"
              }
            ],
            "schema:name": "crystal structure",
            "schema:value": "cubic"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:density"
              }
            ],
            "schema:name": "density",
            "schema:value": "2.20",
            "schema:unitText": "g/cm^3"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:eh"
              }
            ],
            "schema:name": "redox potential (Eh)",
            "schema:value": "0.35",
            "schema:unitText": "V"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:electricfield"
              }
            ],
            "schema:name": "electric field",
            "schema:value": "0",
            "schema:unitText": "V/m"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:electrochemicalpotential"
              }
            ],
            "schema:name": "electrochemical potential",
            "schema:value": "0",
            "schema:unitText": "V"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:magneticfield"
              }
            ],
            "schema:name": "magnetic field",
            "schema:value": "0",
            "schema:unitText": "T"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:magneticmoment"
              }
            ],
            "schema:name": "magnetic moment",
            "schema:value": "0",
            "schema:unitText": "Bohr magneton"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:opacity"
              }
            ],
            "schema:name": "opacity",
            "schema:value": "opaque"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:ph"
              }
            ],
            "schema:name": "pH (acidity)",
            "schema:value": "7.4"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplepreparation"
              }
            ],
            "schema:name": "sample preparation (XDI Sample.prep)",
            "schema:value": "ground powder pressed to 6-layer tape mount"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:pressure"
              }
            ],
            "schema:name": "pressure",
            "schema:value": "1.013e5",
            "schema:unitText": "Pa"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:resistivity"
              }
            ],
            "schema:name": "resistivity",
            "schema:value": "1e6",
            "schema:unitText": "ohm cm"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:temperature"
              }
            ],
            "schema:name": "temperature",
            "schema:value": "298",
            "schema:unitText": "K"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:viscosity"
              }
            ],
            "schema:name": "viscosity",
            "schema:value": "not applicable (solid)"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:volume"
              }
            ],
            "schema:name": "volume",
            "schema:value": "0.005",
            "schema:unitText": "cm^3"
          }
        ]
      }
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "xas:monochromatorenergy",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:name": "energy",
      "schema:alternateName": [
        "Monochromator energy"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
      "schema:propertyID": [
        {
          "@id": "xas:monochromatorenergy"
        }
      ],
      "schema:unitText": "eV",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:simpleUnitOfMeasure": "eV",
      "cdi:uses": "xas:monochromatorenergy",
      "cdi:name": "energy",
      "cdi:displayLabel": "monochromator energy"
    },
    {
      "@id": "xas:incidentintensity",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:name": "i0 monitory intensity",
      "schema:alternateName": [
        "Monitor intensity"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description)",
      "schema:propertyID": [
        {
          "@id": "xas:incidentintensity"
        }
      ],
      "schema:unitText": "counts",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:uses": "xas:incidentintensity",
      "cdi:name": "i0",
      "cdi:displayLabel": "monitor intensity"
    },
    {
      "@id": "xas:transmittedintensity",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
      "schema:propertyID": [
        {
          "@id": "xas:transmittedintensity"
        }
      ],
      "schema:unitText": "counts",
      "schema:name": "itrans",
      "schema:alternateName": [
        "transmission intensity"
      ],
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:uses": "xas:transmittedintensity",
      "cdi:name": "itrans",
      "cdi:displayLabel": "transmission intensity"
    }
  ],
  "cdi:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "cdi:linkRelationship": "projectProposal",
      "cdi:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "cdi:encodingType": "text/html",
        "cdi:name": "name of the proposal",
        "cdi:url": "https://example.org/locatorForProposalText",
        "cdi:identifier": "identifier for proposal, could used text or schema:PropertyValue pattern"
      }
    }
  ],
  "schema:subjectOf": {
    "@id": "xas:ja51-pz63",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "schema:dateModified": "2025-08-26",
    "schema:creator": [
      {
        "@id": "https://ada.org/person/3479",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Richard, Stephen M.",
        "schema:identifier": "https://orcid.org/0000-0002-7933-2154",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "smrTucson@email.org"
        }
      }
    ],
    "schema:about": {
      "@id": "xas:487y54123"
    },
    "schema:description": "metadata about documentation for se_na2so4",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_structure/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/xasOptional/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/xasCore/1.0"
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "dcterms": "http://purl.org/dc/terms/",
      "spdx": "http://spdx.org/rdf/terms#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/xasDocument/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "spdx": "http://spdx.org/rdf/terms#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "time": "http://www.w3.org/2006/time#",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "csvw": "http://www.w3.org/ns/csvw#",
      "xas": "https://w3id.org/cdif/xas/",
      "nxs": "https://manual.nexusformat.org/classes/",
      "prov": "http://www.w3.org/ns/prov#",
      "dcat": "http://www.w3.org/ns/dcat#",
      "cdif": "https://cdif.org/profiles/",
      "ex": "https://example.org/",
      "igsn": "https://igsn.org/"
    }
  ],
  "@id": "xas:487y54123",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "X-ray absorption spectra for K edge, Iron metal, XDI CDIF example",
  "schema:description": "Example metadata including all properties in the CDIF XAS profile",
  "schema:identifier": "https://doi.org/10.9999/aqweropjh",
  "schema:dateModified": "2025-06-22",
  "schema:datePublished": "2025-06-22",
  "schema:creator": {
    "@list": [
      {
        "@id": "https://orcid.org/3547ulkj",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Collectus, Poindexter",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "missing@email.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "Facility",
      "schema:contributor": {
        "@type": [
          "schema:Organization"
        ],
        "@id": "https://ror.org/aps",
        "schema:name": "Argonne Synchotron"
      }
    },
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "dataCollector",
      "schema:contributor": {
        "@id": "https://orcid.org/3547ulkj"
      }
    },
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "principleInvestigator",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "@id": "https://orcid.org/35735ul",
        "schema:name": "Scienceguy, Biggus",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "missing@email.org"
        },
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "@id": "https://ror.org/lejkthoj",
          "schema:name": "Big Science Institute"
        }
      }
    }
  ],
  "schema:license": [
    "https://creativecommons.org/publicdomain/zero/1.0/"
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:TabularTextDataSet"
      ],
      "schema:name": "XDI data file for Se K-edge XAS",
      "schema:contentUrl": "https://github.com/XraySpectroscopy/XASDataLibrary/blob/master/data/Se/Se_Na2SeO4_rt_01.xdi",
      "schema:description": "Fixed-width text file conformant with XDI specification. Contains three data columns: monochromator energy (eV), transmitted intensity (counts), and incident intensity (counts). 27-line header with comment prefix '#'.",
      "schema:encodingFormat": [
        "text/plain"
      ],
      "cdi:isFixedWidth": true,
      "dcterms:conformsTo": [
        {
          "@id": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md"
        }
      ],
      "cdif:hasPhysicalMapping": [
        {
          "cdif:index": 0,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "xas:monochromatorenergy"
          }
        },
        {
          "cdif:index": 1,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "xas:transmittedintensity"
          }
        },
        {
          "cdif:index": 2,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "xas:incidentintensity"
          }
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
      "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01196",
      "schema:termCode": "XAS",
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
      "schema:identifier": "missing",
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
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "schema:Action",
        "prov:Activity"
      ],
      "schema:additionalType": [
        {
          "@id": "xas:analysisevent"
        }
      ],
      "schema:identifier": "20241111_DSC_NU_OREX-803224-0_1",
      "schema:startTime": "2008-04-10T21:58:50",
      "schema:endTime": "2008-04-10T22:14:37",
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
                  "@id": "xas:source"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "source, made up for this example",
              "schema:identifier": [
                "should have a registry with URIs"
              ],
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
                  "@id": "xas:beamline"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "13-BM-D",
              "schema:identifier": [
                "should have a registry with URIs"
              ],
              "schema:additionalProperty": [
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:collimation"
                    }
                  ],
                  "schema:name": "collimation technique",
                  "schema:value": "none"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:focusing"
                    }
                  ],
                  "schema:name": "focusing",
                  "schema:value": "???"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:harmonicrejection"
                    }
                  ],
                  "schema:name": "harmonic_rejection",
                  "schema:value": "Rh-coated mirror, detuned"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:detectortype"
                    }
                  ],
                  "schema:name": "detector",
                  "schema:value": "Vortex ME4 silicon drift detector"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:energyrange"
                    }
                  ],
                  "schema:name": "energy range",
                  "schema:value": "4.5 - 27",
                  "schema:unitText": "keV"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:energyresolution"
                    }
                  ],
                  "schema:name": "energy resolution",
                  "schema:value": "1e-4",
                  "schema:description": "delta_E/E"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:flux"
                    }
                  ],
                  "schema:name": "photon flux",
                  "schema:value": "1e11",
                  "schema:unitText": "photons/s"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:scanmode"
                    }
                  ],
                  "schema:name": "scan mode",
                  "schema:value": "step"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:spotsize"
                    }
                  ],
                  "schema:name": "beam spot size",
                  "schema:value": "500 x 500",
                  "schema:unitText": "um"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:website"
                    }
                  ],
                  "schema:name": "beamline website",
                  "schema:value": "https://www.aps.anl.gov/Beamlines/Directory/13-BM-D"
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
                      "@id": "xas:monochromatorchemicalformula"
                    }
                  ],
                  "schema:name": "chemical formula",
                  "schema:value": "Si"
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
                  "schema:value": "missing"
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
                  "@id": "xas:xraymonitor"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:name": "x-ray intensity monitor",
              "schema:additionalProperty": [
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:monitormode"
                    }
                  ],
                  "schema:name": "monitor mode",
                  "schema:value": "monitor"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:monitorpreset"
                    }
                  ],
                  "schema:name": "monitor preset",
                  "schema:value": "N.A."
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:detectori0"
                    }
                  ],
                  "schema:name": "detector mode i0",
                  "schema:alternateName": [
                    "incident flux measurement method"
                  ],
                  "schema:value": "10cm  N2"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "xas:detectorit"
                    }
                  ],
                  "schema:name": "detector mode it",
                  "schema:alternateName": [
                    "transmitted flux measurement method"
                  ],
                  "schema:value": "10cm  N2"
                }
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:pressure"
            }
          ],
          "schema:name": "experiment environment-pressure",
          "schema:description": "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential",
          "schema:value": 3567,
          "schema:unitText": "KPa"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:edgeenergy"
            }
          ],
          "schema:name": "Absorption edge",
          "schema:value": "12658.0",
          "schema:unitText": "eV"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:calibrationmethod"
            }
          ],
          "schema:name": "calibration method",
          "schema:value": "description of calibration procedure",
          "schema:url": "http://protocols.io/link/to/calibrationMethod"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:experimentdocumentation"
            }
          ],
          "schema:name": "Instrument configuration",
          "schema:value": "description of instrument configuration",
          "schema:url": "http://protocols.io/link/to/calibrationMethod"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "xas:installedoptions"
            }
          ],
          "schema:name": "Installed Options",
          "schema:value": "Description of extra equipment installed on the base instrument(?)"
        }
      ],
      "schema:location": {
        "@id": "ex:xasfacility_37yht",
        "@type": [
          "schema:Place"
        ],
        "schema:additionalType": [
          {
            "@id": "xas:facility"
          }
        ],
        "schema:identifier": "https://ror.org/aps",
        "schema:name": "APS",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:facilityenergy"
              }
            ],
            "schema:name": "Facility energy",
            "schema:value": "7.00",
            "schema:unitText": "GeV"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:facilitycurrent"
              }
            ],
            "schema:name": "Facility current",
            "schema:value": "120",
            "schema:unitText": "Amps"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:xraysourcetype"
              }
            ],
            "schema:name": "X-ray Source",
            "schema:value": "APS bending magnet"
          }
        ]
      },
      "schema:object": {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "MaterialSample",
          {
            "@id": "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          }
        ],
        "schema:name": "Na2SeO4",
        "schema:identifier": "igsn:10.6620/357lkj",
        "schema:description": "physical properties of sample: ph, eh, volume, porosity, density, concentration, resistivity, viscosity, crystal structure, opacity from xdi list...",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:porosity"
              }
            ],
            "schema:name": "Porosity",
            "schema:value": 27,
            "schema:unitText": "percent"
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
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplepreparation"
              }
            ],
            "schema:name": "samaple preparation method",
            "schema:value": "powder on tape, 6 layers"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplemass"
              }
            ],
            "schema:name": "sample mass",
            "schema:value": "10",
            "schema:unitText": "mg"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:pointgroup"
              }
            ],
            "schema:name": "crystallographic point group",
            "schema:value": "mm2"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:sampleunitcell"
              }
            ],
            "schema:name": "Crystal unit cell dimensions",
            "schema:value": "cubic; Z = 4; a = 5.46; V = 162.77"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:parentsample"
              }
            ],
            "schema:name": "parent sample identifier",
            "schema:value": "igsn:10.3476/342573"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplematerial"
              }
            ],
            "schema:name": "material state",
            "schema:value": "solid metal foil"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:concentration"
              }
            ],
            "schema:name": "concentration",
            "schema:value": "0.05",
            "schema:unitText": "mol/L"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplecrystalstructure"
              }
            ],
            "schema:name": "crystal structure",
            "schema:value": "cubic"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:density"
              }
            ],
            "schema:name": "density",
            "schema:value": "2.20",
            "schema:unitText": "g/cm^3"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:eh"
              }
            ],
            "schema:name": "redox potential (Eh)",
            "schema:value": "0.35",
            "schema:unitText": "V"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:electricfield"
              }
            ],
            "schema:name": "electric field",
            "schema:value": "0",
            "schema:unitText": "V/m"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:electrochemicalpotential"
              }
            ],
            "schema:name": "electrochemical potential",
            "schema:value": "0",
            "schema:unitText": "V"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:magneticfield"
              }
            ],
            "schema:name": "magnetic field",
            "schema:value": "0",
            "schema:unitText": "T"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:magneticmoment"
              }
            ],
            "schema:name": "magnetic moment",
            "schema:value": "0",
            "schema:unitText": "Bohr magneton"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:opacity"
              }
            ],
            "schema:name": "opacity",
            "schema:value": "opaque"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:ph"
              }
            ],
            "schema:name": "pH (acidity)",
            "schema:value": "7.4"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:samplepreparation"
              }
            ],
            "schema:name": "sample preparation (XDI Sample.prep)",
            "schema:value": "ground powder pressed to 6-layer tape mount"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:pressure"
              }
            ],
            "schema:name": "pressure",
            "schema:value": "1.013e5",
            "schema:unitText": "Pa"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:resistivity"
              }
            ],
            "schema:name": "resistivity",
            "schema:value": "1e6",
            "schema:unitText": "ohm cm"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:temperature"
              }
            ],
            "schema:name": "temperature",
            "schema:value": "298",
            "schema:unitText": "K"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:viscosity"
              }
            ],
            "schema:name": "viscosity",
            "schema:value": "not applicable (solid)"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "xas:volume"
              }
            ],
            "schema:name": "volume",
            "schema:value": "0.005",
            "schema:unitText": "cm^3"
          }
        ]
      }
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "xas:monochromatorenergy",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:name": "energy",
      "schema:alternateName": [
        "Monochromator energy"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
      "schema:propertyID": [
        {
          "@id": "xas:monochromatorenergy"
        }
      ],
      "schema:unitText": "eV",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:simpleUnitOfMeasure": "eV",
      "cdi:uses": "xas:monochromatorenergy",
      "cdi:name": "energy",
      "cdi:displayLabel": "monochromator energy"
    },
    {
      "@id": "xas:incidentintensity",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:name": "i0 monitory intensity",
      "schema:alternateName": [
        "Monitor intensity"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description)",
      "schema:propertyID": [
        {
          "@id": "xas:incidentintensity"
        }
      ],
      "schema:unitText": "counts",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:uses": "xas:incidentintensity",
      "cdi:name": "i0",
      "cdi:displayLabel": "monitor intensity"
    },
    {
      "@id": "xas:transmittedintensity",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
      "schema:propertyID": [
        {
          "@id": "xas:transmittedintensity"
        }
      ],
      "schema:unitText": "counts",
      "schema:name": "itrans",
      "schema:alternateName": [
        "transmission intensity"
      ],
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:uses": "xas:transmittedintensity",
      "cdi:name": "itrans",
      "cdi:displayLabel": "transmission intensity"
    }
  ],
  "cdi:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "cdi:linkRelationship": "projectProposal",
      "cdi:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "cdi:encodingType": "text/html",
        "cdi:name": "name of the proposal",
        "cdi:url": "https://example.org/locatorForProposalText",
        "cdi:identifier": "identifier for proposal, could used text or schema:PropertyValue pattern"
      }
    }
  ],
  "schema:subjectOf": {
    "@id": "xas:ja51-pz63",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "schema:dateModified": "2025-08-26",
    "schema:creator": [
      {
        "@id": "https://ada.org/person/3479",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Richard, Stephen M.",
        "schema:identifier": "https://orcid.org/0000-0002-7933-2154",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "smrTucson@email.org"
        }
      }
    ],
    "schema:about": {
      "@id": "xas:487y54123"
    },
    "schema:description": "metadata about documentation for se_na2so4",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_structure/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/xasOptional/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/xasCore/1.0"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/profiles/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xas: <https://w3id.org/cdif/xas/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.org/person/3479> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "smrTucson@email.org" ] ;
    schema1:identifier "https://orcid.org/0000-0002-7933-2154" ;
    schema1:name "Richard, Stephen M." .

ex:xasfacility_37yht a schema1:Place ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "X-ray Source" ;
            schema1:propertyID xas:xraysourcetype ;
            schema1:value "APS bending magnet" ],
        [ a schema1:PropertyValue ;
            schema1:name "Facility energy" ;
            schema1:propertyID xas:facilityenergy ;
            schema1:unitText "GeV" ;
            schema1:value "7.00" ],
        [ a schema1:PropertyValue ;
            schema1:name "Facility current" ;
            schema1:propertyID xas:facilitycurrent ;
            schema1:unitText "Amps" ;
            schema1:value "120" ] ;
    schema1:additionalType xas:facility ;
    schema1:identifier "https://ror.org/aps" ;
    schema1:name "APS" .

<https://orcid.org/35735ul> a schema1:Person ;
    schema1:affiliation <https://ror.org/lejkthoj> ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "missing@email.org" ] ;
    schema1:name "Scienceguy, Biggus" .

<https://ror.org/aps> a schema1:Organization ;
    schema1:name "Argonne Synchotron" .

<https://ror.org/lejkthoj> a schema1:Organization ;
    schema1:name "Big Science Institute" .

xas:487y54123 a schema1:Dataset,
        schema1:Product ;
    cdi:relatedLink [ a schema1:LinkRole ;
            cdi:linkRelationship "projectProposal" ;
            cdi:target [ a schema1:EntryPoint ;
                    cdi:encodingType "text/html" ;
                    cdi:identifier "identifier for proposal, could used text or schema:PropertyValue pattern" ;
                    cdi:name "name of the proposal" ;
                    cdi:url "https://example.org/locatorForProposalText" ] ] ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor <https://orcid.org/3547ulkj> ;
            schema1:roleName "dataCollector" ],
        [ a schema1:Role ;
            schema1:contributor <https://orcid.org/35735ul> ;
            schema1:roleName "principleInvestigator" ],
        [ a schema1:Role ;
            schema1:contributor <https://ror.org/aps> ;
            schema1:roleName "Facility" ] ;
    schema1:creator ( <https://orcid.org/3547ulkj> ) ;
    schema1:dateModified "2025-06-22" ;
    schema1:datePublished "2025-06-22" ;
    schema1:description "Example metadata including all properties in the CDIF XAS profile" ;
    schema1:distribution [ a cdi:TabularTextDataSet,
                schema1:DataDownload ;
            cdi:isFixedWidth true ;
            dcterms:conformsTo <https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md> ;
            schema1:contentUrl "https://github.com/XraySpectroscopy/XASDataLibrary/blob/master/data/Se/Se_Na2SeO4_rt_01.xdi" ;
            schema1:description "Fixed-width text file conformant with XDI specification. Contains three data columns: monochromator energy (eV), transmitted intensity (counts), and incident intensity (counts). 27-line header with comment prefix '#'." ;
            schema1:encodingFormat "text/plain" ;
            schema1:name "XDI data file for Se K-edge XAS" ;
            cdif:hasPhysicalMapping [ cdi:isRequired true ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable xas:incidentintensity ;
                    cdif:index 2 ;
                    cdif:physicalDataType "float64" ],
                [ cdi:isRequired true ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable xas:transmittedintensity ;
                    cdif:index 1 ;
                    cdif:physicalDataType "float64" ],
                [ cdi:isRequired true ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable xas:monochromatorenergy ;
                    cdif:index 0 ;
                    cdif:physicalDataType "float64" ] ] ;
    schema1:identifier "https://doi.org/10.9999/aqweropjh" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:about "element.edge" ;
            schema1:identifier "missing" ;
            schema1:inDefinedTermSet "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md" ;
            schema1:name "K-edge" ;
            schema1:termCode "K" ],
        [ a schema1:DefinedTerm ;
            schema1:about "element.symbol" ;
            schema1:identifier "http://sweetontology.net/matrElement/Selenium" ;
            schema1:inDefinedTermSet "http://sweetontology.net/matrElement" ;
            schema1:name "Selenium" ;
            schema1:termCode "Se" ] ;
    schema1:license "https://creativecommons.org/publicdomain/zero/1.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "xas:transmissionMode" ;
            schema1:inDefinedTermSet "nxs:Field/NXxas/ENTRY/DATA/mode" ;
            schema1:name "Transmission" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "http://purl.org/pan-science/PaNET/PaNET01196" ;
            schema1:inDefinedTermSet "http://purl.org/pan-science/PaNET/PaNET.owl" ;
            schema1:name "X-Ray Absorption Spectroscopy" ;
            schema1:termCode "XAS" ] ;
    schema1:name "X-ray absorption spectra for K edge, Iron metal, XDI CDIF example" ;
    schema1:subjectOf xas:ja51-pz63 ;
    schema1:variableMeasured xas:incidentintensity,
        xas:monochromatorenergy,
        xas:transmittedintensity ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:additionalProperty [ a schema1:PropertyValue ;
                    schema1:name "Absorption edge" ;
                    schema1:propertyID xas:edgeenergy ;
                    schema1:unitText "eV" ;
                    schema1:value "12658.0" ],
                [ a schema1:PropertyValue ;
                    schema1:description "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential" ;
                    schema1:name "experiment environment-pressure" ;
                    schema1:propertyID xas:pressure ;
                    schema1:unitText "KPa" ;
                    schema1:value 3567 ],
                [ a schema1:PropertyValue ;
                    schema1:name "calibration method" ;
                    schema1:propertyID xas:calibrationmethod ;
                    schema1:url "http://protocols.io/link/to/calibrationMethod" ;
                    schema1:value "description of calibration procedure" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Instrument configuration" ;
                    schema1:propertyID xas:experimentdocumentation ;
                    schema1:url "http://protocols.io/link/to/calibrationMethod" ;
                    schema1:value "description of instrument configuration" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Installed Options" ;
                    schema1:propertyID xas:installedoptions ;
                    schema1:value "Description of extra equipment installed on the base instrument(?)" ] ;
            schema1:additionalType xas:analysisevent ;
            schema1:endTime "2008-04-10T22:14:37" ;
            schema1:identifier "20241111_DSC_NU_OREX-803224-0_1" ;
            schema1:location ex:xasfacility_37yht ;
            schema1:object [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "pH (acidity)" ;
                            schema1:propertyID xas:ph ;
                            schema1:value "7.4" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "crystallographic point group" ;
                            schema1:propertyID xas:pointgroup ;
                            schema1:value "mm2" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "sample mass" ;
                            schema1:propertyID xas:samplemass ;
                            schema1:unitText "mg" ;
                            schema1:value "10" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "material state" ;
                            schema1:propertyID xas:samplematerial ;
                            schema1:value "solid metal foil" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "concentration" ;
                            schema1:propertyID xas:concentration ;
                            schema1:unitText "mol/L" ;
                            schema1:value "0.05" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "temperature" ;
                            schema1:propertyID xas:temperature ;
                            schema1:unitText "K" ;
                            schema1:value "298" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "viscosity" ;
                            schema1:propertyID xas:viscosity ;
                            schema1:value "not applicable (solid)" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "magnetic moment" ;
                            schema1:propertyID xas:magneticmoment ;
                            schema1:unitText "Bohr magneton" ;
                            schema1:value "0" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "electrochemical potential" ;
                            schema1:propertyID xas:electrochemicalpotential ;
                            schema1:unitText "V" ;
                            schema1:value "0" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Stoichiometry" ;
                            schema1:propertyID xas:samplechemicalcomposition ;
                            schema1:value "Na2SeO4" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "sample preparation (XDI Sample.prep)" ;
                            schema1:propertyID xas:samplepreparation ;
                            schema1:value "ground powder pressed to 6-layer tape mount" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Porosity" ;
                            schema1:propertyID xas:porosity ;
                            schema1:unitText "percent" ;
                            schema1:value 27 ],
                        [ a schema1:PropertyValue ;
                            schema1:name "magnetic field" ;
                            schema1:propertyID xas:magneticfield ;
                            schema1:unitText "T" ;
                            schema1:value "0" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Crystal unit cell dimensions" ;
                            schema1:propertyID xas:sampleunitcell ;
                            schema1:value "cubic; Z = 4; a = 5.46; V = 162.77" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "parent sample identifier" ;
                            schema1:propertyID xas:parentsample ;
                            schema1:value "igsn:10.3476/342573" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "opacity" ;
                            schema1:propertyID xas:opacity ;
                            schema1:value "opaque" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "resistivity" ;
                            schema1:propertyID xas:resistivity ;
                            schema1:unitText "ohm cm" ;
                            schema1:value "1e6" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "electric field" ;
                            schema1:propertyID xas:electricfield ;
                            schema1:unitText "V/m" ;
                            schema1:value "0" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "redox potential (Eh)" ;
                            schema1:propertyID xas:eh ;
                            schema1:unitText "V" ;
                            schema1:value "0.35" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "samaple preparation method" ;
                            schema1:propertyID xas:samplepreparation ;
                            schema1:value "powder on tape, 6 layers" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "volume" ;
                            schema1:propertyID xas:volume ;
                            schema1:unitText "cm^3" ;
                            schema1:value "0.005" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "pressure" ;
                            schema1:propertyID xas:pressure ;
                            schema1:unitText "Pa" ;
                            schema1:value "1.013e5" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "density" ;
                            schema1:propertyID xas:density ;
                            schema1:unitText "g/cm^3" ;
                            schema1:value "2.20" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "crystal structure" ;
                            schema1:propertyID xas:samplecrystalstructure ;
                            schema1:value "cubic" ] ;
                    schema1:additionalType <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample>,
                        "MaterialSample" ;
                    schema1:description "physical properties of sample: ph, eh, volume, porosity, density, concentration, resistivity, viscosity, crystal structure, opacity from xdi list..." ;
                    schema1:identifier "igsn:10.6620/357lkj" ;
                    schema1:name "Na2SeO4" ] ;
            schema1:startTime "2008-04-10T21:58:50" ;
            prov:used [ schema1:instrument [ a schema1:Product,
                                schema1:Thing,
                                prov:Entity ;
                            schema1:additionalProperty [ a schema1:PropertyValue ;
                                    schema1:name "x-ray source" ;
                                    schema1:propertyID xas:xraysourcetype ;
                                    schema1:value "Synchrotron X-ray Source" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "Probe" ;
                                    schema1:propertyID xas:probe ;
                                    schema1:value "x-ray" ] ;
                            schema1:additionalType xas:source,
                                wd:Q3099911 ;
                            schema1:identifier "should have a registry with URIs" ;
                            schema1:name "source, made up for this example" ] ],
                [ schema1:instrument [ a schema1:Product,
                                schema1:Thing,
                                prov:Entity ;
                            schema1:additionalProperty [ a schema1:PropertyValue ;
                                    schema1:name "chemical formula" ;
                                    schema1:propertyID xas:monochromatorchemicalformula ;
                                    schema1:value "Si" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "d-spacing" ;
                                    schema1:propertyID xas:dspacing ;
                                    schema1:unitText "Angstrom" ;
                                    schema1:value "3.13550" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "crystal type" ;
                                    schema1:propertyID xas:monochromatortype ;
                                    schema1:value "missing" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "reflection plane (hkl)" ;
                                    schema1:propertyID xas:reflectionplane ;
                                    schema1:value "1,1,1" ] ;
                            schema1:additionalType xas:xraymonochromator,
                                wd:Q3099911 ;
                            schema1:name "Si 111" ] ],
                [ schema1:instrument [ a schema1:Product,
                                schema1:Thing,
                                prov:Entity ;
                            schema1:additionalProperty [ a schema1:PropertyValue ;
                                    schema1:alternateName "incident flux measurement method" ;
                                    schema1:name "detector mode i0" ;
                                    schema1:propertyID xas:detectori0 ;
                                    schema1:value "10cm  N2" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "monitor preset" ;
                                    schema1:propertyID xas:monitorpreset ;
                                    schema1:value "N.A." ],
                                [ a schema1:PropertyValue ;
                                    schema1:alternateName "transmitted flux measurement method" ;
                                    schema1:name "detector mode it" ;
                                    schema1:propertyID xas:detectorit ;
                                    schema1:value "10cm  N2" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "monitor mode" ;
                                    schema1:propertyID xas:monitormode ;
                                    schema1:value "monitor" ] ;
                            schema1:additionalType xas:xraymonitor,
                                wd:Q3099911 ;
                            schema1:name "x-ray intensity monitor" ] ],
                [ schema1:instrument [ a schema1:Product,
                                schema1:Thing,
                                prov:Entity ;
                            schema1:additionalProperty [ a schema1:PropertyValue ;
                                    schema1:name "beamline website" ;
                                    schema1:propertyID xas:website ;
                                    schema1:value "https://www.aps.anl.gov/Beamlines/Directory/13-BM-D" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "harmonic_rejection" ;
                                    schema1:propertyID xas:harmonicrejection ;
                                    schema1:value "Rh-coated mirror, detuned" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "detector" ;
                                    schema1:propertyID xas:detectortype ;
                                    schema1:value "Vortex ME4 silicon drift detector" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "scan mode" ;
                                    schema1:propertyID xas:scanmode ;
                                    schema1:value "step" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "collimation technique" ;
                                    schema1:propertyID xas:collimation ;
                                    schema1:value "none" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "photon flux" ;
                                    schema1:propertyID xas:flux ;
                                    schema1:unitText "photons/s" ;
                                    schema1:value "1e11" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "energy range" ;
                                    schema1:propertyID xas:energyrange ;
                                    schema1:unitText "keV" ;
                                    schema1:value "4.5 - 27" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "beam spot size" ;
                                    schema1:propertyID xas:spotsize ;
                                    schema1:unitText "um" ;
                                    schema1:value "500 x 500" ],
                                [ a schema1:PropertyValue ;
                                    schema1:description "delta_E/E" ;
                                    schema1:name "energy resolution" ;
                                    schema1:propertyID xas:energyresolution ;
                                    schema1:value "1e-4" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "focusing" ;
                                    schema1:propertyID xas:focusing ;
                                    schema1:value "???" ] ;
                            schema1:additionalType xas:beamline,
                                wd:Q3099911 ;
                            schema1:identifier "should have a registry with URIs" ;
                            schema1:name "13-BM-D" ] ] ] .

xas:ja51-pz63 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/data_description/1.1>,
        <https://w3id.org/cdif/data_structure/1.1>,
        <https://w3id.org/cdif/discovery/1.1>,
        <https://w3id.org/cdif/xasCore/1.0>,
        <https://w3id.org/cdif/xasOptional/1.0> ;
    schema1:about xas:487y54123 ;
    schema1:additionalType dcat:CatalogRecord ;
    schema1:creator <https://ada.org/person/3479> ;
    schema1:dateModified "2025-08-26" ;
    schema1:description "metadata about documentation for se_na2so4" .

<https://orcid.org/3547ulkj> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "missing@email.org" ] ;
    schema1:name "Collectus, Poindexter" .

xas:incidentintensity a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "monitor intensity" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "i0" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:uses "xas:incidentintensity" ;
    schema1:alternateName "Monitor intensity" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description)" ;
    schema1:name "i0 monitory intensity" ;
    schema1:propertyID xas:incidentintensity ;
    schema1:unitText "counts" .

xas:monochromatorenergy a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "monochromator energy" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "energy" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:simpleUnitOfMeasure "eV" ;
    cdi:uses "xas:monochromatorenergy" ;
    schema1:alternateName "Monochromator energy" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description" ;
    schema1:name "energy" ;
    schema1:propertyID xas:monochromatorenergy ;
    schema1:unitText "eV" .

xas:transmittedintensity a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "transmission intensity" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "itrans" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:uses "xas:transmittedintensity" ;
    schema1:alternateName "transmission intensity" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description" ;
    schema1:name "itrans" ;
    schema1:propertyID xas:transmittedintensity ;
    schema1:unitText "counts" .


```


### UKDS/Dataverse-derived XAS record.
Se_Na2SeO4 K-edge XAS record adapted from the UKDSResearch/cdif-xas
prototype (see CHANGES-from-UKDS.md for the transformation log).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "xas": "https://w3id.org/cdif/xas/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "ex:dataset/DV/BYSPHH",
  "@type": [
    "schema:Dataset"
  ],
  "schema:contributor": [
    {
      "@id": "_:b18",
      "@type": [
        "schema:Role"
      ],
      "schema:contributor": {
        "@id": "_:b19",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Richards, Steve"
      },
      "schema:roleName": "Author"
    },
    {
      "@id": "_:b20",
      "@type": [
        "schema:Role"
      ],
      "schema:contributor": {
        "@id": "_:b21",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Richards, Steve"
      },
      "schema:roleName": "Creator"
    },
    {
      "@id": "_:b22",
      "@type": [
        "schema:Role"
      ],
      "schema:contributor": {
        "@id": "_:b23",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "APS"
      },
      "schema:roleName": "Facility"
    }
  ],
  "schema:dateModified": "2026-06-24",
  "schema:description": "Se_Na2SeO4_rt_01.xdi",
  "schema:distribution": [
    {
      "@id": "_:b25",
      "@type": [
        "cdi:PhysicalDataSet",
        "cdi:TabularTextDataSet",
        "schema:DataDownload"
      ],
      "cdi:arrayBase": 1,
      "cdi:commentPrefix": "#",
      "cdi:hasHeader": true,
      "cdi:isDelimited": false,
      "cdi:isFixedWidth": true,
      "cdi:isStructuredBy": {
        "@id": "ex:struct/DV/BYSPHH",
        "@type": [
          "cdi:WideDataStructure"
        ],
        "cdi:has_DataStructureComponent": [
          {
            "@id": "ex:struct/DV/BYSPHH/comp/Column_1",
            "@type": [
              "cdi:MeasureComponent"
            ],
            "cdif:isDefinedBy_RepresentedVariable": {
              "@id": "ex:struct/DV/BYSPHH/rv/Column_1",
              "cdif:name": [
                "energy"
              ]
            }
          },
          {
            "@id": "ex:struct/DV/BYSPHH/comp/Column_2",
            "@type": [
              "cdi:MeasureComponent"
            ],
            "cdif:isDefinedBy_RepresentedVariable": {
              "@id": "ex:struct/DV/BYSPHH/rv/Column_2",
              "cdif:name": [
                "time"
              ]
            }
          },
          {
            "@id": "ex:struct/DV/BYSPHH/comp/Column_3",
            "@type": [
              "cdi:MeasureComponent"
            ],
            "cdif:isDefinedBy_RepresentedVariable": {
              "@id": "ex:struct/DV/BYSPHH/rv/Column_3",
              "cdif:name": [
                "i0"
              ]
            }
          },
          {
            "@id": "ex:struct/DV/BYSPHH/comp/Column_4",
            "@type": [
              "cdi:MeasureComponent"
            ],
            "cdif:isDefinedBy_RepresentedVariable": {
              "@id": "ex:struct/DV/BYSPHH/rv/Column_4",
              "cdif:name": [
                "itrans"
              ]
            }
          }
        ]
      },
      "cdi:skipInitialSpace": true,
      "dcterms:conformsTo": [
        {
          "@id": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md"
        }
      ],
      "schema:contentSize": "29783",
      "schema:contentUrl": "http://localhost:8080/api/access/datafile/29",
      "schema:description": "Se_Na2SeO4_rt_01.xdi",
      "schema:encodingFormat": [
        "application/octet-stream"
      ],
      "cdif:hasPhysicalMapping": [
        {
          "@id": "_:b0",
          "cdi:maximumLength": 15,
          "cdi:minimumLength": 15,
          "cdif:format": "decimal",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:DV/BYSPHH/iv/Column_1"
          },
          "cdif:index": 1,
          "cdif:physicalDataType": "decimal"
        },
        {
          "@id": "_:b1",
          "cdi:maximumLength": 15,
          "cdi:minimumLength": 15,
          "cdif:format": "decimal",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:DV/BYSPHH/iv/Column_2"
          },
          "cdif:index": 2,
          "cdif:physicalDataType": "decimal"
        },
        {
          "@id": "_:b2",
          "cdi:maximumLength": 15,
          "cdi:minimumLength": 15,
          "cdif:format": "decimal",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:DV/BYSPHH/iv/Column_3"
          },
          "cdif:index": 3,
          "cdif:physicalDataType": "decimal"
        },
        {
          "@id": "_:b3",
          "cdi:maximumLength": 15,
          "cdi:minimumLength": 15,
          "cdif:format": "decimal",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:DV/BYSPHH/iv/Column_4"
          },
          "cdif:index": 4,
          "cdif:physicalDataType": "decimal"
        }
      ]
    }
  ],
  "schema:identifier": "http://localhost:8080/citation?persistentId=perma:DV/BYSPHH",
  "schema:keywords": [
    {
      "@id": "_:b11",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:inDefinedTermSet": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md",
      "schema:name": "K-edge",
      "schema:termCode": "K",
      "schema:about": "element.edge"
    },
    {
      "@id": "_:b12",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Selenium",
      "schema:identifier": "http://sweetontology.net/matrElement/Selenium",
      "schema:inDefinedTermSet": "http://sweetontology.net/matrElement",
      "schema:termCode": "Se",
      "schema:about": "element.symbol"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Earth and Environmental Sciences",
      "schema:inDefinedTermSet": "https://data.crossref.org/reports/schemes.html"
    }
  ],
  "schema:license": [
    "http://creativecommons.org/publicdomain/zero/1.0"
  ],
  "schema:measurementTechnique": [
    {
      "@id": "_:b15",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:inDefinedTermSet": "nxs:Field/NXxas/ENTRY/DATA/mode",
      "schema:name": "Transmission"
    },
    {
      "@id": "_:b16",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01196",
      "schema:inDefinedTermSet": "http://purl.org/pan-science/PaNET/PaNET.owl",
      "schema:name": "X-Ray Absorption Spectroscopy",
      "schema:termCode": "XAS"
    }
  ],
  "schema:name": "Se_Na2SeO4_rt_01",
  "schema:sameAs": [
    "https://github.com/CDIF-4-XAS/XAS-CDIF/blob/main/se_na2so4_rt.xdi"
  ],
  "schema:subjectOf": {
    "@id": "ex:dataset/DV/BYSPHH/metadata",
    "@type": [
      "schema:Dataset"
    ],
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_structure/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/xasCore/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/xasOptional/1.0"
      }
    ],
    "schema:about": {
      "@id": "ex:dataset/DV/BYSPHH"
    },
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ]
  },
  "schema:url": "http://localhost:8080/api/access/datafile/29",
  "schema:variableMeasured": [
    {
      "@id": "ex:DV/BYSPHH/iv/Column_1",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:alternateName": [
        "mono energy"
      ],
      "schema:description": "mono energy",
      "schema:name": "energy",
      "schema:propertyID": [
        {
          "@id": "xas:monochromatorenergy"
        }
      ],
      "schema:unitText": "eV",
      "cdif:uses": [
        "https://example.org/struct/DV/BYSPHH/rv/Column_1"
      ]
    },
    {
      "@id": "ex:DV/BYSPHH/iv/Column_2",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:alternateName": [
        "time"
      ],
      "schema:description": "time",
      "schema:name": "time",
      "schema:propertyID": [
        {
          "@id": "xas:time"
        }
      ],
      "schema:unitText": "",
      "cdif:uses": [
        "https://example.org/struct/DV/BYSPHH/rv/Column_2"
      ]
    },
    {
      "@id": "ex:DV/BYSPHH/iv/Column_3",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:alternateName": [
        "monitor intensity"
      ],
      "schema:description": "monitor intensity",
      "schema:name": "i0",
      "schema:propertyID": [
        {
          "@id": "xas:incidentintensity"
        }
      ],
      "schema:unitText": "",
      "cdif:uses": [
        "https://example.org/struct/DV/BYSPHH/rv/Column_3"
      ]
    },
    {
      "@id": "ex:DV/BYSPHH/iv/Column_4",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:alternateName": [
        "transmission intensity"
      ],
      "schema:description": "transmission intensity",
      "schema:name": "itrans",
      "schema:propertyID": [
        {
          "@id": "xas:transmittedintensity"
        }
      ],
      "schema:unitText": "",
      "cdif:uses": [
        "https://example.org/struct/DV/BYSPHH/rv/Column_4"
      ]
    }
  ],
  "schema:version": "5",
  "prov:wasGeneratedBy": [
    {
      "@id": "xas:provevent",
      "@type": [
        "schema:Action",
        "prov:Activity"
      ],
      "schema:additionalType": [
        {
          "@id": "xas:analysisevent"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "_:b24",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:name": "Edge energy",
          "schema:propertyID": [
            {
              "@id": "xas:edgeenergy"
            }
          ],
          "schema:value": "12658.0",
          "schema:unitText": "eV"
        }
      ],
      "schema:startTime": "2008-04-10T21:58:50",
      "schema:endTime": "2008-04-10T22:14:37",
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
                  "schema:name": "X-ray source",
                  "schema:propertyID": [
                    {
                      "@id": "xas:xraysourcetype"
                    }
                  ],
                  "schema:value": "Synchrotron X-ray Source"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "Probe",
                  "schema:propertyID": [
                    {
                      "@id": "xas:probe"
                    }
                  ],
                  "schema:value": "x-ray"
                }
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "@id": "_:b4",
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
              "schema:identifier": [
                "xas:Beamline/13-BM-D"
              ],
              "schema:name": "13-BM-D",
              "schema:additionalProperty": [
                {
                  "@id": "_:b5",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "collimation",
                  "schema:propertyID": [
                    {
                      "@id": "xas:collimation"
                    }
                  ],
                  "schema:value": "none"
                },
                {
                  "@id": "_:b6",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "focusing",
                  "schema:propertyID": [
                    {
                      "@id": "xas:focusing"
                    }
                  ],
                  "schema:value": "no"
                },
                {
                  "@id": "_:b7",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "harmonic rejection",
                  "schema:propertyID": [
                    {
                      "@id": "xas:harmonicrejection"
                    }
                  ],
                  "schema:value": "Rh-coated mirror, detuned "
                }
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "@id": "_:b13",
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
              "schema:identifier": [
                "xas:Mono/Si 111"
              ],
              "schema:name": "Si 111",
              "schema:additionalProperty": [
                {
                  "@id": "_:b14",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "d-spacing",
                  "schema:propertyID": [
                    {
                      "@id": "xas:dspacing"
                    }
                  ],
                  "schema:value": "3.13550",
                  "schema:unitText": "Angstrom"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "crystal type",
                  "schema:propertyID": [
                    {
                      "@id": "xas:monochromatortype"
                    }
                  ],
                  "schema:value": "Si"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "reflection plane",
                  "schema:propertyID": [
                    {
                      "@id": "xas:reflectionplane"
                    }
                  ],
                  "schema:value": "1,1,1"
                }
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "@id": "_:b8",
              "@type": [
                "schema:Thing",
                "schema:Product",
                "prov:Entity"
              ],
              "schema:additionalType": [
                {
                  "@id": "xas:xraymonitor"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:identifier": [
                "xas:Detector"
              ],
              "schema:name": "x-ray intensity monitor",
              "schema:additionalProperty": [
                {
                  "@id": "_:b9",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "incident-flux detection method",
                  "schema:propertyID": [
                    {
                      "@id": "xas:detectori0"
                    }
                  ],
                  "schema:value": "10cm  N2"
                },
                {
                  "@id": "_:b10",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "transmitted-flux detection method",
                  "schema:propertyID": [
                    {
                      "@id": "xas:detectorit"
                    }
                  ],
                  "schema:value": "10cm  N2 (?)"
                }
              ]
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
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/xasDocument/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "ex": "https://example.org/",
      "nxs": "https://manual.nexusformat.org/classes/",
      "xas": "https://w3id.org/cdif/xas/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@id": "ex:dataset/DV/BYSPHH",
  "@type": [
    "schema:Dataset"
  ],
  "schema:contributor": [
    {
      "@id": "_:b18",
      "@type": [
        "schema:Role"
      ],
      "schema:contributor": {
        "@id": "_:b19",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Richards, Steve"
      },
      "schema:roleName": "Author"
    },
    {
      "@id": "_:b20",
      "@type": [
        "schema:Role"
      ],
      "schema:contributor": {
        "@id": "_:b21",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Richards, Steve"
      },
      "schema:roleName": "Creator"
    },
    {
      "@id": "_:b22",
      "@type": [
        "schema:Role"
      ],
      "schema:contributor": {
        "@id": "_:b23",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "APS"
      },
      "schema:roleName": "Facility"
    }
  ],
  "schema:dateModified": "2026-06-24",
  "schema:description": "Se_Na2SeO4_rt_01.xdi",
  "schema:distribution": [
    {
      "@id": "_:b25",
      "@type": [
        "cdi:PhysicalDataSet",
        "cdi:TabularTextDataSet",
        "schema:DataDownload"
      ],
      "cdi:arrayBase": 1,
      "cdi:commentPrefix": "#",
      "cdi:hasHeader": true,
      "cdi:isDelimited": false,
      "cdi:isFixedWidth": true,
      "cdi:isStructuredBy": {
        "@id": "ex:struct/DV/BYSPHH",
        "@type": [
          "cdi:WideDataStructure"
        ],
        "cdi:has_DataStructureComponent": [
          {
            "@id": "ex:struct/DV/BYSPHH/comp/Column_1",
            "@type": [
              "cdi:MeasureComponent"
            ],
            "cdif:isDefinedBy_RepresentedVariable": {
              "@id": "ex:struct/DV/BYSPHH/rv/Column_1",
              "cdif:name": [
                "energy"
              ]
            }
          },
          {
            "@id": "ex:struct/DV/BYSPHH/comp/Column_2",
            "@type": [
              "cdi:MeasureComponent"
            ],
            "cdif:isDefinedBy_RepresentedVariable": {
              "@id": "ex:struct/DV/BYSPHH/rv/Column_2",
              "cdif:name": [
                "time"
              ]
            }
          },
          {
            "@id": "ex:struct/DV/BYSPHH/comp/Column_3",
            "@type": [
              "cdi:MeasureComponent"
            ],
            "cdif:isDefinedBy_RepresentedVariable": {
              "@id": "ex:struct/DV/BYSPHH/rv/Column_3",
              "cdif:name": [
                "i0"
              ]
            }
          },
          {
            "@id": "ex:struct/DV/BYSPHH/comp/Column_4",
            "@type": [
              "cdi:MeasureComponent"
            ],
            "cdif:isDefinedBy_RepresentedVariable": {
              "@id": "ex:struct/DV/BYSPHH/rv/Column_4",
              "cdif:name": [
                "itrans"
              ]
            }
          }
        ]
      },
      "cdi:skipInitialSpace": true,
      "dcterms:conformsTo": [
        {
          "@id": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md"
        }
      ],
      "schema:contentSize": "29783",
      "schema:contentUrl": "http://localhost:8080/api/access/datafile/29",
      "schema:description": "Se_Na2SeO4_rt_01.xdi",
      "schema:encodingFormat": [
        "application/octet-stream"
      ],
      "cdif:hasPhysicalMapping": [
        {
          "@id": "_:b0",
          "cdi:maximumLength": 15,
          "cdi:minimumLength": 15,
          "cdif:format": "decimal",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:DV/BYSPHH/iv/Column_1"
          },
          "cdif:index": 1,
          "cdif:physicalDataType": "decimal"
        },
        {
          "@id": "_:b1",
          "cdi:maximumLength": 15,
          "cdi:minimumLength": 15,
          "cdif:format": "decimal",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:DV/BYSPHH/iv/Column_2"
          },
          "cdif:index": 2,
          "cdif:physicalDataType": "decimal"
        },
        {
          "@id": "_:b2",
          "cdi:maximumLength": 15,
          "cdi:minimumLength": 15,
          "cdif:format": "decimal",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:DV/BYSPHH/iv/Column_3"
          },
          "cdif:index": 3,
          "cdif:physicalDataType": "decimal"
        },
        {
          "@id": "_:b3",
          "cdi:maximumLength": 15,
          "cdi:minimumLength": 15,
          "cdif:format": "decimal",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:DV/BYSPHH/iv/Column_4"
          },
          "cdif:index": 4,
          "cdif:physicalDataType": "decimal"
        }
      ]
    }
  ],
  "schema:identifier": "http://localhost:8080/citation?persistentId=perma:DV/BYSPHH",
  "schema:keywords": [
    {
      "@id": "_:b11",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:inDefinedTermSet": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md",
      "schema:name": "K-edge",
      "schema:termCode": "K",
      "schema:about": "element.edge"
    },
    {
      "@id": "_:b12",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Selenium",
      "schema:identifier": "http://sweetontology.net/matrElement/Selenium",
      "schema:inDefinedTermSet": "http://sweetontology.net/matrElement",
      "schema:termCode": "Se",
      "schema:about": "element.symbol"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Earth and Environmental Sciences",
      "schema:inDefinedTermSet": "https://data.crossref.org/reports/schemes.html"
    }
  ],
  "schema:license": [
    "http://creativecommons.org/publicdomain/zero/1.0"
  ],
  "schema:measurementTechnique": [
    {
      "@id": "_:b15",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:inDefinedTermSet": "nxs:Field/NXxas/ENTRY/DATA/mode",
      "schema:name": "Transmission"
    },
    {
      "@id": "_:b16",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01196",
      "schema:inDefinedTermSet": "http://purl.org/pan-science/PaNET/PaNET.owl",
      "schema:name": "X-Ray Absorption Spectroscopy",
      "schema:termCode": "XAS"
    }
  ],
  "schema:name": "Se_Na2SeO4_rt_01",
  "schema:sameAs": [
    "https://github.com/CDIF-4-XAS/XAS-CDIF/blob/main/se_na2so4_rt.xdi"
  ],
  "schema:subjectOf": {
    "@id": "ex:dataset/DV/BYSPHH/metadata",
    "@type": [
      "schema:Dataset"
    ],
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_structure/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/xasCore/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/xasOptional/1.0"
      }
    ],
    "schema:about": {
      "@id": "ex:dataset/DV/BYSPHH"
    },
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ]
  },
  "schema:url": "http://localhost:8080/api/access/datafile/29",
  "schema:variableMeasured": [
    {
      "@id": "ex:DV/BYSPHH/iv/Column_1",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:alternateName": [
        "mono energy"
      ],
      "schema:description": "mono energy",
      "schema:name": "energy",
      "schema:propertyID": [
        {
          "@id": "xas:monochromatorenergy"
        }
      ],
      "schema:unitText": "eV",
      "cdif:uses": [
        "https://example.org/struct/DV/BYSPHH/rv/Column_1"
      ]
    },
    {
      "@id": "ex:DV/BYSPHH/iv/Column_2",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:alternateName": [
        "time"
      ],
      "schema:description": "time",
      "schema:name": "time",
      "schema:propertyID": [
        {
          "@id": "xas:time"
        }
      ],
      "schema:unitText": "",
      "cdif:uses": [
        "https://example.org/struct/DV/BYSPHH/rv/Column_2"
      ]
    },
    {
      "@id": "ex:DV/BYSPHH/iv/Column_3",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:alternateName": [
        "monitor intensity"
      ],
      "schema:description": "monitor intensity",
      "schema:name": "i0",
      "schema:propertyID": [
        {
          "@id": "xas:incidentintensity"
        }
      ],
      "schema:unitText": "",
      "cdif:uses": [
        "https://example.org/struct/DV/BYSPHH/rv/Column_3"
      ]
    },
    {
      "@id": "ex:DV/BYSPHH/iv/Column_4",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:alternateName": [
        "transmission intensity"
      ],
      "schema:description": "transmission intensity",
      "schema:name": "itrans",
      "schema:propertyID": [
        {
          "@id": "xas:transmittedintensity"
        }
      ],
      "schema:unitText": "",
      "cdif:uses": [
        "https://example.org/struct/DV/BYSPHH/rv/Column_4"
      ]
    }
  ],
  "schema:version": "5",
  "prov:wasGeneratedBy": [
    {
      "@id": "xas:provevent",
      "@type": [
        "schema:Action",
        "prov:Activity"
      ],
      "schema:additionalType": [
        {
          "@id": "xas:analysisevent"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "_:b24",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:name": "Edge energy",
          "schema:propertyID": [
            {
              "@id": "xas:edgeenergy"
            }
          ],
          "schema:value": "12658.0",
          "schema:unitText": "eV"
        }
      ],
      "schema:startTime": "2008-04-10T21:58:50",
      "schema:endTime": "2008-04-10T22:14:37",
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
                  "schema:name": "X-ray source",
                  "schema:propertyID": [
                    {
                      "@id": "xas:xraysourcetype"
                    }
                  ],
                  "schema:value": "Synchrotron X-ray Source"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "Probe",
                  "schema:propertyID": [
                    {
                      "@id": "xas:probe"
                    }
                  ],
                  "schema:value": "x-ray"
                }
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "@id": "_:b4",
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
              "schema:identifier": [
                "xas:Beamline/13-BM-D"
              ],
              "schema:name": "13-BM-D",
              "schema:additionalProperty": [
                {
                  "@id": "_:b5",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "collimation",
                  "schema:propertyID": [
                    {
                      "@id": "xas:collimation"
                    }
                  ],
                  "schema:value": "none"
                },
                {
                  "@id": "_:b6",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "focusing",
                  "schema:propertyID": [
                    {
                      "@id": "xas:focusing"
                    }
                  ],
                  "schema:value": "no"
                },
                {
                  "@id": "_:b7",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "harmonic rejection",
                  "schema:propertyID": [
                    {
                      "@id": "xas:harmonicrejection"
                    }
                  ],
                  "schema:value": "Rh-coated mirror, detuned "
                }
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "@id": "_:b13",
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
              "schema:identifier": [
                "xas:Mono/Si 111"
              ],
              "schema:name": "Si 111",
              "schema:additionalProperty": [
                {
                  "@id": "_:b14",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "d-spacing",
                  "schema:propertyID": [
                    {
                      "@id": "xas:dspacing"
                    }
                  ],
                  "schema:value": "3.13550",
                  "schema:unitText": "Angstrom"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "crystal type",
                  "schema:propertyID": [
                    {
                      "@id": "xas:monochromatortype"
                    }
                  ],
                  "schema:value": "Si"
                },
                {
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "reflection plane",
                  "schema:propertyID": [
                    {
                      "@id": "xas:reflectionplane"
                    }
                  ],
                  "schema:value": "1,1,1"
                }
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "@id": "_:b8",
              "@type": [
                "schema:Thing",
                "schema:Product",
                "prov:Entity"
              ],
              "schema:additionalType": [
                {
                  "@id": "xas:xraymonitor"
                },
                {
                  "@id": "wd:Q3099911"
                }
              ],
              "schema:identifier": [
                "xas:Detector"
              ],
              "schema:name": "x-ray intensity monitor",
              "schema:additionalProperty": [
                {
                  "@id": "_:b9",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "incident-flux detection method",
                  "schema:propertyID": [
                    {
                      "@id": "xas:detectori0"
                    }
                  ],
                  "schema:value": "10cm  N2"
                },
                {
                  "@id": "_:b10",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:name": "transmitted-flux detection method",
                  "schema:propertyID": [
                    {
                      "@id": "xas:detectorit"
                    }
                  ],
                  "schema:value": "10cm  N2 (?)"
                }
              ]
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
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xas: <https://w3id.org/cdif/xas/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/dataset/DV/BYSPHH> a schema1:Dataset ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor [ a schema1:Person ;
                    schema1:name "Richards, Steve" ] ;
            schema1:roleName "Author" ],
        [ a schema1:Role ;
            schema1:contributor [ a schema1:Person ;
                    schema1:name "Richards, Steve" ] ;
            schema1:roleName "Creator" ],
        [ a schema1:Role ;
            schema1:contributor [ a schema1:Organization ;
                    schema1:name "APS" ] ;
            schema1:roleName "Facility" ] ;
    schema1:dateModified "2026-06-24" ;
    schema1:description "Se_Na2SeO4_rt_01.xdi" ;
    schema1:distribution [ a cdi:PhysicalDataSet,
                cdi:TabularTextDataSet,
                schema1:DataDownload ;
            cdi:arrayBase 1 ;
            cdi:commentPrefix "#" ;
            cdi:hasHeader true ;
            cdi:isDelimited false ;
            cdi:isFixedWidth true ;
            cdi:isStructuredBy <https://example.org/struct/DV/BYSPHH> ;
            cdi:skipInitialSpace true ;
            dcterms:conformsTo <https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md> ;
            schema1:contentSize "29783" ;
            schema1:contentUrl "http://localhost:8080/api/access/datafile/29" ;
            schema1:description "Se_Na2SeO4_rt_01.xdi" ;
            schema1:encodingFormat "application/octet-stream" ;
            cdif:hasPhysicalMapping [ cdi:maximumLength 15 ;
                    cdi:minimumLength 15 ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable <https://example.org/DV/BYSPHH/iv/Column_1> ;
                    cdif:index 1 ;
                    cdif:physicalDataType "decimal" ],
                [ cdi:maximumLength 15 ;
                    cdi:minimumLength 15 ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable <https://example.org/DV/BYSPHH/iv/Column_2> ;
                    cdif:index 2 ;
                    cdif:physicalDataType "decimal" ],
                [ cdi:maximumLength 15 ;
                    cdi:minimumLength 15 ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable <https://example.org/DV/BYSPHH/iv/Column_3> ;
                    cdif:index 3 ;
                    cdif:physicalDataType "decimal" ],
                [ cdi:maximumLength 15 ;
                    cdi:minimumLength 15 ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable <https://example.org/DV/BYSPHH/iv/Column_4> ;
                    cdif:index 4 ;
                    cdif:physicalDataType "decimal" ] ] ;
    schema1:identifier "http://localhost:8080/citation?persistentId=perma:DV/BYSPHH" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://data.crossref.org/reports/schemes.html" ;
            schema1:name "Earth and Environmental Sciences" ],
        [ a schema1:DefinedTerm ;
            schema1:about "element.edge" ;
            schema1:inDefinedTermSet "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md" ;
            schema1:name "K-edge" ;
            schema1:termCode "K" ],
        [ a schema1:DefinedTerm ;
            schema1:about "element.symbol" ;
            schema1:identifier "http://sweetontology.net/matrElement/Selenium" ;
            schema1:inDefinedTermSet "http://sweetontology.net/matrElement" ;
            schema1:name "Selenium" ;
            schema1:termCode "Se" ] ;
    schema1:license "http://creativecommons.org/publicdomain/zero/1.0" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "nxs:Field/NXxas/ENTRY/DATA/mode" ;
            schema1:name "Transmission" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "http://purl.org/pan-science/PaNET/PaNET01196" ;
            schema1:inDefinedTermSet "http://purl.org/pan-science/PaNET/PaNET.owl" ;
            schema1:name "X-Ray Absorption Spectroscopy" ;
            schema1:termCode "XAS" ] ;
    schema1:name "Se_Na2SeO4_rt_01" ;
    schema1:sameAs "https://github.com/CDIF-4-XAS/XAS-CDIF/blob/main/se_na2so4_rt.xdi" ;
    schema1:subjectOf <https://example.org/dataset/DV/BYSPHH/metadata> ;
    schema1:url "http://localhost:8080/api/access/datafile/29" ;
    schema1:variableMeasured <https://example.org/DV/BYSPHH/iv/Column_1>,
        <https://example.org/DV/BYSPHH/iv/Column_2>,
        <https://example.org/DV/BYSPHH/iv/Column_3>,
        <https://example.org/DV/BYSPHH/iv/Column_4> ;
    schema1:version "5" ;
    prov:wasGeneratedBy xas:provevent .

<https://example.org/dataset/DV/BYSPHH/metadata> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/data_description/1.1>,
        <https://w3id.org/cdif/data_structure/1.1>,
        <https://w3id.org/cdif/discovery/1.1>,
        <https://w3id.org/cdif/xasCore/1.0>,
        <https://w3id.org/cdif/xasOptional/1.0> ;
    schema1:about <https://example.org/dataset/DV/BYSPHH> ;
    schema1:additionalType dcat:CatalogRecord .

<https://example.org/struct/DV/BYSPHH> a cdi:WideDataStructure ;
    cdi:has_DataStructureComponent <https://example.org/struct/DV/BYSPHH/comp/Column_1>,
        <https://example.org/struct/DV/BYSPHH/comp/Column_2>,
        <https://example.org/struct/DV/BYSPHH/comp/Column_3>,
        <https://example.org/struct/DV/BYSPHH/comp/Column_4> .

<https://example.org/struct/DV/BYSPHH/comp/Column_1> a cdi:MeasureComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/DV/BYSPHH/rv/Column_1> .

<https://example.org/struct/DV/BYSPHH/comp/Column_2> a cdi:MeasureComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/DV/BYSPHH/rv/Column_2> .

<https://example.org/struct/DV/BYSPHH/comp/Column_3> a cdi:MeasureComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/DV/BYSPHH/rv/Column_3> .

<https://example.org/struct/DV/BYSPHH/comp/Column_4> a cdi:MeasureComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/DV/BYSPHH/rv/Column_4> .

<https://example.org/struct/DV/BYSPHH/rv/Column_1> cdif:name "energy" .

<https://example.org/struct/DV/BYSPHH/rv/Column_2> cdif:name "time" .

<https://example.org/struct/DV/BYSPHH/rv/Column_3> cdif:name "i0" .

<https://example.org/struct/DV/BYSPHH/rv/Column_4> cdif:name "itrans" .

xas:provevent a schema1:Action,
        prov:Activity ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Edge energy" ;
            schema1:propertyID xas:edgeenergy ;
            schema1:unitText "eV" ;
            schema1:value "12658.0" ] ;
    schema1:additionalType xas:analysisevent ;
    schema1:endTime "2008-04-10T22:14:37" ;
    schema1:startTime "2008-04-10T21:58:50" ;
    prov:used [ schema1:instrument [ a schema1:Product,
                        schema1:Thing,
                        prov:Entity ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "crystal type" ;
                            schema1:propertyID xas:monochromatortype ;
                            schema1:value "Si" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "reflection plane" ;
                            schema1:propertyID xas:reflectionplane ;
                            schema1:value "1,1,1" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "d-spacing" ;
                            schema1:propertyID xas:dspacing ;
                            schema1:unitText "Angstrom" ;
                            schema1:value "3.13550" ] ;
                    schema1:additionalType xas:xraymonochromator,
                        wd:Q3099911 ;
                    schema1:identifier "xas:Mono/Si 111" ;
                    schema1:name "Si 111" ] ],
        [ schema1:instrument [ a schema1:Product,
                        schema1:Thing,
                        prov:Entity ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "transmitted-flux detection method" ;
                            schema1:propertyID xas:detectorit ;
                            schema1:value "10cm  N2 (?)" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "incident-flux detection method" ;
                            schema1:propertyID xas:detectori0 ;
                            schema1:value "10cm  N2" ] ;
                    schema1:additionalType xas:xraymonitor,
                        wd:Q3099911 ;
                    schema1:identifier "xas:Detector" ;
                    schema1:name "x-ray intensity monitor" ] ],
        [ schema1:instrument [ a schema1:Product,
                        schema1:Thing,
                        prov:Entity ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "Probe" ;
                            schema1:propertyID xas:probe ;
                            schema1:value "x-ray" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "X-ray source" ;
                            schema1:propertyID xas:xraysourcetype ;
                            schema1:value "Synchrotron X-ray Source" ] ;
                    schema1:additionalType xas:source,
                        wd:Q3099911 ;
                    schema1:name "APS bending magnet source" ] ],
        [ schema1:instrument [ a schema1:Product,
                        schema1:Thing,
                        prov:Entity ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "collimation" ;
                            schema1:propertyID xas:collimation ;
                            schema1:value "none" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "focusing" ;
                            schema1:propertyID xas:focusing ;
                            schema1:value "no" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "harmonic rejection" ;
                            schema1:propertyID xas:harmonicrejection ;
                            schema1:value "Rh-coated mirror, detuned " ] ;
                    schema1:additionalType xas:beamline,
                        wd:Q3099911 ;
                    schema1:identifier "xas:Beamline/13-BM-D" ;
                    schema1:name "13-BM-D" ] ] .

<https://example.org/DV/BYSPHH/iv/Column_1> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:alternateName "mono energy" ;
    schema1:description "mono energy" ;
    schema1:name "energy" ;
    schema1:propertyID xas:monochromatorenergy ;
    schema1:unitText "eV" ;
    cdif:uses "https://example.org/struct/DV/BYSPHH/rv/Column_1" .

<https://example.org/DV/BYSPHH/iv/Column_2> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:alternateName "time" ;
    schema1:description "time" ;
    schema1:name "time" ;
    schema1:propertyID xas:time ;
    schema1:unitText "" ;
    cdif:uses "https://example.org/struct/DV/BYSPHH/rv/Column_2" .

<https://example.org/DV/BYSPHH/iv/Column_3> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:alternateName "monitor intensity" ;
    schema1:description "monitor intensity" ;
    schema1:name "i0" ;
    schema1:propertyID xas:incidentintensity ;
    schema1:unitText "" ;
    cdif:uses "https://example.org/struct/DV/BYSPHH/rv/Column_3" .

<https://example.org/DV/BYSPHH/iv/Column_4> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:alternateName "transmission intensity" ;
    schema1:description "transmission intensity" ;
    schema1:name "itrans" ;
    schema1:propertyID xas:transmittedintensity ;
    schema1:unitText "" ;
    cdif:uses "https://example.org/struct/DV/BYSPHH/rv/Column_4" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: CDIF XAS document profile
description: CDIF document-level profile for X-ray Absorption Spectroscopy datasets.
  Composes the four base CDIF 1.1 profiles (core, discovery, data description, data
  structure) with the two XAS extensions (xasCore mandatory, xasOptional recommended)
  so a conforming document is discoverable, describes its measured variables, describes
  its physical/tabular structure, and carries the XAS-specific metadata that lets
  a domain client interpret the spectrum.
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifCore/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDiscovery/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataDescription/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasCore/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasOptional/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  cdif: https://w3id.org/cdif/
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  geosparql: http://www.opengis.net/ont/geosparql#
  spdx: http://spdx.org/rdf/terms#
  csvw: http://www.w3.org/ns/csvw#
  time: http://www.w3.org/2006/time#
  skos: http://www.w3.org/2004/02/skos/core#
  prov: http://www.w3.org/ns/prov#
  xas: https://w3id.org/cdif/xas/
  nxs: https://manual.nexusformat.org/classes/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/xasDocument/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/xasDocument/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "csvw": "http://www.w3.org/ns/csvw#",
    "time": "http://www.w3.org/2006/time#",
    "xas": "cdif:xas/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "ada": "https://ada.astromat.org/metadata/",
    "wd": "https://www.wikidata.org/entity/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/xasDocument/context.jsonld)

## Sources

* [CDIF book](https://cross-domain-interoperability-framework.github.io/cdifbook/)
* [XAS SKOS glossary](https://w3id.org/cdif/xas/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifCompositeProfile/xasDocument`

