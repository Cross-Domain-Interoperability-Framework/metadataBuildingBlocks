
# CDIF Archive Distribution (Schema)

`cdif.bbr.metadata.cdifProperties.cdifArchiveDistribution` *v0.1*

Adds archive distribution (cdifArchive) as a valid schema:distribution item type. cdifOptional already provides DataDownload and WebAPI; this building block extends distribution with the cdifArchive option for archive files containing component files described via schema:hasPart.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Archive Distribution

Adds archive distribution as a valid `schema:distribution` item type. The `cdifOptional` building block already defines `schema:distribution` with DataDownload and WebAPI options; this building block extends that with the [cdifArchive](../cdifArchive/) option.

### Dependencies

- [cdifArchive](../cdifArchive/) - archive item schema (DataDownload with hasPart component files)

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Archive Distribution
description: Building block that adds archive distribution as a valid distribution
  item type. cdifOptional already defines schema:distribution with DataDownload and
  WebAPI options; this building block extends that with the cdifArchive option (DataDownload
  with schema:hasPart component files).
type: object
properties:
  schema:distribution:
    type: array
    items:
      anyOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchive/schema.yaml
      - {}

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/context.jsonld)

## Sources

* [schema.org DataDownload](https://schema.org/DataDownload)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifArchiveDistribution`

