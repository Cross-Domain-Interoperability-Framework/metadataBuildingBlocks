
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
        "@id": "https://w3id.org/cdif/provenance/1.0"
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
        "@id": "https://w3id.org/cdif/provenance/1.0"
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
    dcterms:conformsTo <https://w3id.org/cdif/provenance/1.0> ;
    schema1:about ex:dataset_with_provenance_001 ;
    schema1:additionalType "dcat:CatalogRecord" .


```


### EPMA Provenance with actionProcess HowTo and steps
Electron microprobe analysis of olivine with three chained activities
(sample preparation, WDS analysis, data reduction). Each activity uses
schema:actionProcess with a schema:HowTo containing ordered
schema:HowToStep entries describing the methodology. Activities are
linked via schema:object references for action chaining.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "bios": "https://bioschemas.org/",
    "ex": "https://example.org/"
  },
  "@id": "ex:dataset_epma_olivine_001",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Olivine major element compositions, Kilauea Iki lava lake",
  "schema:identifier": "https://doi.org/10.1234/olivine-kilauea-2024",
  "schema:dateModified": "2024-08-15",
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:metadata_epma_olivine_001",
    "schema:about": {
      "@id": "ex:dataset_epma_olivine_001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      }
    ]
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "@id": "#SamplePreparation",
      "schema:name": "Sample preparation for EPMA",
      "schema:additionalType": [
        "schema:CreateAction",
        "bios:LabProcess"
      ],
      "schema:description": "Olivine grains from Kilauea Iki lava lake drill core KI81-1 mounted in epoxy, ground, polished, and carbon coated for electron microprobe analysis.",
      "schema:actionProcess": {
        "@type": [
          "schema:HowTo"
        ],
        "schema:name": "EPMA sample preparation protocol",
        "schema:step": [
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Grain mounting",
            "schema:position": 1,
            "schema:description": "Selected olivine grains picked from crushed drill core and mounted in 1-inch epoxy rounds."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Grinding and polishing",
            "schema:position": 2,
            "schema:description": "Mounts ground with SiC paper (240–1200 grit) then polished with diamond suspension (6 um, 3 um, 1 um) to achieve flat, scratch-free surface."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Carbon coating",
            "schema:position": 3,
            "schema:description": "Polished mounts coated with ~20 nm amorphous carbon using a Denton DV-502A vacuum evaporator for electrical conductivity."
          }
        ]
      },
      "schema:actionStatus": "schema:CompletedActionStatus",
      "schema:startTime": "2024-06-01",
      "schema:endTime": "2024-06-03",
      "schema:agent": {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Chen, Wei",
        "schema:identifier": "https://orcid.org/0000-0002-5555-6666"
      },
      "prov:used": [
        {
          "@id": "#KI81-1-olivine",
          "schema:name": "Olivine separates from drill core KI81-1",
          "schema:description": "Hand-picked olivine grains (Fo85-88) from Kilauea Iki lava lake drill core."
        }
      ],
      "schema:result": [
        {
          "@id": "#PolishedMount-A",
          "schema:name": "Polished and carbon-coated epoxy mount A"
        }
      ]
    },
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "@id": "#EPMAAnalysis",
      "schema:name": "EPMA major element analysis of olivine",
      "schema:additionalType": [
        "schema:CreateAction",
        "bios:LabProcess"
      ],
      "schema:description": "Quantitative WDS electron microprobe analysis of olivine for major and minor elements using a JEOL JXA-8530F field-emission electron microprobe at 15 kV / 20 nA.",
      "schema:actionProcess": {
        "@type": [
          "schema:HowTo"
        ],
        "@id": "https://registry.onegeochemistry.org/methods/jeol-8530f-olivine-v1",
        "schema:name": "JEOL-8530F WDS olivine major elements v1.0",
        "schema:url": "https://doi.org/10.5281/zenodo.example-olivine-method",
        "schema:step": [
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Instrument calibration",
            "schema:position": 1,
            "schema:description": "Calibrate WDS spectrometers on primary standards: San Carlos olivine (SiO2, MgO, FeO), chromite NMNH 117075 (Cr2O3), rhodonite (MnO), Kakanui hornblende (CaO, TiO2), jadeite (Na2O, Al2O3), synthetic NiO (NiO). Verify calibration on secondary standard San Carlos olivine NMNH 111312/444."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Beam condition setup",
            "schema:position": 2,
            "schema:description": "Set accelerating voltage to 15 kV, beam current to 20 nA measured on Faraday cup, focused beam (~1 um). Verify beam current stability within 0.5% over 5 minutes."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "WDS acquisition",
            "schema:position": 3,
            "schema:description": "Acquire major elements simultaneously on 5 WDS spectrometers: Sp1 TAP (SiO2 Ka 30s, Al2O3 Ka 40s), Sp2 LiFH (FeO Ka 30s, MnO Ka 30s), Sp3 PETJ (CaO Ka 30s, TiO2 Ka 40s, Cr2O3 Ka 30s), Sp4 TAP (MgO Ka 30s), Sp5 LiF (NiO Ka 40s). Backgrounds measured on both sides of each peak."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Matrix correction and quantification",
            "schema:position": 4,
            "schema:description": "Apply ZAF matrix correction using Probe for EPMA v13.0.6 with LINEMU mass absorption coefficients. Report oxide weight percent with oxygen calculated by stoichiometry."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Quality control",
            "schema:position": 5,
            "schema:description": "Analyze San Carlos olivine NMNH 111312/444 as secondary standard at start, middle, and end of each session. Accept session if all major elements within 1% relative of accepted values. Monitor Faraday cup current every 30 minutes; recalibrate if drift exceeds 1%."
          }
        ]
      },
      "schema:actionStatus": "schema:CompletedActionStatus",
      "schema:startTime": "2024-06-10T08:00:00Z",
      "schema:endTime": "2024-06-10T17:30:00Z",
      "schema:agent": {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Chen, Wei",
        "schema:identifier": "https://orcid.org/0000-0002-5555-6666"
      },
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:Product",
              "schema:Thing"
            ],
            "schema:name": "JEOL JXA-8530F Plus Field Emission Electron Microprobe",
            "schema:manufacturer": {
              "@type": [
                "schema:Organization"
              ],
              "schema:name": "JEOL"
            },
            "schema:model": {
              "@type": [
                "schema:ProductModel"
              ],
              "schema:name": "JXA-8530F Plus"
            }
          }
        },
        {
          "@id": "#PolishedMount-A"
        }
      ],
      "schema:object": {
        "@id": "#SamplePreparation"
      },
      "schema:result": [
        {
          "@id": "#OlivineCompositions",
          "schema:name": "Quantitative olivine WDS analyses",
          "schema:description": "142 point analyses of olivine major and minor element oxide concentrations (wt%) with detection limits and analytical totals."
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Electron Microprobe Laboratory, Department of Earth Sciences, Example University"
      },
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:name": "Accelerating Voltage",
          "schema:value": 15,
          "schema:unitText": "kV"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:name": "Beam Current",
          "schema:value": 20,
          "schema:unitText": "nA"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:name": "Beam Diameter",
          "schema:value": "focused (~1 um)"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:name": "Matrix Correction Model",
          "schema:value": "ZAF (LINEMU MACs)"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:name": "Number of Analyses",
          "schema:value": 142
        }
      ]
    },
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "@id": "#DataReduction",
      "schema:name": "Data reduction and filtering",
      "schema:additionalType": [
        "schema:CreateAction"
      ],
      "schema:description": "Analyses filtered for quality: rejected points with analytical totals outside 98.5–101.0 wt% or with anomalous stoichiometry. Forsterite content (Fo) calculated from Mg/(Mg+Fe) atomic ratio. Final dataset exported as CSV.",
      "schema:actionProcess": {
        "@type": [
          "schema:HowTo"
        ],
        "schema:name": "EPMA data reduction protocol",
        "schema:step": [
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Total oxide filter",
            "schema:position": 1,
            "schema:description": "Reject analyses with oxide totals < 98.5% or > 101.0%."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Stoichiometry check",
            "schema:position": 2,
            "schema:description": "Calculate cations per 4 oxygen. Reject analyses with Si > 1.02 or total cations outside 2.98–3.02 (expected 3.00 for olivine)."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Forsterite calculation and export",
            "schema:position": 3,
            "schema:description": "Calculate Fo = 100 * Mg/(Mg+Fe) from atomic proportions. Export accepted analyses with Fo, oxide wt%, detection limits, and analytical totals to CSV."
          }
        ]
      },
      "schema:actionStatus": "schema:CompletedActionStatus",
      "schema:startTime": "2024-06-12",
      "schema:endTime": "2024-06-12",
      "schema:agent": {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Chen, Wei",
        "schema:identifier": "https://orcid.org/0000-0002-5555-6666"
      },
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "Probe for EPMA",
            "schema:version": "13.0.6",
            "schema:url": "https://www.probesoftware.com/"
          }
        }
      ],
      "schema:object": {
        "@id": "#EPMAAnalysis"
      },
      "schema:result": [
        {
          "@id": "ex:dataset_epma_olivine_001",
          "schema:name": "Final olivine composition dataset"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvenance/context.jsonld",
    {
      "schema": "http://schema.org/",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "bios": "https://bioschemas.org/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:dataset_epma_olivine_001",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Olivine major element compositions, Kilauea Iki lava lake",
  "schema:identifier": "https://doi.org/10.1234/olivine-kilauea-2024",
  "schema:dateModified": "2024-08-15",
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:metadata_epma_olivine_001",
    "schema:about": {
      "@id": "ex:dataset_epma_olivine_001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      }
    ]
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "@id": "#SamplePreparation",
      "schema:name": "Sample preparation for EPMA",
      "schema:additionalType": [
        "schema:CreateAction",
        "bios:LabProcess"
      ],
      "schema:description": "Olivine grains from Kilauea Iki lava lake drill core KI81-1 mounted in epoxy, ground, polished, and carbon coated for electron microprobe analysis.",
      "schema:actionProcess": {
        "@type": [
          "schema:HowTo"
        ],
        "schema:name": "EPMA sample preparation protocol",
        "schema:step": [
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Grain mounting",
            "schema:position": 1,
            "schema:description": "Selected olivine grains picked from crushed drill core and mounted in 1-inch epoxy rounds."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Grinding and polishing",
            "schema:position": 2,
            "schema:description": "Mounts ground with SiC paper (240\u20131200 grit) then polished with diamond suspension (6 um, 3 um, 1 um) to achieve flat, scratch-free surface."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Carbon coating",
            "schema:position": 3,
            "schema:description": "Polished mounts coated with ~20 nm amorphous carbon using a Denton DV-502A vacuum evaporator for electrical conductivity."
          }
        ]
      },
      "schema:actionStatus": "schema:CompletedActionStatus",
      "schema:startTime": "2024-06-01",
      "schema:endTime": "2024-06-03",
      "schema:agent": {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Chen, Wei",
        "schema:identifier": "https://orcid.org/0000-0002-5555-6666"
      },
      "prov:used": [
        {
          "@id": "#KI81-1-olivine",
          "schema:name": "Olivine separates from drill core KI81-1",
          "schema:description": "Hand-picked olivine grains (Fo85-88) from Kilauea Iki lava lake drill core."
        }
      ],
      "schema:result": [
        {
          "@id": "#PolishedMount-A",
          "schema:name": "Polished and carbon-coated epoxy mount A"
        }
      ]
    },
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "@id": "#EPMAAnalysis",
      "schema:name": "EPMA major element analysis of olivine",
      "schema:additionalType": [
        "schema:CreateAction",
        "bios:LabProcess"
      ],
      "schema:description": "Quantitative WDS electron microprobe analysis of olivine for major and minor elements using a JEOL JXA-8530F field-emission electron microprobe at 15 kV / 20 nA.",
      "schema:actionProcess": {
        "@type": [
          "schema:HowTo"
        ],
        "@id": "https://registry.onegeochemistry.org/methods/jeol-8530f-olivine-v1",
        "schema:name": "JEOL-8530F WDS olivine major elements v1.0",
        "schema:url": "https://doi.org/10.5281/zenodo.example-olivine-method",
        "schema:step": [
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Instrument calibration",
            "schema:position": 1,
            "schema:description": "Calibrate WDS spectrometers on primary standards: San Carlos olivine (SiO2, MgO, FeO), chromite NMNH 117075 (Cr2O3), rhodonite (MnO), Kakanui hornblende (CaO, TiO2), jadeite (Na2O, Al2O3), synthetic NiO (NiO). Verify calibration on secondary standard San Carlos olivine NMNH 111312/444."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Beam condition setup",
            "schema:position": 2,
            "schema:description": "Set accelerating voltage to 15 kV, beam current to 20 nA measured on Faraday cup, focused beam (~1 um). Verify beam current stability within 0.5% over 5 minutes."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "WDS acquisition",
            "schema:position": 3,
            "schema:description": "Acquire major elements simultaneously on 5 WDS spectrometers: Sp1 TAP (SiO2 Ka 30s, Al2O3 Ka 40s), Sp2 LiFH (FeO Ka 30s, MnO Ka 30s), Sp3 PETJ (CaO Ka 30s, TiO2 Ka 40s, Cr2O3 Ka 30s), Sp4 TAP (MgO Ka 30s), Sp5 LiF (NiO Ka 40s). Backgrounds measured on both sides of each peak."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Matrix correction and quantification",
            "schema:position": 4,
            "schema:description": "Apply ZAF matrix correction using Probe for EPMA v13.0.6 with LINEMU mass absorption coefficients. Report oxide weight percent with oxygen calculated by stoichiometry."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Quality control",
            "schema:position": 5,
            "schema:description": "Analyze San Carlos olivine NMNH 111312/444 as secondary standard at start, middle, and end of each session. Accept session if all major elements within 1% relative of accepted values. Monitor Faraday cup current every 30 minutes; recalibrate if drift exceeds 1%."
          }
        ]
      },
      "schema:actionStatus": "schema:CompletedActionStatus",
      "schema:startTime": "2024-06-10T08:00:00Z",
      "schema:endTime": "2024-06-10T17:30:00Z",
      "schema:agent": {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Chen, Wei",
        "schema:identifier": "https://orcid.org/0000-0002-5555-6666"
      },
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:Product",
              "schema:Thing"
            ],
            "schema:name": "JEOL JXA-8530F Plus Field Emission Electron Microprobe",
            "schema:manufacturer": {
              "@type": [
                "schema:Organization"
              ],
              "schema:name": "JEOL"
            },
            "schema:model": {
              "@type": [
                "schema:ProductModel"
              ],
              "schema:name": "JXA-8530F Plus"
            }
          }
        },
        {
          "@id": "#PolishedMount-A"
        }
      ],
      "schema:object": {
        "@id": "#SamplePreparation"
      },
      "schema:result": [
        {
          "@id": "#OlivineCompositions",
          "schema:name": "Quantitative olivine WDS analyses",
          "schema:description": "142 point analyses of olivine major and minor element oxide concentrations (wt%) with detection limits and analytical totals."
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Electron Microprobe Laboratory, Department of Earth Sciences, Example University"
      },
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:name": "Accelerating Voltage",
          "schema:value": 15,
          "schema:unitText": "kV"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:name": "Beam Current",
          "schema:value": 20,
          "schema:unitText": "nA"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:name": "Beam Diameter",
          "schema:value": "focused (~1 um)"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:name": "Matrix Correction Model",
          "schema:value": "ZAF (LINEMU MACs)"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:name": "Number of Analyses",
          "schema:value": 142
        }
      ]
    },
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "@id": "#DataReduction",
      "schema:name": "Data reduction and filtering",
      "schema:additionalType": [
        "schema:CreateAction"
      ],
      "schema:description": "Analyses filtered for quality: rejected points with analytical totals outside 98.5\u2013101.0 wt% or with anomalous stoichiometry. Forsterite content (Fo) calculated from Mg/(Mg+Fe) atomic ratio. Final dataset exported as CSV.",
      "schema:actionProcess": {
        "@type": [
          "schema:HowTo"
        ],
        "schema:name": "EPMA data reduction protocol",
        "schema:step": [
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Total oxide filter",
            "schema:position": 1,
            "schema:description": "Reject analyses with oxide totals < 98.5% or > 101.0%."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Stoichiometry check",
            "schema:position": 2,
            "schema:description": "Calculate cations per 4 oxygen. Reject analyses with Si > 1.02 or total cations outside 2.98\u20133.02 (expected 3.00 for olivine)."
          },
          {
            "@type": [
              "schema:HowToStep"
            ],
            "schema:name": "Forsterite calculation and export",
            "schema:position": 3,
            "schema:description": "Calculate Fo = 100 * Mg/(Mg+Fe) from atomic proportions. Export accepted analyses with Fo, oxide wt%, detection limits, and analytical totals to CSV."
          }
        ]
      },
      "schema:actionStatus": "schema:CompletedActionStatus",
      "schema:startTime": "2024-06-12",
      "schema:endTime": "2024-06-12",
      "schema:agent": {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Chen, Wei",
        "schema:identifier": "https://orcid.org/0000-0002-5555-6666"
      },
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "Probe for EPMA",
            "schema:version": "13.0.6",
            "schema:url": "https://www.probesoftware.com/"
          }
        }
      ],
      "schema:object": {
        "@id": "#EPMAAnalysis"
      },
      "schema:result": [
        {
          "@id": "ex:dataset_epma_olivine_001",
          "schema:name": "Final olivine composition dataset"
        }
      ]
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
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/#DataReduction> a schema1:Action,
        prov:Activity ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:name "EPMA data reduction protocol" ;
            schema1:step [ a schema1:HowToStep ;
                    schema1:description "Calculate cations per 4 oxygen. Reject analyses with Si > 1.02 or total cations outside 2.98–3.02 (expected 3.00 for olivine)." ;
                    schema1:name "Stoichiometry check" ;
                    schema1:position 2 ],
                [ a schema1:HowToStep ;
                    schema1:description "Calculate Fo = 100 * Mg/(Mg+Fe) from atomic proportions. Export accepted analyses with Fo, oxide wt%, detection limits, and analytical totals to CSV." ;
                    schema1:name "Forsterite calculation and export" ;
                    schema1:position 3 ],
                [ a schema1:HowToStep ;
                    schema1:description "Reject analyses with oxide totals < 98.5% or > 101.0%." ;
                    schema1:name "Total oxide filter" ;
                    schema1:position 1 ] ] ;
    schema1:actionStatus "schema:CompletedActionStatus" ;
    schema1:additionalType "schema:CreateAction" ;
    schema1:agent [ a schema1:Person ;
            schema1:identifier "https://orcid.org/0000-0002-5555-6666" ;
            schema1:name "Chen, Wei" ] ;
    schema1:description "Analyses filtered for quality: rejected points with analytical totals outside 98.5–101.0 wt% or with anomalous stoichiometry. Forsterite content (Fo) calculated from Mg/(Mg+Fe) atomic ratio. Final dataset exported as CSV." ;
    schema1:endTime "2024-06-12" ;
    schema1:name "Data reduction and filtering" ;
    schema1:object <file:///github/workspace/#EPMAAnalysis> ;
    schema1:result ex:dataset_epma_olivine_001 ;
    schema1:startTime "2024-06-12" ;
    prov:used [ schema1:instrument [ a schema1:SoftwareApplication ;
                    schema1:name "Probe for EPMA" ;
                    schema1:url "https://www.probesoftware.com/" ;
                    schema1:version "13.0.6" ] ] .

<file:///github/workspace/#KI81-1-olivine> schema1:description "Hand-picked olivine grains (Fo85-88) from Kilauea Iki lava lake drill core." ;
    schema1:name "Olivine separates from drill core KI81-1" .

<file:///github/workspace/#OlivineCompositions> schema1:description "142 point analyses of olivine major and minor element oxide concentrations (wt%) with detection limits and analytical totals." ;
    schema1:name "Quantitative olivine WDS analyses" .

ex:metadata_epma_olivine_001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/provenance/1.0> ;
    schema1:about ex:dataset_epma_olivine_001 ;
    schema1:additionalType "dcat:CatalogRecord" .

<https://registry.onegeochemistry.org/methods/jeol-8530f-olivine-v1> a schema1:HowTo ;
    schema1:name "JEOL-8530F WDS olivine major elements v1.0" ;
    schema1:step [ a schema1:HowToStep ;
            schema1:description "Acquire major elements simultaneously on 5 WDS spectrometers: Sp1 TAP (SiO2 Ka 30s, Al2O3 Ka 40s), Sp2 LiFH (FeO Ka 30s, MnO Ka 30s), Sp3 PETJ (CaO Ka 30s, TiO2 Ka 40s, Cr2O3 Ka 30s), Sp4 TAP (MgO Ka 30s), Sp5 LiF (NiO Ka 40s). Backgrounds measured on both sides of each peak." ;
            schema1:name "WDS acquisition" ;
            schema1:position 3 ],
        [ a schema1:HowToStep ;
            schema1:description "Analyze San Carlos olivine NMNH 111312/444 as secondary standard at start, middle, and end of each session. Accept session if all major elements within 1% relative of accepted values. Monitor Faraday cup current every 30 minutes; recalibrate if drift exceeds 1%." ;
            schema1:name "Quality control" ;
            schema1:position 5 ],
        [ a schema1:HowToStep ;
            schema1:description "Apply ZAF matrix correction using Probe for EPMA v13.0.6 with LINEMU mass absorption coefficients. Report oxide weight percent with oxygen calculated by stoichiometry." ;
            schema1:name "Matrix correction and quantification" ;
            schema1:position 4 ],
        [ a schema1:HowToStep ;
            schema1:description "Set accelerating voltage to 15 kV, beam current to 20 nA measured on Faraday cup, focused beam (~1 um). Verify beam current stability within 0.5% over 5 minutes." ;
            schema1:name "Beam condition setup" ;
            schema1:position 2 ],
        [ a schema1:HowToStep ;
            schema1:description "Calibrate WDS spectrometers on primary standards: San Carlos olivine (SiO2, MgO, FeO), chromite NMNH 117075 (Cr2O3), rhodonite (MnO), Kakanui hornblende (CaO, TiO2), jadeite (Na2O, Al2O3), synthetic NiO (NiO). Verify calibration on secondary standard San Carlos olivine NMNH 111312/444." ;
            schema1:name "Instrument calibration" ;
            schema1:position 1 ] ;
    schema1:url "https://doi.org/10.5281/zenodo.example-olivine-method" .

<file:///github/workspace/#EPMAAnalysis> a schema1:Action,
        prov:Activity ;
    schema1:actionProcess <https://registry.onegeochemistry.org/methods/jeol-8530f-olivine-v1> ;
    schema1:actionStatus "schema:CompletedActionStatus" ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Beam Diameter" ;
            schema1:value "focused (~1 um)" ],
        [ a schema1:PropertyValue ;
            schema1:name "Beam Current" ;
            schema1:unitText "nA" ;
            schema1:value 20 ],
        [ a schema1:PropertyValue ;
            schema1:name "Matrix Correction Model" ;
            schema1:value "ZAF (LINEMU MACs)" ],
        [ a schema1:PropertyValue ;
            schema1:name "Number of Analyses" ;
            schema1:value 142 ],
        [ a schema1:PropertyValue ;
            schema1:name "Accelerating Voltage" ;
            schema1:unitText "kV" ;
            schema1:value 15 ] ;
    schema1:additionalType "bios:LabProcess",
        "schema:CreateAction" ;
    schema1:agent [ a schema1:Person ;
            schema1:identifier "https://orcid.org/0000-0002-5555-6666" ;
            schema1:name "Chen, Wei" ] ;
    schema1:description "Quantitative WDS electron microprobe analysis of olivine for major and minor elements using a JEOL JXA-8530F field-emission electron microprobe at 15 kV / 20 nA." ;
    schema1:endTime "2024-06-10T17:30:00Z" ;
    schema1:location [ a schema1:Place ;
            schema1:name "Electron Microprobe Laboratory, Department of Earth Sciences, Example University" ] ;
    schema1:name "EPMA major element analysis of olivine" ;
    schema1:object <file:///github/workspace/#SamplePreparation> ;
    schema1:result <file:///github/workspace/#OlivineCompositions> ;
    schema1:startTime "2024-06-10T08:00:00Z" ;
    prov:used [ schema1:instrument [ a schema1:Product,
                        schema1:Thing ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "JEOL" ] ;
                    schema1:model [ a schema1:ProductModel ;
                            schema1:name "JXA-8530F Plus" ] ;
                    schema1:name "JEOL JXA-8530F Plus Field Emission Electron Microprobe" ] ],
        <file:///github/workspace/#PolishedMount-A> .

<file:///github/workspace/#PolishedMount-A> schema1:name "Polished and carbon-coated epoxy mount A" .

<file:///github/workspace/#SamplePreparation> a schema1:Action,
        prov:Activity ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:name "EPMA sample preparation protocol" ;
            schema1:step [ a schema1:HowToStep ;
                    schema1:description "Polished mounts coated with ~20 nm amorphous carbon using a Denton DV-502A vacuum evaporator for electrical conductivity." ;
                    schema1:name "Carbon coating" ;
                    schema1:position 3 ],
                [ a schema1:HowToStep ;
                    schema1:description "Selected olivine grains picked from crushed drill core and mounted in 1-inch epoxy rounds." ;
                    schema1:name "Grain mounting" ;
                    schema1:position 1 ],
                [ a schema1:HowToStep ;
                    schema1:description "Mounts ground with SiC paper (240–1200 grit) then polished with diamond suspension (6 um, 3 um, 1 um) to achieve flat, scratch-free surface." ;
                    schema1:name "Grinding and polishing" ;
                    schema1:position 2 ] ] ;
    schema1:actionStatus "schema:CompletedActionStatus" ;
    schema1:additionalType "bios:LabProcess",
        "schema:CreateAction" ;
    schema1:agent [ a schema1:Person ;
            schema1:identifier "https://orcid.org/0000-0002-5555-6666" ;
            schema1:name "Chen, Wei" ] ;
    schema1:description "Olivine grains from Kilauea Iki lava lake drill core KI81-1 mounted in epoxy, ground, polished, and carbon coated for electron microprobe analysis." ;
    schema1:endTime "2024-06-03" ;
    schema1:name "Sample preparation for EPMA" ;
    schema1:result <file:///github/workspace/#PolishedMount-A> ;
    schema1:startTime "2024-06-01" ;
    prov:used <file:///github/workspace/#KI81-1-olivine> .

ex:dataset_epma_olivine_001 a schema1:Dataset ;
    schema1:dateModified "2024-08-15" ;
    schema1:identifier "https://doi.org/10.1234/olivine-kilauea-2024" ;
    schema1:name "Final olivine composition dataset",
        "Olivine major element compositions, Kilauea Iki lava lake" ;
    schema1:subjectOf ex:metadata_epma_olivine_001 ;
    prov:wasGeneratedBy <file:///github/workspace/#DataReduction>,
        <file:///github/workspace/#EPMAAnalysis>,
        <file:///github/workspace/#SamplePreparation> .


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
              const: https://w3id.org/cdif/provenance/1.0
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

