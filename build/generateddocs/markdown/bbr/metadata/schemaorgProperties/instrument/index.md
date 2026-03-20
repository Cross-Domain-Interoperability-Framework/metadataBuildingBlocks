
# Instrument Description (Schema)

`cdif.bbr.metadata.schemaorgProperties.instrument` *v0.2*

Schema for describing laboratory instruments and instrument systems. Supports ownership (schema:contributor with roles), manufacturer, model, commissioning dates, instrument type classification, hierarchical sub-components via schema:hasPart, domain-specific properties, and related links. Uses building blocks: identifier, organization, person, definedTerm, agentInRole, additionalProperty, labeledLink (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Instrument Description

Schema for describing laboratory instruments and instrument systems. Combines instrument identity, ownership, manufacturer/model, commissioning lifecycle, hierarchical sub-components, and domain-specific properties.

### Defined properties

- **@context** - JSON-LD context (requires schema prefix)
- **@id** - persistent identifier URI for this instrument record
- **@type** - must include schema:Product and schema:Thing
- **schema:additionalType** - domain-specific type classifications (e.g. wd:Q3099911 for scientific instrument)
- **schema:name** - human-readable name (min 3 characters)
- **schema:description** - text description of purpose and capabilities
- **schema:alternateName** - alternate names (make/model, abbreviation)
- **schema:identifier** - formal identifiers (PIDINST, serial number, inventory number)
- **schema:url** - landing page URL
- **schema:manufacturer** - organization that manufactured the instrument
- **schema:model** - product model (name, identifier)
- **schema:category** - instrument type from controlled vocabulary
- **schema:owner** - organization that owns the instrument
- **schema:contributor** - agents in roles (operator, custodian, PI — use schema:owner for ownership)
- **schema:additionalProperty** - instrument-specific properties (measured variables, detection limits, calibration, etc.)
- **schema:validFrom** / **schema:validThrough** - commissioned/decommissioned dates
- **schema:hasPart** - sub-components of the instrument system
- **schema:relatedLink** - links to manuals, datasheets, calibration records
- **schema:subjectOf** - catalog record metadata

### Dependencies

- [identifier](../identifier/) - structured identifier pattern
- [organization](../organization/) - organization schema
- [person](../person/) - person schema
- [definedTerm](../definedTerm/) - controlled vocabulary term
- [agentInRole](../agentInRole/) - agent with qualified role
- [additionalProperty](../additionalProperty/) - PropertyValue for extension properties
- [labeledLink](../labeledLink/) - typed link to related resource

## Examples

### Example Py-GC-MS/MS instrument system with sub-components.
NASA GSFC Astrobiology Analytical Lab Pyrolysis-GC-MS/MS system
demonstrating the full instrument description building block:
schema:Product + schema:Thing typing, manufacturer (Thermo Fisher),
model (TSQ 9000), category (NERC vocab), contributors with roles
(owner, PI, operator), additionalProperty (measured variables,
detection limits), validFrom (commissioned date), hasPart
sub-components (pyrolysis oven, gas chromatograph, mass spectrometer
each with their own manufacturer/model/properties), relatedLink
(manual, publication, calibration record), and subjectOf catalog record.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "spdx": "http://spdx.org/rdf/terms#",
    "wd": "https://www.wikidata.org/entity/",
    "ex": "https://example.org/"
  },
  "@id": "ex:instrument-pygcmsms-gsfc-001",
  "@type": [
    "schema:Product",
    "schema:Thing"
  ],
  "schema:additionalType": [
    "wd:Q3099911",
    "wd:Q420427"
  ],
  "schema:name": "Pyrolysis-GC-MS/MS System (NASA GSFC Astrobiology Analytical Lab)",
  "schema:description": "Integrated pyrolysis-gas chromatography-tandem mass spectrometry instrument system used for characterization of complex organic mixtures in bulk solid samples. Combines a flash pyrolysis front-end (up to 1300°C at 10°C/ms) with gas chromatographic separation and triple-quadrupole mass spectrometry with simultaneous full scan and timed SRM/MRM acquisition. Primary application: direct microanalysis of extraterrestrial materials without chemical pretreatment.",
  "schema:alternateName": [
    "Py-GC-MS/MS",
    "GSFC Astrobiology Lab Pyrolysis GC-MS System"
  ],
  "schema:identifier": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://doi.org",
      "schema:value": "10.xxxx/instrument.pygcms.gsfc.001",
      "schema:url": "https://doi.org/10.xxxx/instrument.pygcms.gsfc.001"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "inventoryNumber",
      "schema:value": "GSFC-AAL-PYGCMS-001"
    }
  ],
  "schema:url": "https://science.gsfc.nasa.gov/sed/bio/jason.p.dworkin",
  "schema:manufacturer": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Thermo Fisher Scientific",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://ror.org",
      "schema:value": "03x1z2w73",
      "schema:url": "https://ror.org/03x1z2w73"
    },
    "schema:contactPoint": {
      "@type": [
        "schema:ContactPoint"
      ],
      "schema:email": "info@thermofisher.com",
      "schema:url": "https://www.thermofisher.com/contact-us.html"
    }
  },
  "schema:model": {
    "@type": [
      "schema:ProductModel"
    ],
    "schema:name": "TSQ 9000 Triple Quadrupole GC-MS/MS",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "serialNumber",
      "schema:value": "TSQ96CI2301004"
    }
  },
  "schema:category": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Gas Chromatography Mass Spectrometry",
      "schema:termCode": "GCMS",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://vocab.nerc.ac.uk/collection/L05/current/",
        "schema:value": "LAB02",
        "schema:url": "https://vocab.nerc.ac.uk/collection/L05/current/LAB02/"
      },
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Pyrolysis Gas Chromatography Mass Spectrometry",
      "schema:termCode": "Py-GC-MS",
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/"
    }
  ],
  "schema:owner": {
    "@id": "https://ror.org/0171mag52",
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "NASA Goddard Space Flight Center",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://ror.org",
      "schema:value": "0171mag52",
      "schema:url": "https://ror.org/0171mag52"
    },
    "schema:contactPoint": {
      "@type": [
        "schema:ContactPoint"
      ],
      "schema:email": "gsfc-aal@nasa.gov"
    }
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Principal Investigator",
        "schema:inDefinedTermSet": "https://credit.niso.org/",
        "schema:termCode": "investigation"
      },
      "schema:contributor": {
        "@id": "https://orcid.org/0000-0002-4805-7062",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Dworkin, Jason P.",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://orcid.org",
          "schema:value": "0000-0002-4805-7062",
          "schema:url": "https://orcid.org/0000-0002-4805-7062"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "jason.p.dworkin@nasa.gov"
        }
      }
    },
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "Operator",
      "schema:contributor": {
        "@id": "https://orcid.org/0000-0001-8898-3457",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Mojarro, Angel",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://orcid.org",
          "schema:value": "0000-0001-8898-3457",
          "schema:url": "https://orcid.org/0000-0001-8898-3457"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "angel.mojarro@nasa.gov"
        }
      }
    }
  ],
  "schema:additionalProperty": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "MeasuredVariable"
      ],
      "schema:name": "Measured variables",
      "schema:value": "mass-to-charge ratio (m/z); ion abundance; retention time"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "detectionLimit"
      ],
      "schema:name": "Full scan detection limit",
      "schema:value": "sub-nanogram",
      "schema:unitText": "ng"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "scanRange"
      ],
      "schema:name": "Full scan m/z range",
      "schema:value": "50-500"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "mrmCapability"
      ],
      "schema:name": "MRM target compounds",
      "schema:value": 38
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "ionizationMode"
      ],
      "schema:name": "Ionization mode",
      "schema:value": "Electron Ionization (EI), positive polarity"
    }
  ],
  "schema:validFrom": "2023-01-15",
  "schema:hasPart": [
    {
      "@type": [
        "schema:Thing",
        "schema:Product"
      ],
      "@id": "ex:component-pyrolysis-oven",
      "schema:name": "Pyrolysis Oven",
      "schema:description": "Flash pyrolysis front-end interface coupled to GC-MS. Flash heats at 10°C/ms to temperatures up to 1300°C. Samples loaded in quartz tubes.",
      "schema:additionalType": "wd:Q3099911",
      "schema:manufacturer": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "CDS Analytical"
      },
      "schema:model": {
        "@type": [
          "schema:ProductModel"
        ],
        "schema:name": "Pyroprobe 6150"
      },
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "maxTemperature"
          ],
          "schema:name": "Maximum temperature",
          "schema:value": 1300,
          "schema:unitText": "°C"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "heatingRate"
          ],
          "schema:name": "Maximum heating rate",
          "schema:value": 10,
          "schema:unitText": "°C/ms"
        }
      ]
    },
    {
      "@type": [
        "schema:Thing",
        "schema:Product"
      ],
      "@id": "ex:component-gas-chromatograph",
      "schema:name": "Gas Chromatograph with Rtx-5ms column",
      "schema:description": "GC with Rtx-5ms (5% diphenyl / 95% dimethyl polysiloxane) fused silica capillary column, 30 m × 0.250 mm × 0.50 µm, with 5 m × 0.250 mm guard column. Helium carrier gas at 1.500 mL/min.",
      "schema:additionalType": "wd:Q848143",
      "schema:manufacturer": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "Thermo Fisher Scientific"
      },
      "schema:model": {
        "@type": [
          "schema:ProductModel"
        ],
        "schema:name": "TRACE 1310"
      },
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "columnType"
          ],
          "schema:name": "Column",
          "schema:value": "Rtx-5ms, 30 m × 0.250 mm × 0.50 µm + 5 m guard"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "carrierGas"
          ],
          "schema:name": "Carrier gas",
          "schema:value": "Helium"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "carrierGasFlow"
          ],
          "schema:name": "Carrier gas flow rate",
          "schema:value": 1.5,
          "schema:unitText": "mL/min"
        }
      ]
    },
    {
      "@type": [
        "schema:Thing",
        "schema:Product"
      ],
      "@id": "ex:component-mass-spectrometer",
      "schema:name": "Thermo Scientific TSQ Triple-Quadrupole Mass Spectrometer",
      "schema:description": "TSQ triple-quadrupole MS operated in EI mode, positive polarity, with simultaneous full scan (m/z 50-500) and timed SRM/MRM capability targeting 38 organic compounds.",
      "schema:additionalType": "wd:Q180809",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "serialNumber",
        "schema:value": "TSQ96CI2301004"
      },
      "schema:manufacturer": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "Thermo Fisher Scientific"
      },
      "schema:model": {
        "@type": [
          "schema:ProductModel"
        ],
        "schema:name": "TSQ 9000"
      },
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "detectorGain"
          ],
          "schema:name": "Detector gain",
          "schema:value": 100000
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "scanTime"
          ],
          "schema:name": "Full scan time",
          "schema:value": 0.1,
          "schema:unitText": "s"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "ionSourceTemperature"
          ],
          "schema:name": "Ion source temperature",
          "schema:value": 300,
          "schema:unitText": "°C"
        }
      ]
    }
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "TSQ 9000 User Guide",
      "schema:url": "https://www.thermofisher.com/document-connect/document-connect.html?url=https://assets.thermofisher.com/TFS-Assets/CMD/manuals/man-80000-97071-tsq-9000-user-guide.pdf",
      "schema:description": "User manual for the TSQ 9000 triple quadrupole GC-MS/MS system"
    },
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Dworkin et al. (2024) — Organic compounds in asteroid Bennu samples",
      "schema:url": "https://doi.org/10.1038/s41586-024-08335-1"
    },
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "2023 annual calibration report",
      "schema:url": "https://example.org/calibration/pygcms-gsfc-2023.pdf"
    }
  ],
  "schema:subjectOf": {
    "@id": "ex:metadata-instrument-pygcms-001",
    "@type": [
      "schema:DigitalDocument"
    ],
    "schema:dateModified": "2026-03-15",
    "schema:about": {
      "@id": "ex:instrument-pygcmsms-gsfc-001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/instrumentDescription/v0.1"
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
      "dcterms": "http://purl.org/dc/terms/",
      "wd": "https://www.wikidata.org/entity/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "spdx": "http://spdx.org/rdf/terms#",
      "wd": "https://www.wikidata.org/entity/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:instrument-pygcmsms-gsfc-001",
  "@type": [
    "schema:Product",
    "schema:Thing"
  ],
  "schema:additionalType": [
    "wd:Q3099911",
    "wd:Q420427"
  ],
  "schema:name": "Pyrolysis-GC-MS/MS System (NASA GSFC Astrobiology Analytical Lab)",
  "schema:description": "Integrated pyrolysis-gas chromatography-tandem mass spectrometry instrument system used for characterization of complex organic mixtures in bulk solid samples. Combines a flash pyrolysis front-end (up to 1300\u00b0C at 10\u00b0C/ms) with gas chromatographic separation and triple-quadrupole mass spectrometry with simultaneous full scan and timed SRM/MRM acquisition. Primary application: direct microanalysis of extraterrestrial materials without chemical pretreatment.",
  "schema:alternateName": [
    "Py-GC-MS/MS",
    "GSFC Astrobiology Lab Pyrolysis GC-MS System"
  ],
  "schema:identifier": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://doi.org",
      "schema:value": "10.xxxx/instrument.pygcms.gsfc.001",
      "schema:url": "https://doi.org/10.xxxx/instrument.pygcms.gsfc.001"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "inventoryNumber",
      "schema:value": "GSFC-AAL-PYGCMS-001"
    }
  ],
  "schema:url": "https://science.gsfc.nasa.gov/sed/bio/jason.p.dworkin",
  "schema:manufacturer": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Thermo Fisher Scientific",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://ror.org",
      "schema:value": "03x1z2w73",
      "schema:url": "https://ror.org/03x1z2w73"
    },
    "schema:contactPoint": {
      "@type": [
        "schema:ContactPoint"
      ],
      "schema:email": "info@thermofisher.com",
      "schema:url": "https://www.thermofisher.com/contact-us.html"
    }
  },
  "schema:model": {
    "@type": [
      "schema:ProductModel"
    ],
    "schema:name": "TSQ 9000 Triple Quadrupole GC-MS/MS",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "serialNumber",
      "schema:value": "TSQ96CI2301004"
    }
  },
  "schema:category": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Gas Chromatography Mass Spectrometry",
      "schema:termCode": "GCMS",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://vocab.nerc.ac.uk/collection/L05/current/",
        "schema:value": "LAB02",
        "schema:url": "https://vocab.nerc.ac.uk/collection/L05/current/LAB02/"
      },
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Pyrolysis Gas Chromatography Mass Spectrometry",
      "schema:termCode": "Py-GC-MS",
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/"
    }
  ],
  "schema:owner": {
    "@id": "https://ror.org/0171mag52",
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "NASA Goddard Space Flight Center",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://ror.org",
      "schema:value": "0171mag52",
      "schema:url": "https://ror.org/0171mag52"
    },
    "schema:contactPoint": {
      "@type": [
        "schema:ContactPoint"
      ],
      "schema:email": "gsfc-aal@nasa.gov"
    }
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Principal Investigator",
        "schema:inDefinedTermSet": "https://credit.niso.org/",
        "schema:termCode": "investigation"
      },
      "schema:contributor": {
        "@id": "https://orcid.org/0000-0002-4805-7062",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Dworkin, Jason P.",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://orcid.org",
          "schema:value": "0000-0002-4805-7062",
          "schema:url": "https://orcid.org/0000-0002-4805-7062"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "jason.p.dworkin@nasa.gov"
        }
      }
    },
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "Operator",
      "schema:contributor": {
        "@id": "https://orcid.org/0000-0001-8898-3457",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Mojarro, Angel",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://orcid.org",
          "schema:value": "0000-0001-8898-3457",
          "schema:url": "https://orcid.org/0000-0001-8898-3457"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "angel.mojarro@nasa.gov"
        }
      }
    }
  ],
  "schema:additionalProperty": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "MeasuredVariable"
      ],
      "schema:name": "Measured variables",
      "schema:value": "mass-to-charge ratio (m/z); ion abundance; retention time"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "detectionLimit"
      ],
      "schema:name": "Full scan detection limit",
      "schema:value": "sub-nanogram",
      "schema:unitText": "ng"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "scanRange"
      ],
      "schema:name": "Full scan m/z range",
      "schema:value": "50-500"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "mrmCapability"
      ],
      "schema:name": "MRM target compounds",
      "schema:value": 38
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        "ionizationMode"
      ],
      "schema:name": "Ionization mode",
      "schema:value": "Electron Ionization (EI), positive polarity"
    }
  ],
  "schema:validFrom": "2023-01-15",
  "schema:hasPart": [
    {
      "@type": [
        "schema:Thing",
        "schema:Product"
      ],
      "@id": "ex:component-pyrolysis-oven",
      "schema:name": "Pyrolysis Oven",
      "schema:description": "Flash pyrolysis front-end interface coupled to GC-MS. Flash heats at 10\u00b0C/ms to temperatures up to 1300\u00b0C. Samples loaded in quartz tubes.",
      "schema:additionalType": "wd:Q3099911",
      "schema:manufacturer": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "CDS Analytical"
      },
      "schema:model": {
        "@type": [
          "schema:ProductModel"
        ],
        "schema:name": "Pyroprobe 6150"
      },
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "maxTemperature"
          ],
          "schema:name": "Maximum temperature",
          "schema:value": 1300,
          "schema:unitText": "\u00b0C"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "heatingRate"
          ],
          "schema:name": "Maximum heating rate",
          "schema:value": 10,
          "schema:unitText": "\u00b0C/ms"
        }
      ]
    },
    {
      "@type": [
        "schema:Thing",
        "schema:Product"
      ],
      "@id": "ex:component-gas-chromatograph",
      "schema:name": "Gas Chromatograph with Rtx-5ms column",
      "schema:description": "GC with Rtx-5ms (5% diphenyl / 95% dimethyl polysiloxane) fused silica capillary column, 30 m \u00d7 0.250 mm \u00d7 0.50 \u00b5m, with 5 m \u00d7 0.250 mm guard column. Helium carrier gas at 1.500 mL/min.",
      "schema:additionalType": "wd:Q848143",
      "schema:manufacturer": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "Thermo Fisher Scientific"
      },
      "schema:model": {
        "@type": [
          "schema:ProductModel"
        ],
        "schema:name": "TRACE 1310"
      },
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "columnType"
          ],
          "schema:name": "Column",
          "schema:value": "Rtx-5ms, 30 m \u00d7 0.250 mm \u00d7 0.50 \u00b5m + 5 m guard"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "carrierGas"
          ],
          "schema:name": "Carrier gas",
          "schema:value": "Helium"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "carrierGasFlow"
          ],
          "schema:name": "Carrier gas flow rate",
          "schema:value": 1.5,
          "schema:unitText": "mL/min"
        }
      ]
    },
    {
      "@type": [
        "schema:Thing",
        "schema:Product"
      ],
      "@id": "ex:component-mass-spectrometer",
      "schema:name": "Thermo Scientific TSQ Triple-Quadrupole Mass Spectrometer",
      "schema:description": "TSQ triple-quadrupole MS operated in EI mode, positive polarity, with simultaneous full scan (m/z 50-500) and timed SRM/MRM capability targeting 38 organic compounds.",
      "schema:additionalType": "wd:Q180809",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "serialNumber",
        "schema:value": "TSQ96CI2301004"
      },
      "schema:manufacturer": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "Thermo Fisher Scientific"
      },
      "schema:model": {
        "@type": [
          "schema:ProductModel"
        ],
        "schema:name": "TSQ 9000"
      },
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "detectorGain"
          ],
          "schema:name": "Detector gain",
          "schema:value": 100000
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "scanTime"
          ],
          "schema:name": "Full scan time",
          "schema:value": 0.1,
          "schema:unitText": "s"
        },
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "ionSourceTemperature"
          ],
          "schema:name": "Ion source temperature",
          "schema:value": 300,
          "schema:unitText": "\u00b0C"
        }
      ]
    }
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "TSQ 9000 User Guide",
      "schema:url": "https://www.thermofisher.com/document-connect/document-connect.html?url=https://assets.thermofisher.com/TFS-Assets/CMD/manuals/man-80000-97071-tsq-9000-user-guide.pdf",
      "schema:description": "User manual for the TSQ 9000 triple quadrupole GC-MS/MS system"
    },
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Dworkin et al. (2024) \u2014 Organic compounds in asteroid Bennu samples",
      "schema:url": "https://doi.org/10.1038/s41586-024-08335-1"
    },
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "2023 annual calibration report",
      "schema:url": "https://example.org/calibration/pygcms-gsfc-2023.pdf"
    }
  ],
  "schema:subjectOf": {
    "@id": "ex:metadata-instrument-pygcms-001",
    "@type": [
      "schema:DigitalDocument"
    ],
    "schema:dateModified": "2026-03-15",
    "schema:about": {
      "@id": "ex:instrument-pygcmsms-gsfc-001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/instrumentDescription/v0.1"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:component-gas-chromatograph a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Carrier gas" ;
            schema1:propertyID "carrierGas" ;
            schema1:value "Helium" ],
        [ a schema1:PropertyValue ;
            schema1:name "Carrier gas flow rate" ;
            schema1:propertyID "carrierGasFlow" ;
            schema1:unitText "mL/min" ;
            schema1:value 1.5e+00 ],
        [ a schema1:PropertyValue ;
            schema1:name "Column" ;
            schema1:propertyID "columnType" ;
            schema1:value "Rtx-5ms, 30 m × 0.250 mm × 0.50 µm + 5 m guard" ] ;
    schema1:additionalType "wd:Q848143" ;
    schema1:description "GC with Rtx-5ms (5% diphenyl / 95% dimethyl polysiloxane) fused silica capillary column, 30 m × 0.250 mm × 0.50 µm, with 5 m × 0.250 mm guard column. Helium carrier gas at 1.500 mL/min." ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "TRACE 1310" ] ;
    schema1:name "Gas Chromatograph with Rtx-5ms column" .

ex:component-mass-spectrometer a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Detector gain" ;
            schema1:propertyID "detectorGain" ;
            schema1:value 100000 ],
        [ a schema1:PropertyValue ;
            schema1:name "Full scan time" ;
            schema1:propertyID "scanTime" ;
            schema1:unitText "s" ;
            schema1:value 1e-01 ],
        [ a schema1:PropertyValue ;
            schema1:name "Ion source temperature" ;
            schema1:propertyID "ionSourceTemperature" ;
            schema1:unitText "°C" ;
            schema1:value 300 ] ;
    schema1:additionalType "wd:Q180809" ;
    schema1:description "TSQ triple-quadrupole MS operated in EI mode, positive polarity, with simultaneous full scan (m/z 50-500) and timed SRM/MRM capability targeting 38 organic compounds." ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "serialNumber" ;
            schema1:value "TSQ96CI2301004" ] ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "TSQ 9000" ] ;
    schema1:name "Thermo Scientific TSQ Triple-Quadrupole Mass Spectrometer" .

ex:component-pyrolysis-oven a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Maximum heating rate" ;
            schema1:propertyID "heatingRate" ;
            schema1:unitText "°C/ms" ;
            schema1:value 10 ],
        [ a schema1:PropertyValue ;
            schema1:name "Maximum temperature" ;
            schema1:propertyID "maxTemperature" ;
            schema1:unitText "°C" ;
            schema1:value 1300 ] ;
    schema1:additionalType "wd:Q3099911" ;
    schema1:description "Flash pyrolysis front-end interface coupled to GC-MS. Flash heats at 10°C/ms to temperatures up to 1300°C. Samples loaded in quartz tubes." ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "CDS Analytical" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Pyroprobe 6150" ] ;
    schema1:name "Pyrolysis Oven" .

ex:instrument-pygcmsms-gsfc-001 a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Full scan detection limit" ;
            schema1:propertyID "detectionLimit" ;
            schema1:unitText "ng" ;
            schema1:value "sub-nanogram" ],
        [ a schema1:PropertyValue ;
            schema1:name "MRM target compounds" ;
            schema1:propertyID "mrmCapability" ;
            schema1:value 38 ],
        [ a schema1:PropertyValue ;
            schema1:name "Ionization mode" ;
            schema1:propertyID "ionizationMode" ;
            schema1:value "Electron Ionization (EI), positive polarity" ],
        [ a schema1:PropertyValue ;
            schema1:name "Full scan m/z range" ;
            schema1:propertyID "scanRange" ;
            schema1:value "50-500" ],
        [ a schema1:PropertyValue ;
            schema1:name "Measured variables" ;
            schema1:propertyID "MeasuredVariable" ;
            schema1:value "mass-to-charge ratio (m/z); ion abundance; retention time" ] ;
    schema1:additionalType "wd:Q3099911",
        "wd:Q420427" ;
    schema1:alternateName "GSFC Astrobiology Lab Pyrolysis GC-MS System",
        "Py-GC-MS/MS" ;
    schema1:category [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.nerc.ac.uk/collection/L05/current/" ;
            schema1:name "Pyrolysis Gas Chromatography Mass Spectrometry" ;
            schema1:termCode "Py-GC-MS" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://vocab.nerc.ac.uk/collection/L05/current/" ;
                    schema1:url "https://vocab.nerc.ac.uk/collection/L05/current/LAB02/" ;
                    schema1:value "LAB02" ] ;
            schema1:inDefinedTermSet "https://vocab.nerc.ac.uk/collection/L05/current/" ;
            schema1:name "Gas Chromatography Mass Spectrometry" ;
            schema1:termCode "GCMS" ] ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor <https://orcid.org/0000-0002-4805-7062> ;
            schema1:roleName [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "https://credit.niso.org/" ;
                    schema1:name "Principal Investigator" ;
                    schema1:termCode "investigation" ] ],
        [ a schema1:Role ;
            schema1:contributor <https://orcid.org/0000-0001-8898-3457> ;
            schema1:roleName "Operator" ] ;
    schema1:description "Integrated pyrolysis-gas chromatography-tandem mass spectrometry instrument system used for characterization of complex organic mixtures in bulk solid samples. Combines a flash pyrolysis front-end (up to 1300°C at 10°C/ms) with gas chromatographic separation and triple-quadrupole mass spectrometry with simultaneous full scan and timed SRM/MRM acquisition. Primary application: direct microanalysis of extraterrestrial materials without chemical pretreatment." ;
    schema1:hasPart ex:component-gas-chromatograph,
        ex:component-mass-spectrometer,
        ex:component-pyrolysis-oven ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "inventoryNumber" ;
            schema1:value "GSFC-AAL-PYGCMS-001" ],
        [ a schema1:PropertyValue ;
            schema1:propertyID "https://doi.org" ;
            schema1:url "https://doi.org/10.xxxx/instrument.pygcms.gsfc.001" ;
            schema1:value "10.xxxx/instrument.pygcms.gsfc.001" ] ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:contactPoint [ a schema1:ContactPoint ;
                    schema1:email "info@thermofisher.com" ;
                    schema1:url "https://www.thermofisher.com/contact-us.html" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://ror.org" ;
                    schema1:url "https://ror.org/03x1z2w73" ;
                    schema1:value "03x1z2w73" ] ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "serialNumber" ;
                    schema1:value "TSQ96CI2301004" ] ;
            schema1:name "TSQ 9000 Triple Quadrupole GC-MS/MS" ] ;
    schema1:name "Pyrolysis-GC-MS/MS System (NASA GSFC Astrobiology Analytical Lab)" ;
    schema1:owner <https://ror.org/0171mag52> ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:name "2023 annual calibration report" ;
            schema1:url "https://example.org/calibration/pygcms-gsfc-2023.pdf" ],
        [ a schema1:CreativeWork ;
            schema1:name "Dworkin et al. (2024) — Organic compounds in asteroid Bennu samples" ;
            schema1:url "https://doi.org/10.1038/s41586-024-08335-1" ],
        [ a schema1:CreativeWork ;
            schema1:description "User manual for the TSQ 9000 triple quadrupole GC-MS/MS system" ;
            schema1:name "TSQ 9000 User Guide" ;
            schema1:url "https://www.thermofisher.com/document-connect/document-connect.html?url=https://assets.thermofisher.com/TFS-Assets/CMD/manuals/man-80000-97071-tsq-9000-user-guide.pdf" ] ;
    schema1:subjectOf ex:metadata-instrument-pygcms-001 ;
    schema1:url "https://science.gsfc.nasa.gov/sed/bio/jason.p.dworkin" ;
    schema1:validFrom "2023-01-15" .

ex:metadata-instrument-pygcms-001 a schema1:DigitalDocument ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/instrumentDescription/v0.1> ;
    schema1:about ex:instrument-pygcmsms-gsfc-001 ;
    schema1:dateModified "2026-03-15" .

<https://orcid.org/0000-0001-8898-3457> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "angel.mojarro@nasa.gov" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://orcid.org" ;
            schema1:url "https://orcid.org/0000-0001-8898-3457" ;
            schema1:value "0000-0001-8898-3457" ] ;
    schema1:name "Mojarro, Angel" .

<https://orcid.org/0000-0002-4805-7062> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "jason.p.dworkin@nasa.gov" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://orcid.org" ;
            schema1:url "https://orcid.org/0000-0002-4805-7062" ;
            schema1:value "0000-0002-4805-7062" ] ;
    schema1:name "Dworkin, Jason P." .

<https://ror.org/0171mag52> a schema1:Organization ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "gsfc-aal@nasa.gov" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://ror.org" ;
            schema1:url "https://ror.org/0171mag52" ;
            schema1:value "0171mag52" ] ;
    schema1:name "NASA Goddard Space Flight Center" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Instrument Description
description: Schema for describing laboratory instruments and instrument systems.
  Supports ownership, manufacturer, model, commissioning dates, hierarchical sub-components
  via schema:hasPart, and domain-specific typing. Instruments may be standalone devices
  or complex systems with sub-components.
type: object
properties:
  '@context':
    type: object
    description: JSON-LD context declaring namespace prefixes.
    properties:
      schema:
        const: http://schema.org/
      dcterms:
        const: http://purl.org/dc/terms/
    required:
    - schema
  '@id':
    type: string
    description: Persistent identifier URI for this instrument metadata record.
  '@type':
    type: array
    items:
      type: string
    minItems: 2
    description: Must include schema:Product and schema:Thing. May include additional
      types.
    allOf:
    - contains:
        const: schema:Product
    - contains:
        const: schema:Thing
  schema:additionalType:
    description: Domain-specific type classifications. Should include a scientific
      instrument type URI (e.g. wd:Q3099911 for Wikidata scientific instrument).
    type: array
    items:
      type: string
    minItems: 1
  schema:name:
    type: string
    minLength: 3
    description: Human-readable name for this instrument.
  schema:description:
    type: string
    description: Text description of this instrument, its purpose, and capabilities.
  schema:alternateName:
    description: Alternate name(s), e.g. specific make/model designation, common abbreviation.
    anyOf:
    - type: string
    - type: array
      items:
        type: string
  schema:identifier:
    description: Formal identifier(s) for this instrument. Use PropertyValue for structured
      identifiers (e.g. PIDINST, serial number, inventory number).
    anyOf:
    - type: string
    - $ref: '#/$defs/Identifier'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/Identifier'
  schema:url:
    type: string
    format: uri
    description: Landing page URL for this instrument.
  schema:manufacturer:
    description: Organization that manufactured this instrument.
    $ref: '#/$defs/Organization'
  schema:model:
    type: object
    description: Product model information for this instrument.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:ProductModel
        minItems: 1
      schema:name:
        type: string
        description: Model name or number.
      schema:identifier:
        description: Model identifier.
        anyOf:
        - type: string
        - $ref: '#/$defs/Identifier'
    required:
    - schema:name
  schema:category:
    description: Instrument type classification(s) from a controlled vocabulary.
    type: array
    items:
      $ref: '#/$defs/DefinedTerm'
  schema:owner:
    description: Organization that owns this instrument.
    $ref: '#/$defs/Organization'
  schema:contributor:
    description: Agents associated with this instrument in specific roles (e.g. operator,
      custodian, principal investigator). Use schema:owner for the owning organization.
    type: array
    items:
      $ref: '#/$defs/AgentInRole'
  schema:additionalProperty:
    type: array
    description: Instrument-specific properties (measured variables, detection limits,
      calibration information, operating parameters, etc.).
    items:
      $ref: '#/$defs/AdditionalProperty'
  schema:validFrom:
    type: string
    description: Date the instrument was commissioned (ISO 8601).
  schema:validThrough:
    type: string
    description: Date the instrument was decommissioned (ISO 8601). Absent if still
      operational.
  schema:hasPart:
    type: array
    description: Sub-components of this instrument system. Each item is either an
      inline instrument description or an @id reference.
    items:
      anyOf:
      - $ref: '#/$defs/InstrumentComponent'
      - type: object
        properties:
          '@id':
            type: string
            description: Reference to a sub-component defined elsewhere.
        required:
        - '@id'
  schema:relatedLink:
    type: array
    description: Links to related resources (manuals, datasheets, calibration records,
      related instruments).
    items:
      $ref: '#/$defs/LabeledLink'
  schema:subjectOf:
    description: Catalog record metadata-about-metadata for this instrument description.
    type: object
    properties:
      '@id':
        type: string
      '@type':
        type: array
        items:
          type: string
      schema:dateModified:
        type: string
        description: Date this metadata record was last modified (ISO 8601).
      schema:about:
        type: object
        properties:
          '@id':
            type: string
            description: Reference back to the instrument @id.
      dcterms:conformsTo:
        description: Schema or profile this metadata record conforms to.
        type: array
        items:
          anyOf:
          - type: string
          - type: object
            properties:
              '@id':
                type: string
required:
- '@type'
- schema:name
- schema:identifier
$defs:
  Identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
  Organization:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
  Person:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  AgentInRole:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.yaml
  AdditionalProperty:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
  LabeledLink:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
  InstrumentComponent:
    type: object
    description: A sub-component of an instrument system. Uses the same structure
      as the parent instrument but without nesting (single level of hasPart).
    properties:
      '@type':
        type: array
        items:
          type: string
        minItems: 1
        contains:
          const: schema:Thing
      '@id':
        type: string
      schema:name:
        type: string
        minLength: 3
      schema:description:
        type: string
      schema:alternateName:
        anyOf:
        - type: string
        - type: array
          items:
            type: string
      schema:identifier:
        anyOf:
        - type: string
        - $ref: '#/$defs/Identifier'
      schema:additionalType:
        description: Component type classification.
        anyOf:
        - type: string
        - type: array
          items:
            type: string
      schema:additionalProperty:
        type: array
        items:
          $ref: '#/$defs/AdditionalProperty'
      schema:manufacturer:
        $ref: '#/$defs/Organization'
      schema:model:
        type: object
        properties:
          '@type':
            type: array
            items:
              type: string
            contains:
              const: schema:ProductModel
            minItems: 1
          schema:name:
            type: string
          schema:identifier:
            anyOf:
            - type: string
            - $ref: '#/$defs/Identifier'
    required:
    - schema:name
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/context.jsonld)

## Sources

* [schema.org Product](https://schema.org/Product)
* [schema.org instrument property](https://schema.org/instrument)
* [PIDINST - Persistent Identification of Instruments](https://doi.org/10.15497/RDA00070)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/instrument`

