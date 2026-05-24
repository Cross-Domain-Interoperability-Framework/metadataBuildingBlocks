
# CDIF LocatorMapping building block (Schema)

`cdif.bbr.metadata.cdifProperties.cdifLocatorMapping` *v0.1*

Locates a variable's value(s) within a structured (hierarchical) dataset such as XML or JSON using a locator expression (XPath, JSONPath). Defines cdi:locator and cdif:formats_InstanceVariable. DDI-CDI LocatorMapping; used instead of column-index/text mappings for cdi:StructuredDataSet distributions.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF LocatorMapping

Locates a variable's value(s) within a **structured** (hierarchical) dataset such as
XML or JSON, via a locator expression (XPath, JSONPath, JSON Pointer, etc.). DDI-CDI
`LocatorMapping`.

- `cdi:locator` (required) — the locator expression
- `cdif:formats_InstanceVariable` — reference to the `schema:variableMeasured` variable this locates

Used as the item type for `cdif:hasPhysicalMapping` on a distribution typed
`cdi:StructuredDataSet`, where a column index / text mapping does not apply.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Locator Mapping Type
description: Locates a variable's value(s) within a structured (hierarchical) dataset
  such as XML or JSON, via a locator expression (e.g., XPath or JSONPath). DDI-CDI
  LocatorMapping. Used in place of column-index/text mappings for cdi:StructuredDataSet
  distributions.
type: object
properties:
  cdi:locator:
    type: string
    description: Expression locating the variable's value(s) in the structured document
      (XPath, JSONPath, pointer, etc.). LocatorMapping.locator.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/locator
  cdif:formats_InstanceVariable:
    type: object
    description: Reference to a variable defined in schema:variableMeasured.
    properties:
      '@id':
        type: string
        description: This should be a reference to a variable defined in the schema:variableMeasured
          section.
    x-jsonld-id: https://cdif.org/0.1/formats_InstanceVariable
required:
- cdi:locator
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  cdif: https://cdif.org/0.1/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifLocatorMapping/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifLocatorMapping/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifLocatorMapping/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifLocatorMapping`

