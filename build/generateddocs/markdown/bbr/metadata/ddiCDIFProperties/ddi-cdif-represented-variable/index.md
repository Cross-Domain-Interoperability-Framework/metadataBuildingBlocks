
# DDI-CDI Represented Variable (Schema)

`cdif.bbr.metadata.ddiCDIFProperties.ddi-cdif-represented-variable` *v0.1*

Conceptual variable with a substantive value domain specified.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI RepresentedVariable describes a conceptual variable together with its substantive value domain, independent of any particular dataset. The root `cdi:RepresentedVariable` carries `cdi:takesSubstantiveValuesFrom` and `cdi:takesSentinelValuesFrom` (referencing `ddicdiValueDomain`), `cdi:takesSubstantiveConceptsFrom` and `cdi:takesSentinelConceptsFrom` (local conceptual-domain `$defs`), `cdi:measures` linking to a `cdi:UnitType`, and the unit-of-measure properties `cdi:describedUnitOfMeasure`, `cdi:simpleUnitOfMeasure`, and `cdi:unitOfMeasureKind`.

It is referenced from `ddicdiDataStructureComponent` via `cdi:isDefinedBy` so that each component in a data structure is anchored to a reusable conceptual variable. Together with `ddicdiInstanceVariable` (the dataset-bound realization) and `ddicdiValueDomain` (the allowed values), RepresentedVariable forms the conceptual layer of the CDIF Data Description profile.

## Examples

### Minimal RepresentedVariable
Bare cdi:RepresentedVariable — schema only requires @type.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:RepresentedVariable"],
  "@id": "ex:rep-var/age-in-years"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-represented-variable/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:RepresentedVariable"
  ],
  "@id": "ex:rep-var/age-in-years"
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

<https://example.org/rep-var/age-in-years> a cdi:RepresentedVariable .


```


### Complete RepresentedVariable
Fully described RepresentedVariable exercising every schema property
including substantive/sentinel conceptual domain references, unit type,
value and concept descriptions, controlled vocabulary entries, and SKOS
concept references.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "ex": "https://example.org/"
  },
  "@type": [
    "cdi:RepresentedVariable"
  ],
  "@id": "ex:rv/seaWaterTemperature",
  "cdi:identifier": {
    "@type": [
      "cdi:Identifier"
    ],
    "cdi:uri": "https://example.org/rv/seaWaterTemperature",
    "cdi:ddiIdentifier": {
      "@type": [
        "cdi:InternationalRegistrationDataIdentifier"
      ],
      "cdi:dataIdentifier": "OCEAN-RV-SEA_WATER_TEMP",
      "cdi:registrationAuthorityIdentifier": "0000.0000.0000",
      "cdi:versionIdentifier": "1.0.0"
    },
    "cdi:nonDdiIdentifier": [
      {
        "@type": [
          "cdi:NonDdiIdentifier"
        ],
        "cdi:identifierContent": "ODC-RV-SST-1",
        "cdi:managingAgency": "Example Ocean Data Center"
      }
    ]
  },
  "cdi:name": [
    {
      "@type": [
        "cdi:ObjectName"
      ],
      "cdi:name": "sea_water_temperature",
      "cdi:context": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "technical-name"
        ],
        "cdi:name": "DDI-CDI naming context",
        "cdi:vocabulary": {
          "@type": [
            "cdif:Reference"
          ],
          "cdi:uri": "https://ddialliance.org/Specification/DDI-CDI/1.0/naming-context"
        }
      }
    },
    {
      "@type": [
        "cdi:ObjectName"
      ],
      "cdi:name": "Sea Water Temperature",
      "cdi:context": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "display-name"
        ]
      }
    }
  ],
  "cdi:displayLabel": [
    {
      "@type": [
        "cdi:LabelForDisplay"
      ],
      "cdi:maxLength": 32,
      "cdi:locationVariant": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "en-US"
        ]
      },
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Sea Water Temperature",
        "cdi:language": "en"
      }
    },
    {
      "@type": [
        "cdi:LabelForDisplay"
      ],
      "cdi:maxLength": 80,
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Temperature de l'eau de mer",
        "cdi:language": "fr"
      }
    }
  ],
  "cdi:descriptiveText": {
    "@type": [
      "cdi:InternationalString"
    ],
    "cdi:languageSpecificString": [
      {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "In-situ temperature of sea water at a stated depth and station, expressed in degrees Celsius.",
        "cdi:language": "en"
      },
      {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Temperatura del agua de mar in situ a una profundidad y estacion declaradas, en grados Celsius.",
        "cdi:language": "es"
      }
    ]
  },
  "cdi:definition": {
    "@type": [
      "cdi:InternationalString"
    ],
    "cdi:languageSpecificString": {
      "@type": [
        "cdi:LanguageString"
      ],
      "cdi:content": "Temperature of the water column measured in situ by a CTD or other oceanographic sensor at a specified depth.",
      "cdi:language": "en"
    }
  },
  "cdi:externalDefinition": {
    "@type": [
      "cdif:Reference"
    ],
    "cdi:uri": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/",
    "cdi:description": "BODC P01 'Temperature of the water column' parameter usage",
    "cdi:semantic": {
      "@type": [
        "cdi:ControlledVocabularyEntry"
      ],
      "cdi:entryValue": [
        "definedBy"
      ]
    }
  },
  "cdi:describedUnitOfMeasure": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "DEG_C"
    ],
    "cdi:name": "QUDT Units",
    "cdi:entryReference": [
      {
        "@type": [
          "cdif:Reference"
        ],
        "cdi:uri": "http://qudt.org/vocab/unit/DEG_C",
        "cdi:description": "degree Celsius"
      }
    ],
    "cdi:vocabulary": {
      "@type": [
        "cdif:Reference"
      ],
      "cdi:uri": "http://qudt.org/vocab/unit/"
    }
  },
  "cdi:simpleUnitOfMeasure": "Cel",
  "cdi:unitOfMeasureKind": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "temperature"
    ],
    "cdi:name": "Kinds of unit of measure",
    "cdi:vocabulary": {
      "@type": [
        "cdif:Reference"
      ],
      "cdi:uri": "http://qudt.org/vocab/quantitykind/"
    }
  },
  "cdi:hasIntendedDataType": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "xsd:decimal"
    ],
    "cdi:name": "XML Schema Datatypes",
    "cdi:entryReference": [
      {
        "@type": [
          "cdif:Reference"
        ],
        "cdi:uri": "http://www.w3.org/2001/XMLSchema#decimal"
      }
    ]
  },
  "cdi:takesSubstantiveValuesFrom": {
    "@id": "ex:vd/temperatureCelsius"
  },
  "cdi:takesSentinelValuesFrom": [
    {
      "@id": "ex:vd/temperatureSentinel"
    },
    {
      "@type": [
        "cdi:SentinelValueDomain"
      ],
      "@id": "ex:vd/temperatureSentinelInline",
      "cdi:identifier": {
        "@type": [
          "cdi:Identifier"
        ],
        "cdi:uri": "https://example.org/vd/temperatureSentinelInline"
      },
      "cdi:displayLabel": [
        {
          "@type": [
            "cdi:LabelForDisplay"
          ],
          "cdi:languageSpecificString": {
            "@type": [
              "cdi:LanguageString"
            ],
            "cdi:content": "Inline R-style sentinel domain",
            "cdi:language": "en"
          }
        }
      ],
      "cdi:platformType": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "Rstyle"
        ]
      }
    }
  ],
  "cdi:takesSubstantiveConceptsFrom": {
    "@type": [
      "cdi:SubstantiveConceptualDomain"
    ],
    "@id": "ex:cd/seaWaterTemperatureConcept",
    "cdi:identifier": {
      "@type": [
        "cdi:Identifier"
      ],
      "cdi:uri": "https://example.org/cd/seaWaterTemperatureConcept"
    },
    "cdi:displayLabel": [
      {
        "@type": [
          "cdi:LabelForDisplay"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Sea water temperature conceptual domain",
          "cdi:language": "en"
        }
      }
    ],
    "cdi:isDescribedBy": {
      "@type": [
        "cdi:ValueAndConceptDescription"
      ],
      "@id": "ex:cd/seaWaterTemperatureConcept/desc",
      "cdi:classificationLevel": "Continuous",
      "cdi:description": {
        "@type": [
          "cdi:InternationalString"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Continuous conceptual domain of plausible sea water temperatures.",
          "cdi:language": "en"
        }
      },
      "cdi:minimumValueInclusive": "-2.0",
      "cdi:maximumValueInclusive": "35.5"
    },
    "cdi:takesConceptsFrom": {
      "@id": "ex:cs/oceanographicConcepts"
    }
  },
  "cdi:takesSentinelConceptsFrom": {
    "@id": "ex:cd/temperatureSentinelConcepts"
  },
  "cdi:measures": {
    "@type": [
      "cdi:UnitType"
    ],
    "@id": "ex:ut/oceanographicStation",
    "cdi:identifier": {
      "@type": [
        "cdi:Identifier"
      ],
      "cdi:uri": "https://example.org/ut/oceanographicStation"
    },
    "cdi:name": [
      {
        "@type": [
          "cdi:ObjectName"
        ],
        "cdi:name": "OceanographicStation"
      }
    ],
    "cdi:displayLabel": [
      {
        "@type": [
          "cdi:LabelForDisplay"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Oceanographic monitoring station",
          "cdi:language": "en"
        }
      }
    ],
    "cdi:descriptiveText": {
      "@type": [
        "cdi:InternationalString"
      ],
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Fixed or moored oceanographic monitoring station hosting a CTD or comparable temperature sensor.",
        "cdi:language": "en"
      }
    },
    "cdi:definition": {
      "@type": [
        "cdi:InternationalString"
      ],
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Unit type for fixed oceanographic monitoring stations, the bearer of in-situ temperature observations.",
        "cdi:language": "en"
      }
    },
    "cdi:uses": [
      {
        "@type": [
          "cdi:Concept"
        ],
        "@id": "ex:concept/monitoringStation",
        "cdi:identifier": {
          "@type": [
            "cdi:Identifier"
          ],
          "cdi:uri": "https://example.org/concept/monitoringStation"
        },
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "monitoringStation"
          }
        ],
        "cdi:displayLabel": [
          {
            "@type": [
              "cdi:LabelForDisplay"
            ],
            "cdi:languageSpecificString": {
              "@type": [
                "cdi:LanguageString"
              ],
              "cdi:content": "monitoring station concept",
              "cdi:language": "en"
            }
          }
        ],
        "cdi:definition": {
          "@type": [
            "cdi:InternationalString"
          ],
          "cdi:languageSpecificString": {
            "@type": [
              "cdi:LanguageString"
            ],
            "cdi:content": "A site at which environmental observations are recorded over time.",
            "cdi:language": "en"
          }
        }
      }
    ]
  },
  "cdi:uses": [
    {
      "@type": [
        "cdi:Concept"
      ],
      "@id": "ex:concept/temperatureMeasurement",
      "cdi:identifier": {
        "@type": [
          "cdi:Identifier"
        ],
        "cdi:uri": "https://example.org/concept/temperatureMeasurement"
      },
      "cdi:name": [
        {
          "@type": [
            "cdi:ObjectName"
          ],
          "cdi:name": "temperatureMeasurement"
        }
      ],
      "cdi:displayLabel": [
        {
          "@type": [
            "cdi:LabelForDisplay"
          ],
          "cdi:languageSpecificString": {
            "@type": [
              "cdi:LanguageString"
            ],
            "cdi:content": "temperature measurement",
            "cdi:language": "en"
          }
        }
      ],
      "cdi:definition": {
        "@type": [
          "cdi:InternationalString"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "The act of measuring temperature with a calibrated sensor.",
          "cdi:language": "en"
        }
      }
    },
    {
      "@id": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-represented-variable/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:RepresentedVariable"
  ],
  "@id": "ex:rv/seaWaterTemperature",
  "cdi:identifier": {
    "@type": [
      "cdi:Identifier"
    ],
    "cdi:uri": "https://example.org/rv/seaWaterTemperature",
    "cdi:ddiIdentifier": {
      "@type": [
        "cdi:InternationalRegistrationDataIdentifier"
      ],
      "cdi:dataIdentifier": "OCEAN-RV-SEA_WATER_TEMP",
      "cdi:registrationAuthorityIdentifier": "0000.0000.0000",
      "cdi:versionIdentifier": "1.0.0"
    },
    "cdi:nonDdiIdentifier": [
      {
        "@type": [
          "cdi:NonDdiIdentifier"
        ],
        "cdi:identifierContent": "ODC-RV-SST-1",
        "cdi:managingAgency": "Example Ocean Data Center"
      }
    ]
  },
  "cdi:name": [
    {
      "@type": [
        "cdi:ObjectName"
      ],
      "cdi:name": "sea_water_temperature",
      "cdi:context": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "technical-name"
        ],
        "cdi:name": "DDI-CDI naming context",
        "cdi:vocabulary": {
          "@type": [
            "cdif:Reference"
          ],
          "cdi:uri": "https://ddialliance.org/Specification/DDI-CDI/1.0/naming-context"
        }
      }
    },
    {
      "@type": [
        "cdi:ObjectName"
      ],
      "cdi:name": "Sea Water Temperature",
      "cdi:context": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "display-name"
        ]
      }
    }
  ],
  "cdi:displayLabel": [
    {
      "@type": [
        "cdi:LabelForDisplay"
      ],
      "cdi:maxLength": 32,
      "cdi:locationVariant": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "en-US"
        ]
      },
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Sea Water Temperature",
        "cdi:language": "en"
      }
    },
    {
      "@type": [
        "cdi:LabelForDisplay"
      ],
      "cdi:maxLength": 80,
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Temperature de l'eau de mer",
        "cdi:language": "fr"
      }
    }
  ],
  "cdi:descriptiveText": {
    "@type": [
      "cdi:InternationalString"
    ],
    "cdi:languageSpecificString": [
      {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "In-situ temperature of sea water at a stated depth and station, expressed in degrees Celsius.",
        "cdi:language": "en"
      },
      {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Temperatura del agua de mar in situ a una profundidad y estacion declaradas, en grados Celsius.",
        "cdi:language": "es"
      }
    ]
  },
  "cdi:definition": {
    "@type": [
      "cdi:InternationalString"
    ],
    "cdi:languageSpecificString": {
      "@type": [
        "cdi:LanguageString"
      ],
      "cdi:content": "Temperature of the water column measured in situ by a CTD or other oceanographic sensor at a specified depth.",
      "cdi:language": "en"
    }
  },
  "cdi:externalDefinition": {
    "@type": [
      "cdif:Reference"
    ],
    "cdi:uri": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/",
    "cdi:description": "BODC P01 'Temperature of the water column' parameter usage",
    "cdi:semantic": {
      "@type": [
        "cdi:ControlledVocabularyEntry"
      ],
      "cdi:entryValue": [
        "definedBy"
      ]
    }
  },
  "cdi:describedUnitOfMeasure": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "DEG_C"
    ],
    "cdi:name": "QUDT Units",
    "cdi:entryReference": [
      {
        "@type": [
          "cdif:Reference"
        ],
        "cdi:uri": "http://qudt.org/vocab/unit/DEG_C",
        "cdi:description": "degree Celsius"
      }
    ],
    "cdi:vocabulary": {
      "@type": [
        "cdif:Reference"
      ],
      "cdi:uri": "http://qudt.org/vocab/unit/"
    }
  },
  "cdi:simpleUnitOfMeasure": "Cel",
  "cdi:unitOfMeasureKind": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "temperature"
    ],
    "cdi:name": "Kinds of unit of measure",
    "cdi:vocabulary": {
      "@type": [
        "cdif:Reference"
      ],
      "cdi:uri": "http://qudt.org/vocab/quantitykind/"
    }
  },
  "cdi:hasIntendedDataType": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "xsd:decimal"
    ],
    "cdi:name": "XML Schema Datatypes",
    "cdi:entryReference": [
      {
        "@type": [
          "cdif:Reference"
        ],
        "cdi:uri": "http://www.w3.org/2001/XMLSchema#decimal"
      }
    ]
  },
  "cdi:takesSubstantiveValuesFrom": {
    "@id": "ex:vd/temperatureCelsius"
  },
  "cdi:takesSentinelValuesFrom": [
    {
      "@id": "ex:vd/temperatureSentinel"
    },
    {
      "@type": [
        "cdi:SentinelValueDomain"
      ],
      "@id": "ex:vd/temperatureSentinelInline",
      "cdi:identifier": {
        "@type": [
          "cdi:Identifier"
        ],
        "cdi:uri": "https://example.org/vd/temperatureSentinelInline"
      },
      "cdi:displayLabel": [
        {
          "@type": [
            "cdi:LabelForDisplay"
          ],
          "cdi:languageSpecificString": {
            "@type": [
              "cdi:LanguageString"
            ],
            "cdi:content": "Inline R-style sentinel domain",
            "cdi:language": "en"
          }
        }
      ],
      "cdi:platformType": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "Rstyle"
        ]
      }
    }
  ],
  "cdi:takesSubstantiveConceptsFrom": {
    "@type": [
      "cdi:SubstantiveConceptualDomain"
    ],
    "@id": "ex:cd/seaWaterTemperatureConcept",
    "cdi:identifier": {
      "@type": [
        "cdi:Identifier"
      ],
      "cdi:uri": "https://example.org/cd/seaWaterTemperatureConcept"
    },
    "cdi:displayLabel": [
      {
        "@type": [
          "cdi:LabelForDisplay"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Sea water temperature conceptual domain",
          "cdi:language": "en"
        }
      }
    ],
    "cdi:isDescribedBy": {
      "@type": [
        "cdi:ValueAndConceptDescription"
      ],
      "@id": "ex:cd/seaWaterTemperatureConcept/desc",
      "cdi:classificationLevel": "Continuous",
      "cdi:description": {
        "@type": [
          "cdi:InternationalString"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Continuous conceptual domain of plausible sea water temperatures.",
          "cdi:language": "en"
        }
      },
      "cdi:minimumValueInclusive": "-2.0",
      "cdi:maximumValueInclusive": "35.5"
    },
    "cdi:takesConceptsFrom": {
      "@id": "ex:cs/oceanographicConcepts"
    }
  },
  "cdi:takesSentinelConceptsFrom": {
    "@id": "ex:cd/temperatureSentinelConcepts"
  },
  "cdi:measures": {
    "@type": [
      "cdi:UnitType"
    ],
    "@id": "ex:ut/oceanographicStation",
    "cdi:identifier": {
      "@type": [
        "cdi:Identifier"
      ],
      "cdi:uri": "https://example.org/ut/oceanographicStation"
    },
    "cdi:name": [
      {
        "@type": [
          "cdi:ObjectName"
        ],
        "cdi:name": "OceanographicStation"
      }
    ],
    "cdi:displayLabel": [
      {
        "@type": [
          "cdi:LabelForDisplay"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Oceanographic monitoring station",
          "cdi:language": "en"
        }
      }
    ],
    "cdi:descriptiveText": {
      "@type": [
        "cdi:InternationalString"
      ],
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Fixed or moored oceanographic monitoring station hosting a CTD or comparable temperature sensor.",
        "cdi:language": "en"
      }
    },
    "cdi:definition": {
      "@type": [
        "cdi:InternationalString"
      ],
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Unit type for fixed oceanographic monitoring stations, the bearer of in-situ temperature observations.",
        "cdi:language": "en"
      }
    },
    "cdi:uses": [
      {
        "@type": [
          "cdi:Concept"
        ],
        "@id": "ex:concept/monitoringStation",
        "cdi:identifier": {
          "@type": [
            "cdi:Identifier"
          ],
          "cdi:uri": "https://example.org/concept/monitoringStation"
        },
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "monitoringStation"
          }
        ],
        "cdi:displayLabel": [
          {
            "@type": [
              "cdi:LabelForDisplay"
            ],
            "cdi:languageSpecificString": {
              "@type": [
                "cdi:LanguageString"
              ],
              "cdi:content": "monitoring station concept",
              "cdi:language": "en"
            }
          }
        ],
        "cdi:definition": {
          "@type": [
            "cdi:InternationalString"
          ],
          "cdi:languageSpecificString": {
            "@type": [
              "cdi:LanguageString"
            ],
            "cdi:content": "A site at which environmental observations are recorded over time.",
            "cdi:language": "en"
          }
        }
      }
    ]
  },
  "cdi:uses": [
    {
      "@type": [
        "cdi:Concept"
      ],
      "@id": "ex:concept/temperatureMeasurement",
      "cdi:identifier": {
        "@type": [
          "cdi:Identifier"
        ],
        "cdi:uri": "https://example.org/concept/temperatureMeasurement"
      },
      "cdi:name": [
        {
          "@type": [
            "cdi:ObjectName"
          ],
          "cdi:name": "temperatureMeasurement"
        }
      ],
      "cdi:displayLabel": [
        {
          "@type": [
            "cdi:LabelForDisplay"
          ],
          "cdi:languageSpecificString": {
            "@type": [
              "cdi:LanguageString"
            ],
            "cdi:content": "temperature measurement",
            "cdi:language": "en"
          }
        }
      ],
      "cdi:definition": {
        "@type": [
          "cdi:InternationalString"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "The act of measuring temperature with a calibrated sensor.",
          "cdi:language": "en"
        }
      }
    },
    {
      "@id": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/rv/seaWaterTemperature> a cdi:RepresentedVariable ;
    cdi:definition [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Temperature of the water column measured in situ by a CTD or other oceanographic sensor at a specified depth." ;
                    cdi:language "en" ] ] ;
    cdi:describedUnitOfMeasure [ a cdi:ControlledVocabularyEntry ;
            cdi:entryReference [ a <cdif:Reference> ;
                    cdi:description "degree Celsius" ;
                    cdi:uri "http://qudt.org/vocab/unit/DEG_C" ] ;
            cdi:entryValue "DEG_C" ;
            cdi:name "QUDT Units" ;
            cdi:vocabulary [ a <cdif:Reference> ;
                    cdi:uri "http://qudt.org/vocab/unit/" ] ] ;
    cdi:descriptiveText [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Temperatura del agua de mar in situ a una profundidad y estacion declaradas, en grados Celsius." ;
                    cdi:language "es" ],
                [ a cdi:LanguageString ;
                    cdi:content "In-situ temperature of sea water at a stated depth and station, expressed in degrees Celsius." ;
                    cdi:language "en" ] ] ;
    cdi:displayLabel [ a cdi:LabelForDisplay ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Sea Water Temperature" ;
                    cdi:language "en" ] ;
            cdi:locationVariant [ a cdi:ControlledVocabularyEntry ;
                    cdi:entryValue "en-US" ] ;
            cdi:maxLength 32 ],
        [ a cdi:LabelForDisplay ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Temperature de l'eau de mer" ;
                    cdi:language "fr" ] ;
            cdi:maxLength 80 ] ;
    cdi:externalDefinition [ a <cdif:Reference> ;
            cdi:description "BODC P01 'Temperature of the water column' parameter usage" ;
            cdi:semantic [ a cdi:ControlledVocabularyEntry ;
                    cdi:entryValue "definedBy" ] ;
            cdi:uri "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/" ] ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryReference [ a <cdif:Reference> ;
                    cdi:uri "http://www.w3.org/2001/XMLSchema#decimal" ] ;
            cdi:entryValue "xsd:decimal" ;
            cdi:name "XML Schema Datatypes" ] ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:ddiIdentifier [ a cdi:InternationalRegistrationDataIdentifier ;
                    cdi:dataIdentifier "OCEAN-RV-SEA_WATER_TEMP" ;
                    cdi:registrationAuthorityIdentifier "0000.0000.0000" ;
                    cdi:versionIdentifier "1.0.0" ] ;
            cdi:nonDdiIdentifier [ a cdi:NonDdiIdentifier ;
                    cdi:identifierContent "ODC-RV-SST-1" ;
                    cdi:managingAgency "Example Ocean Data Center" ] ;
            cdi:uri "https://example.org/rv/seaWaterTemperature" ] ;
    cdi:measures <https://example.org/ut/oceanographicStation> ;
    cdi:name [ a cdi:ObjectName ;
            cdi:context [ a cdi:ControlledVocabularyEntry ;
                    cdi:entryValue "display-name" ] ;
            cdi:name "Sea Water Temperature" ],
        [ a cdi:ObjectName ;
            cdi:context [ a cdi:ControlledVocabularyEntry ;
                    cdi:entryValue "technical-name" ;
                    cdi:name "DDI-CDI naming context" ;
                    cdi:vocabulary [ a <cdif:Reference> ;
                            cdi:uri "https://ddialliance.org/Specification/DDI-CDI/1.0/naming-context" ] ] ;
            cdi:name "sea_water_temperature" ] ;
    cdi:simpleUnitOfMeasure "Cel" ;
    cdi:takesSentinelConceptsFrom <https://example.org/cd/temperatureSentinelConcepts> ;
    cdi:takesSentinelValuesFrom <https://example.org/vd/temperatureSentinel>,
        <https://example.org/vd/temperatureSentinelInline> ;
    cdi:takesSubstantiveConceptsFrom <https://example.org/cd/seaWaterTemperatureConcept> ;
    cdi:takesSubstantiveValuesFrom <https://example.org/vd/temperatureCelsius> ;
    cdi:unitOfMeasureKind [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "temperature" ;
            cdi:name "Kinds of unit of measure" ;
            cdi:vocabulary [ a <cdif:Reference> ;
                    cdi:uri "http://qudt.org/vocab/quantitykind/" ] ] ;
    cdi:uses <http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/>,
        <https://example.org/concept/temperatureMeasurement> .

<https://example.org/cd/seaWaterTemperatureConcept> a cdi:SubstantiveConceptualDomain ;
    cdi:displayLabel [ a cdi:LabelForDisplay ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Sea water temperature conceptual domain" ;
                    cdi:language "en" ] ] ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:uri "https://example.org/cd/seaWaterTemperatureConcept" ] ;
    cdi:isDescribedBy <https://example.org/cd/seaWaterTemperatureConcept/desc> ;
    cdi:takesConceptsFrom <https://example.org/cs/oceanographicConcepts> .

<https://example.org/cd/seaWaterTemperatureConcept/desc> a cdi:ValueAndConceptDescription ;
    cdi:classificationLevel "Continuous" ;
    cdi:description [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Continuous conceptual domain of plausible sea water temperatures." ;
                    cdi:language "en" ] ] ;
    cdi:maximumValueInclusive "35.5" ;
    cdi:minimumValueInclusive "-2.0" .

<https://example.org/concept/monitoringStation> a cdi:Concept ;
    cdi:definition [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "A site at which environmental observations are recorded over time." ;
                    cdi:language "en" ] ] ;
    cdi:displayLabel [ a cdi:LabelForDisplay ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "monitoring station concept" ;
                    cdi:language "en" ] ] ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:uri "https://example.org/concept/monitoringStation" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "monitoringStation" ] .

<https://example.org/concept/temperatureMeasurement> a cdi:Concept ;
    cdi:definition [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "The act of measuring temperature with a calibrated sensor." ;
                    cdi:language "en" ] ] ;
    cdi:displayLabel [ a cdi:LabelForDisplay ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "temperature measurement" ;
                    cdi:language "en" ] ] ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:uri "https://example.org/concept/temperatureMeasurement" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "temperatureMeasurement" ] .

<https://example.org/ut/oceanographicStation> a cdi:UnitType ;
    cdi:definition [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Unit type for fixed oceanographic monitoring stations, the bearer of in-situ temperature observations." ;
                    cdi:language "en" ] ] ;
    cdi:descriptiveText [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Fixed or moored oceanographic monitoring station hosting a CTD or comparable temperature sensor." ;
                    cdi:language "en" ] ] ;
    cdi:displayLabel [ a cdi:LabelForDisplay ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Oceanographic monitoring station" ;
                    cdi:language "en" ] ] ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:uri "https://example.org/ut/oceanographicStation" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "OceanographicStation" ] ;
    cdi:uses <https://example.org/concept/monitoringStation> .

<https://example.org/vd/temperatureSentinelInline> a cdi:SentinelValueDomain ;
    cdi:displayLabel [ a cdi:LabelForDisplay ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Inline R-style sentinel domain" ;
                    cdi:language "en" ] ] ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:uri "https://example.org/vd/temperatureSentinelInline" ] ;
    cdi:platformType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "Rstyle" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Represented Variable
description: Conceptual variable with a substantive value domain specified.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: cdi:RepresentedVariable
    minItems: 1
  '@id':
    type: string
    description: Identifier for this RepresentedVariable node
  cdi:describedUnitOfMeasure:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
    description: The unit in which the data values are measured (kg, pound, euro),
      expressed as a value from a controlled system of entries (i.e., QDT). Supports
      the provision of an identifier for the entry in the authoritative source (a
      URI, etc.), and the specific vocabulary.
  cdi:hasIntendedDataType:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
    description: The data type intended to be used by this variable. Supports the
      optional use of an external controlled vocabulary.
  cdi:takesSentinelValuesFrom:
    type: array
    items:
      anyOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-value-domain/schema.yaml
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    minItems: 1
  cdi:takesSubstantiveValuesFrom:
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-value-domain/schema.yaml
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
  cdi:simpleUnitOfMeasure:
    type: string
    description: The unit in which the data values are measured (kg, pound, euro),
      expressed as a simple string, in cases where no additional information is available
      (in the legacy system) or needed (as in the case of broad agreement within the
      community of use [i.e., ISO country codes, currencies, etc. in SDMX])
  cdi:descriptiveText:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
    description: A short natural language account of the characteristics of the object.
  cdi:takesSentinelConceptsFrom:
    anyOf:
    - $ref: '#/$defs/SentinelConceptualDomain'
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
  cdi:takesSubstantiveConceptsFrom:
    anyOf:
    - $ref: '#/$defs/SubstantiveConceptualDomain'
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
  cdi:measures:
    anyOf:
    - $ref: '#/$defs/UnitType'
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
  cdi:unitOfMeasureKind:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
    description: Kind of unit of measure, so that it may be prone to translation to
      equivalent UOMs. Example values include "acceleration," "temperature," "salinity",
      etc. This description exists at the conceptual level, indicating a limitation
      on the type of representations which may be used for the variable as it is made
      more concrete.
  cdi:definition:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
    description: Natural language statement conveying the meaning of a concept, differentiating
      it from other concepts. Supports the use of multiple languages and structured
      text. 'externalDefinition' can't be used if 'definition' is used.
  cdi:displayLabel:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/LabelForDisplay
    minItems: 1
    description: A human-readable display label for the object. Supports the use of
      multiple languages. Repeat for labels with different content, for example, labels
      with differing length limitations.
  cdi:externalDefinition:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Reference
    description: A reference to an external definition of a concept (that is, a concept
      which is described outside the content of the DDI-CDI metadata description).
      An example is a SKOS concept. The definition property is assumed to duplicate
      the external one referenced if externalDefinition is used. Other corresponding
      properties are assumed to be included unchanged if used.
  cdi:identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
    description: Identifier for objects requiring short- or long-lasting referencing
      and management.
  cdi:name:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ObjectName
    minItems: 1
    description: Human understandable name (linguistic signifier, word, phrase, or
      mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context provided
      to specify usage.
  cdi:uses:
    type: array
    items:
      anyOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    minItems: 1
required:
- '@type'
$defs:
  ConceptSystem:
    type: object
    description: Set of concepts structured by the relations among them [GSIM 1.1].
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ConceptSystem
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ConceptSystem node
      cdi:allowsDuplicates:
        type: boolean
        description: "If value is False, the members are unique within the collection
          - if True, there may be duplicates. (Note that a mathematical \u201Cbag\u201D
          permits duplicates and is unordered - a \u201Cset\u201D does not have duplicates
          and may be ordered.)"
      cdi:externalDefinition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Reference
        description: A reference to an external definition of a concept (that is,
          a concept which is described outside the content of the DDI-CDI metadata
          description). An example is a SKOS concept. The definition property is assumed
          to duplicate the external one referenced if externalDefinition is used.
          Other corresponding properties are assumed to be included unchanged if used.
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (liguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
      cdi:isDefinedBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
    required:
    - '@type'
  SentinelConceptualDomain:
    type: object
    description: Conceptual domain of sentinel concepts.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:SentinelConceptualDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this SentinelConceptualDomain node
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isDescribedBy:
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:takesConceptsFrom:
        anyOf:
        - $ref: '#/$defs/ConceptSystem'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  SubstantiveConceptualDomain:
    type: object
    description: Conceptual domain of substantive concepts.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:SubstantiveConceptualDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this SubstantiveConceptualDomain node
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isDescribedBy:
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:takesConceptsFrom:
        anyOf:
        - $ref: '#/$defs/ConceptSystem'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  TypedString:
    type: object
    description: TypedString combines a type with content defined as a simple string.
      May be used wherever a simple string needs to support a type definition to clarify
      its content.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:TypedString
        minItems: 1
      cdi:content:
        type: string
        description: Content of the property expressed as a simple string.
      cdi:typeOfContent:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Optional use of a controlled vocabulary to specifically type
          the associated content.
  UnitType:
    type: object
    description: Unit type is a type or class of objects of interest (units).
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:UnitType
        minItems: 1
      '@id':
        type: string
        description: Identifier for this UnitType node
      cdi:descriptiveText:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
        description: A short natural language account of the characteristics of the
          object.
      cdi:definition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
        description: Natural language statement conveying the meaning of a concept,
          differentiating it from other concepts. Supports the use of multiple languages
          and structured text. 'externalDefinition' can't be used if 'definition'
          is used.
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
      cdi:externalDefinition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Reference
        description: A reference to an external definition of a concept (that is,
          a concept which is described outside the content of the DDI-CDI metadata
          description). An example is a SKOS concept. The definition property is assumed
          to duplicate the external one referenced if externalDefinition is used.
          Other corresponding properties are assumed to be included unchanged if used.
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
      cdi:uses:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
    required:
    - '@type'
  ValueAndConceptDescription:
    type: object
    description: Formal description of a set of values.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ValueAndConceptDescription
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ValueAndConceptDescription node
      cdi:classificationLevel:
        type: string
        enum:
        - Continuous
        - Interval
        - Nominal
        - Ordinal
        - Ratio
        description: Indicates the type of relationship, nominal, ordinal, interval,
          ratio, or continuous. Use where appropriate for the representation type.
      cdi:description:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
        description: A formal description of the set of values in human-readable language.
      cdi:formatPattern:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        description: 'A pattern for a number as described in Unicode Locale Data Markup
          Language (LDML) (http://www.unicode.org/reports/tr35/tr35.html) Part 3:
          Numbers (http://www.unicode.org/reports/tr35/tr35-numbers.html#Number_Format_Patterns)
          and Part 4. Dates (http://www.unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns)
          . Examples would be #,##0.### to describe the pattern for a decimal number,
          or yyyy.MM.dd G ''at'' HH:mm:ss zzz for a datetime pattern.'
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:logicalExpression:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        description: A logical expression where the values of "x" making the expression
          true are the members of the set of valid values. For example, "(all reals
          x such that x > 0)" describes the real numbers greater than 0.
      cdi:maximumValueExclusive:
        type: string
        description: 'A string denoting the maximum possible value (excluding this
          value). From the W3C Recommendation "Metadata Vocabulary for Tabular Data"
          (https://www.w3.org/TR/tabular-metadata/) 5.11.2: "maxExclusive: An atomic
          property that contains a single number or string that is the maximum valid
          value (exclusive). The value of this property becomes the maximum exclusive
          annotation for the described datatype. See Value Constraints in [tabular-data-model]
          for details."'
      cdi:maximumValueInclusive:
        type: string
        description: 'A string denoting the maximum possible value. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.11.2: "maximum: An atomic property that contains a single number or string
          that is the maximum valid value (inclusive); equivalent to maxInclusive.
          The value of this property becomes the maximum annotation for the described
          datatype. See Value Constraints in [tabular-data-model] for details."'
      cdi:minimumValueExclusive:
        type: string
        description: 'A string denoting the minimum possible value (excluding this
          value). From the W3C Recommendation "Metadata Vocabulary for Tabular Data"
          (https://www.w3.org/TR/tabular-metadata/) 5.11.2: "minExclusive: An atomic
          property that contains a single number or string that is the minimum valid
          value (exclusive). The value of this property becomes the minimum exclusive
          annotation for the described datatype. See Value Constraints in [tabular-data-model]
          for details."'
      cdi:minimumValueInclusive:
        type: string
        description: 'A string denoting the minimum possible value. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.11.2: "minimum: An atomic property that contains a single number or string
          that is the minimum valid value (inclusive); equivalent to minInclusive.
          The value of this property becomes the minimum annotation for the described
          datatype. See Value Constraints in [tabular-data-model] for details."'
      cdi:regularExpression:
        $ref: '#/$defs/TypedString'
        description: A regular expression where strings matching the expression belong
          to the set of valid values. Use typeOfContent to specify the syntax of the
          regularExpression found in content.
    required:
    - '@type'
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-represented-variable/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-represented-variable/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-represented-variable/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiCDIFProperties/ddi-cdif-represented-variable`

