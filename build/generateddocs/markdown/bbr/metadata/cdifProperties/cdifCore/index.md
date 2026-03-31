
# CDIF Core metadata (Schema)

`cdif.bbr.metadata.cdifProperties.cdifCore` *v0.1*

Core properties for CDIF metadata, applicable to any resource type. Required properties: @id, @type, schema:name, schema:identifier, schema:dateModified, schema:conditionsOfAccess or schema:license, schema:url or schema:distribution, schema:subjectOf. Optional core properties: schema:description, schema:additionalType, schema:sameAs, schema:version, schema:inLanguage, schema:datePublished, schema:relatedLink, schema:publishingPrinciples, schema:keywords, schema:creator, schema:contributor, schema:publisher, schema:provider, schema:funding, prov:wasGeneratedBy, prov:wasDerivedFrom. Uses building blocks: labeledLink, identifier, definedTerm, dataDownload, webAPI, person, organization, agentInRole, funder, generatedBy, derivedFrom, cdifCatalogRecord.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Core Metadata Properties

Defines the core properties for any CDIF metadata record, implementing the schema.org-based [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) metadata model.

### Required properties
- `@id`, `@type`, `@context` (JSON-LD structural)
- `schema:name` -- descriptive name for the resource
- `schema:identifier` -- primary identifier (string or PropertyValue)
- `schema:dateModified` -- last update date (ISO 8601)
- `schema:license` or `schema:conditionsOfAccess` -- access/use terms
- `schema:url` or `schema:distribution` -- how to obtain the resource
- `schema:subjectOf` -- metadata catalog record with `dcterms:conformsTo`

### Optional core properties
- `schema:description` -- summary text
- `schema:additionalType` -- non-schema.org type identifiers
- `schema:sameAs` -- alternate identifiers
- `schema:version` -- version number/string
- `schema:inLanguage` -- content language
- `schema:datePublished` -- publication date
- `schema:relatedLink` -- typed links to related resources
- `schema:publishingPrinciples` -- maintenance/persistence policies
- `schema:keywords` -- subject keywords (strings or DefinedTerms)
- `schema:creator` -- authors (ordered `@list`)
- `schema:contributor` -- other contributing parties (with roles via agentInRole)
- `schema:publisher` -- publishing party
- `schema:provider` -- distribution provider
- `schema:funding` -- funding sources
- `prov:wasGeneratedBy` -- provenance: how the resource was created
- `prov:wasDerivedFrom` -- provenance: source datasets

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
        "@id": "https://w3id.org/cdif/core/1.0"
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
        "@id": "https://w3id.org/cdif/core/1.0"
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
        <https://w3id.org/cdif/core/1.0> ;
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


### Example CDIF core, Minimal required.
Simplest valid CDIF core instance with only required properties.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:coreMin23578",
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
      "@id": "ex:coreMin23578"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
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
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCore/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:coreMin23578",
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
      "@id": "ex:coreMin23578"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:URIforMetadata3575 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0> ;
    schema1:about ex:coreMin23578 ;
    schema1:additionalType "dcat:CatalogRecord" .

ex:coreMin23578 a schema1:Dataset ;
    schema1:dateModified "2022-12-12" ;
    schema1:identifier "https://doi.org/23566/aslry" ;
    schema1:license "https://creativecommons.org/publicdomain/zero/1.0/" ;
    schema1:name "Bathymetry Bay of Biscay" ;
    schema1:subjectOf ex:URIforMetadata3575 ;
    schema1:url "https://example.org/landingPage254266" .


```


### Example CDIF core, All properties.
CDIF core instance exercising every property allowed by the cdifCore schema.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#"
  },
  "@id": "ex:completeCoreDataset99001",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Global Ocean Temperature Profiles 2010-2024",
  "schema:description": "Quality-controlled temperature profiles from Argo floats deployed worldwide. Profiles extend from the surface to 2000m depth with 2dbar vertical resolution.",
  "schema:identifier": {
    "@id": "ex:datasetIdentifier001",
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.5281/zenodo.99001",
    "schema:url": "https://doi.org/10.5281/zenodo.99001"
  },
  "schema:additionalType": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Observational Data",
      "schema:identifier": "https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords/EARTH_SCIENCE/OCEANS/OCEAN_TEMPERATURE",
      "schema:inDefinedTermSet": "https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords",
      "schema:termCode": "EARTH SCIENCE > OCEANS > OCEAN TEMPERATURE"
    }
  ],
  "schema:sameAs": [
    "https://doi.org/10.5281/zenodo.99001",
    {
      "@id": "https://n2t.net/ark:/99999/fk4ocean2024"
    }
  ],
  "schema:version": "3.2",
  "schema:inLanguage": "en",
  "schema:dateModified": "2024-11-15",
  "schema:datePublished": "2024-01-10",
  "schema:url": "https://example.org/datasets/ocean-temp-profiles",
  "schema:conditionsOfAccess": [
    "Free access after registration",
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Data Access Terms",
      "schema:url": "https://example.org/terms/data-access-v2"
    }
  ],
  "schema:license": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "NetCDF download",
      "schema:description": "Complete dataset in CF-compliant NetCDF4 format",
      "schema:contentUrl": "https://example.org/data/ocean-temp-profiles.nc",
      "schema:encodingFormat": [
        "application/x-netcdf"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "checksumAlgorithm_sha256",
        "spdx:checksumValue": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2"
      },
      "dcterms:conformsTo": [
        {
          "@id": "https://www.unidata.ucar.edu/software/netcdf/"
        }
      ],
      "schema:provider": [
        {
          "@id": "https://ror.org/04t3en479",
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Ocean Data Repository"
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "CSV download",
      "schema:contentUrl": "https://example.org/data/ocean-temp-profiles.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "https://www.ietf.org/rfc/rfc4180"
        }
      ]
    }
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "documentation",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:name": "User Guide",
        "schema:url": "https://example.org/docs/ocean-temp-guide.pdf",
        "schema:encodingFormat": "application/pdf"
      }
    }
  ],
  "schema:publishingPrinciples": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Data Retention and Update Policy",
      "schema:url": "https://example.org/policies/data-retention"
    }
  ],
  "schema:keywords": [
    "ocean temperature",
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Argo",
      "schema:identifier": "https://vocab.nerc.ac.uk/collection/L06/current/46/",
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L06/current/",
      "schema:termCode": "L06:46"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Sea water temperature",
      "schema:identifier": "https://vocab.nerc.ac.uk/collection/P01/current/TEMPPR01/",
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/P01/current/",
      "schema:termCode": "TEMPPR01"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://orcid.org/0000-0001-2345-6789",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Marchand, Jean-Pierre",
        "schema:alternateName": "JP Marchand",
        "schema:description": "Principal investigator for ocean observation program",
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Institut Océanographique",
          "schema:url": "https://example.org/io"
        },
        "schema:identifier": {
          "@id": "ex:marchandOrcid",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
          "schema:value": "0000-0001-2345-6789",
          "schema:url": "https://orcid.org/0000-0001-2345-6789"
        },
        "schema:sameAs": [
          "https://orcid.org/0000-0001-2345-6789"
        ],
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "jp.marchand@ocean-inst.org"
        }
      },
      {
        "@id": "https://ror.org/04t3en479",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "Ocean Data Repository",
        "schema:alternateName": "ODR",
        "schema:description": "International consortium for ocean data management",
        "schema:identifier": {
          "@id": "ex:odrRor",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://registry.identifiers.org/registry/ror",
          "schema:value": "04t3en479",
          "schema:url": "https://ror.org/04t3en479"
        },
        "schema:additionalType": [
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "Research Infrastructure",
            "schema:identifier": "https://example.org/org-types/RI",
            "schema:inDefinedTermSet": "https://example.org/org-types",
            "schema:termCode": "RI"
          }
        ],
        "schema:sameAs": [
          "https://ror.org/04t3en479"
        ],
        "schema:url": "https://example.org/odr",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "info@ocean-data-repo.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "data quality reviewer",
      "schema:contributor": {
        "@id": "https://orcid.org/0000-0002-9876-5432",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Li, Wei",
        "schema:identifier": {
          "@id": "ex:liOrcid",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
          "schema:value": "0000-0002-9876-5432",
          "schema:url": "https://orcid.org/0000-0002-9876-5432"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "wei.li@ocean-research.org"
        }
      }
    }
  ],
  "schema:publisher": {
    "@id": "https://ror.org/04t3en479",
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Ocean Data Repository"
  },
  "schema:provider": [
    {
      "@id": "https://ror.org/04t3en479"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Global Ocean Observations Initiative",
      "schema:identifier": {
        "@id": "ex:grantId001",
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://example.org/grant-registry",
        "schema:value": "GOO-2020-0042"
      },
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "European Research Council",
        "schema:identifier": {
          "@id": "ex:ercRor",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://registry.identifiers.org/registry/ror",
          "schema:value": "0472cxd90",
          "schema:url": "https://ror.org/0472cxd90"
        }
      }
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity"
      ],
      "prov:used": [
        {
          "@id": "ex:argoFloatNetwork"
        }
      ]
    }
  ],
  "prov:wasDerivedFrom": [
    {
      "@id": "ex:argoRawProfiles",
      "@type": [
        "schema:Dataset"
      ],
      "schema:name": "Argo Raw Profile Database",
      "schema:url": "https://example.org/argo-raw"
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:metadataRecord99001",
    "schema:about": {
      "@id": "ex:completeCoreDataset99001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore"
      },
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      }
    ],
    "schema:maintainer": {
      "@id": "https://orcid.org/0000-0003-1111-2222",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Dubois, Marie",
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "m.dubois@ocean-data-repo.org"
      }
    },
    "schema:sdDatePublished": "2024-11-20",
    "schema:includedInDataCatalog": {
      "@id": "https://example.org/catalog/ocean-data",
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "Global Ocean Data Catalog",
      "schema:url": "https://example.org/catalog/ocean-data",
      "schema:identifier": {
        "@id": "ex:oceanCatalogId",
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://example.org/catalog-registry",
        "schema:value": "ocean-data-catalog-001"
      }
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
      "dcterms": "http://purl.org/dc/terms/",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCore/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#"
    }
  ],
  "@id": "ex:completeCoreDataset99001",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Global Ocean Temperature Profiles 2010-2024",
  "schema:description": "Quality-controlled temperature profiles from Argo floats deployed worldwide. Profiles extend from the surface to 2000m depth with 2dbar vertical resolution.",
  "schema:identifier": {
    "@id": "ex:datasetIdentifier001",
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.5281/zenodo.99001",
    "schema:url": "https://doi.org/10.5281/zenodo.99001"
  },
  "schema:additionalType": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Observational Data",
      "schema:identifier": "https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords/EARTH_SCIENCE/OCEANS/OCEAN_TEMPERATURE",
      "schema:inDefinedTermSet": "https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords",
      "schema:termCode": "EARTH SCIENCE > OCEANS > OCEAN TEMPERATURE"
    }
  ],
  "schema:sameAs": [
    "https://doi.org/10.5281/zenodo.99001",
    {
      "@id": "https://n2t.net/ark:/99999/fk4ocean2024"
    }
  ],
  "schema:version": "3.2",
  "schema:inLanguage": "en",
  "schema:dateModified": "2024-11-15",
  "schema:datePublished": "2024-01-10",
  "schema:url": "https://example.org/datasets/ocean-temp-profiles",
  "schema:conditionsOfAccess": [
    "Free access after registration",
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Data Access Terms",
      "schema:url": "https://example.org/terms/data-access-v2"
    }
  ],
  "schema:license": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "NetCDF download",
      "schema:description": "Complete dataset in CF-compliant NetCDF4 format",
      "schema:contentUrl": "https://example.org/data/ocean-temp-profiles.nc",
      "schema:encodingFormat": [
        "application/x-netcdf"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "checksumAlgorithm_sha256",
        "spdx:checksumValue": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2"
      },
      "dcterms:conformsTo": [
        {
          "@id": "https://www.unidata.ucar.edu/software/netcdf/"
        }
      ],
      "schema:provider": [
        {
          "@id": "https://ror.org/04t3en479",
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Ocean Data Repository"
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "CSV download",
      "schema:contentUrl": "https://example.org/data/ocean-temp-profiles.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "https://www.ietf.org/rfc/rfc4180"
        }
      ]
    }
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "documentation",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:name": "User Guide",
        "schema:url": "https://example.org/docs/ocean-temp-guide.pdf",
        "schema:encodingFormat": "application/pdf"
      }
    }
  ],
  "schema:publishingPrinciples": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Data Retention and Update Policy",
      "schema:url": "https://example.org/policies/data-retention"
    }
  ],
  "schema:keywords": [
    "ocean temperature",
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Argo",
      "schema:identifier": "https://vocab.nerc.ac.uk/collection/L06/current/46/",
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L06/current/",
      "schema:termCode": "L06:46"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Sea water temperature",
      "schema:identifier": "https://vocab.nerc.ac.uk/collection/P01/current/TEMPPR01/",
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/P01/current/",
      "schema:termCode": "TEMPPR01"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://orcid.org/0000-0001-2345-6789",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Marchand, Jean-Pierre",
        "schema:alternateName": "JP Marchand",
        "schema:description": "Principal investigator for ocean observation program",
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Institut Oc\u00e9anographique",
          "schema:url": "https://example.org/io"
        },
        "schema:identifier": {
          "@id": "ex:marchandOrcid",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
          "schema:value": "0000-0001-2345-6789",
          "schema:url": "https://orcid.org/0000-0001-2345-6789"
        },
        "schema:sameAs": [
          "https://orcid.org/0000-0001-2345-6789"
        ],
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "jp.marchand@ocean-inst.org"
        }
      },
      {
        "@id": "https://ror.org/04t3en479",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "Ocean Data Repository",
        "schema:alternateName": "ODR",
        "schema:description": "International consortium for ocean data management",
        "schema:identifier": {
          "@id": "ex:odrRor",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://registry.identifiers.org/registry/ror",
          "schema:value": "04t3en479",
          "schema:url": "https://ror.org/04t3en479"
        },
        "schema:additionalType": [
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "Research Infrastructure",
            "schema:identifier": "https://example.org/org-types/RI",
            "schema:inDefinedTermSet": "https://example.org/org-types",
            "schema:termCode": "RI"
          }
        ],
        "schema:sameAs": [
          "https://ror.org/04t3en479"
        ],
        "schema:url": "https://example.org/odr",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "info@ocean-data-repo.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "data quality reviewer",
      "schema:contributor": {
        "@id": "https://orcid.org/0000-0002-9876-5432",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Li, Wei",
        "schema:identifier": {
          "@id": "ex:liOrcid",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
          "schema:value": "0000-0002-9876-5432",
          "schema:url": "https://orcid.org/0000-0002-9876-5432"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "wei.li@ocean-research.org"
        }
      }
    }
  ],
  "schema:publisher": {
    "@id": "https://ror.org/04t3en479",
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Ocean Data Repository"
  },
  "schema:provider": [
    {
      "@id": "https://ror.org/04t3en479"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Global Ocean Observations Initiative",
      "schema:identifier": {
        "@id": "ex:grantId001",
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://example.org/grant-registry",
        "schema:value": "GOO-2020-0042"
      },
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "European Research Council",
        "schema:identifier": {
          "@id": "ex:ercRor",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://registry.identifiers.org/registry/ror",
          "schema:value": "0472cxd90",
          "schema:url": "https://ror.org/0472cxd90"
        }
      }
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity"
      ],
      "prov:used": [
        {
          "@id": "ex:argoFloatNetwork"
        }
      ]
    }
  ],
  "prov:wasDerivedFrom": [
    {
      "@id": "ex:argoRawProfiles",
      "@type": [
        "schema:Dataset"
      ],
      "schema:name": "Argo Raw Profile Database",
      "schema:url": "https://example.org/argo-raw"
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:metadataRecord99001",
    "schema:about": {
      "@id": "ex:completeCoreDataset99001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore"
      },
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      }
    ],
    "schema:maintainer": {
      "@id": "https://orcid.org/0000-0003-1111-2222",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Dubois, Marie",
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "m.dubois@ocean-data-repo.org"
      }
    },
    "schema:sdDatePublished": "2024-11-20",
    "schema:includedInDataCatalog": {
      "@id": "https://example.org/catalog/ocean-data",
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "Global Ocean Data Catalog",
      "schema:url": "https://example.org/catalog/ocean-data",
      "schema:identifier": {
        "@id": "ex:oceanCatalogId",
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://example.org/catalog-registry",
        "schema:value": "ocean-data-catalog-001"
      }
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .

ex:argoRawProfiles a schema1:Dataset ;
    schema1:name "Argo Raw Profile Database" ;
    schema1:url "https://example.org/argo-raw" .

<https://example.org/catalog/ocean-data> a schema1:DataCatalog ;
    schema1:identifier ex:oceanCatalogId ;
    schema1:name "Global Ocean Data Catalog" ;
    schema1:url "https://example.org/catalog/ocean-data" .

ex:completeCoreDataset99001 a schema1:Dataset ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:identifier "https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords/EARTH_SCIENCE/OCEANS/OCEAN_TEMPERATURE" ;
            schema1:inDefinedTermSet "https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords" ;
            schema1:name "Observational Data" ;
            schema1:termCode "EARTH SCIENCE > OCEANS > OCEAN TEMPERATURE" ] ;
    schema1:conditionsOfAccess [ a schema1:CreativeWork ;
            schema1:name "Data Access Terms" ;
            schema1:url "https://example.org/terms/data-access-v2" ],
        "Free access after registration" ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor <https://orcid.org/0000-0002-9876-5432> ;
            schema1:roleName "data quality reviewer" ] ;
    schema1:creator ( <https://orcid.org/0000-0001-2345-6789> <https://ror.org/04t3en479> ) ;
    schema1:dateModified "2024-11-15" ;
    schema1:datePublished "2024-01-10" ;
    schema1:description "Quality-controlled temperature profiles from Argo floats deployed worldwide. Profiles extend from the surface to 2000m depth with 2dbar vertical resolution." ;
    schema1:distribution [ a schema1:DataDownload ;
            dcterms:conformsTo <https://www.unidata.ucar.edu/software/netcdf/> ;
            schema1:contentUrl "https://example.org/data/ocean-temp-profiles.nc" ;
            schema1:description "Complete dataset in CF-compliant NetCDF4 format" ;
            schema1:encodingFormat "application/x-netcdf" ;
            schema1:name "NetCDF download" ;
            schema1:provider <https://ror.org/04t3en479> ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "checksumAlgorithm_sha256" ;
                    spdx:checksumValue "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2" ] ],
        [ a schema1:DataDownload ;
            dcterms:conformsTo <https://www.ietf.org/rfc/rfc4180> ;
            schema1:contentUrl "https://example.org/data/ocean-temp-profiles.csv" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "CSV download" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:funder [ a schema1:Organization ;
                    schema1:identifier ex:ercRor ;
                    schema1:name "European Research Council" ] ;
            schema1:identifier ex:grantId001 ;
            schema1:name "Global Ocean Observations Initiative" ] ;
    schema1:identifier ex:datasetIdentifier001 ;
    schema1:inLanguage "en" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier "https://vocab.nerc.ac.uk/collection/L06/current/46/" ;
            schema1:inDefinedTermSet "https://vocab.nerc.ac.uk/collection/L06/current/" ;
            schema1:name "Argo" ;
            schema1:termCode "L06:46" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "https://vocab.nerc.ac.uk/collection/P01/current/TEMPPR01/" ;
            schema1:inDefinedTermSet "https://vocab.nerc.ac.uk/collection/P01/current/" ;
            schema1:name "Sea water temperature" ;
            schema1:termCode "TEMPPR01" ],
        "ocean temperature" ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Creative Commons Attribution 4.0" ;
            schema1:url "https://creativecommons.org/licenses/by/4.0/" ] ;
    schema1:name "Global Ocean Temperature Profiles 2010-2024" ;
    schema1:provider <https://ror.org/04t3en479> ;
    schema1:publisher <https://ror.org/04t3en479> ;
    schema1:publishingPrinciples [ a schema1:CreativeWork ;
            schema1:name "Data Retention and Update Policy" ;
            schema1:url "https://example.org/policies/data-retention" ] ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "documentation" ;
            schema1:target [ a schema1:EntryPoint ;
                    schema1:encodingFormat "application/pdf" ;
                    schema1:name "User Guide" ;
                    schema1:url "https://example.org/docs/ocean-temp-guide.pdf" ] ] ;
    schema1:sameAs <https://n2t.net/ark:/99999/fk4ocean2024>,
        "https://doi.org/10.5281/zenodo.99001" ;
    schema1:subjectOf ex:metadataRecord99001 ;
    schema1:url "https://example.org/datasets/ocean-temp-profiles" ;
    schema1:version "3.2" ;
    prov:wasDerivedFrom ex:argoRawProfiles ;
    prov:wasGeneratedBy [ a prov:Activity ;
            prov:used ex:argoFloatNetwork ] .

ex:datasetIdentifier001 a schema1:PropertyValue ;
    schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
    schema1:url "https://doi.org/10.5281/zenodo.99001" ;
    schema1:value "10.5281/zenodo.99001" .

ex:ercRor a schema1:PropertyValue ;
    schema1:propertyID "https://registry.identifiers.org/registry/ror" ;
    schema1:url "https://ror.org/0472cxd90" ;
    schema1:value "0472cxd90" .

ex:grantId001 a schema1:PropertyValue ;
    schema1:propertyID "https://example.org/grant-registry" ;
    schema1:value "GOO-2020-0042" .

ex:liOrcid a schema1:PropertyValue ;
    schema1:propertyID "https://registry.identifiers.org/registry/orcid" ;
    schema1:url "https://orcid.org/0000-0002-9876-5432" ;
    schema1:value "0000-0002-9876-5432" .

ex:marchandOrcid a schema1:PropertyValue ;
    schema1:propertyID "https://registry.identifiers.org/registry/orcid" ;
    schema1:url "https://orcid.org/0000-0001-2345-6789" ;
    schema1:value "0000-0001-2345-6789" .

ex:metadataRecord99001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore>,
        <https://w3id.org/cdif/core/1.0> ;
    schema1:about ex:completeCoreDataset99001 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:includedInDataCatalog <https://example.org/catalog/ocean-data> ;
    schema1:maintainer <https://orcid.org/0000-0003-1111-2222> ;
    schema1:sdDatePublished "2024-11-20" .

ex:oceanCatalogId a schema1:PropertyValue ;
    schema1:propertyID "https://example.org/catalog-registry" ;
    schema1:value "ocean-data-catalog-001" .

ex:odrRor a schema1:PropertyValue ;
    schema1:propertyID "https://registry.identifiers.org/registry/ror" ;
    schema1:url "https://ror.org/04t3en479" ;
    schema1:value "04t3en479" .

<https://orcid.org/0000-0001-2345-6789> a schema1:Person ;
    schema1:affiliation [ a schema1:Organization ;
            schema1:name "Institut Océanographique" ;
            schema1:url "https://example.org/io" ] ;
    schema1:alternateName "JP Marchand" ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "jp.marchand@ocean-inst.org" ] ;
    schema1:description "Principal investigator for ocean observation program" ;
    schema1:identifier ex:marchandOrcid ;
    schema1:name "Marchand, Jean-Pierre" ;
    schema1:sameAs "https://orcid.org/0000-0001-2345-6789" .

<https://orcid.org/0000-0002-9876-5432> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "wei.li@ocean-research.org" ] ;
    schema1:identifier ex:liOrcid ;
    schema1:name "Li, Wei" .

<https://orcid.org/0000-0003-1111-2222> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "m.dubois@ocean-data-repo.org" ] ;
    schema1:name "Dubois, Marie" .

<https://ror.org/04t3en479> a schema1:Organization ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:identifier "https://example.org/org-types/RI" ;
            schema1:inDefinedTermSet "https://example.org/org-types" ;
            schema1:name "Research Infrastructure" ;
            schema1:termCode "RI" ] ;
    schema1:alternateName "ODR" ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "info@ocean-data-repo.org" ] ;
    schema1:description "International consortium for ocean data management" ;
    schema1:identifier ex:odrRor ;
    schema1:name "Ocean Data Repository" ;
    schema1:sameAs "https://ror.org/04t3en479" ;
    schema1:url "https://example.org/odr" .


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
                const: https://w3id.org/cdif/core/1.0
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

