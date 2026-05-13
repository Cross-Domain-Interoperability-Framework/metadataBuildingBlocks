
# CDIF Data Description (Schema)

`cdif.bbr.metadata.cdifProperties.cdifDataDescription` *v0.1*

Additional constraints for CDIF data description level. Adds cdi:physicalDataType requirement on variableMeasured items and distribution-level cdi properties for file characterization (characterSet, fileSize, fileSizeUofM). Used by CDIFDataDescriptionProfile and CDIFcompleteProfile profiles.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Additional constraints for CDIF data description level metadata. Adds the `cdi:physicalDataType` requirement on variableMeasured items (PropertyValue-type variables must specify their physical data type at this level). Also adds distribution-level CDI properties for file characterization: `cdi:characterSet`, `cdi:fileSize`, and `cdi:fileSizeUofM`.

## Examples

### Minimal CDIF Data Description
Bare schema:Dataset claiming conformance to the CDIF data_description
profile via schema:subjectOf, with one InstanceVariable carrying the
minimum required CdifInstanceVariableNode shape.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/"
  },
  "@type": ["schema:Dataset"],
  "@id": "ex:dataset/minimal-dd",
  "schema:name": "Minimal data-description example",
  "schema:subjectOf": {
    "dcterms:conformsTo": [
      { "@id": "https://w3id.org/cdif/data_description/1.0" }
    ]
  },
  "schema:variableMeasured": [
    {
      "@type": ["cdi:InstanceVariable", "schema:PropertyValue"],
      "@id": "ex:var/temperature",
      "schema:name": "temperature",
      "cdi:name": [
        {
          "@type": ["cdi:ObjectName"],
          "cdi:name": "temperature"
        }
      ],
      "cdi:definition": {
        "@type": ["cdi:InternationalString"],
        "cdi:languageSpecificString": [
          {
            "@type": ["cdi:LanguageString"],
            "cdi:content": "Air temperature measurement.",
            "cdi:language": "en"
          }
        ]
      },
      "cdi:takesSubstantiveValuesFrom": { "@id": "ex:value-domain/decimal" }
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataDescription/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "schema:Dataset"
  ],
  "@id": "ex:dataset/minimal-dd",
  "schema:name": "Minimal data-description example",
  "schema:subjectOf": {
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "@id": "ex:var/temperature",
      "schema:name": "temperature",
      "cdi:name": [
        {
          "@type": [
            "cdi:ObjectName"
          ],
          "cdi:name": "temperature"
        }
      ],
      "cdi:definition": {
        "@type": [
          "cdi:InternationalString"
        ],
        "cdi:languageSpecificString": [
          {
            "@type": [
              "cdi:LanguageString"
            ],
            "cdi:content": "Air temperature measurement.",
            "cdi:language": "en"
          }
        ]
      },
      "cdi:takesSubstantiveValuesFrom": {
        "@id": "ex:value-domain/decimal"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/dataset/minimal-dd> a schema1:Dataset ;
    schema1:name "Minimal data-description example" ;
    schema1:subjectOf [ dcterms:conformsTo <https://w3id.org/cdif/data_description/1.0> ] ;
    schema1:variableMeasured <https://example.org/var/temperature> .

<https://example.org/var/temperature> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:definition [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Air temperature measurement." ;
                    cdi:language "en" ] ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "temperature" ] ;
    cdi:takesSubstantiveValuesFrom <https://example.org/value-domain/decimal> ;
    schema1:name "temperature" .


```


### Complete CDIF Data Description
Ocean-temperature dataset with full data-description level properties
including variable types, distribution file characterization (charset,
fileSize, fileSizeUofM), and full schema:subjectOf CatalogRecord.
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
  "@id": "ex:dataset/oceanTemp2025",
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
    "@id": "ex:dataset/oceanTemp2025/metadata",
    "schema:about": {
      "@id": "ex:dataset/oceanTemp2025"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "sea_water_temperature",
      "schema:alternateName": [
        "sst",
        "TEMPST01"
      ],
      "schema:description": "Temperature of sea water at measurement depth",
      "schema:propertyID": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "Sea Water Temperature",
          "schema:identifier": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/",
          "schema:inDefinedTermSet": "http://vocab.nerc.ac.uk/collection/P01/"
        },
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
        },
        "TEMPST01"
      ],
      "schema:unitText": "degrees Celsius",
      "schema:unitCode": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "degree Celsius",
        "schema:identifier": "http://qudt.org/vocab/unit/DEG_C",
        "schema:inDefinedTermSet": "http://qudt.org/vocab/unit/"
      },
      "schema:minValue": -2.0,
      "schema:maxValue": 35.5,
      "schema:measurementTechnique": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "CTD sensor",
        "schema:identifier": "https://example.org/techniques/ctd"
      },
      "schema:url": "https://example.org/datasets/ocean-temp-2025/variables/sea_water_temperature",
      "cdi:identifier": "ex:dataset/oceanTemp2025/var/seaWaterTemp",
      "cdi:physicalDataType": [
        "xsd:decimal",
        {
          "@id": "http://www.w3.org/2001/XMLSchema#decimal"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "decimal",
          "schema:identifier": "http://www.w3.org/2001/XMLSchema#decimal"
        }
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "Measure",
      "cdi:name": "sea_water_temperature",
      "cdi:displayLabel": "Sea Water Temperature",
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "degree Celsius",
        "schema:identifier": "http://qudt.org/vocab/unit/DEG_C",
        "schema:inDefinedTermSet": "http://qudt.org/vocab/unit/"
      },
      "cdi:simpleUnitOfMeasure": "Cel",
      "cdi:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
        },
        "sea-water-temperature",
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "Sea water temperature",
          "schema:identifier": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
        }
      ]
    },
    {
      "@id": "ex:dataset/oceanTemp2025/var/measurementDepth",
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
        "xsd:decimal"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "Dimension",
      "cdi:name": "measurement_depth",
      "cdi:displayLabel": "Measurement Depth",
      "cdi:simpleUnitOfMeasure": "m"
    },
    {
      "@id": "ex:dataset/oceanTemp2025/var/stationId",
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
        "xsd:string"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#string",
      "cdi:role": "Descriptor",
      "cdi:name": "station_id",
      "cdi:identifier": "ex:dataset/oceanTemp2025/var/stationId"
    },
    {
      "@id": "ex:dataset/oceanTemp2025/var/qcFlag",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "qc_flag",
      "schema:description": "QARTOD-style quality control flag for the temperature observation",
      "schema:propertyID": [
        "qc_flag"
      ],
      "cdi:physicalDataType": [
        "xsd:integer"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#integer",
      "cdi:role": "Attribute",
      "cdi:name": "qc_flag",
      "cdi:displayLabel": "QC flag",
      "cdi:qualifies": {
        "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp"
      }
    },
    {
      "@id": "ex:dataset/oceanTemp2025/var/sourceCruise",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "source_cruise",
      "schema:description": "Reference to the source cruise that produced this observation",
      "schema:propertyID": [
        "source_cruise"
      ],
      "cdi:physicalDataType": [
        "xsd:string"
      ],
      "cdi:role": "ReferenceVariable",
      "cdi:name": "source_cruise",
      "cdi:displayLabel": "Source Cruise"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:TabularTextDataSet",
        "cdi:PhysicalDataSet"
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
            "@id": "ex:dataset/oceanTemp2025/var/stationId"
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
            "@id": "ex:dataset/oceanTemp2025/var/measurementDepth"
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
            "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp"
          }
        },
        {
          "cdi:index": 3,
          "cdi:physicalDataType": "Integer",
          "cdi:isRequired": false,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/qcFlag"
          }
        },
        {
          "cdi:index": 4,
          "cdi:physicalDataType": "String",
          "cdi:isRequired": false,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/sourceCruise"
          }
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload",
        "cdi:StructuredDataSet",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "Ocean temperature NetCDF cube",
      "schema:contentUrl": "https://example.org/downloads/ocean-temp-2025.nc",
      "schema:encodingFormat": [
        "application/x-netcdf"
      ],
      "cdi:characterSet": "UTF-8",
      "cdi:fileSize": 240.0,
      "cdi:fileSizeUofM": "MB",
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/measurements/seaWaterTemperature",
          "cdi:nullSequence": "NaN",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp"
          }
        },
        {
          "cdi:index": 1,
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/coordinates/depth",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/measurementDepth"
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
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    },
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
  "@id": "ex:dataset/oceanTemp2025",
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
    "@id": "ex:dataset/oceanTemp2025/metadata",
    "schema:about": {
      "@id": "ex:dataset/oceanTemp2025"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "sea_water_temperature",
      "schema:alternateName": [
        "sst",
        "TEMPST01"
      ],
      "schema:description": "Temperature of sea water at measurement depth",
      "schema:propertyID": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "Sea Water Temperature",
          "schema:identifier": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/",
          "schema:inDefinedTermSet": "http://vocab.nerc.ac.uk/collection/P01/"
        },
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
        },
        "TEMPST01"
      ],
      "schema:unitText": "degrees Celsius",
      "schema:unitCode": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "degree Celsius",
        "schema:identifier": "http://qudt.org/vocab/unit/DEG_C",
        "schema:inDefinedTermSet": "http://qudt.org/vocab/unit/"
      },
      "schema:minValue": -2.0,
      "schema:maxValue": 35.5,
      "schema:measurementTechnique": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "CTD sensor",
        "schema:identifier": "https://example.org/techniques/ctd"
      },
      "schema:url": "https://example.org/datasets/ocean-temp-2025/variables/sea_water_temperature",
      "cdi:identifier": "ex:dataset/oceanTemp2025/var/seaWaterTemp",
      "cdi:physicalDataType": [
        "xsd:decimal",
        {
          "@id": "http://www.w3.org/2001/XMLSchema#decimal"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "decimal",
          "schema:identifier": "http://www.w3.org/2001/XMLSchema#decimal"
        }
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "Measure",
      "cdi:name": "sea_water_temperature",
      "cdi:displayLabel": "Sea Water Temperature",
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "degree Celsius",
        "schema:identifier": "http://qudt.org/vocab/unit/DEG_C",
        "schema:inDefinedTermSet": "http://qudt.org/vocab/unit/"
      },
      "cdi:simpleUnitOfMeasure": "Cel",
      "cdi:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
        },
        "sea-water-temperature",
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "Sea water temperature",
          "schema:identifier": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
        }
      ]
    },
    {
      "@id": "ex:dataset/oceanTemp2025/var/measurementDepth",
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
        "xsd:decimal"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "Dimension",
      "cdi:name": "measurement_depth",
      "cdi:displayLabel": "Measurement Depth",
      "cdi:simpleUnitOfMeasure": "m"
    },
    {
      "@id": "ex:dataset/oceanTemp2025/var/stationId",
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
        "xsd:string"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#string",
      "cdi:role": "Descriptor",
      "cdi:name": "station_id",
      "cdi:identifier": "ex:dataset/oceanTemp2025/var/stationId"
    },
    {
      "@id": "ex:dataset/oceanTemp2025/var/qcFlag",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "qc_flag",
      "schema:description": "QARTOD-style quality control flag for the temperature observation",
      "schema:propertyID": [
        "qc_flag"
      ],
      "cdi:physicalDataType": [
        "xsd:integer"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#integer",
      "cdi:role": "Attribute",
      "cdi:name": "qc_flag",
      "cdi:displayLabel": "QC flag",
      "cdi:qualifies": {
        "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp"
      }
    },
    {
      "@id": "ex:dataset/oceanTemp2025/var/sourceCruise",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "source_cruise",
      "schema:description": "Reference to the source cruise that produced this observation",
      "schema:propertyID": [
        "source_cruise"
      ],
      "cdi:physicalDataType": [
        "xsd:string"
      ],
      "cdi:role": "ReferenceVariable",
      "cdi:name": "source_cruise",
      "cdi:displayLabel": "Source Cruise"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:TabularTextDataSet",
        "cdi:PhysicalDataSet"
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
            "@id": "ex:dataset/oceanTemp2025/var/stationId"
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
            "@id": "ex:dataset/oceanTemp2025/var/measurementDepth"
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
            "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp"
          }
        },
        {
          "cdi:index": 3,
          "cdi:physicalDataType": "Integer",
          "cdi:isRequired": false,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/qcFlag"
          }
        },
        {
          "cdi:index": 4,
          "cdi:physicalDataType": "String",
          "cdi:isRequired": false,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/sourceCruise"
          }
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload",
        "cdi:StructuredDataSet",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "Ocean temperature NetCDF cube",
      "schema:contentUrl": "https://example.org/downloads/ocean-temp-2025.nc",
      "schema:encodingFormat": [
        "application/x-netcdf"
      ],
      "cdi:characterSet": "UTF-8",
      "cdi:fileSize": 240.0,
      "cdi:fileSizeUofM": "MB",
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/measurements/seaWaterTemperature",
          "cdi:nullSequence": "NaN",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp"
          }
        },
        {
          "cdi:index": 1,
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/coordinates/depth",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/measurementDepth"
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/dataset/oceanTemp2025> a schema1:Dataset ;
    schema1:dateModified "2025-09-01" ;
    schema1:distribution [ a cdi:PhysicalDataSet,
                cdi:StructuredDataSet,
                schema1:DataDownload ;
            cdi:characterSet "UTF-8" ;
            cdi:fileSize 2.4e+02 ;
            cdi:fileSizeUofM "MB" ;
            cdi:hasPhysicalMapping [ cdi:formats_InstanceVariable <https://example.org/dataset/oceanTemp2025/var/measurementDepth> ;
                    cdi:index 1 ;
                    cdi:isRequired true ;
                    cdi:locator "/coordinates/depth" ;
                    cdi:physicalDataType "float32" ],
                [ cdi:formats_InstanceVariable <https://example.org/dataset/oceanTemp2025/var/seaWaterTemp> ;
                    cdi:index 0 ;
                    cdi:isRequired true ;
                    cdi:locator "/measurements/seaWaterTemperature" ;
                    cdi:nullSequence "NaN" ;
                    cdi:physicalDataType "float32" ] ;
            schema1:contentUrl "https://example.org/downloads/ocean-temp-2025.nc" ;
            schema1:encodingFormat "application/x-netcdf" ;
            schema1:name "Ocean temperature NetCDF cube" ],
        [ a cdi:PhysicalDataSet,
                cdi:TabularTextDataSet,
                schema1:DataDownload ;
            cdi:characterSet "UTF-8" ;
            cdi:fileSize 1.2e+00 ;
            cdi:fileSizeUofM "MB" ;
            cdi:hasPhysicalMapping [ cdi:decimalPositions 2 ;
                    cdi:defaultValue "NaN" ;
                    cdi:format "0.00" ;
                    cdi:formats_InstanceVariable <https://example.org/dataset/oceanTemp2025/var/seaWaterTemp> ;
                    cdi:index 2 ;
                    cdi:isRequired false ;
                    cdi:maximumLength 10 ;
                    cdi:minimumLength 1 ;
                    cdi:nullSequence "-999.99" ;
                    cdi:physicalDataType "Numeric" ;
                    cdi:scale 2 ],
                [ cdi:formats_InstanceVariable <https://example.org/dataset/oceanTemp2025/var/stationId> ;
                    cdi:index 0 ;
                    cdi:isRequired true ;
                    cdi:length 20 ;
                    cdi:physicalDataType "String" ],
                [ cdi:decimalPositions 1 ;
                    cdi:format "0.0" ;
                    cdi:formats_InstanceVariable <https://example.org/dataset/oceanTemp2025/var/measurementDepth> ;
                    cdi:index 1 ;
                    cdi:isRequired true ;
                    cdi:nullSequence "-999.9" ;
                    cdi:physicalDataType "Numeric" ;
                    cdi:scale 1 ],
                [ cdi:formats_InstanceVariable <https://example.org/dataset/oceanTemp2025/var/qcFlag> ;
                    cdi:index 3 ;
                    cdi:isRequired false ;
                    cdi:physicalDataType "Integer" ],
                [ cdi:formats_InstanceVariable <https://example.org/dataset/oceanTemp2025/var/sourceCruise> ;
                    cdi:index 4 ;
                    cdi:isRequired false ;
                    cdi:physicalDataType "String" ] ;
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
    schema1:subjectOf <https://example.org/dataset/oceanTemp2025/metadata> ;
    schema1:url "https://example.org/datasets/ocean-temp-2025" ;
    schema1:variableMeasured <https://example.org/dataset/oceanTemp2025/var/measurementDepth>,
        <https://example.org/dataset/oceanTemp2025/var/qcFlag>,
        <https://example.org/dataset/oceanTemp2025/var/seaWaterTemp>,
        <https://example.org/dataset/oceanTemp2025/var/sourceCruise>,
        <https://example.org/dataset/oceanTemp2025/var/stationId> .

<https://example.org/dataset/oceanTemp2025/metadata> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/data_description/1.0> ;
    schema1:about <https://example.org/dataset/oceanTemp2025> ;
    schema1:additionalType "dcat:CatalogRecord" .

<https://example.org/dataset/oceanTemp2025/var/qcFlag> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "QC flag" ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#integer" ;
    cdi:name "qc_flag" ;
    cdi:physicalDataType "xsd:integer" ;
    cdi:qualifies <https://example.org/dataset/oceanTemp2025/var/seaWaterTemp> ;
    cdi:role "Attribute" ;
    schema1:description "QARTOD-style quality control flag for the temperature observation" ;
    schema1:name "qc_flag" ;
    schema1:propertyID "qc_flag" .

<https://example.org/dataset/oceanTemp2025/var/sourceCruise> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "Source Cruise" ;
    cdi:name "source_cruise" ;
    cdi:physicalDataType "xsd:string" ;
    cdi:role "ReferenceVariable" ;
    schema1:description "Reference to the source cruise that produced this observation" ;
    schema1:name "source_cruise" ;
    schema1:propertyID "source_cruise" .

<https://example.org/dataset/oceanTemp2025/var/stationId> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:identifier "ex:dataset/oceanTemp2025/var/stationId" ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#string" ;
    cdi:name "station_id" ;
    cdi:physicalDataType "xsd:string" ;
    cdi:role "Descriptor" ;
    schema1:description "Identifier for the monitoring station" ;
    schema1:name "station_id" ;
    schema1:propertyID "station_id" .

<https://example.org/dataset/oceanTemp2025/var/measurementDepth> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "Measurement Depth" ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:name "measurement_depth" ;
    cdi:physicalDataType "xsd:decimal" ;
    cdi:role "Dimension" ;
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

<https://example.org/dataset/oceanTemp2025/var/seaWaterTemp> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:describedUnitOfMeasure [ a schema1:DefinedTerm ;
            schema1:identifier "http://qudt.org/vocab/unit/DEG_C" ;
            schema1:inDefinedTermSet "http://qudt.org/vocab/unit/" ;
            schema1:name "degree Celsius" ] ;
    cdi:displayLabel "Sea Water Temperature" ;
    cdi:identifier "ex:dataset/oceanTemp2025/var/seaWaterTemp" ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:name "sea_water_temperature" ;
    cdi:physicalDataType [ a schema1:DefinedTerm ;
            schema1:identifier "http://www.w3.org/2001/XMLSchema#decimal" ;
            schema1:name "decimal" ],
        xsd:decimal,
        "xsd:decimal" ;
    cdi:role "Measure" ;
    cdi:simpleUnitOfMeasure "Cel" ;
    cdi:uses [ a schema1:DefinedTerm ;
            schema1:identifier "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/" ;
            schema1:name "Sea water temperature" ],
        <http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/>,
        "sea-water-temperature" ;
    schema1:alternateName "TEMPST01",
        "sst" ;
    schema1:description "Temperature of sea water at measurement depth" ;
    schema1:maxValue 3.55e+01 ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://example.org/techniques/ctd" ;
            schema1:name "CTD sensor" ] ;
    schema1:minValue -2e+00 ;
    schema1:name "sea_water_temperature" ;
    schema1:propertyID [ a schema1:DefinedTerm ;
            schema1:identifier "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/" ;
            schema1:inDefinedTermSet "http://vocab.nerc.ac.uk/collection/P01/" ;
            schema1:name "Sea Water Temperature" ],
        <http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/>,
        "TEMPST01" ;
    schema1:unitCode [ a schema1:DefinedTerm ;
            schema1:identifier "http://qudt.org/vocab/unit/DEG_C" ;
            schema1:inDefinedTermSet "http://qudt.org/vocab/unit/" ;
            schema1:name "degree Celsius" ] ;
    schema1:unitText "degrees Celsius" ;
    schema1:url "https://example.org/datasets/ocean-temp-2025/variables/sea_water_temperature" .


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
  cdif:hasPrimaryKey:
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifKey/schema.yaml
    - type: object
      description: object reference via URI or URI fragment to a cdif:Key defined
        elsewhere in the same document
      properties:
        '@id':
          type: string
      required:
      - '@id'
    description: 'Primary key of the dataset: a cdif:Key whose cdif:isComposedOf is
      an ordered list of cdi:InstanceVariables (from schema:variableMeasured) that
      uniquely identify each data instance.'
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
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifInstanceVariable/schema.yaml
  schema:distribution:
    items:
      properties:
        '@type':
          description: Each distribution item is additionally typed as a cdi:PhysicalDataSet
            or cdi:LogicalDataSet (alongside the base schema:DataDownload / schema:WebAPI).
          anyOf:
          - contains:
              const: cdi:PhysicalDataSet
          - contains:
              const: cdi:LogicalDataSet
        cdi:isStructuredBy:
          description: Points at the Data Structure node that describes how this distribution's
            bytes are organized. Inline cdifDataStructure or @id-reference to a node
            defined elsewhere in the document.
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructure/schema.yaml
          - type: object
            properties:
              '@id':
                type: string
            required:
            - '@id'
        cdi:characterSet:
          type: string
          description: The character set used in the distribution (e.g., UTF-8, ASCII).
        cdi:fileSize:
          type: number
          description: The size of the distribution file.
        cdi:fileSizeUofM:
          type: string
          description: Unit of measure for the file size (e.g., bytes, KB, MB, GB).
required:
- schema:variableMeasured

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
    "cdif": "https://cdif.org/0.1/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
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

