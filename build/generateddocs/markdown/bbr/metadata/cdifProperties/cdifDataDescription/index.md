
# CDIF Data Description (Schema)

`cdif.bbr.metadata.cdifProperties.cdifDataDescription` *v0.1*

Additional constraints for CDIF data description level. Adds cdi:physicalDataType requirement on variableMeasured items and distribution-level cdi properties for file characterization (characterSet, fileSize, fileSizeUofM). Used by CDIFDataDescription and CDIFcomplete profiles.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Additional constraints for CDIF data description level metadata. Adds the `cdi:physicalDataType` requirement on variableMeasured items (PropertyValue-type variables must specify their physical data type at this level). Also adds distribution-level CDI properties for file characterization: `cdi:characterSet`, `cdi:fileSize`, and `cdi:fileSizeUofM`.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Data Description properties
description: Additional constraints for CDIF data description level. Adds cdi:physicalDataType
  requirement on variableMeasured items and distribution-level cdi properties for
  file characterization (characterSet, fileSize, fileSizeUofM).
type: object
properties:
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

