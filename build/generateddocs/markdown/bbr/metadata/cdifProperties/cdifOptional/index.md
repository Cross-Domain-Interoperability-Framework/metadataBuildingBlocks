
# CDIF discovery metadata, Optional elements (Schema)

`cdif.bbr.metadata.cdifProperties.cdifOptional` *v0.1*

Definition of optional metadata elements for CDIF discovery profile. Defines properties: schema:description, schema:additionalType, schema:sameAs, schema:version, schema:inLanguage, schema:datePublished, schema:relatedLink, schema:publishingPrinciples, schema:keywords, schema:creator, schema:contributor, schema:publisher, schema:provider, schema:funding, schema:variableMeasured, schema:spatialCoverage, schema:temporalCoverage, prov:wasGeneratedBy, prov:wasDerivedFrom, dqv:hasQualityMeasurement, schema:distribution. At this level prov:wasGeneratedBy uses the simple generatedBy pattern (string or @id references only); the extended cdifProvActivity pattern (instruments, agents, temporal bounds) is introduced at the CDIFcomplete profile level or by domain-specific building blocks. Uses building blocks: labeledLink (schemaorgProperties), identifier (schemaorgProperties), definedTerm (schemaorgProperties), person (schemaorgProperties), organization (schemaorgProperties), agentInRole (schemaorgProperties), funder (schemaorgProperties), variableMeasured (schemaorgProperties), spatialExtent (schemaorgProperties), temporalExtent (schemaorgProperties), generatedBy (provProperties), derivedFrom (provProperties), qualityMeasure (qualityProperties), dataDownload (schemaorgProperties), webAPI (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Base Metadata properties

Defines simple properties included in CDIF discovery metadata for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.

### Provenance

At this level, `prov:wasGeneratedBy` uses the simple `generatedBy` pattern from provProperties — activity items accept only string names or `@id` references to instruments/software. The extended `cdifProvActivity` pattern (with structured instruments, agents, temporal bounds, methodology, and action chaining) is introduced at the CDIFcomplete profile level or by domain-specific building blocks (e.g., ddeImagery, xasRequired).
## Examples

### Example CDIF record
Example CDIF record with mandatory and optional properties.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@id": "ex:cdifOptional_23578",
    "@type": ["schema:Dataset"],
    "schema:name": "Bathymetry Bay of Biscay",
    "schema:identifier":"https://doi.org/23566/aslry",
    "schema:additionalType": [""],
    "schema:description": "description of resource",
    "schema:version": "1.0",
    "schema:url": "https://example.org/landingPage254266",
    "schema:inLanguage": "en",
    "schema:dateModified": "2022-12-12",
    "schema:datePublished": "2021-11-14",
    "schema:license": ["https://creativecommons.org/publicdomain/zero/1.0/"],
    "schema:conditionsOfAccess": [
        {
            "@id": "ex:LabeledLinkExample_qZc",
            "@type": "schema:CreativeWork",
            "schema:name": "conditions of access statement",
            "schema:description": "URL to get the document",
            "schema:url": "https://example.org/conditions/2342747"
        }
    ],
    "schema:relatedLink": [
        {
            "@type": "schema:LinkRole",
            "schema:linkRelationship": "related data",
            "target": {
                "@type": "schema:EntryPoint",
                "schema:encodingFormat": "image/jpg",
                "schema:name": "Image of seafloor geology map, bay of Biscay",
                "schema:url": "https://example.org/geology/baybiscay"
            }
        },
        {
            "@type": "schema:LinkRole",
            "schema:linkRelationship": {
                "@type": "schema:DefinedTerm",
                "schema:name": "related dataset",
                "schema:inDefinedTermSet": "https://www.iana.org/assignments/link-relations/",
                "schema:termCode": "related"
            },
            "target": {
                "@type": "schema:EntryPoint",
                "schema:name": "Bay of Biscay current velocity dataset",
                "schema:url": "https://example.org/currents/baybiscay"
            }
        }
    ],
    "schema:publishingPrinciples": ["https://example.org/principles/3478"],
    "schema:creator": {
        "@list": [
            {
                "@type": "schema:Person",
                "schema:name": "Example, Author",
                "schema:identifier": "https://orcid.org/0000-0001-2345-6789",
                "schema:contactPoint": {
                    "@type": "schema:ContactPoint",
                    "schema:email": "author@example.org"
                }
            }
        ]
    },
    "schema:contributor": [
        {
            "@type": "schema:Role",
            "schema:roleName": "editor",
            "schema:contributor": {
                "@id": "ex:PersonExample_zZc",
                "@type": "schema:Person",
                "schema:name": "Joe B. Test",
                "schema:identifier": {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": "https://orcid.org",
                    "schema:value": "0000-0002-9876-5432",
                    "schema:url": "https://orcid.org/0000-0002-9876-5432"
                },
                "schema:contactPoint": {
                    "@type": "schema:ContactPoint",
                    "schema:email": "joe@example.org"
                }
            }
        }
    ],
    "schema:keywords": [
        "bathymetry",
        "ocean floor"
    ],
    "schema:subjectOf": {
        "dcterms:conformsTo": [
            {
                "@id": "https://w3id.org/cdif/discovery/1.0/"
            }
        ]
    }
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "https//schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifOptional/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@id": "ex:cdifOptional_23578",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Bathymetry Bay of Biscay",
  "schema:identifier": "https://doi.org/23566/aslry",
  "schema:additionalType": [
    ""
  ],
  "schema:description": "description of resource",
  "schema:version": "1.0",
  "schema:url": "https://example.org/landingPage254266",
  "schema:inLanguage": "en",
  "schema:dateModified": "2022-12-12",
  "schema:datePublished": "2021-11-14",
  "schema:license": [
    "https://creativecommons.org/publicdomain/zero/1.0/"
  ],
  "schema:conditionsOfAccess": [
    {
      "@id": "ex:LabeledLinkExample_qZc",
      "@type": "schema:CreativeWork",
      "schema:name": "conditions of access statement",
      "schema:description": "URL to get the document",
      "schema:url": "https://example.org/conditions/2342747"
    }
  ],
  "schema:relatedLink": [
    {
      "@type": "schema:LinkRole",
      "schema:linkRelationship": "related data",
      "target": {
        "@type": "schema:EntryPoint",
        "schema:encodingFormat": "image/jpg",
        "schema:name": "Image of seafloor geology map, bay of Biscay",
        "schema:url": "https://example.org/geology/baybiscay"
      }
    },
    {
      "@type": "schema:LinkRole",
      "schema:linkRelationship": {
        "@type": "schema:DefinedTerm",
        "schema:name": "related dataset",
        "schema:inDefinedTermSet": "https://www.iana.org/assignments/link-relations/",
        "schema:termCode": "related"
      },
      "target": {
        "@type": "schema:EntryPoint",
        "schema:name": "Bay of Biscay current velocity dataset",
        "schema:url": "https://example.org/currents/baybiscay"
      }
    }
  ],
  "schema:publishingPrinciples": [
    "https://example.org/principles/3478"
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Person",
        "schema:name": "Example, Author",
        "schema:identifier": "https://orcid.org/0000-0001-2345-6789",
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "author@example.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": "schema:Role",
      "schema:roleName": "editor",
      "schema:contributor": {
        "@id": "ex:PersonExample_zZc",
        "@type": "schema:Person",
        "schema:name": "Joe B. Test",
        "schema:identifier": {
          "@type": "schema:PropertyValue",
          "schema:propertyID": "https://orcid.org",
          "schema:value": "0000-0002-9876-5432",
          "schema:url": "https://orcid.org/0000-0002-9876-5432"
        },
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "joe@example.org"
        }
      }
    }
  ],
  "schema:keywords": [
    "bathymetry",
    "ocean floor"
  ],
  "schema:subjectOf": {
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix ns1: <dcterms:> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .

ex:cdifOptional_23578 a schema1:Dataset ;
    schema1:additionalType "" ;
    schema1:conditionsOfAccess ex:LabeledLinkExample_qZc ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor ex:PersonExample_zZc ;
            schema1:roleName "editor" ] ;
    schema1:creator ( [ a schema1:Person ;
                schema1:contactPoint [ a schema1:ContactPoint ;
                        schema1:email "author@example.org" ] ;
                schema1:identifier "https://orcid.org/0000-0001-2345-6789" ;
                schema1:name "Example, Author" ] ) ;
    schema1:dateModified "2022-12-12" ;
    schema1:datePublished "2021-11-14" ;
    schema1:description "description of resource" ;
    schema1:identifier "https://doi.org/23566/aslry" ;
    schema1:inLanguage "en" ;
    schema1:keywords "bathymetry",
        "ocean floor" ;
    schema1:license "https://creativecommons.org/publicdomain/zero/1.0/" ;
    schema1:name "Bathymetry Bay of Biscay" ;
    schema1:publishingPrinciples "https://example.org/principles/3478" ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "related data" ],
        [ a schema1:LinkRole ;
            schema1:linkRelationship [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "https://www.iana.org/assignments/link-relations/" ;
                    schema1:name "related dataset" ;
                    schema1:termCode "related" ] ] ;
    schema1:subjectOf [ ns1:conformsTo <https://w3id.org/cdif/discovery/1.0/> ] ;
    schema1:url "https://example.org/landingPage254266" ;
    schema1:version "1.0" .

ex:LabeledLinkExample_qZc a schema1:CreativeWork ;
    schema1:description "URL to get the document" ;
    schema1:name "conditions of access statement" ;
    schema1:url "https://example.org/conditions/2342747" .

ex:PersonExample_zZc a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "joe@example.org" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://orcid.org" ;
            schema1:url "https://orcid.org/0000-0002-9876-5432" ;
            schema1:value "0000-0002-9876-5432" ] ;
    schema1:name "Joe B. Test" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: 'Optional properties for CDIF discovery metadata schema, with schema: prefixes'
description: Building block specifies properties for CDIF schama.org discovery record
properties:
  '@context':
    type: object
    description: Additional JSON-LD namespace prefixes used by optional CDIF properties.
    properties:
      geosparql:
        const: http://www.opengis.net/ont/geosparql#
      prov:
        const: http://www.w3.org/ns/prov#
      dqv:
        const: http://www.w3.org/ns/dqv#
      cdi:
        const: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  schema:description:
    type: string
    description: A short summary describing a dataset. This text will be indexed by
      search applications, so the more information here, the better.
  schema:additionalType:
    description: identifiers for datatypes from other vocabularies (not schema.org)
      that apply to this metadata.
    type: array
    minItems: 0
    items:
      anyOf:
      - type: string
      - $ref: '#/$defs/DefinedTerm'
  schema:sameAs:
    description: Other identifiers for the dataset, as IRI references, literal strings,
      or structured identifiers using schema:PropertyValue.
    type: array
    minItems: 1
    items:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: IRI for an equivalent resource or alternate identifier
      - $ref: '#/$defs/Identifier'
  schema:version:
    type:
    - string
    - number
    description: The version number or identifier for this dataset (text or numeric).
      The values should sort from oldest to newest using an alphanumeric sort on version
      strings
  schema:inLanguage:
    type: string
    description: the language of the dataset content
  schema:datePublished:
    type: string
    description: ISO8601 formatted date (and optional time if relevant) when Dataset
      was made public.
  schema:relatedLink:
    type: array
    description: links to related resources; linkRelationship specifies how the resource
      is related.
    items:
      type: object
      properties:
        '@type':
          anyOf:
          - type: string
            const: schema:LinkRole
          - type: array
            items:
              type: string
            contains:
              const: schema:LinkRole
        schema:linkRelationship:
          anyOf:
          - $ref: '#/$defs/DefinedTerm'
          - type: string
        schema:target:
          type: object
          properties:
            '@type':
              anyOf:
              - type: string
                const: schema:EntryPoint
              - type: array
                items:
                  type: string
                contains:
                  const: schema:EntryPoint
            schema:encodingFormat:
              type: string
              description: registered MIME types are expected
            schema:name:
              type: string
            schema:url:
              type: string
              format: uri
  schema:publishingPrinciples:
    description: FDOF digitalObjectMutability, RDA digitalObjectPolicy, FDOF PersistencyPolicy.
      Policies related to maintenance, update, expected time to live. If an online
      resource documents the policies or a URI is used to identify the conditions,
      recommend using schema:CreativeWork to provide a label (name) and an identifier
      (URI or URL).
    type: array
    minItems: 0
    items:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: a reference to a publishing principles statement
      - $ref: '#/$defs/LabeledLink'
  schema:measurementTechnique:
    description: The technique, technology, or methodology used for measurement or
      determination of the dataset values. Can be a string, a URI reference, a DefinedTerm,
      or an array combining these.
    anyOf:
    - type: string
    - $ref: '#/$defs/DefinedTerm'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/DefinedTerm'
  schema:keywords:
    description: Keywords are an array of strings, an array of schema:DefinedTerms,
      or some combination of these. If you have information about a controlled vocabulary
      from which keywords come from, use schema:DefinedTerm to descibe that keyword.
      This allowed variability makes parsing metadata hard; recommend using DefinedTerm
      for all keywords if any of them are from a known vocabulary, otherwise an array
      of strings.
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/DefinedTerm'
      - type: string
  schema:creator:
    description: author or orginator of intellectual content of dataset. Uset the
      JSON-LD @list construct to preserve author order. Use contributor with the Role
      property to specify other roles related to creation or stewardship of the resource.
    type: object
    properties:
      '@list':
        type: array
        items:
          anyOf:
          - type: object
            properties:
              '@id':
                type: string
                description: a identifier for an agent defined in this metadata, or
                  externally; must be dereferenceable
            required:
            - '@id'
          - $ref: '#/$defs/Person'
          - $ref: '#/$defs/Organization'
  schema:contributor:
    description: other parties who played a role in production of dataset
    type: array
    items:
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
      - $ref: '#/$defs/Contributor'
  schema:publisher:
    description: Party who made the dataset publicly available
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
  schema:provider:
    description: Party who maintains the distribution options for the dataset. If
      there are multiple distributions from different providers, use the provider
      property on distribution/DataDownload
    type: array
    items:
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
  schema:funding:
    type: array
    items:
      $ref: '#/$defs/Funder'
  schema:variableMeasured:
    description: What does the dataset measure? (e.g., temperature, pressure)
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/VariableMeasured'
      - $ref: '#/$defs/StatisticalVariable'
  schema:spatialCoverage:
    description: To specify location that is the subject of resource content; use
      schema.org place names, bounding box, point or optional OGC WKT gemetry.
    type: array
    items:
      $ref: '#/$defs/SpatialExtent'
  schema:temporalCoverage:
    description: The time interval during which data was collected or observations
      were made; or a time period that an activity or collection is linked to intellectually
      or thematically (for example, 1997 to 1998; the 18th century) (see https://documentation.ardc.edu.au/display/DOC/Temporal+coverage).
      For documentation of Earth Science, Paleobiology or Paleontology datasets, we
      are interested in the second case-- the time period that data are linked to
      thematically.
    type: array
    items:
      $ref: '#/$defs/TemporalExtent'
  prov:wasGeneratedBy:
    description: Brief information about instruments, software or experimental protocols
      used
    type: array
    items:
      $ref: '#/$defs/GeneratedBy'
  prov:wasDerivedFrom:
    description: Brief information about sources of data used in aggregate datasets
    type: array
    items:
      $ref: '#/$defs/DerivedFrom'
  dqv:hasQualityMeasurement:
    description: Brief information quality measurements reported to assess the resource
    type: array
    items:
      $ref: '#/$defs/QualityMeasure'
  schema:subjectOf:
    properties:
      dcterms:conformsTo:
        type: array
        items:
          type: object
          properties:
            '@id':
              type: string
              description: uri for specifications that this metadata record conforms
                to
        minItems: 1
        contains:
          type: object
          properties:
            '@id':
              const: https://w3id.org/cdif/discovery/1.0/
  schema:distribution:
    description: Distribution options for the dataset.
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/DataDownload'
      - $ref: '#/$defs/WebAPI'
$defs:
  LabeledLink:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
  Identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  Person:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
  Organization:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
  Contributor:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.yaml
  Funder:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/funder/schema.yaml
  VariableMeasured:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.yaml
  StatisticalVariable:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/statisticalVariable/schema.yaml
  SpatialExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
  TemporalExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/temporalExtent/schema.yaml
  GeneratedBy:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/generatedBy/schema.yaml
  DerivedFrom:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/derivedFrom/schema.yaml
  QualityMeasure:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/schema.yaml
  DataDownload:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.yaml
  WebAPI:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/webAPI/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifOptional/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifOptional/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "time": "http://www.w3.org/2006/time#",
    "prov": "http://www.w3.org/ns/prov#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifOptional/context.jsonld)

## Sources

* [schema.org](https://schema.org/Dataset)
* [Cross Domain Interoperability Framework Discovery Profile](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/discovery.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifOptional`

