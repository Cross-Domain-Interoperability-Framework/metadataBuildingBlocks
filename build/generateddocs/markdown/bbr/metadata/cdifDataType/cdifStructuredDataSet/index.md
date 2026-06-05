
# CDIF StructuredDataSet building block (Schema)

`cdif.bbr.metadata.cdifDataType.cdifStructuredDataSet` *v0.1*

Dataset-level marker for a structured (hierarchical) dataset such as XML or JSON. A subclass of cdi:PhysicalDataSet carried on a schema:DataDownload distribution dual-typed cdi:StructuredDataSet. DDI-CDI StructuredDataSet; fields are located with cdifLocatorMapping (not column-index/text mappings). Defines cdif:encoding (cdif: because the DDI-CDI ControlledVocabularyEntry type is simplified to a plain charset string).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF StructuredDataSet

Dataset-level marker for a **structured** (hierarchical) dataset such as XML or JSON. A
subclass of DDI-CDI `PhysicalDataSet`; in CDIF it is carried on a `schema:DataDownload`
distribution dual-typed `cdi:StructuredDataSet`.

This building block is an **attribute mixin** (no `@type` of its own). It has no
tabular-layout attributes; instead, each measured variable is located in the document
with a [`cdifLocatorMapping`](../cdifLocatorMapping/) value of `cdif:hasPhysicalMapping`
(an `XPath`/`JSONPath`-style locator), rather than a column index or text mapping.

`cdif:encoding` records the serialization (e.g., `application/json`, `application/xml`) — `cdif:`
because the DDI-CDI `ControlledVocabularyEntry` type is simplified here to a plain charset string.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Structured DataSet
description: Dataset-level marker for a structured (hierarchical) dataset such as
  XML or JSON. A subclass of cdi:PhysicalDataSet, carried on a schema:DataDownload
  distribution dual-typed cdi:StructuredDataSet. DDI-CDI StructuredDataSet. It has
  no distinct tabular-layout attributes; fields are located with cdifLocatorMapping
  values of cdif:hasPhysicalMapping (rather than column-index/text mappings). This
  is an attribute mixin (no @type of its own; the token is carried by the distribution).
type: object
properties:
  cdif:encoding:
    type: string
    description: Character encoding / serialization of the structured document (e.g.,
      utf-8, application/json). CDIF simplification (plain charset string) of DDI-CDI
      PhysicalDataSet.encoding, whose model type is ControlledVocabularyEntry. The
      cdi/cdif namespace policy does not allow a ControlledVocabularyEntry as a plain
      string in the cdi namespace, so this property is in the cdif namespace.
    x-jsonld-id: https://w3id.org/cdif/encoding
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  cdif: https://w3id.org/cdif/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifStructuredDataSet/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifStructuredDataSet/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifStructuredDataSet/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifStructuredDataSet`

