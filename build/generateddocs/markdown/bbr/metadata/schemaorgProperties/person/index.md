
# Person (Schema)

`cdif.bbr.metadata.schemaorgProperties.person` *v0.1*

Schema defining propertis of a person, a profile of schema.org/Person. Defines properties: @id, @type, schema:name, schema:description, schema:identifier, schema:alternateName, schema:affiliation, schema:contactPoint, schema:sameAs. Uses building blocks: identifier (schemaorgProperties), organization (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Person properties

Defines a set of properties for use describing a person for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Example person.
Example person instance.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "ex:PersonExample_zZc",
  "@type": [
    "schema:Person"
  ],
  "schema:name": "Joe Test",
  "schema:alternateName": "Test, Joe",
  "schema:affiliation": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Test organization"
  },
  "schema:description": "Metadata specialist, based in Portland, Maine",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://orcid.org",
    "schema:value": "0000-0001-2345-6789",
    "schema:url": "https://orcid.org/0000-0001-2345-6789"
  },
  "schema:contactPoint": {
    "@type": [
      "schema:ContactPoint"
    ],
    "schema:email": "joe@bmanuco.org"
  },
  "schema:sameAs": [
    "https://ark.org/46737",
    "uri:test:43737"
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@id": "ex:PersonExample_zZc",
  "@type": [
    "schema:Person"
  ],
  "schema:name": "Joe Test",
  "schema:alternateName": "Test, Joe",
  "schema:affiliation": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Test organization"
  },
  "schema:description": "Metadata specialist, based in Portland, Maine",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://orcid.org",
    "schema:value": "0000-0001-2345-6789",
    "schema:url": "https://orcid.org/0000-0001-2345-6789"
  },
  "schema:contactPoint": {
    "@type": [
      "schema:ContactPoint"
    ],
    "schema:email": "joe@bmanuco.org"
  },
  "schema:sameAs": [
    "https://ark.org/46737",
    "uri:test:43737"
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:PersonExample_zZc a schema1:Person ;
    schema1:affiliation [ a schema1:Organization ;
            schema1:name "Test organization" ] ;
    schema1:alternateName "Test, Joe" ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "joe@bmanuco.org" ] ;
    schema1:description "Metadata specialist, based in Portland, Maine" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://orcid.org" ;
            schema1:url "https://orcid.org/0000-0001-2345-6789" ;
            schema1:value "0000-0001-2345-6789" ] ;
    schema1:name "Joe Test" ;
    schema1:sameAs "https://ark.org/46737",
        "uri:test:43737" .


```


### Complete person example.
Person instance exercising all properties: name, description, alternateName,
identifier (ORCID), affiliation, contactPoint, and sameAs (string and object).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/"
  },
  "@id": "ex:PersonComplete_001",
  "@type": ["schema:Person"],
  "schema:name": "Jane A. Researcher",
  "schema:description": "Marine geochemist specializing in isotope analysis, based at Woods Hole Oceanographic Institution",
  "schema:alternateName": "Researcher, J.A.",
  "schema:identifier": {
    "@type": ["schema:PropertyValue"],
    "schema:propertyID": "https://orcid.org",
    "schema:value": "0000-0002-1825-0097",
    "schema:url": "https://orcid.org/0000-0002-1825-0097"
  },
  "schema:affiliation": {
    "@type": ["schema:Organization"],
    "schema:name": "Woods Hole Oceanographic Institution",
    "schema:identifier": {
      "@type": ["schema:PropertyValue"],
      "schema:propertyID": "https://ror.org",
      "schema:value": "03zbnzt98",
      "schema:url": "https://ror.org/03zbnzt98"
    }
  },
  "schema:contactPoint": {
    "@type": ["schema:ContactPoint"],
    "schema:email": "jresearcher@whoi.edu"
  },
  "schema:sameAs": [
    "https://scholar.google.com/citations?user=abc123",
    {"@id": "https://www.wikidata.org/entity/Q12345678"}
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:PersonComplete_001",
  "@type": [
    "schema:Person"
  ],
  "schema:name": "Jane A. Researcher",
  "schema:description": "Marine geochemist specializing in isotope analysis, based at Woods Hole Oceanographic Institution",
  "schema:alternateName": "Researcher, J.A.",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://orcid.org",
    "schema:value": "0000-0002-1825-0097",
    "schema:url": "https://orcid.org/0000-0002-1825-0097"
  },
  "schema:affiliation": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Woods Hole Oceanographic Institution",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://ror.org",
      "schema:value": "03zbnzt98",
      "schema:url": "https://ror.org/03zbnzt98"
    }
  },
  "schema:contactPoint": {
    "@type": [
      "schema:ContactPoint"
    ],
    "schema:email": "jresearcher@whoi.edu"
  },
  "schema:sameAs": [
    "https://scholar.google.com/citations?user=abc123",
    {
      "@id": "https://www.wikidata.org/entity/Q12345678"
    }
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:PersonComplete_001 a schema1:Person ;
    schema1:affiliation [ a schema1:Organization ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://ror.org" ;
                    schema1:url "https://ror.org/03zbnzt98" ;
                    schema1:value "03zbnzt98" ] ;
            schema1:name "Woods Hole Oceanographic Institution" ] ;
    schema1:alternateName "Researcher, J.A." ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "jresearcher@whoi.edu" ] ;
    schema1:description "Marine geochemist specializing in isotope analysis, based at Woods Hole Oceanographic Institution" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://orcid.org" ;
            schema1:url "https://orcid.org/0000-0002-1825-0097" ;
            schema1:value "0000-0002-1825-0097" ] ;
    schema1:name "Jane A. Researcher" ;
    schema1:sameAs <https://www.wikidata.org/entity/Q12345678>,
        "https://scholar.google.com/citations?user=abc123" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: schema for cdif profile of schema.org/Person
type: object
properties:
  '@id':
    type: string
  '@type':
    type: array
    items:
      type: string
    contains:
      const: schema:Person
    minItems: 1
  schema:name:
    type: string
    description: string label for person that is meaningful for human users
  schema:description:
    type: string
  schema:identifier:
    description: identifier for person, recommend ORCID
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
    - type: string
  schema:alternateName:
    type: string
    description: other labels by which the person might be known
  schema:affiliation:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
    description: if affiliation is present, value must be a schema:Organization.
  schema:contactPoint:
    type: object
    properties:
      '@type':
        default: schema:ContactPoint
        type: array
        items:
          type: string
        contains:
          const: schema:ContactPoint
        minItems: 1
      schema:email:
        type: string
    description: restrict to email only. Schema.org allows telephone and postal contacts
      as well
  schema:sameAs:
    type: array
    description: other identifiers for the person
    items:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
allOf:
- required:
  - '@type'
- anyOf:
  - required:
    - schema:name
  - required:
    - schema:identifier
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/context.jsonld)

## Sources

* [schema.org](https://schema.org/Person)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/person`

