
# DDI-CDI Activity (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiActivity` *v0.1*

DDI-CDI Activity class for CDIF metadata, describing tasks at a conceptual level using DDI-CDI vocabulary (cdi:Activity, cdi:Step, cdi:Parameter). Defines properties: @type, @id, cdi:name, cdi:description, cdi:definition, cdi:displayLabel, cdi:identifier, cdi:entityUsed, cdi:entityProduced, cdi:hasSubActivity, cdi:has_Step, cdi:standardModelMapping, cdi:start, cdi:end, cdi:hasInternal.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI Activity describes a task or process at the conceptual level, using the `cdi:Activity`, `cdi:Step`, and `cdi:Parameter` vocabulary from the DDI Cross-Domain Integration specification (DDICDILibrary/Classes/Process). An activity carries a structured name, definition, optional start/end timestamps, and may decompose into nested sub-activities (`cdi:hasSubActivity`) or ordered `cdi:Step` items via `cdi:has_Step`.

Each step may receive and produce `cdi:Parameter` items (`cdi:receives`, `cdi:produces`), reference executable code via `cdi:script` (`cdi:CommandCode`, `cdi:CommandFile`, `cdi:Command`), and capture inputs and outputs through `cdi:entityUsed` and `cdi:entityProduced`. Activities can also be aligned to standard process models such as GSBPM via `cdi:standardModelMapping`, and linked to internal control logic through `cdi:hasInternal`. The BB is used wherever the provenance, processing chain, or transformation history of data needs to be described in machine-actionable form.

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
      "cdi:entryValue": [
        "5"
      ],
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
      "cdi:entryValue": [
        "5"
      ],
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
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .

ex:activity-statistical-compilation a cdi:Activity ;
    cdi:definition [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Une activite de compilation de donnees statistiques qui integre les microdonnees d'enquetes sur l'emploi de plusieurs sources nationales en un ensemble de donnees harmonise." ;
                    cdi:language "fr" ],
                [ a cdi:LanguageString ;
                    cdi:content "A statistical data compilation activity that integrates employment survey microdata from multiple national sources into a harmonized cross-country dataset following GSBPM standards." ;
                    cdi:language "en" ] ] ;
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
            cdi:description "French Labour Force Survey 2024 microdata" ;
            cdi:uri "https://example.org/datasets/national-lfs-2024-FR" ],
        [ a cdi:Reference ;
            cdi:description "Austrian Labour Force Survey 2024 microdata" ;
            cdi:uri "https://example.org/datasets/national-lfs-2024-AT" ],
        [ a cdi:Reference ;
            cdi:description "German Labour Force Survey 2024 microdata" ;
            cdi:uri "https://example.org/datasets/national-lfs-2024-DE" ],
        [ a cdi:Reference ;
            cdi:description "Swiss Labour Force Survey 2024 microdata" ;
            cdi:uri "https://example.org/datasets/national-lfs-2024-CH" ] ;
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


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Activity
description: DDI-CDI Activity class (DDICDILibrary/Classes/Process/Activity). Describes
  tasks at a conceptual level using cdi:Activity, cdi:Step, and cdi:Parameter vocabulary
  from the DDI Cross-Domain Integration specification. Includes definition, start/end
  timestamps, hasInternal (ControlLogic), and full Step/Parameter support.
type: object
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
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
  cdi:description:
    type: string
    description: Plain text description of the activity
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/description
  cdi:definition:
    description: Formal multilingual definition (InternationalString)
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    - type: array
      items:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/definition
  cdi:displayLabel:
    description: Multilingual display label
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
    - type: array
      items:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
  cdi:identifier:
    description: Formal identifier for this activity
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
  cdi:entityUsed:
    description: Entities used as inputs by this activity
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/entityUsed
  cdi:entityProduced:
    description: Entities produced as outputs by this activity
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/entityProduced
  cdi:standardModelMapping:
    description: Reference to a standard process model (e.g. GSBPM)
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
    - type: array
      items:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/standardModelMapping
  cdi:start:
    type: string
    format: date-time
    description: Start date-time of the activity (xsd:dateTime)
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/start
  cdi:end:
    type: string
    format: date-time
    description: End date-time of the activity (xsd:dateTime)
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/end
  cdi:hasSubActivity:
    description: Nested sub-activities (cdi:Activity). @id references.
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasSubActivity
  cdi:has_Step:
    description: Ordered steps within this activity (cdi:Step)
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/Step'
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_Step
  cdi:hasInternal:
    description: Internal control logic elements (cdi:ControlLogic). @id references.
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasInternal
required:
- '@type'
- cdi:name
$defs:
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:description:
        type: string
        description: Plain text description of the step
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/description
      cdi:definition:
        description: Formal multilingual definition (InternationalString)
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        - type: array
          items:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/definition
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:start:
        type: string
        format: date-time
        description: Start date-time of the step (xsd:dateTime)
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/start
      cdi:end:
        type: string
        format: date-time
        description: End date-time of the step (xsd:dateTime)
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/end
      cdi:script:
        description: Executable script or code for this step
        $ref: '#/$defs/CommandCode'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/script
      cdi:scriptingLanguage:
        description: Programming or scripting language used
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/scriptingLanguage
      cdi:receives:
        description: Input parameters received by this step (cdi:Parameter)
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Parameter'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/receives
      cdi:produces:
        description: Output parameters produced by this step (cdi:Parameter)
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Parameter'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/produces
      cdi:entityUsed:
        description: Entities used as inputs by this step
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/entityUsed
      cdi:entityProduced:
        description: Entities produced as outputs by this step
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/entityProduced
      cdi:hasSubStep:
        description: Nested sub-steps (cdi:Step)
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Step'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasSubStep
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/description
      cdi:commandFile:
        description: External script file reference
        anyOf:
        - $ref: '#/$defs/CommandFile'
        - type: array
          items:
            $ref: '#/$defs/CommandFile'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/commandFile
      cdi:command:
        description: Inline command content
        anyOf:
        - $ref: '#/$defs/Command'
        - type: array
          items:
            $ref: '#/$defs/Command'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/command
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/commandContent
      cdi:programLanguage:
        description: Language of this command
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/programLanguage
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uri
      cdi:location:
        type: string
        description: Human-readable file location
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/location
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:entityBound:
        description: Reference to the entity this parameter is bound to
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        - type: array
          items:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/entityBound
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

