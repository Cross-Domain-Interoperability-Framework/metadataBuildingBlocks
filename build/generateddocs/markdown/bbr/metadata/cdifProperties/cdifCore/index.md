
# CDIF Core metadata (Schema)

`cdif.bbr.metadata.cdifProperties.cdifCore` *v0.1*

Definition of metadata elements that are required for CDIF core metadata. Defines properties: @id, @type, schema:name, schema:identifier, schema:dateModified, schema:conditionsOfAccess, schema:license, schema:url, schema:distribution, schema:subjectOf. Uses building blocks: labeledLink (schemaorgProperties), identifier (schemaorgProperties), definedTerm (schemaorgProperties), dataDownload (schemaorgProperties), webAPI (schemaorgProperties), cdifCatalogRecord (cdifProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Base Metadata properties

Defines simple properties included in CDIF discvoery metadata for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Example CDIF discovery, Minimal.
Example CDIF discovery instance with mandatory properties only.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:baseDiscovery23578",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Bathymetry Bay of Biscay",
  "schema:identifier": "https://doi.org/23566/aslry",
  "schema:url": "https://example.org/landingPage254266",
  "schema:dateModified": "2022-12-12",
  "schema:license": [
    "https://creativecommons.org/publicdomain/zero/1.0/"
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:URIforMetadata3575",
    "schema:about": {
      "@id": "ex:baseDiscovery23578"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore"
      },
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      }
    ],
    "schema:maintainer": {
      "@id": "https://orcid.org/3333-4442-9456-9347",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Goodge, Alice",
      "schema:alternateName": "Metadata curator",
      "schema:contactPoint": {
        "@id": "ex:aContactPoint",
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "goodgea@bwc.org"
      },
      "schema:identifier": {
        "@id": "ex:maintainerIdentifier",
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
        "schema:url": "https://orcid.org/3333-4442-9456-9347"
      }
    },
    "schema:sdDatePublished": "2025-10-24",
    "schema:includedInDataCatalog": {
      "@id": "https://ror.org/04sfkyrt24",
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "Global Wildlife Aggregator",
      "schema:url": "http://example.com/wildlifecatalog"
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCore/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:baseDiscovery23578",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Bathymetry Bay of Biscay",
  "schema:identifier": "https://doi.org/23566/aslry",
  "schema:url": "https://example.org/landingPage254266",
  "schema:dateModified": "2022-12-12",
  "schema:license": [
    "https://creativecommons.org/publicdomain/zero/1.0/"
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:URIforMetadata3575",
    "schema:about": {
      "@id": "ex:baseDiscovery23578"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore"
      },
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      }
    ],
    "schema:maintainer": {
      "@id": "https://orcid.org/3333-4442-9456-9347",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Goodge, Alice",
      "schema:alternateName": "Metadata curator",
      "schema:contactPoint": {
        "@id": "ex:aContactPoint",
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "goodgea@bwc.org"
      },
      "schema:identifier": {
        "@id": "ex:maintainerIdentifier",
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
        "schema:url": "https://orcid.org/3333-4442-9456-9347"
      }
    },
    "schema:sdDatePublished": "2025-10-24",
    "schema:includedInDataCatalog": {
      "@id": "https://ror.org/04sfkyrt24",
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "Global Wildlife Aggregator",
      "schema:url": "http://example.com/wildlifecatalog"
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:URIforMetadata3575 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore>,
        <https://w3id.org/cdif/core/1.0/> ;
    schema1:about ex:baseDiscovery23578 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:includedInDataCatalog <https://ror.org/04sfkyrt24> ;
    schema1:maintainer <https://orcid.org/3333-4442-9456-9347> ;
    schema1:sdDatePublished "2025-10-24" .

ex:aContactPoint a schema1:ContactPoint ;
    schema1:email "goodgea@bwc.org" .

ex:baseDiscovery23578 a schema1:Dataset ;
    schema1:dateModified "2022-12-12" ;
    schema1:identifier "https://doi.org/23566/aslry" ;
    schema1:license "https://creativecommons.org/publicdomain/zero/1.0/" ;
    schema1:name "Bathymetry Bay of Biscay" ;
    schema1:subjectOf ex:URIforMetadata3575 ;
    schema1:url "https://example.org/landingPage254266" .

ex:maintainerIdentifier a schema1:PropertyValue ;
    schema1:propertyID "https://registry.identifiers.org/registry/orcid" ;
    schema1:url "https://orcid.org/3333-4442-9456-9347" .

<https://orcid.org/3333-4442-9456-9347> a schema1:Person ;
    schema1:alternateName "Metadata curator" ;
    schema1:contactPoint ex:aContactPoint ;
    schema1:identifier ex:maintainerIdentifier ;
    schema1:name "Goodge, Alice" .

<https://ror.org/04sfkyrt24> a schema1:DataCatalog ;
    schema1:name "Global Wildlife Aggregator" ;
    schema1:url "http://example.com/wildlifecatalog" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: 'Core properties for CDIF metadata schema, with schema: prefixes'
description: Building block specifies core properties for CDIF schema.org metadata
  record, applicable to any resource type.
properties:
  '@context':
    type: object
    description: JSON-LD context declaring namespace prefixes used in the metadata
      record.
    properties:
      schema:
        const: http://schema.org/
      dcterms:
        const: http://purl.org/dc/terms/
      spdx:
        const: http://spdx.org/rdf/terms#
      dcat:
        const: http://www.w3.org/ns/dcat#
      prov:
        const: http://www.w3.org/ns/prov#
    required:
    - schema
    - dcterms
    - dcat
    - prov
  '@id':
    type: string
    description: 'The URI for the resource should be the @id value for the root of
      the JSON instance document tree. Must be an IRI (e.g. https://doi.org/..., urn:...,
      or a relative URI like #localid). Note that this identifier can be interpreted
      to identify the resource that is the subject of this metadata record, or the
      JSON-LD object that is the digital object containing the metadata information.'
  '@type':
    description: a schema.org Class that specifies the expected information content
      for the metadata record. The array must include at least one schema.org type
      value. Default is schema:Dataset.
    type: array
    items:
      type: string
      enum:
      - schema:CreativeWork
      - schema:SoftwareApplication
      - schema:SoftwareSourceCode
      - schema:Product
      - schema:WebAPI
      - schema:Dataset
      - schema:DigitalDocument
      - schema:Collection
      - schema:ImageObject
      - schema:DataCatalog
      - schema:DefinedTermSet
      - schema:MediaObject
    default: schema:Dataset
    minItems: 1
    contains:
      const: schema:Dataset
  schema:name:
    type: string
    description: A descriptive name of a dataset (e.g., 'Snow depth in Northern Hemisphere').
      The name should uniquely identify the described resource for human use, in the
      scope of the metadata catalog containing this metadata record.
  schema:description:
    type: string
    description: A short summary describing a dataset. This text will be indexed by
      search applications, so the more information here, the better.
  schema:identifier:
    description: The primary identifier for the dataset; other identifiers should
      be listed in the sameAs field. Schema.org has three ways of encoding identifiers--
      a text description, a URL, or by using the schema:PropertyValue field. The Science
      on Schema.org guidance strongly recommends using the PropertyValue approach.
      see https://github.com/ESIPFed/science-on-schema.org   .... Dataset.md#identifier.  Ideally,
      for any given data provided they would provide identifiers either all as strings
      or all as identifier_type.
    anyOf:
    - $ref: '#/$defs/Identifier'
    - type: string
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
  schema:dateModified:
    type: string
    description: ISO8601 formatted date (and optional time if relevant) when Dataset
      was last updated
  schema:datePublished:
    type: string
    description: ISO8601 formatted date (and optional time if relevant) when Dataset
      was made public.
  schema:conditionsOfAccess:
    description: 'text statement of conditions for use and access; if an online resource
      documents the restrictions or a URI is used to identify the conditions, recommend
      using schema:CreativeWork to provide a label (name) and an identifier (URI or
      URL). '
    type: array
    minItems: 0
    items:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: a reference to a resource defining conditions of Access
      - $ref: '#/$defs/LabeledLink'
  schema:license:
    description: 'legal statement of conditions for use and access; recommend using
      schema:CreativeWork to provide a label (name) for the license, and an identifier.
      Sources of license identifiers: https://opensource.org/licenses/, https://creativecommons.org/about/cclicenses/,
      https://spdx.org/licenses/, http://cor.esipfed.org/ont/earthcube/swl. If only
      a string is provided, it should be an identifier for the license, ideally a
      resolvable URI'
    type: array
    minItems: 0
    items:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: a reference to a license defintion
      - $ref: '#/$defs/LabeledLink'
  schema:url:
    type: string
    format: uri
    description: Web Location of a page describing the dataset (landing page), typically
      providing links or instructions to get the actual resource content; analogous
      to dcat:accessURL. If a direct link is available to get the data, put in distribution/contentUrl
  schema:distribution:
    description: specifies how to download the data in a specific format or access
      via a web API. This property describes where to get the data and in what format
      by using the schema:DataDownload type. If user must access data through a landing
      page, provide link to landing page in the 'url' property for the dataset
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/DataDownload'
      - $ref: '#/$defs/WebAPI'
  schema:relatedLink:
    type: array
    description: links to related resources; linkRelationship specifies how the resource
      is related.
    items:
      type: object
      properties:
        '@type':
          type: array
          items:
            type: string
          contains:
            const: schema:LinkRole
          minItems: 1
        schema:linkRelationship:
          anyOf:
          - $ref: '#/$defs/DefinedTerm'
          - type: string
        schema:target:
          type: object
          properties:
            '@type':
              type: array
              items:
                type: string
              contains:
                const: schema:EntryPoint
              minItems: 1
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
  schema:subjectOf:
    $ref: '#/$defs/CdifCatalogRecord'
allOf:
- properties:
    schema:subjectOf:
      properties:
        dcterms:conformsTo:
          contains:
            type: object
            properties:
              '@id':
                const: https://w3id.org/cdif/core/1.0/
- required:
  - '@id'
  - '@type'
  - '@context'
  - schema:name
  - schema:identifier
  - schema:dateModified
  - schema:subjectOf
- anyOf:
  - required:
    - schema:license
  - required:
    - schema:conditionsOfAccess
- anyOf:
  - required:
    - schema:url
  - required:
    - schema:distribution
$defs:
  LabeledLink:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
  Identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  DataDownload:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.yaml
  WebAPI:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/webAPI/schema.yaml
  Person:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
  Organization:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
  Contributor:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.yaml
  Funder:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/funder/schema.yaml
  GeneratedBy:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/generatedBy/schema.yaml
  DerivedFrom:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/derivedFrom/schema.yaml
  CdifCatalogRecord:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCatalogRecord/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCore/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCore/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCore/context.jsonld)

## Sources

* [schema.org](https://schema.org/Dataset)
* [Cross Domain Interoperability Framework Discovery Profile](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/discovery.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifCore`

