
# MonetaryGrant (Schema)

`cdif.bbr.metadata.schemaorgProperties.monetaryGrant` *v0.1*

properties for acknowledging funding, CDIF profile of schema.org/MonetaryGrant. Defines properties: @type, schema:identifier, schema:description, schema:name, schema:funder. Uses building blocks: person (schemaorgProperties), organization (schemaorgProperties), identifier (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## MonetaryGrant properties

Defines a set of properties for use funding that supported development or maintenance of a resource, for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.  Based on schema.org/MonetaryGrant
## Examples

### Example MonetaryGrant.
Example MonetaryGrant instance.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@type": [
    "schema:MonetaryGrant"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "NSF award number",
    "schema:value": "2227407",
    "schema:url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2227407"
  },
  "schema:name": "Big Bucks for Research",
  "schema:funder": {
    "@id": "https://ror.org/021nxhr62"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/monetaryGrant/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@type": [
    "schema:MonetaryGrant"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "NSF award number",
    "schema:value": "2227407",
    "schema:url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2227407"
  },
  "schema:name": "Big Bucks for Research",
  "schema:funder": {
    "@id": "https://ror.org/021nxhr62"
  }
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:MonetaryGrant ;
    schema1:funder <https://ror.org/021nxhr62> ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "NSF award number" ;
            schema1:url "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2227407" ;
            schema1:value "2227407" ] ;
    schema1:name "Big Bucks for Research" .


```


### Complete MonetaryGrant example.
MonetaryGrant instance exercising all properties: name, description, identifier (NSF
award), and funder (inline Organization with additionalType, ROR identifier).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/"
  },
  "@id": "ex:FunderComplete_001",
  "@type": ["schema:MonetaryGrant"],
  "schema:name": "Collaborative Research: Ocean Carbon Cycling and Geochemical Tracers",
  "schema:description": "Three-year collaborative research grant supporting field campaigns and laboratory analysis of ocean carbon cycling using novel geochemical tracers",
  "schema:identifier": {
    "@type": ["schema:PropertyValue"],
    "schema:propertyID": "NSF award number",
    "schema:value": "2345678",
    "schema:url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2345678"
  },
  "schema:funder": {
    "@id": "https://ror.org/021nxhr62",
    "@type": ["schema:Organization"],
    "schema:additionalType": ["schema:FundingAgency"],
    "schema:name": "National Science Foundation",
    "schema:alternateName": "NSF",
    "schema:identifier": {
      "@type": ["schema:PropertyValue"],
      "schema:propertyID": "https://registry.identifiers.org/registry/ror",
      "schema:value": "021nxhr62",
      "schema:url": "https://ror.org/021nxhr62"
    }
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/monetaryGrant/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:FunderComplete_001",
  "@type": [
    "schema:MonetaryGrant"
  ],
  "schema:name": "Collaborative Research: Ocean Carbon Cycling and Geochemical Tracers",
  "schema:description": "Three-year collaborative research grant supporting field campaigns and laboratory analysis of ocean carbon cycling using novel geochemical tracers",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "NSF award number",
    "schema:value": "2345678",
    "schema:url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2345678"
  },
  "schema:funder": {
    "@id": "https://ror.org/021nxhr62",
    "@type": [
      "schema:Organization"
    ],
    "schema:additionalType": [
      "schema:FundingAgency"
    ],
    "schema:name": "National Science Foundation",
    "schema:alternateName": "NSF",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://registry.identifiers.org/registry/ror",
      "schema:value": "021nxhr62",
      "schema:url": "https://ror.org/021nxhr62"
    }
  }
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:FunderComplete_001 a schema1:MonetaryGrant ;
    schema1:description "Three-year collaborative research grant supporting field campaigns and laboratory analysis of ocean carbon cycling using novel geochemical tracers" ;
    schema1:funder <https://ror.org/021nxhr62> ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "NSF award number" ;
            schema1:url "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2345678" ;
            schema1:value "2345678" ] ;
    schema1:name "Collaborative Research: Ocean Carbon Cycling and Geochemical Tracers" .

<https://ror.org/021nxhr62> a schema1:Organization ;
    schema1:additionalType "schema:FundingAgency" ;
    schema1:alternateName "NSF" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/ror" ;
            schema1:url "https://ror.org/021nxhr62" ;
            schema1:value "021nxhr62" ] ;
    schema1:name "National Science Foundation" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Funding acknowledgement properties, profile of schema.org/MonetaryGrant
type: object
properties:
  '@id':
    type: string
    description: URI identifier for this funding record
  '@type':
    default: schema:MonetaryGrant
    type: array
    items:
      type: string
    contains:
      const: schema:MonetaryGrant
    minItems: 1
  schema:identifier:
    $ref: '#/$defs/Identifier'
    description: identifier for a particular grant
  schema:description:
    type: string
    description: description of the funding or grant
  schema:name:
    type: string
    description: title of the grant
  schema:funder:
    anyOf:
    - type: object
      properties:
        '@id':
          type: string
          description: a identifier for an agent defined in this metadata, or externally;
            must be dereferenceable
      required:
      - '@id'
    - $ref: '#/$defs/Person'
    - $ref: '#/$defs/Organization'
anyOf:
- required:
  - schema:funder
- required:
  - schema:identifier
- required:
  - schema:name
$defs:
  Person:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
  Organization:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
  Identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/monetaryGrant/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/monetaryGrant/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/monetaryGrant/context.jsonld)

## Sources

* [schema.org](https://schema.org/funding)
* [schema.org](https://schema.org/MonetaryGrant)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/monetaryGrant`

