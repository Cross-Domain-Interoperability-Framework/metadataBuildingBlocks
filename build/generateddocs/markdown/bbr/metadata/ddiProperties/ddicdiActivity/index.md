
# DDI-CDI Activity (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiActivity` *v0.1*

DDI-CDI Activity class for CDIF metadata, describing tasks at a conceptual level using DDI-CDI vocabulary (cdi:Activity, cdi:Step, cdi:Parameter). Defines properties: @type, @id, cdi:name, cdi:description, cdi:definition, cdi:displayLabel, cdi:identifier, cdi:entityUsed, cdi:entityProduced, cdi:hasSubActivity, cdi:has_Step, cdi:standardModelMapping, cdi:start, cdi:end, cdi:hasInternal.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Example DDI-CDI activity.
Data processing activity expressed in DDI-CDI vocabulary.
Demonstrates Activity with entityUsed/entityProduced, Steps with
script and Parameters, start/end timestamps, and definition.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@graph": [
    {
      "@id": "ex:activity-statistical-compilation",
      "@type": [
        "cdi:Activity"
      ],
      "cdi:name": {
        "@type": [
          "cdi:ObjectName"
        ],
        "cdi:name": "Statistical data compilation - Regional Employment Survey 2025"
      },
      "cdi:description": "Compilation and harmonization of regional employment survey microdata from four national statistical offices, producing a cross-country comparable dataset.",
      "cdi:definition": {
        "@type": [
          "cdi:InternationalString"
        ],
        "cdi:languageSpecificString": [
          {
            "@type": [
              "cdi:LanguageString"
            ],
            "cdi:content": "A statistical data compilation activity that integrates employment survey microdata from multiple national sources into a harmonized cross-country dataset following GSBPM standards.",
            "cdi:language": "en"
          },
          {
            "@type": [
              "cdi:LanguageString"
            ],
            "cdi:content": "Une activite de compilation de donnees statistiques qui integre les microdonnees d'enquetes sur l'emploi de plusieurs sources nationales en un ensemble de donnees harmonise.",
            "cdi:language": "fr"
          }
        ]
      },
      "cdi:displayLabel": {
        "@type": [
          "cdi:LabelForDisplay"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Regional Employment Compilation 2025",
          "cdi:language": "en"
        }
      },
      "cdi:identifier": {
        "@type": [
          "cdi:Identifier"
        ],
        "cdi:uri": "https://example.org/activities/regional-employment-compilation-2025",
        "cdi:nonDdiIdentifier": {
          "@type": [
            "cdi:NonDdiIdentifier"
          ],
          "cdi:identifierContent": "REC-2025-001",
          "cdi:managingAgency": "Regional Statistical Consortium"
        }
      },
      "cdi:start": "2025-03-01T09:00:00Z",
      "cdi:end": "2025-06-15T17:00:00Z",
      "cdi:entityUsed": [
        {
          "@type": [
            "cdi:Reference"
          ],
          "cdi:uri": "https://example.org/datasets/national-lfs-2024-AT",
          "cdi:description": "Austrian Labour Force Survey 2024 microdata"
        },
        {
          "@type": [
            "cdi:Reference"
          ],
          "cdi:uri": "https://example.org/datasets/national-lfs-2024-DE",
          "cdi:description": "German Labour Force Survey 2024 microdata"
        },
        {
          "@type": [
            "cdi:Reference"
          ],
          "cdi:uri": "https://example.org/datasets/national-lfs-2024-CH",
          "cdi:description": "Swiss Labour Force Survey 2024 microdata"
        },
        {
          "@type": [
            "cdi:Reference"
          ],
          "cdi:uri": "https://example.org/datasets/national-lfs-2024-FR",
          "cdi:description": "French Labour Force Survey 2024 microdata"
        }
      ],
      "cdi:entityProduced": [
        {
          "@type": [
            "cdi:Reference"
          ],
          "cdi:uri": "https://doi.org/10.5281/zenodo.example-regional-employment-2025",
          "cdi:description": "Harmonized regional employment dataset 2025"
        }
      ],
      "cdi:standardModelMapping": {
        "@type": [
          "cdi:Reference"
        ],
        "cdi:uri": "https://statswiki.unece.org/display/GSBPM/GSBPM+v5.1",
        "cdi:description": "Generic Statistical Business Process Model v5.1 - Phase 5: Process",
        "cdi:semantic": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": "5",
          "cdi:name": "Process"
        }
      },
      "cdi:has_Step": [
        {
          "@id": "ex:step-variable-harmonization"
        },
        {
          "@id": "ex:step-data-integration"
        }
      ]
    },
    {
      "@id": "ex:step-variable-harmonization",
      "@type": [
        "cdi:Step"
      ],
      "cdi:name": {
        "@type": [
          "cdi:ObjectName"
        ],
        "cdi:name": "Variable harmonization and recoding"
      },
      "cdi:description": "Recode national variable classifications to common ISCO-08 occupation and ISCED-2011 education coding schemes.",
      "cdi:definition": {
        "@type": [
          "cdi:InternationalString"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Harmonization step that maps national occupation and education classification variables to international standards.",
          "cdi:language": "en"
        }
      },
      "cdi:start": "2025-03-15T09:00:00Z",
      "cdi:end": "2025-04-30T17:00:00Z",
      "cdi:script": {
        "@type": [
          "cdi:CommandCode"
        ],
        "cdi:description": "R script for variable recoding and harmonization",
        "cdi:commandFile": {
          "@type": [
            "cdi:CommandFile"
          ],
          "cdi:uri": "https://example.org/scripts/harmonize_variables.R",
          "cdi:location": "scripts/harmonize_variables.R"
        }
      },
      "cdi:scriptingLanguage": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": "R",
        "cdi:name": "R statistical language"
      },
      "cdi:receives": [
        {
          "@id": "ex:param-raw-microdata"
        }
      ],
      "cdi:produces": [
        {
          "@id": "ex:param-harmonized-variables"
        }
      ]
    },
    {
      "@id": "ex:step-data-integration",
      "@type": [
        "cdi:Step"
      ],
      "cdi:name": {
        "@type": [
          "cdi:ObjectName"
        ],
        "cdi:name": "Cross-country data integration"
      },
      "cdi:description": "Merge harmonized national datasets into a single cross-country file with consistent weighting and stratification variables.",
      "cdi:start": "2025-05-01T09:00:00Z",
      "cdi:end": "2025-06-15T17:00:00Z",
      "cdi:script": {
        "@type": [
          "cdi:CommandCode"
        ],
        "cdi:description": "Python script for dataset integration and weight calibration",
        "cdi:commandFile": {
          "@type": [
            "cdi:CommandFile"
          ],
          "cdi:uri": "https://example.org/scripts/integrate_datasets.py",
          "cdi:location": "scripts/integrate_datasets.py"
        }
      },
      "cdi:scriptingLanguage": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": "Python",
        "cdi:name": "Python programming language"
      },
      "cdi:receives": [
        {
          "@id": "ex:param-harmonized-variables"
        }
      ],
      "cdi:produces": [
        {
          "@id": "ex:param-integrated-dataset"
        }
      ]
    },
    {
      "@id": "ex:param-raw-microdata",
      "@type": [
        "cdi:Parameter"
      ],
      "cdi:name": {
        "@type": [
          "cdi:ObjectName"
        ],
        "cdi:name": "Raw national microdata"
      },
      "cdi:entityBound": {
        "@type": [
          "cdi:Reference"
        ],
        "cdi:description": "National labour force survey microdata files from AT, DE, CH, FR"
      }
    },
    {
      "@id": "ex:param-harmonized-variables",
      "@type": [
        "cdi:Parameter"
      ],
      "cdi:name": {
        "@type": [
          "cdi:ObjectName"
        ],
        "cdi:name": "Harmonized variables"
      },
      "cdi:entityBound": {
        "@type": [
          "cdi:Reference"
        ],
        "cdi:description": "National microdata with recoded occupation (ISCO-08) and education (ISCED-2011) variables"
      }
    },
    {
      "@id": "ex:param-integrated-dataset",
      "@type": [
        "cdi:Parameter"
      ],
      "cdi:name": {
        "@type": [
          "cdi:ObjectName"
        ],
        "cdi:name": "Integrated cross-country dataset"
      },
      "cdi:entityBound": {
        "@type": [
          "cdi:Reference"
        ],
        "cdi:uri": "https://doi.org/10.5281/zenodo.example-regional-employment-2025",
        "cdi:description": "Final harmonized and integrated regional employment dataset"
      }
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiActivity/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@graph": [
    {
      "@id": "ex:activity-statistical-compilation",
      "@type": [
        "cdi:Activity"
      ],
      "cdi:name": {
        "@type": [
          "cdi:ObjectName"
        ],
        "cdi:name": "Statistical data compilation - Regional Employment Survey 2025"
      },
      "cdi:description": "Compilation and harmonization of regional employment survey microdata from four national statistical offices, producing a cross-country comparable dataset.",
      "cdi:definition": {
        "@type": [
          "cdi:InternationalString"
        ],
        "cdi:languageSpecificString": [
          {
            "@type": [
              "cdi:LanguageString"
            ],
            "cdi:content": "A statistical data compilation activity that integrates employment survey microdata from multiple national sources into a harmonized cross-country dataset following GSBPM standards.",
            "cdi:language": "en"
          },
          {
            "@type": [
              "cdi:LanguageString"
            ],
            "cdi:content": "Une activite de compilation de donnees statistiques qui integre les microdonnees d'enquetes sur l'emploi de plusieurs sources nationales en un ensemble de donnees harmonise.",
            "cdi:language": "fr"
          }
        ]
      },
      "cdi:displayLabel": {
        "@type": [
          "cdi:LabelForDisplay"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Regional Employment Compilation 2025",
          "cdi:language": "en"
        }
      },
      "cdi:identifier": {
        "@type": [
          "cdi:Identifier"
        ],
        "cdi:uri": "https://example.org/activities/regional-employment-compilation-2025",
        "cdi:nonDdiIdentifier": {
          "@type": [
            "cdi:NonDdiIdentifier"
          ],
          "cdi:identifierContent": "REC-2025-001",
          "cdi:managingAgency": "Regional Statistical Consortium"
        }
      },
      "cdi:start": "2025-03-01T09:00:00Z",
      "cdi:end": "2025-06-15T17:00:00Z",
      "cdi:entityUsed": [
        {
          "@type": [
            "cdi:Reference"
          ],
          "cdi:uri": "https://example.org/datasets/national-lfs-2024-AT",
          "cdi:description": "Austrian Labour Force Survey 2024 microdata"
        },
        {
          "@type": [
            "cdi:Reference"
          ],
          "cdi:uri": "https://example.org/datasets/national-lfs-2024-DE",
          "cdi:description": "German Labour Force Survey 2024 microdata"
        },
        {
          "@type": [
            "cdi:Reference"
          ],
          "cdi:uri": "https://example.org/datasets/national-lfs-2024-CH",
          "cdi:description": "Swiss Labour Force Survey 2024 microdata"
        },
        {
          "@type": [
            "cdi:Reference"
          ],
          "cdi:uri": "https://example.org/datasets/national-lfs-2024-FR",
          "cdi:description": "French Labour Force Survey 2024 microdata"
        }
      ],
      "cdi:entityProduced": [
        {
          "@type": [
            "cdi:Reference"
          ],
          "cdi:uri": "https://doi.org/10.5281/zenodo.example-regional-employment-2025",
          "cdi:description": "Harmonized regional employment dataset 2025"
        }
      ],
      "cdi:standardModelMapping": {
        "@type": [
          "cdi:Reference"
        ],
        "cdi:uri": "https://statswiki.unece.org/display/GSBPM/GSBPM+v5.1",
        "cdi:description": "Generic Statistical Business Process Model v5.1 - Phase 5: Process",
        "cdi:semantic": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": "5",
          "cdi:name": "Process"
        }
      },
      "cdi:has_Step": [
        {
          "@id": "ex:step-variable-harmonization"
        },
        {
          "@id": "ex:step-data-integration"
        }
      ]
    },
    {
      "@id": "ex:step-variable-harmonization",
      "@type": [
        "cdi:Step"
      ],
      "cdi:name": {
        "@type": [
          "cdi:ObjectName"
        ],
        "cdi:name": "Variable harmonization and recoding"
      },
      "cdi:description": "Recode national variable classifications to common ISCO-08 occupation and ISCED-2011 education coding schemes.",
      "cdi:definition": {
        "@type": [
          "cdi:InternationalString"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Harmonization step that maps national occupation and education classification variables to international standards.",
          "cdi:language": "en"
        }
      },
      "cdi:start": "2025-03-15T09:00:00Z",
      "cdi:end": "2025-04-30T17:00:00Z",
      "cdi:script": {
        "@type": [
          "cdi:CommandCode"
        ],
        "cdi:description": "R script for variable recoding and harmonization",
        "cdi:commandFile": {
          "@type": [
            "cdi:CommandFile"
          ],
          "cdi:uri": "https://example.org/scripts/harmonize_variables.R",
          "cdi:location": "scripts/harmonize_variables.R"
        }
      },
      "cdi:scriptingLanguage": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": "R",
        "cdi:name": "R statistical language"
      },
      "cdi:receives": [
        {
          "@id": "ex:param-raw-microdata"
        }
      ],
      "cdi:produces": [
        {
          "@id": "ex:param-harmonized-variables"
        }
      ]
    },
    {
      "@id": "ex:step-data-integration",
      "@type": [
        "cdi:Step"
      ],
      "cdi:name": {
        "@type": [
          "cdi:ObjectName"
        ],
        "cdi:name": "Cross-country data integration"
      },
      "cdi:description": "Merge harmonized national datasets into a single cross-country file with consistent weighting and stratification variables.",
      "cdi:start": "2025-05-01T09:00:00Z",
      "cdi:end": "2025-06-15T17:00:00Z",
      "cdi:script": {
        "@type": [
          "cdi:CommandCode"
        ],
        "cdi:description": "Python script for dataset integration and weight calibration",
        "cdi:commandFile": {
          "@type": [
            "cdi:CommandFile"
          ],
          "cdi:uri": "https://example.org/scripts/integrate_datasets.py",
          "cdi:location": "scripts/integrate_datasets.py"
        }
      },
      "cdi:scriptingLanguage": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": "Python",
        "cdi:name": "Python programming language"
      },
      "cdi:receives": [
        {
          "@id": "ex:param-harmonized-variables"
        }
      ],
      "cdi:produces": [
        {
          "@id": "ex:param-integrated-dataset"
        }
      ]
    },
    {
      "@id": "ex:param-raw-microdata",
      "@type": [
        "cdi:Parameter"
      ],
      "cdi:name": {
        "@type": [
          "cdi:ObjectName"
        ],
        "cdi:name": "Raw national microdata"
      },
      "cdi:entityBound": {
        "@type": [
          "cdi:Reference"
        ],
        "cdi:description": "National labour force survey microdata files from AT, DE, CH, FR"
      }
    },
    {
      "@id": "ex:param-harmonized-variables",
      "@type": [
        "cdi:Parameter"
      ],
      "cdi:name": {
        "@type": [
          "cdi:ObjectName"
        ],
        "cdi:name": "Harmonized variables"
      },
      "cdi:entityBound": {
        "@type": [
          "cdi:Reference"
        ],
        "cdi:description": "National microdata with recoded occupation (ISCO-08) and education (ISCED-2011) variables"
      }
    },
    {
      "@id": "ex:param-integrated-dataset",
      "@type": [
        "cdi:Parameter"
      ],
      "cdi:name": {
        "@type": [
          "cdi:ObjectName"
        ],
        "cdi:name": "Integrated cross-country dataset"
      },
      "cdi:entityBound": {
        "@type": [
          "cdi:Reference"
        ],
        "cdi:uri": "https://doi.org/10.5281/zenodo.example-regional-employment-2025",
        "cdi:description": "Final harmonized and integrated regional employment dataset"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .

ex:activity-statistical-compilation a cdi:Activity ;
    cdi:definition [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "A statistical data compilation activity that integrates employment survey microdata from multiple national sources into a harmonized cross-country dataset following GSBPM standards." ;
                    cdi:language "en" ],
                [ a cdi:LanguageString ;
                    cdi:content "Une activite de compilation de donnees statistiques qui integre les microdonnees d'enquetes sur l'emploi de plusieurs sources nationales en un ensemble de donnees harmonise." ;
                    cdi:language "fr" ] ] ;
    cdi:description "Compilation and harmonization of regional employment survey microdata from four national statistical offices, producing a cross-country comparable dataset." ;
    cdi:displayLabel [ a cdi:LabelForDisplay ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Regional Employment Compilation 2025" ;
                    cdi:language "en" ] ] ;
    cdi:end "2025-06-15T17:00:00Z" ;
    cdi:entityProduced [ a cdi:Reference ;
            cdi:description "Harmonized regional employment dataset 2025" ;
            cdi:uri "https://doi.org/10.5281/zenodo.example-regional-employment-2025" ] ;
    cdi:entityUsed [ a cdi:Reference ;
            cdi:description "Austrian Labour Force Survey 2024 microdata" ;
            cdi:uri "https://example.org/datasets/national-lfs-2024-AT" ],
        [ a cdi:Reference ;
            cdi:description "French Labour Force Survey 2024 microdata" ;
            cdi:uri "https://example.org/datasets/national-lfs-2024-FR" ],
        [ a cdi:Reference ;
            cdi:description "Swiss Labour Force Survey 2024 microdata" ;
            cdi:uri "https://example.org/datasets/national-lfs-2024-CH" ],
        [ a cdi:Reference ;
            cdi:description "German Labour Force Survey 2024 microdata" ;
            cdi:uri "https://example.org/datasets/national-lfs-2024-DE" ] ;
    cdi:has_Step ex:step-data-integration,
        ex:step-variable-harmonization ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:nonDdiIdentifier [ a cdi:NonDdiIdentifier ;
                    cdi:identifierContent "REC-2025-001" ;
                    cdi:managingAgency "Regional Statistical Consortium" ] ;
            cdi:uri "https://example.org/activities/regional-employment-compilation-2025" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Statistical data compilation - Regional Employment Survey 2025" ] ;
    cdi:standardModelMapping [ a cdi:Reference ;
            cdi:description "Generic Statistical Business Process Model v5.1 - Phase 5: Process" ;
            cdi:semantic [ a cdi:ControlledVocabularyEntry ;
                    cdi:entryValue "5" ;
                    cdi:name "Process" ] ;
            cdi:uri "https://statswiki.unece.org/display/GSBPM/GSBPM+v5.1" ] ;
    cdi:start "2025-03-01T09:00:00Z" .

ex:param-integrated-dataset a cdi:Parameter ;
    cdi:entityBound [ a cdi:Reference ;
            cdi:description "Final harmonized and integrated regional employment dataset" ;
            cdi:uri "https://doi.org/10.5281/zenodo.example-regional-employment-2025" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Integrated cross-country dataset" ] .

ex:param-raw-microdata a cdi:Parameter ;
    cdi:entityBound [ a cdi:Reference ;
            cdi:description "National labour force survey microdata files from AT, DE, CH, FR" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Raw national microdata" ] .

ex:step-data-integration a cdi:Step ;
    cdi:description "Merge harmonized national datasets into a single cross-country file with consistent weighting and stratification variables." ;
    cdi:end "2025-06-15T17:00:00Z" ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Cross-country data integration" ] ;
    cdi:produces ex:param-integrated-dataset ;
    cdi:receives ex:param-harmonized-variables ;
    cdi:script [ a cdi:CommandCode ;
            cdi:commandFile [ a cdi:CommandFile ;
                    cdi:location "scripts/integrate_datasets.py" ;
                    cdi:uri "https://example.org/scripts/integrate_datasets.py" ] ;
            cdi:description "Python script for dataset integration and weight calibration" ] ;
    cdi:scriptingLanguage [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "Python" ;
            cdi:name "Python programming language" ] ;
    cdi:start "2025-05-01T09:00:00Z" .

ex:step-variable-harmonization a cdi:Step ;
    cdi:definition [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Harmonization step that maps national occupation and education classification variables to international standards." ;
                    cdi:language "en" ] ] ;
    cdi:description "Recode national variable classifications to common ISCO-08 occupation and ISCED-2011 education coding schemes." ;
    cdi:end "2025-04-30T17:00:00Z" ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Variable harmonization and recoding" ] ;
    cdi:produces ex:param-harmonized-variables ;
    cdi:receives ex:param-raw-microdata ;
    cdi:script [ a cdi:CommandCode ;
            cdi:commandFile [ a cdi:CommandFile ;
                    cdi:location "scripts/harmonize_variables.R" ;
                    cdi:uri "https://example.org/scripts/harmonize_variables.R" ] ;
            cdi:description "R script for variable recoding and harmonization" ] ;
    cdi:scriptingLanguage [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "R" ;
            cdi:name "R statistical language" ] ;
    cdi:start "2025-03-15T09:00:00Z" .

ex:param-harmonized-variables a cdi:Parameter ;
    cdi:entityBound [ a cdi:Reference ;
            cdi:description "National microdata with recoded occupation (ISCO-08) and education (ISCED-2011) variables" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Harmonized variables" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Activity
description: DDI-CDI Activity class (DDICDILibrary/Classes/Process/Activity). Describes
  tasks at a conceptual level using cdi:Activity, cdi:Step, and cdi:Parameter vocabulary
  from the DDI Cross-Domain Integration specification. Includes definition, start/end
  timestamps, hasInternal (ControlLogic), and full Step/Parameter support.
anyOf:
- description: Single Activity node
  $ref: '#/$defs/Activity'
- description: Unwrapped @graph array of nodes (OGC pipeline)
  type: array
  contains:
    $ref: '#/$defs/Activity'
  items:
    if:
      type: object
      properties:
        '@type':
          type: array
          contains:
            const: cdi:Activity
      required:
      - '@type'
    then:
      $ref: '#/$defs/Activity'
- description: JSON-LD document with @context and @graph
  type: object
  properties:
    '@context': {}
    '@graph':
      type: array
      contains:
        $ref: '#/$defs/Activity'
      items:
        if:
          type: object
          properties:
            '@type':
              type: array
              contains:
                const: cdi:Activity
          required:
          - '@type'
        then:
          $ref: '#/$defs/Activity'
  required:
  - '@graph'
$defs:
  Activity:
    type: object
    description: "DDI-CDI Activity (cls-Activity) \u2014 task described at a conceptual
      level"
    properties:
      '@type':
        description: Must be or include cdi:Activity
        type: array
        items:
          type: string
        contains:
          const: cdi:Activity
        minItems: 1
      '@id':
        type: string
        description: Identifier for this activity node
      cdi:name:
        description: Structured name for the activity (ObjectName)
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        - type: array
          items:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
      cdi:description:
        type: string
        description: Plain text description of the activity
      cdi:definition:
        description: Formal multilingual definition (InternationalString)
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        - type: array
          items:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
      cdi:displayLabel:
        description: Multilingual display label
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        - type: array
          items:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
      cdi:identifier:
        description: Formal identifier for this activity
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
      cdi:entityUsed:
        description: Entities used as inputs by this activity
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
      cdi:entityProduced:
        description: Entities produced as outputs by this activity
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
      cdi:standardModelMapping:
        description: Reference to a standard process model (e.g. GSBPM)
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        - type: array
          items:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
      cdi:start:
        type: string
        format: date-time
        description: Start date-time of the activity (xsd:dateTime)
      cdi:end:
        type: string
        format: date-time
        description: End date-time of the activity (xsd:dateTime)
      cdi:hasSubActivity:
        description: Nested sub-activities (cdi:Activity). @id references.
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:has_Step:
        description: Ordered steps within this activity (cdi:Step)
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Step'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:hasInternal:
        description: Internal control logic elements (cdi:ControlLogic). @id references.
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    required:
    - '@type'
    - cdi:name
  Step:
    type: object
    description: DDI-CDI Step within an Activity (cls-Step, extends Activity)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Step
        minItems: 1
      '@id':
        type: string
        description: Identifier for this step node
      cdi:name:
        description: Structured name for the step
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        - type: array
          items:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
      cdi:description:
        type: string
        description: Plain text description of the step
      cdi:definition:
        description: Formal multilingual definition (InternationalString)
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        - type: array
          items:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
      cdi:start:
        type: string
        format: date-time
        description: Start date-time of the step (xsd:dateTime)
      cdi:end:
        type: string
        format: date-time
        description: End date-time of the step (xsd:dateTime)
      cdi:script:
        description: Executable script or code for this step
        $ref: '#/$defs/CommandCode'
      cdi:scriptingLanguage:
        description: Programming or scripting language used
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
      cdi:receives:
        description: Input parameters received by this step (cdi:Parameter)
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Parameter'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:produces:
        description: Output parameters produced by this step (cdi:Parameter)
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Parameter'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:entityUsed:
        description: Entities used as inputs by this step
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
      cdi:entityProduced:
        description: Entities produced as outputs by this step
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
      cdi:hasSubStep:
        description: Nested sub-steps (cdi:Step)
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Step'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    required:
    - '@type'
    - cdi:name
  CommandCode:
    type: object
    description: DDI-CDI executable code reference (dt-CommandCode)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:CommandCode
        minItems: 1
      cdi:description:
        type: string
        description: Description of the code
      cdi:commandFile:
        description: External script file reference
        anyOf:
        - $ref: '#/$defs/CommandFile'
        - type: array
          items:
            $ref: '#/$defs/CommandFile'
      cdi:command:
        description: Inline command content
        anyOf:
        - $ref: '#/$defs/Command'
        - type: array
          items:
            $ref: '#/$defs/Command'
  Command:
    type: object
    description: DDI-CDI individual command statement (dt-Command)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Command
        minItems: 1
      cdi:commandContent:
        type: string
        description: The command or code text
      cdi:programLanguage:
        description: Language of this command
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
  CommandFile:
    type: object
    description: DDI-CDI external script file (dt-CommandFile)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:CommandFile
        minItems: 1
      cdi:uri:
        type: string
        format: uri
        description: URI of the script file
      cdi:location:
        type: string
        description: Human-readable file location
  Parameter:
    type: object
    description: DDI-CDI parameter for step data flow (cls-Parameter)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Parameter
        minItems: 1
      '@id':
        type: string
        description: Identifier for this parameter node
      cdi:name:
        description: Structured name for the parameter
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        - type: array
          items:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
      cdi:entityBound:
        description: Reference to the entity this parameter is bound to
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        - type: array
          items:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
    required:
    - '@type'
    - cdi:name
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiActivity/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiActivity/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiActivity/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiActivity`

