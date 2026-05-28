
# DDI-CDI Physical Data Set (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiPhysicalDataSet` *v0.1*

Organized collection of wide data. It is structured by a wide data structure.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI PhysicalDataSet describes an organized collection of data values organized in one of the layouts supported by DDI-CDI. Polymorphic root over `cdi:WideDataSet`, `cdi:LongDataSet`, and `cdi:DimensionalDataSet`.

Each variant references its structure via `cdi:isStructuredBy` (pointing at a `ddicdiDataStructure` of the matching kind) and holds the data points themselves through `cdi:has_DataPoint`, with optional `cdi:has_Key` for compound-key indexing. `DimensionalDataSet` adds `cdi:represents` linking to scoped measures. PhysicalDataSet is the dataset-as-realized counterpart to `ddicdiDataStructure` and is the target a CDIF distribution-level description ultimately ties to when the full DDI-CDI Data Description profile is in use.

## Examples

### Minimal WideDataSet
TODO: replace with a JSON-LD example.
## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Physical Data Set
description: Organized collection of wide data. It is structured by a wide data structure.
anyOf:
- $ref: '#/$defs/WideDataSet'
- $ref: '#/$defs/LongDataSet'
- $ref: '#/$defs/DimensionalDataSet'
- $ref: '#/$defs/TabularTextDataSet'
- $ref: '#/$defs/StructuredDataSet'
$defs:
  WideDataSet:
    type: object
    description: Organized collection of wide data. It is structured by a wide data
      structure.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:WideDataSet
        minItems: 1
      '@id':
        type: string
        description: Identifier for this WideDataSet node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:recordCount:
        type: integer
        description: Number of records in the data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/recordCount
      cdi:fingerprint:
        $ref: '#/$defs/DataFingerprint'
        description: Universal Numerical Fingerprint or similar format-independent
          canonical hash value of the physical representation of data in the physical
          data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/fingerprint
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:has_InstanceVariable:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiInstanceVariable/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_InstanceVariable
      cdi:has_DataPoint:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/DataPoint'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_DataPoint
      cdi:has_Key:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifKey/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_Key
      cdi:isStructuredBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructure/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isStructuredBy
    required:
    - '@type'
  LongDataSet:
    type: object
    description: Organized collection of long data. It is structured by a long data
      structure.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:LongDataSet
        minItems: 1
      '@id':
        type: string
        description: Identifier for this LongDataSet node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:recordCount:
        type: integer
        description: Number of records in the data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/recordCount
      cdi:fingerprint:
        $ref: '#/$defs/DataFingerprint'
        description: Universal Numerical Fingerprint or similar format-independent
          canonical hash value of the physical representation of data in the physical
          data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/fingerprint
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:has_InstanceVariable:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiInstanceVariable/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_InstanceVariable
      cdi:has_DataPoint:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/DataPoint'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_DataPoint
      cdi:has_Key:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifKey/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_Key
      cdi:isStructuredBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructure/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isStructuredBy
    required:
    - '@type'
  DimensionalDataSet:
    type: object
    description: Organized collection of multidimensional data. It is structured by
      a dimensional data structure.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DimensionalDataSet
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DimensionalDataSet node
      cdi:represents:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ScopedMeasure'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/represents
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:recordCount:
        type: integer
        description: Number of records in the data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/recordCount
      cdi:fingerprint:
        $ref: '#/$defs/DataFingerprint'
        description: Universal Numerical Fingerprint or similar format-independent
          canonical hash value of the physical representation of data in the physical
          data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/fingerprint
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:has_InstanceVariable:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiInstanceVariable/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_InstanceVariable
      cdi:has_DataPoint:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/DataPoint'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_DataPoint
      cdi:has_Key:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifKey/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_Key
      cdi:isStructuredBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructure/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isStructuredBy
    required:
    - '@type'
  TabularTextDataSet:
    type: object
    description: Information describing the physical aspects of a data set which is
      encoded using a text-based method and which has an essentially tabular structure.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:TabularTextDataSet
        minItems: 1
      '@id':
        type: string
        description: Identifier for this TabularTextDataSet node
      cdi:arrayBase:
        type: integer
        description: 'The starting value for the numbering of cells, rows, columns,
          etc. when they constitute an ordered sequence (an array). Note that in DDI,
          this is typically either 0 or 1. In related W3C work (Model for Tabular
          Data and Metadata on the Web), they appear to standardize on 1 (see https://www.w3.org/TR/tabular-data-model/
          4.3 [Columns] and 4.4 [Rows]: "number - the position of the column amongst
          the columns for the associated table, starting from 1.")'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/arrayBase
      cdi:commentPrefix:
        type: string
        description: 'A string used to indicate that an input line is a comment, a
          string which precedes a comment in the data file. From https://www.w3.org/TR/tabular-metadata/
          5.9 Dialect commentPrefix: ''An atomic property that sets the comment prefix
          flag to the single provided value, which MUST be a string. The default is
          "#".'''
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/commentPrefix
      cdi:delimiter:
        type: string
        description: 'The Delimiting character in the data. Must be used if isDelimited
          is True. "The separator between cells, set by the delimiter property of
          a dialect description. The default is ,. See the W3C Recommendation "Metadata
          Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-data-model/#encoding).
          From the "CSV Dialect" specification (https://specs.frictionlessdata.io/csv-dialect/#specification):
          "delimiter: specifies a one-character string to use as the field separator.
          Default = ,."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/delimiter
      cdi:escapeCharacter:
        type: string
        description: '"The string that is used to escape the quote character within
          escaped cells, or null" see https://www.w3.org/TR/tabular-data-model/#encoding.
          From https://www.w3.org/TR/tabular-metadata/ 5.9 Dialect "doubleQuote: A
          boolean atomic property that, if true, sets the escape character flag to
          ". If false, to \. The default is true." From http://specs.frictionlessdata.io/csv-dialect/
          "doubleQuote: controls the handling of quotes inside fields. If true, two
          consecutive quotes should be interpreted as one. Default = true".'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/escapeCharacter
      cdi:hasHeader:
        type: boolean
        description: 'True if the file contains a header containing column names.
          From https://www.w3.org/TR/tabular-metadata/ 5.9 Dialect "header: A boolean
          atomic property that, if true, sets the header row count flag to 1, and
          if false to 0, unless headerRowCount is provided, in which case the value
          provided for the header property is ignored. The default is true." From
          http://specs.frictionlessdata.io/csv-dialect/ "header: indicates whether
          the file includes a header row. If true the first row in the file is a header
          row, not data. Default = true".'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasHeader
      cdi:headerIsCaseSensitive:
        type: boolean
        description: 'If True, the case of the labels in the header is significant.
          From the "CSV Dialect" specification (http://specs.frictionlessdata.io/csv-dialect/):
          "caseSensitiveHeader: indicates that case in the header is meaningful. For
          example, columns CAT and Cat should not be equated. Default = false."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/headerIsCaseSensitive
      cdi:headerRowCount:
        type: integer
        description: 'The number of lines in the header From https://www.w3.org/TR/tabular-metadata/
          5.9 Dialect "headerRowCount: A numeric atomic property that sets the header
          row count flag to the single provided value, which MUST be a non-negative
          integer. The default is 1."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/headerRowCount
      cdi:isDelimited:
        type: boolean
        description: Indicates whether the data are in a delimited format. If "true,"
          the format is delimited, and the isFixedWidth property must be set to "false."
          If not set to "true," the property isFixedWitdh must be set to "true."
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDelimited
      cdi:isFixedWidth:
        type: boolean
        description: Set to true if the file is fixed-width. If true, isDelimited
          must be set to false.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isFixedWidth
      cdi:lineTerminator:
        type: array
        items:
          type: string
        description: 'The strings that can be used at the end of a row, set by the
          lineTerminators property of a dialect description. The default is [CRLF,
          LF]. See the W3C Recommendation "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-data-model/#encoding)
          5.9 Dialect "lineTerminators: An atomic property that sets the line terminators
          flag to either an array containing the single provided string value, or
          the provided array. The default is [''rn'', ''n'']." Also, from the "CSV
          Dialect" specification (http://specs.frictionlessdata.io/csv-dialect/):
          "lineTerminator: specifies the character sequence which should terminate
          rows. Default = rn."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/lineTerminator
      cdi:nullSequence:
        type: string
        description: 'A string indicating a null value. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          4.3: "null: the string or strings which cause the value of cells having
          string value matching any of these values to be null." From the same source,
          Inherited 5.7: "null: An atomic property giving the string or strings used
          for null values within the data. If the string value of the cell is equal
          to any one of these values, the cell value is null. See Parsing Cells in
          [tabular-data-model] for more details. If not specified, the default for
          the null property is the empty string ''''. The value of this property becomes
          the null annotation for the described column."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/nullSequence
      cdi:quoteCharacter:
        type: string
        description: '"The string that is used around escaped cells, or null, set
          by the quoteChar property of a dialect description. The default is ".".
          See W3C Recommendation "Model for Tabular Data and Metadata on the Web",
          https://www.w3.org/TR/tabular-data-model/#parsing. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.9 Dialect: "quoteChar: An atomic property that sets the quote character
          flag to the single provided value, which MUST be a string or null. If the
          value is null, the escape character flag is also set to null. The default
          is ''"''." From the CSV Dialect specification (http://specs.frictionlessdata.io/csv-dialect/):
          "quoteChar: specifies a one-character string to use as the quoting character.
          Default = "."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/quoteCharacter
      cdi:skipBlankRows:
        type: boolean
        description: 'If the value is True, blank rows are ignored. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.9 Dialect: "skipBlankRows: A boolean atomic property that sets the skip
          blank rows flag to the single provided boolean value. The default is false."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/skipBlankRows
      cdi:skipDataColumns:
        type: integer
        description: 'The number of columns to skip at the beginning of the row. From
          the W3C Recommendation "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.9 Dialect: "skipColumns: A numeric atomic property that sets the skip
          columns flag to the single provided numeric value, which MUST be a non-negative
          integer. The default is 0." A value other than 0 will mean that the source
          numbers of columns will be different from their numbers.'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/skipDataColumns
      cdi:skipInitialSpace:
        type: boolean
        description: 'If the value is True, skip whitespace at the beginning of a
          line or following a delimiter. From the W3C Recommendation "Metadata Vocabulary
          for Tabular Data" (https://www.w3.org/TR/tabular-metadata/) 5.9 Dialect:
          "skipInitialSpace: A boolean atomic property that, if true, sets the trim
          flag to ''start'' and if false, to false. If the trim property is provided,
          the skipInitialSpace property is ignored. The default is false." From the
          CSV Dialect specification (http://specs.frictionlessdata.io/csv-dialect/):
          "skipInitialSpace: specifies how to interpret whitespace which immediately
          follows a delimiter; if false, it means that whitespace immediately after
          a delimiter should be treated as part of the following field. Default =
          true."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/skipInitialSpace
      cdi:skipRows:
        type: integer
        description: 'Number of input rows to skip preceding the header or data. From
          the W3C Recommendation "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.9 Dialect: "skipRows: A numeric atomic property that sets the skip rows
          flag to the single provided numeric value, which MUST be a non-negative
          integer. The default is 0." A value greater than 0 will mean that the source
          numbers of rows will be different from their numbers.'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/skipRows
      cdi:tableDirection:
        type: string
        enum:
        - Auto
        - Ltr
        - Rtl
        description: 'Indicates the direction in which columns are arranged in each
          row. From the W3C Recommendation "Metadata Vocabulary for Tabular Data"
          (https://www.w3.org/TR/tabular-metadata/) 5.3.2: "tableDirection: An atomic
          property that MUST have a single string value that is one of ''rtl'', ''ltr'',
          or ''auto''. Indicates whether the tables in the group should be displayed
          with the first column on the right, on the left, or based on the first character
          in the table that has a specific direction. The value of this property becomes
          the value of the table direction annotation for all the tables in the table
          group. See Bidirectional Tables in [tabular-data-model] for details. The
          default value for this property is ''auto''."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/tableDirection
      cdi:textDirection:
        type: string
        enum:
        - Auto
        - Inherit
        - Ltr
        - Rtl
        description: 'Indicates the reading order of text within cells. From the W3C
          Recommendation "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          Inherited 5.7: "textDirection: An atomic property that MUST have a single
          string value that is one of ''ltr'', ''rtl'', ''auto'' or ''inherit'' (the
          default). Indicates whether the text within cells should be displayed as
          left-to-right text (ltr), as right-to-left text (rtl), according to the
          content of the cell (auto) or in the direction inherited from the table
          direction annotation of the table. The value of this property determines
          the text direction annotation for the column, and the text direction annotation
          for the cells within that column: if the value is inherit then the value
          of the text direction annotation is the value of the table direction annotation
          on the table, otherwise it is the value of this property. See Bidirectional
          Tables in [tabular-data-model] for details."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/textDirection
      cdi:treatConsecutiveDelimitersAsOne:
        type: boolean
        description: If the value is True, consecutive (adjacent) delimiters are treated
          as a single delimiter; if the value is False consecutive (adjacent) delimiters
          indicate a missing value.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/treatConsecutiveDelimitersAsOne
      cdi:trim:
        type: string
        enum:
        - Both
        - End
        - Neither
        - Start
        description: 'Specifies which spaces to remove from a data value (start, end,
          both, neither) From the W3C Recommendation "Metadata Vocabulary for Tabular
          Data" (https://www.w3.org/TR/tabular-metadata/) 5.9 Dialect: "trim: An atomic
          property that, if the boolean true, sets the trim flag to true and if the
          boolean false to false. If the value provided is a string, sets the trim
          flag to the provided value, which MUST be one of ''true'', ''false'', ''start'',
          or ''end''. The default is true."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/trim
      cdi:isDefinedBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDefinedBy
      cdi:characterSet:
        type: string
        description: Default character set used in the physical data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/characterSet
      cdi:encoding:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: 'The character encoding of the represented data. From the W3C
          Recommendation "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.9 Dialect: "encoding - An atomic property that sets the encoding flag
          to the single provided string value, which MUST be a defined in [encoding].
          The default is ''utf-8''." From the same W3C recommendation 7.2 Encoding:
          "CSV files should be encoded using UTF-8, and should be in Unicode Normal
          Form C as defined in [UAX15]. If a CSV file is not encoded using UTF-8,
          the encoding should be specified through the charset parameter in the Content-Type
          header."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/encoding
      cdi:fileSize:
        type: number
        description: File size expressed as a real number.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/fileSize
      cdi:fileSizeUofM:
        type: string
        description: Unit of measure of the fileSize as a simple string, e.g. KB,
          megabyte, GB, etc.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/fileSizeUofM
      cdi:fingerprint:
        $ref: '#/$defs/DataFingerprint'
        description: Universal Numerical Fingerprint or similar format-independent,
          canonical hash value of the physical representation of data in the physical
          data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/fingerprint
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:name:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:overview:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Short natural language account of the information obtained from
          the combination of properties and relationships associated with an object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/overview
      cdi:physicalFileURL:
        type: string
        description: URL for the physical data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/physicalFileURL
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purpose
      cdi:recordCount:
        type: integer
        description: Number of records in the physical data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/recordCount
      cdi:standard:
        type: array
        items:
          $ref: '#/$defs/conformsTo'
        description: An established standard to which the described resource conforms.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/standard
      cdi:has_InstanceVariable:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiInstanceVariable/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_InstanceVariable
      cdi:has_PhysicalMapping:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPhysicalMapping/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_PhysicalMapping
      cdi:has_PhysicalMappingPosition:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/PhysicalMappingPosition'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_PhysicalMappingPosition
      cdi:correspondsTo:
        anyOf:
        - $ref: '#/$defs/DataSet'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/correspondsTo
      cdi:uses:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiLogicalRecord/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
    required:
    - '@type'
  StructuredDataSet:
    type: object
    description: Information describing the physical aspects of a data set using a
      binary or highly structured text-based encoding.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:StructuredDataSet
        minItems: 1
      '@id':
        type: string
        description: Identifier for this StructuredDataSet node
      cdi:characterSet:
        type: string
        description: Default character set used in the physical data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/characterSet
      cdi:encoding:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: 'The character encoding of the represented data. From the W3C
          Recommendation "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.9 Dialect: "encoding - An atomic property that sets the encoding flag
          to the single provided string value, which MUST be a defined in [encoding].
          The default is ''utf-8''." From the same W3C recommendation 7.2 Encoding:
          "CSV files should be encoded using UTF-8, and should be in Unicode Normal
          Form C as defined in [UAX15]. If a CSV file is not encoded using UTF-8,
          the encoding should be specified through the charset parameter in the Content-Type
          header."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/encoding
      cdi:fileSize:
        type: number
        description: File size expressed as a real number.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/fileSize
      cdi:fileSizeUofM:
        type: string
        description: Unit of measure of the fileSize as a simple string, e.g. KB,
          megabyte, GB, etc.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/fileSizeUofM
      cdi:fingerprint:
        $ref: '#/$defs/DataFingerprint'
        description: Universal Numerical Fingerprint or similar format-independent,
          canonical hash value of the physical representation of data in the physical
          data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/fingerprint
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:name:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:overview:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Short natural language account of the information obtained from
          the combination of properties and relationships associated with an object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/overview
      cdi:physicalFileURL:
        type: string
        description: URL for the physical data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/physicalFileURL
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purpose
      cdi:recordCount:
        type: integer
        description: Number of records in the physical data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/recordCount
      cdi:standard:
        type: array
        items:
          $ref: '#/$defs/conformsTo'
        description: An established standard to which the described resource conforms.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/standard
      cdi:has_InstanceVariable:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiInstanceVariable/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_InstanceVariable
      cdi:has_PhysicalMapping:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPhysicalMapping/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_PhysicalMapping
      cdi:has_PhysicalMappingPosition:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/PhysicalMappingPosition'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_PhysicalMappingPosition
      cdi:isDefinedBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDefinedBy
      cdi:correspondsTo:
        anyOf:
        - $ref: '#/$defs/DataSet'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/correspondsTo
      cdi:uses:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiLogicalRecord/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
    required:
    - '@type'
  Category:
    type: object
    description: Concept whose role is to define and measure a characteristic.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Category
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Category node
      cdi:descriptiveText:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: A short natural language account of the characteristics of the
          object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/descriptiveText
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
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
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purpose
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has
      cdi:isDefinedBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDefinedBy
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
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:takesConceptsFrom:
        anyOf:
        - $ref: '#/$defs/ConceptSystem'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesConceptsFrom
      cdi:isDescribedBy:
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDescribedBy
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
    required:
    - '@type'
  DataFingerprint:
    type: object
    description: Hash value (digital fingerprint) of the logical or physical representation
      of data.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DataFingerprint
        minItems: 1
      cdi:value:
        type: string
        description: The value of the digital fingerprint.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/value
      cdi:algorithmSpecification:
        type: string
        description: The algorithm used to compute the value of the fingerprint.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/algorithmSpecification
      cdi:algorithmVersion:
        type: string
        description: The version of the algorithm used to compute the value of the
          fingerprint.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/algorithmVersion
      cdi:typeOfFingerprint:
        type: string
        description: The type of fingerprint, which may be computed on the physical
          data set (storage format specific) or data set (format neutral).
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/typeOfFingerprint
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
      cdi:isDescribedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiInstanceVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDescribedBy
      cdi:correspondsTo:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/correspondsTo
    required:
    - '@type'
  DataSet:
    type: object
    description: Organized collection of data based on keys.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DataSet
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DataSet node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:recordCount:
        type: integer
        description: Number of records in the data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/recordCount
      cdi:fingerprint:
        $ref: '#/$defs/DataFingerprint'
        description: Universal Numerical Fingerprint or similar format-independent
          canonical hash value of the physical representation of data in the physical
          data set.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/fingerprint
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:has_InstanceVariable:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiInstanceVariable/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_InstanceVariable
      cdi:has_DataPoint:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/DataPoint'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_DataPoint
      cdi:has_Key:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifKey/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_Key
      cdi:isStructuredBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructure/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isStructuredBy
    required:
    - '@type'
  DimensionalKeyDefinition:
    type: object
    description: Collection of concepts that uniquely defines a collection of data
      points in a dimensional dataset.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DimensionalKeyDefinition
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DimensionalKeyDefinition node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:correspondsTo_Universe:
        anyOf:
        - $ref: '#/$defs/Universe'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/correspondsTo_Universe
      cdi:correspondsTo_Unit:
        anyOf:
        - $ref: '#/$defs/Unit'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/correspondsTo_Unit
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/KeyDefinitionMember'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has
    required:
    - '@type'
  InstanceValue:
    type: object
    description: Single data instance corresponding to a concept (with a notion of
      equality defined) being observed, captured, or derived.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:InstanceValue
        minItems: 1
      '@id':
        type: string
        description: Identifier for this InstanceValue node
      cdi:content:
        $ref: '#/$defs/TypedString'
        description: The content of this value expressed as a string.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/content
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
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
      cdi:hasValueFrom:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiValueDomain/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasValueFrom
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
    required:
    - '@type'
  KeyDefinitionMember:
    type: object
    description: Single concept that is part of the structure of a key definition.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:KeyDefinitionMember
        minItems: 1
      '@id':
        type: string
        description: Identifier for this KeyDefinitionMember node
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
    required:
    - '@type'
  Notation:
    type: object
    description: Representation of a category in the context of a code or a classification
      item, as opposed of the corresponding instance value which would appear when
      used in a dataset.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Notation
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Notation node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:content:
        $ref: '#/$defs/TypedString'
        description: The actual content of this value as a string.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/content
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
      cdi:represents:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Category'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/represents
    required:
    - '@type'
  PhysicalMappingPosition:
    type: object
    description: Denotes the position of a physical mapping in a sequence within a
      physical data set.
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
        description: Index value of the member in an ordered array.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/value
      cdi:indexes:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPhysicalMapping/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/indexes
    required:
    - '@type'
  QualifiedMeasure:
    type: object
    description: A measure having a specific production method.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:QualifiedMeasure
        minItems: 1
      '@id':
        type: string
        description: Identifier for this QualifiedMeasure node
      cdi:refines:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/refines
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/PairedControlledVocabularyEntry
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/semantic
      cdi:specialization:
        $ref: '#/$defs/SpecializationRole'
        description: The role played by the component for the data set for purposes
          of harmonization and integration, typically regarding geography, time, etc.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/specialization
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiRepresentedVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDefinedBy
    required:
    - '@type'
  RevisableDatum:
    type: object
    description: A datum that can be qualified by a revision.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:RevisableDatum
        minItems: 1
      '@id':
        type: string
        description: Identifier for this RevisableDatum node
      cdi:vintage:
        type: integer
        description: A revision sequence number for a datum.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/vintage
      cdi:correspondsTo:
        anyOf:
        - $ref: '#/$defs/Revision'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/correspondsTo
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:isBoundedBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiInstanceVariable/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isBoundedBy
      cdi:uses_InstanceValue:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/InstanceValue'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses_InstanceValue
      cdi:uses_Notation:
        anyOf:
        - $ref: '#/$defs/Notation'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses_Notation
      cdi:denotes:
        anyOf:
        - $ref: '#/$defs/ConceptualValue'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/denotes
    required:
    - '@type'
  Revision:
    type: object
    description: Algorithm applied to produce a revised datum.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Revision
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Revision node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:overview:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Short natural language account of the information obtained from
          the combination of properties and relationships associated with an object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/overview
      cdi:algorithm:
        type: string
        description: Actual code or reference to specific algorithm
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/algorithm
    required:
    - '@type'
  ScopedMeasure:
    type: object
    description: A qualified measure whose domain is a universe as an aggregate, i.e.
      a measure with a specific production method applied to a specific cell in a
      cube.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ScopedMeasure
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ScopedMeasure node
      cdi:frequency:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Time interval between successive measurements (i.e. applications)
          of a Scoped Measure.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/frequency
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:circumscribes:
        anyOf:
        - $ref: '#/$defs/DimensionalKeyDefinition'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/circumscribes
      cdi:restricts:
        anyOf:
        - $ref: '#/$defs/QualifiedMeasure'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/restricts
      cdi:generates:
        anyOf:
        - $ref: '#/$defs/RevisableDatum'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/generates
    required:
    - '@type'
  SpecializationRole:
    type: object
    description: Specific roles played by represented variables in terms of time,
      geography, and other concepts which are important for the harmonization and
      integration of data.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:SpecializationRole
        minItems: 1
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
  Unit:
    type: object
    description: Individual object of interest for some statistical activity, such
      as data collection.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Unit
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Unit node
      cdi:definition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Natural language statement conveying the meaning of a concept,
          differentiating it from other concepts. Supports the use of multiple languages
          and structured text.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/definition
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/UnitType'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has
    required:
    - '@type'
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
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: A short natural language account of the characteristics of the
          object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/descriptiveText
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
    required:
    - '@type'
  Universe:
    type: object
    description: Specialized unit type, with the specialization based upon characteristics
      other than time and geography.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Universe
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Universe node
      cdi:isInclusive:
        type: boolean
        description: Default value is True. The description statement of a universe
          is generally stated in inclusive terms such as "All persons with university
          degree". Occasionally a universe is defined by what it excludes, i.e., "All
          persons except those with university degree". In this case the value would
          be changed to False.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isInclusive
      cdi:descriptiveText:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: A short natural language account of the characteristics of the
          object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/descriptiveText
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
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
          x such that x &gt; 0)" describes the real numbers greater than 0.
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
  conformsTo:
    type: object
    description: An established standard to which the described resource conforms.
      (See DCMI Metadata Terms - https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#conformsTo)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:conformsTo
        minItems: 1
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPhysicalDataSet/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPhysicalDataSet/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema": "http://schema.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "prov": "http://www.w3.org/ns/prov#",
    "cdif": "https://cdif.org/0.1/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPhysicalDataSet/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiPhysicalDataSet`

