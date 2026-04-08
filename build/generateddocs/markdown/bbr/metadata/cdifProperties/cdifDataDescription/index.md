
# CDIF Data Description (Schema)

`cdif.bbr.metadata.cdifProperties.cdifDataDescription` *v0.1*

Additional constraints for CDIF data description level. Adds cdi:physicalDataType requirement on variableMeasured items and distribution-level cdi properties for file characterization (characterSet, fileSize, fileSizeUofM). Used by CDIFDataDescriptionProfile and CDIFcompleteProfile profiles.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Additional constraints for CDIF data description level metadata. Adds the `cdi:physicalDataType` requirement on variableMeasured items (PropertyValue-type variables must specify their physical data type at this level). Also adds distribution-level CDI properties for file characterization: `cdi:characterSet`, `cdi:fileSize`, and `cdi:fileSizeUofM`.

## Examples

### Example CDIF Data Description record
Example dataset with data description level properties including variable types and distribution file characterization.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "csvw": "http://www.w3.org/ns/csvw#",
        "dcterms": "http://purl.org/dc/terms/",
        "dcat": "http://www.w3.org/ns/dcat#",
        "ex": "https://example.org/"
    },
    "@id": "ex:dataset_datadesc_001",
    "@type": ["schema:Dataset"],
    "schema:name": "Ocean Temperature Monitoring Data",
    "schema:identifier": "https://doi.org/10.1234/ocean-temp-2025",
    "schema:url": "https://example.org/datasets/ocean-temp-2025",
    "schema:dateModified": "2025-09-01",
    "schema:license": ["https://creativecommons.org/licenses/by/4.0/"],
    "schema:subjectOf": {
        "@type": ["schema:Dataset"],
        "schema:additionalType": ["dcat:CatalogRecord"],
        "@id": "ex:metadata_datadesc_001",
        "schema:about": {
            "@id": "ex:dataset_datadesc_001"
        },
        "dcterms:conformsTo": [
            {
                "@id": "https://w3id.org/cdif/data_description/1.0"
            }
        ]
    },
    "schema:variableMeasured": [
        {
            "@id": "ex:var_sea_water_temp",
            "@type": ["schema:PropertyValue", "cdi:InstanceVariable"],
            "schema:name": "sea_water_temperature",
            "schema:description": "Temperature of sea water at measurement depth",
            "schema:propertyID": [
                {
                    "@type": ["schema:DefinedTerm"],
                    "schema:name": "Sea Water Temperature",
                    "schema:identifier": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/",
                    "schema:inDefinedTermSet": "http://vocab.nerc.ac.uk/collection/P01/"
                }
            ],
            "schema:unitText": "degrees Celsius",
            "schema:unitCode": "CEL",
            "schema:minValue": -2.0,
            "schema:maxValue": 35.5,
            "schema:measurementTechnique": "CTD sensor",
            "cdi:physicalDataType": ["Numeric"],
            "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
            "cdi:role": "MeasureComponent",
            "cdi:name": "sea_water_temperature",
            "cdi:displayLabel": "Water Temperature",
            "cdi:describedUnitOfMeasure": {
                "@type": ["schema:DefinedTerm"],
                "schema:name": "degree Celsius",
                "schema:identifier": "http://qudt.org/vocab/unit/DEG_C"
            },
            "cdi:uses": [
                {
                    "@id": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
                }
            ]
        },
        {
            "@id": "ex:var_measurement_depth",
            "@type": ["schema:PropertyValue", "cdi:InstanceVariable"],
            "schema:name": "measurement_depth",
            "schema:description": "Depth below sea surface at which temperature was recorded",
            "schema:propertyID": [
                {
                    "@type": ["schema:DefinedTerm"],
                    "schema:name": "Depth",
                    "schema:identifier": "http://vocab.nerc.ac.uk/collection/P01/current/ADEPZZ01/"
                }
            ],
            "schema:unitText": "meters",
            "schema:unitCode": "MTR",
            "schema:minValue": 0,
            "schema:maxValue": 5000,
            "cdi:physicalDataType": ["Numeric"],
            "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
            "cdi:role": "DimensionComponent",
            "cdi:name": "measurement_depth",
            "cdi:displayLabel": "Measurement Depth",
            "cdi:simpleUnitOfMeasure": "m"
        },
        {
            "@id": "ex:var_station_id",
            "@type": ["schema:PropertyValue", "cdi:InstanceVariable"],
            "schema:name": "station_id",
            "schema:description": "Identifier for the monitoring station",
            "schema:propertyID": ["station_id"],
            "cdi:physicalDataType": ["String"],
            "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#string",
            "cdi:role": "DescriptorComponent",
            "cdi:name": "station_id",
            "cdi:identifier": "ex:var_station_id"
        }
    ],
    "schema:distribution": [
        {
            "@type": ["schema:DataDownload", "cdi:TabularTextDataSet"],
            "schema:name": "Ocean temperature CSV",
            "schema:contentUrl": "https://example.org/downloads/ocean-temp-2025.csv",
            "schema:encodingFormat": ["text/csv"],
            "cdi:characterSet": "UTF-8",
            "cdi:fileSize": 1.2,
            "cdi:fileSizeUofM": "MB",
            "cdi:isDelimited": true,
            "csvw:delimiter": ",",
            "csvw:header": true,
            "csvw:headerRowCount": 1,
            "csvw:skipRows": 0,
            "csvw:skipBlankRows": true,
            "csvw:commentPrefix": "#",
            "csvw:quoteChar": "\"",
            "csvw:trim": "true",
            "cdi:hasPhysicalMapping": [
                {
                    "cdi:index": 0,
                    "cdi:physicalDataType": "String",
                    "cdi:length": 20,
                    "cdi:isRequired": true,
                    "cdi:formats_InstanceVariable": {
                        "@id": "ex:var_station_id"
                    }
                },
                {
                    "cdi:index": 1,
                    "cdi:physicalDataType": "Numeric",
                    "cdi:format": "0.0",
                    "cdi:scale": 1,
                    "cdi:decimalPositions": 1,
                    "cdi:nullSequence": "-999.9",
                    "cdi:isRequired": true,
                    "cdi:formats_InstanceVariable": {
                        "@id": "ex:var_measurement_depth"
                    }
                },
                {
                    "cdi:index": 2,
                    "cdi:physicalDataType": "Numeric",
                    "cdi:format": "0.00",
                    "cdi:scale": 2,
                    "cdi:decimalPositions": 2,
                    "cdi:nullSequence": "-999.99",
                    "cdi:defaultValue": "NaN",
                    "cdi:minimumLength": 1,
                    "cdi:maximumLength": 10,
                    "cdi:isRequired": false,
                    "cdi:formats_InstanceVariable": {
                        "@id": "ex:var_sea_water_temp"
                    }
                }
            ]
        }
    ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataDescription/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:dataset_datadesc_001",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Ocean Temperature Monitoring Data",
  "schema:identifier": "https://doi.org/10.1234/ocean-temp-2025",
  "schema:url": "https://example.org/datasets/ocean-temp-2025",
  "schema:dateModified": "2025-09-01",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:metadata_datadesc_001",
    "schema:about": {
      "@id": "ex:dataset_datadesc_001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "@id": "ex:var_sea_water_temp",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "sea_water_temperature",
      "schema:description": "Temperature of sea water at measurement depth",
      "schema:propertyID": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "Sea Water Temperature",
          "schema:identifier": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/",
          "schema:inDefinedTermSet": "http://vocab.nerc.ac.uk/collection/P01/"
        }
      ],
      "schema:unitText": "degrees Celsius",
      "schema:unitCode": "CEL",
      "schema:minValue": -2.0,
      "schema:maxValue": 35.5,
      "schema:measurementTechnique": "CTD sensor",
      "cdi:physicalDataType": [
        "Numeric"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:name": "sea_water_temperature",
      "cdi:displayLabel": "Water Temperature",
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "degree Celsius",
        "schema:identifier": "http://qudt.org/vocab/unit/DEG_C"
      },
      "cdi:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
        }
      ]
    },
    {
      "@id": "ex:var_measurement_depth",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measurement_depth",
      "schema:description": "Depth below sea surface at which temperature was recorded",
      "schema:propertyID": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "Depth",
          "schema:identifier": "http://vocab.nerc.ac.uk/collection/P01/current/ADEPZZ01/"
        }
      ],
      "schema:unitText": "meters",
      "schema:unitCode": "MTR",
      "schema:minValue": 0,
      "schema:maxValue": 5000,
      "cdi:physicalDataType": [
        "Numeric"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "DimensionComponent",
      "cdi:name": "measurement_depth",
      "cdi:displayLabel": "Measurement Depth",
      "cdi:simpleUnitOfMeasure": "m"
    },
    {
      "@id": "ex:var_station_id",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "station_id",
      "schema:description": "Identifier for the monitoring station",
      "schema:propertyID": [
        "station_id"
      ],
      "cdi:physicalDataType": [
        "String"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#string",
      "cdi:role": "DescriptorComponent",
      "cdi:name": "station_id",
      "cdi:identifier": "ex:var_station_id"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:TabularTextDataSet"
      ],
      "schema:name": "Ocean temperature CSV",
      "schema:contentUrl": "https://example.org/downloads/ocean-temp-2025.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "cdi:characterSet": "UTF-8",
      "cdi:fileSize": 1.2,
      "cdi:fileSizeUofM": "MB",
      "cdi:isDelimited": true,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "csvw:skipRows": 0,
      "csvw:skipBlankRows": true,
      "csvw:commentPrefix": "#",
      "csvw:quoteChar": "\"",
      "csvw:trim": "true",
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:physicalDataType": "String",
          "cdi:length": 20,
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var_station_id"
          }
        },
        {
          "cdi:index": 1,
          "cdi:physicalDataType": "Numeric",
          "cdi:format": "0.0",
          "cdi:scale": 1,
          "cdi:decimalPositions": 1,
          "cdi:nullSequence": "-999.9",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var_measurement_depth"
          }
        },
        {
          "cdi:index": 2,
          "cdi:physicalDataType": "Numeric",
          "cdi:format": "0.00",
          "cdi:scale": 2,
          "cdi:decimalPositions": 2,
          "cdi:nullSequence": "-999.99",
          "cdi:defaultValue": "NaN",
          "cdi:minimumLength": 1,
          "cdi:maximumLength": 10,
          "cdi:isRequired": false,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var_sea_water_temp"
          }
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:dataset_datadesc_001 a schema1:Dataset ;
    schema1:dateModified "2025-09-01" ;
    schema1:distribution [ a cdi:TabularTextDataSet,
                schema1:DataDownload ;
            cdi:characterSet "UTF-8" ;
            cdi:fileSize 1.2e+00 ;
            cdi:fileSizeUofM "MB" ;
            cdi:hasPhysicalMapping [ cdi:formats_InstanceVariable ex:var_station_id ;
                    cdi:index 0 ;
                    cdi:isRequired true ;
                    cdi:length 20 ;
                    cdi:physicalDataType "String" ],
                [ cdi:decimalPositions 1 ;
                    cdi:format "0.0" ;
                    cdi:formats_InstanceVariable ex:var_measurement_depth ;
                    cdi:index 1 ;
                    cdi:isRequired true ;
                    cdi:nullSequence "-999.9" ;
                    cdi:physicalDataType "Numeric" ;
                    cdi:scale 1 ],
                [ cdi:decimalPositions 2 ;
                    cdi:defaultValue "NaN" ;
                    cdi:format "0.00" ;
                    cdi:formats_InstanceVariable ex:var_sea_water_temp ;
                    cdi:index 2 ;
                    cdi:isRequired false ;
                    cdi:maximumLength 10 ;
                    cdi:minimumLength 1 ;
                    cdi:nullSequence "-999.99" ;
                    cdi:physicalDataType "Numeric" ;
                    cdi:scale 2 ] ;
            cdi:isDelimited true ;
            schema1:contentUrl "https://example.org/downloads/ocean-temp-2025.csv" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "Ocean temperature CSV" ;
            csvw:commentPrefix "#" ;
            csvw:delimiter "," ;
            csvw:header true ;
            csvw:headerRowCount 1 ;
            csvw:quoteChar "\"" ;
            csvw:skipBlankRows true ;
            csvw:skipRows 0 ;
            csvw:trim "true" ] ;
    schema1:identifier "https://doi.org/10.1234/ocean-temp-2025" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:name "Ocean Temperature Monitoring Data" ;
    schema1:subjectOf ex:metadata_datadesc_001 ;
    schema1:url "https://example.org/datasets/ocean-temp-2025" ;
    schema1:variableMeasured ex:var_measurement_depth,
        ex:var_sea_water_temp,
        ex:var_station_id .

ex:metadata_datadesc_001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/data_description/1.0> ;
    schema1:about ex:dataset_datadesc_001 ;
    schema1:additionalType "dcat:CatalogRecord" .

ex:var_measurement_depth a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "Measurement Depth" ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:name "measurement_depth" ;
    cdi:physicalDataType "Numeric" ;
    cdi:role "DimensionComponent" ;
    cdi:simpleUnitOfMeasure "m" ;
    schema1:description "Depth below sea surface at which temperature was recorded" ;
    schema1:maxValue 5000 ;
    schema1:minValue 0 ;
    schema1:name "measurement_depth" ;
    schema1:propertyID [ a schema1:DefinedTerm ;
            schema1:identifier "http://vocab.nerc.ac.uk/collection/P01/current/ADEPZZ01/" ;
            schema1:name "Depth" ] ;
    schema1:unitCode "MTR" ;
    schema1:unitText "meters" .

ex:var_sea_water_temp a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:describedUnitOfMeasure [ a schema1:DefinedTerm ;
            schema1:identifier "http://qudt.org/vocab/unit/DEG_C" ;
            schema1:name "degree Celsius" ] ;
    cdi:displayLabel "Water Temperature" ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:name "sea_water_temperature" ;
    cdi:physicalDataType "Numeric" ;
    cdi:role "MeasureComponent" ;
    cdi:uses <http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/> ;
    schema1:description "Temperature of sea water at measurement depth" ;
    schema1:maxValue 3.55e+01 ;
    schema1:measurementTechnique "CTD sensor" ;
    schema1:minValue -2e+00 ;
    schema1:name "sea_water_temperature" ;
    schema1:propertyID [ a schema1:DefinedTerm ;
            schema1:identifier "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/" ;
            schema1:inDefinedTermSet "http://vocab.nerc.ac.uk/collection/P01/" ;
            schema1:name "Sea Water Temperature" ] ;
    schema1:unitCode "CEL" ;
    schema1:unitText "degrees Celsius" .

ex:var_station_id a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:identifier "ex:var_station_id" ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#string" ;
    cdi:name "station_id" ;
    cdi:physicalDataType "String" ;
    cdi:role "DescriptorComponent" ;
    schema1:description "Identifier for the monitoring station" ;
    schema1:name "station_id" ;
    schema1:propertyID "station_id" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Data Description properties
description: Additional constraints for CDIF data description level. Adds cdi:physicalDataType
  requirement on variableMeasured items and distribution-level cdi properties for
  file characterization (characterSet, fileSize, fileSizeUofM).
type: object
properties:
  schema:subjectOf:
    properties:
      dcterms:conformsTo:
        type: array
        items:
          type: object
          properties:
            '@id':
              type: string
              description: uri for specifications that this metadata record conforms
                to
        minItems: 1
        contains:
          type: object
          properties:
            '@id':
              const: https://w3id.org/cdif/data_description/1.0
  '@context':
    type: object
    description: Additional namespace prefix for data description properties.
    properties:
      csvw:
        const: http://www.w3.org/ns/csvw#
  schema:variableMeasured:
    type: array
    items:
      allOf:
      - type: object
        description: All variableMeasured items at data description level must have
          an @id and cdi:physicalDataType so physical mappings can reference them.
        properties:
          '@id':
            type: string
            description: URI identifier for this variable, used as the target of cdi:formats_InstanceVariable
              references in physical mappings.
        required:
        - '@id'
      - $ref: '#/$defs/cdifVariableMeasured'
  schema:distribution:
    items:
      properties:
        cdi:characterSet:
          type: string
          description: The character set used in the distribution (e.g., UTF-8, ASCII).
        cdi:fileSize:
          type: number
          description: The size of the distribution file.
        cdi:fileSizeUofM:
          type: string
          description: Unit of measure for the file size (e.g., bytes, KB, MB, GB).
$defs:
  cdifVariableMeasured:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifVariableMeasured/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataDescription/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataDescription/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "prov": "http://www.w3.org/ns/prov#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataDescription/context.jsonld)

## Sources

* [CDIF](https://cdif.codata.org/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifDataDescription`

