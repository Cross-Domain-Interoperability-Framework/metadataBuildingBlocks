
# X-ray absorbtion spectroscopy (Xas) CDIF profile (Schema)

`cdif.bbr.metadata.profiles.cdifProfiles.CDIFxas` *v0.1*

Gather building blocks to generate CDIF schema for XAS data 

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF XAS metadata

Profile assembling building blocks for using and Extended CDIF discovery schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) to document X-Ray absorbtion spectroscopy data.
## Examples

### Example CDIF XAS test record.
Example CDIF XAS metadata, not real values.
#### json
```json
{
  "@context": {
    "@vocab": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "time": "http://www.w3.org/2006/time#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
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
        "cdi:PhysicalDataset"
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
      "allowsDuplicates": false,
      "isStructuredBy": {
        "@type": [
          "WideDataStructure"
        ],
        "has_DataStructureComponent": [
          {
            "@type": [
              "IdentifierComponent"
            ],
            "isDefinedBy_InstanceVariable": {
              "@id": "xas:monochromatorEnergy"
            },
            "has": {
              "@type": [
                "ValueMapping"
              ],
              "hasIndex": 1,
              "length": 12
            }
          },
          {
            "@type": [
              "MeasureComponent"
            ],
            "isDefinedBy_InstanceVariable": {
              "@id": "xas:incidentIntensity"
            },
            "has": {
              "@type": [
                "ValueMapping"
              ],
              "hasIndex": 3,
              "length": 13
            }
          },
          {
            "@type": [
              "MeasureComponent"
            ],
            "isDefinedBy_InstanceVariable": {
              "@id": "xas:transmittedIntensity"
            },
            "has": {
              "@type": [
                "ValueMapping"
              ],
              "hasIndex": 2,
              "length": 12
            }
          }
        ],
        "allowsDuplicates": false,
        "arrayBase": 1,
        "commentPrefix": "#",
        "hasHeader": true,
        "headerRowCount": 27,
        "skipInitialSpace": true,
        "isDelimited": false,
        "isFixedWidth": true
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
      "schema:inDefinedTermSet": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Selenium",
      "schema:identifier": "http://sweetontology.net/matrElement/Selenium",
      "schema:termCode": "Se",
      "schema:inDefinedTermSet": "http://sweetontology.net/matrElement"
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "schema:Action",
        "xas:AnalysisEvent",
        "prov:Activity"
      ],
      "schema:identifier": "20241111_DSC_NU_OREX-803224-0_1",
      "schema:startDate": "2008-04-10T21:58:50",
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing",
              "schema:Product"
            ],
            "schema:name": "APS 13-BM-D XAS beamline instrument",
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
                "schema:name": "source, made up for this example",
                "schema:identifier": "should have a registry with URIs",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXsource/type"
                    ],
                    "schema:name": "x-ray source",
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
                "schema:additionalType": "xas:Beamline",
                "schema:name": "13-BM-D",
                "schema:identifier": "should have a registry with URIs",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "xas:collimation"
                    ],
                    "schema:name": "collimation technique",
                    "schema:value": "none"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "xas:focusing"
                    ],
                    "schema:name": "focusing",
                    "schema:value": "???"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "xas:harmonic_rejection"
                    ],
                    "schema:name": "harmonic_rejection",
                    "schema:value": "Rh-coated mirror, detuned"
                  }
                ]
              },
              {
                "@type": [
                  "schema:Thing",
                  "schema:Product"
                ],
                "schema:additionalType": "nxs:BaseClass/NXmonochromator",
                "schema:name": "Si 111",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/d_spacing"
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
                      "nxs:Field/NXcrystal/chemical_formula"
                    ],
                    "schema:name": "chemical formula",
                    "schema:value": "Si"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/type"
                    ],
                    "schema:name": "crystal type",
                    "schema:value": "missing"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/reflection"
                    ],
                    "schema:name": "reflection plane (hkl)",
                    "schema:value": "1,1,1"
                  }
                ]
              },
              {
                "@type": [
                  "schema:Thing",
                  "schema:Product"
                ],
                "schema:additionalType": "nxs:BaseClass/NXmonitor",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXmonitor/mode"
                    ],
                    "schema:name": "monitor mode",
                    "schema:value": "monitor"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXmonitor/preset"
                    ],
                    "schema:name": "monitor preset",
                    "schema:value": "N.A."
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "xas:detector.i0"
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
                      "xas:detector.it"
                    ],
                    "schema:name": "detector mode it",
                    "schema:alternateName": "transmitted flux measurement method",
                    "schema:value": "10cm  N2"
                  }
                ]
              }
            ]
          }
        }
      ],
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "xas:pressure"
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
            "xas:edge_energy"
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
            "nxs:Group/NXdetector/calibration_method"
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
            "nxs:Group/NXentry/experiment_documentation"
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
            "xas:installedOptions"
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
          "xas:Facility"
        ],
        "schema:identifier": "https://ror.org/aps",
        "schema:name": "APS",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "xas:energy"
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
              "xas:current"
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
              "xas:xray_source"
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
          "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
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
              "xas:porosity"
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
              "xas:stoichiometry"
            ],
            "schema:name": "Stoichiometry",
            "schema:value": "Na2SeO4"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "xas:samplePreparation"
            ],
            "schema:name": "samaple preparation method",
            "schema:value": "powder on tape, 6 layers"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "nxs:Field/NXsample/mass"
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
              "nxs:Field/NXsample/point_group"
            ],
            "schema:name": "crystallographic point group",
            "schema:value": "mm2"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "nxs:Field/NXsample/unit_cell"
            ],
            "schema:name": "Crystal unit cell dimensions",
            "schema:value": "cubic; Z = 4; a = 5.46; V = 162.77"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "xas:parentSample"
            ],
            "schema:name": "parent sample identifier",
            "schema:value": "igsn:10.3476/342573"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "xas:materialState"
            ],
            "schema:name": "material state",
            "schema:value": "solid metal foil"
          }
        ]
      }
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "xas:monochromatorEnergy",
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
        "xas:monochromatorEnergyConcept"
      ],
      "schema:unitText": "eV",
      "identifier": "should be URI from nexusFormat organization",
      "physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "simpleUnitOfMeasure": "eV",
      "uses": "xas:monochromatorEnergyConcept",
      "name": "energy",
      "displayLabel": "monochromator energy"
    },
    {
      "@id": "xas:incidentIntensity",
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
        "xas:incidentIntensityConcept"
      ],
      "schema:unitText": "counts",
      "identifier": "should be URI from nexusFormat organization",
      "physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "uses": "xas:incidentIntensityConcept",
      "name": "i0",
      "displayLabel": "monitor intensity"
    },
    {
      "@id": "xas:transmittedIntensity",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
      "schema:propertyID": [
        "xas:transmittedIntensityConcept"
      ],
      "schema:unitText": "counts",
      "schema:name": "itrans",
      "schema:alternateName": [
        "transmission intensity"
      ],
      "physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "identifier": "should be URI from nexusFormat organization",
      "uses": "xas:transmittedIntensityConcept",
      "name": "itrans",
      "displayLabel": "transmission intensity"
    }
  ],
  "relatedLink": [
    {
      "@type": [
        "LinkRole"
      ],
      "linkRelationship": "projectProposal",
      "target": {
        "@type": [
          "EntryPoint"
        ],
        "encodingType": "text/html",
        "name": "name of the proposal",
        "url": "https://example.org/locatorForProposalText",
        "identifier": "identifier for proposal, could used text or schema:PropertyValue pattern"
      }
    }
  ],
  "schema:subjectOf": {
    "@id": "xas:ja51-pz63",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
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
        "@id": "https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFxas"
      },
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
        "@id": "https://w3id.org/cdif/xasCore/1.0/"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFxas/context.jsonld",
    {
      "@vocab": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "spdx": "http://spdx.org/rdf/terms#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "time": "http://www.w3.org/2006/time#",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "xas": "https://xas.org/dictionary/",
      "nxs": "http://purl.org/nexusformat/definitions/",
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
        "cdi:PhysicalDataset"
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
      "allowsDuplicates": false,
      "isStructuredBy": {
        "@type": [
          "WideDataStructure"
        ],
        "has_DataStructureComponent": [
          {
            "@type": [
              "IdentifierComponent"
            ],
            "isDefinedBy_InstanceVariable": {
              "@id": "xas:monochromatorEnergy"
            },
            "has": {
              "@type": [
                "ValueMapping"
              ],
              "hasIndex": 1,
              "length": 12
            }
          },
          {
            "@type": [
              "MeasureComponent"
            ],
            "isDefinedBy_InstanceVariable": {
              "@id": "xas:incidentIntensity"
            },
            "has": {
              "@type": [
                "ValueMapping"
              ],
              "hasIndex": 3,
              "length": 13
            }
          },
          {
            "@type": [
              "MeasureComponent"
            ],
            "isDefinedBy_InstanceVariable": {
              "@id": "xas:transmittedIntensity"
            },
            "has": {
              "@type": [
                "ValueMapping"
              ],
              "hasIndex": 2,
              "length": 12
            }
          }
        ],
        "allowsDuplicates": false,
        "arrayBase": 1,
        "commentPrefix": "#",
        "hasHeader": true,
        "headerRowCount": 27,
        "skipInitialSpace": true,
        "isDelimited": false,
        "isFixedWidth": true
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
      "schema:inDefinedTermSet": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Selenium",
      "schema:identifier": "http://sweetontology.net/matrElement/Selenium",
      "schema:termCode": "Se",
      "schema:inDefinedTermSet": "http://sweetontology.net/matrElement"
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "schema:Action",
        "xas:AnalysisEvent",
        "prov:Activity"
      ],
      "schema:identifier": "20241111_DSC_NU_OREX-803224-0_1",
      "schema:startDate": "2008-04-10T21:58:50",
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing",
              "schema:Product"
            ],
            "schema:name": "APS 13-BM-D XAS beamline instrument",
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
                "schema:name": "source, made up for this example",
                "schema:identifier": "should have a registry with URIs",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXsource/type"
                    ],
                    "schema:name": "x-ray source",
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
                "schema:additionalType": "xas:Beamline",
                "schema:name": "13-BM-D",
                "schema:identifier": "should have a registry with URIs",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "xas:collimation"
                    ],
                    "schema:name": "collimation technique",
                    "schema:value": "none"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "xas:focusing"
                    ],
                    "schema:name": "focusing",
                    "schema:value": "???"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "xas:harmonic_rejection"
                    ],
                    "schema:name": "harmonic_rejection",
                    "schema:value": "Rh-coated mirror, detuned"
                  }
                ]
              },
              {
                "@type": [
                  "schema:Thing",
                  "schema:Product"
                ],
                "schema:additionalType": "nxs:BaseClass/NXmonochromator",
                "schema:name": "Si 111",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/d_spacing"
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
                      "nxs:Field/NXcrystal/chemical_formula"
                    ],
                    "schema:name": "chemical formula",
                    "schema:value": "Si"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/type"
                    ],
                    "schema:name": "crystal type",
                    "schema:value": "missing"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/reflection"
                    ],
                    "schema:name": "reflection plane (hkl)",
                    "schema:value": "1,1,1"
                  }
                ]
              },
              {
                "@type": [
                  "schema:Thing",
                  "schema:Product"
                ],
                "schema:additionalType": "nxs:BaseClass/NXmonitor",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXmonitor/mode"
                    ],
                    "schema:name": "monitor mode",
                    "schema:value": "monitor"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXmonitor/preset"
                    ],
                    "schema:name": "monitor preset",
                    "schema:value": "N.A."
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "xas:detector.i0"
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
                      "xas:detector.it"
                    ],
                    "schema:name": "detector mode it",
                    "schema:alternateName": "transmitted flux measurement method",
                    "schema:value": "10cm  N2"
                  }
                ]
              }
            ]
          }
        }
      ],
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "xas:pressure"
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
            "xas:edge_energy"
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
            "nxs:Group/NXdetector/calibration_method"
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
            "nxs:Group/NXentry/experiment_documentation"
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
            "xas:installedOptions"
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
          "xas:Facility"
        ],
        "schema:identifier": "https://ror.org/aps",
        "schema:name": "APS",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "xas:energy"
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
              "xas:current"
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
              "xas:xray_source"
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
          "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
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
              "xas:porosity"
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
              "xas:stoichiometry"
            ],
            "schema:name": "Stoichiometry",
            "schema:value": "Na2SeO4"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "xas:samplePreparation"
            ],
            "schema:name": "samaple preparation method",
            "schema:value": "powder on tape, 6 layers"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "nxs:Field/NXsample/mass"
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
              "nxs:Field/NXsample/point_group"
            ],
            "schema:name": "crystallographic point group",
            "schema:value": "mm2"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "nxs:Field/NXsample/unit_cell"
            ],
            "schema:name": "Crystal unit cell dimensions",
            "schema:value": "cubic; Z = 4; a = 5.46; V = 162.77"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "xas:parentSample"
            ],
            "schema:name": "parent sample identifier",
            "schema:value": "igsn:10.3476/342573"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "xas:materialState"
            ],
            "schema:name": "material state",
            "schema:value": "solid metal foil"
          }
        ]
      }
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "xas:monochromatorEnergy",
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
        "xas:monochromatorEnergyConcept"
      ],
      "schema:unitText": "eV",
      "identifier": "should be URI from nexusFormat organization",
      "physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "simpleUnitOfMeasure": "eV",
      "uses": "xas:monochromatorEnergyConcept",
      "name": "energy",
      "displayLabel": "monochromator energy"
    },
    {
      "@id": "xas:incidentIntensity",
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
        "xas:incidentIntensityConcept"
      ],
      "schema:unitText": "counts",
      "identifier": "should be URI from nexusFormat organization",
      "physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "uses": "xas:incidentIntensityConcept",
      "name": "i0",
      "displayLabel": "monitor intensity"
    },
    {
      "@id": "xas:transmittedIntensity",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
      "schema:propertyID": [
        "xas:transmittedIntensityConcept"
      ],
      "schema:unitText": "counts",
      "schema:name": "itrans",
      "schema:alternateName": [
        "transmission intensity"
      ],
      "physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "identifier": "should be URI from nexusFormat organization",
      "uses": "xas:transmittedIntensityConcept",
      "name": "itrans",
      "displayLabel": "transmission intensity"
    }
  ],
  "relatedLink": [
    {
      "@type": [
        "LinkRole"
      ],
      "linkRelationship": "projectProposal",
      "target": {
        "@type": [
          "EntryPoint"
        ],
        "encodingType": "text/html",
        "name": "name of the proposal",
        "url": "https://example.org/locatorForProposalText",
        "identifier": "identifier for proposal, could used text or schema:PropertyValue pattern"
      }
    }
  ],
  "schema:subjectOf": {
    "@id": "xas:ja51-pz63",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
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
        "@id": "https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFxas"
      },
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
        "@id": "https://w3id.org/cdif/xasCore/1.0/"
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
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix xas: <https://xas.org/dictionary/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

xas:487y54 a schema1:Dataset,
        schema1:Product ;
    cdi:relatedLink [ a cdi:LinkRole ;
            cdi:linkRelationship "projectProposal" ;
            cdi:target [ a cdi:EntryPoint ;
                    cdi:encodingType "text/html" ;
                    cdi:identifier "identifier for proposal, could used text or schema:PropertyValue pattern" ;
                    cdi:name "name of the proposal" ;
                    cdi:url "https://example.org/locatorForProposalText" ] ] ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor <https://orcid.org/35735ul> ;
            schema1:roleName "principleInvestigator" ],
        [ a schema1:Role ;
            schema1:contributor <https://ror.org/aps> ;
            schema1:roleName "Facility" ],
        [ a schema1:Role ;
            schema1:contributor <https://orcid.org/3547ulkj> ;
            schema1:roleName "dataCollector" ] ;
    schema1:creator ( <https://orcid.org/3547ulkj> ) ;
    schema1:dateModified "2025-06-22" ;
    schema1:description "Example metadata including all properties in the CDIF XAS profile" ;
    schema1:distribution [ a cdi:PhysicalDataset,
                schema1:DataDownload ;
            cdi:allowsDuplicates false ;
            cdi:isStructuredBy [ a cdi:WideDataStructure ;
                    cdi:allowsDuplicates false ;
                    cdi:arrayBase 1 ;
                    cdi:commentPrefix "#" ;
                    cdi:hasHeader true ;
                    cdi:has_DataStructureComponent [ a cdi:MeasureComponent ;
                            cdi:has [ a cdi:ValueMapping ;
                                    cdi:hasIndex 3 ;
                                    cdi:length 13 ] ;
                            cdi:isDefinedBy_InstanceVariable xas:incidentIntensity ],
                        [ a cdi:IdentifierComponent ;
                            cdi:has [ a cdi:ValueMapping ;
                                    cdi:hasIndex 1 ;
                                    cdi:length 12 ] ;
                            cdi:isDefinedBy_InstanceVariable xas:monochromatorEnergy ],
                        [ a cdi:MeasureComponent ;
                            cdi:has [ a cdi:ValueMapping ;
                                    cdi:hasIndex 2 ;
                                    cdi:length 12 ] ;
                            cdi:isDefinedBy_InstanceVariable xas:transmittedIntensity ] ;
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
            schema1:identifier "missing" ;
            schema1:inDefinedTermSet "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md" ;
            schema1:name "K-edge" ;
            schema1:termCode "K" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "http://sweetontology.net/matrElement/Selenium" ;
            schema1:inDefinedTermSet "http://sweetontology.net/matrElement" ;
            schema1:name "Selenium" ;
            schema1:termCode "Se" ] ;
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
    schema1:variableMeasured xas:incidentIntensity,
        xas:monochromatorEnergy,
        xas:transmittedIntensity ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity,
                xas:AnalysisEvent ;
            schema1:additionalProperty [ a schema1:PropertyValue ;
                    schema1:name "Absorption edge" ;
                    schema1:propertyID "xas:edge_energy" ;
                    schema1:unitText "eV" ;
                    schema1:value "12658.0" ],
                [ a schema1:PropertyValue ;
                    schema1:name "calibration method" ;
                    schema1:propertyID "nxs:Group/NXdetector/calibration_method" ;
                    schema1:url "http://protocols.io/link/to/calibrationMethod" ;
                    schema1:value "description of calibration procedure" ],
                [ a schema1:PropertyValue ;
                    schema1:description "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential" ;
                    schema1:name "experiment environment-pressure" ;
                    schema1:propertyID "xas:pressure" ;
                    schema1:unitText "KPa" ;
                    schema1:value "3567" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Installed Options" ;
                    schema1:propertyID "xas:installedOptions" ;
                    schema1:value "Description of extra equipment installed on the base instrument(?)" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Instrument configuration" ;
                    schema1:propertyID "nxs:Group/NXentry/experiment_documentation" ;
                    schema1:url "http://protocols.io/link/to/calibrationMethod" ;
                    schema1:value "description of instrument configuration" ] ;
            schema1:identifier "20241111_DSC_NU_OREX-803224-0_1" ;
            schema1:location ex:xasfacility_37yht ;
            schema1:object [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "material state" ;
                            schema1:propertyID "xas:materialState" ;
                            schema1:value "solid metal foil" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Porosity" ;
                            schema1:propertyID "xas:porosity" ;
                            schema1:unitText "percent" ;
                            schema1:value "27" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "parent sample identifier" ;
                            schema1:propertyID "xas:parentSample" ;
                            schema1:value "igsn:10.3476/342573" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "samaple preparation method" ;
                            schema1:propertyID "xas:samplePreparation" ;
                            schema1:value "powder on tape, 6 layers" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Stoichiometry" ;
                            schema1:propertyID "xas:stoichiometry" ;
                            schema1:value "Na2SeO4" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "sample mass" ;
                            schema1:propertyID "nxs:Field/NXsample/mass" ;
                            schema1:unitText "mg" ;
                            schema1:value "10" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "crystallographic point group" ;
                            schema1:propertyID "nxs:Field/NXsample/point_group" ;
                            schema1:value "mm2" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Crystal unit cell dimensions" ;
                            schema1:propertyID "nxs:Field/NXsample/unit_cell" ;
                            schema1:value "cubic; Z = 4; a = 5.46; V = 162.77" ] ;
                    schema1:additionalType "MaterialSample",
                        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample" ;
                    schema1:description "physical properties of sample: ph, eh, volume, porosity, density, concentration, resistivity, viscosity, crystal structure, opacity from xdi list..." ;
                    schema1:identifier "igsn:10.6620/357lkj" ;
                    schema1:name "Na2SeO4" ] ;
            schema1:startDate "2008-04-10T21:58:50" ;
            prov:used [ schema1:instrument [ a schema1:Product,
                                schema1:Thing ;
                            schema1:category [ a schema1:DefinedTerm ;
                                    schema1:name "X-ray absorption spectroscopy beamline" ;
                                    schema1:termCode "XAS-beamline" ] ;
                            schema1:hasPart [ a schema1:Product,
                                        schema1:Thing ;
                                    schema1:additionalProperty [ a schema1:PropertyValue ;
                                            schema1:name "Probe" ;
                                            schema1:propertyID "nxs:Field/NXsource/probe" ;
                                            schema1:value "x-ray" ],
                                        [ a schema1:PropertyValue ;
                                            schema1:name "x-ray source" ;
                                            schema1:propertyID "nxs:Field/NXsource/type" ;
                                            schema1:value "Synchrotron X-ray Source" ] ;
                                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                                    schema1:identifier "should have a registry with URIs" ;
                                    schema1:name "source, made up for this example" ],
                                [ a schema1:Product,
                                        schema1:Thing ;
                                    schema1:additionalProperty [ a schema1:PropertyValue ;
                                            schema1:name "monitor preset" ;
                                            schema1:propertyID "nxs:Field/NXmonitor/preset" ;
                                            schema1:value "N.A." ],
                                        [ a schema1:PropertyValue ;
                                            schema1:name "monitor mode" ;
                                            schema1:propertyID "nxs:Field/NXmonitor/mode" ;
                                            schema1:value "monitor" ],
                                        [ a schema1:PropertyValue ;
                                            schema1:alternateName "transmitted flux measurement method" ;
                                            schema1:name "detector mode it" ;
                                            schema1:propertyID "xas:detector.it" ;
                                            schema1:value "10cm  N2" ],
                                        [ a schema1:PropertyValue ;
                                            schema1:alternateName "incident flux measurement method" ;
                                            schema1:name "detector mode i0" ;
                                            schema1:propertyID "xas:detector.i0" ;
                                            schema1:value "10cm  N2" ] ;
                                    schema1:additionalType "nxs:BaseClass/NXmonitor" ],
                                [ a schema1:Product,
                                        schema1:Thing ;
                                    schema1:additionalProperty [ a schema1:PropertyValue ;
                                            schema1:name "focusing" ;
                                            schema1:propertyID "xas:focusing" ;
                                            schema1:value "???" ],
                                        [ a schema1:PropertyValue ;
                                            schema1:name "collimation technique" ;
                                            schema1:propertyID "xas:collimation" ;
                                            schema1:value "none" ],
                                        [ a schema1:PropertyValue ;
                                            schema1:name "harmonic_rejection" ;
                                            schema1:propertyID "xas:harmonic_rejection" ;
                                            schema1:value "Rh-coated mirror, detuned" ] ;
                                    schema1:additionalType "xas:Beamline" ;
                                    schema1:identifier "should have a registry with URIs" ;
                                    schema1:name "13-BM-D" ],
                                [ a schema1:Product,
                                        schema1:Thing ;
                                    schema1:additionalProperty [ a schema1:PropertyValue ;
                                            schema1:name "crystal type" ;
                                            schema1:propertyID "nxs:Field/NXcrystal/type" ;
                                            schema1:value "missing" ],
                                        [ a schema1:PropertyValue ;
                                            schema1:name "reflection plane (hkl)" ;
                                            schema1:propertyID "nxs:Field/NXcrystal/reflection" ;
                                            schema1:value "1,1,1" ],
                                        [ a schema1:PropertyValue ;
                                            schema1:name "chemical formula" ;
                                            schema1:propertyID "nxs:Field/NXcrystal/chemical_formula" ;
                                            schema1:value "Si" ],
                                        [ a schema1:PropertyValue ;
                                            schema1:name "d-spacing" ;
                                            schema1:propertyID "nxs:Field/NXcrystal/d_spacing" ;
                                            schema1:unitText "Angstrom" ;
                                            schema1:value "3.13550" ] ;
                                    schema1:additionalType "nxs:BaseClass/NXmonochromator" ;
                                    schema1:name "Si 111" ] ;
                            schema1:name "APS 13-BM-D XAS beamline instrument" ] ] ] .

ex:xasfacility_37yht a schema1:Place ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Facility current" ;
            schema1:propertyID "xas:current" ;
            schema1:unitText "Amps" ;
            schema1:value "120" ],
        [ a schema1:PropertyValue ;
            schema1:name "X-ray Source" ;
            schema1:propertyID "xas:xray_source" ;
            schema1:value "APS bending magnet" ],
        [ a schema1:PropertyValue ;
            schema1:name "Facility energy" ;
            schema1:propertyID "xas:energy" ;
            schema1:unitText "GeV" ;
            schema1:value "7.00" ] ;
    schema1:additionalType "xas:Facility" ;
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
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore>,
        <https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFxas>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/>,
        <https://w3id.org/cdif/xasCore/1.0/>,
        <https://w3id.org/cdif/xasDiscovery/1.0/> ;
    schema1:about xas:485749 ;
    schema1:additionalType "dcat:CatalogRecord" ;
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

xas:incidentIntensity a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "monitor intensity" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "i0" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:uses "xas:incidentIntensityConcept" ;
    schema1:alternateName "Monitor intensity" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description)" ;
    schema1:name "i0 monitory intensity" ;
    schema1:propertyID "xas:incidentIntensityConcept" ;
    schema1:unitText "counts" .

xas:monochromatorEnergy a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "monochromator energy" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "energy" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:simpleUnitOfMeasure "eV" ;
    cdi:uses "xas:monochromatorEnergyConcept" ;
    schema1:alternateName "Monochromator energy" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description" ;
    schema1:name "energy" ;
    schema1:propertyID "xas:monochromatorEnergyConcept" ;
    schema1:unitText "eV" .

xas:transmittedIntensity a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "transmission intensity" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "itrans" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:uses "xas:transmittedIntensityConcept" ;
    schema1:alternateName "transmission intensity" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description" ;
    schema1:name "itrans" ;
    schema1:propertyID "xas:transmittedIntensityConcept" ;
    schema1:unitText "counts" .


```


### Actual data CDIF XAS record.
Metadata for an example XAS dataset.
#### json
```json
{
    "@context": {
        "@vocab": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "schema": "http://schema.org/",
        "dcterms": "http://purl.org/dc/terms/",
        "geosparql": "http://www.opengis.net/ont/geosparql#",
        "spdx": "http://spdx.org/rdf/terms#",
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "time": "http://www.w3.org/2006/time#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "csvw": "http://www.w3.org/ns/csvw#",
        "xas": "https://xas.org/dictionary/",
        "nxs": "http://purl.org/nexusformat/definitions/",
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
                "@type": "schema:Person",
                "schema:name": "Collectus, Poindexter",
                "schema:contactPoint": {
                    "@type": "schema:ContactPoint",
                    "schema:email": "missing@email.org"
                }
            }
        ]
    },
    "schema:contributor": [
        {
            "@type": "schema:Role",
            "schema:roleName": "Facility",
            "schema:contributor": {
                "@type": "schema:Organization",
                "@id": "https://ror.org/aps",
                "schema:name": "Argonne Synchotron"
            }
        },
        {
            "@type": "schema:Role",
            "schema:roleName": "dataCollector",
            "schema:contributor": {
                "@id": "https://orcid.org/3547ulkj"
            }
        },
        {
            "@type": "schema:Role",
            "schema:roleName": "principleInvestigator",
            "schema:contributor": {
                "@type": "schema:Person",
                "@id": "https://orcid.org/35735ul",
                "schema:name": "Scienceguy, Biggus",
                "schema:contactPoint": {
                    "@type": "schema:ContactPoint",
                    "schema:email": "missing@email.org"
                },
                "schema:affiliation": {
                    "@type": "schema:Organization",
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
            "cdi:hasPhysicalMapping": [
                {
                    "cdi:index": 0,
                    "cdi:format": "decimal",
                    "cdi:physicalDataType": "float64",
                    "cdi:isRequired": true,
                    "cdi:formats_InstanceVariable": {
                        "@id": "xas:monochromatorEnergy"
                    }
                },
                {
                    "cdi:index": 1,
                    "cdi:format": "decimal",
                    "cdi:physicalDataType": "float64",
                    "cdi:isRequired": true,
                    "cdi:formats_InstanceVariable": {
                        "@id": "xas:transmittedIntensity"
                    }
                },
                {
                    "cdi:index": 2,
                    "cdi:format": "decimal",
                    "cdi:physicalDataType": "float64",
                    "cdi:isRequired": true,
                    "cdi:formats_InstanceVariable": {
                        "@id": "xas:incidentIntensity"
                    }
                }
            ]
        }
    ],
    "schema:measurementTechnique": [
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "X-Ray Absorption Spectroscopy",
            "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01196",
            "schema:termCode": "XAS",
            "schema:inDefinedTermSet": "http://purl.org/pan-science/PaNET/PaNET.owl"
        },
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Transmission",
            "schema:identifier": "xas:transmissionMode",
            "schema:inDefinedTermSet": "nxs:Field/NXxas/ENTRY/DATA/mode"
        }
    ],
    "schema:keywords": [
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "K-edge",
            "schema:identifier": "missing",
            "schema:termCode": "K",
            "schema:inDefinedTermSet": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md"
        },
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Selenium",
            "schema:identifier": "http://sweetontology.net/matrElement/Selenium",
            "schema:termCode": "Se",
            "schema:inDefinedTermSet": "http://sweetontology.net/matrElement"
        }
    ],
    "prov:wasGeneratedBy": [
        {
            "@type": [
                "schema:Action",
                "xas:AnalysisEvent",
                "prov:Activity"
            ],
            "schema:identifier": "20241111_DSC_NU_OREX-803224-0_1",
            "schema:startDate": "2008-04-10T21:58:50",
            "prov:used": [
                {
                    "@type": [
                        "schema:Thing",
                        "schema:Product"
                    ],
                    "schema:additionalType": "nxs:BaseClass/NXsource",
                    "schema:name": "source, made up for this example",
                    "schema:identifier": "should have a registry with URIs",
                    "schema:additionalProperty": [
                        {
                            "@type": "schema:PropertyValue",
                            "schema:propertyID": [
                                "nxs:Field/NXsource/type"
                            ],
                            "schema:name": "x-ray source",
                            "schema:value": "Synchrotron X-ray Source"
                        },
                        {
                            "@type": "schema:PropertyValue",
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
                    "schema:additionalType": "xas:Beamline",
                    "schema:name": "13-BM-D",
                    "schema:identifier": "should have a registry with URIs",
                    "schema:additionalProperty": [
                        {
                            "@type": "schema:PropertyValue",
                            "schema:propertyID": [
                                "xas:collimation"
                            ],
                            "schema:name": "collimation technique",
                            "schema:value": "none"
                        },
                        {
                            "@type": "schema:PropertyValue",
                            "schema:propertyID": [
                                "xas:focusing"
                            ],
                            "schema:name": "focusing",
                            "schema:value": "???"
                        },
                        {
                            "@type": "schema:PropertyValue",
                            "schema:propertyID": [
                                "xas:harmonic_rejection"
                            ],
                            "schema:name": "harmonic_rejection",
                            "schema:value": "Rh-coated mirror, detuned"
                        }
                    ]
                },
                {
                    "@type": [
                        "schema:Thing",
                        "schema:Product"
                    ],
                    "schema:additionalType": "nxs:BaseClass/NXmonochromator",
                    "schema:name": "Si 111",
                    "schema:additionalProperty": [
                        {
                            "@type": "schema:PropertyValue",
                            "schema:propertyID": [
                                "nxs:Field/NXcrystal/d_spacing"
                            ],
                            "schema:name": "d-spacing",
                            "schema:value": "3.13550",
                            "schema:unitText": "Angstrom"
                        },
                        {
                            "@type": "schema:PropertyValue",
                            "schema:propertyID": [
                                "nxs:Field/NXcrystal/chemical_formula"
                            ],
                            "schema:name": "chemical formula",
                            "schema:value": "Si"
                        },
                        {
                            "@type": "schema:PropertyValue",
                            "schema:propertyID": [
                                "nxs:Field/NXcrystal/type"
                            ],
                            "schema:name": "crystal type",
                            "schema:value": "missing"
                        },
                        {
                            "@type": "schema:PropertyValue",
                            "schema:propertyID": [
                                "nxs:Field/NXcrystal/reflection"
                            ],
                            "schema:name": "reflection plane (hkl)",
                            "schema:value": "1,1,1"
                        }
                    ]
                },
                {
                    "@type": [
                        "schema:Thing",
                        "schema:Product"
                    ],
                    "schema:additionalType": "nxs:BaseClass/NXmonitor",
                    "schema:additionalProperty": [
                        {
                            "@type": "schema:PropertyValue",
                            "schema:propertyID": [
                                "nxs:Field/NXmonitor/mode"
                            ],
                            "schema:name": "monitor mode",
                            "schema:value": "monitor"
                        },
                        {
                            "@type": "schema:PropertyValue",
                            "schema:propertyID": [
                                "nxs:Field/NXmonitor/preset"
                            ],
                            "schema:name": "monitor preset",
                            "schema:value": "N.A."
                        },
                        {
                            "@type": "schema:PropertyValue",
                            "schema:propertyID": [
                                "xas:detector.i0"
                            ],
                            "schema:name": "detector mode i0",
                            "schema:alternateName": [
                                "incident flux measurement method"
                            ],
                            "schema:value": "10cm  N2"
                        },
                        {
                            "@type": "schema:PropertyValue",
                            "schema:propertyID": [
                                "xas:detector.it"
                            ],
                            "schema:name": "detector mode it",
                            "schema:alternateName": [
                                "transmitted flux measurement method"
                            ],
                            "schema:value": "10cm  N2"
                        }
                    ]
                }
            ],
            "schema:additionalProperty": [
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": [
                        "xas:pressure"
                    ],
                    "schema:name": "experiment environment-pressure",
                    "schema:description": "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential",
                    "schema:value": 3567,
                    "schema:unitText": "KPa"
                },
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": [
                        "xas:edge_energy"
                    ],
                    "schema:name": "Absorption edge",
                    "schema:value": "12658.0",
                    "schema:unitText": "eV"
                },
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": [
                        "nxs:Group/NXdetector/calibration_method"
                    ],
                    "schema:name": "calibration method",
                    "schema:value": "description of calibration procedure",
                    "schema:url": "http://protocols.io/link/to/calibrationMethod"
                },
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": [
                        "nxs:Group/NXentry/experiment_documentation"
                    ],
                    "schema:name": "Instrument configuration",
                    "schema:value": "description of instrument configuration",
                    "schema:url": "http://protocols.io/link/to/calibrationMethod"
                },
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": [
                        "xas:installedOptions"
                    ],
                    "schema:name": "Installed Options",
                    "schema:value": "Description of extra equipment installed on the base instrument(?)"
                }
            ],
            "schema:location": {
                "@id": "ex:xasfacility_37yht",
                "@type": "schema:Place",
                "schema:additionalType": [
                    "xas:Facility"
                ],
                "schema:identifier": "https://ror.org/aps",
                "schema:name": "APS",
                "schema:additionalProperty": [
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": [
                            "xas:energy"
                        ],
                        "schema:name": "Facility energy",
                        "schema:value": "7.00",
                        "schema:unitText": "GeV"
                    },
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": [
                            "xas:current"
                        ],
                        "schema:name": "Facility current",
                        "schema:value": "120",
                        "schema:unitText": "Amps"
                    },
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": [
                            "xas:xray_source"
                        ],
                        "schema:name": "X-ray Source",
                        "schema:value": "APS bending magnet"
                    }
                ]
            },
            "schema:mainEntity": {
                "@type": [
                    "schema:Thing",
                    "schema:Product"
                ],
                "schema:additionalType": [
                    "MaterialSample",
                    "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
                ],
                "schema:name": "Na2SeO4",
                "schema:identifier": "igsn:10.6620/357lkj",
                "schema:description": "physical properties of sample: ph, eh, volume, porosity, density, concentration, resistivity, viscosity, crystal structure, opacity from xdi list...",
                "schema:additionalProperty": [
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": [
                            "xas:porosity"
                        ],
                        "schema:name": "Porosity",
                        "schema:value": 27,
                        "schema:unitText": "percent"
                    },
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": [
                            "xas:stoichiometry"
                        ],
                        "schema:name": "Stoichiometry",
                        "schema:value": "Na2SeO4"
                    },
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": [
                            "xas:samplePreparation"
                        ],
                        "schema:name": "samaple preparation method",
                        "schema:value": "powder on tape, 6 layers"
                    },
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": [
                            "nxs:Field/NXsample/mass"
                        ],
                        "schema:name": "sample mass",
                        "schema:value": "10",
                        "schema:unitText": "mg"
                    },
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": [
                            "nxs:Field/NXsample/point_group"
                        ],
                        "schema:name": "crystallographic point group",
                        "schema:value": "mm2"
                    },
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": [
                            "nxs:Field/NXsample/unit_cell"
                        ],
                        "schema:name": "Crystal unit cell dimensions",
                        "schema:value": "cubic; Z = 4; a = 5.46; V = 162.77"
                    },
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": [
                            "xas:parentSample"
                        ],
                        "schema:name": "parent sample identifier",
                        "schema:value": "igsn:10.3476/342573"
                    },
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": [
                            "xas:materialState"
                        ],
                        "schema:name": "material state",
                        "schema:value": "solid metal foil"
                    }
                ]
            }
        }
    ],
    "schema:variableMeasured": [
        {
            "@id": "xas:monochromatorEnergy",
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
                "xas:monochromatorEnergyConcept"
            ],
            "schema:unitText": "eV",
            "identifier": "should be URI from nexusFormat organization",
            "physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
            "simpleUnitOfMeasure": "eV",
            "uses": "xas:monochromatorEnergyConcept",
            "name": "energy",
            "displayLabel": "monochromator energy"
        },
        {
            "@id": "xas:incidentIntensity",
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
                "xas:incidentIntensityConcept"
            ],
            "schema:unitText": "counts",
            "identifier": "should be URI from nexusFormat organization",
            "physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
            "uses": "xas:incidentIntensityConcept",
            "name": "i0",
            "displayLabel": "monitor intensity"
        },
        {
            "@id": "xas:transmittedIntensity",
            "@type": [
                "cdi:InstanceVariable",
                "schema:PropertyValue"
            ],
            "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
            "schema:propertyID": [
                "xas:transmittedIntensityConcept"
            ],
            "schema:unitText": "counts",
            "schema:name": "itrans",
            "schema:alternateName": [
                "transmission intensity"
            ],
            "physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
            "identifier": "should be URI from nexusFormat organization",
            "uses": "xas:transmittedIntensityConcept",
            "name": "itrans",
            "displayLabel": "transmission intensity"
        }
    ],
    "relatedLink": [
        {
            "@type": "LinkRole",
            "linkRelationship": "projectProposal",
            "target": {
                "@type": "EntryPoint",
                "encodingType": "text/html",
                "name": "name of the proposal",
                "url": "https://example.org/locatorForProposalText",
                "identifier": "identifier for proposal, could used text or schema:PropertyValue pattern"
            }
        }
    ],
    "schema:subjectOf": {
        "@id": "xas:ja51-pz63",
        "@type": [
            "schema:Dataset"
        ],
        "schema:additionalType": [
            "dcat:CatalogRecord"
        ],
        "schema:dateModified": "2025-08-26",
        "schema:creator": [
            {
                "@id": "https://ada.org/person/3479",
                "@type": "schema:Person",
                "schema:name": "Richard, Stephen M.",
                "schema:identifier": "https://orcid.org/0000-0002-7933-2154",
                "schema:contactPoint": {
                    "@type": "schema:ContactPoint",
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
                "@id": "https://w3id.org/cdif/core/1.0/"
            },
            {
                "@id": "https://w3id.org/cdif/discovery/1.0/"
            },
            {
                "@id": "https://w3id.org/cdif/xasDiscovery/1.0/"
            },
            {
                "@id": "https://w3id.org/cdif/xasCore/1.0/"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFxas/context.jsonld",
    {
      "@vocab": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "spdx": "http://spdx.org/rdf/terms#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "time": "http://www.w3.org/2006/time#",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "csvw": "http://www.w3.org/ns/csvw#",
      "xas": "https://xas.org/dictionary/",
      "nxs": "http://purl.org/nexusformat/definitions/",
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
        "@type": "schema:Person",
        "schema:name": "Collectus, Poindexter",
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "missing@email.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": "schema:Role",
      "schema:roleName": "Facility",
      "schema:contributor": {
        "@type": "schema:Organization",
        "@id": "https://ror.org/aps",
        "schema:name": "Argonne Synchotron"
      }
    },
    {
      "@type": "schema:Role",
      "schema:roleName": "dataCollector",
      "schema:contributor": {
        "@id": "https://orcid.org/3547ulkj"
      }
    },
    {
      "@type": "schema:Role",
      "schema:roleName": "principleInvestigator",
      "schema:contributor": {
        "@type": "schema:Person",
        "@id": "https://orcid.org/35735ul",
        "schema:name": "Scienceguy, Biggus",
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "missing@email.org"
        },
        "schema:affiliation": {
          "@type": "schema:Organization",
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
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "xas:monochromatorEnergy"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "xas:transmittedIntensity"
          }
        },
        {
          "cdi:index": 2,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "xas:incidentIntensity"
          }
        }
      ]
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "X-Ray Absorption Spectroscopy",
      "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01196",
      "schema:termCode": "XAS",
      "schema:inDefinedTermSet": "http://purl.org/pan-science/PaNET/PaNET.owl"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Transmission",
      "schema:identifier": "xas:transmissionMode",
      "schema:inDefinedTermSet": "nxs:Field/NXxas/ENTRY/DATA/mode"
    }
  ],
  "schema:keywords": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "K-edge",
      "schema:identifier": "missing",
      "schema:termCode": "K",
      "schema:inDefinedTermSet": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Selenium",
      "schema:identifier": "http://sweetontology.net/matrElement/Selenium",
      "schema:termCode": "Se",
      "schema:inDefinedTermSet": "http://sweetontology.net/matrElement"
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "schema:Action",
        "xas:AnalysisEvent",
        "prov:Activity"
      ],
      "schema:identifier": "20241111_DSC_NU_OREX-803224-0_1",
      "schema:startDate": "2008-04-10T21:58:50",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": "nxs:BaseClass/NXsource",
          "schema:name": "source, made up for this example",
          "schema:identifier": "should have a registry with URIs",
          "schema:additionalProperty": [
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "nxs:Field/NXsource/type"
              ],
              "schema:name": "x-ray source",
              "schema:value": "Synchrotron X-ray Source"
            },
            {
              "@type": "schema:PropertyValue",
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
          "schema:additionalType": "xas:Beamline",
          "schema:name": "13-BM-D",
          "schema:identifier": "should have a registry with URIs",
          "schema:additionalProperty": [
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "xas:collimation"
              ],
              "schema:name": "collimation technique",
              "schema:value": "none"
            },
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "xas:focusing"
              ],
              "schema:name": "focusing",
              "schema:value": "???"
            },
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "xas:harmonic_rejection"
              ],
              "schema:name": "harmonic_rejection",
              "schema:value": "Rh-coated mirror, detuned"
            }
          ]
        },
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": "nxs:BaseClass/NXmonochromator",
          "schema:name": "Si 111",
          "schema:additionalProperty": [
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "nxs:Field/NXcrystal/d_spacing"
              ],
              "schema:name": "d-spacing",
              "schema:value": "3.13550",
              "schema:unitText": "Angstrom"
            },
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "nxs:Field/NXcrystal/chemical_formula"
              ],
              "schema:name": "chemical formula",
              "schema:value": "Si"
            },
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "nxs:Field/NXcrystal/type"
              ],
              "schema:name": "crystal type",
              "schema:value": "missing"
            },
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "nxs:Field/NXcrystal/reflection"
              ],
              "schema:name": "reflection plane (hkl)",
              "schema:value": "1,1,1"
            }
          ]
        },
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": "nxs:BaseClass/NXmonitor",
          "schema:additionalProperty": [
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "nxs:Field/NXmonitor/mode"
              ],
              "schema:name": "monitor mode",
              "schema:value": "monitor"
            },
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "nxs:Field/NXmonitor/preset"
              ],
              "schema:name": "monitor preset",
              "schema:value": "N.A."
            },
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "xas:detector.i0"
              ],
              "schema:name": "detector mode i0",
              "schema:alternateName": [
                "incident flux measurement method"
              ],
              "schema:value": "10cm  N2"
            },
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "xas:detector.it"
              ],
              "schema:name": "detector mode it",
              "schema:alternateName": [
                "transmitted flux measurement method"
              ],
              "schema:value": "10cm  N2"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "xas:pressure"
          ],
          "schema:name": "experiment environment-pressure",
          "schema:description": "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential",
          "schema:value": 3567,
          "schema:unitText": "KPa"
        },
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "xas:edge_energy"
          ],
          "schema:name": "Absorption edge",
          "schema:value": "12658.0",
          "schema:unitText": "eV"
        },
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "nxs:Group/NXdetector/calibration_method"
          ],
          "schema:name": "calibration method",
          "schema:value": "description of calibration procedure",
          "schema:url": "http://protocols.io/link/to/calibrationMethod"
        },
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "nxs:Group/NXentry/experiment_documentation"
          ],
          "schema:name": "Instrument configuration",
          "schema:value": "description of instrument configuration",
          "schema:url": "http://protocols.io/link/to/calibrationMethod"
        },
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "xas:installedOptions"
          ],
          "schema:name": "Installed Options",
          "schema:value": "Description of extra equipment installed on the base instrument(?)"
        }
      ],
      "schema:location": {
        "@id": "ex:xasfacility_37yht",
        "@type": "schema:Place",
        "schema:additionalType": [
          "xas:Facility"
        ],
        "schema:identifier": "https://ror.org/aps",
        "schema:name": "APS",
        "schema:additionalProperty": [
          {
            "@type": "schema:PropertyValue",
            "schema:propertyID": [
              "xas:energy"
            ],
            "schema:name": "Facility energy",
            "schema:value": "7.00",
            "schema:unitText": "GeV"
          },
          {
            "@type": "schema:PropertyValue",
            "schema:propertyID": [
              "xas:current"
            ],
            "schema:name": "Facility current",
            "schema:value": "120",
            "schema:unitText": "Amps"
          },
          {
            "@type": "schema:PropertyValue",
            "schema:propertyID": [
              "xas:xray_source"
            ],
            "schema:name": "X-ray Source",
            "schema:value": "APS bending magnet"
          }
        ]
      },
      "schema:mainEntity": {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "MaterialSample",
          "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
        ],
        "schema:name": "Na2SeO4",
        "schema:identifier": "igsn:10.6620/357lkj",
        "schema:description": "physical properties of sample: ph, eh, volume, porosity, density, concentration, resistivity, viscosity, crystal structure, opacity from xdi list...",
        "schema:additionalProperty": [
          {
            "@type": "schema:PropertyValue",
            "schema:propertyID": [
              "xas:porosity"
            ],
            "schema:name": "Porosity",
            "schema:value": 27,
            "schema:unitText": "percent"
          },
          {
            "@type": "schema:PropertyValue",
            "schema:propertyID": [
              "xas:stoichiometry"
            ],
            "schema:name": "Stoichiometry",
            "schema:value": "Na2SeO4"
          },
          {
            "@type": "schema:PropertyValue",
            "schema:propertyID": [
              "xas:samplePreparation"
            ],
            "schema:name": "samaple preparation method",
            "schema:value": "powder on tape, 6 layers"
          },
          {
            "@type": "schema:PropertyValue",
            "schema:propertyID": [
              "nxs:Field/NXsample/mass"
            ],
            "schema:name": "sample mass",
            "schema:value": "10",
            "schema:unitText": "mg"
          },
          {
            "@type": "schema:PropertyValue",
            "schema:propertyID": [
              "nxs:Field/NXsample/point_group"
            ],
            "schema:name": "crystallographic point group",
            "schema:value": "mm2"
          },
          {
            "@type": "schema:PropertyValue",
            "schema:propertyID": [
              "nxs:Field/NXsample/unit_cell"
            ],
            "schema:name": "Crystal unit cell dimensions",
            "schema:value": "cubic; Z = 4; a = 5.46; V = 162.77"
          },
          {
            "@type": "schema:PropertyValue",
            "schema:propertyID": [
              "xas:parentSample"
            ],
            "schema:name": "parent sample identifier",
            "schema:value": "igsn:10.3476/342573"
          },
          {
            "@type": "schema:PropertyValue",
            "schema:propertyID": [
              "xas:materialState"
            ],
            "schema:name": "material state",
            "schema:value": "solid metal foil"
          }
        ]
      }
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "xas:monochromatorEnergy",
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
        "xas:monochromatorEnergyConcept"
      ],
      "schema:unitText": "eV",
      "identifier": "should be URI from nexusFormat organization",
      "physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "simpleUnitOfMeasure": "eV",
      "uses": "xas:monochromatorEnergyConcept",
      "name": "energy",
      "displayLabel": "monochromator energy"
    },
    {
      "@id": "xas:incidentIntensity",
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
        "xas:incidentIntensityConcept"
      ],
      "schema:unitText": "counts",
      "identifier": "should be URI from nexusFormat organization",
      "physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "uses": "xas:incidentIntensityConcept",
      "name": "i0",
      "displayLabel": "monitor intensity"
    },
    {
      "@id": "xas:transmittedIntensity",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
      "schema:propertyID": [
        "xas:transmittedIntensityConcept"
      ],
      "schema:unitText": "counts",
      "schema:name": "itrans",
      "schema:alternateName": [
        "transmission intensity"
      ],
      "physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "identifier": "should be URI from nexusFormat organization",
      "uses": "xas:transmittedIntensityConcept",
      "name": "itrans",
      "displayLabel": "transmission intensity"
    }
  ],
  "relatedLink": [
    {
      "@type": "LinkRole",
      "linkRelationship": "projectProposal",
      "target": {
        "@type": "EntryPoint",
        "encodingType": "text/html",
        "name": "name of the proposal",
        "url": "https://example.org/locatorForProposalText",
        "identifier": "identifier for proposal, could used text or schema:PropertyValue pattern"
      }
    }
  ],
  "schema:subjectOf": {
    "@id": "xas:ja51-pz63",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:dateModified": "2025-08-26",
    "schema:creator": [
      {
        "@id": "https://ada.org/person/3479",
        "@type": "schema:Person",
        "schema:name": "Richard, Stephen M.",
        "schema:identifier": "https://orcid.org/0000-0002-7933-2154",
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
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
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/xasDiscovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/xasCore/1.0/"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix xas: <https://xas.org/dictionary/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

xas:487y54123 a schema1:Dataset,
        schema1:Product ;
    cdi:relatedLink [ a cdi:LinkRole ;
            cdi:linkRelationship "projectProposal" ;
            cdi:target [ a cdi:EntryPoint ;
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
            cdi:hasPhysicalMapping [ cdi:format "decimal" ;
                    cdi:formats_InstanceVariable xas:incidentIntensity ;
                    cdi:index 2 ;
                    cdi:isRequired true ;
                    cdi:physicalDataType "float64" ],
                [ cdi:format "decimal" ;
                    cdi:formats_InstanceVariable xas:transmittedIntensity ;
                    cdi:index 1 ;
                    cdi:isRequired true ;
                    cdi:physicalDataType "float64" ],
                [ cdi:format "decimal" ;
                    cdi:formats_InstanceVariable xas:monochromatorEnergy ;
                    cdi:index 0 ;
                    cdi:isRequired true ;
                    cdi:physicalDataType "float64" ] ;
            cdi:isFixedWidth true ;
            dcterms:conformsTo <https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md> ;
            schema1:contentUrl "https://github.com/XraySpectroscopy/XASDataLibrary/blob/master/data/Se/Se_Na2SeO4_rt_01.xdi" ;
            schema1:description "Fixed-width text file conformant with XDI specification. Contains three data columns: monochromator energy (eV), transmitted intensity (counts), and incident intensity (counts). 27-line header with comment prefix '#'." ;
            schema1:encodingFormat "text/plain" ;
            schema1:name "XDI data file for Se K-edge XAS" ] ;
    schema1:identifier "https://doi.org/10.9999/aqweropjh" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier "missing" ;
            schema1:inDefinedTermSet "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md" ;
            schema1:name "K-edge" ;
            schema1:termCode "K" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "http://sweetontology.net/matrElement/Selenium" ;
            schema1:inDefinedTermSet "http://sweetontology.net/matrElement" ;
            schema1:name "Selenium" ;
            schema1:termCode "Se" ] ;
    schema1:license "https://creativecommons.org/publicdomain/zero/1.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "http://purl.org/pan-science/PaNET/PaNET01196" ;
            schema1:inDefinedTermSet "http://purl.org/pan-science/PaNET/PaNET.owl" ;
            schema1:name "X-Ray Absorption Spectroscopy" ;
            schema1:termCode "XAS" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "xas:transmissionMode" ;
            schema1:inDefinedTermSet "nxs:Field/NXxas/ENTRY/DATA/mode" ;
            schema1:name "Transmission" ] ;
    schema1:name "X-ray absorption spectra for K edge, Iron metal, XDI CDIF example" ;
    schema1:subjectOf xas:ja51-pz63 ;
    schema1:variableMeasured xas:incidentIntensity,
        xas:monochromatorEnergy,
        xas:transmittedIntensity ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity,
                xas:AnalysisEvent ;
            schema1:additionalProperty [ a schema1:PropertyValue ;
                    schema1:name "calibration method" ;
                    schema1:propertyID "nxs:Group/NXdetector/calibration_method" ;
                    schema1:url "http://protocols.io/link/to/calibrationMethod" ;
                    schema1:value "description of calibration procedure" ],
                [ a schema1:PropertyValue ;
                    schema1:description "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential" ;
                    schema1:name "experiment environment-pressure" ;
                    schema1:propertyID "xas:pressure" ;
                    schema1:unitText "KPa" ;
                    schema1:value 3567 ],
                [ a schema1:PropertyValue ;
                    schema1:name "Installed Options" ;
                    schema1:propertyID "xas:installedOptions" ;
                    schema1:value "Description of extra equipment installed on the base instrument(?)" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Absorption edge" ;
                    schema1:propertyID "xas:edge_energy" ;
                    schema1:unitText "eV" ;
                    schema1:value "12658.0" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Instrument configuration" ;
                    schema1:propertyID "nxs:Group/NXentry/experiment_documentation" ;
                    schema1:url "http://protocols.io/link/to/calibrationMethod" ;
                    schema1:value "description of instrument configuration" ] ;
            schema1:identifier "20241111_DSC_NU_OREX-803224-0_1" ;
            schema1:location ex:xasfacility_37yht ;
            schema1:mainEntity [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "parent sample identifier" ;
                            schema1:propertyID "xas:parentSample" ;
                            schema1:value "igsn:10.3476/342573" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Porosity" ;
                            schema1:propertyID "xas:porosity" ;
                            schema1:unitText "percent" ;
                            schema1:value 27 ],
                        [ a schema1:PropertyValue ;
                            schema1:name "material state" ;
                            schema1:propertyID "xas:materialState" ;
                            schema1:value "solid metal foil" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "samaple preparation method" ;
                            schema1:propertyID "xas:samplePreparation" ;
                            schema1:value "powder on tape, 6 layers" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Crystal unit cell dimensions" ;
                            schema1:propertyID "nxs:Field/NXsample/unit_cell" ;
                            schema1:value "cubic; Z = 4; a = 5.46; V = 162.77" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "crystallographic point group" ;
                            schema1:propertyID "nxs:Field/NXsample/point_group" ;
                            schema1:value "mm2" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Stoichiometry" ;
                            schema1:propertyID "xas:stoichiometry" ;
                            schema1:value "Na2SeO4" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "sample mass" ;
                            schema1:propertyID "nxs:Field/NXsample/mass" ;
                            schema1:unitText "mg" ;
                            schema1:value "10" ] ;
                    schema1:additionalType "MaterialSample",
                        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample" ;
                    schema1:description "physical properties of sample: ph, eh, volume, porosity, density, concentration, resistivity, viscosity, crystal structure, opacity from xdi list..." ;
                    schema1:identifier "igsn:10.6620/357lkj" ;
                    schema1:name "Na2SeO4" ] ;
            schema1:startDate "2008-04-10T21:58:50" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "crystal type" ;
                            schema1:propertyID "nxs:Field/NXcrystal/type" ;
                            schema1:value "missing" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "reflection plane (hkl)" ;
                            schema1:propertyID "nxs:Field/NXcrystal/reflection" ;
                            schema1:value "1,1,1" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "d-spacing" ;
                            schema1:propertyID "nxs:Field/NXcrystal/d_spacing" ;
                            schema1:unitText "Angstrom" ;
                            schema1:value "3.13550" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "chemical formula" ;
                            schema1:propertyID "nxs:Field/NXcrystal/chemical_formula" ;
                            schema1:value "Si" ] ;
                    schema1:additionalType "nxs:BaseClass/NXmonochromator" ;
                    schema1:name "Si 111" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "Probe" ;
                            schema1:propertyID "nxs:Field/NXsource/probe" ;
                            schema1:value "x-ray" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "x-ray source" ;
                            schema1:propertyID "nxs:Field/NXsource/type" ;
                            schema1:value "Synchrotron X-ray Source" ] ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:identifier "should have a registry with URIs" ;
                    schema1:name "source, made up for this example" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:alternateName "transmitted flux measurement method" ;
                            schema1:name "detector mode it" ;
                            schema1:propertyID "xas:detector.it" ;
                            schema1:value "10cm  N2" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "monitor preset" ;
                            schema1:propertyID "nxs:Field/NXmonitor/preset" ;
                            schema1:value "N.A." ],
                        [ a schema1:PropertyValue ;
                            schema1:alternateName "incident flux measurement method" ;
                            schema1:name "detector mode i0" ;
                            schema1:propertyID "xas:detector.i0" ;
                            schema1:value "10cm  N2" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "monitor mode" ;
                            schema1:propertyID "nxs:Field/NXmonitor/mode" ;
                            schema1:value "monitor" ] ;
                    schema1:additionalType "nxs:BaseClass/NXmonitor" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "focusing" ;
                            schema1:propertyID "xas:focusing" ;
                            schema1:value "???" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "harmonic_rejection" ;
                            schema1:propertyID "xas:harmonic_rejection" ;
                            schema1:value "Rh-coated mirror, detuned" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "collimation technique" ;
                            schema1:propertyID "xas:collimation" ;
                            schema1:value "none" ] ;
                    schema1:additionalType "xas:Beamline" ;
                    schema1:identifier "should have a registry with URIs" ;
                    schema1:name "13-BM-D" ] ] .

<https://ada.org/person/3479> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "smrTucson@email.org" ] ;
    schema1:identifier "https://orcid.org/0000-0002-7933-2154" ;
    schema1:name "Richard, Stephen M." .

ex:xasfacility_37yht a schema1:Place ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "X-ray Source" ;
            schema1:propertyID "xas:xray_source" ;
            schema1:value "APS bending magnet" ],
        [ a schema1:PropertyValue ;
            schema1:name "Facility energy" ;
            schema1:propertyID "xas:energy" ;
            schema1:unitText "GeV" ;
            schema1:value "7.00" ],
        [ a schema1:PropertyValue ;
            schema1:name "Facility current" ;
            schema1:propertyID "xas:current" ;
            schema1:unitText "Amps" ;
            schema1:value "120" ] ;
    schema1:additionalType "xas:Facility" ;
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
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/>,
        <https://w3id.org/cdif/xasCore/1.0/>,
        <https://w3id.org/cdif/xasDiscovery/1.0/> ;
    schema1:about xas:485749 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:creator <https://ada.org/person/3479> ;
    schema1:dateModified "2025-08-26" ;
    schema1:description "metadata about documentation for se_na2so4" .

<https://orcid.org/3547ulkj> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "missing@email.org" ] ;
    schema1:name "Collectus, Poindexter" .

xas:incidentIntensity a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "monitor intensity" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "i0" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:uses "xas:incidentIntensityConcept" ;
    schema1:alternateName "Monitor intensity" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description)" ;
    schema1:name "i0 monitory intensity" ;
    schema1:propertyID "xas:incidentIntensityConcept" ;
    schema1:unitText "counts" .

xas:monochromatorEnergy a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "monochromator energy" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "energy" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:simpleUnitOfMeasure "eV" ;
    cdi:uses "xas:monochromatorEnergyConcept" ;
    schema1:alternateName "Monochromator energy" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description" ;
    schema1:name "energy" ;
    schema1:propertyID "xas:monochromatorEnergyConcept" ;
    schema1:unitText "eV" .

xas:transmittedIntensity a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "transmission intensity" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "itrans" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:uses "xas:transmittedIntensityConcept" ;
    schema1:alternateName "transmission intensity" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description" ;
    schema1:name "itrans" ;
    schema1:propertyID "xas:transmittedIntensityConcept" ;
    schema1:unitText "counts" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: CDIF XAS metadata profile
description: CDIF XAS profile for X-ray Absorption Spectroscopy datasets. Composes
  cdifCore with discovery properties and XAS-specific constraints.
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCore/schema.yaml
- type: object
  properties:
    '@context':
      type: object
      description: Additional JSON-LD namespace prefixes for discovery and XAS properties.
      properties:
        geosparql:
          const: http://www.opengis.net/ont/geosparql#
        dqv:
          const: http://www.w3.org/ns/dqv#
        cdi:
          const: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
    schema:measurementTechnique:
      description: The technique, technology, or methodology used for measurement
        or determination of the dataset values.
      anyOf:
      - type: string
      - $ref: '#/$defs/DefinedTerm'
      - type: array
        items:
          anyOf:
          - type: string
          - $ref: '#/$defs/DefinedTerm'
    schema:variableMeasured:
      description: What does the dataset measure? (e.g., temperature, pressure)
      type: array
      items:
        anyOf:
        - $ref: '#/$defs/VariableMeasured'
        - $ref: '#/$defs/StatisticalVariable'
    schema:spatialCoverage:
      description: Geographic extent of resource content.
      type: array
      items:
        $ref: '#/$defs/SpatialExtent'
    schema:temporalCoverage:
      description: Temporal extent of resource content.
      type: array
      items:
        $ref: '#/$defs/TemporalExtent'
    dqv:hasQualityMeasurement:
      description: Quality measurements reported to assess the resource.
      type: array
      items:
        $ref: '#/$defs/QualityMeasure'
    schema:subjectOf:
      properties:
        dcterms:conformsTo:
          contains:
            type: object
            properties:
              '@id':
                const: https://w3id.org/cdif/discovery/1.0/
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasOptional/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasCore/schema.yaml
$defs:
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  VariableMeasured:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.yaml
  StatisticalVariable:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/statisticalVariable/schema.yaml
  SpatialExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
  TemporalExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/temporalExtent/schema.yaml
  QualityMeasure:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  dcterms: http://purl.org/dc/terms/
  geosparql: http://www.opengis.net/ont/geosparql#
  spdx: http://spdx.org/rdf/terms#
  time: http://www.w3.org/2006/time#
  skos: http://www.w3.org/2004/02/skos/core#
  xas: https://xas.org/dictionary/
  nxs: http://purl.org/nexusformat/definitions/
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFxas/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFxas/schema.yaml)


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
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "time": "http://www.w3.org/2006/time#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFxas/context.jsonld)

## Sources

* [CDIF book](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#schema-org-implementation-of-cdif-metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifProfiles/CDIFxas`

