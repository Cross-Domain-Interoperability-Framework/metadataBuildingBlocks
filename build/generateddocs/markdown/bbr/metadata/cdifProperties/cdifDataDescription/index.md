
# CDIF Data Description (Schema)

`cdif.bbr.metadata.cdifProperties.cdifDataDescription` *v0.1*

Additional constraints for CDIF data description level. Adds cdi:physicalDataType requirement on variableMeasured items and distribution-level cdi properties for file characterization (characterSet, fileSize, fileSizeUofM). Used by CDIFDataDescription and CDIFcomplete profiles.

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
                "@id": "https://w3id.org/cdif/data_description/1.0/"
            }
        ]
    },
    "schema:variableMeasured": [
        {
            "@type": ["schema:PropertyValue", "cdi:InstanceVariable"],
            "schema:name": "sea_water_temperature",
            "schema:description": "Temperature of sea water at measurement depth",
            "schema:unitText": "degrees Celsius",
            "schema:unitCode": "CEL",
            "cdi:physicalDataType": "Numeric"
        },
        {
            "@type": ["schema:PropertyValue", "cdi:InstanceVariable"],
            "schema:name": "measurement_depth",
            "schema:description": "Depth below sea surface at which temperature was recorded",
            "schema:unitText": "meters",
            "schema:unitCode": "MTR",
            "cdi:physicalDataType": "Numeric"
        }
    ],
    "schema:distribution": [
        {
            "@type": ["schema:DataDownload"],
            "schema:name": "Ocean temperature CSV",
            "schema:contentUrl": "https://example.org/downloads/ocean-temp-2025.csv",
            "schema:encodingFormat": ["text/csv"],
            "cdi:characterSet": "UTF-8",
            "cdi:fileSize": 1.2,
            "cdi:fileSizeUofM": "MB"
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
        "@id": "https://w3id.org/cdif/data_description/1.0/"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "sea_water_temperature",
      "schema:description": "Temperature of sea water at measurement depth",
      "schema:unitText": "degrees Celsius",
      "schema:unitCode": "CEL",
      "cdi:physicalDataType": "Numeric"
    },
    {
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measurement_depth",
      "schema:description": "Depth below sea surface at which temperature was recorded",
      "schema:unitText": "meters",
      "schema:unitCode": "MTR",
      "cdi:physicalDataType": "Numeric"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Ocean temperature CSV",
      "schema:contentUrl": "https://example.org/downloads/ocean-temp-2025.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "cdi:characterSet": "UTF-8",
      "cdi:fileSize": 1.2,
      "cdi:fileSizeUofM": "MB"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:dataset_datadesc_001 a schema1:Dataset ;
    schema1:dateModified "2025-09-01" ;
    schema1:distribution [ a schema1:DataDownload ;
            cdi:characterSet "UTF-8" ;
            cdi:fileSize 1.2e+00 ;
            cdi:fileSizeUofM "MB" ;
            schema1:contentUrl "https://example.org/downloads/ocean-temp-2025.csv" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "Ocean temperature CSV" ] ;
    schema1:identifier "https://doi.org/10.1234/ocean-temp-2025" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:name "Ocean Temperature Monitoring Data" ;
    schema1:subjectOf ex:metadata_datadesc_001 ;
    schema1:url "https://example.org/datasets/ocean-temp-2025" ;
    schema1:variableMeasured [ a cdi:InstanceVariable,
                schema1:PropertyValue ;
            cdi:physicalDataType "Numeric" ;
            schema1:description "Depth below sea surface at which temperature was recorded" ;
            schema1:name "measurement_depth" ;
            schema1:unitCode "MTR" ;
            schema1:unitText "meters" ],
        [ a cdi:InstanceVariable,
                schema1:PropertyValue ;
            cdi:physicalDataType "Numeric" ;
            schema1:description "Temperature of sea water at measurement depth" ;
            schema1:name "sea_water_temperature" ;
            schema1:unitCode "CEL" ;
            schema1:unitText "degrees Celsius" ] .

ex:metadata_datadesc_001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/data_description/1.0/> ;
    schema1:about ex:dataset_datadesc_001 ;
    schema1:additionalType "dcat:CatalogRecord" .


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
              const: https://w3id.org/cdif/data_description/1.0/
  '@context':
    type: object
    description: Additional namespace prefix for data description properties.
    properties:
      csvw:
        const: http://www.w3.org/ns/csvw#
  schema:variableMeasured:
    type: array
    items:
      anyOf:
      - type: object
        description: PropertyValue variables at data description level must include
          cdi:physicalDataType and cdi:InstanceVariable typing.
        properties:
          '@type':
            type: array
            items:
              type: string
            contains:
              const: cdi:InstanceVariable
            minItems: 2
        required:
        - cdi:physicalDataType
      - $ref: '#/$defs/StatisticalVariable'
  schema:distribution:
    type: array
    items:
      type: object
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
  StatisticalVariable:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/statisticalVariable/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataDescription/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataDescription/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataDescription/context.jsonld)

## Sources

* [CDIF](https://cdif.codata.org/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifDataDescription`

