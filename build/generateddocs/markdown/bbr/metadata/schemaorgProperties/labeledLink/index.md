
# Labeled Link (Schema)

`cdif.bbr.metadata.schemaorgProperties.labeledLink` *v0.1*

Schema for a labeled link, implemented as a profile of schema.org/CreativeWork: a resolvable URL with an optional name and description. Optionally carries the DCAT relation surface for a link that expresses a typed relationship. Absorbed the cdifDataType/cdifReference block on 2026-09-23, which was this schema plus exactly these two optional properties. Defines properties: @type, schema:name, schema:description, schema:url, dcat:hadRole, dcterms:relation. Uses building blocks: cdifConceptOrTermOrString (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Labeled Link properties

Defines a set of properties for use describing a web link (url) with a label to indicate the target, like an html:anchor. For the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Labeled Link building block.
Example labeled link instance.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "ex:LabeledLinkExample_zZc",
  "@type": [
    "schema:CreativeWork"
  ],
  "schema:name": "Some related resource",
  "schema:description": "URL to get the related resource",
  "schema:url": "https://example.org/relatedresource/2342747"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@id": "ex:LabeledLinkExample_zZc",
  "@type": [
    "schema:CreativeWork"
  ],
  "schema:name": "Some related resource",
  "schema:description": "URL to get the related resource",
  "schema:url": "https://example.org/relatedresource/2342747"
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:LabeledLinkExample_zZc a schema1:CreativeWork ;
    schema1:description "URL to get the related resource" ;
    schema1:name "Some related resource" ;
    schema1:url "https://example.org/relatedresource/2342747" .


```


### Complete labeled link example.
LabeledLink instance exercising all properties: name, description, and url.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/"
  },
  "@id": "ex:LabeledLinkComplete_001",
  "@type": ["schema:CreativeWork"],
  "schema:name": "Data Quality Assessment Report",
  "schema:description": "Detailed report documenting the quality control procedures, flagging criteria, and validation results for this dataset",
  "schema:url": "https://example.org/reports/quality-assessment-2024.pdf"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:LabeledLinkComplete_001",
  "@type": [
    "schema:CreativeWork"
  ],
  "schema:name": "Data Quality Assessment Report",
  "schema:description": "Detailed report documenting the quality control procedures, flagging criteria, and validation results for this dataset",
  "schema:url": "https://example.org/reports/quality-assessment-2024.pdf"
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:LabeledLinkComplete_001 a schema1:CreativeWork ;
    schema1:description "Detailed report documenting the quality control procedures, flagging criteria, and validation results for this dataset" ;
    schema1:name "Data Quality Assessment Report" ;
    schema1:url "https://example.org/reports/quality-assessment-2024.pdf" .


```


### Labeled link expressing a relation.
A labeled link that also declares dcat:Relationship and carries
dcterms:relation -- the DCAT pointer to the related resource, distinct from
schema:url, which is the link's own presentation URL.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "ex": "https://example.org/"
  },
  "@id": "ex:CdifRelationExample_001",
  "@type": ["schema:CreativeWork", "dcat:Relationship"],
  "schema:name": "Predecessor version of this dataset",
  "schema:url": "https://example.org/datasets/source-2023",
  "dcterms:relation": "https://example.org/datasets/source-2023"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:CdifRelationExample_001",
  "@type": [
    "schema:CreativeWork",
    "dcat:Relationship"
  ],
  "schema:name": "Predecessor version of this dataset",
  "schema:url": "https://example.org/datasets/source-2023",
  "dcterms:relation": "https://example.org/datasets/source-2023"
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:CdifRelationExample_001 a schema1:CreativeWork,
        dcat:Relationship ;
    dcterms:relation "https://example.org/datasets/source-2023" ;
    schema1:name "Predecessor version of this dataset" ;
    schema1:url "https://example.org/datasets/source-2023" .


```


### Complete relation example, with a SKOS-typed role.
The full relation surface: dcat:hadRole classifying the relationship with a
skos:Concept, alongside dcterms:relation and the descriptive properties.
Moved here from cdifDataType/cdifReference when that block was folded into
this one.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "ex": "https://example.org/"
  },
  "@id": "ex:CdifRelationComplete_001",
  "@type": [
    "schema:CreativeWork",
    "dcat:Relationship"
  ],
  "schema:name": "Predecessor version of this dataset",
  "schema:description": "Relationship pointing at the previous published version, expressed in the DCAT qualifiedRelation pattern with a SKOS-typed role.",
  "schema:url": "https://example.org/datasets/source-2023",
  "dcterms:relation": "https://doi.org/10.5281/zenodo.7654320",
  "dcat:hadRole": {
    "@id": "ex:concepts/isVersionOf",
    "@type": [
      "skos:Concept"
    ],
    "skos:prefLabel": {
      "@value": "is version of",
      "@language": "en"
    },
    "skos:definition": {
      "@value": "The related resource is a version, edition, or adaptation of the described resource.",
      "@language": "en"
    },
    "skos:inScheme": {
      "@id": "ex:vocab/relationRoles"
    },
    "skos:notation": "isVersionOf"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/context.jsonld",
    {
      "schema": "http://schema.org/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:CdifRelationComplete_001",
  "@type": [
    "schema:CreativeWork",
    "dcat:Relationship"
  ],
  "schema:name": "Predecessor version of this dataset",
  "schema:description": "Relationship pointing at the previous published version, expressed in the DCAT qualifiedRelation pattern with a SKOS-typed role.",
  "schema:url": "https://example.org/datasets/source-2023",
  "dcterms:relation": "https://doi.org/10.5281/zenodo.7654320",
  "dcat:hadRole": {
    "@id": "ex:concepts/isVersionOf",
    "@type": [
      "skos:Concept"
    ],
    "skos:prefLabel": {
      "@value": "is version of",
      "@language": "en"
    },
    "skos:definition": {
      "@value": "The related resource is a version, edition, or adaptation of the described resource.",
      "@language": "en"
    },
    "skos:inScheme": {
      "@id": "ex:vocab/relationRoles"
    },
    "skos:notation": "isVersionOf"
  }
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ex:CdifRelationComplete_001 a schema1:CreativeWork,
        dcat:Relationship ;
    dcterms:relation "https://doi.org/10.5281/zenodo.7654320" ;
    schema1:description "Relationship pointing at the previous published version, expressed in the DCAT qualifiedRelation pattern with a SKOS-typed role." ;
    schema1:name "Predecessor version of this dataset" ;
    schema1:url "https://example.org/datasets/source-2023" ;
    dcat:hadRole <https://example.org/concepts/isVersionOf> .

<https://example.org/concepts/isVersionOf> a skos:Concept ;
    skos:definition "The related resource is a version, edition, or adaptation of the described resource."@en ;
    skos:inScheme <https://example.org/vocab/relationRoles> ;
    skos:notation "isVersionOf" ;
    skos:prefLabel "is version of"@en .


```


### A pure DCAT relationship, with no schema.org co-type.
A dcat:Relationship on its own: no schema:CreativeWork, no schema:url, and
both DCAT-native forms -- dcterms:relation as an @id reference and
dcat:hadRole typed dcat:Role, which is DCAT's declared range for that
property.

This is the first example in the register of the shape a DCAT catalogue
actually produces, and the absence of one is why three separate problems went
unnoticed until a PSDI validator reported them from outside
(profile-core#16). Every other example here declares both co-types and
carries a schema:url, so none of them could reach the paths that were broken:
CDIFRelationShape demanding schema:url of a class that has no such property,
dcterms:relation rejecting the @id form DCMI recommends, and dcat:hadRole
accepting only one of the five value forms the JSON Schema permits.

Keep an example of this shape. A constraint on a class nothing instantiates
is a constraint nothing tests.
#### json
```json
{
  "@context": {
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "ex": "https://example.org/"
  },
  "@id": "ex:CdifDcatRelationshipExample_001",
  "@type": ["dcat:Relationship"],
  "dcterms:relation": {
    "@id": "ex:datasets/source-2023"
  },
  "dcat:hadRole": {
    "@id": "http://www.iana.org/assignments/relation/describedby",
    "@type": ["dcat:Role"]
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/context.jsonld",
    {
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:CdifDcatRelationshipExample_001",
  "@type": [
    "dcat:Relationship"
  ],
  "dcterms:relation": {
    "@id": "ex:datasets/source-2023"
  },
  "dcat:hadRole": {
    "@id": "http://www.iana.org/assignments/relation/describedby",
    "@type": [
      "dcat:Role"
    ]
  }
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .

ex:CdifDcatRelationshipExample_001 a dcat:Relationship ;
    dcterms:relation <https://example.org/datasets/source-2023> ;
    dcat:hadRole <http://www.iana.org/assignments/relation/describedby> .

<http://www.iana.org/assignments/relation/describedby> a dcat:Role .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Schema for a labeled link, a profile of schema.org/CreativeWork: a resolvable
  URL with an optional name and description. Optionally carries the DCAT relation
  surface (dcat:hadRole, dcterms:relation) for a link that expresses a typed relationship
  rather than a plain reference.

  Those two properties were a separate block, cdifDataType/cdifReference, which was
  an allOf of this schema plus exactly those two optional properties and nothing else
  -- its dcat:Relationship co-type mandate had already been removed because it made
  every labeled link unsatisfiable and broke every schema:license example that followed
  schema.org''s own advice. Since both are optional, folding them in here changes
  no document''s validity while removing a block and five levels of $defs/Reference
  indirection. cdifReference was retired 2026-09-23.'
type: object
properties:
  '@type':
    description: 'Either construct, or both. A labeled link is a schema:CreativeWork
      at a URL; a dcat:Relationship is DCAT''s association class for a typed relation
      to another resource. A node may declare both -- CDIF''s own relation examples
      do -- but NEITHER IS REQUIRED TO ACCOMPANY THE OTHER.

      That is the whole point of the anyOf. Until 2026-09-08 this block''s Relation
      half required contains: dcat:Relationship while the labeled-link half required
      contains: schema:CreativeWork, and under allOf both applied to every instance,
      so an ordinary labeled link was unsatisfiable. Of profile-core''s licenses the
      29 plain strings and 1 @id-reference passed while the 10 that followed schema.org''s
      own recommendation -- "use schema:CreativeWork to provide a label (name) for
      the license" -- failed. 412782113 fixed that by deleting the dcat:Relationship
      mandate outright, which left the JSON Schema with no notion of dcat:Relationship
      at all while rules.shacl went on targeting it as a class. A pure DCAT relation
      then met a SHACL requirement with no schema counterpart. This anyOf restores
      the type to the schema WITHOUT restoring the conjunction.'
    default:
    - schema:CreativeWork
    type: array
    items:
      type: string
    minItems: 1
    anyOf:
    - contains:
        const: schema:CreativeWork
    - contains:
        const: dcat:Relationship
  schema:name:
    type: string
    x-jsonld-id: http://schema.org/name
  schema:description:
    type: string
    x-jsonld-id: http://schema.org/description
  schema:url:
    type: string
    format: uri
    x-jsonld-id: http://schema.org/url
  dcat:hadRole:
    description: 'Role of the related resource. Present only on a link that expresses
      a relationship; a plain labeled link such as a license omits it.

      DCAT''s declared range is dcat:Role (dcat.ttl: rdfs:range dcat:Role, and dcat:Role
      rdfs:subClassOf skos:Concept), so the DCAT-native form is a node typed dcat:Role.
      That form was NOT accepted here before 2026-10-01: this property was cdifConceptOrTermOrString
      alone, which matches a bare string, a sealed @id reference, a schema:DefinedTerm
      or a skos:Concept -- none of which a dcat:Role-typed node satisfies, because
      JSON Schema does no subclass reasoning.

      dcat:Role is added as a branch rather than replacing the others, so the DCAT-native
      form becomes valid without invalidating anything already written. Note this
      leaves CDIF LOOSER than DCAT, deliberately: DCAT''s range is dcat:Role alone,
      and CDIF also accepts a plain skos:Concept, a DefinedTerm, an @id reference
      and a string. That is the same both-forms stance taken on dcterms:relation,
      and it is a choice rather than an oversight -- do not read the extra branches
      as something not yet tightened.'
    anyOf:
    - $ref: '#/$defs/DcatRole'
    - $ref: '#/$defs/cdifConceptOrTermOrString'
    x-jsonld-id: http://www.w3.org/ns/dcat#hadRole
  dcterms:relation:
    description: 'The related resource -- the DCAT canonical pointer to what is being
      related to, which is distinct from schema:url, the presentation URL of the link
      itself.

      An @id reference is the RECOMMENDED form and a string is permitted, which is
      DCMI''s own position: "Recommended practice is to identify the related resource
      by means of a URI. If this is not possible or feasible, a string conforming
      to a formal identification system may be provided." DCMI declares no rdfs:range
      for this property, and of the 13 DCMI properties carrying an "intended to be
      used with non-literal values" restriction, this is deliberately not one. dcat.ttl
      does not re-declare or constrain it at all -- the only triple mentioning it
      in the whole DCAT vocabulary is `dcat:distribution rdfs:subPropertyOf dcterms:relation`.

      So objectReference-only would be stricter than both DCAT and DCMI and would
      reject a form the specification sanctions. The anyOf matches how schema:additionalType
      is handled here: both forms valid, the object form used in examples and required
      only where a `contains` pins a specific value.

      It was string-only until 2026-10-01, which rejected the @id form outright. Reported
      from outside by a PSDI validator taking a things-not-strings approach (profile-core#16):
      their DCAT catalogue mirrors the DCAT-3 spec examples and wrote {"@id": ...},
      which failed both layers -- while CDIF''s own documented URI serialization policy
      (agents.md) says URI values SHOULD be {"@id": ...}. The register required the
      one form its own policy argues against.'
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
    - type: string
      format: uri
    x-jsonld-id: http://purl.org/dc/terms/relation
required:
- '@type'
allOf:
- if:
    required:
    - '@type'
    properties:
      '@type':
        contains:
          const: schema:CreativeWork
  then:
    required:
    - schema:url
$defs:
  cdifConceptOrTermOrString:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTermOrString/schema.yaml
  DcatRole:
    description: 'A dcat:Role -- DCAT''s declared range for dcat:hadRole. Defined
      inline rather than as its own building block because nothing else in the register
      needs it yet; dcat:hadRole''s domain is owl:unionOf [prov:Attribution, dcat:Relationship],
      so promote it to a block if a qualified attribution ever needs the same shape.

      dcat:Role rdfs:subClassOf skos:Concept, so the skos:prefLabel / skos:inScheme
      furniture of a concept is permitted alongside; it is not required here because
      DCAT states no cardinality constraints on the class -- dcat.ttl declares no
      rdfs:subClassOf and no owl:Restriction on dcat:Relationship, and the "mandatory"
      wording in the DCAT-3 document is prose in the spec tables rather than an axiom
      in the vocabulary.'
    type: object
    properties:
      '@id':
        type: string
        description: IRI of the role concept, ideally from a controlled vocabulary.
      '@type':
        type: array
        items:
          type: string
        contains:
          const: dcat:Role
        minItems: 1
    required:
    - '@type'
x-jsonld-prefixes:
  schema: http://schema.org/
  skos: http://www.w3.org/2004/02/skos/core#
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/context.jsonld)

## Sources

* [schema.org](https://schema.org/CreativeWork)
* [DCAT Relationship](https://www.w3.org/TR/vocab-dcat-3/#Class:Relationship)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/labeledLink`

