
# CDIF Data Cube structure (Schema)

`cdif.bbr.metadata.cdifProperties.cdifDataCube` *v0.1*

metadata to document physical data structure for data cube or hierarchical data. Defines properties: @type, cdi:hasPhysicalMapping. Uses building blocks: cdifPhysicalMapping (cdifProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Data structure description

Describes structured data files-- hierarchical datastructures like JSON, and multidimensional data array structures serialized in data cube format like hdf5 or netCDF. T

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
  cdi:hasPhysicalMapping:
    type: array
    description: Links variables to their physical representation in this dataset.
    items:
      allOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifPhysicalMapping/schema.yaml
      - type: object
        properties:
          cdi:locator:
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

