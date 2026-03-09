
# XDI data structure description (Schema)

`cdif.bbr.metadata.xasProperties.xasXdiTabularTextDataset` *v0.1*

Schema defining properties to describe the structure of an XDI file. This is a fixed-wide tabular text data structure for describing the result of x-ray absorption spectroscopy experiments. Defines properties: @type, cdi:has_DataStructureComponent, cdi:allowsDuplicates, cdi:arrayBase, cdi:commentPrefix, cdi:hasHeader, cdi:headerRowCount, cdi:skipInitialSpace, cdi:isDelimited, cdi:isFixedWidth.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## XDI format tabular text data structure properties

Defintion of properties to describe structure of tabular data formatted following the xdi specification.  This is a very simplified description for tabular text data with fixed width columns. TBD--generalize for generic delimited tabular text formats, based on CSV for the web, Croissant, other applicable specifications.[Format specification](https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md)
## Examples

### Example XDI-format data download for simple tabular text description.
Defintion of properties to describe structure of tabular data formatted following the xdi specification.  This is a very simplified description for tabular text data with fixed width columns. TBD--generalize for generic delimited tabular text formats, based on CSV for the web, Croissant, other applicable specifications.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "xas": "https://xas.org/dictionary/"
    },
    "@id": "ex:xasXDIdownload_23463h",
    "@type": "cdi:WideDataStructure",
    "cdi:has_DataStructureComponent": [
        {
            "@type": "cdi:IdentifierComponent",
            "cdi:isDefinedBy_InstanceVariable": {"@id": "xas:monochromatorEnergyVariable"},
            "cdi:has": {
                "@type": "cdi:ValueMapping",
                "cdi:hasIndex": 1,
                "cdi:haslength": 12
            }
        },
        {
            "@type": "cdi:MeasureComponent",
            "cdi:isDefinedBy_InstanceVariable": {"@id": "xas:incidentIntensityVariable"},
            "cdi:has": {
                "@type": "cdi:ValueMapping",
                "cdi:hasIndex": 3,
                "cdi:haslength": 13
            }
        },
        {
            "@type": "cdi:MeasureComponent",
            "cdi:isDefinedBy_InstanceVariable": {"@id": "xas:transmittedIntensityVariable"},
            "cdi:has": {
                "@type": "cdi:ValueMapping",
                "cdi:hasIndex": 2,
                "cdi:haslength": 12
            }
        }
    ],
    "cdi:allowsDuplicates": false,
    "cdi:arrayBase": 1,
    "cdi:commentPrefix": "#",
    "cdi:hasHeader": true,
    "cdi:headerRowCount": 27,
    "cdi:skipInitialSpace": true,
    "cdi:isDelimited": false,
    "cdi:isFixedWidth": true
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org"
    },
    "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasXdiTabularTextDataset/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "xas": "https://xas.org/dictionary/"
    }
  ],
  "@id": "ex:xasXDIdownload_23463h",
  "@type": "cdi:WideDataStructure",
  "cdi:has_DataStructureComponent": [
    {
      "@type": "cdi:IdentifierComponent",
      "cdi:isDefinedBy_InstanceVariable": {
        "@id": "xas:monochromatorEnergyVariable"
      },
      "cdi:has": {
        "@type": "cdi:ValueMapping",
        "cdi:hasIndex": 1,
        "cdi:haslength": 12
      }
    },
    {
      "@type": "cdi:MeasureComponent",
      "cdi:isDefinedBy_InstanceVariable": {
        "@id": "xas:incidentIntensityVariable"
      },
      "cdi:has": {
        "@type": "cdi:ValueMapping",
        "cdi:hasIndex": 3,
        "cdi:haslength": 13
      }
    },
    {
      "@type": "cdi:MeasureComponent",
      "cdi:isDefinedBy_InstanceVariable": {
        "@id": "xas:transmittedIntensityVariable"
      },
      "cdi:has": {
        "@type": "cdi:ValueMapping",
        "cdi:hasIndex": 2,
        "cdi:haslength": 12
      }
    }
  ],
  "cdi:allowsDuplicates": false,
  "cdi:arrayBase": 1,
  "cdi:commentPrefix": "#",
  "cdi:hasHeader": true,
  "cdi:headerRowCount": 27,
  "cdi:skipInitialSpace": true,
  "cdi:isDelimited": false,
  "cdi:isFixedWidth": true
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix xas: <https://xas.org/dictionary/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:xasXDIdownload_23463h a cdi:WideDataStructure ;
    cdi:allowsDuplicates false ;
    cdi:arrayBase 1 ;
    cdi:commentPrefix "#" ;
    cdi:hasHeader true ;
    cdi:has_DataStructureComponent [ a cdi:MeasureComponent ;
            cdi:has [ a cdi:ValueMapping ;
                    cdi:hasIndex 3 ;
                    cdi:haslength 13 ] ;
            cdi:isDefinedBy_InstanceVariable xas:incidentIntensityVariable ],
        [ a cdi:MeasureComponent ;
            cdi:has [ a cdi:ValueMapping ;
                    cdi:hasIndex 2 ;
                    cdi:haslength 12 ] ;
            cdi:isDefinedBy_InstanceVariable xas:transmittedIntensityVariable ],
        [ a cdi:IdentifierComponent ;
            cdi:has [ a cdi:ValueMapping ;
                    cdi:hasIndex 1 ;
                    cdi:haslength 12 ] ;
            cdi:isDefinedBy_InstanceVariable xas:monochromatorEnergyVariable ] ;
    cdi:headerRowCount 27 ;
    cdi:isDelimited false ;
    cdi:isFixedWidth true ;
    cdi:skipInitialSpace true .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: definitions for roles used in XAS profile
type: object
properties:
  '@type':
    const: cdi:WideDataStructure
  cdi:has_DataStructureComponent:
    type: array
    items:
      type: object
      properties:
        '@type':
          oneOf:
          - const: cdi:IdentifierComponent
          - const: cdi:MeasureComponent
        cdi:isDefinedBy_InstanceVariable:
          type: object
          description: this must be a reference to a variable defined in the schema:variableMeasured
            part of the metadata record; This condition will need to be validated
            by SHACL rule
          properties:
            '@id':
              type: string
        cdi:has:
          type: object
          properties:
            '@type':
              const: cdi:ValueMapping
            cdi:hasIndex:
              type: integer
            cdi:haslength:
              type: integer
          required:
          - '@type'
      required:
      - cdi:isDefinedBy_InstanceVariable
      - cdi:has
  cdi:allowsDuplicates:
    type: boolean
    default: false
  cdi:arrayBase:
    type: integer
    default: 1
  cdi:commentPrefix:
    type: string
  cdi:hasHeader:
    type: boolean
  cdi:headerRowCount:
    type: integer
  cdi:skipInitialSpace:
    type: boolean
    default: true
  cdi:isDelimited:
    type: boolean
    default: false
  cdi:isFixedWidth:
    type: boolean
    default: true
required:
- '@type'
- cdi:has_DataStructureComponent
- cdi:hasHeader
- cdi:headerRowCount
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasXdiTabularTextDataset/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasXdiTabularTextDataset/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasXdiTabularTextDataset/context.jsonld)

## Sources

* [XDI Format specification](https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/xasProperties/xasXdiTabularTextDataset`

