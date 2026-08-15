
# CDIF Manifest (Schema)

`cdif.bbr.metadata.profiles.cdifProfile.cdifManifest` *v0.1*

Profile module for packages: the resources that make up a dataset and where to retrieve each of them. Declares schema:hasPart in the two places a package needs it -- on the schema:Dataset, for parts that are independently accessible at their own addresses (resourcePartArray / resourcePartItem), and on a schema:distribution item, for component files inside a bundle that have no address of their own (archivePartArray / archivePartItem). Note that schema:hasPart carries a different meaning on schema:instrument (sub-components of an instrument system) and on a bioschemas ComputationalWorkflow; the object it sits on is what disambiguates them. Both part shapes here carry schema:about, so a part that describes another -- a codebook, a data dictionary, a metadata sidecar -- can say which one. Requires that the metadata record declare conformance to https://w3id.org/cdif/manifest/1.1, and requires schema:hasPart on any distribution positively typed with schema:Collection in @type (alongside schema:DataDownload). (Merged from the previous cdifArchive building block, which only published the archive $defs.)

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Manifest

Adds archive distribution as a valid `schema:distribution` item type. The `cdifOptional` building block already defines `schema:distribution` with DataDownload and WebAPI options; this building block extends that with the [cdifArchive](../cdifArchive/) option.

### Dependencies

- [cdifArchive](../cdifArchive/) - archive item schema (DataDownload with hasPart component files)

## Examples

### Minimal CDIF Manifest
Bare schema:Dataset with one archive distribution exercising
cdifArchive at the smallest valid shape.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/"
  },
  "@type": ["schema:Dataset"],
  "@id": "ex:dataset/minimal-archived",
  "schema:name": "Minimal archived dataset",
  "schema:subjectOf": {
    "dcterms:conformsTo": [
      { "@id": "https://w3id.org/cdif/manifest/1.1" }
    ]
  },
  "schema:distribution": [
    {
      "@type": ["schema:DataDownload", "schema:Collection"],
      "schema:name": "Bundle",
      "schema:contentUrl": "https://example.org/data/bundle.zip",
      "schema:encodingFormat": ["application/zip"],
      "schema:hasPart": [
        {
          "@id": "#part-1",
          "@type": ["schema:MediaObject"],
          "schema:name": "data.csv",
          "schema:encodingFormat": ["text/csv"]
        }
      ]
    }
  ]
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifManifest/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "schema:Dataset"
  ],
  "@id": "ex:dataset/minimal-archived",
  "schema:name": "Minimal archived dataset",
  "schema:subjectOf": {
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/manifest/1.1"
      }
    ]
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "schema:Collection"
      ],
      "schema:name": "Bundle",
      "schema:contentUrl": "https://example.org/data/bundle.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "schema:hasPart": [
        {
          "@id": "#part-1",
          "@type": [
            "schema:MediaObject"
          ],
          "schema:name": "data.csv",
          "schema:encodingFormat": [
            "text/csv"
          ]
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/dataset/minimal-archived> a schema1:Dataset ;
    schema1:distribution [ a schema1:Collection,
                schema1:DataDownload ;
            schema1:contentUrl "https://example.org/data/bundle.zip" ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart <file:///github/workspace/#part-1> ;
            schema1:name "Bundle" ] ;
    schema1:name "Minimal archived dataset" ;
    schema1:subjectOf [ dcterms:conformsTo <https://w3id.org/cdif/manifest/1.1> ] .

<file:///github/workspace/#part-1> a schema1:MediaObject ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "data.csv" .


```


### Complete CDIF Manifest
Geochemistry-package Dataset with full schema:subjectOf CatalogRecord,
SPDX checksum on the archive distribution, and a full hasPart manifest.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "spdx": "http://spdx.org/rdf/terms#",
    "ex": "https://example.org/"
  },
  "@id": "ex:dataset_archive_001",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Geochemical Analysis Results Package",
  "schema:identifier": "https://doi.org/10.1234/geochem-archive-2025",
  "schema:url": "https://example.org/datasets/geochem-archive-2025",
  "schema:dateModified": "2025-08-01",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "ex:metadata_archive_001",
    "schema:about": {
      "@id": "ex:dataset_archive_001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/manifest/1.1"
      }
    ]
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "schema:Collection"
      ],
      "schema:name": "Geochemistry results archive",
      "schema:contentUrl": "https://example.org/downloads/geochem-results-2025.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "https://w3id.org/cdif/manifest/1.1"
        }
      ],
      "schema:hasPart": [
        {
          "@id": "#data-csv",
          "@type": [
            "schema:MediaObject"
          ],
          "schema:name": "results.csv",
          "schema:description": "Tabular geochemical analysis results",
          "schema:encodingFormat": [
            "text/csv"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 245000,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "sha256",
            "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
          }
        },
        {
          "@id": "#metadata-json",
          "@type": [
            "schema:MediaObject"
          ],
          "schema:name": "metadata.json",
          "schema:description": "Metadata sidecar for the results file",
          "schema:encodingFormat": [
            "application/json"
          ],
          "schema:about": [
            {
              "@id": "#data-csv"
            }
          ]
        }
      ]
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "spdx": "http://spdx.org/rdf/terms#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifManifest/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "spdx": "http://spdx.org/rdf/terms#",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:dataset_archive_001",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Geochemical Analysis Results Package",
  "schema:identifier": "https://doi.org/10.1234/geochem-archive-2025",
  "schema:url": "https://example.org/datasets/geochem-archive-2025",
  "schema:dateModified": "2025-08-01",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "ex:metadata_archive_001",
    "schema:about": {
      "@id": "ex:dataset_archive_001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/manifest/1.1"
      }
    ]
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "schema:Collection"
      ],
      "schema:name": "Geochemistry results archive",
      "schema:contentUrl": "https://example.org/downloads/geochem-results-2025.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "https://w3id.org/cdif/manifest/1.1"
        }
      ],
      "schema:hasPart": [
        {
          "@id": "#data-csv",
          "@type": [
            "schema:MediaObject"
          ],
          "schema:name": "results.csv",
          "schema:description": "Tabular geochemical analysis results",
          "schema:encodingFormat": [
            "text/csv"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 245000,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "sha256",
            "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
          }
        },
        {
          "@id": "#metadata-json",
          "@type": [
            "schema:MediaObject"
          ],
          "schema:name": "metadata.json",
          "schema:description": "Metadata sidecar for the results file",
          "schema:encodingFormat": [
            "application/json"
          ],
          "schema:about": [
            {
              "@id": "#data-csv"
            }
          ]
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/#metadata-json> a schema1:MediaObject ;
    schema1:about <file:///github/workspace/#data-csv> ;
    schema1:description "Metadata sidecar for the results file" ;
    schema1:encodingFormat "application/json" ;
    schema1:name "metadata.json" .

ex:dataset_archive_001 a schema1:Dataset ;
    schema1:dateModified "2025-08-01" ;
    schema1:distribution [ a schema1:Collection,
                schema1:DataDownload ;
            dcterms:conformsTo <https://w3id.org/cdif/manifest/1.1> ;
            schema1:contentUrl "https://example.org/downloads/geochem-results-2025.zip" ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart <file:///github/workspace/#data-csv>,
                <file:///github/workspace/#metadata-json> ;
            schema1:name "Geochemistry results archive" ] ;
    schema1:identifier "https://doi.org/10.1234/geochem-archive-2025" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:name "Geochemical Analysis Results Package" ;
    schema1:subjectOf ex:metadata_archive_001 ;
    schema1:url "https://example.org/datasets/geochem-archive-2025" .

ex:metadata_archive_001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/manifest/1.1> ;
    schema1:about ex:dataset_archive_001 ;
    schema1:additionalType dcat:CatalogRecord .

<file:///github/workspace/#data-csv> a schema1:MediaObject ;
    schema1:description "Tabular geochemical analysis results" ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "results.csv" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 245000 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "sha256" ;
            spdx:checksumValue "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Manifest
description: "Profile module for packages: the resources that make up a dataset and
  where to retrieve each of them. Marks the catalog record as conformant to the CDIF
  manifest spec (https://w3id.org/cdif/manifest/1.1) and declares schema:hasPart in
  the two places a package needs it \u2014 on the Dataset, for parts that are independently
  accessible at their own addresses, and on a schema:distribution item, for component
  files inside an archive (ZIP, etc.) that have no address of their own. Both part
  shapes carry schema:about, so a part that describes another \u2014 a codebook, a
  data dictionary, a metadata sidecar \u2014 can say which one. The base schema:distribution
  anyOf [DataDownload, WebAPI] contributed by cdifCore is preserved \u2014 this BB
  only adds property constraints, no new anyOf branch. (Merged from the previous cdifProfile/cdifArchive
  BB, which held only the $defs for ArchivePart; everything now lives here.)"
type: object
properties:
  schema:subjectOf:
    properties:
      dcterms:conformsTo:
        type: array
        items:
          type: object
          required:
          - '@id'
          additionalProperties: false
          properties:
            '@id':
              type: string
              description: uri for specifications that this metadata record conforms
                to
        minItems: 1
        contains:
          type: object
          required:
          - '@id'
          additionalProperties: false
          properties:
            '@id':
              const: https://w3id.org/cdif/manifest/1.1
  schema:hasPart:
    $ref: '#/$defs/resourcePartArray'
    description: Component resources of a package whose parts are independently accessible,
      each with its own distribution. Parts may differ in content type, format and
      data structure. For component files inside an archive, which have no address
      of their own, use schema:hasPart on the distribution instead.
  schema:distribution:
    type: array
    items:
      allOf:
      - properties:
          schema:hasPart:
            $ref: '#/$defs/archivePartArray'
            description: For bundle/archive distributions (positively typed with schema:Collection
              in @type), describes the component files. Each component is typed as
              schema:MediaObject and may include CDIF data description extensions
              (cdifTabularData, cdifDataCube) to describe its internal structure.
      - if:
          properties:
            '@type':
              type: array
              contains:
                const: schema:Collection
          required:
          - '@type'
        then:
          required:
          - schema:hasPart
$defs:
  resourcePartArray:
    type: array
    description: Array of the resources that make up a package. Each part is independently
      retrievable, so unlike an archive part it may carry its own schema:distribution
      and may be typed schema:DataDownload.
    items:
      $ref: '#/$defs/resourcePartItem'
  resourcePartItem:
    type: object
    description: 'One independently accessible member of a package. Type it for what
      it is: schema:Dataset for data, schema:CreativeWork for a codebook, methods
      document or quality report, schema:MediaObject for a browse image. Parts under
      separate stewardship should carry their own schema:provider, schema:conditionsOfAccess
      and schema:dateModified, since those are what differ.'
    properties:
      '@id':
        type: string
        description: Identifier for this part.
      '@type':
        type: array
        description: What kind of resource this part is. Must include schema:CreativeWork
          or one of its subclasses -- everything a package can contain is a creative
          work of some kind, and saying which one is what lets a consumer tell the
          data from the codebook from the browse image. Additional types beyond that
          are free, so domain vocabularies (ada:otherFileType and the like) sit alongside.
          Not constrained to schema:MediaObject as an archive part is, because a part
          with its own address may well be a Dataset or a DataDownload.
        items:
          type: string
        minItems: 1
        contains:
          type: string
          pattern: ^(schema:|http://schema\.org/)(CreativeWork|Dataset|DataDownload|DataCatalog|MediaObject|ImageObject|VideoObject|AudioObject|3DModel|DigitalDocument|TextDigitalDocument|SpreadsheetDigitalDocument|PresentationDigitalDocument|NoteDigitalDocument|SoftwareApplication|WebApplication|SoftwareSourceCode|Article|ScholarlyArticle|TechArticle|Report|Book|Chapter|Thesis|Manuscript|Map|WebPage|WebSite|Collection|Course|HowTo|Guide|Legislation|Photograph|Painting|Drawing|Poster|Atlas|Periodical|PublicationIssue|PublicationVolume|CreativeWorkSeries|Review|Comment)$
      schema:name:
        type: string
      schema:description:
        type: string
      schema:encodingFormat:
        type: array
        items:
          type: string
      schema:url:
        type: string
      schema:about:
        type: array
        description: The part this one is about. Use it on a part that describes another
          -- a codebook, a data dictionary, a quality report, a metadata sidecar --
          so that a consumer can tell WHICH part it documents rather than only that
          both are in the package. Equivalent in this use to cito:documents, which
          is how OAI-ORE packages express the same relationship; schema:subjectOf
          is the declared inverse.
        items:
          type: object
          required:
          - '@id'
          additionalProperties: false
          properties:
            '@id':
              type: string
              description: Reference to the @id of the part being described.
  archivePartArray:
    type: array
    description: Array describing the files contained in the archive. Each item represents
      a component file that is part of the archive and is not independently accessible.
    items:
      $ref: '#/$defs/archivePartItem'
  archivePartItem:
    allOf:
    - type: object
      properties:
        '@id':
          type: string
          description: Identifier for this file, typically a hash-based anchor (e.g.
            '#abc123'). Used for cross-references from schema:about in metadata sidecar
            files.
        '@type':
          type: array
          description: Must include schema:MediaObject. Must NOT include schema:DataDownload
            since this file is not independently accessible. May include additional
            types for categorization.
          items:
            type: string
          contains:
            const: schema:MediaObject
          not:
            contains:
              const: schema:DataDownload
          minItems: 1
        schema:name:
          type: string
          description: Filename of the component file within the archive.
        schema:description:
          type: string
          description: Description of the file content. May include checksum information.
        schema:encodingFormat:
          type: array
          description: MIME type(s) for this file.
          items:
            type: string
        schema:size:
          type: object
          description: File size as a QuantitativeValue.
          properties:
            '@type':
              type: array
              items:
                type: string
              contains:
                const: schema:QuantitativeValue
              minItems: 1
            schema:value:
              type: number
              description: Numeric size value.
            schema:unitText:
              type: string
              description: Unit of measure for size (e.g. 'byte').
        schema:about:
          type: array
          description: For metadata sidecar files, references the data file this metadata
            describes.
          items:
            type: object
            required:
            - '@id'
            additionalProperties: false
            properties:
              '@id':
                type: string
                description: Reference to the @id of the data file described by this
                  sidecar.
        spdx:checksum:
          type: object
          description: Checksum for integrity verification of this component file.
          properties:
            '@type':
              type: array
              items:
                type: string
              contains:
                const: spdx:Checksum
              minItems: 1
            spdx:algorithm:
              type: string
            spdx:checksumValue:
              type: string
          required:
          - '@type'
      required:
      - '@type'
      - schema:name
      - schema:encodingFormat
    - anyOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataCube/schema.yaml
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifTabularData/schema.yaml
      - {}

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifManifest/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifManifest/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifManifest/context.jsonld)

## Sources

* [schema.org DataDownload](https://schema.org/DataDownload)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifProfile/cdifManifest`

