
# DDI-CDI Physical Mapping (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiPhysicalMapping` *v0.1*

Describes how an InstanceVariable's values are physically represented in a dataset - format, length, decimal handling, null sequences, W3C tabular-data-model parameters. Successor to the DDI-CDI 1.0 ValueMapping class (renamed PhysicalMapping in the 2026-03 model, with the variable relationship reversed: PhysicalMapping formats InstanceVariable). Root validates any of PhysicalMapping, TextMapping (text-dialect detail), or LocatorMapping (locator string for non-tabular layouts); provides a $def for PhysicalMappingPosition. Composes building block: ddicdiDataTypes (ddiProperties); cdifInstanceVariable (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI **PhysicalMapping** describes how the values of an `InstanceVariable` are physically represented in a dataset — format, datatype, length, decimal handling, null sequences, and the W3C tabular-data-model parameters.

It is the successor to the DDI-CDI 1.0 `ValueMapping` class. In the 2026-03 DDI-CDI model `ValueMapping` was renamed `PhysicalMapping`, moved into the `FormatDescription` package, and the relationship to the variable was **reversed**: a `PhysicalMapping` now points at the `InstanceVariable` it formats (`cdi:formats`), rather than the variable carrying an outward `has_ValueMapping` link.

## Root

The root validates **any of** the three concrete mapping types:

- **`cdi:PhysicalMapping`** — the base mapping: `cdi:format`, `cdi:physicalDataType`, `cdi:decimalPositions`, `cdi:scale`, `cdi:numberPattern`, `cdi:defaultValue`, `cdi:nullSequence`, `cdi:isRequired`, `cdi:length` / `cdi:minimumLength` / `cdi:maximumLength`, `cdi:position`, and `cdi:formats` → the `InstanceVariable`.
- **`cdi:TextMapping`** — a PhysicalMapping for delimited or fixed-width text. Adds `cdi:defaultDecimalSeparator`, `cdi:defaultDigitGroupSeparator`, and `cdi:mappingLabel` (`LabelForDisplay`).
- **`cdi:LocatorMapping`** — a PhysicalMapping that carries a required `cdi:locator` string addressing the value's position in a non-tabular physical layout (e.g. an XPath, JSON pointer, or array-index expression).

## `$defs`

- **`PhysicalMappingPosition`** — assigns an integer `cdi:value` position to a `PhysicalMapping` (`cdi:indexes`) within an ordered sequence of mappings.

## Relationship to the CDIF building blocks

CDIF's own `cdifProperties/cdifPhysicalMapping` and `cdifProperties/cdifTabularData` building blocks cover the same ground for the CDIF schema.org profiles. `ddicdiPhysicalMapping` is the canonical DDI-CDI counterpart, kept for completeness alongside the rest of the `ddiProperties` set.

## Examples

### TextMapping for a delimited-text column
A cdi:TextMapping describing how a sea-water-temperature InstanceVariable's
values appear in a delimited text file - decimal handling, null sequence,
field length - with cdi:formats pointing at the variable by @id.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:TextMapping"],
  "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp/mapping",
  "cdi:format": {
    "@type": ["cdi:ControlledVocabularyEntry"],
    "cdi:entryValue": ["#0.00"],
    "cdi:name": "LDML number pattern"
  },
  "cdi:physicalDataType": {
    "@type": ["cdi:ControlledVocabularyEntry"],
    "cdi:entryValue": ["xsd:decimal"]
  },
  "cdi:decimalPositions": 2,
  "cdi:defaultDecimalSeparator": ".",
  "cdi:defaultDigitGroupSeparator": ",",
  "cdi:defaultValue": "NaN",
  "cdi:nullSequence": "-9999",
  "cdi:numberPattern": "#0.00",
  "cdi:isRequired": true,
  "cdi:length": 6,
  "cdi:minimumLength": 1,
  "cdi:maximumLength": 8,
  "cdi:position": 3,
  "cdi:mappingLabel": [
    {
      "@type": ["cdi:LabelForDisplay"],
      "cdi:languageSpecificString": {
        "@type": ["cdi:LanguageString"],
        "cdi:content": "Sea-water temperature column",
        "cdi:language": "en"
      }
    }
  ],
  "cdi:formats": {
    "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPhysicalMapping/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:TextMapping"
  ],
  "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp/mapping",
  "cdi:format": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "#0.00"
    ],
    "cdi:name": "LDML number pattern"
  },
  "cdi:physicalDataType": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "xsd:decimal"
    ]
  },
  "cdi:decimalPositions": 2,
  "cdi:defaultDecimalSeparator": ".",
  "cdi:defaultDigitGroupSeparator": ",",
  "cdi:defaultValue": "NaN",
  "cdi:nullSequence": "-9999",
  "cdi:numberPattern": "#0.00",
  "cdi:isRequired": true,
  "cdi:length": 6,
  "cdi:minimumLength": 1,
  "cdi:maximumLength": 8,
  "cdi:position": 3,
  "cdi:mappingLabel": [
    {
      "@type": [
        "cdi:LabelForDisplay"
      ],
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Sea-water temperature column",
        "cdi:language": "en"
      }
    }
  ],
  "cdi:formats": {
    "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/dataset/oceanTemp2025/var/seaWaterTemp/mapping> a cdi:TextMapping ;
    cdi:decimalPositions 2 ;
    cdi:defaultDecimalSeparator "." ;
    cdi:defaultDigitGroupSeparator "," ;
    cdi:defaultValue "NaN" ;
    cdi:format [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "#0.00" ;
            cdi:name "LDML number pattern" ] ;
    cdi:formats <https://example.org/dataset/oceanTemp2025/var/seaWaterTemp> ;
    cdi:isRequired true ;
    cdi:length 6 ;
    cdi:mappingLabel [ a cdi:LabelForDisplay ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Sea-water temperature column" ;
                    cdi:language "en" ] ] ;
    cdi:maximumLength 8 ;
    cdi:minimumLength 1 ;
    cdi:nullSequence "-9999" ;
    cdi:numberPattern "#0.00" ;
    cdi:physicalDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
    cdi:position 3 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Physical Mapping
description: 'Describes how the value of an InstanceVariable is physically represented
  in a dataset - format, length, decimal handling, null sequences, and the W3C tabular-data-model
  parameters. Successor to the DDI-CDI 1.0 ValueMapping class; in the 2026-03 model
  it was renamed PhysicalMapping and the relationship to the variable reversed (PhysicalMapping
  formats InstanceVariable). PhysicalMapping has two subclasses: TextMapping (adds
  text-dialect detail) and LocatorMapping (adds a locator string for non-tabular physical
  layouts). The root validates any of the three.'
type: object
anyOf:
- $ref: '#/$defs/PhysicalMapping'
- $ref: '#/$defs/TextMapping'
- $ref: '#/$defs/LocatorMapping'
$defs:
  PhysicalMapping:
    type: object
    description: The base physical mapping - format and representation detail for
      an InstanceVariable's values in a dataset.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:PhysicalMapping
        minItems: 1
      '@id':
        type: string
        description: Identifier for this PhysicalMapping node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:format:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The format of the physical representation of the value (W3C tabular-metadata
          format; DDI 3.2 ManagedNumericRepresentation@format).
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/format
      cdi:physicalDataType:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The base datatype of the physical representation (e.g. an integer
          variable stored as a floating point number).
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/physicalDataType
      cdi:decimalPositions:
        type: integer
        description: The number of decimal positions, used when the decimal position
          is implied (no decimal separator present).
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/decimalPositions
      cdi:scale:
        type: integer
        description: The scale of the number - a multiplier used with the value to
          determine the measurement.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/scale
      cdi:numberPattern:
        type: string
        description: A pattern description of the format of a numeric value (W3C tabular-metadata
          pattern / UAX35 number format pattern).
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/numberPattern
      cdi:defaultValue:
        type: string
        description: A default string indicating the value to substitute for an empty
          string.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/defaultValue
      cdi:nullSequence:
        type: string
        description: A string indicating a null value.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/nullSequence
      cdi:isRequired:
        type: boolean
        description: If True, a value is required for the referenced instance variable.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isRequired
      cdi:length:
        type: integer
        description: The length in characters of the physical representation of the
          value.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/length
      cdi:minimumLength:
        type: integer
        description: The smallest possible length of the physical representation of
          the value.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/minimumLength
      cdi:maximumLength:
        type: integer
        description: The largest possible length of the physical representation of
          the value.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/maximumLength
      cdi:position:
        type: integer
        description: The position of this mapping in an ordered sequence of mappings.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/position
      cdi:formats:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        description: The InstanceVariable whose values this mapping physically represents.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/formats
    required:
    - '@type'
  TextMapping:
    type: object
    description: A PhysicalMapping for delimited or fixed-width text - adds the decimal/digit-group
      separators, a display label, and the field length.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:TextMapping
        minItems: 1
      '@id':
        type: string
        description: Identifier for this TextMapping node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:format:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The format of the physical representation of the value.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/format
      cdi:physicalDataType:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The base datatype of the physical representation.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/physicalDataType
      cdi:decimalPositions:
        type: integer
        description: The number of decimal positions, used when the decimal position
          is implied (no decimal separator present).
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/decimalPositions
      cdi:scale:
        type: integer
        description: The scale of the number.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/scale
      cdi:numberPattern:
        type: string
        description: A pattern description of the format of a numeric value.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/numberPattern
      cdi:defaultValue:
        type: string
        description: A default string indicating the value to substitute for an empty
          string.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/defaultValue
      cdi:nullSequence:
        type: string
        description: A string indicating a null value.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/nullSequence
      cdi:isRequired:
        type: boolean
        description: If True, a value is required for the referenced instance variable.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isRequired
      cdi:length:
        type: integer
        description: The length in characters of the physical representation of the
          value.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/length
      cdi:minimumLength:
        type: integer
        description: The smallest possible length of the physical representation.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/minimumLength
      cdi:maximumLength:
        type: integer
        description: The largest possible length of the physical representation.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/maximumLength
      cdi:position:
        type: integer
        description: The position of this mapping in an ordered sequence of mappings.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/position
      cdi:defaultDecimalSeparator:
        type: string
        description: The character separating the integer part from the fractional
          part of a decimal or real number. Default is "." (period).
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/defaultDecimalSeparator
      cdi:defaultDigitGroupSeparator:
        type: string
        description: A character separating groups of digits (for readability). Default
          is null.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/defaultDigitGroupSeparator
      cdi:mappingLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for this mapping. Ordered; repeat
          for labels with different content.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/mappingLabel
      cdi:formats:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        description: The InstanceVariable whose values this mapping physically represents.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/formats
    required:
    - '@type'
  LocatorMapping:
    type: object
    description: A PhysicalMapping that carries a locator string addressing the value's
      position in a non-tabular physical layout (e.g. an XPath, JSON pointer, or array
      index expression).
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:LocatorMapping
        minItems: 1
      '@id':
        type: string
        description: Identifier for this LocatorMapping node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:locator:
        type: string
        description: A string that addresses the value's position in the physical
          layout (e.g. an XPath, JSON pointer, or array index expression).
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/locator
      cdi:format:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The format of the physical representation of the value.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/format
      cdi:physicalDataType:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The base datatype of the physical representation.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/physicalDataType
      cdi:decimalPositions:
        type: integer
        description: The number of decimal positions, used when the decimal position
          is implied.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/decimalPositions
      cdi:scale:
        type: integer
        description: The scale of the number.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/scale
      cdi:numberPattern:
        type: string
        description: A pattern description of the format of a numeric value.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/numberPattern
      cdi:defaultValue:
        type: string
        description: A default string indicating the value to substitute for an empty
          string.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/defaultValue
      cdi:nullSequence:
        type: string
        description: A string indicating a null value.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/nullSequence
      cdi:isRequired:
        type: boolean
        description: If True, a value is required for the referenced instance variable.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isRequired
      cdi:length:
        type: integer
        description: The length in characters of the physical representation of the
          value.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/length
      cdi:minimumLength:
        type: integer
        description: The smallest possible length of the physical representation.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/minimumLength
      cdi:maximumLength:
        type: integer
        description: The largest possible length of the physical representation.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/maximumLength
      cdi:position:
        type: integer
        description: The position of this mapping in an ordered sequence of mappings.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/position
      cdi:formats:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        description: The InstanceVariable whose values this mapping physically represents.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/formats
    required:
    - '@type'
    - cdi:locator
  PhysicalMappingPosition:
    type: object
    description: Assigns a position to a PhysicalMapping within an ordered sequence
      of mappings.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:PhysicalMappingPosition
        minItems: 1
      '@id':
        type: string
        description: Identifier for this PhysicalMappingPosition node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:value:
        type: integer
        description: Index value of the mapping in the ordered sequence.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/value
      cdi:indexes:
        anyOf:
        - $ref: '#/$defs/PhysicalMapping'
        - $ref: '#/$defs/TextMapping'
        - $ref: '#/$defs/LocatorMapping'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        description: The PhysicalMapping this position applies to.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/indexes
    required:
    - '@type'
    - cdi:value
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPhysicalMapping/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPhysicalMapping/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "schema": "http://schema.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPhysicalMapping/context.jsonld)

## Sources

* [DDI-CDI Specification (2026-03 model)](https://ddialliance.org/Specification/DDI-CDI/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiPhysicalMapping`

