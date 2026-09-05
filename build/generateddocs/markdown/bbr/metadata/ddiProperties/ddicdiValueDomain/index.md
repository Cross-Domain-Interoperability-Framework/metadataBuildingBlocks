
# DDI-CDI Value Domain (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiValueDomain` *v0.1*

DDI-CDI ValueDomain building block for CDIF metadata, covering both SubstantiveValueDomain (subject-matter values) and SentinelValueDomain (processing/missing-value codes). Inherits from ValueDomain. Defines properties: @type, @id, cdi:catalogDetails, cdi:displayLabel, cdi:identifier, cdi:recommendedDataType, cdi:isDescribedBy, cdi:takesValuesFrom, cdi:takesConceptsFrom, cdi:platformType (sentinel only).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI ValueDomain describes the allowed values for a variable, either as an enumeration or a formal description. Polymorphic root over `cdi:SubstantiveValueDomain` (the set of values of substantive interest), `cdi:SentinelValueDomain` (sentinel/missing-value codes), and `cdi:DescriptorValueDomain` (values used as variable descriptors).

Each variant carries `cdi:takesValuesFrom` referencing a `ddicdiEnumerationDomain` (where the values are enumerated) and/or `cdi:isDescribedBy` referencing a local `ValueAndConceptDescription` (where the values are characterized by classification level, format pattern, regular expression, min/max, etc.). Substantive and sentinel variants additionally link to a conceptual domain via `cdi:takesConceptsFrom`. ValueDomain is the value-set anchor referenced from `ddicdiRepresentedVariable`, `ddicdiInstanceVariable`, and `ddicdiDataStructureComponent` (`DimensionComponent.cdi:isStructuredBy`) in the CDIF Data Description profile.

## Examples

### Example DDI-CDI value domains (substantive and sentinel).
Two value domains for a height variable: a SubstantiveValueDomain
with a described numeric domain (0-3 meters, Ratio level), and a
SentinelValueDomain with missing value codes for the SAS platform.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@type": [
    "cdi:SubstantiveValueDomain"
  ],
  "@id": "ex:vd/temperatureCelsius",
  "cdi:identifier": {
    "@type": [
      "cdi:Identifier"
    ],
    "cdi:uri": "https://example.org/vd/temperatureCelsius",
    "cdi:ddiIdentifier": {
      "@type": [
        "cdi:InternationalRegistrationDataIdentifier"
      ],
      "cdi:dataIdentifier": "OCEAN-VD-TEMP-C",
      "cdi:registrationAuthorityIdentifier": "0000.0000.0000",
      "cdi:versionIdentifier": "1.0.0"
    },
    "cdi:nonDdiIdentifier": [
      {
        "@type": [
          "cdi:NonDdiIdentifier"
        ],
        "cdi:identifierContent": "VD/TEMP-C/v1",
        "cdi:managingAgency": "Example Ocean Data Center"
      }
    ]
  },
  "cdi:displayLabel": [
    {
      "@type": [
        "cdi:LabelForDisplay"
      ],
      "cdi:maxLength": 40,
      "cdi:locationVariant": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "en-US"
        ],
        "cdi:name": "BCP47"
      },
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Sea Water Temperature (degrees Celsius)",
        "cdi:language": "en"
      }
    },
    {
      "@type": [
        "cdi:LabelForDisplay"
      ],
      "cdi:maxLength": 60,
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Temperatura del agua de mar (grados Celsius)",
        "cdi:language": "es"
      }
    }
  ],
  "cdi:recommendedDataType": [
    {
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
            "cdi:Reference"
          ],
          "cdi:uri": "http://www.w3.org/2001/XMLSchema#decimal"
        }
      ],
      "cdi:vocabulary": {
        "@type": [
          "cdi:Reference"
        ],
        "cdi:uri": "http://www.w3.org/2001/XMLSchema",
        "cdi:description": "W3C XML Schema Definition Language datatypes"
      }
    },
    {
      "@type": [
        "cdi:ControlledVocabularyEntry"
      ],
      "cdi:entryValue": [
        "xsd:double"
      ],
      "cdi:name": "XML Schema Datatypes",
      "cdi:entryReference": [
        {
          "@type": [
            "cdi:Reference"
          ],
          "cdi:uri": "http://www.w3.org/2001/XMLSchema#double"
        }
      ]
    }
  ],
  "cdi:isDescribedBy": {
    "@type": [
      "cdi:ValueAndConceptDescription"
    ],
    "@id": "ex:vd/temperatureCelsius/desc",
    "cdi:classificationLevel": "Continuous",
    "cdi:description": {
      "@type": [
        "cdi:InternationalString"
      ],
      "cdi:languageSpecificString": [
        {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Real-valued sea water temperatures, expressed in degrees Celsius, in the plausible oceanographic range from -2 (freezing seawater) up to 35.5 (warm tropical surface).",
          "cdi:language": "en"
        },
        {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Temperatures du seuil oceanographique en degres Celsius.",
          "cdi:language": "fr"
        }
      ]
    },
    "cdi:formatPattern": {
      "@type": [
        "cdi:ControlledVocabularyEntry"
      ],
      "cdi:entryValue": [
        "#0.00"
      ],
      "cdi:name": "LDML number pattern",
      "cdi:vocabulary": {
        "@type": [
          "cdi:Reference"
        ],
        "cdi:uri": "http://www.unicode.org/reports/tr35/tr35-numbers.html#Number_Format_Patterns"
      }
    },
    "cdi:logicalExpression": {
      "@type": [
        "cdi:ControlledVocabularyEntry"
      ],
      "cdi:entryValue": [
        "all reals x such that -2 <= x <= 35.5"
      ],
      "cdi:name": "informal range expression"
    },
    "cdi:identifier": {
      "@type": [
        "cdi:Identifier"
      ],
      "cdi:uri": "https://example.org/vd/temperatureCelsius/desc"
    },
    "cdi:minimumValueInclusive": "-2.0",
    "cdi:maximumValueInclusive": "35.5",
    "cdi:minimumValueExclusive": "-3.0",
    "cdi:maximumValueExclusive": "40.0",
    "cdi:regularExpression": {
      "@type": [
        "cdi:TypedString"
      ],
      "cdi:content": "^-?\\d+(\\.\\d+)?$",
      "cdi:typeOfContent": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "ECMAScript"
        ],
        "cdi:name": "regex syntax"
      }
    }
  },
  "cdi:takesConceptsFrom": {
    "@type": [
      "cdi:SubstantiveConceptualDomain"
    ],
    "@id": "ex:cd/seaWaterTemperature",
    "cdi:displayLabel": [
      {
        "@type": [
          "cdi:LabelForDisplay"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Sea Water Temperature (concept)",
          "cdi:language": "en"
        }
      }
    ],
    "cdi:identifier": {
      "@type": [
        "cdi:Identifier"
      ],
      "cdi:uri": "https://example.org/cd/seaWaterTemperature"
    },
    "cdi:isDescribedBy": {
      "@id": "ex:vd/temperatureCelsius/desc"
    },
    "cdi:takesConceptsFrom": {
      "@id": "ex:cs/oceanographicConcepts"
    }
  },
  "cdi:takesValuesFrom": {
    "@id": "ex:enum/temperatureSampleEnum"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiValueDomain/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:SubstantiveValueDomain"
  ],
  "@id": "ex:vd/temperatureCelsius",
  "cdi:identifier": {
    "@type": [
      "cdi:Identifier"
    ],
    "cdi:uri": "https://example.org/vd/temperatureCelsius",
    "cdi:ddiIdentifier": {
      "@type": [
        "cdi:InternationalRegistrationDataIdentifier"
      ],
      "cdi:dataIdentifier": "OCEAN-VD-TEMP-C",
      "cdi:registrationAuthorityIdentifier": "0000.0000.0000",
      "cdi:versionIdentifier": "1.0.0"
    },
    "cdi:nonDdiIdentifier": [
      {
        "@type": [
          "cdi:NonDdiIdentifier"
        ],
        "cdi:identifierContent": "VD/TEMP-C/v1",
        "cdi:managingAgency": "Example Ocean Data Center"
      }
    ]
  },
  "cdi:displayLabel": [
    {
      "@type": [
        "cdi:LabelForDisplay"
      ],
      "cdi:maxLength": 40,
      "cdi:locationVariant": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "en-US"
        ],
        "cdi:name": "BCP47"
      },
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Sea Water Temperature (degrees Celsius)",
        "cdi:language": "en"
      }
    },
    {
      "@type": [
        "cdi:LabelForDisplay"
      ],
      "cdi:maxLength": 60,
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Temperatura del agua de mar (grados Celsius)",
        "cdi:language": "es"
      }
    }
  ],
  "cdi:recommendedDataType": [
    {
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
            "cdi:Reference"
          ],
          "cdi:uri": "http://www.w3.org/2001/XMLSchema#decimal"
        }
      ],
      "cdi:vocabulary": {
        "@type": [
          "cdi:Reference"
        ],
        "cdi:uri": "http://www.w3.org/2001/XMLSchema",
        "cdi:description": "W3C XML Schema Definition Language datatypes"
      }
    },
    {
      "@type": [
        "cdi:ControlledVocabularyEntry"
      ],
      "cdi:entryValue": [
        "xsd:double"
      ],
      "cdi:name": "XML Schema Datatypes",
      "cdi:entryReference": [
        {
          "@type": [
            "cdi:Reference"
          ],
          "cdi:uri": "http://www.w3.org/2001/XMLSchema#double"
        }
      ]
    }
  ],
  "cdi:isDescribedBy": {
    "@type": [
      "cdi:ValueAndConceptDescription"
    ],
    "@id": "ex:vd/temperatureCelsius/desc",
    "cdi:classificationLevel": "Continuous",
    "cdi:description": {
      "@type": [
        "cdi:InternationalString"
      ],
      "cdi:languageSpecificString": [
        {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Real-valued sea water temperatures, expressed in degrees Celsius, in the plausible oceanographic range from -2 (freezing seawater) up to 35.5 (warm tropical surface).",
          "cdi:language": "en"
        },
        {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Temperatures du seuil oceanographique en degres Celsius.",
          "cdi:language": "fr"
        }
      ]
    },
    "cdi:formatPattern": {
      "@type": [
        "cdi:ControlledVocabularyEntry"
      ],
      "cdi:entryValue": [
        "#0.00"
      ],
      "cdi:name": "LDML number pattern",
      "cdi:vocabulary": {
        "@type": [
          "cdi:Reference"
        ],
        "cdi:uri": "http://www.unicode.org/reports/tr35/tr35-numbers.html#Number_Format_Patterns"
      }
    },
    "cdi:logicalExpression": {
      "@type": [
        "cdi:ControlledVocabularyEntry"
      ],
      "cdi:entryValue": [
        "all reals x such that -2 <= x <= 35.5"
      ],
      "cdi:name": "informal range expression"
    },
    "cdi:identifier": {
      "@type": [
        "cdi:Identifier"
      ],
      "cdi:uri": "https://example.org/vd/temperatureCelsius/desc"
    },
    "cdi:minimumValueInclusive": "-2.0",
    "cdi:maximumValueInclusive": "35.5",
    "cdi:minimumValueExclusive": "-3.0",
    "cdi:maximumValueExclusive": "40.0",
    "cdi:regularExpression": {
      "@type": [
        "cdi:TypedString"
      ],
      "cdi:content": "^-?\\d+(\\.\\d+)?$",
      "cdi:typeOfContent": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "ECMAScript"
        ],
        "cdi:name": "regex syntax"
      }
    }
  },
  "cdi:takesConceptsFrom": {
    "@type": [
      "cdi:SubstantiveConceptualDomain"
    ],
    "@id": "ex:cd/seaWaterTemperature",
    "cdi:displayLabel": [
      {
        "@type": [
          "cdi:LabelForDisplay"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Sea Water Temperature (concept)",
          "cdi:language": "en"
        }
      }
    ],
    "cdi:identifier": {
      "@type": [
        "cdi:Identifier"
      ],
      "cdi:uri": "https://example.org/cd/seaWaterTemperature"
    },
    "cdi:isDescribedBy": {
      "@id": "ex:vd/temperatureCelsius/desc"
    },
    "cdi:takesConceptsFrom": {
      "@id": "ex:cs/oceanographicConcepts"
    }
  },
  "cdi:takesValuesFrom": {
    "@id": "ex:enum/temperatureSampleEnum"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/vd/temperatureCelsius> a cdi:SubstantiveValueDomain ;
    cdi:displayLabel [ a cdi:LabelForDisplay ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Sea Water Temperature (degrees Celsius)" ;
                    cdi:language "en" ] ;
            cdi:locationVariant [ a cdi:ControlledVocabularyEntry ;
                    cdi:entryValue "en-US" ;
                    cdi:name "BCP47" ] ;
            cdi:maxLength 40 ],
        [ a cdi:LabelForDisplay ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Temperatura del agua de mar (grados Celsius)" ;
                    cdi:language "es" ] ;
            cdi:maxLength 60 ] ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:ddiIdentifier [ a cdi:InternationalRegistrationDataIdentifier ;
                    cdi:dataIdentifier "OCEAN-VD-TEMP-C" ;
                    cdi:registrationAuthorityIdentifier "0000.0000.0000" ;
                    cdi:versionIdentifier "1.0.0" ] ;
            cdi:nonDdiIdentifier [ a cdi:NonDdiIdentifier ;
                    cdi:identifierContent "VD/TEMP-C/v1" ;
                    cdi:managingAgency "Example Ocean Data Center" ] ;
            cdi:uri "https://example.org/vd/temperatureCelsius" ] ;
    cdi:isDescribedBy <https://example.org/vd/temperatureCelsius/desc> ;
    cdi:recommendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryReference [ a cdi:Reference ;
                    cdi:uri "http://www.w3.org/2001/XMLSchema#double" ] ;
            cdi:entryValue "xsd:double" ;
            cdi:name "XML Schema Datatypes" ],
        [ a cdi:ControlledVocabularyEntry ;
            cdi:entryReference [ a cdi:Reference ;
                    cdi:uri "http://www.w3.org/2001/XMLSchema#decimal" ] ;
            cdi:entryValue "xsd:decimal" ;
            cdi:name "XML Schema Datatypes" ;
            cdi:vocabulary [ a cdi:Reference ;
                    cdi:description "W3C XML Schema Definition Language datatypes" ;
                    cdi:uri "http://www.w3.org/2001/XMLSchema" ] ] ;
    cdi:takesConceptsFrom <https://example.org/cd/seaWaterTemperature> ;
    cdi:takesValuesFrom <https://example.org/enum/temperatureSampleEnum> .

<https://example.org/cd/seaWaterTemperature> a cdi:SubstantiveConceptualDomain ;
    cdi:displayLabel [ a cdi:LabelForDisplay ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Sea Water Temperature (concept)" ;
                    cdi:language "en" ] ] ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:uri "https://example.org/cd/seaWaterTemperature" ] ;
    cdi:isDescribedBy <https://example.org/vd/temperatureCelsius/desc> ;
    cdi:takesConceptsFrom <https://example.org/cs/oceanographicConcepts> .

<https://example.org/vd/temperatureCelsius/desc> a cdi:ValueAndConceptDescription ;
    cdi:classificationLevel "Continuous" ;
    cdi:description [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Temperatures du seuil oceanographique en degres Celsius." ;
                    cdi:language "fr" ],
                [ a cdi:LanguageString ;
                    cdi:content "Real-valued sea water temperatures, expressed in degrees Celsius, in the plausible oceanographic range from -2 (freezing seawater) up to 35.5 (warm tropical surface)." ;
                    cdi:language "en" ] ] ;
    cdi:formatPattern [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "#0.00" ;
            cdi:name "LDML number pattern" ;
            cdi:vocabulary [ a cdi:Reference ;
                    cdi:uri "http://www.unicode.org/reports/tr35/tr35-numbers.html#Number_Format_Patterns" ] ] ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:uri "https://example.org/vd/temperatureCelsius/desc" ] ;
    cdi:logicalExpression [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "all reals x such that -2 <= x <= 35.5" ;
            cdi:name "informal range expression" ] ;
    cdi:maximumValueExclusive "40.0" ;
    cdi:maximumValueInclusive "35.5" ;
    cdi:minimumValueExclusive "-3.0" ;
    cdi:minimumValueInclusive "-2.0" ;
    cdi:regularExpression [ a cdi:TypedString ;
            cdi:content "^-?\\d+(\\.\\d+)?$" ;
            cdi:typeOfContent [ a cdi:ControlledVocabularyEntry ;
                    cdi:entryValue "ECMAScript" ;
                    cdi:name "regex syntax" ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Value Domain
description: Value domain for a substantive conceptual domain. Typically a description
  and/or enumeration of allowed values of interest.
anyOf:
- $ref: '#/$defs/SubstantiveValueDomain'
- $ref: '#/$defs/SentinelValueDomain'
- $ref: '#/$defs/DescriptorValueDomain'
- $ref: '#/$defs/Descriptor'
$defs:
  SubstantiveValueDomain:
    type: object
    description: Value domain for a substantive conceptual domain. Typically a description
      and/or enumeration of allowed values of interest.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:SubstantiveValueDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this SubstantiveValueDomain node
      cdi:takesValuesFrom:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiEnumerationDomain/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesValuesFrom
      cdi:isDescribedBy:
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDescribedBy
      cdi:takesConceptsFrom:
        anyOf:
        - $ref: '#/$defs/SubstantiveConceptualDomain'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesConceptsFrom
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:recommendedDataType:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        minItems: 1
        description: The data types that are recommended for use with this domain.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/recommendedDataType
    required:
    - '@type'
  SentinelValueDomain:
    type: object
    description: Value domain for a sentinel conceptual domain.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:SentinelValueDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this SentinelValueDomain node
      cdi:takesConceptsFrom:
        anyOf:
        - $ref: '#/$defs/SentinelConceptualDomain'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesConceptsFrom
      cdi:takesValuesFrom:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiEnumerationDomain/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesValuesFrom
      cdi:isDescribedBy:
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDescribedBy
      cdi:platformType:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: 'The type of platform under which sentinel codes will be used.
          Statistical software platforms use different sets of codes to indicate missing
          values. The external controlled vocabulary should list platform types and
          a description of the allowed missing value types. A sample list would be:


          - BlankString - A Blank string indicates missing. Comparison is based on
          lexical order. - EmptyString - An empty string indicates missing. Use in
          comparisons returns missing. - Rstyle - Codes drawn from NA and the IEEE
          754 values of NaN -Inf +Inf. Comparisons return NA. - SASNumeric - codes
          drawn from . ._ .A .B .C .D .E .F .G .H .I .J .K .L .M .N .O .P .Q .R .S
          .T .U .V .W .X .Y .Z Sentinel code treated as less than any substantive
          value - SPSSstyle - System missing (a dot) a set of individual values drawn
          from the same datatype as the SubstantiveValueDomain, and a range of values
          drawn from the same datatype as the SubstantiveValueDomain. Comparisons
          return system missing. Some functions substitute with valid values (e.g.
          SUM replaces missing values with 0). - StataNumeric - codes drawn from .
          ._ .A .B .C .D .E .F .G .H .I .J .K .L .M .N .O .P .Q .R .S .T .U .V .W
          .X .Y .Z Sentinel code treated as greater than any substantive value - Unrestricted
          - No restrictions on codes for sentinel values. Use in comparisons is indeterminate.'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/platformType
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:recommendedDataType:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        minItems: 1
        description: The data types that are recommended for use with this domain.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/recommendedDataType
    required:
    - '@type'
  DescriptorValueDomain:
    type: object
    description: Set of permissible values for a variable playing the role of a variable
      descriptor component.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DescriptorValueDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DescriptorValueDomain node
      cdi:takesValuesFrom:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiEnumerationDomain/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesValuesFrom
      cdi:isDescribedBy:
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDescribedBy
      cdi:takesConceptsFrom:
        anyOf:
        - $ref: '#/$defs/SubstantiveConceptualDomain'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesConceptsFrom
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:recommendedDataType:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        minItems: 1
        description: The data types that are recommended for use with this domain.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/recommendedDataType
    required:
    - '@type'
  Descriptor:
    type: object
    description: Use of a code for variable identification in the context of a data
      structure and a variable descriptor component.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Descriptor
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Descriptor node
      cdi:refersTo:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ReferenceValue'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/refersTo
      cdi:identifies:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPresentationalVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifies
      cdi:hasValueFrom:
        anyOf:
        - $ref: '#/$defs/DescriptorValueDomain'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasValueFrom
      cdi:isBasedOn:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isBasedOn
      cdi:content:
        $ref: '#/$defs/TypedString'
        description: The content of this value expressed as a string.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/content
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:isStoredIn:
        anyOf:
        - $ref: '#/$defs/DataPoint'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isStoredIn
      cdi:represents:
        anyOf:
        - $ref: '#/$defs/ConceptualValue'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/represents
      cdi:whiteSpace:
        type: string
        enum:
        - Collapse
        - Preserve
        - Replace
        description: 'The usual setting "collapse" states that leading and trailing
          white space will be removed and multiple adjacent white spaces will be treated
          as a single white space. When setting to "replace" all occurrences of #x9
          (tab), #xA (line feed) and #xD (carriage return) are replaced with #x20
          (space) but leading and trailing spaces will be retained. If the existence
          of any of these white spaces is critical to the understanding of the content,
          change the value of this attribute to "preserve".'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/whiteSpace
    required:
    - '@type'
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/allowsDuplicates
      cdi:externalDefinition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        description: A reference to an external definition of a concept (that is,
          a concept which is described outside the content of the DDI-CDI metadata
          description). An example is a SKOS concept. The definition property is assumed
          to duplicate the external one referenced if externalDefinition is used.
          Other corresponding properties are assumed to be included unchanged if used.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/externalDefinition
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (liguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:isDefinedBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDefinedBy
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purpose
    required:
    - '@type'
  ConceptualDomain:
    type: object
    description: Set of concepts, where each concept is intended to be used as the
      meaning (signified) for a datum.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ConceptualDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ConceptualDomain node
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:isDescribedBy:
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDescribedBy
      cdi:takesConceptsFrom:
        anyOf:
        - $ref: '#/$defs/ConceptSystem'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesConceptsFrom
    required:
    - '@type'
  ConceptualValue:
    type: object
    description: Concept (with a notion of equality defined) being observed, captured,
      or derived which is associated to a single data instance.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ConceptualValue
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ConceptualValue node
      cdi:hasConceptFrom:
        anyOf:
        - $ref: '#/$defs/ConceptualDomain'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasConceptFrom
      cdi:definition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Natural language statement conveying the meaning of a concept,
          differentiating it from other concepts. Supports the use of multiple languages
          and structured text. 'externalDefinition' can't be used if 'definition'
          is used.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/definition
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:externalDefinition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        description: A reference to an external definition of a concept (that is,
          a concept which is described outside the content of the DDI-CDI metadata
          description). An example is a SKOS concept. The definition property is assumed
          to duplicate the external one referenced if externalDefinition is used.
          Other corresponding properties are assumed to be included unchanged if used.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/externalDefinition
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:uses:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
    required:
    - '@type'
  DataPoint:
    type: object
    description: Container for an instance value.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DataPoint
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DataPoint node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:correspondsTo:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/correspondsTo
      cdi:isDescribedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiInstanceVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDescribedBy
    required:
    - '@type'
  ReferenceValue:
    type: object
    description: Recorded value in a variable value component. Value referenced by
      a descriptor.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ReferenceValue
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ReferenceValue node
      cdi:correspondsTo:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/correspondsTo
      cdi:hasValueFrom:
        anyOf:
        - $ref: '#/$defs/ReferenceValueDomain'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasValueFrom
      cdi:content:
        $ref: '#/$defs/TypedString'
        description: The content of this value expressed as a string.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/content
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:isStoredIn:
        anyOf:
        - $ref: '#/$defs/DataPoint'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isStoredIn
      cdi:represents:
        anyOf:
        - $ref: '#/$defs/ConceptualValue'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/represents
      cdi:whiteSpace:
        type: string
        enum:
        - Collapse
        - Preserve
        - Replace
        description: 'The usual setting "collapse" states that leading and trailing
          white space will be removed and multiple adjacent white spaces will be treated
          as a single white space. When setting to "replace" all occurrences of #x9
          (tab), #xA (line feed) and #xD (carriage return) are replaced with #x20
          (space) but leading and trailing spaces will be retained. If the existence
          of any of these white spaces is critical to the understanding of the content,
          change the value of this attribute to "preserve".'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/whiteSpace
    required:
    - '@type'
  ReferenceValueDomain:
    type: object
    description: Set of permissible values for a variable playing the role of a variable
      value component.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ReferenceValueDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ReferenceValueDomain node
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:recommendedDataType:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        minItems: 1
        description: The data types that are recommended for use with this domain.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/recommendedDataType
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
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:isDescribedBy:
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDescribedBy
      cdi:takesConceptsFrom:
        anyOf:
        - $ref: '#/$defs/ConceptSystem'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesConceptsFrom
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
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:isDescribedBy:
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDescribedBy
      cdi:takesConceptsFrom:
        anyOf:
        - $ref: '#/$defs/ConceptSystem'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesConceptsFrom
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/content
      cdi:typeOfContent:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Optional use of a controlled vocabulary to specifically type
          the associated content.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/typeOfContent
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/classificationLevel
      cdi:description:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: A formal description of the set of values in human-readable language.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/description
      cdi:formatPattern:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: 'A pattern for a number as described in Unicode Locale Data Markup
          Language (LDML) (http://www.unicode.org/reports/tr35/tr35.html) Part 3:
          Numbers (http://www.unicode.org/reports/tr35/tr35-numbers.html#Number_Format_Patterns)
          and Part 4. Dates (http://www.unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns)
          . Examples would be #,##0.### to describe the pattern for a decimal number,
          or yyyy.MM.dd G ''at'' HH:mm:ss zzz for a datetime pattern.'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/formatPattern
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:logicalExpression:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: A logical expression where the values of "x" making the expression
          true are the members of the set of valid values. For example, "(all reals
          x such that x > 0)" describes the real numbers greater than 0.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/logicalExpression
      cdi:maximumValueExclusive:
        type: string
        description: 'A string denoting the maximum possible value (excluding this
          value). From the W3C Recommendation "Metadata Vocabulary for Tabular Data"
          (https://www.w3.org/TR/tabular-metadata/) 5.11.2: "maxExclusive: An atomic
          property that contains a single number or string that is the maximum valid
          value (exclusive). The value of this property becomes the maximum exclusive
          annotation for the described datatype. See Value Constraints in [tabular-data-model]
          for details."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/maximumValueExclusive
      cdi:maximumValueInclusive:
        type: string
        description: 'A string denoting the maximum possible value. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.11.2: "maximum: An atomic property that contains a single number or string
          that is the maximum valid value (inclusive); equivalent to maxInclusive.
          The value of this property becomes the maximum annotation for the described
          datatype. See Value Constraints in [tabular-data-model] for details."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/maximumValueInclusive
      cdi:minimumValueExclusive:
        type: string
        description: 'A string denoting the minimum possible value (excluding this
          value). From the W3C Recommendation "Metadata Vocabulary for Tabular Data"
          (https://www.w3.org/TR/tabular-metadata/) 5.11.2: "minExclusive: An atomic
          property that contains a single number or string that is the minimum valid
          value (exclusive). The value of this property becomes the minimum exclusive
          annotation for the described datatype. See Value Constraints in [tabular-data-model]
          for details."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/minimumValueExclusive
      cdi:minimumValueInclusive:
        type: string
        description: 'A string denoting the minimum possible value. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.11.2: "minimum: An atomic property that contains a single number or string
          that is the minimum valid value (inclusive); equivalent to minInclusive.
          The value of this property becomes the minimum annotation for the described
          datatype. See Value Constraints in [tabular-data-model] for details."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/minimumValueInclusive
      cdi:regularExpression:
        $ref: '#/$defs/TypedString'
        description: A regular expression where strings matching the expression belong
          to the set of valid values. Use typeOfContent to specify the syntax of the
          regularExpression found in content.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/regularExpression
    required:
    - '@type'
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiValueDomain/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiValueDomain/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiValueDomain/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiValueDomain`

