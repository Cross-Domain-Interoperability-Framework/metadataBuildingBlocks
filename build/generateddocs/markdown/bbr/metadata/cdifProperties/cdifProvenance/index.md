
# CDIF Provenance (Schema)

`cdif.bbr.metadata.cdifProperties.cdifProvenance` *v0.1*

Defines the prov:wasGeneratedBy property for CDIF metadata records. Wraps the cdifProvActivity building block as an array of provenance activities describing how the resource was generated.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Provenance

Defines the `prov:wasGeneratedBy` property for CDIF metadata records. This building block wraps the cdifProvActivity building block as an array of provenance activities.

### Defined properties

- **prov:wasGeneratedBy** - array of provenance activities describing how the described resource was generated

### Dependencies

- [cdifProvActivity](../cdifProvActivity/) - extended provenance activity with schema.org Action properties

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Provenance
description: Building block that defines the prov:wasGeneratedBy property for CDIF
  metadata records. Wraps the cdifProvActivity building block as an array of provenance
  activities that describe how the described resource was generated.
type: object
properties:
  prov:wasGeneratedBy:
    description: Provenance activities describing how the resource was generated,
      including agents, instruments, methodology, temporal bounds, and action chaining.
    type: array
    items:
      $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvActivity/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvenance/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvenance/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvenance/context.jsonld)

## Sources

* [W3C PROV-O](https://www.w3.org/TR/prov-o/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifProvenance`

