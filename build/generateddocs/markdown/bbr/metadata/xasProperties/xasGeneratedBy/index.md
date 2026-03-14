
# X-ray absorption, PROV wasGeneratedBy Activity (Schema)

`cdif.bbr.metadata.xasProperties.xasGeneratedBy` *v0.1*

Extends cdifProvActivity with XAS-specific provenance: dual-typed activity (schema:Event + xas:AnalysisEvent), XAS facility location, sample object, XAS instrument wrappers via prov:used, and XAS additional properties (edge_energy, calibration method, instrument configuration, installedOptions). Defines properties: @type, schema:startDate, prov:used, schema:additionalProperty, schema:location, schema:object. Uses building blocks: cdifProvActivity (cdifProperties), identifier (schemaorgProperties), xasSample (xasProperties), additionalProperty (schemaorgProperties), xasFacility (xasProperties), xasInstrument (xasProperties).

[*Status*](http://www.opengis.net/def/status): Under development

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
        "ex": "https://example.org/",
        "xas": "https://xas.org/dictionary/",
        "nxs": "http://purl.org/nexusformat/definitions/",
        "wd": "https://www.wikidata.org/entity/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@id": "ex:exampleGeneratedBy_w46j6j",
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
                "schema:additionalType": ["wd:Q3099911"],
                "schema:name": "x-ray absorption analysis system",
                "schema:hasPart": [
                    {
                        "@type": [
                            "schema:Thing",
                            "schema:Product"
                        ],
                        "schema:additionalType": ["nxs:BaseClass/NXsource", "wd:Q3099911"],
                        "schema:name": "APS bending magnet source",
                        "schema:identifier": "https://www.aps.anl.gov/Beamlines/Directory/source/13-BM",
                        "schema:additionalProperty": [
                            {
                                "@type": "schema:PropertyValue",
                                "schema:propertyID": ["nxs:Field/NXsource/type"],
                                "schema:name": "X-ray source",
                                "schema:value": "Synchrotron X-ray Source"
                            },
                            {
                                "@type": "schema:PropertyValue",
                                "schema:propertyID": ["nxs:Field/NXsource/probe"],
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
                        "schema:additionalType": ["wd:Q3099911", "xas:Beamline"],
                        "schema:name": "13-BM-D",
                        "schema:identifier": "https://www.aps.anl.gov/Beamlines/Directory/13-BM-D",
                        "schema:additionalProperty": [
                            {
                                "@type": "schema:PropertyValue",
                                "schema:propertyID": ["xas:collimation"],
                                "schema:name": "beamline collimation",
                                "schema:value": "none"
                            },
                            {
                                "@type": "schema:PropertyValue",
                                "schema:propertyID": ["xas:focusing"],
                                "schema:name": "focusing",
                                "schema:value": "unknown"
                            },
                            {
                                "@type": "schema:PropertyValue",
                                "schema:propertyID": ["xas:harmonic_rejection"],
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
                        "schema:additionalType": ["wd:Q3099911", "nxs:BaseClass/NXmonochromator"],
                        "schema:name": "Si 111",
                        "schema:additionalProperty": [
                            {
                                "@type": "schema:PropertyValue",
                                "schema:propertyID": ["nxs:Field/NXcrystal/d_spacing"],
                                "schema:name": "Monochromator d-spacing",
                                "schema:value": "3.13550",
                                "schema:unitText": "Angstrom"
                            },
                            {
                                "@type": "schema:PropertyValue",
                                "schema:propertyID": ["nxs:Field/NXcrystal/chemical_formula"],
                                "schema:name": "Monochromator chemical formula",
                                "schema:value": "Si"
                            },
                            {
                                "@type": "schema:PropertyValue",
                                "schema:propertyID": ["nxs:Field/NXcrystal/type"],
                                "schema:name": "Monochromator crystal type",
                                "schema:value": "crystal type"
                            },
                            {
                                "@type": "schema:PropertyValue",
                                "schema:propertyID": ["nxs:Field/NXcrystal/reflection"],
                                "schema:name": "Reflecting plane",
                                "schema:value": "1,1,1"
                            }
                        ]
                    },
                    {
                        "@type": [
                            "schema:Thing",
                            "schema:Product"
                        ],
                        "schema:additionalType": ["wd:Q3099911", "nxs:BaseClass/NXmonitor"],
                        "schema:name": "x-ray intensity monitor",
                        "schema:additionalProperty": [
                            {
                                "@type": "schema:PropertyValue",
                                "schema:propertyID": ["nxs:Field/NXmonitor/mode"],
                                "schema:name": "monitor mode",
                                "schema:value": "monitor"
                            },
                            {
                                "@type": "schema:PropertyValue",
                                "schema:propertyID": ["nxs:Field/NXmonitor/preset"],
                                "schema:name": "monitor preset",
                                "schema:value": "N.A."
                            },
                            {
                                "@type": "schema:PropertyValue",
                                "schema:propertyID": ["xas:detector.i0"],
                                "schema:name": "detector mode i0",
                                "schema:alternateName": "incident flux measurement method",
                                "schema:value": "10cm  N2"
                            },
                            {
                                "@type": "schema:PropertyValue",
                                "schema:propertyID": ["xas:detector.it"],
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
            "@type": "schema:PropertyValue",
            "schema:propertyID": ["xas:pressure"],
            "schema:description": "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential",
            "schema:value": "3567",
            "schema:name": "Environment Pressure",
            "schema:unitText": "KPa"
        },
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": ["xas:edge_energy"],
            "schema:value": "12658.0",
            "schema:name": "Edge energy",
            "schema:unitText": "eV"
        },
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": ["nxs:Group/NXdetector/calibration_method"],
            "schema:name": "calibration method",
            "schema:value": "description of calibration procedure",
            "schema:url": "http://protocols.io/link/to/calibrationMethod"
        },
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": ["nxs:Group/NXentry/experiment_documentation"],
            "schema:name": "Instrument configuration",
            "schema:value": "description of instrument configuration",
            "schema:url": "http://protocols.io/link/to/calibrationMethod"
        },
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": ["xas:installedOptions"],
            "schema:name": "Installed Options",
            "schema:value": "Description of extra equipment installed on the base instrument(?)"
        }
    ],
    "schema:location": {
        "@id": "ex:xasfacility_37yht",
        "@type": "schema:Place",
        "schema:additionalType": ["xas:Facility"],
        "schema:identifier": "https://ror.org/aps",
        "schema:name": "APS",
        "schema:additionalProperty": [
            {
                "@type": "schema:PropertyValue",
                "schema:propertyID": ["xas:energy"],
                "schema:name": "Facility energy",
                "schema:value": "7.00",
                "schema:unitText": "GeV"
            },
            {
                "@type": "schema:PropertyValue",
                "schema:propertyID": ["xas:current"],
                "schema:name": "Facility current",
                "schema:value": "120",
                "schema:unitText": "Amps"
            },
            {
                "@type": "schema:PropertyValue",
                "schema:propertyID": ["xas:xray_source"],
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
                "@type": "schema:PropertyValue",
                "schema:propertyID": ["xas:porosity"],
                "schema:name": "Porosity",
                "schema:value": "27",
                "schema:unitText": "percent"
            },
            {
                "@type": "schema:PropertyValue",
                "schema:propertyID": ["xas:stoichiometry"],
                "schema:name": "Stoichiometry",
                "schema:value": "Na2SeO4"
            },
            {
                "@type": "schema:PropertyValue",
                "schema:propertyID": ["xas:samplePreparation"],
                "schema:name": "Sample preparation",
                "schema:value": "powder on tape, 6 layers"
            },
            {
                "@type": "schema:PropertyValue",
                "schema:propertyID": ["nxs:Field/NXsample/mass"],
                "schema:name": "Sample mass",
                "schema:value": "10",
                "schema:unitText": "mg"
            },
            {
                "@type": "schema:PropertyValue",
                "schema:propertyID": ["nxs:Field/NXsample/point_group"],
                "schema:name": "Point group",
                "schema:value": "mm2"
            },
            {
                "@type": "schema:PropertyValue",
                "schema:propertyID": ["nxs:Field/NXsample/unit_cell"],
                "schema:name": "Unit cell",
                "schema:value": "cubic; Z = 4; a = 5.46; V = 162.77"
            },
            {
                "@type": "schema:PropertyValue",
                "schema:propertyID": ["xas:parentSample"],
                "schema:name": "Parent sample",
                "schema:value": "igsn:10.3476/342573"
            },
            {
                "@type": "schema:PropertyValue",
                "schema:propertyID": ["xas:materialState"],
                "schema:name": "Material state",
                "schema:value": "solid metal foil"
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
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasGeneratedBy/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xas": "https://xas.org/dictionary/",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "wd": "https://www.wikidata.org/entity/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@id": "ex:exampleGeneratedBy_w46j6j",
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
        "schema:additionalType": [
          "wd:Q3099911"
        ],
        "schema:name": "x-ray absorption analysis system",
        "schema:hasPart": [
          {
            "@type": [
              "schema:Thing",
              "schema:Product"
            ],
            "schema:additionalType": [
              "nxs:BaseClass/NXsource",
              "wd:Q3099911"
            ],
            "schema:name": "APS bending magnet source",
            "schema:identifier": "https://www.aps.anl.gov/Beamlines/Directory/source/13-BM",
            "schema:additionalProperty": [
              {
                "@type": "schema:PropertyValue",
                "schema:propertyID": [
                  "nxs:Field/NXsource/type"
                ],
                "schema:name": "X-ray source",
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
            "schema:additionalType": [
              "wd:Q3099911",
              "xas:Beamline"
            ],
            "schema:name": "13-BM-D",
            "schema:identifier": "https://www.aps.anl.gov/Beamlines/Directory/13-BM-D",
            "schema:additionalProperty": [
              {
                "@type": "schema:PropertyValue",
                "schema:propertyID": [
                  "xas:collimation"
                ],
                "schema:name": "beamline collimation",
                "schema:value": "none"
              },
              {
                "@type": "schema:PropertyValue",
                "schema:propertyID": [
                  "xas:focusing"
                ],
                "schema:name": "focusing",
                "schema:value": "unknown"
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
            "schema:additionalType": [
              "wd:Q3099911",
              "nxs:BaseClass/NXmonochromator"
            ],
            "schema:name": "Si 111",
            "schema:additionalProperty": [
              {
                "@type": "schema:PropertyValue",
                "schema:propertyID": [
                  "nxs:Field/NXcrystal/d_spacing"
                ],
                "schema:name": "Monochromator d-spacing",
                "schema:value": "3.13550",
                "schema:unitText": "Angstrom"
              },
              {
                "@type": "schema:PropertyValue",
                "schema:propertyID": [
                  "nxs:Field/NXcrystal/chemical_formula"
                ],
                "schema:name": "Monochromator chemical formula",
                "schema:value": "Si"
              },
              {
                "@type": "schema:PropertyValue",
                "schema:propertyID": [
                  "nxs:Field/NXcrystal/type"
                ],
                "schema:name": "Monochromator crystal type",
                "schema:value": "crystal type"
              },
              {
                "@type": "schema:PropertyValue",
                "schema:propertyID": [
                  "nxs:Field/NXcrystal/reflection"
                ],
                "schema:name": "Reflecting plane",
                "schema:value": "1,1,1"
              }
            ]
          },
          {
            "@type": [
              "schema:Thing",
              "schema:Product"
            ],
            "schema:additionalType": [
              "wd:Q3099911",
              "nxs:BaseClass/NXmonitor"
            ],
            "schema:name": "x-ray intensity monitor",
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
                "schema:alternateName": "incident flux measurement method",
                "schema:value": "10cm  N2"
              },
              {
                "@type": "schema:PropertyValue",
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
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "xas:pressure"
      ],
      "schema:description": "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential",
      "schema:value": "3567",
      "schema:name": "Environment Pressure",
      "schema:unitText": "KPa"
    },
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "xas:edge_energy"
      ],
      "schema:value": "12658.0",
      "schema:name": "Edge energy",
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
        "@type": "schema:PropertyValue",
        "schema:propertyID": [
          "xas:porosity"
        ],
        "schema:name": "Porosity",
        "schema:value": "27",
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
        "schema:name": "Sample preparation",
        "schema:value": "powder on tape, 6 layers"
      },
      {
        "@type": "schema:PropertyValue",
        "schema:propertyID": [
          "nxs:Field/NXsample/mass"
        ],
        "schema:name": "Sample mass",
        "schema:value": "10",
        "schema:unitText": "mg"
      },
      {
        "@type": "schema:PropertyValue",
        "schema:propertyID": [
          "nxs:Field/NXsample/point_group"
        ],
        "schema:name": "Point group",
        "schema:value": "mm2"
      },
      {
        "@type": "schema:PropertyValue",
        "schema:propertyID": [
          "nxs:Field/NXsample/unit_cell"
        ],
        "schema:name": "Unit cell",
        "schema:value": "cubic; Z = 4; a = 5.46; V = 162.77"
      },
      {
        "@type": "schema:PropertyValue",
        "schema:propertyID": [
          "xas:parentSample"
        ],
        "schema:name": "Parent sample",
        "schema:value": "igsn:10.3476/342573"
      },
      {
        "@type": "schema:PropertyValue",
        "schema:propertyID": [
          "xas:materialState"
        ],
        "schema:name": "Material state",
        "schema:value": "solid metal foil"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xas: <https://xas.org/dictionary/> .

ex:exampleGeneratedBy_w46j6j a schema1:Action,
        prov:Activity,
        xas:AnalysisEvent ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Installed Options" ;
            schema1:propertyID "xas:installedOptions" ;
            schema1:value "Description of extra equipment installed on the base instrument(?)" ],
        [ a schema1:PropertyValue ;
            schema1:name "Edge energy" ;
            schema1:propertyID "xas:edge_energy" ;
            schema1:unitText "eV" ;
            schema1:value "12658.0" ],
        [ a schema1:PropertyValue ;
            schema1:name "Instrument configuration" ;
            schema1:propertyID "nxs:Group/NXentry/experiment_documentation" ;
            schema1:url "http://protocols.io/link/to/calibrationMethod" ;
            schema1:value "description of instrument configuration" ],
        [ a schema1:PropertyValue ;
            schema1:description "extrinsic properties of measurement environment--temperature, pressure, e-field, mag-field.  have to check magnetic_moment, electrochemical_potential" ;
            schema1:name "Environment Pressure" ;
            schema1:propertyID "xas:pressure" ;
            schema1:unitText "KPa" ;
            schema1:value "3567" ],
        [ a schema1:PropertyValue ;
            schema1:name "calibration method" ;
            schema1:propertyID "nxs:Group/NXdetector/calibration_method" ;
            schema1:url "http://protocols.io/link/to/calibrationMethod" ;
            schema1:value "description of calibration procedure" ] ;
    schema1:identifier "20241111_DSC_NU_OREX-803224-0_1" ;
    schema1:location ex:xasfacility_37yht ;
    schema1:object [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty [ a schema1:PropertyValue ;
                    schema1:name "Material state" ;
                    schema1:propertyID "xas:materialState" ;
                    schema1:value "solid metal foil" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Porosity" ;
                    schema1:propertyID "xas:porosity" ;
                    schema1:unitText "percent" ;
                    schema1:value "27" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Sample mass" ;
                    schema1:propertyID "nxs:Field/NXsample/mass" ;
                    schema1:unitText "mg" ;
                    schema1:value "10" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Unit cell" ;
                    schema1:propertyID "nxs:Field/NXsample/unit_cell" ;
                    schema1:value "cubic; Z = 4; a = 5.46; V = 162.77" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Sample preparation" ;
                    schema1:propertyID "xas:samplePreparation" ;
                    schema1:value "powder on tape, 6 layers" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Parent sample" ;
                    schema1:propertyID "xas:parentSample" ;
                    schema1:value "igsn:10.3476/342573" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Stoichiometry" ;
                    schema1:propertyID "xas:stoichiometry" ;
                    schema1:value "Na2SeO4" ],
                [ a schema1:PropertyValue ;
                    schema1:name "Point group" ;
                    schema1:propertyID "nxs:Field/NXsample/point_group" ;
                    schema1:value "mm2" ] ;
            schema1:additionalType "MaterialSample",
                "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample" ;
            schema1:description "physical properties of sample: ph, eh, volume, porosity, density, concentration, resistivity, viscosity, crystal structure, opacity from xdi list..." ;
            schema1:identifier "igsn:10.6620/357lkj" ;
            schema1:name "Na2SeO4" ] ;
    schema1:startDate "2008-04-10T21:58:50" ;
    prov:used [ schema1:instrument [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "wd:Q3099911" ;
                    schema1:hasPart [ a schema1:Product,
                                schema1:Thing ;
                            schema1:additionalProperty [ a schema1:PropertyValue ;
                                    schema1:name "beamline collimation" ;
                                    schema1:propertyID "xas:collimation" ;
                                    schema1:value "none" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "harmonic_rejection" ;
                                    schema1:propertyID "xas:harmonic_rejection" ;
                                    schema1:value "Rh-coated mirror, detuned" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "focusing" ;
                                    schema1:propertyID "xas:focusing" ;
                                    schema1:value "unknown" ] ;
                            schema1:additionalType "wd:Q3099911",
                                "xas:Beamline" ;
                            schema1:identifier "https://www.aps.anl.gov/Beamlines/Directory/13-BM-D" ;
                            schema1:name "13-BM-D" ],
                        [ a schema1:Product,
                                schema1:Thing ;
                            schema1:additionalProperty [ a schema1:PropertyValue ;
                                    schema1:name "Probe" ;
                                    schema1:propertyID "nxs:Field/NXsource/probe" ;
                                    schema1:value "x-ray" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "X-ray source" ;
                                    schema1:propertyID "nxs:Field/NXsource/type" ;
                                    schema1:value "Synchrotron X-ray Source" ] ;
                            schema1:additionalType "nxs:BaseClass/NXsource",
                                "wd:Q3099911" ;
                            schema1:identifier "https://www.aps.anl.gov/Beamlines/Directory/source/13-BM" ;
                            schema1:name "APS bending magnet source" ],
                        [ a schema1:Product,
                                schema1:Thing ;
                            schema1:additionalProperty [ a schema1:PropertyValue ;
                                    schema1:name "Reflecting plane" ;
                                    schema1:propertyID "nxs:Field/NXcrystal/reflection" ;
                                    schema1:value "1,1,1" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "Monochromator crystal type" ;
                                    schema1:propertyID "nxs:Field/NXcrystal/type" ;
                                    schema1:value "crystal type" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "Monochromator d-spacing" ;
                                    schema1:propertyID "nxs:Field/NXcrystal/d_spacing" ;
                                    schema1:unitText "Angstrom" ;
                                    schema1:value "3.13550" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "Monochromator chemical formula" ;
                                    schema1:propertyID "nxs:Field/NXcrystal/chemical_formula" ;
                                    schema1:value "Si" ] ;
                            schema1:additionalType "nxs:BaseClass/NXmonochromator",
                                "wd:Q3099911" ;
                            schema1:name "Si 111" ],
                        [ a schema1:Product,
                                schema1:Thing ;
                            schema1:additionalProperty [ a schema1:PropertyValue ;
                                    schema1:alternateName "incident flux measurement method" ;
                                    schema1:name "detector mode i0" ;
                                    schema1:propertyID "xas:detector.i0" ;
                                    schema1:value "10cm  N2" ],
                                [ a schema1:PropertyValue ;
                                    schema1:alternateName "transmitted flux measurement method" ;
                                    schema1:name "detector mode it" ;
                                    schema1:propertyID "xas:detector.it" ;
                                    schema1:value "10cm  N2" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "monitor mode" ;
                                    schema1:propertyID "nxs:Field/NXmonitor/mode" ;
                                    schema1:value "monitor" ],
                                [ a schema1:PropertyValue ;
                                    schema1:name "monitor preset" ;
                                    schema1:propertyID "nxs:Field/NXmonitor/preset" ;
                                    schema1:value "N.A." ] ;
                            schema1:additionalType "nxs:BaseClass/NXmonitor",
                                "wd:Q3099911" ;
                            schema1:name "x-ray intensity monitor" ] ;
                    schema1:name "x-ray absorption analysis system" ] ] .

ex:xasfacility_37yht a schema1:Place ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Facility energy" ;
            schema1:propertyID "xas:energy" ;
            schema1:unitText "GeV" ;
            schema1:value "7.00" ],
        [ a schema1:PropertyValue ;
            schema1:name "X-ray Source" ;
            schema1:propertyID "xas:xray_source" ;
            schema1:value "APS bending magnet" ],
        [ a schema1:PropertyValue ;
            schema1:name "Facility current" ;
            schema1:propertyID "xas:current" ;
            schema1:unitText "Amps" ;
            schema1:value "120" ] ;
    schema1:additionalType "xas:Facility" ;
    schema1:identifier "https://ror.org/aps" ;
    schema1:name "APS" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: XAS Analysis Event activity
description: XAS-specific provenance activity building block. Extends cdifProvActivity
  with XAS analysis event typing (xas:AnalysisEvent), XAS facility location, sample
  object, XAS-specific instrument type, and XAS additional properties (edge_energy,
  calibration method, instrument configuration, installedOptions).
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvActivity/schema.yaml
- type: object
  properties:
    '@type':
      type: array
      items:
        type: string
      contains:
        const: xas:AnalysisEvent
    schema:startDate:
      type: string
      description: Date/time the XAS analysis started
    prov:used:
      type: array
      items:
        anyOf:
        - type: object
          required:
          - schema:instrument
          properties:
            schema:instrument:
              $ref: '#/$defs/Instrument'
        - type: string
        - type: object
          properties:
            '@id':
              type: string
    schema:additionalProperty:
      type: array
      description: XAS-specific additional properties for the analysis activity
      items:
        allOf:
        - $ref: '#/$defs/AdditionalProperty'
        - properties:
            schema:propertyID:
              type: array
              minItems: 1
              items:
                anyOf:
                - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml#/$defs/propertyID_item
                - enum:
                  - xas:edge_energy
                  - calibration method
                  - Instrument configuration
                  - xas:installedOptions
    schema:location:
      $ref: '#/$defs/Facility'
    schema:object:
      description: Sample being analyzed (per Ocean Info Hub recommendation)
      $ref: '#/$defs/Sample'
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
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasInstrument/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasGeneratedBy/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasGeneratedBy/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org",
    "prov": "http://www.w3.org/ns/prov#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "xas": "https://xas.org/dictionary/",
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

