
# CDIF Data Cube structure (Schema)

`cdif.bbr.metadata.cdifProperties.cdifDataCube` *v0.1*

metadata to document physical data structure for data cube or hierarchical data. Defines properties: @type, cdif:hasPhysicalMapping. Uses building blocks: cdifPhysicalMapping (cdifProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Data structure description

Describes structured data files-- hierarchical datastructures like JSON, and multidimensional data array structures serialized in data cube format like hdf5 or netCDF. T

## Examples

### Minimal Data Cube
Bare cdi:StructuredDataSet — schema only constrains @type to contain
that const.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
  },
  "@type": ["cdi:StructuredDataSet"]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataCube/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    }
  ],
  "@type": [
    "cdi:StructuredDataSet"
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

[] a cdi:StructuredDataSet .


```


### Complete Data Cube
Multi-dimensional data cube with cdif:hasPhysicalMapping entries that
use cdif:locator HDF5-style paths for each variable.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "ex": "https://example.org/"
    },
    "@type": ["cdi:StructuredDataSet"],
    "cdif:hasPhysicalMapping": [
        {
            "cdif:index": 0,
            "cdif:format": "float64",
            "cdif:physicalDataType": "Numeric",
            "cdif:formats_InstanceVariable": {
                "@id": "ex:var-temperature"
            },
            "cdif:locator": "/temperature[*][*]"
        },
        {
            "cdif:index": 1,
            "cdif:format": "float64",
            "cdif:physicalDataType": "Numeric",
            "cdif:formats_InstanceVariable": {
                "@id": "ex:var-pressure"
            },
            "cdif:locator": "/pressure[*][*]"
        }
    ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataCube/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:StructuredDataSet"
  ],
  "cdif:hasPhysicalMapping": [
    {
      "cdif:index": 0,
      "cdif:format": "float64",
      "cdif:physicalDataType": "Numeric",
      "cdif:formats_InstanceVariable": {
        "@id": "ex:var-temperature"
      },
      "cdif:locator": "/temperature[*][*]"
    },
    {
      "cdif:index": 1,
      "cdif:format": "float64",
      "cdif:physicalDataType": "Numeric",
      "cdif:formats_InstanceVariable": {
        "@id": "ex:var-pressure"
      },
      "cdif:locator": "/pressure[*][*]"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix ns1: <cdif:> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a cdi:StructuredDataSet ;
    ns1:hasPhysicalMapping [ ns1:format "float64" ;
            ns1:formats_InstanceVariable ex:var-temperature ;
            ns1:index 0 ;
            ns1:locator "/temperature[*][*]" ;
            ns1:physicalDataType "Numeric" ],
        [ ns1:format "float64" ;
            ns1:formats_InstanceVariable ex:var-pressure ;
            ns1:index 1 ;
            ns1:locator "/pressure[*][*]" ;
            ns1:physicalDataType "Numeric" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Data Cube Type
description: Multi-dimensional data cube structure using DDI-CDI. Typed as ada:dataCube
  and cdi:StructuredDataSet per CDIF 2026 alignment.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    allOf:
    - contains:
        const: cdi:StructuredDataSet
  cdif:hasPhysicalMapping:
    type: array
    description: Links variables to their physical representation in this dataset.
    items:
      allOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifPhysicalMapping/schema.yaml
      - type: object
        properties:
          cdif:locator:
            type: string
            description: String that can be used by software to locate values of the
              variable in this physical dataset.
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataCube/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataCube/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataCube/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifDataCube`

