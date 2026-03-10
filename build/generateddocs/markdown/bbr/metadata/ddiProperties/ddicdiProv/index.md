
# DDI-CDI Provenance Activity (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiProv` *v0.1*

DDI-CDI native provenance activity for CDIF metadata, expressing workflows, agents, instruments, and methodology using DDI-CDI vocabulary (cdi:Activity, cdi:Step, cdi:ProcessingAgent). Defines properties: @type, @id, cdi:name, cdi:description, cdi:displayLabel, cdi:identifier, cdi:entityUsed, cdi:entityProduced, cdi:hasSubActivity, cdi:has_Step, cdi:standardModelMapping.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Example DDI-CDI provenance activity.
Soil chemistry analysis workflow expressed in DDI-CDI vocabulary.
Demonstrates Activity with entityUsed/entityProduced, Steps with
script and Parameters, ProcessingAgent, and ProductionEnvironment.
#### json
```json
{
    "@context": {
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "ex": "https://example.org/"
    },
    "@id": "ex:activity-soil-chem-analysis",
    "@type": "cdi:Activity",
    "cdi:name": {
        "@type": "cdi:ObjectName",
        "cdi:name": "Soil Chemistry Analysis - Great Basin Transect 2025"
    },
    "cdi:description": "Major and trace element analysis of soil samples collected along a 200 km transect across the Great Basin, using ICP-MS and XRF spectrometry with certified reference materials.",
    "cdi:displayLabel": {
        "@type": "cdi:LabelForDisplay",
        "cdi:languageSpecificString": {
            "@type": "cdi:LanguageString",
            "cdi:content": "GB Soil Chemistry 2025",
            "cdi:language": "en"
        }
    },
    "cdi:entityUsed": [
        {
            "@type": "cdi:Reference",
            "cdi:uri": "https://vocab.nerc.ac.uk/collection/L05/current/LAB02",
            "cdi:description": "NERC laboratory analysis technique vocabulary"
        },
        {
            "@type": "cdi:Reference",
            "cdi:description": "Soil core samples collected June 2025, sites GB-001 through GB-045"
        },
        {
            "@type": "cdi:Reference",
            "cdi:uri": "https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination",
            "cdi:description": "EPA Method 6200 - XRF Analysis of Soils"
        }
    ],
    "cdi:entityProduced": [
        {
            "@type": "cdi:Reference",
            "cdi:uri": "https://doi.org/10.5281/zenodo.example-soil-chem-gb-2025",
            "cdi:description": "Output dataset: Great Basin soil geochemistry results"
        }
    ],
    "cdi:has_Step": [
        {
            "@id": "ex:step-sample-prep",
            "@type": "cdi:Step",
            "cdi:name": {
                "@type": "cdi:ObjectName",
                "cdi:name": "Sample preparation and acid digestion"
            },
            "cdi:description": "Homogenize dried samples, split 0.5 g aliquots, digest with HNO3-HCl-HF mixture at 190 C in closed vessels.",
            "cdi:script": {
                "@type": "cdi:CommandCode",
                "cdi:commandFile": {
                    "@type": "cdi:CommandFile",
                    "cdi:uri": "https://www.epa.gov/hw-sw846/sw-846-test-method-3052-microwave-assisted-acid-digestion"
                }
            },
            "cdi:scriptingLanguage": {
                "@type": "cdi:ControlledVocabularyEntry",
                "cdi:entryValue": "Laboratory protocol"
            },
            "cdi:receives": [
                {
                    "@id": "ex:param-soil-samples",
                    "@type": "cdi:Parameter",
                    "cdi:name": {
                        "@type": "cdi:ObjectName",
                        "cdi:name": "Soil samples"
                    },
                    "cdi:entityBound": {
                        "@type": "cdi:Reference",
                        "cdi:description": "Dried and sieved soil samples (<2 mm fraction) from Great Basin transect, sites GB-001 through GB-045"
                    }
                }
            ],
            "cdi:produces": [
                {
                    "@id": "ex:param-digested-solutions",
                    "@type": "cdi:Parameter",
                    "cdi:name": {
                        "@type": "cdi:ObjectName",
                        "cdi:name": "Digested solutions"
                    },
                    "cdi:entityBound": {
                        "@type": "cdi:Reference",
                        "cdi:description": "Acid-digested soil solutions ready for ICP-MS analysis"
                    }
                }
            ]
        },
        {
            "@id": "ex:step-icpms-measurement",
            "@type": "cdi:Step",
            "cdi:name": {
                "@type": "cdi:ObjectName",
                "cdi:name": "ICP-MS measurement and calibration"
            },
            "cdi:description": "Analyze digested solutions by ICP-MS using external calibration with NIST SRM 2710a and 2711a as quality control standards.",
            "cdi:script": {
                "@type": "cdi:CommandCode",
                "cdi:commandFile": {
                    "@type": "cdi:CommandFile",
                    "cdi:uri": "https://www.epa.gov/hw-sw846/sw-846-test-method-6020b-inductively-coupled-plasma-mass-spectrometry"
                }
            },
            "cdi:scriptingLanguage": {
                "@type": "cdi:ControlledVocabularyEntry",
                "cdi:entryValue": "Instrumental method"
            },
            "cdi:receives": [
                {
                    "@id": "ex:param-digested-solutions"
                }
            ],
            "cdi:produces": [
                {
                    "@id": "ex:param-measurement-data",
                    "@type": "cdi:Parameter",
                    "cdi:name": {
                        "@type": "cdi:ObjectName",
                        "cdi:name": "Measurement data"
                    },
                    "cdi:entityBound": {
                        "@type": "cdi:Reference",
                        "cdi:uri": "https://doi.org/10.5281/zenodo.example-soil-chem-gb-2025",
                        "cdi:description": "Raw ICP-MS measurement data with element concentrations"
                    }
                }
            ]
        }
    ],
    "cdi:standardModelMapping": {
        "@type": "cdi:Reference",
        "cdi:uri": "https://statswiki.unece.org/display/GSBPM/GSBPM+v5.1",
        "cdi:description": "Generic Statistical Business Process Model v5.1"
    }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiProv/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:activity-soil-chem-analysis",
  "@type": "cdi:Activity",
  "cdi:name": {
    "@type": "cdi:ObjectName",
    "cdi:name": "Soil Chemistry Analysis - Great Basin Transect 2025"
  },
  "cdi:description": "Major and trace element analysis of soil samples collected along a 200 km transect across the Great Basin, using ICP-MS and XRF spectrometry with certified reference materials.",
  "cdi:displayLabel": {
    "@type": "cdi:LabelForDisplay",
    "cdi:languageSpecificString": {
      "@type": "cdi:LanguageString",
      "cdi:content": "GB Soil Chemistry 2025",
      "cdi:language": "en"
    }
  },
  "cdi:entityUsed": [
    {
      "@type": "cdi:Reference",
      "cdi:uri": "https://vocab.nerc.ac.uk/collection/L05/current/LAB02",
      "cdi:description": "NERC laboratory analysis technique vocabulary"
    },
    {
      "@type": "cdi:Reference",
      "cdi:description": "Soil core samples collected June 2025, sites GB-001 through GB-045"
    },
    {
      "@type": "cdi:Reference",
      "cdi:uri": "https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination",
      "cdi:description": "EPA Method 6200 - XRF Analysis of Soils"
    }
  ],
  "cdi:entityProduced": [
    {
      "@type": "cdi:Reference",
      "cdi:uri": "https://doi.org/10.5281/zenodo.example-soil-chem-gb-2025",
      "cdi:description": "Output dataset: Great Basin soil geochemistry results"
    }
  ],
  "cdi:has_Step": [
    {
      "@id": "ex:step-sample-prep",
      "@type": "cdi:Step",
      "cdi:name": {
        "@type": "cdi:ObjectName",
        "cdi:name": "Sample preparation and acid digestion"
      },
      "cdi:description": "Homogenize dried samples, split 0.5 g aliquots, digest with HNO3-HCl-HF mixture at 190 C in closed vessels.",
      "cdi:script": {
        "@type": "cdi:CommandCode",
        "cdi:commandFile": {
          "@type": "cdi:CommandFile",
          "cdi:uri": "https://www.epa.gov/hw-sw846/sw-846-test-method-3052-microwave-assisted-acid-digestion"
        }
      },
      "cdi:scriptingLanguage": {
        "@type": "cdi:ControlledVocabularyEntry",
        "cdi:entryValue": "Laboratory protocol"
      },
      "cdi:receives": [
        {
          "@id": "ex:param-soil-samples",
          "@type": "cdi:Parameter",
          "cdi:name": {
            "@type": "cdi:ObjectName",
            "cdi:name": "Soil samples"
          },
          "cdi:entityBound": {
            "@type": "cdi:Reference",
            "cdi:description": "Dried and sieved soil samples (<2 mm fraction) from Great Basin transect, sites GB-001 through GB-045"
          }
        }
      ],
      "cdi:produces": [
        {
          "@id": "ex:param-digested-solutions",
          "@type": "cdi:Parameter",
          "cdi:name": {
            "@type": "cdi:ObjectName",
            "cdi:name": "Digested solutions"
          },
          "cdi:entityBound": {
            "@type": "cdi:Reference",
            "cdi:description": "Acid-digested soil solutions ready for ICP-MS analysis"
          }
        }
      ]
    },
    {
      "@id": "ex:step-icpms-measurement",
      "@type": "cdi:Step",
      "cdi:name": {
        "@type": "cdi:ObjectName",
        "cdi:name": "ICP-MS measurement and calibration"
      },
      "cdi:description": "Analyze digested solutions by ICP-MS using external calibration with NIST SRM 2710a and 2711a as quality control standards.",
      "cdi:script": {
        "@type": "cdi:CommandCode",
        "cdi:commandFile": {
          "@type": "cdi:CommandFile",
          "cdi:uri": "https://www.epa.gov/hw-sw846/sw-846-test-method-6020b-inductively-coupled-plasma-mass-spectrometry"
        }
      },
      "cdi:scriptingLanguage": {
        "@type": "cdi:ControlledVocabularyEntry",
        "cdi:entryValue": "Instrumental method"
      },
      "cdi:receives": [
        {
          "@id": "ex:param-digested-solutions"
        }
      ],
      "cdi:produces": [
        {
          "@id": "ex:param-measurement-data",
          "@type": "cdi:Parameter",
          "cdi:name": {
            "@type": "cdi:ObjectName",
            "cdi:name": "Measurement data"
          },
          "cdi:entityBound": {
            "@type": "cdi:Reference",
            "cdi:uri": "https://doi.org/10.5281/zenodo.example-soil-chem-gb-2025",
            "cdi:description": "Raw ICP-MS measurement data with element concentrations"
          }
        }
      ]
    }
  ],
  "cdi:standardModelMapping": {
    "@type": "cdi:Reference",
    "cdi:uri": "https://statswiki.unece.org/display/GSBPM/GSBPM+v5.1",
    "cdi:description": "Generic Statistical Business Process Model v5.1"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .

ex:activity-soil-chem-analysis a cdi:Activity ;
    cdi:description "Major and trace element analysis of soil samples collected along a 200 km transect across the Great Basin, using ICP-MS and XRF spectrometry with certified reference materials." ;
    cdi:displayLabel [ a cdi:LabelForDisplay ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "GB Soil Chemistry 2025" ;
                    cdi:language "en" ] ] ;
    cdi:entityProduced [ a cdi:Reference ;
            cdi:description "Output dataset: Great Basin soil geochemistry results" ;
            cdi:uri "https://doi.org/10.5281/zenodo.example-soil-chem-gb-2025" ] ;
    cdi:entityUsed [ a cdi:Reference ;
            cdi:description "NERC laboratory analysis technique vocabulary" ;
            cdi:uri "https://vocab.nerc.ac.uk/collection/L05/current/LAB02" ],
        [ a cdi:Reference ;
            cdi:description "Soil core samples collected June 2025, sites GB-001 through GB-045" ],
        [ a cdi:Reference ;
            cdi:description "EPA Method 6200 - XRF Analysis of Soils" ;
            cdi:uri "https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination" ] ;
    cdi:has_Step ex:step-icpms-measurement,
        ex:step-sample-prep ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Soil Chemistry Analysis - Great Basin Transect 2025" ] ;
    cdi:standardModelMapping [ a cdi:Reference ;
            cdi:description "Generic Statistical Business Process Model v5.1" ;
            cdi:uri "https://statswiki.unece.org/display/GSBPM/GSBPM+v5.1" ] .

ex:param-measurement-data a cdi:Parameter ;
    cdi:entityBound [ a cdi:Reference ;
            cdi:description "Raw ICP-MS measurement data with element concentrations" ;
            cdi:uri "https://doi.org/10.5281/zenodo.example-soil-chem-gb-2025" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Measurement data" ] .

ex:param-soil-samples a cdi:Parameter ;
    cdi:entityBound [ a cdi:Reference ;
            cdi:description "Dried and sieved soil samples (<2 mm fraction) from Great Basin transect, sites GB-001 through GB-045" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Soil samples" ] .

ex:step-icpms-measurement a cdi:Step ;
    cdi:description "Analyze digested solutions by ICP-MS using external calibration with NIST SRM 2710a and 2711a as quality control standards." ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "ICP-MS measurement and calibration" ] ;
    cdi:produces ex:param-measurement-data ;
    cdi:receives ex:param-digested-solutions ;
    cdi:script [ a cdi:CommandCode ;
            cdi:commandFile [ a cdi:CommandFile ;
                    cdi:uri "https://www.epa.gov/hw-sw846/sw-846-test-method-6020b-inductively-coupled-plasma-mass-spectrometry" ] ] ;
    cdi:scriptingLanguage [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "Instrumental method" ] .

ex:step-sample-prep a cdi:Step ;
    cdi:description "Homogenize dried samples, split 0.5 g aliquots, digest with HNO3-HCl-HF mixture at 190 C in closed vessels." ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Sample preparation and acid digestion" ] ;
    cdi:produces ex:param-digested-solutions ;
    cdi:receives ex:param-soil-samples ;
    cdi:script [ a cdi:CommandCode ;
            cdi:commandFile [ a cdi:CommandFile ;
                    cdi:uri "https://www.epa.gov/hw-sw846/sw-846-test-method-3052-microwave-assisted-acid-digestion" ] ] ;
    cdi:scriptingLanguage [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "Laboratory protocol" ] .

ex:param-digested-solutions a cdi:Parameter ;
    cdi:entityBound [ a cdi:Reference ;
            cdi:description "Acid-digested soil solutions ready for ICP-MS analysis" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Digested solutions" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Provenance Activity
description: DDI-CDI native provenance activity. Describes workflows using cdi:Activity,
  cdi:Step, cdi:ProcessingAgent, and cdi:Parameter vocabulary from the DDI Cross-Domain
  Integration specification.
type: object
properties:
  '@type':
    description: Must be or include cdi:Activity
    anyOf:
    - type: string
      const: cdi:Activity
    - type: array
      items:
        type: string
      contains:
        const: cdi:Activity
  '@id':
    type: string
    description: Identifier for this activity node
  cdi:name:
    description: Structured name for the activity (ObjectName)
    anyOf:
    - $ref: '#/$defs/ObjectName'
    - type: array
      items:
        $ref: '#/$defs/ObjectName'
  cdi:description:
    type: string
    description: Plain text description of the activity
  cdi:displayLabel:
    description: Multilingual display label
    anyOf:
    - $ref: '#/$defs/LabelForDisplay'
    - type: array
      items:
        $ref: '#/$defs/LabelForDisplay'
  cdi:identifier:
    description: Formal identifier for this activity
    $ref: '#/$defs/Identifier'
  cdi:entityUsed:
    description: Entities used as inputs by this activity
    type: array
    items:
      $ref: '#/$defs/Reference'
  cdi:entityProduced:
    description: Entities produced as outputs by this activity
    type: array
    items:
      $ref: '#/$defs/Reference'
  cdi:hasSubActivity:
    description: Nested sub-activities within this activity (cdi:Activity). Use @id
      references to Activity nodes defined elsewhere in the graph.
    type: array
    items:
      $ref: '#/$defs/id-reference'
  cdi:has_Step:
    description: Ordered steps within this activity (cdi:Step)
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/Step'
      - $ref: '#/$defs/id-reference'
  cdi:standardModelMapping:
    description: Reference to a standard process model (e.g. GSBPM)
    anyOf:
    - $ref: '#/$defs/Reference'
    - type: array
      items:
        $ref: '#/$defs/Reference'
required:
- '@type'
- cdi:name
$defs:
  id-reference:
    type: object
    description: JSON-LD @id reference to a node defined elsewhere in the graph
    properties:
      '@id':
        type: string
        description: IRI or blank node identifier of the referenced node
    required:
    - '@id'
  ObjectName:
    type: object
    description: DDI-CDI structured name wrapper (dt-ObjectName)
    properties:
      '@type':
        type: string
        const: cdi:ObjectName
      cdi:name:
        type: string
        description: The name string
      cdi:context:
        description: Context or usage of this name
        $ref: '#/$defs/ControlledVocabularyEntry'
    required:
    - cdi:name
  LabelForDisplay:
    type: object
    description: DDI-CDI multilingual display label (dt-LabelForDisplay)
    properties:
      '@type':
        type: string
        const: cdi:LabelForDisplay
      cdi:locationVariant:
        description: Geographic or locale variant
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:maxLength:
        type: integer
        description: Maximum display length
      cdi:languageSpecificString:
        description: The label text with language tag
        $ref: '#/$defs/LanguageString'
  LanguageString:
    type: object
    description: DDI-CDI language-tagged string (dt-LanguageString)
    properties:
      '@type':
        type: string
        const: cdi:LanguageString
      cdi:content:
        type: string
        description: The text content
      cdi:language:
        type: string
        description: ISO language code (e.g. en, fr, de)
    required:
    - cdi:content
  Identifier:
    type: object
    description: DDI-CDI composite identifier (dt-Identifier)
    properties:
      '@type':
        type: string
        const: cdi:Identifier
      cdi:ddiIdentifier:
        description: DDI-specific IRDI identifier
        $ref: '#/$defs/InternationalRegistrationDataIdentifier'
      cdi:uri:
        type: string
        format: uri
        description: URI form of the identifier
      cdi:nonDdiIdentifier:
        description: Non-DDI identifier
        anyOf:
        - $ref: '#/$defs/NonDdiIdentifier'
        - type: array
          items:
            $ref: '#/$defs/NonDdiIdentifier'
  InternationalRegistrationDataIdentifier:
    type: object
    description: DDI-CDI IRDI (dt-InternationalRegistrationDataIdentifier)
    properties:
      '@type':
        type: string
        const: cdi:InternationalRegistrationDataIdentifier
      cdi:dataIdentifier:
        type: string
      cdi:registrationAuthorityIdentifier:
        type: string
      cdi:versionIdentifier:
        type: string
    required:
    - cdi:dataIdentifier
    - cdi:registrationAuthorityIdentifier
    - cdi:versionIdentifier
  NonDdiIdentifier:
    type: object
    description: Non-DDI identifier (dt-NonDdiIdentifier)
    properties:
      '@type':
        type: string
        const: cdi:NonDdiIdentifier
      cdi:identifierContent:
        type: string
        description: The identifier value
      cdi:managingAgency:
        type: string
        description: Agency managing this identifier scheme
    required:
    - cdi:identifierContent
  Reference:
    type: object
    description: DDI-CDI reference to an entity (dt-Reference)
    properties:
      '@type':
        type: string
        const: cdi:Reference
      cdi:uri:
        type: string
        format: uri
        description: URI of the referenced entity
      cdi:description:
        type: string
        description: Human-readable description of the reference
      cdi:ddiReference:
        description: DDI IRDI reference
        $ref: '#/$defs/InternationalRegistrationDataIdentifier'
      cdi:semantic:
        description: Semantic role of this reference
        $ref: '#/$defs/ControlledVocabularyEntry'
  Step:
    type: object
    description: DDI-CDI Step within an Activity (cls-Step, extends Activity)
    properties:
      '@type':
        type: string
        const: cdi:Step
      '@id':
        type: string
        description: Identifier for this step node
      cdi:name:
        description: Structured name for the step
        anyOf:
        - $ref: '#/$defs/ObjectName'
        - type: array
          items:
            $ref: '#/$defs/ObjectName'
      cdi:description:
        type: string
        description: Plain text description of the step
      cdi:identifier:
        $ref: '#/$defs/Identifier'
      cdi:script:
        description: Executable script or code for this step
        $ref: '#/$defs/CommandCode'
      cdi:scriptingLanguage:
        description: Programming or scripting language used
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:receives:
        description: Input parameters received by this step (cdi:Parameter)
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Parameter'
          - $ref: '#/$defs/id-reference'
      cdi:produces:
        description: Output parameters produced by this step (cdi:Parameter)
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Parameter'
          - $ref: '#/$defs/id-reference'
      cdi:entityUsed:
        description: Entities used as inputs by this step
        type: array
        items:
          $ref: '#/$defs/Reference'
      cdi:entityProduced:
        description: Entities produced as outputs by this step
        type: array
        items:
          $ref: '#/$defs/Reference'
      cdi:hasSubStep:
        description: Nested sub-steps (cdi:Step)
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Step'
          - $ref: '#/$defs/id-reference'
    required:
    - '@type'
    - cdi:name
  CommandCode:
    type: object
    description: DDI-CDI executable code reference (dt-CommandCode)
    properties:
      '@type':
        type: string
        const: cdi:CommandCode
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
        type: string
        const: cdi:Command
      cdi:commandContent:
        type: string
        description: The command or code text
      cdi:programLanguage:
        description: Language of this command
        $ref: '#/$defs/ControlledVocabularyEntry'
  CommandFile:
    type: object
    description: DDI-CDI external script file (dt-CommandFile)
    properties:
      '@type':
        type: string
        const: cdi:CommandFile
      cdi:uri:
        type: string
        format: uri
        description: URI of the script file
      cdi:location:
        type: string
        description: Human-readable file location
  ControlledVocabularyEntry:
    type: object
    description: DDI-CDI controlled vocabulary entry (dt-ControlledVocabularyEntry)
    properties:
      '@type':
        type: string
        const: cdi:ControlledVocabularyEntry
      cdi:entryValue:
        type: string
        description: The vocabulary code or value
      cdi:name:
        type: string
        description: Human-readable name
      cdi:vocabulary:
        description: Reference to the vocabulary scheme
        $ref: '#/$defs/Reference'
  Parameter:
    type: object
    description: DDI-CDI parameter for step data flow (cls-Parameter)
    properties:
      '@type':
        type: string
        const: cdi:Parameter
      '@id':
        type: string
        description: Identifier for this parameter node
      cdi:name:
        description: Structured name for the parameter
        anyOf:
        - $ref: '#/$defs/ObjectName'
        - type: array
          items:
            $ref: '#/$defs/ObjectName'
      cdi:identifier:
        $ref: '#/$defs/Identifier'
      cdi:entityBound:
        description: Reference to the entity this parameter is bound to
        anyOf:
        - $ref: '#/$defs/Reference'
        - type: array
          items:
            $ref: '#/$defs/Reference'
    required:
    - '@type'
    - cdi:name
  ProcessingAgent:
    type: object
    description: DDI-CDI agent that performs activities (cls-ProcessingAgent)
    properties:
      '@type':
        type: string
        const: cdi:ProcessingAgent
      '@id':
        type: string
        description: Identifier for this agent node
      cdi:identifier:
        $ref: '#/$defs/Identifier'
      cdi:purpose:
        type: string
        description: Purpose or role description of this agent
      cdi:performs:
        description: Activities this agent performs (cdi:Activity). Use @id references
          to Activity nodes defined elsewhere in the graph.
        type: array
        items:
          $ref: '#/$defs/id-reference'
      cdi:operatesOn:
        description: Production environments this agent operates on (cdi:ProductionEnvironment)
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ProductionEnvironment'
          - $ref: '#/$defs/id-reference'
    required:
    - '@type'
  ProductionEnvironment:
    type: object
    description: DDI-CDI production environment (cls-ProductionEnvironment)
    properties:
      '@type':
        type: string
        const: cdi:ProductionEnvironment
      '@id':
        type: string
        description: Identifier for this environment node
      cdi:name:
        description: Structured name for the environment
        anyOf:
        - $ref: '#/$defs/ObjectName'
        - type: array
          items:
            $ref: '#/$defs/ObjectName'
      cdi:description:
        type: string
        description: Description of the environment
      cdi:identifier:
        $ref: '#/$defs/Identifier'
      cdi:displayLabel:
        description: Multilingual display label
        anyOf:
        - $ref: '#/$defs/LabelForDisplay'
        - type: array
          items:
            $ref: '#/$defs/LabelForDisplay'
    required:
    - '@type'
    - cdi:name
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiProv/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiProv/schema.yaml)


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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiProv/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)
* [BBeuster EU-SoGreen-Prov Example](https://github.com/ddialliance/ddi-cdi_provenance-examples)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiProv`

