
# CDIF TextMapping building block (Schema)

`cdif.bbr.metadata.cdifDataType.cdifTextMapping` *v0.1*

Physical mapping for a variable in a delimited or fixed-width text dataset. Extends cdifPhysicalMapping with cdi:length, cdi:defaultDecimalSeparator, cdi:defaultDigitGroupSeparator, and cdif:displayLabel (cdif: because LabelForDisplay is simplified to a plain string). DDI-CDI TextMapping (a specialization of PhysicalMapping).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF TextMapping

Physical mapping for a variable in a delimited or fixed-width **text** dataset. Extends
[`cdifPhysicalMapping`](../cdifPhysicalMapping/) (via `allOf`) with the text-format
properties from DDI-CDI `TextMapping`:

- `cdi:length` — column width for fixed-width text
- `cdi:defaultDecimalSeparator`
- `cdi:defaultDigitGroupSeparator`
- `cdif:displayLabel` (cdif: — LabelForDisplay simplified to a plain string)

Used as the item type for `cdif:hasPhysicalMapping` on a distribution typed
`cdi:TabularTextDataSet`. The base `cdifPhysicalMapping` carries the
serialization-agnostic properties (index, format, physical data type, scale, lengths,
null sequence, default value, number pattern); structured-document location is in
`cdifLocatorMapping`.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Text Mapping Type
description: Physical mapping for a variable in a delimited or fixed-width text dataset.
  Extends cdifPhysicalMapping with text-format properties (column width and number
  formatting). DDI-CDI TextMapping.
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifPhysicalMapping/schema.yaml
- type: object
  properties:
    '@type':
      type: array
      items:
        type: string
      contains:
        const: cdif:TextMapping
      minItems: 1
      description: A cdifTextMapping instance must be typed cdif:TextMapping (not
        the base cdif:PhysicalMapping). It composes cdifPhysicalMapping via allOf
        for its properties; the base @type accepts the physical-mapping family.
    cdi:length:
      type: integer
      description: The column width if the tabular text is fixed width (TextMapping.length).
      x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/length
    cdi:defaultDecimalSeparator:
      type: string
      description: Decimal separator used when not otherwise specified (TextMapping.defaultDecimalSeparator).
      x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/defaultDecimalSeparator
    cdi:defaultDigitGroupSeparator:
      type: string
      description: Digit-group (thousands) separator (TextMapping.defaultDigitGroupSeparator).
      x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/defaultDigitGroupSeparator
    cdif:displayLabel:
      type: array
      items:
        type: string
      description: Human-readable label(s) for display. CDIF simplification (plain
        string) of DDI-CDI TextMapping.displayLabel, whose model type is LabelForDisplay.
        Per the cdi/cdif namespace policy a structured-string type simplified to a
        plain string is in the cdif namespace.
      x-jsonld-id: https://w3id.org/cdif/displayLabel
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  cdif: https://w3id.org/cdif/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifTextMapping/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifTextMapping/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdif": "https://w3id.org/cdif/",
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifTextMapping/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifTextMapping`

