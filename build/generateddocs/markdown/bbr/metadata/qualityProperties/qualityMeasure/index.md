
# Simple quality measurement properties (Schema)

`cdif.bbr.metadata.qualityProperties.qualityMeasure` *v0.1*

Schema defining properties for documenting a quality measuremenet associated with a resource. Defines properties: @type, dqv:isMeasurementOf, dqv:value. Uses building blocks: definedTerm (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Person properties

Defines a set of properties for use describing a person for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Example quality measure.
Example quality measure
#### json
```json
{
    "@type": "dqv:QualityMeasurement",
    "dqv:isMeasurementOf": {
        "@type": "schema:DefinedTerm",
        "schema:name": "Positional Accuracy",
        "schema:identifier": "https://standards.iso.org/iso/19157/qualityMeasure/28",
        "schema:inDefinedTermSet": "https://standards.iso.org/iso/19157",
        "schema:termCode": "DQ_AbsoluteExternalPositionalAccuracy"
    },
    "dqv:value": {
        "@type": "schema:DefinedTerm",
        "schema:name": "Pass",
        "schema:identifier": {
            "@type": "schema:PropertyValue",
            "schema:propertyID": "https://standards.iso.org/iso/19157/qualityResult",
            "schema:value": "conformant",
            "schema:url": "http://example.com/resource?foo=bar#fragment"
        },
        "schema:inDefinedTermSet": "https://standards.iso.org/iso/19157/conformanceResult",
        "schema:termCode": "pass"
    }
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/context.jsonld"
  ],
  "@type": "dqv:QualityMeasurement",
  "dqv:isMeasurementOf": {
    "@type": "schema:DefinedTerm",
    "schema:name": "Positional Accuracy",
    "schema:identifier": "https://standards.iso.org/iso/19157/qualityMeasure/28",
    "schema:inDefinedTermSet": "https://standards.iso.org/iso/19157",
    "schema:termCode": "DQ_AbsoluteExternalPositionalAccuracy"
  },
  "dqv:value": {
    "@type": "schema:DefinedTerm",
    "schema:name": "Pass",
    "schema:identifier": {
      "@type": "schema:PropertyValue",
      "schema:propertyID": "https://standards.iso.org/iso/19157/qualityResult",
      "schema:value": "conformant",
      "schema:url": "http://example.com/resource?foo=bar#fragment"
    },
    "schema:inDefinedTermSet": "https://standards.iso.org/iso/19157/conformanceResult",
    "schema:termCode": "pass"
  }
}
```

#### ttl
```ttl
@prefix ns1: <dqv:> .
@prefix schema1: <http://schema.org/> .

[] a ns1:QualityMeasurement ;
    ns1:isMeasurementOf [ a schema1:DefinedTerm ;
            schema1:identifier "https://standards.iso.org/iso/19157/qualityMeasure/28" ;
            schema1:inDefinedTermSet "https://standards.iso.org/iso/19157" ;
            schema1:name "Positional Accuracy" ;
            schema1:termCode "DQ_AbsoluteExternalPositionalAccuracy" ] ;
    ns1:value [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://standards.iso.org/iso/19157/qualityResult" ;
                    schema1:url "http://example.com/resource?foo=bar#fragment" ;
                    schema1:value "conformant" ] ;
            schema1:inDefinedTermSet "https://standards.iso.org/iso/19157/conformanceResult" ;
            schema1:name "Pass" ;
            schema1:termCode "pass" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: definitions for simple quality measure property
type: object
properties:
  '@type':
    anyOf:
    - type: string
      const: dqv:QualityMeasurement
    - type: array
      items:
        type: string
      contains:
        const: dqv:QualityMeasurement
  dqv:isMeasurementOf:
    description: specify the quality measure that is reported, by name, with an ID
      ref, or as a Defined Term
    anyOf:
    - type: string
    - type: object
      properties:
        '@id':
          type: string
          description: a resolvable reference to a representation of a quality measure
    - $ref: '#/$defs/DefinedTerm'
  dqv:value:
    description: the reported result of the quality measure, either as a string or
      a defined term from a vocabulary
    anyOf:
    - type: string
    - $ref: '#/$defs/DefinedTerm'
required:
- dqv:isMeasurementOf
- dqv:value
$defs:
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/context.jsonld)

## Sources

* 

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/qualityProperties/qualityMeasure`

