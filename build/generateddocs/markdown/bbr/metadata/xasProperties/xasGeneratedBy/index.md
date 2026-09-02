
# X-ray absorption, PROV wasGeneratedBy Activity (Schema)

`cdif.bbr.metadata.xasProperties.xasGeneratedBy` *v1.0*

Extends cdifProvActivity with XAS-specific provenance: triple-typed activity (schema:Action + xas:analysisevent + prov:Activity), XAS facility location, sample object, XAS instrument wrappers via prov:used, and XAS additional properties (edge_energy, calibration method, instrument configuration, installedOptions). Defines properties: @type, schema:startTime, schema:endTime, prov:used, schema:additionalProperty, schema:location, schema:object. Uses building blocks: cdifProvActivity (cdifDataType), identifier (schemaorgProperties), xasSample (xasProperties), additionalProperty (schemaorgProperties), xasFacility (xasProperties), xasInstrument (xasProperties).

[*Status*](http://www.opengis.net/def/status): Stable

## Description

## XAS Analysis Event Activity

Extends the [cdifProvActivity](../../cdifProperties/cdifProvActivity/) building block with X-ray Absorption Spectroscopy (XAS)-specific provenance activity typing and properties.

### Key features

- **Activity typing** — requires `@type` of `xas:AnalysisEvent` to distinguish XAS analysis activities from generic provenance.
- **XAS facility location** — `schema:location` references an [xasFacility](../xasFacility/) describing the synchrotron or laboratory where the analysis was performed.
- **Sample object** — `schema:object` references an [xasSample](../xasSample/) describing the sample being analyzed (following the Ocean Info Hub recommendation to use `schema:object` rather than `schema:mainEntity`).
- **XAS-specific instruments** — `prov:used` items accept [xasInstrument](../xasInstrument/) wrappers via `schema:instrument` sub-keys with hierarchical `hasPart` structure for beamline components (source, monochromator, detector).
- **XAS additional properties** — `schema:additionalProperty` supports XAS-specific property IDs: `xas:edge_energy`, `calibration method`, `Instrument configuration`, and `xas:installedOptions`.

## Examples

### Example XAS GeneratedBy activity.
Example XAS GeneratedBy provenance activity
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/",
    "xas": "https://w3id.org/cdif/xas/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "wd": "https://www.wikidata.org/entity/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "ex:exampleGeneratedBy_w46j6j",
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
          "schema:name": "APS bending magnet source",
          "schema:identifier": [
            "https://www.aps.anl.gov/Beamlines/Directory/source/13-BM"
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
              "schema:name": "X-ray source",
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
            "https://www.aps.anl.gov/Beamlines/Directory/13-BM-D"
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
              "schema:name": "beamline collimation",
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
              "schema:value": "unknown"
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
              "schema:name": "Monochromator d-spacing",
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
              "schema:name": "Monochromator chemical formula",
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
              "schema:name": "Monochromator crystal type",
              "schema:value": "crystal type"
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
              "schema:name": "Reflecting plane",
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
      "schema:description": "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential",
      "schema:value": "3567",
      "schema:name": "Environment Pressure",
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
      "schema:value": "12658.0",
      "schema:name": "Edge energy",
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
        "schema:name": "Sample preparation",
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
        "schema:name": "Sample mass",
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
        "schema:name": "Point group",
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
        "schema:name": "Unit cell",
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
        "schema:name": "Parent sample",
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
        "schema:name": "Material state",
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

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasGeneratedBy/context.jsonld",
    {
      "schema": "http://schema.org/",
      "prov": "http://www.w3.org/ns/prov#",
      "ex": "https://example.org/",
      "xas": "https://w3id.org/cdif/xas/",
      "nxs": "https://manual.nexusformat.org/classes/",
      "wd": "https://www.wikidata.org/entity/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@id": "ex:exampleGeneratedBy_w46j6j",
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
          "schema:name": "APS bending magnet source",
          "schema:identifier": [
            "https://www.aps.anl.gov/Beamlines/Directory/source/13-BM"
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
              "schema:name": "X-ray source",
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
            "https://www.aps.anl.gov/Beamlines/Directory/13-BM-D"
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
              "schema:name": "beamline collimation",
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
              "schema:value": "unknown"
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
              "schema:name": "Monochromator d-spacing",
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
              "schema:name": "Monochromator chemical formula",
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
              "schema:name": "Monochromator crystal type",
              "schema:value": "crystal type"
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
              "schema:name": "Reflecting plane",
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
      "schema:description": "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential",
      "schema:value": "3567",
      "schema:name": "Environment Pressure",
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
      "schema:value": "12658.0",
      "schema:name": "Edge energy",
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
        "schema:name": "Sample preparation",
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
        "schema:name": "Sample mass",
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
        "schema:name": "Point group",
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
        "schema:name": "Unit cell",
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
        "schema:name": "Parent sample",
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
        "schema:name": "Material state",
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
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xas: <https://w3id.org/cdif/xas/> .

ex:exampleGeneratedBy_w46j6j a schema1:Action,
        prov:Activity ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
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
            schema1:value "Description of extra equipment installed on the base instrument(?)" ],
        [ a schema1:PropertyValue ;
            schema1:name "Edge energy" ;
            schema1:propertyID xas:edgeenergy ;
            schema1:unitText "eV" ;
            schema1:value "12658.0" ],
        [ a schema1:PropertyValue ;
            schema1:description "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential" ;
            schema1:name "Environment Pressure" ;
            schema1:propertyID xas:pressure ;
            schema1:unitText "KPa" ;
            schema1:value "3567" ] ;
    schema1:additionalType xas:analysisevent ;
    schema1:endTime "2008-04-10T22:14:37" ;
    schema1:identifier "20241111_DSC_NU_OREX-803224-0_1" ;
    schema1:location ex:xasfacility_37yht ;
    schema1:object [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty [ a schema1:PropertyValue ;
                    schema1:name "Sample mass" ;
                    schema1:propertyID xas:samplemass ;
                    schema1:unitText "mg" ;
                    schema1:value "10" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Sample preparation" ;
                    schema1:propertyID xas:samplepreparation ;
                    schema1:value "powder on tape, 6 layers" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Material state" ;
                    schema1:propertyID xas:samplematerial ;
                    schema1:value "solid metal foil" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Stoichiometry" ;
                    schema1:propertyID xas:samplechemicalcomposition ;
                    schema1:value "Na2SeO4" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Porosity" ;
                    schema1:propertyID xas:porosity ;
                    schema1:unitText "percent" ;
                    schema1:value "27" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Unit cell" ;
                    schema1:propertyID xas:sampleunitcell ;
                    schema1:value "cubic; Z = 4; a = 5.46; V = 162.77" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Point group" ;
                    schema1:propertyID xas:pointgroup ;
                    schema1:value "mm2" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Parent sample" ;
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
                            schema1:alternateName "incident flux measurement method" ;
                            schema1:name "detector mode i0" ;
                            schema1:propertyID xas:detectori0 ;
                            schema1:value "10cm  N2" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "monitor mode" ;
                            schema1:propertyID xas:monitormode ;
                            schema1:value "monitor" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "monitor preset" ;
                            schema1:propertyID xas:monitorpreset ;
                            schema1:value "N.A." ],
                        [ a schema1:PropertyValue ;
                            schema1:alternateName "transmitted flux measurement method" ;
                            schema1:name "detector mode it" ;
                            schema1:propertyID xas:detectorit ;
                            schema1:value "10cm  N2" ] ;
                    schema1:additionalType xas:xraymonitor,
                        wd:Q3099911 ;
                    schema1:name "x-ray intensity monitor" ] ],
        [ schema1:instrument [ a schema1:Product,
                        schema1:Thing,
                        prov:Entity ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "X-ray source" ;
                            schema1:propertyID xas:xraysourcetype ;
                            schema1:value "Synchrotron X-ray Source" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Probe" ;
                            schema1:propertyID xas:probe ;
                            schema1:value "x-ray" ] ;
                    schema1:additionalType xas:source,
                        wd:Q3099911 ;
                    schema1:identifier "https://www.aps.anl.gov/Beamlines/Directory/source/13-BM" ;
                    schema1:name "APS bending magnet source" ] ],
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
                            schema1:value "unknown" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "beamline collimation" ;
                            schema1:propertyID xas:collimation ;
                            schema1:value "none" ] ;
                    schema1:additionalType xas:beamline,
                        wd:Q3099911 ;
                    schema1:identifier "https://www.aps.anl.gov/Beamlines/Directory/13-BM-D" ;
                    schema1:name "13-BM-D" ] ],
        [ schema1:instrument [ a schema1:Product,
                        schema1:Thing,
                        prov:Entity ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "Monochromator crystal type" ;
                            schema1:propertyID xas:monochromatortype ;
                            schema1:value "crystal type" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Monochromator d-spacing" ;
                            schema1:propertyID xas:dspacing ;
                            schema1:unitText "Angstrom" ;
                            schema1:value "3.13550" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Monochromator chemical formula" ;
                            schema1:propertyID xas:monochromatorchemicalformula ;
                            schema1:value "Si" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Reflecting plane" ;
                            schema1:propertyID xas:reflectionplane ;
                            schema1:value "1,1,1" ] ;
                    schema1:additionalType xas:xraymonochromator,
                        wd:Q3099911 ;
                    schema1:name "Si 111" ] ] .

ex:xasfacility_37yht a schema1:Place ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Facility current" ;
            schema1:propertyID xas:facilitycurrent ;
            schema1:unitText "Amps" ;
            schema1:value "120" ],
        [ a schema1:PropertyValue ;
            schema1:name "X-ray Source" ;
            schema1:propertyID xas:xraysourcetype ;
            schema1:value "APS bending magnet" ],
        [ a schema1:PropertyValue ;
            schema1:name "Facility energy" ;
            schema1:propertyID xas:facilityenergy ;
            schema1:unitText "GeV" ;
            schema1:value "7.00" ] ;
    schema1:additionalType xas:facility ;
    schema1:identifier "https://ror.org/aps" ;
    schema1:name "APS" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: XAS Analysis Event activity
description: XAS-specific provenance activity building block. Extends cdifProvActivity
  with XAS analysis event typing (xas:analysisevent), XAS facility location, sample
  object, XAS-specific instrument type, and XAS additional properties (edge_energy,
  calibration method, instrument configuration, installedOptions).
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifProvActivity/schema.yaml
- type: object
  required:
  - schema:additionalType
  properties:
    '@type':
      type: array
      items:
        type: string
    schema:additionalType:
      description: Domain type(s) for the activity; must include xas:analysisevent
        (an XAS analysis event).
      type: array
      items:
        anyOf:
        - type: string
        - type: object
          additionalProperties: false
          required:
          - '@id'
          properties:
            '@id':
              type: string
      contains:
        type: object
        additionalProperties: false
        required:
        - '@id'
        properties:
          '@id':
            const: xas:analysisevent
      x-jsonld-id: http://schema.org/additionalType
    schema:startTime:
      type: string
      description: Date/time the XAS analysis started
      x-jsonld-id: http://schema.org/startTime
    schema:endTime:
      type: string
      description: Date/time the XAS analysis finished
      x-jsonld-id: http://schema.org/endTime
    prov:used:
      type: array
      items:
        anyOf:
        - type: object
          required:
          - schema:instrument
          properties:
            schema:instrument:
              type: array
              minItems: 1
              items:
                $ref: '#/$defs/Instrument'
              x-jsonld-id: http://schema.org/instrument
        - type: string
        - type: object
          required:
          - '@id'
          additionalProperties: false
          properties:
            '@id':
              type: string
      allOf:
      - description: Must contain a prov:used entry whose schema:instrument is classified
          as an xas:beamline (via schema:additionalType) and carries a schema:name
          (the beamline name).
        contains:
          type: object
          properties:
            schema:instrument:
              type: array
              contains:
                type: object
                properties:
                  schema:additionalType:
                    anyOf:
                    - type: object
                      additionalProperties: false
                      required:
                      - '@id'
                      properties:
                        '@id':
                          const: xas:beamline
                    - type: array
                      contains:
                        type: object
                        additionalProperties: false
                        required:
                        - '@id'
                        properties:
                          '@id':
                            const: xas:beamline
                  schema:name:
                    type: string
                required:
                - schema:additionalType
                - schema:name
          required:
          - schema:instrument
      - description: Must contain a prov:used entry whose schema:instrument is classified
          as an xas:xraymonochromator (via schema:additionalType) and has a schema:additionalProperty
          carrying the xas:dspacing PropertyValue with a schema:value.
        contains:
          type: object
          properties:
            schema:instrument:
              type: array
              contains:
                type: object
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
                  schema:additionalProperty:
                    type: array
                    contains:
                      type: object
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
                      required:
                      - schema:propertyID
                      - schema:value
                required:
                - schema:additionalType
                - schema:additionalProperty
          required:
          - schema:instrument
      x-jsonld-id: http://www.w3.org/ns/prov#used
    schema:additionalProperty:
      type: array
      description: Additional properties on the XAS analysis activity (base AdditionalProperty
        shape). The activity-level propertyID enum (xas:edgeenergy, calibration method,
        ...) is layered on in xasOptional so it applies at the profile level, not
        this shape.
      items:
        $ref: '#/$defs/AdditionalProperty'
      x-jsonld-id: http://schema.org/additionalProperty
    schema:location:
      $ref: '#/$defs/Facility'
      x-jsonld-id: http://schema.org/location
    schema:object:
      description: Sample being analyzed (per Ocean Info Hub recommendation)
      $ref: '#/$defs/Sample'
      x-jsonld-id: http://schema.org/object
$defs:
  Identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
  Sample:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasSample/schema.yaml
  AdditionalProperty:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
  Facility:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasFacility/schema.yaml
  Instrument:
    allOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasInstrument/schema.yaml
    - type: object
      description: As a prov:used entity, the instrument's @type includes prov:Entity
        (the PROV-O range of prov:used) alongside schema:Thing / schema:Product.
      properties:
        '@type':
          contains:
            const: prov:Entity
x-jsonld-prefixes:
  schema: http://schema.org/
  nxs: https://manual.nexusformat.org/classes/
  prov: http://www.w3.org/ns/prov#
  wd: https://www.wikidata.org/entity/
  xas: https://w3id.org/cdif/xas/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasGeneratedBy/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasGeneratedBy/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "wd": "https://www.wikidata.org/entity/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "xas": "cdif:xas/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasGeneratedBy/context.jsonld)

## Sources

* [schema.org](https://schema.org/Action)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/xasProperties/xasGeneratedBy`

