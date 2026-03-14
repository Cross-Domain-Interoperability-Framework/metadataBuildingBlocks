
# schema additionalProperty properties (Schema)

`cdif.bbr.metadata.schemaorgProperties.additionalProperty` *v0.1*

Schema for a schema:PropertyValue used to specify a property of an element that is not defined in the JSON schema. Defines properties: @type, schema:propertyID, schema:name, schema:value. Uses building blocks: definedTerm (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Additional Property (PropertyValue) properties

PropertyValue pattern for soft-typed properties with name/value pairs. Used as values for schema:additionalProperty in extension profiles. Not used in CDIF Mandatory or CDIF Optional.

### Defined properties

- **@type** — must be schema:PropertyValue
- **schema:propertyID** — identifier or name for the property concept (string, URI reference, or DefinedTerm)
- **schema:name** — name of the property
- **schema:value** — value of the property

### Dependencies

- [definedTerm](../definedTerm/) — controlled vocabulary term for property identification

## Examples

### Example additional property.
Example of soft-typed additional property implementation, based on schema.org PropertyValue
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "nxs": "http://purl.org/nexusformat/definitions/"
    },
    "@id": "ex:exampleAdditionalProperty_lkj09",
    "@type": "schema:PropertyValue",
    "schema:propertyID": [
        "nxs:Field/NXsource/probe",
        {
            "@id": "ex:addPropdefinedTerm_zZc",
            "@type": "schema:DefinedTerm",
            "schema:name":"probe",
            "schema:identifier": {
                "@id": "ex:addPropIDPropertyValue_53yh",
                "@type": "schema:PropertyValue",
                "schema:propertyID": "https://purl.org/nexusformat/definitions/Field/NXsource/probe",
                "schema:url": "https://purl.org/nexusformat/definitions/Field/NXsource/probe"
            },
            "schema:inDefinedTermSet": "http://ogc.org/defs"
        }
    ],
    "schema:name": "example additional property",
    "schema:value": "x-ray"
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "nxs": "http://purl.org/nexusformat/definitions/"
    }
  ],
  "@id": "ex:exampleAdditionalProperty_lkj09",
  "@type": "schema:PropertyValue",
  "schema:propertyID": [
    "nxs:Field/NXsource/probe",
    {
      "@id": "ex:addPropdefinedTerm_zZc",
      "@type": "schema:DefinedTerm",
      "schema:name": "probe",
      "schema:identifier": {
        "@id": "ex:addPropIDPropertyValue_53yh",
        "@type": "schema:PropertyValue",
        "schema:propertyID": "https://purl.org/nexusformat/definitions/Field/NXsource/probe",
        "schema:url": "https://purl.org/nexusformat/definitions/Field/NXsource/probe"
      },
      "schema:inDefinedTermSet": "http://ogc.org/defs"
    }
  ],
  "schema:name": "example additional property",
  "schema:value": "x-ray"
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:exampleAdditionalProperty_lkj09 a schema1:PropertyValue ;
    schema1:name "example additional property" ;
    schema1:propertyID ex:addPropdefinedTerm_zZc,
        "nxs:Field/NXsource/probe" ;
    schema1:value "x-ray" .

ex:addPropIDPropertyValue_53yh a schema1:PropertyValue ;
    schema1:propertyID "https://purl.org/nexusformat/definitions/Field/NXsource/probe" ;
    schema1:url "https://purl.org/nexusformat/definitions/Field/NXsource/probe" .

ex:addPropdefinedTerm_zZc a schema1:DefinedTerm ;
    schema1:identifier ex:addPropIDPropertyValue_53yh ;
    schema1:inDefinedTermSet "http://ogc.org/defs" ;
    schema1:name "probe" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: additionalProperty PropertyValue
description: 'PropertyValue values required to define a soft-typed property with a
  value. '
properties:
  '@type':
    anyOf:
    - type: string
      const: schema:PropertyValue
    - type: array
      items:
        type: string
      contains:
        const: schema:PropertyValue
  schema:propertyID:
    type: array
    items:
      $ref: '#/$defs/propertyID_item'
    minItems: 1
    description: identifier or name for the property concept quantified by the values
      in this variable slot. Multiple values can specify the property at different
      levels of granularity.
  schema:name:
    type: string
  schema:value:
    anyOf:
    - type: string
    - type: number
    - type: boolean
    - type: object
  schema:unitCode:
    anyOf:
    - type: string
    - $ref: '#/$defs/DefinedTerm'
  schema:unitText:
    type: string
required:
- schema:name
- schema:value
$defs:
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  propertyID_item:
    anyOf:
    - type: string
    - type: object
      properties:
        '@id':
          type: string
    - $ref: '#/$defs/DefinedTerm'
x-jsonld-prefixes:
  schema: http://schema.org/
  nxs: http://purl.org/nexusformat/definitions/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/context.jsonld)

## Sources

* [schema.org](https://schema.org/additionalProperty)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/additionalProperty`

