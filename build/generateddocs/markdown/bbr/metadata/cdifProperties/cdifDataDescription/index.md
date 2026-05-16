
# CDIF Data Description (Schema)

`cdif.bbr.metadata.cdifProperties.cdifDataDescription` *v0.1*

Additional constraints for CDIF data description level. Adds cdif:physicalDataType requirement on variableMeasured items and distribution-level cdi properties for file characterization (characterSet, fileSize, fileSizeUofM). Used by CDIFDataDescriptionProfile and CDIFcompleteProfile profiles.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Additional constraints for CDIF data description level metadata. Adds the `cdif:physicalDataType` requirement on variableMeasured items (PropertyValue-type variables must specify their physical data type at this level). Adds distribution-level properties: `cdif:hasPhysicalMapping` (per-field physical mappings linking measured variables to their physical representation, via the `cdifPhysicalMapping` building block) and the file-characterization properties `cdi:characterSet`, `cdif:fileSize`, and `cdif:fileSizeUofM`.

`cdi:isStructuredBy` is **not** part of the data description level — pointing a distribution at a full Data Structure node is a Data Structure profile concern. The data description level describes variables (`schema:variableMeasured` with `cdi:role`), the primary key (`cdif:hasPrimaryKey` on the dataset), summary statistics (`cdif:statistics`), and per-field physical mappings (`cdif:hasPhysicalMapping` on distributions).

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
      "cdif:physicalDataType": [
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
      "cdif:role": "Measure",
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
      "cdif:uses": [
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
      "cdif:physicalDataType": [
        "xsd:decimal"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Dimension",
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
      "cdif:physicalDataType": [
        "xsd:string"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#string",
      "cdif:role": "Descriptor",
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
      "cdif:physicalDataType": [
        "xsd:integer"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#integer",
      "cdif:role": "Attribute",
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
      "cdif:physicalDataType": [
        "xsd:string"
      ],
      "cdif:role": "ReferenceVariable",
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
      "cdif:fileSize": 1.2,
      "cdif:fileSizeUofM": "MB",
      "cdi:isDelimited": true,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "csvw:skipRows": 0,
      "csvw:skipBlankRows": true,
      "csvw:commentPrefix": "#",
      "csvw:quoteChar": "\"",
      "csvw:trim": "true",
      "cdif:hasPhysicalMapping": [
        {
          "cdif:index": 0,
          "cdif:physicalDataType": "String",
          "cdi:length": 20,
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/stationId"
          }
        },
        {
          "cdif:index": 1,
          "cdif:physicalDataType": "Numeric",
          "cdif:format": "0.0",
          "cdi:scale": 1,
          "cdi:decimalPositions": 1,
          "cdi:nullSequence": "-999.9",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/measurementDepth"
          }
        },
        {
          "cdif:index": 2,
          "cdif:physicalDataType": "Numeric",
          "cdif:format": "0.00",
          "cdi:scale": 2,
          "cdi:decimalPositions": 2,
          "cdi:nullSequence": "-999.99",
          "cdi:defaultValue": "NaN",
          "cdi:minimumLength": 1,
          "cdi:maximumLength": 10,
          "cdi:isRequired": false,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp"
          }
        },
        {
          "cdif:index": 3,
          "cdif:physicalDataType": "Integer",
          "cdi:isRequired": false,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/qcFlag"
          }
        },
        {
          "cdif:index": 4,
          "cdif:physicalDataType": "String",
          "cdi:isRequired": false,
          "cdif:formats_InstanceVariable": {
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
      "cdif:fileSize": 240.0,
      "cdif:fileSizeUofM": "MB",
      "cdif:hasPhysicalMapping": [
        {
          "cdif:index": 0,
          "cdif:physicalDataType": "float32",
          "cdif:locator": "/measurements/seaWaterTemperature",
          "cdi:nullSequence": "NaN",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp"
          }
        },
        {
          "cdif:index": 1,
          "cdif:physicalDataType": "float32",
          "cdif:locator": "/coordinates/depth",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
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
      "cdif:physicalDataType": [
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
      "cdif:role": "Measure",
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
      "cdif:uses": [
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
      "cdif:physicalDataType": [
        "xsd:decimal"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Dimension",
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
      "cdif:physicalDataType": [
        "xsd:string"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#string",
      "cdif:role": "Descriptor",
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
      "cdif:physicalDataType": [
        "xsd:integer"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#integer",
      "cdif:role": "Attribute",
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
      "cdif:physicalDataType": [
        "xsd:string"
      ],
      "cdif:role": "ReferenceVariable",
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
      "cdif:fileSize": 1.2,
      "cdif:fileSizeUofM": "MB",
      "cdi:isDelimited": true,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "csvw:skipRows": 0,
      "csvw:skipBlankRows": true,
      "csvw:commentPrefix": "#",
      "csvw:quoteChar": "\"",
      "csvw:trim": "true",
      "cdif:hasPhysicalMapping": [
        {
          "cdif:index": 0,
          "cdif:physicalDataType": "String",
          "cdi:length": 20,
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/stationId"
          }
        },
        {
          "cdif:index": 1,
          "cdif:physicalDataType": "Numeric",
          "cdif:format": "0.0",
          "cdi:scale": 1,
          "cdi:decimalPositions": 1,
          "cdi:nullSequence": "-999.9",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/measurementDepth"
          }
        },
        {
          "cdif:index": 2,
          "cdif:physicalDataType": "Numeric",
          "cdif:format": "0.00",
          "cdi:scale": 2,
          "cdi:decimalPositions": 2,
          "cdi:nullSequence": "-999.99",
          "cdi:defaultValue": "NaN",
          "cdi:minimumLength": 1,
          "cdi:maximumLength": 10,
          "cdi:isRequired": false,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp"
          }
        },
        {
          "cdif:index": 3,
          "cdif:physicalDataType": "Integer",
          "cdi:isRequired": false,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/qcFlag"
          }
        },
        {
          "cdif:index": 4,
          "cdif:physicalDataType": "String",
          "cdi:isRequired": false,
          "cdif:formats_InstanceVariable": {
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
      "cdif:fileSize": 240.0,
      "cdif:fileSizeUofM": "MB",
      "cdif:hasPhysicalMapping": [
        {
          "cdif:index": 0,
          "cdif:physicalDataType": "float32",
          "cdif:locator": "/measurements/seaWaterTemperature",
          "cdi:nullSequence": "NaN",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:dataset/oceanTemp2025/var/seaWaterTemp"
          }
        },
        {
          "cdif:index": 1,
          "cdif:physicalDataType": "float32",
          "cdif:locator": "/coordinates/depth",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
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
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/dataset/oceanTemp2025> a schema1:Dataset ;
    schema1:dateModified "2025-09-01" ;
    schema1:distribution [ a cdi:PhysicalDataSet,
                cdi:TabularTextDataSet,
                schema1:DataDownload ;
            cdi:characterSet "UTF-8" ;
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
            csvw:trim "true" ;
            cdif:fileSize 1.2e+00 ;
            cdif:fileSizeUofM "MB" ;
            cdif:hasPhysicalMapping [ cdi:decimalPositions 1 ;
                    cdi:isRequired true ;
                    cdi:nullSequence "-999.9" ;
                    cdi:scale 1 ;
                    cdif:format "0.0" ;
                    cdif:formats_InstanceVariable <https://example.org/dataset/oceanTemp2025/var/measurementDepth> ;
                    cdif:index 1 ;
                    cdif:physicalDataType "Numeric" ],
                [ cdi:isRequired false ;
                    cdif:formats_InstanceVariable <https://example.org/dataset/oceanTemp2025/var/sourceCruise> ;
                    cdif:index 4 ;
                    cdif:physicalDataType "String" ],
                [ cdi:decimalPositions 2 ;
                    cdi:defaultValue "NaN" ;
                    cdi:isRequired false ;
                    cdi:maximumLength 10 ;
                    cdi:minimumLength 1 ;
                    cdi:nullSequence "-999.99" ;
                    cdi:scale 2 ;
                    cdif:format "0.00" ;
                    cdif:formats_InstanceVariable <https://example.org/dataset/oceanTemp2025/var/seaWaterTemp> ;
                    cdif:index 2 ;
                    cdif:physicalDataType "Numeric" ],
                [ cdi:isRequired false ;
                    cdif:formats_InstanceVariable <https://example.org/dataset/oceanTemp2025/var/qcFlag> ;
                    cdif:index 3 ;
                    cdif:physicalDataType "Integer" ],
                [ cdi:isRequired true ;
                    cdi:length 20 ;
                    cdif:formats_InstanceVariable <https://example.org/dataset/oceanTemp2025/var/stationId> ;
                    cdif:index 0 ;
                    cdif:physicalDataType "String" ] ],
        [ a cdi:PhysicalDataSet,
                cdi:StructuredDataSet,
                schema1:DataDownload ;
            cdi:characterSet "UTF-8" ;
            schema1:contentUrl "https://example.org/downloads/ocean-temp-2025.nc" ;
            schema1:encodingFormat "application/x-netcdf" ;
            schema1:name "Ocean temperature NetCDF cube" ;
            cdif:fileSize 2.4e+02 ;
            cdif:fileSizeUofM "MB" ;
            cdif:hasPhysicalMapping [ cdi:isRequired true ;
                    cdif:formats_InstanceVariable <https://example.org/dataset/oceanTemp2025/var/measurementDepth> ;
                    cdif:index 1 ;
                    cdif:locator "/coordinates/depth" ;
                    cdif:physicalDataType "float32" ],
                [ cdi:isRequired true ;
                    cdi:nullSequence "NaN" ;
                    cdif:formats_InstanceVariable <https://example.org/dataset/oceanTemp2025/var/seaWaterTemp> ;
                    cdif:index 0 ;
                    cdif:locator "/measurements/seaWaterTemperature" ;
                    cdif:physicalDataType "float32" ] ] ;
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
    cdi:qualifies <https://example.org/dataset/oceanTemp2025/var/seaWaterTemp> ;
    schema1:description "QARTOD-style quality control flag for the temperature observation" ;
    schema1:name "qc_flag" ;
    schema1:propertyID "qc_flag" ;
    cdif:physicalDataType "xsd:integer" ;
    cdif:role "Attribute" .

<https://example.org/dataset/oceanTemp2025/var/sourceCruise> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "Source Cruise" ;
    cdi:name "source_cruise" ;
    schema1:description "Reference to the source cruise that produced this observation" ;
    schema1:name "source_cruise" ;
    schema1:propertyID "source_cruise" ;
    cdif:physicalDataType "xsd:string" ;
    cdif:role "ReferenceVariable" .

<https://example.org/dataset/oceanTemp2025/var/stationId> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:identifier "ex:dataset/oceanTemp2025/var/stationId" ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#string" ;
    cdi:name "station_id" ;
    schema1:description "Identifier for the monitoring station" ;
    schema1:name "station_id" ;
    schema1:propertyID "station_id" ;
    cdif:physicalDataType "xsd:string" ;
    cdif:role "Descriptor" .

<https://example.org/dataset/oceanTemp2025/var/measurementDepth> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "Measurement Depth" ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:name "measurement_depth" ;
    cdi:simpleUnitOfMeasure "m" ;
    schema1:description "Depth below sea surface at which temperature was recorded" ;
    schema1:maxValue 5000 ;
    schema1:minValue 0 ;
    schema1:name "measurement_depth" ;
    schema1:propertyID [ a schema1:DefinedTerm ;
            schema1:identifier "http://vocab.nerc.ac.uk/collection/P01/current/ADEPZZ01/" ;
            schema1:name "Depth" ] ;
    schema1:unitCode "MTR" ;
    schema1:unitText "meters" ;
    cdif:physicalDataType "xsd:decimal" ;
    cdif:role "Dimension" .

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
    cdi:simpleUnitOfMeasure "Cel" ;
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
    schema1:url "https://example.org/datasets/ocean-temp-2025/variables/sea_water_temperature" ;
    cdif:physicalDataType [ a schema1:DefinedTerm ;
            schema1:identifier "http://www.w3.org/2001/XMLSchema#decimal" ;
            schema1:name "decimal" ],
        xsd:decimal,
        "xsd:decimal" ;
    cdif:role "Measure" ;
    cdif:uses [ a schema1:DefinedTerm ;
            schema1:identifier "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/" ;
            schema1:name "Sea water temperature" ],
        <http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/>,
        "sea-water-temperature" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Data Description properties
description: Additional constraints for CDIF data description level. Adds cdif:physicalDataType
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
  cdif:statistics:
    type: array
    description: "Summary statistics describing the dataset's values. Each entry is
      a cdi:Statistics bundle (one or more Statistic value objects, optionally weighted
      by an InstanceVariable, optionally broken down by Category) or a cdi:StatisticsCollection
      (groups multiple Statistics nodes and records which InstanceVariables they index).
      Inline node or @id-reference to one declared elsewhere in the document. cdif:
      namespaced \u2014 DDI-CDI has no `statistics` association from a dataset; this
      is a CDIF attachment property."
    items:
      anyOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifStatistics/schema.yaml
      - type: object
        properties:
          '@id':
            type: string
        required:
        - '@id'
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
          an @id and cdif:physicalDataType so physical mappings can reference them.
        properties:
          '@id':
            type: string
            description: URI identifier for this variable, used as the target of cdif:formats_InstanceVariable
              references in physical mappings.
        required:
        - '@id'
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifInstanceVariable/schema.yaml
      - type: object
        description: At the Data Description profile level, InstanceVariables may
          also carry substantive and sentinel value domains directly (in profiles
          that introduce a RepresentedVariable - e.g., CDIFDataStructureProfile -
          these properties live on the RepresentedVariable instead and are disallowed
          here).
        properties:
          cdi:takesSentinelValuesFrom:
            type: array
            items:
              anyOf:
              - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifValueDomain/schema.yaml#/$defs/SentinelValueDomain
              - type: object
                properties:
                  '@id':
                    type: string
                required:
                - '@id'
            description: Sentinel (missing / not-applicable) value domain(s) for this
              variable (RepresentedVariable.takesSentinelValuesFrom).
          cdi:takesSubstantiveValuesFrom:
            anyOf:
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifValueDomain/schema.yaml#/$defs/SubstantiveValueDomain
            - type: object
              properties:
                '@id':
                  type: string
              required:
              - '@id'
            description: The substantive value domain for this variable - the set
              of valid, meaningful values (RepresentedVariable.takesSubstantiveValuesFrom).
  schema:distribution:
    description: 'Each schema:DataDownload distribution item SHOULD additionally be
      typed as cdi:PhysicalDataSet or one of its subclasses (cdi:TabularTextDataSet,
      cdi:StructuredDataSet). schema:WebAPI distribution items do not require a cdi:
      dataset type. Not enforced at schema level (the merge with cdifCore and cdifArchiveDistribution
      drops the @type constraint at profile resolution); consider a SHACL rule if
      runtime enforcement is needed.'
    items:
      properties:
        cdif:hasPhysicalMapping:
          type: array
          description: Per-field physical mappings linking the variables measured
            by this distribution to their physical representation in the file - column
            index, format, physical data type, length, null sequence, etc. Applies
            to schema:DataDownload items typed as cdi:PhysicalDataSet or one of its
            subclasses. Each item is a cdifPhysicalMapping.
          items:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifPhysicalMapping/schema.yaml
        cdi:characterSet:
          type: string
          description: The character set used in the distribution (e.g., UTF-8, ASCII).
        cdif:fileSize:
          type: number
          description: The size of the distribution file.
        cdif:fileSizeUofM:
          type: string
          description: Unit of measure for the file size (e.g., bytes, KB, MB, GB).
        schema:potentialAction:
          description: For schema:WebAPI distributions, the potentialAction.result
            describes the physical realization of the API response bytes - analogous
            to a DataDownload distribution. The result MAY be additionally typed as
            cdi:PhysicalDataSet or one of its subclasses, and MAY carry the same physical-realization
            properties (cdif:hasPhysicalMapping, cdi:characterSet, cdif:fileSize,
            cdif:fileSizeUofM) as a DataDownload distribution. cdi:PhysicalDataSet
            typing belongs on the result, NOT on the WebAPI distribution itself -
            the WebAPI distribution describes the service; the result describes the
            bytes the service produces.
          items:
            properties:
              schema:result:
                properties:
                  cdif:hasPhysicalMapping:
                    type: array
                    description: Per-field physical mappings for the API response
                      bytes. cdif:formats_InstanceVariable should reference the @ids
                      of variables in the parent dataset's schema:variableMeasured
                      (the API response is another physical realization of those same
                      InstanceVariables).
                    items:
                      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifPhysicalMapping/schema.yaml
                  cdi:characterSet:
                    type: string
                    description: The character set used in the API response (e.g.,
                      UTF-8).
                  cdif:fileSize:
                    type: number
                    description: The size of the API response payload.
                  cdif:fileSizeUofM:
                    type: string
                    description: Unit of measure for the response size (e.g., bytes,
                      KB, MB).
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
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "ada": "https://ada.astromat.org/metadata/",
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

