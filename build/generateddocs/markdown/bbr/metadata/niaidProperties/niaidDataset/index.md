
# NIAID dataset properties (Schema)

`cdif.bbr.metadata.niaidProperties.niaidDataset` *v1.0*

The properties NIAID Data Discovery Portal records add to a CDIF dataset, layered on cdifCore by the cdifNIAID profile: NIAID's nde: terms (species, topic category, portal date, ClinicalTrials.gov id, curator, samples, related resources) and cdifniaid: terms for names the portal uses that neither NIAID's schema nor Bioschemas declares. NIAID's additions to terms, grants, cited works, places and catalogs are in type-bound blocks it uses. Requires schema:includedInDataCatalog and a cdifNIAID conformsTo claim. Uses building blocks: niaidDefinedTerm, niaidMonetaryGrant, niaidCreativeWork, niaidPlace, niaidDataCatalog (niaidProperties), bioschemasSample (bioschemasProperties), objectReference (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## NIAID dataset properties

The properties that dataset records from the
[NIAID Data Discovery Portal](https://data.niaid.nih.gov/) add to a CDIF dataset.
The [`cdifNIAID`](../../profiles/cdifCompositeProfile/cdifNIAID/) profile
composes this module with `cdifCore`; it does not re-embed `cdifCore`.
`converters/NIAID/harvest_niaid_to_cdif.py` produces records in this form, driven
by `converters/mappings/niaid-to-cdif.sssom.tsv`.

### Namespaces

| Prefix | IRI | Used for |
|---|---|---|
| `nde:` | `https://discovery.biothings.io/ns/nde/` | Terms NIAID's [schema](https://github.com/NIAID-Data-Ecosystem/nde-schemas) declares |
| `bios:` | `https://bioschemas.org/` | Bioschemas terms with the same definition, from [`bioschemasSample`](../../bioschemasProperties/bioschemasSample/) |
| `cdifniaid:` | `https://w3id.org/cdif/niaid/terms/` | Names the portal uses that neither declares, defined below |

The `cdifniaid:` IRIs do not resolve yet; like other `cdif:` terms they are
defined here and nowhere else. They sit under `terms/` so that the profile URI
`https://w3id.org/cdif/niaid/1.0` is never compacted to a `cdifniaid:` CURIE.

### What the module requires

- `schema:includedInDataCatalog`: the repositories the portal aggregates the
  record from.
- A `dcterms:conformsTo` of `https://w3id.org/cdif/niaid/1.0` on the catalog
  record.

Everything else is optional but typed. Every property accepts one value or an
array, because framing collapses a one-element array to its value.

### NIAID Blueprint completeness

The [NIAID Blueprint for Digital Objects](https://doi.org/10.5281/zenodo.17161561) (v2, 26 September 2025) asks for 17 elements on
every dataset. `rules.shacl` checks the record's root dataset for each of them with an
`sh:Warning`, so a record reports what it lacks against the Blueprint without failing
the profile. The Blueprint's host is `nde:species`, and its funder and grant are
`schema:funding`.

### Extensions of other types

NIAID adds properties to five other types, each in a block that requires the
type. `niaidDataset` points its properties at them.

| Block | Type | NIAID properties | Used for |
|---|---|---|---|
| [`niaidDefinedTerm`](../niaidDefinedTerm/) | `schema:DefinedTerm` | `nde:isCurated`, `nde:originalName`, `nde:curatedBy`, `cdifniaid:commonName` | `nde:species`, `schema:infectiousAgent`, `schema:healthCondition`; `schema:keywords`, `schema:measurementTechnique` and `schema:variableMeasured` items that carry an annotation |
| [`niaidMonetaryGrant`](../niaidMonetaryGrant/) | `schema:MonetaryGrant` | `cdifniaid:projectNumSplit` | `schema:funding` |
| [`niaidCreativeWork`](../niaidCreativeWork/) | `schema:CreativeWork` or `schema:ScholarlyArticle` | `nde:pmid`, `nde:doi`, `nde:journalName`, `nde:journalNameAbbrev` | `schema:citation` and `nde:citedBy` items that carry one of them |
| [`niaidPlace`](../niaidPlace/) | `schema:Place` | `nde:administrativeType` | `schema:spatialCoverage` |
| [`niaidDataCatalog`](../niaidDataCatalog/) | `schema:DataCatalog` | `nde:versionDate`, `schema:archivedAt` | `schema:includedInDataCatalog` |

### NIAID terms on the dataset

| Property | On | Value |
|---|---|---|
| `nde:date` | dataset | The portal's summary date |
| `nde:species` | dataset, sample | Host organisms, e.g. Homo sapiens, as NIAID defined terms; the pathogen is in `schema:infectiousAgent` |
| `nde:nctid` | dataset | ClinicalTrials.gov id, `NCT` and eight digits |
| `nde:citedBy` | dataset | Works citing the dataset |
| `nde:curatedBy` | dataset | The repository that curated the record, with `nde:versionDate` |
| `nde:isBasisFor` | dataset | Related resources, with `nde:relationship` |
| `nde:sample` | dataset | An `nde:Sample` or `nde:SampleCollection` |
| `nde:cellType`, `nde:associatedGenotype` | sample | Term or text |

### cdifniaid terms on the dataset

| Term | On | Definition |
|---|---|---|
| `cdifniaid:correctionApproved` | source organization | A correction to the portal's record of the project was approved |
| `cdifniaid:assayformat` | dataset | The assay format, as the portal gives it |
| `cdifniaid:publication` | dataset | PubMed ids of publications about the dataset |

The portal's `from*` flags (`fromGPT`, `fromPMID`, `fromEXTRACT`, `fromNCT`) are
not properties here: the converter turns them into one sentence each, "Metadata
source from GPT." and so on, on the catalog record's description. A person's
`role` becomes a `schema:contributor` that is a `schema:Role` holding the person,
CDIF's pattern for roles.

NIAID's `isRelatedTo` is not a property here either: each related resource is a
`schema:relatedLink` LinkRole with `schema:linkRelationship` "related to", its
address as target, and the portal's relationship in the LinkRole's description.
A temporal interval with more than dates (a name, a temporalType, a text
duration) is a `schema:temporalCoverage` interval with calendar-date bounds,
whose description gives those as `nde:name: ...; nde:temporalType: ...`.

## Examples

### A NIAID Data Discovery Portal record in CDIF.
A real record from the NIAID Data Discovery Portal API (index build 2026-10-28),
converted by converters/NIAID/harvest_niaid_to_cdif.py.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "nde": "https://discovery.biothings.io/ns/nde/",
    "bios": "https://bioschemas.org/",
    "time": "http://www.w3.org/2006/time#",
    "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
  },
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=pxd027351",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=pxd027351"
    },
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record pxd027351, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.\n\nMetadata source from PMID.\n\nMetadata source from GPT.",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=pxd027351#metadata",
    "schema:name": "Metadata record for: Online Nanoflow Two-Dimension Comprehensive Active Modulation Reversed Phase-Reversed Phase Liquid Chromatography High R",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.identifiers.org/registry/doi"
    },
    "schema:value": "10.6019/PXD027351",
    "schema:url": "https://doi.org/10.6019/PXD027351"
  },
  "bios:alternateIdentifier": [
    "PXD027351"
  ],
  "schema:dateModified": "2022-05-20",
  "schema:datePublished": "2022-05-20",
  "schema:dateCreated": "2021-07-16",
  "nde:date": "2022-05-20",
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Woods Hole Oceanographic Inst."
        },
        "schema:identifier": "https://orcid.org/0000-0002-5301-8365",
        "schema:name": "Matthew McIlvin"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Marine Chemistry and Geochemistry, Woods Hole Oceanographic Institution, Unites States"
        },
        "schema:name": "Mak Saito"
      }
    ]
  },
  "schema:citation": [
    {
      "@type": [
        "schema:ScholarlyArticle"
      ],
      "schema:author": [
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "McIlvin MR"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Saito MA"
        }
      ],
      "schema:datePublished": "2021-09-03",
      "schema:identifier": "PMID:34384028",
      "nde:journalName": "Journal of proteome research",
      "schema:name": "Online Nanoflow Two-Dimension Comprehensive Active Modulation Reversed Phase-Reversed Phase Liquid Chromatography High-Resolution Mass Spectrometry for Metaproteomics of Environmental and Microbiome Samples.",
      "nde:pmid": "34384028",
      "schema:url": "https://pubmed.ncbi.nlm.nih.gov/34384028/"
    }
  ],
  "schema:conditionsOfAccess": [
    "Open"
  ],
  "schema:description": "Metaproteomics is a powerful analytical approach that can assess the functional capabilities deployed by microbial communi-ties in both environmental and biomedical microbiome settings. Yet the mass spectra resulting from these mixed biological communities are challenging due to the high number of low intensity peak features. The use of multiple dimensions of chroma-tographic separation prior to mass spectrometry analyses has been applied to proteomics previously but can require increased sampling handling and instrument time. Here we demonstrate an automated online comprehensive active-modulation two-dimensional liquid chromatography method for metaproteome sample analysis. A high pH PLRP-S column was used in the first dimension followed by low pH separation in the second dimension using dual modulating C18 traps and a C18 column. This method increased the number of unique peptides found in ocean metaproteome samples by more than 50% when com-pared to a one dimension separation while using the same amount of sample and instrument time.",
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "https://www.omicsdi.org/ws/dataset/pride/PXD027351",
      "schema:encodingFormat": [
        "XML"
      ]
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:endDate": "2024-04-30",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "NIGMS",
          "U.S. National Institute of General Medical Sciences"
        ],
        "schema:identifier": "https://ror.org/04q48ey07",
        "schema:name": "National Institute of General Medical Sciences",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "1R01GM135709-01A1"
      },
      "schema:name": "Response of the Bacterial Metalloproteome to Environmental Conditions",
      "cdifniaid:projectNumSplit": {
        "cdifniaid:activityCode": "R01",
        "cdifniaid:applTypeCode": "1",
        "cdifniaid:fullSupportYear": "01A1",
        "cdifniaid:icCode": "GM",
        "cdifniaid:serialNum": "135709",
        "cdifniaid:suffixCode": "A1",
        "cdifniaid:supportYear": "01"
      },
      "schema:startDate": "2020-06-10",
      "schema:url": "https://reporter.nih.gov/project-details/10052790"
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Disease-free",
        "Disease Free"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2024-11-30",
        "schema:name": "Biothings API",
        "schema:url": "https://biothings.io/"
      },
      "schema:identifier": "C173158",
      "schema:inDefinedTermSet": "NCIT",
      "nde:isCurated": true,
      "schema:name": "Disease Free",
      "nde:originalName": "disease-free",
      "schema:url": "http://purl.obolibrary.org/obo/NCIT_C173158"
    }
  ],
  "schema:includedInDataCatalog": [
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:archivedAt": "https://www.omicsdi.org/dataset/pride/PXD027351",
      "schema:name": "Omics Discovery Index (OmicsDI)",
      "schema:url": "https://www.omicsdi.org/",
      "nde:versionDate": "2026-10-23"
    },
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:archivedAt": "http://www.ebi.ac.uk/pride/archive/projects/PXD027351",
      "schema:name": "ProteomeXchange",
      "schema:url": "https://www.proteomexchange.org/",
      "nde:versionDate": "2026-10-01"
    }
  ],
  "schema:infectiousAgent": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "uncultured marine plankton"
      ],
      "schema:identifier": "632957",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": false,
      "schema:name": "marine plankton environmental sample",
      "nde:originalName": "Marine Plankton Environmental Sample",
      "schema:url": "https://www.uniprot.org/taxonomy/632957"
    }
  ],
  "schema:keywords": [
    "",
    "Metaproteomics",
    "Lcms",
    "Proteomics",
    "Automated",
    "Rprp",
    "Lc",
    "2dlc",
    "Comprehensive active modulation",
    "Ocean",
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_3370",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Analytical chemistry",
      "schema:url": "http://edamontology.org/topic_3370",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_0121",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Proteomics",
      "schema:url": "http://edamontology.org/topic_0121",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_3174",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Metagenomics",
      "schema:url": "http://edamontology.org/topic_3174",
      "schema:about": "topicCategory"
    },
    {
      "schema:name": "infectiousAgent",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    },
    {
      "schema:name": "host",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:license": [
    "https://www.proteomexchange.org/pxcollaborativeagreement_2024.pdf"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0000534",
      "schema:inDefinedTermSet": "MMO",
      "nde:isCurated": true,
      "schema:name": "mass spectrometry",
      "nde:originalName": "Mass Spectrometry",
      "schema:url": "http://purl.obolibrary.org/obo/MMO_0000534"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0000470",
      "schema:inDefinedTermSet": "OBI",
      "nde:isCurated": true,
      "schema:name": "mass spectrometry assay",
      "nde:originalName": "Mass Spectrometry",
      "schema:url": "http://purl.obolibrary.org/obo/OBI_0000470"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0000428",
      "schema:inDefinedTermSet": "PRIDE",
      "nde:isCurated": true,
      "schema:name": "Bottom-up proteomics",
      "nde:originalName": "Shotgun proteomics",
      "schema:url": "http://purl.obolibrary.org/obo/PRIDE_0000428"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0003229",
      "schema:inDefinedTermSet": "OBI",
      "nde:isCurated": true,
      "schema:name": "plasma proteomics assay",
      "nde:originalName": "Shotgun proteomics",
      "schema:url": "http://purl.obolibrary.org/obo/OBI_0003229"
    }
  ],
  "schema:name": "Online Nanoflow Two-Dimension Comprehensive Active Modulation Reversed Phase-Reversed Phase Liquid Chromatography High Resolution Mass Spectrometry for Metaproteomics of Environmen-tal and Microbiome Samples",
  "schema:sameAs": [
    "https://www.ebi.ac.uk/pride/archive/projects/PXD027351"
  ],
  "nde:sample": {
    "@type": [
      "nde:Sample",
      "bios:Sample"
    ],
    "schema:instrument": [
      {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Orbitrap Fusion"
      }
    ]
  },
  "schema:sdPublisher": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Pride",
    "schema:url": "https://www.omicsdi.org/dataset/pride/PXD027351"
  },
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Homo sapients",
        "human",
        "Homo sapiens Linnaeus, 1758",
        "Homo sapians",
        "Homo sapien",
        "Homo sapian",
        "Homo spaiens",
        "Human",
        "Homo sapines",
        "Home sapiens",
        "Homo sapience",
        "Homo spiens",
        "Homo sapeins",
        "Homo sapiense",
        "Humo sapiens",
        "Homo sampiens"
      ],
      "cdifniaid:commonName": "Human",
      "schema:identifier": "9606",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": false,
      "schema:name": "Homo sapiens",
      "nde:originalName": "Homo Sapiens (human)",
      "schema:url": "https://www.uniprot.org/taxonomy/9606"
    }
  ],
  "schema:url": "https://www.omicsdi.org/dataset/pride/PXD027351",
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "nde:usageInfo",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:url": "https://www.proteomexchange.org/docs/reprocessed_guidelines_px.pdf"
      }
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Proteomics",
      "@type": [
        "schema:PropertyValue"
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
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataset/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "time": "http://www.w3.org/2006/time#",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=pxd027351",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=pxd027351"
    },
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record pxd027351, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.\n\nMetadata source from PMID.\n\nMetadata source from GPT.",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=pxd027351#metadata",
    "schema:name": "Metadata record for: Online Nanoflow Two-Dimension Comprehensive Active Modulation Reversed Phase-Reversed Phase Liquid Chromatography High R",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.identifiers.org/registry/doi"
    },
    "schema:value": "10.6019/PXD027351",
    "schema:url": "https://doi.org/10.6019/PXD027351"
  },
  "bios:alternateIdentifier": [
    "PXD027351"
  ],
  "schema:dateModified": "2022-05-20",
  "schema:datePublished": "2022-05-20",
  "schema:dateCreated": "2021-07-16",
  "nde:date": "2022-05-20",
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Woods Hole Oceanographic Inst."
        },
        "schema:identifier": "https://orcid.org/0000-0002-5301-8365",
        "schema:name": "Matthew McIlvin"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Marine Chemistry and Geochemistry, Woods Hole Oceanographic Institution, Unites States"
        },
        "schema:name": "Mak Saito"
      }
    ]
  },
  "schema:citation": [
    {
      "@type": [
        "schema:ScholarlyArticle"
      ],
      "schema:author": [
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "McIlvin MR"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Saito MA"
        }
      ],
      "schema:datePublished": "2021-09-03",
      "schema:identifier": "PMID:34384028",
      "nde:journalName": "Journal of proteome research",
      "schema:name": "Online Nanoflow Two-Dimension Comprehensive Active Modulation Reversed Phase-Reversed Phase Liquid Chromatography High-Resolution Mass Spectrometry for Metaproteomics of Environmental and Microbiome Samples.",
      "nde:pmid": "34384028",
      "schema:url": "https://pubmed.ncbi.nlm.nih.gov/34384028/"
    }
  ],
  "schema:conditionsOfAccess": [
    "Open"
  ],
  "schema:description": "Metaproteomics is a powerful analytical approach that can assess the functional capabilities deployed by microbial communi-ties in both environmental and biomedical microbiome settings. Yet the mass spectra resulting from these mixed biological communities are challenging due to the high number of low intensity peak features. The use of multiple dimensions of chroma-tographic separation prior to mass spectrometry analyses has been applied to proteomics previously but can require increased sampling handling and instrument time. Here we demonstrate an automated online comprehensive active-modulation two-dimensional liquid chromatography method for metaproteome sample analysis. A high pH PLRP-S column was used in the first dimension followed by low pH separation in the second dimension using dual modulating C18 traps and a C18 column. This method increased the number of unique peptides found in ocean metaproteome samples by more than 50% when com-pared to a one dimension separation while using the same amount of sample and instrument time.",
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "https://www.omicsdi.org/ws/dataset/pride/PXD027351",
      "schema:encodingFormat": [
        "XML"
      ]
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:endDate": "2024-04-30",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "NIGMS",
          "U.S. National Institute of General Medical Sciences"
        ],
        "schema:identifier": "https://ror.org/04q48ey07",
        "schema:name": "National Institute of General Medical Sciences",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "1R01GM135709-01A1"
      },
      "schema:name": "Response of the Bacterial Metalloproteome to Environmental Conditions",
      "cdifniaid:projectNumSplit": {
        "cdifniaid:activityCode": "R01",
        "cdifniaid:applTypeCode": "1",
        "cdifniaid:fullSupportYear": "01A1",
        "cdifniaid:icCode": "GM",
        "cdifniaid:serialNum": "135709",
        "cdifniaid:suffixCode": "A1",
        "cdifniaid:supportYear": "01"
      },
      "schema:startDate": "2020-06-10",
      "schema:url": "https://reporter.nih.gov/project-details/10052790"
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Disease-free",
        "Disease Free"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2024-11-30",
        "schema:name": "Biothings API",
        "schema:url": "https://biothings.io/"
      },
      "schema:identifier": "C173158",
      "schema:inDefinedTermSet": "NCIT",
      "nde:isCurated": true,
      "schema:name": "Disease Free",
      "nde:originalName": "disease-free",
      "schema:url": "http://purl.obolibrary.org/obo/NCIT_C173158"
    }
  ],
  "schema:includedInDataCatalog": [
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:archivedAt": "https://www.omicsdi.org/dataset/pride/PXD027351",
      "schema:name": "Omics Discovery Index (OmicsDI)",
      "schema:url": "https://www.omicsdi.org/",
      "nde:versionDate": "2026-10-23"
    },
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:archivedAt": "http://www.ebi.ac.uk/pride/archive/projects/PXD027351",
      "schema:name": "ProteomeXchange",
      "schema:url": "https://www.proteomexchange.org/",
      "nde:versionDate": "2026-10-01"
    }
  ],
  "schema:infectiousAgent": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "uncultured marine plankton"
      ],
      "schema:identifier": "632957",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": false,
      "schema:name": "marine plankton environmental sample",
      "nde:originalName": "Marine Plankton Environmental Sample",
      "schema:url": "https://www.uniprot.org/taxonomy/632957"
    }
  ],
  "schema:keywords": [
    "",
    "Metaproteomics",
    "Lcms",
    "Proteomics",
    "Automated",
    "Rprp",
    "Lc",
    "2dlc",
    "Comprehensive active modulation",
    "Ocean",
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_3370",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Analytical chemistry",
      "schema:url": "http://edamontology.org/topic_3370",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_0121",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Proteomics",
      "schema:url": "http://edamontology.org/topic_0121",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_3174",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Metagenomics",
      "schema:url": "http://edamontology.org/topic_3174",
      "schema:about": "topicCategory"
    },
    {
      "schema:name": "infectiousAgent",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    },
    {
      "schema:name": "host",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:license": [
    "https://www.proteomexchange.org/pxcollaborativeagreement_2024.pdf"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0000534",
      "schema:inDefinedTermSet": "MMO",
      "nde:isCurated": true,
      "schema:name": "mass spectrometry",
      "nde:originalName": "Mass Spectrometry",
      "schema:url": "http://purl.obolibrary.org/obo/MMO_0000534"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0000470",
      "schema:inDefinedTermSet": "OBI",
      "nde:isCurated": true,
      "schema:name": "mass spectrometry assay",
      "nde:originalName": "Mass Spectrometry",
      "schema:url": "http://purl.obolibrary.org/obo/OBI_0000470"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0000428",
      "schema:inDefinedTermSet": "PRIDE",
      "nde:isCurated": true,
      "schema:name": "Bottom-up proteomics",
      "nde:originalName": "Shotgun proteomics",
      "schema:url": "http://purl.obolibrary.org/obo/PRIDE_0000428"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0003229",
      "schema:inDefinedTermSet": "OBI",
      "nde:isCurated": true,
      "schema:name": "plasma proteomics assay",
      "nde:originalName": "Shotgun proteomics",
      "schema:url": "http://purl.obolibrary.org/obo/OBI_0003229"
    }
  ],
  "schema:name": "Online Nanoflow Two-Dimension Comprehensive Active Modulation Reversed Phase-Reversed Phase Liquid Chromatography High Resolution Mass Spectrometry for Metaproteomics of Environmen-tal and Microbiome Samples",
  "schema:sameAs": [
    "https://www.ebi.ac.uk/pride/archive/projects/PXD027351"
  ],
  "nde:sample": {
    "@type": [
      "nde:Sample",
      "bios:Sample"
    ],
    "schema:instrument": [
      {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Orbitrap Fusion"
      }
    ]
  },
  "schema:sdPublisher": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Pride",
    "schema:url": "https://www.omicsdi.org/dataset/pride/PXD027351"
  },
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Homo sapients",
        "human",
        "Homo sapiens Linnaeus, 1758",
        "Homo sapians",
        "Homo sapien",
        "Homo sapian",
        "Homo spaiens",
        "Human",
        "Homo sapines",
        "Home sapiens",
        "Homo sapience",
        "Homo spiens",
        "Homo sapeins",
        "Homo sapiense",
        "Humo sapiens",
        "Homo sampiens"
      ],
      "cdifniaid:commonName": "Human",
      "schema:identifier": "9606",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": false,
      "schema:name": "Homo sapiens",
      "nde:originalName": "Homo Sapiens (human)",
      "schema:url": "https://www.uniprot.org/taxonomy/9606"
    }
  ],
  "schema:url": "https://www.omicsdi.org/dataset/pride/PXD027351",
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "nde:usageInfo",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:url": "https://www.proteomexchange.org/docs/reprocessed_guidelines_px.pdf"
      }
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Proteomics",
      "@type": [
        "schema:PropertyValue"
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix bios: <https://bioschemas.org/> .
@prefix cdifniaid: <https://w3id.org/cdif/niaid/terms/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://data.niaid.nih.gov/resources?id=pxd027351> a schema1:Dataset ;
    schema1:citation [ a schema1:ScholarlyArticle ;
            schema1:author [ a schema1:Person ;
                    schema1:name "McIlvin MR" ],
                [ a schema1:Person ;
                    schema1:name "Saito MA" ] ;
            schema1:datePublished "2021-09-03" ;
            schema1:identifier "PMID:34384028" ;
            schema1:name "Online Nanoflow Two-Dimension Comprehensive Active Modulation Reversed Phase-Reversed Phase Liquid Chromatography High-Resolution Mass Spectrometry for Metaproteomics of Environmental and Microbiome Samples." ;
            schema1:url "https://pubmed.ncbi.nlm.nih.gov/34384028/" ;
            nde:journalName "Journal of proteome research" ;
            nde:pmid "34384028" ] ;
    schema1:conditionsOfAccess "Open" ;
    schema1:creator ( [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "Woods Hole Oceanographic Inst." ] ;
                schema1:identifier "https://orcid.org/0000-0002-5301-8365" ;
                schema1:name "Matthew McIlvin" ] [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "Marine Chemistry and Geochemistry, Woods Hole Oceanographic Institution, Unites States" ] ;
                schema1:name "Mak Saito" ] ) ;
    schema1:dateCreated "2021-07-16" ;
    schema1:dateModified "2022-05-20" ;
    schema1:datePublished "2022-05-20" ;
    schema1:description "Metaproteomics is a powerful analytical approach that can assess the functional capabilities deployed by microbial communi-ties in both environmental and biomedical microbiome settings. Yet the mass spectra resulting from these mixed biological communities are challenging due to the high number of low intensity peak features. The use of multiple dimensions of chroma-tographic separation prior to mass spectrometry analyses has been applied to proteomics previously but can require increased sampling handling and instrument time. Here we demonstrate an automated online comprehensive active-modulation two-dimensional liquid chromatography method for metaproteome sample analysis. A high pH PLRP-S column was used in the first dimension followed by low pH separation in the second dimension using dual modulating C18 traps and a C18 column. This method increased the number of unique peptides found in ocean metaproteome samples by more than 50% when com-pared to a one dimension separation while using the same amount of sample and instrument time." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://www.omicsdi.org/ws/dataset/pride/PXD027351" ;
            schema1:encodingFormat "XML" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:endDate "2024-04-30" ;
            schema1:funder [ a schema1:Organization ;
                    schema1:alternateName "NIGMS",
                        "U.S. National Institute of General Medical Sciences" ;
                    schema1:identifier "https://ror.org/04q48ey07" ;
                    schema1:name "National Institute of General Medical Sciences" ;
                    schema1:parentOrganization "National Institutes of Health" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:value "1R01GM135709-01A1" ] ;
            schema1:name "Response of the Bacterial Metalloproteome to Environmental Conditions" ;
            schema1:startDate "2020-06-10" ;
            schema1:url "https://reporter.nih.gov/project-details/10052790" ;
            cdifniaid:projectNumSplit [ cdifniaid:activityCode "R01" ;
                    cdifniaid:applTypeCode "1" ;
                    cdifniaid:fullSupportYear "01A1" ;
                    cdifniaid:icCode "GM" ;
                    cdifniaid:serialNum "135709" ;
                    cdifniaid:suffixCode "A1" ;
                    cdifniaid:supportYear "01" ] ] ;
    schema1:healthCondition [ a schema1:DefinedTerm ;
            schema1:alternateName "Disease Free",
                "Disease-free" ;
            schema1:identifier "C173158" ;
            schema1:inDefinedTermSet "NCIT" ;
            schema1:name "Disease Free" ;
            schema1:url "http://purl.obolibrary.org/obo/NCIT_C173158" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:dateModified "2024-11-30" ;
                    schema1:name "Biothings API" ;
                    schema1:url "https://biothings.io/" ] ;
            nde:isCurated true ;
            nde:originalName "disease-free" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID <https://registry.identifiers.org/registry/doi> ;
            schema1:url "https://doi.org/10.6019/PXD027351" ;
            schema1:value "10.6019/PXD027351" ] ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:archivedAt "http://www.ebi.ac.uk/pride/archive/projects/PXD027351" ;
            schema1:name "ProteomeXchange" ;
            schema1:url "https://www.proteomexchange.org/" ;
            nde:versionDate "2026-10-01" ],
        [ a schema1:DataCatalog ;
            schema1:archivedAt "https://www.omicsdi.org/dataset/pride/PXD027351" ;
            schema1:name "Omics Discovery Index (OmicsDI)" ;
            schema1:url "https://www.omicsdi.org/" ;
            nde:versionDate "2026-10-23" ] ;
    schema1:infectiousAgent [ a schema1:DefinedTerm ;
            schema1:alternateName "uncultured marine plankton" ;
            schema1:identifier "632957" ;
            schema1:inDefinedTermSet "UniProt" ;
            schema1:name "marine plankton environmental sample" ;
            schema1:url "https://www.uniprot.org/taxonomy/632957" ;
            nde:isCurated false ;
            nde:originalName "Marine Plankton Environmental Sample" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:about "topicCategory" ;
            schema1:identifier "topic_3174" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Metagenomics" ;
            schema1:url "http://edamontology.org/topic_3174" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:name "GPT-4o-mini" ;
                    schema1:url "https://openai.com/index/chatgpt" ] ],
        [ a schema1:DefinedTerm ;
            schema1:about "topicCategory" ;
            schema1:identifier "topic_3370" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Analytical chemistry" ;
            schema1:url "http://edamontology.org/topic_3370" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:name "GPT-4o-mini" ;
                    schema1:url "https://openai.com/index/chatgpt" ] ],
        [ a schema1:DefinedTerm ;
            schema1:about "NIAID classification" ;
            schema1:name "infectiousAgent" ],
        [ a schema1:DefinedTerm ;
            schema1:about "NIAID classification" ;
            schema1:name "host" ],
        [ a schema1:DefinedTerm ;
            schema1:about "topicCategory" ;
            schema1:identifier "topic_0121" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Proteomics" ;
            schema1:url "http://edamontology.org/topic_0121" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:name "GPT-4o-mini" ;
                    schema1:url "https://openai.com/index/chatgpt" ] ],
        "",
        "2dlc",
        "Automated",
        "Comprehensive active modulation",
        "Lc",
        "Lcms",
        "Metaproteomics",
        "Ocean",
        "Proteomics",
        "Rprp" ;
    schema1:license "https://www.proteomexchange.org/pxcollaborativeagreement_2024.pdf" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "0000534" ;
            schema1:inDefinedTermSet "MMO" ;
            schema1:name "mass spectrometry" ;
            schema1:url "http://purl.obolibrary.org/obo/MMO_0000534" ;
            nde:isCurated true ;
            nde:originalName "Mass Spectrometry" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "0000470" ;
            schema1:inDefinedTermSet "OBI" ;
            schema1:name "mass spectrometry assay" ;
            schema1:url "http://purl.obolibrary.org/obo/OBI_0000470" ;
            nde:isCurated true ;
            nde:originalName "Mass Spectrometry" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "0003229" ;
            schema1:inDefinedTermSet "OBI" ;
            schema1:name "plasma proteomics assay" ;
            schema1:url "http://purl.obolibrary.org/obo/OBI_0003229" ;
            nde:isCurated true ;
            nde:originalName "Shotgun proteomics" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "0000428" ;
            schema1:inDefinedTermSet "PRIDE" ;
            schema1:name "Bottom-up proteomics" ;
            schema1:url "http://purl.obolibrary.org/obo/PRIDE_0000428" ;
            nde:isCurated true ;
            nde:originalName "Shotgun proteomics" ] ;
    schema1:name "Online Nanoflow Two-Dimension Comprehensive Active Modulation Reversed Phase-Reversed Phase Liquid Chromatography High Resolution Mass Spectrometry for Metaproteomics of Environmen-tal and Microbiome Samples" ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "nde:usageInfo" ;
            schema1:target [ a schema1:EntryPoint ;
                    schema1:url "https://www.proteomexchange.org/docs/reprocessed_guidelines_px.pdf" ] ] ;
    schema1:sameAs "https://www.ebi.ac.uk/pride/archive/projects/PXD027351" ;
    schema1:sdPublisher [ a schema1:Organization ;
            schema1:name "Pride" ;
            schema1:url "https://www.omicsdi.org/dataset/pride/PXD027351" ] ;
    schema1:subjectOf <https://data.niaid.nih.gov/resources?id=pxd027351#metadata> ;
    schema1:url "https://www.omicsdi.org/dataset/pride/PXD027351" ;
    schema1:variableMeasured [ a schema1:PropertyValue ;
            schema1:name "Proteomics" ] ;
    bios:alternateIdentifier "PXD027351" ;
    nde:date "2022-05-20" ;
    nde:sample [ a bios:Sample,
                nde:Sample ;
            schema1:instrument [ a schema1:DefinedTerm ;
                    schema1:name "Orbitrap Fusion" ] ] ;
    nde:species [ a schema1:DefinedTerm ;
            schema1:alternateName "Home sapiens",
                "Homo sampiens",
                "Homo sapeins",
                "Homo sapian",
                "Homo sapians",
                "Homo sapien",
                "Homo sapience",
                "Homo sapiens Linnaeus, 1758",
                "Homo sapiense",
                "Homo sapients",
                "Homo sapines",
                "Homo spaiens",
                "Homo spiens",
                "Human",
                "Humo sapiens",
                "human" ;
            schema1:identifier "9606" ;
            schema1:inDefinedTermSet "UniProt" ;
            schema1:name "Homo sapiens" ;
            schema1:url "https://www.uniprot.org/taxonomy/9606" ;
            nde:isCurated false ;
            nde:originalName "Homo Sapiens (human)" ;
            cdifniaid:commonName "Human" ] .

<https://data.niaid.nih.gov/resources?id=pxd027351#metadata> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/discovery/1.1>,
        <https://w3id.org/cdif/niaid/1.0> ;
    schema1:about <https://data.niaid.nih.gov/resources?id=pxd027351> ;
    schema1:additionalType dcat:CatalogRecord ;
    schema1:description """CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record pxd027351, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.

Metadata source from PMID.

Metadata source from GPT.""" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "NIAID Data Discovery Portal" ;
            schema1:url "https://data.niaid.nih.gov/" ] ;
    schema1:name "Metadata record for: Online Nanoflow Two-Dimension Comprehensive Active Modulation Reversed Phase-Reversed Phase Liquid Chromatography High R" ;
    schema1:sdDatePublished "2026-10-28" .


```


### VDJServer record vdj_prjna272713
Record vdj_prjna272713 from VDJServer, as the NIAID Data Discovery Portal API returned it
(converters/NIAID/niaidExamples/vdj_prjna272713.json), converted by harvest_niaid_to_cdif.py.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "nde": "https://discovery.biothings.io/ns/nde/",
    "bios": "https://bioschemas.org/",
    "time": "http://www.w3.org/2006/time#",
    "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
  },
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=vdj_prjna272713",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=vdj_prjna272713"
    },
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record vdj_prjna272713, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.\n\nMetadata source from PMID.\n\nMetadata source from GPT.",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=vdj_prjna272713#metadata",
    "schema:name": "Metadata record for: Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.identifiers.org/registry/bioproject"
    },
    "schema:value": "PRJNA272713",
    "schema:url": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA272713"
  },
  "schema:dateModified": "2023-01-20",
  "schema:datePublished": "2020-08-17",
  "nde:date": "2023-01-20",
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Vaccine Research Center, National Institutes of Health, Bethesda, Maryland 20892, USA"
        },
        "schema:name": "Lawrence Shapiro"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "brandon.windsor@utsouthwestern.edu"
        },
        "schema:name": "Brandon Windsor"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Xueling Wu"
      }
    ]
  },
  "schema:citation": [
    {
      "@type": [
        "schema:ScholarlyArticle"
      ],
      "schema:author": [
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Wu X"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Zhang Z"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Schramm CA"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Joyce MG"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Kwon YD"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Zhou T"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Sheng Z"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Zhang B"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "O'Dell S"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "McKee K"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Georgiev IS"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Chuang GY"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Longo NS"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Lynch RM"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Saunders KO"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Soto C"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Srivatsan S"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Yang Y"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Bailer RT"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Louder MK"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Mullikin JC"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Connors M"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Kwong PD"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Mascola JR"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Shapiro L"
        },
        {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "NISC Comparative Sequencing Program"
        }
      ],
      "schema:datePublished": "2015-04-23",
      "schema:identifier": "PMID:25865483",
      "nde:journalName": "Cell",
      "schema:name": "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection.",
      "nde:pmid": "25865483",
      "schema:url": "https://pubmed.ncbi.nlm.nih.gov/25865483/"
    }
  ],
  "schema:conditionsOfAccess": [
    "Open",
    "AIRR Data Commons usage info: The software is under the GNU Affero General Public License, the data is Public Domain"
  ],
  "schema:description": "HIV-1-neutralizing antibodies develop in most HIV-1-infected individuals, although highly effective antibodies are generally observed only after years of chronic infection. Here, we characterize the rate of maturation and extent of diversity for the lineage that produced the broadly neutralizing antibody VRC01 through longitudinal sampling of peripheral B cell transcripts over 15 years and co-crystal structures of lineage members. Next-generation sequencing identified VRC01-lineage transcripts, which encompassed diverse antibodies organized into distinct phylogenetic clades. Prevalent clades maintained characteristic features of antigen recognition, though each evolved binding loops and disulfides that formed distinct recognition surfaces. Over the course of the study period, VRC01-lineage clades showed continuous evolution, with rates of ∼2 substitutions per 100 nucleotides per year, comparable to that of HIV-1 evolution. This high rate of antibody evolution provides a mechanism by which antibody lineages can achieve extraordinary diversity and, over years of chronic infection, develop effective HIV-1 neutralization.",
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767442_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767441_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767437_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767438_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767430_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767425_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767424_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767423_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767422_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767419_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767447_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767446_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767445_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767444_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767443_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767440_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767439_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767436_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767435_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767434_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767433_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767432_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767431_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767429_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767428_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767427_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767426_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767421_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767420_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767418_1.unique.igblast.airr.tsv.gz"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "National Institute of Allergy & Infectious Diseases",
          "NIAID",
          "Instituto Nacional de Alergias y Enfermedades Infecciosas"
        ],
        "schema:identifier": "https://ror.org/043z4tv69",
        "schema:name": "National Institute of Allergy and Infectious Diseases",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "1ZIAAI005022-08"
      },
      "schema:name": "Neutralization Mechanisms Of Anti-HIV-1 Monoclonal Antibodies",
      "schema:url": "https://reporter.nih.gov/project-details/7964824"
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:endDate": "2019-03-31",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "National Institute of Allergy & Infectious Diseases",
          "NIAID",
          "Instituto Nacional de Alergias y Enfermedades Infecciosas"
        ],
        "schema:employee": [
          {
            "@type": [
              "schema:Person"
            ],
            "schema:familyName": "SINGH",
            "schema:givenName": "ANJALI",
            "schema:name": "ANJALI SINGH"
          }
        ],
        "schema:identifier": "https://ror.org/043z4tv69",
        "schema:name": "National Institute of Allergy and Infectious Diseases",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "1P01AI104722-01A1"
      },
      "schema:name": "High Resolution Analysis of Env-directed B Cells to Accelerate Vaccine Design",
      "schema:startDate": "2014-04-01",
      "schema:url": "https://reporter.nih.gov/project-details/8680621"
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Human immunodeficiency virus disease or disorder",
        "Human immunodeficiency virus caused disease or disorder",
        "Human immunodeficiency virus infectious disease",
        "HIV infection"
      ],
      "schema:identifier": "0005109",
      "schema:inDefinedTermSet": "MONDO",
      "nde:isCurated": true,
      "schema:name": "HIV infectious disease",
      "nde:originalName": "human immunodeficiency virus infectious disease",
      "schema:url": "http://purl.obolibrary.org/obo/MONDO_0005109"
    }
  ],
  "schema:includedInDataCatalog": {
    "@type": [
      "schema:DataCatalog"
    ],
    "schema:archivedAt": "https://vdjserver.org/community?study_id=PRJNA272713",
    "schema:name": "VDJServer",
    "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713",
    "nde:versionDate": "2026-10-25"
  },
  "schema:infectiousAgent": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "AIDS virus",
        "HIV"
      ],
      "schema:identifier": "12721",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": false,
      "schema:name": "Human immunodeficiency virus",
      "schema:url": "https://www.uniprot.org/taxonomy/12721"
    }
  ],
  "schema:isAccessibleForFree": true,
  "schema:keywords": [
    "Chronic",
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_0804",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Immunology",
      "schema:url": "http://edamontology.org/topic_0804",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_3053",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Genetics",
      "schema:url": "http://edamontology.org/topic_3053",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_3299",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Evolutionary biology",
      "schema:url": "http://edamontology.org/topic_3299",
      "schema:about": "topicCategory"
    },
    {
      "schema:name": "infectiousAgent",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    },
    {
      "schema:name": "host",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:license": [
    "https://creativecommons.org/public-domain/"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0200082",
      "schema:inDefinedTermSet": "OBI",
      "nde:isCurated": true,
      "schema:name": "longitudinal data analysis",
      "nde:originalName": "Longitudinal Study",
      "schema:url": "http://purl.obolibrary.org/obo/OBI_0200082"
    }
  ],
  "schema:name": "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection",
  "nde:sample": {
    "@type": [
      "nde:SampleCollection"
    ],
    "schema:aggregateElement": {
      "@type": [
        "nde:Sample",
        "bios:Sample"
      ],
      "schema:additionalType": "ExperimentalRunSample",
      "bios:alternateIdentifier": [
        "788514286596919786-242ac116-0001-012",
        "SRR1767442",
        "812477722660105750-242ac116-0001-012",
        "803761420497719786-242ac116-0001-012",
        "SRR1767441",
        "794610658708745750-242ac116-0001-012",
        "819695749165879786-242ac116-0001-012",
        "SRR1767437",
        "775583953587465750-242ac116-0001-012",
        "834384537318199786-242ac116-0001-012",
        "SRR1767438",
        "758532933422345750-242ac116-0001-012",
        "896618613437239786-242ac116-0001-012",
        "SRR1767430",
        "741310114565385750-242ac116-0001-012",
        "909245817287479786-242ac116-0001-012",
        "SRR1767425",
        "659233289538825750-242ac116-0001-012",
        "928659069465399786-242ac116-0001-012",
        "SRR1767424",
        "644029105310985750-242ac116-0001-012",
        "943605555655479786-242ac116-0001-012",
        "SRR1767423",
        "627493481221385750-242ac116-0001-012",
        "962889958814519786-242ac116-0001-012",
        "SRR1767422",
        "612246347320585750-242ac116-0001-012",
        "980628173746999786-242ac116-0001-012",
        "SRR1767419",
        "595109427809545750-242ac116-0001-012",
        "1015503308190519786-242ac116-0001-012",
        "SRR1767447",
        "578402005028105750-242ac116-0001-012",
        "1092125524751159786-242ac116-0001-012",
        "SRR1767446",
        "497656619863305750-242ac116-0001-012",
        "1105053376312119786-242ac116-0001-012",
        "SRR1767445",
        "482967831710985750-242ac116-0001-012",
        "1118969070351159786-242ac116-0001-012",
        "SRR1767444",
        "460719901117705750-242ac116-0001-012",
        "1131811022566199786-242ac116-0001-012",
        "SRR1767443",
        "439373913656585750-242ac116-0001-012",
        "1146285062353719786-242ac116-0001-012",
        "SRR1767440",
        "422322893491465750-242ac116-0001-012",
        "1161789894292279786-242ac116-0001-012",
        "SRR1767439",
        "406861011225865750-242ac116-0001-012",
        "1176779330155319786-242ac116-0001-012",
        "SRR1767436",
        "386932362972425750-242ac116-0001-012",
        "1267875586503479786-242ac116-0001-012",
        "SRR1767435",
        "309751800663305750-242ac116-0001-012",
        "1281748330869559786-242ac116-0001-012",
        "SRR1767434",
        "279901777956105750-242ac116-0001-012",
        "1305886047073079786-242ac116-0001-012",
        "SRR1767433",
        "264482845363465750-242ac116-0001-012",
        "1322078073778999786-242ac116-0001-012",
        "SRR1767432",
        "165140251806985750-242ac116-0001-012",
        "1343982406988599786-242ac116-0001-012",
        "SRR1767431",
        "150451463654665750-242ac116-0001-012",
        "1360174433694519786-242ac116-0001-012",
        "SRR1767429",
        "125497703664905750-242ac116-0001-012",
        "1376022863016759786-242ac116-0001-012",
        "SRR1767428",
        "105783803776265750-242ac116-0001-012",
        "1391355896263479786-242ac116-0001-012",
        "SRR1767427",
        "89677676416265750-242ac116-0001-012",
        "1458615084118839786-242ac116-0001-012",
        "SRR1767426",
        "74258743823625750-242ac116-0001-012",
        "1471800633717559786-242ac116-0001-012",
        "SRR1767421",
        "59226358287625750-242ac116-0001-012",
        "1496110148612919786-242ac116-0001-012",
        "SRR1767420",
        "44193972751625750-242ac116-0001-012",
        "1513461816488759786-242ac116-0001-012",
        "SRR1767418",
        "43380410413879786-242ac116-0001-012"
      ],
      "bios:anatomicalStructure": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "UBERON:0000178",
          "schema:inDefinedTermSet": "UBERON",
          "schema:name": "blood"
        }
      ],
      "bios:collector": [
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "VACCINE RESEARCH CENTER"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "VACCINE RESEARCH CENTER"
        }
      ],
      "schema:conditionsOfAccess": "Open",
      "bios:developmentalStage": [
        {
          "@type": [
            "schema:QuantitativeValue"
          ],
          "schema:maxValue": 60,
          "schema:minValue": 45,
          "schema:unitCode": "UO:0000036",
          "schema:unitText": "year"
        }
      ],
      "schema:distribution": [
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767442_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767441_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767437_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767438_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767430_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767425_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767424_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767423_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767422_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767419_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767447_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767446_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767445_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767444_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767443_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767440_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767439_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767436_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767435_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767434_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767433_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767432_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767431_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767429_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767428_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767427_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767426_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767421_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767420_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767418_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        }
      ],
      "schema:healthCondition": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "HIV-1 positive"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "DOID:526",
          "schema:inDefinedTermSet": "DOID",
          "schema:name": "human immunodeficiency virus infectious disease"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "HIV-1 positive"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "DOID:526",
          "schema:inDefinedTermSet": "DOID",
          "schema:name": "human immunodeficiency virus infectious disease"
        }
      ],
      "schema:instrument": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "454 GS FLX+"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "454 GS FLX+"
        }
      ],
      "schema:isAccessibleForFree": true,
      "schema:license": "https://creativecommons.org/public-domain/",
      "schema:measurementTechnique": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "NCIT:C15273",
          "schema:inDefinedTermSet": "NCIT",
          "schema:name": "Longitudinal Study"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "PCR"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "NCIT:C15273",
          "schema:inDefinedTermSet": "NCIT",
          "schema:name": "Longitudinal Study"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "PCR"
        }
      ],
      "schema:name": [
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (788514286596919786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (803761420497719786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (819695749165879786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (834384537318199786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (896618613437239786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (909245817287479786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (928659069465399786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (943605555655479786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (962889958814519786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (980628173746999786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1015503308190519786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1092125524751159786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1105053376312119786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1118969070351159786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1131811022566199786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1146285062353719786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1161789894292279786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1176779330155319786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1267875586503479786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1281748330869559786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1305886047073079786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1322078073778999786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1343982406988599786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1360174433694519786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1376022863016759786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1391355896263479786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1458615084118839786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1471800633717559786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1496110148612919786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1513461816488759786-242ac116-0001-012)"
      ],
      "bios:sampleProcess": [
        "Single cell: False",
        "none",
        "Single cell: False",
        "none"
      ],
      "bios:sampleState": [
        "partial",
        "partial"
      ],
      "bios:sampleType": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "DNA"
        }
      ],
      "bios:sex": [
        "male"
      ],
      "nde:species": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "NCBITAXON:9606",
          "schema:inDefinedTermSet": "NCBITAXON",
          "schema:name": "Homo sapiens"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "NCBITAXON:9606",
          "schema:inDefinedTermSet": "NCBITAXON",
          "schema:name": "Homo sapiens"
        }
      ],
      "schema:temporalCoverage": [
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "08-19-2008"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "08-19-2008"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "01-17-2008"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "07-14-2006"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "07-30-2001"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "03-20-1995"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "12-31-2009"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "06-02-2009"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "07-12-2007"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "01-09-2007"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "04-16-2002"
        }
      ],
      "schema:usageInfo": {
        "@type": [
          "schema:Thing"
        ],
        "schema:description": "The software is under the GNU Affero General Public License, the data is Public Domain",
        "schema:name": "AIRR Data Commons usage info"
      },
      "schema:variableMeasured": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "C20971",
          "schema:inDefinedTermSet": "NCIT",
          "schema:name": "V(D)J Recombination",
          "schema:url": "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "data_2977",
          "schema:inDefinedTermSet": "EDAM",
          "schema:name": "Nucleic acid sequence",
          "schema:url": "https://edamontology.org/data_2977"
        },
        {
          "schema:description": "African American",
          "schema:name": "race"
        },
        {
          "schema:description": "Chronic",
          "schema:name": "disease severity"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:description": "African American",
          "schema:name": "race"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:description": "Chronic",
          "schema:name": "disease severity"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "IGH"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "C20971",
          "schema:inDefinedTermSet": "NCIT",
          "schema:name": "V(D)J Recombination",
          "schema:url": "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "data_2977",
          "schema:inDefinedTermSet": "EDAM",
          "schema:name": "Nucleic acid sequence",
          "schema:url": "https://edamontology.org/data_2977"
        },
        {
          "schema:description": "African American",
          "schema:name": "race"
        },
        {
          "schema:description": "Chronic",
          "schema:name": "disease severity"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:description": "African American",
          "schema:name": "race"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:description": "Chronic",
          "schema:name": "disease severity"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "IGH"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "IGK"
        }
      ]
    },
    "schema:itemListElement": [
      {
        "schema:identifier": "SRS823718",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823719",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823720",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823721",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823722",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823723",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823724",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823725",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823726",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823727",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823728",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823729",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823730",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823731",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823732",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823733",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823734",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823735",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823736",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823737",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823738",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823739",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823740",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823741",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823742",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823743",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823744",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823745",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823746",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823747",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      }
    ],
    "schema:numberOfItems": {
      "@type": [
        "schema:QuantitativeValue"
      ],
      "schema:unitText": "sample",
      "schema:value": 30
    }
  },
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Human",
        "Homo sapiens Linnaeus, 1758",
        "human",
        "Home sapiens",
        "Homo sampiens",
        "Homo sapeins",
        "Homo sapian",
        "Homo sapians",
        "Homo sapien",
        "Homo sapience",
        "Homo sapiense",
        "Homo sapients",
        "Homo sapines",
        "Homo spaiens",
        "Homo spiens",
        "Humo sapiens"
      ],
      "cdifniaid:commonName": "Human",
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2023-10-05",
        "schema:name": "PubTator",
        "schema:url": "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html"
      },
      "schema:identifier": "9606",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": true,
      "schema:name": "Homo sapiens",
      "nde:originalName": "homo sapiens",
      "schema:url": "https://www.uniprot.org/taxonomy/9606"
    }
  ],
  "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713",
  "schema:variableMeasured": [
    {
      "@type": [
        "schema:PropertyValue",
        "schema:DefinedTerm"
      ],
      "schema:identifier": "C20971",
      "schema:inDefinedTermSet": "NCIT",
      "schema:name": "V(D)J Recombination",
      "schema:url": "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971"
    },
    {
      "@type": [
        "schema:PropertyValue",
        "schema:DefinedTerm"
      ],
      "schema:identifier": "data_2977",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Nucleic acid sequence",
      "schema:url": "https://edamontology.org/data_2977"
    },
    {
      "schema:description": "African American",
      "schema:name": "race",
      "@type": [
        "schema:PropertyValue"
      ]
    },
    {
      "schema:description": "Chronic",
      "schema:name": "disease severity",
      "@type": [
        "schema:PropertyValue"
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
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataset/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "time": "http://www.w3.org/2006/time#",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=vdj_prjna272713",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=vdj_prjna272713"
    },
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record vdj_prjna272713, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.\n\nMetadata source from PMID.\n\nMetadata source from GPT.",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=vdj_prjna272713#metadata",
    "schema:name": "Metadata record for: Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.identifiers.org/registry/bioproject"
    },
    "schema:value": "PRJNA272713",
    "schema:url": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA272713"
  },
  "schema:dateModified": "2023-01-20",
  "schema:datePublished": "2020-08-17",
  "nde:date": "2023-01-20",
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Vaccine Research Center, National Institutes of Health, Bethesda, Maryland 20892, USA"
        },
        "schema:name": "Lawrence Shapiro"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "brandon.windsor@utsouthwestern.edu"
        },
        "schema:name": "Brandon Windsor"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Xueling Wu"
      }
    ]
  },
  "schema:citation": [
    {
      "@type": [
        "schema:ScholarlyArticle"
      ],
      "schema:author": [
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Wu X"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Zhang Z"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Schramm CA"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Joyce MG"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Kwon YD"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Zhou T"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Sheng Z"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Zhang B"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "O'Dell S"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "McKee K"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Georgiev IS"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Chuang GY"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Longo NS"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Lynch RM"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Saunders KO"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Soto C"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Srivatsan S"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Yang Y"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Bailer RT"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Louder MK"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Mullikin JC"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Connors M"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Kwong PD"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Mascola JR"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Shapiro L"
        },
        {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "NISC Comparative Sequencing Program"
        }
      ],
      "schema:datePublished": "2015-04-23",
      "schema:identifier": "PMID:25865483",
      "nde:journalName": "Cell",
      "schema:name": "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection.",
      "nde:pmid": "25865483",
      "schema:url": "https://pubmed.ncbi.nlm.nih.gov/25865483/"
    }
  ],
  "schema:conditionsOfAccess": [
    "Open",
    "AIRR Data Commons usage info: The software is under the GNU Affero General Public License, the data is Public Domain"
  ],
  "schema:description": "HIV-1-neutralizing antibodies develop in most HIV-1-infected individuals, although highly effective antibodies are generally observed only after years of chronic infection. Here, we characterize the rate of maturation and extent of diversity for the lineage that produced the broadly neutralizing antibody VRC01 through longitudinal sampling of peripheral B cell transcripts over 15 years and co-crystal structures of lineage members. Next-generation sequencing identified VRC01-lineage transcripts, which encompassed diverse antibodies organized into distinct phylogenetic clades. Prevalent clades maintained characteristic features of antigen recognition, though each evolved binding loops and disulfides that formed distinct recognition surfaces. Over the course of the study period, VRC01-lineage clades showed continuous evolution, with rates of \u223c2 substitutions per 100 nucleotides per year, comparable to that of HIV-1 evolution. This high rate of antibody evolution provides a mechanism by which antibody lineages can achieve extraordinary diversity and, over years of chronic infection, develop effective HIV-1 neutralization.",
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767442_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767441_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767437_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767438_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767430_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767425_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767424_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767423_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767422_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767419_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767447_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767446_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767445_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767444_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767443_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767440_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767439_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767436_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767435_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767434_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767433_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767432_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767431_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767429_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767428_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767427_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767426_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767421_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767420_1.unique.igblast.airr.tsv.gz"
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR1767418_1.unique.igblast.airr.tsv.gz"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "National Institute of Allergy & Infectious Diseases",
          "NIAID",
          "Instituto Nacional de Alergias y Enfermedades Infecciosas"
        ],
        "schema:identifier": "https://ror.org/043z4tv69",
        "schema:name": "National Institute of Allergy and Infectious Diseases",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "1ZIAAI005022-08"
      },
      "schema:name": "Neutralization Mechanisms Of Anti-HIV-1 Monoclonal Antibodies",
      "schema:url": "https://reporter.nih.gov/project-details/7964824"
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:endDate": "2019-03-31",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "National Institute of Allergy & Infectious Diseases",
          "NIAID",
          "Instituto Nacional de Alergias y Enfermedades Infecciosas"
        ],
        "schema:employee": [
          {
            "@type": [
              "schema:Person"
            ],
            "schema:familyName": "SINGH",
            "schema:givenName": "ANJALI",
            "schema:name": "ANJALI SINGH"
          }
        ],
        "schema:identifier": "https://ror.org/043z4tv69",
        "schema:name": "National Institute of Allergy and Infectious Diseases",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "1P01AI104722-01A1"
      },
      "schema:name": "High Resolution Analysis of Env-directed B Cells to Accelerate Vaccine Design",
      "schema:startDate": "2014-04-01",
      "schema:url": "https://reporter.nih.gov/project-details/8680621"
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Human immunodeficiency virus disease or disorder",
        "Human immunodeficiency virus caused disease or disorder",
        "Human immunodeficiency virus infectious disease",
        "HIV infection"
      ],
      "schema:identifier": "0005109",
      "schema:inDefinedTermSet": "MONDO",
      "nde:isCurated": true,
      "schema:name": "HIV infectious disease",
      "nde:originalName": "human immunodeficiency virus infectious disease",
      "schema:url": "http://purl.obolibrary.org/obo/MONDO_0005109"
    }
  ],
  "schema:includedInDataCatalog": {
    "@type": [
      "schema:DataCatalog"
    ],
    "schema:archivedAt": "https://vdjserver.org/community?study_id=PRJNA272713",
    "schema:name": "VDJServer",
    "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713",
    "nde:versionDate": "2026-10-25"
  },
  "schema:infectiousAgent": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "AIDS virus",
        "HIV"
      ],
      "schema:identifier": "12721",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": false,
      "schema:name": "Human immunodeficiency virus",
      "schema:url": "https://www.uniprot.org/taxonomy/12721"
    }
  ],
  "schema:isAccessibleForFree": true,
  "schema:keywords": [
    "Chronic",
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_0804",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Immunology",
      "schema:url": "http://edamontology.org/topic_0804",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_3053",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Genetics",
      "schema:url": "http://edamontology.org/topic_3053",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_3299",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Evolutionary biology",
      "schema:url": "http://edamontology.org/topic_3299",
      "schema:about": "topicCategory"
    },
    {
      "schema:name": "infectiousAgent",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    },
    {
      "schema:name": "host",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:license": [
    "https://creativecommons.org/public-domain/"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0200082",
      "schema:inDefinedTermSet": "OBI",
      "nde:isCurated": true,
      "schema:name": "longitudinal data analysis",
      "nde:originalName": "Longitudinal Study",
      "schema:url": "http://purl.obolibrary.org/obo/OBI_0200082"
    }
  ],
  "schema:name": "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection",
  "nde:sample": {
    "@type": [
      "nde:SampleCollection"
    ],
    "schema:aggregateElement": {
      "@type": [
        "nde:Sample",
        "bios:Sample"
      ],
      "schema:additionalType": "ExperimentalRunSample",
      "bios:alternateIdentifier": [
        "788514286596919786-242ac116-0001-012",
        "SRR1767442",
        "812477722660105750-242ac116-0001-012",
        "803761420497719786-242ac116-0001-012",
        "SRR1767441",
        "794610658708745750-242ac116-0001-012",
        "819695749165879786-242ac116-0001-012",
        "SRR1767437",
        "775583953587465750-242ac116-0001-012",
        "834384537318199786-242ac116-0001-012",
        "SRR1767438",
        "758532933422345750-242ac116-0001-012",
        "896618613437239786-242ac116-0001-012",
        "SRR1767430",
        "741310114565385750-242ac116-0001-012",
        "909245817287479786-242ac116-0001-012",
        "SRR1767425",
        "659233289538825750-242ac116-0001-012",
        "928659069465399786-242ac116-0001-012",
        "SRR1767424",
        "644029105310985750-242ac116-0001-012",
        "943605555655479786-242ac116-0001-012",
        "SRR1767423",
        "627493481221385750-242ac116-0001-012",
        "962889958814519786-242ac116-0001-012",
        "SRR1767422",
        "612246347320585750-242ac116-0001-012",
        "980628173746999786-242ac116-0001-012",
        "SRR1767419",
        "595109427809545750-242ac116-0001-012",
        "1015503308190519786-242ac116-0001-012",
        "SRR1767447",
        "578402005028105750-242ac116-0001-012",
        "1092125524751159786-242ac116-0001-012",
        "SRR1767446",
        "497656619863305750-242ac116-0001-012",
        "1105053376312119786-242ac116-0001-012",
        "SRR1767445",
        "482967831710985750-242ac116-0001-012",
        "1118969070351159786-242ac116-0001-012",
        "SRR1767444",
        "460719901117705750-242ac116-0001-012",
        "1131811022566199786-242ac116-0001-012",
        "SRR1767443",
        "439373913656585750-242ac116-0001-012",
        "1146285062353719786-242ac116-0001-012",
        "SRR1767440",
        "422322893491465750-242ac116-0001-012",
        "1161789894292279786-242ac116-0001-012",
        "SRR1767439",
        "406861011225865750-242ac116-0001-012",
        "1176779330155319786-242ac116-0001-012",
        "SRR1767436",
        "386932362972425750-242ac116-0001-012",
        "1267875586503479786-242ac116-0001-012",
        "SRR1767435",
        "309751800663305750-242ac116-0001-012",
        "1281748330869559786-242ac116-0001-012",
        "SRR1767434",
        "279901777956105750-242ac116-0001-012",
        "1305886047073079786-242ac116-0001-012",
        "SRR1767433",
        "264482845363465750-242ac116-0001-012",
        "1322078073778999786-242ac116-0001-012",
        "SRR1767432",
        "165140251806985750-242ac116-0001-012",
        "1343982406988599786-242ac116-0001-012",
        "SRR1767431",
        "150451463654665750-242ac116-0001-012",
        "1360174433694519786-242ac116-0001-012",
        "SRR1767429",
        "125497703664905750-242ac116-0001-012",
        "1376022863016759786-242ac116-0001-012",
        "SRR1767428",
        "105783803776265750-242ac116-0001-012",
        "1391355896263479786-242ac116-0001-012",
        "SRR1767427",
        "89677676416265750-242ac116-0001-012",
        "1458615084118839786-242ac116-0001-012",
        "SRR1767426",
        "74258743823625750-242ac116-0001-012",
        "1471800633717559786-242ac116-0001-012",
        "SRR1767421",
        "59226358287625750-242ac116-0001-012",
        "1496110148612919786-242ac116-0001-012",
        "SRR1767420",
        "44193972751625750-242ac116-0001-012",
        "1513461816488759786-242ac116-0001-012",
        "SRR1767418",
        "43380410413879786-242ac116-0001-012"
      ],
      "bios:anatomicalStructure": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "UBERON:0000178",
          "schema:inDefinedTermSet": "UBERON",
          "schema:name": "blood"
        }
      ],
      "bios:collector": [
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "VACCINE RESEARCH CENTER"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "VACCINE RESEARCH CENTER"
        }
      ],
      "schema:conditionsOfAccess": "Open",
      "bios:developmentalStage": [
        {
          "@type": [
            "schema:QuantitativeValue"
          ],
          "schema:maxValue": 60,
          "schema:minValue": 45,
          "schema:unitCode": "UO:0000036",
          "schema:unitText": "year"
        }
      ],
      "schema:distribution": [
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767442_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767441_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767437_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767438_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767430_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767425_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767424_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767423_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767422_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767419_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767447_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767446_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767445_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767444_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767443_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767440_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767439_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767436_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767435_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767434_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767433_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767432_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767431_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767429_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767428_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767427_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767426_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767421_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767420_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        },
        {
          "@type": [
            "schema:DataDownload"
          ],
          "schema:contentUrl": "SRR1767418_R1.fastq",
          "schema:description": "direction: forward",
          "schema:encodingFormat": [
            "fastq"
          ]
        }
      ],
      "schema:healthCondition": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "HIV-1 positive"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "DOID:526",
          "schema:inDefinedTermSet": "DOID",
          "schema:name": "human immunodeficiency virus infectious disease"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "HIV-1 positive"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "DOID:526",
          "schema:inDefinedTermSet": "DOID",
          "schema:name": "human immunodeficiency virus infectious disease"
        }
      ],
      "schema:instrument": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "454 GS FLX+"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "454 GS FLX+"
        }
      ],
      "schema:isAccessibleForFree": true,
      "schema:license": "https://creativecommons.org/public-domain/",
      "schema:measurementTechnique": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "NCIT:C15273",
          "schema:inDefinedTermSet": "NCIT",
          "schema:name": "Longitudinal Study"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "PCR"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "NCIT:C15273",
          "schema:inDefinedTermSet": "NCIT",
          "schema:name": "Longitudinal Study"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "PCR"
        }
      ],
      "schema:name": [
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (788514286596919786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (803761420497719786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (819695749165879786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (834384537318199786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (896618613437239786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (909245817287479786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (928659069465399786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (943605555655479786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (962889958814519786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (980628173746999786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1015503308190519786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1092125524751159786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1105053376312119786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1118969070351159786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1131811022566199786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1146285062353719786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1161789894292279786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1176779330155319786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1267875586503479786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1281748330869559786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1305886047073079786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1322078073778999786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1343982406988599786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1360174433694519786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1376022863016759786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1391355896263479786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1458615084118839786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1471800633717559786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1496110148612919786-242ac116-0001-012)",
        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1513461816488759786-242ac116-0001-012)"
      ],
      "bios:sampleProcess": [
        "Single cell: False",
        "none",
        "Single cell: False",
        "none"
      ],
      "bios:sampleState": [
        "partial",
        "partial"
      ],
      "bios:sampleType": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "DNA"
        }
      ],
      "bios:sex": [
        "male"
      ],
      "nde:species": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "NCBITAXON:9606",
          "schema:inDefinedTermSet": "NCBITAXON",
          "schema:name": "Homo sapiens"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "NCBITAXON:9606",
          "schema:inDefinedTermSet": "NCBITAXON",
          "schema:name": "Homo sapiens"
        }
      ],
      "schema:temporalCoverage": [
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "08-19-2008"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "08-19-2008"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "01-17-2008"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "07-14-2006"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "07-30-2001"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "03-20-1995"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "12-31-2009"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "06-02-2009"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "07-12-2007"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "01-09-2007"
        },
        {
          "@type": [
            "nde:TemporalInterval"
          ],
          "schema:name": "04-16-2002"
        }
      ],
      "schema:usageInfo": {
        "@type": [
          "schema:Thing"
        ],
        "schema:description": "The software is under the GNU Affero General Public License, the data is Public Domain",
        "schema:name": "AIRR Data Commons usage info"
      },
      "schema:variableMeasured": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "C20971",
          "schema:inDefinedTermSet": "NCIT",
          "schema:name": "V(D)J Recombination",
          "schema:url": "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "data_2977",
          "schema:inDefinedTermSet": "EDAM",
          "schema:name": "Nucleic acid sequence",
          "schema:url": "https://edamontology.org/data_2977"
        },
        {
          "schema:description": "African American",
          "schema:name": "race"
        },
        {
          "schema:description": "Chronic",
          "schema:name": "disease severity"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:description": "African American",
          "schema:name": "race"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:description": "Chronic",
          "schema:name": "disease severity"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "IGH"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "C20971",
          "schema:inDefinedTermSet": "NCIT",
          "schema:name": "V(D)J Recombination",
          "schema:url": "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:identifier": "data_2977",
          "schema:inDefinedTermSet": "EDAM",
          "schema:name": "Nucleic acid sequence",
          "schema:url": "https://edamontology.org/data_2977"
        },
        {
          "schema:description": "African American",
          "schema:name": "race"
        },
        {
          "schema:description": "Chronic",
          "schema:name": "disease severity"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:description": "African American",
          "schema:name": "race"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:description": "Chronic",
          "schema:name": "disease severity"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "IGH"
        },
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "IGK"
        }
      ]
    },
    "schema:itemListElement": [
      {
        "schema:identifier": "SRS823718",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823719",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823720",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823721",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823722",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823723",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823724",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823725",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823726",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823727",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823728",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823729",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823730",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823731",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823732",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823733",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823734",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823735",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823736",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823737",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823738",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823739",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823740",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823741",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823742",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823743",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823744",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823745",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823746",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      },
      {
        "schema:identifier": "SRS823747",
        "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713"
      }
    ],
    "schema:numberOfItems": {
      "@type": [
        "schema:QuantitativeValue"
      ],
      "schema:unitText": "sample",
      "schema:value": 30
    }
  },
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Human",
        "Homo sapiens Linnaeus, 1758",
        "human",
        "Home sapiens",
        "Homo sampiens",
        "Homo sapeins",
        "Homo sapian",
        "Homo sapians",
        "Homo sapien",
        "Homo sapience",
        "Homo sapiense",
        "Homo sapients",
        "Homo sapines",
        "Homo spaiens",
        "Homo spiens",
        "Humo sapiens"
      ],
      "cdifniaid:commonName": "Human",
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2023-10-05",
        "schema:name": "PubTator",
        "schema:url": "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html"
      },
      "schema:identifier": "9606",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": true,
      "schema:name": "Homo sapiens",
      "nde:originalName": "homo sapiens",
      "schema:url": "https://www.uniprot.org/taxonomy/9606"
    }
  ],
  "schema:url": "https://vdjserver.org/community?study_id=PRJNA272713",
  "schema:variableMeasured": [
    {
      "@type": [
        "schema:PropertyValue",
        "schema:DefinedTerm"
      ],
      "schema:identifier": "C20971",
      "schema:inDefinedTermSet": "NCIT",
      "schema:name": "V(D)J Recombination",
      "schema:url": "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971"
    },
    {
      "@type": [
        "schema:PropertyValue",
        "schema:DefinedTerm"
      ],
      "schema:identifier": "data_2977",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Nucleic acid sequence",
      "schema:url": "https://edamontology.org/data_2977"
    },
    {
      "schema:description": "African American",
      "schema:name": "race",
      "@type": [
        "schema:PropertyValue"
      ]
    },
    {
      "schema:description": "Chronic",
      "schema:name": "disease severity",
      "@type": [
        "schema:PropertyValue"
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix bios: <https://bioschemas.org/> .
@prefix cdifniaid: <https://w3id.org/cdif/niaid/terms/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://data.niaid.nih.gov/resources?id=vdj_prjna272713> a schema1:Dataset ;
    schema1:citation [ a schema1:ScholarlyArticle ;
            schema1:author [ a schema1:Person ;
                    schema1:name "Soto C" ],
                [ a schema1:Organization ;
                    schema1:name "NISC Comparative Sequencing Program" ],
                [ a schema1:Person ;
                    schema1:name "Chuang GY" ],
                [ a schema1:Person ;
                    schema1:name "Yang Y" ],
                [ a schema1:Person ;
                    schema1:name "Saunders KO" ],
                [ a schema1:Person ;
                    schema1:name "Schramm CA" ],
                [ a schema1:Person ;
                    schema1:name "Shapiro L" ],
                [ a schema1:Person ;
                    schema1:name "Joyce MG" ],
                [ a schema1:Person ;
                    schema1:name "Bailer RT" ],
                [ a schema1:Person ;
                    schema1:name "Zhou T" ],
                [ a schema1:Person ;
                    schema1:name "Longo NS" ],
                [ a schema1:Person ;
                    schema1:name "Sheng Z" ],
                [ a schema1:Person ;
                    schema1:name "Mullikin JC" ],
                [ a schema1:Person ;
                    schema1:name "McKee K" ],
                [ a schema1:Person ;
                    schema1:name "Srivatsan S" ],
                [ a schema1:Person ;
                    schema1:name "Kwong PD" ],
                [ a schema1:Person ;
                    schema1:name "Kwon YD" ],
                [ a schema1:Person ;
                    schema1:name "O'Dell S" ],
                [ a schema1:Person ;
                    schema1:name "Louder MK" ],
                [ a schema1:Person ;
                    schema1:name "Zhang B" ],
                [ a schema1:Person ;
                    schema1:name "Wu X" ],
                [ a schema1:Person ;
                    schema1:name "Zhang Z" ],
                [ a schema1:Person ;
                    schema1:name "Georgiev IS" ],
                [ a schema1:Person ;
                    schema1:name "Mascola JR" ],
                [ a schema1:Person ;
                    schema1:name "Lynch RM" ],
                [ a schema1:Person ;
                    schema1:name "Connors M" ] ;
            schema1:datePublished "2015-04-23" ;
            schema1:identifier "PMID:25865483" ;
            schema1:name "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection." ;
            schema1:url "https://pubmed.ncbi.nlm.nih.gov/25865483/" ;
            nde:journalName "Cell" ;
            nde:pmid "25865483" ] ;
    schema1:conditionsOfAccess "AIRR Data Commons usage info: The software is under the GNU Affero General Public License, the data is Public Domain",
        "Open" ;
    schema1:creator ( [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "Vaccine Research Center, National Institutes of Health, Bethesda, Maryland 20892, USA" ] ;
                schema1:name "Lawrence Shapiro" ] [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "brandon.windsor@utsouthwestern.edu" ] ;
                schema1:name "Brandon Windsor" ] [ a schema1:Person ;
                schema1:name "Xueling Wu" ] ) ;
    schema1:dateModified "2023-01-20" ;
    schema1:datePublished "2020-08-17" ;
    schema1:description "HIV-1-neutralizing antibodies develop in most HIV-1-infected individuals, although highly effective antibodies are generally observed only after years of chronic infection. Here, we characterize the rate of maturation and extent of diversity for the lineage that produced the broadly neutralizing antibody VRC01 through longitudinal sampling of peripheral B cell transcripts over 15 years and co-crystal structures of lineage members. Next-generation sequencing identified VRC01-lineage transcripts, which encompassed diverse antibodies organized into distinct phylogenetic clades. Prevalent clades maintained characteristic features of antigen recognition, though each evolved binding loops and disulfides that formed distinct recognition surfaces. Over the course of the study period, VRC01-lineage clades showed continuous evolution, with rates of ∼2 substitutions per 100 nucleotides per year, comparable to that of HIV-1 evolution. This high rate of antibody evolution provides a mechanism by which antibody lineages can achieve extraordinary diversity and, over years of chronic infection, develop effective HIV-1 neutralization." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767444_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767440_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767439_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767420_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767418_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767427_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767430_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767436_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767431_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767442_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767433_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767443_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767438_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767445_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767426_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767421_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767434_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767423_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767447_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767429_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767425_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767446_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767422_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767424_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767428_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767435_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767419_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767437_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767441_1.unique.igblast.airr.tsv.gz" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR1767432_1.unique.igblast.airr.tsv.gz" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:endDate "2019-03-31" ;
            schema1:funder [ a schema1:Organization ;
                    schema1:alternateName "Instituto Nacional de Alergias y Enfermedades Infecciosas",
                        "NIAID",
                        "National Institute of Allergy & Infectious Diseases" ;
                    schema1:employee [ a schema1:Person ;
                            schema1:familyName "SINGH" ;
                            schema1:givenName "ANJALI" ;
                            schema1:name "ANJALI SINGH" ] ;
                    schema1:identifier "https://ror.org/043z4tv69" ;
                    schema1:name "National Institute of Allergy and Infectious Diseases" ;
                    schema1:parentOrganization "National Institutes of Health" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:value "1P01AI104722-01A1" ] ;
            schema1:name "High Resolution Analysis of Env-directed B Cells to Accelerate Vaccine Design" ;
            schema1:startDate "2014-04-01" ;
            schema1:url "https://reporter.nih.gov/project-details/8680621" ],
        [ a schema1:MonetaryGrant ;
            schema1:funder [ a schema1:Organization ;
                    schema1:alternateName "Instituto Nacional de Alergias y Enfermedades Infecciosas",
                        "NIAID",
                        "National Institute of Allergy & Infectious Diseases" ;
                    schema1:identifier "https://ror.org/043z4tv69" ;
                    schema1:name "National Institute of Allergy and Infectious Diseases" ;
                    schema1:parentOrganization "National Institutes of Health" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:value "1ZIAAI005022-08" ] ;
            schema1:name "Neutralization Mechanisms Of Anti-HIV-1 Monoclonal Antibodies" ;
            schema1:url "https://reporter.nih.gov/project-details/7964824" ] ;
    schema1:healthCondition [ a schema1:DefinedTerm ;
            schema1:alternateName "HIV infection",
                "Human immunodeficiency virus caused disease or disorder",
                "Human immunodeficiency virus disease or disorder",
                "Human immunodeficiency virus infectious disease" ;
            schema1:identifier "0005109" ;
            schema1:inDefinedTermSet "MONDO" ;
            schema1:name "HIV infectious disease" ;
            schema1:url "http://purl.obolibrary.org/obo/MONDO_0005109" ;
            nde:isCurated true ;
            nde:originalName "human immunodeficiency virus infectious disease" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID <https://registry.identifiers.org/registry/bioproject> ;
            schema1:url "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA272713" ;
            schema1:value "PRJNA272713" ] ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:archivedAt "https://vdjserver.org/community?study_id=PRJNA272713" ;
            schema1:name "VDJServer" ;
            schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ;
            nde:versionDate "2026-10-25" ] ;
    schema1:infectiousAgent [ a schema1:DefinedTerm ;
            schema1:alternateName "AIDS virus",
                "HIV" ;
            schema1:identifier "12721" ;
            schema1:inDefinedTermSet "UniProt" ;
            schema1:name "Human immunodeficiency virus" ;
            schema1:url "https://www.uniprot.org/taxonomy/12721" ;
            nde:isCurated false ] ;
    schema1:isAccessibleForFree true ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:about "NIAID classification" ;
            schema1:name "infectiousAgent" ],
        [ a schema1:DefinedTerm ;
            schema1:about "topicCategory" ;
            schema1:identifier "topic_3053" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Genetics" ;
            schema1:url "http://edamontology.org/topic_3053" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:name "GPT-4o-mini" ;
                    schema1:url "https://openai.com/index/chatgpt" ] ],
        [ a schema1:DefinedTerm ;
            schema1:about "NIAID classification" ;
            schema1:name "host" ],
        [ a schema1:DefinedTerm ;
            schema1:about "topicCategory" ;
            schema1:identifier "topic_0804" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Immunology" ;
            schema1:url "http://edamontology.org/topic_0804" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:name "GPT-4o-mini" ;
                    schema1:url "https://openai.com/index/chatgpt" ] ],
        [ a schema1:DefinedTerm ;
            schema1:about "topicCategory" ;
            schema1:identifier "topic_3299" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Evolutionary biology" ;
            schema1:url "http://edamontology.org/topic_3299" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:name "GPT-4o-mini" ;
                    schema1:url "https://openai.com/index/chatgpt" ] ],
        "Chronic" ;
    schema1:license "https://creativecommons.org/public-domain/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "0200082" ;
            schema1:inDefinedTermSet "OBI" ;
            schema1:name "longitudinal data analysis" ;
            schema1:url "http://purl.obolibrary.org/obo/OBI_0200082" ;
            nde:isCurated true ;
            nde:originalName "Longitudinal Study" ] ;
    schema1:name "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection" ;
    schema1:subjectOf <https://data.niaid.nih.gov/resources?id=vdj_prjna272713#metadata> ;
    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ;
    schema1:variableMeasured [ a schema1:DefinedTerm,
                schema1:PropertyValue ;
            schema1:identifier "C20971" ;
            schema1:inDefinedTermSet "NCIT" ;
            schema1:name "V(D)J Recombination" ;
            schema1:url "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971" ],
        [ a schema1:PropertyValue ;
            schema1:description "Chronic" ;
            schema1:name "disease severity" ],
        [ a schema1:DefinedTerm,
                schema1:PropertyValue ;
            schema1:identifier "data_2977" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Nucleic acid sequence" ;
            schema1:url "https://edamontology.org/data_2977" ],
        [ a schema1:PropertyValue ;
            schema1:description "African American" ;
            schema1:name "race" ] ;
    nde:date "2023-01-20" ;
    nde:sample [ a nde:SampleCollection ;
            schema1:aggregateElement [ a bios:Sample,
                        nde:Sample ;
                    schema1:additionalType "ExperimentalRunSample" ;
                    schema1:conditionsOfAccess "Open" ;
                    schema1:distribution [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767435_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767423_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767422_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767421_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767428_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767424_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767418_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767420_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767433_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767430_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767427_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767432_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767441_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767426_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767447_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767425_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767439_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767444_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767438_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767436_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767431_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767445_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767429_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767437_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767443_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767419_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767440_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767446_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767434_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ],
                        [ a schema1:DataDownload ;
                            schema1:contentUrl "SRR1767442_R1.fastq" ;
                            schema1:description "direction: forward" ;
                            schema1:encodingFormat "fastq" ] ;
                    schema1:healthCondition [ a schema1:DefinedTerm ;
                            schema1:name "HIV-1 positive" ],
                        [ a schema1:DefinedTerm ;
                            schema1:identifier "DOID:526" ;
                            schema1:inDefinedTermSet "DOID" ;
                            schema1:name "human immunodeficiency virus infectious disease" ],
                        [ a schema1:DefinedTerm ;
                            schema1:identifier "DOID:526" ;
                            schema1:inDefinedTermSet "DOID" ;
                            schema1:name "human immunodeficiency virus infectious disease" ],
                        [ a schema1:DefinedTerm ;
                            schema1:name "HIV-1 positive" ] ;
                    schema1:instrument [ a schema1:DefinedTerm ;
                            schema1:name "454 GS FLX+" ],
                        [ a schema1:DefinedTerm ;
                            schema1:name "454 GS FLX+" ] ;
                    schema1:isAccessibleForFree true ;
                    schema1:license "https://creativecommons.org/public-domain/" ;
                    schema1:measurementTechnique [ a schema1:DefinedTerm ;
                            schema1:name "PCR" ],
                        [ a schema1:DefinedTerm ;
                            schema1:name "PCR" ],
                        [ a schema1:DefinedTerm ;
                            schema1:identifier "NCIT:C15273" ;
                            schema1:inDefinedTermSet "NCIT" ;
                            schema1:name "Longitudinal Study" ],
                        [ a schema1:DefinedTerm ;
                            schema1:identifier "NCIT:C15273" ;
                            schema1:inDefinedTermSet "NCIT" ;
                            schema1:name "Longitudinal Study" ] ;
                    schema1:name "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1015503308190519786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1092125524751159786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1105053376312119786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1118969070351159786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1131811022566199786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1146285062353719786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1161789894292279786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1176779330155319786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1267875586503479786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1281748330869559786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1305886047073079786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1322078073778999786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1343982406988599786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1360174433694519786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1376022863016759786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1391355896263479786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1458615084118839786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1471800633717559786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1496110148612919786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (1513461816488759786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (788514286596919786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (803761420497719786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (819695749165879786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (834384537318199786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (896618613437239786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (909245817287479786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (928659069465399786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (943605555655479786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (962889958814519786-242ac116-0001-012)",
                        "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection (980628173746999786-242ac116-0001-012)" ;
                    schema1:temporalCoverage [ a nde:TemporalInterval ;
                            schema1:name "08-19-2008" ],
                        [ a nde:TemporalInterval ;
                            schema1:name "01-17-2008" ],
                        [ a nde:TemporalInterval ;
                            schema1:name "07-30-2001" ],
                        [ a nde:TemporalInterval ;
                            schema1:name "06-02-2009" ],
                        [ a nde:TemporalInterval ;
                            schema1:name "01-09-2007" ],
                        [ a nde:TemporalInterval ;
                            schema1:name "12-31-2009" ],
                        [ a nde:TemporalInterval ;
                            schema1:name "03-20-1995" ],
                        [ a nde:TemporalInterval ;
                            schema1:name "07-14-2006" ],
                        [ a nde:TemporalInterval ;
                            schema1:name "04-16-2002" ],
                        [ a nde:TemporalInterval ;
                            schema1:name "08-19-2008" ],
                        [ a nde:TemporalInterval ;
                            schema1:name "07-12-2007" ] ;
                    schema1:usageInfo [ a schema1:Thing ;
                            schema1:description "The software is under the GNU Affero General Public License, the data is Public Domain" ;
                            schema1:name "AIRR Data Commons usage info" ] ;
                    schema1:variableMeasured [ a schema1:DefinedTerm ;
                            schema1:description "African American" ;
                            schema1:name "race" ],
                        [ a schema1:DefinedTerm ;
                            schema1:name "IGH" ],
                        [ a schema1:DefinedTerm ;
                            schema1:name "IGH" ],
                        [ schema1:description "African American" ;
                            schema1:name "race" ],
                        [ schema1:description "Chronic" ;
                            schema1:name "disease severity" ],
                        [ a schema1:DefinedTerm ;
                            schema1:description "Chronic" ;
                            schema1:name "disease severity" ],
                        [ a schema1:DefinedTerm ;
                            schema1:name "IGK" ],
                        [ a schema1:DefinedTerm ;
                            schema1:identifier "C20971" ;
                            schema1:inDefinedTermSet "NCIT" ;
                            schema1:name "V(D)J Recombination" ;
                            schema1:url "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971" ],
                        [ schema1:description "Chronic" ;
                            schema1:name "disease severity" ],
                        [ a schema1:DefinedTerm ;
                            schema1:description "African American" ;
                            schema1:name "race" ],
                        [ schema1:description "African American" ;
                            schema1:name "race" ],
                        [ a schema1:DefinedTerm ;
                            schema1:identifier "data_2977" ;
                            schema1:inDefinedTermSet "EDAM" ;
                            schema1:name "Nucleic acid sequence" ;
                            schema1:url "https://edamontology.org/data_2977" ],
                        [ a schema1:DefinedTerm ;
                            schema1:description "Chronic" ;
                            schema1:name "disease severity" ],
                        [ a schema1:DefinedTerm ;
                            schema1:identifier "C20971" ;
                            schema1:inDefinedTermSet "NCIT" ;
                            schema1:name "V(D)J Recombination" ;
                            schema1:url "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971" ],
                        [ a schema1:DefinedTerm ;
                            schema1:identifier "data_2977" ;
                            schema1:inDefinedTermSet "EDAM" ;
                            schema1:name "Nucleic acid sequence" ;
                            schema1:url "https://edamontology.org/data_2977" ] ;
                    bios:alternateIdentifier "1015503308190519786-242ac116-0001-012",
                        "105783803776265750-242ac116-0001-012",
                        "1092125524751159786-242ac116-0001-012",
                        "1105053376312119786-242ac116-0001-012",
                        "1118969070351159786-242ac116-0001-012",
                        "1131811022566199786-242ac116-0001-012",
                        "1146285062353719786-242ac116-0001-012",
                        "1161789894292279786-242ac116-0001-012",
                        "1176779330155319786-242ac116-0001-012",
                        "125497703664905750-242ac116-0001-012",
                        "1267875586503479786-242ac116-0001-012",
                        "1281748330869559786-242ac116-0001-012",
                        "1305886047073079786-242ac116-0001-012",
                        "1322078073778999786-242ac116-0001-012",
                        "1343982406988599786-242ac116-0001-012",
                        "1360174433694519786-242ac116-0001-012",
                        "1376022863016759786-242ac116-0001-012",
                        "1391355896263479786-242ac116-0001-012",
                        "1458615084118839786-242ac116-0001-012",
                        "1471800633717559786-242ac116-0001-012",
                        "1496110148612919786-242ac116-0001-012",
                        "150451463654665750-242ac116-0001-012",
                        "1513461816488759786-242ac116-0001-012",
                        "165140251806985750-242ac116-0001-012",
                        "264482845363465750-242ac116-0001-012",
                        "279901777956105750-242ac116-0001-012",
                        "309751800663305750-242ac116-0001-012",
                        "386932362972425750-242ac116-0001-012",
                        "406861011225865750-242ac116-0001-012",
                        "422322893491465750-242ac116-0001-012",
                        "43380410413879786-242ac116-0001-012",
                        "439373913656585750-242ac116-0001-012",
                        "44193972751625750-242ac116-0001-012",
                        "460719901117705750-242ac116-0001-012",
                        "482967831710985750-242ac116-0001-012",
                        "497656619863305750-242ac116-0001-012",
                        "578402005028105750-242ac116-0001-012",
                        "59226358287625750-242ac116-0001-012",
                        "595109427809545750-242ac116-0001-012",
                        "612246347320585750-242ac116-0001-012",
                        "627493481221385750-242ac116-0001-012",
                        "644029105310985750-242ac116-0001-012",
                        "659233289538825750-242ac116-0001-012",
                        "741310114565385750-242ac116-0001-012",
                        "74258743823625750-242ac116-0001-012",
                        "758532933422345750-242ac116-0001-012",
                        "775583953587465750-242ac116-0001-012",
                        "788514286596919786-242ac116-0001-012",
                        "794610658708745750-242ac116-0001-012",
                        "803761420497719786-242ac116-0001-012",
                        "812477722660105750-242ac116-0001-012",
                        "819695749165879786-242ac116-0001-012",
                        "834384537318199786-242ac116-0001-012",
                        "896618613437239786-242ac116-0001-012",
                        "89677676416265750-242ac116-0001-012",
                        "909245817287479786-242ac116-0001-012",
                        "928659069465399786-242ac116-0001-012",
                        "943605555655479786-242ac116-0001-012",
                        "962889958814519786-242ac116-0001-012",
                        "980628173746999786-242ac116-0001-012",
                        "SRR1767418",
                        "SRR1767419",
                        "SRR1767420",
                        "SRR1767421",
                        "SRR1767422",
                        "SRR1767423",
                        "SRR1767424",
                        "SRR1767425",
                        "SRR1767426",
                        "SRR1767427",
                        "SRR1767428",
                        "SRR1767429",
                        "SRR1767430",
                        "SRR1767431",
                        "SRR1767432",
                        "SRR1767433",
                        "SRR1767434",
                        "SRR1767435",
                        "SRR1767436",
                        "SRR1767437",
                        "SRR1767438",
                        "SRR1767439",
                        "SRR1767440",
                        "SRR1767441",
                        "SRR1767442",
                        "SRR1767443",
                        "SRR1767444",
                        "SRR1767445",
                        "SRR1767446",
                        "SRR1767447" ;
                    bios:anatomicalStructure [ a schema1:DefinedTerm ;
                            schema1:identifier "UBERON:0000178" ;
                            schema1:inDefinedTermSet "UBERON" ;
                            schema1:name "blood" ] ;
                    bios:collector [ a schema1:Person ;
                            schema1:name "VACCINE RESEARCH CENTER" ],
                        [ a schema1:Person ;
                            schema1:name "VACCINE RESEARCH CENTER" ] ;
                    bios:developmentalStage [ a schema1:QuantitativeValue ;
                            schema1:maxValue 60 ;
                            schema1:minValue 45 ;
                            schema1:unitCode "UO:0000036" ;
                            schema1:unitText "year" ] ;
                    bios:sampleProcess "Single cell: False",
                        "none" ;
                    bios:sampleState "partial" ;
                    bios:sampleType [ a schema1:DefinedTerm ;
                            schema1:name "DNA" ] ;
                    bios:sex "male" ;
                    nde:species [ a schema1:DefinedTerm ;
                            schema1:identifier "NCBITAXON:9606" ;
                            schema1:inDefinedTermSet "NCBITAXON" ;
                            schema1:name "Homo sapiens" ],
                        [ a schema1:DefinedTerm ;
                            schema1:identifier "NCBITAXON:9606" ;
                            schema1:inDefinedTermSet "NCBITAXON" ;
                            schema1:name "Homo sapiens" ] ] ;
            schema1:itemListElement [ schema1:identifier "SRS823746" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823734" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823743" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823747" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823737" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823726" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823732" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823719" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823744" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823741" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823727" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823740" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823721" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823745" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823723" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823730" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823736" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823728" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823742" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823725" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823735" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823720" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823739" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823738" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823729" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823724" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823731" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823733" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823718" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ],
                [ schema1:identifier "SRS823722" ;
                    schema1:url "https://vdjserver.org/community?study_id=PRJNA272713" ] ;
            schema1:numberOfItems [ a schema1:QuantitativeValue ;
                    schema1:unitText "sample" ;
                    schema1:value 30 ] ] ;
    nde:species [ a schema1:DefinedTerm ;
            schema1:alternateName "Home sapiens",
                "Homo sampiens",
                "Homo sapeins",
                "Homo sapian",
                "Homo sapians",
                "Homo sapien",
                "Homo sapience",
                "Homo sapiens Linnaeus, 1758",
                "Homo sapiense",
                "Homo sapients",
                "Homo sapines",
                "Homo spaiens",
                "Homo spiens",
                "Human",
                "Humo sapiens",
                "human" ;
            schema1:identifier "9606" ;
            schema1:inDefinedTermSet "UniProt" ;
            schema1:name "Homo sapiens" ;
            schema1:url "https://www.uniprot.org/taxonomy/9606" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:dateModified "2023-10-05" ;
                    schema1:name "PubTator" ;
                    schema1:url "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html" ] ;
            nde:isCurated true ;
            nde:originalName "homo sapiens" ;
            cdifniaid:commonName "Human" ] .

<https://data.niaid.nih.gov/resources?id=vdj_prjna272713#metadata> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/discovery/1.1>,
        <https://w3id.org/cdif/niaid/1.0> ;
    schema1:about <https://data.niaid.nih.gov/resources?id=vdj_prjna272713> ;
    schema1:additionalType dcat:CatalogRecord ;
    schema1:description """CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record vdj_prjna272713, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.

Metadata source from PMID.

Metadata source from GPT.""" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "NIAID Data Discovery Portal" ;
            schema1:url "https://data.niaid.nih.gov/" ] ;
    schema1:name "Metadata record for: Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection" ;
    schema1:sdDatePublished "2026-10-28" .


```


### Immunology Database and Analysis Portal (ImmPort) record sdy2580
Record sdy2580 from Immunology Database and Analysis Portal (ImmPort), as the NIAID Data Discovery Portal API returned it
(converters/NIAID/niaidExamples/sdy2580.json), converted by harvest_niaid_to_cdif.py.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "nde": "https://discovery.biothings.io/ns/nde/",
    "bios": "https://bioschemas.org/",
    "time": "http://www.w3.org/2006/time#",
    "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
  },
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=sdy2580",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=sdy2580"
    },
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=sdy2580#metadata",
    "schema:name": "Metadata record for: Polymer delivery of Influenza Vaccine",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record sdy2580, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.",
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.identifiers.org/registry/doi"
    },
    "schema:value": "10.21430/m3c49tyd79",
    "schema:url": "https://doi.org/10.21430/m3c49tyd79"
  },
  "bios:alternateIdentifier": [
    "SDY2580"
  ],
  "schema:dateModified": "2025-10-30",
  "nde:date": "2025-10-30",
  "schema:alternateName": [
    "SDY2580",
    "10.21430/m3c49tyd79",
    "Polymer delivery of Influenza Vaccine"
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "University of North Carolina"
        },
        "schema:name": "Kristy Ainslie"
      }
    ]
  },
  "nde:citedBy": [
    {
      "@type": [
        "schema:ScholarlyArticle"
      ],
      "nde:doi": "10.1021/acsami.2c04671",
      "schema:name": "Metal-Organic Coordination Polymer for Delivery of a Subunit Broadly Acting Influenza Vaccine.",
      "nde:pmid": "35704854",
      "schema:url": "https://pubmed.ncbi.nlm.nih.gov/35704854"
    }
  ],
  "schema:conditionsOfAccess": [
    "Closed"
  ],
  "nde:curatedBy": {
    "@type": [
      "schema:DataCatalog"
    ],
    "schema:archivedAt": "https://immport.org/shared/study/SDY2580",
    "schema:name": "ImmPort",
    "schema:url": "https://immport.org",
    "nde:versionDate": "2025-10-30T00:00:00"
  },
  "schema:description": "Using polymers to deliver broadly reactive influenza subunit vaccines\n\nNot Provided",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:endDate": "2020-09-09",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "National Institute of Allergy & Infectious Diseases",
          "NIAID",
          "Instituto Nacional de Alergias y Enfermedades Infecciosas"
        ],
        "schema:identifier": "https://ror.org/043z4tv69",
        "schema:name": "National Institute of Allergy and Infectious Diseases",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "75N93019C00052-0-9999-1"
      },
      "schema:name": "CIVIC: University of Georgia Center for Influenza Vaccine Research in High Risk Populations",
      "schema:startDate": "2019-09-10",
      "schema:url": "https://reporter.nih.gov/project-details/10021763"
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "National Institute of Allergy & Infectious Diseases",
          "NIAID",
          "Instituto Nacional de Alergias y Enfermedades Infecciosas"
        ],
        "schema:identifier": "https://ror.org/043z4tv69",
        "schema:name": "National Institute of Allergy and Infectious Diseases",
        "schema:parentOrganization": "National Institutes of Health"
      }
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "ImmPort Curation",
        "schema:url": "https://www.immport.org"
      },
      "schema:identifier": "8469",
      "schema:inDefinedTermSet": "DOID",
      "nde:isCurated": true,
      "schema:name": "influenza",
      "nde:originalName": "influenza",
      "schema:url": "http://purl.obolibrary.org/obo/DOID_8469"
    }
  ],
  "schema:includedInDataCatalog": {
    "@type": [
      "schema:DataCatalog"
    ],
    "schema:archivedAt": "https://immport.org/shared/study/SDY2580",
    "schema:name": "Immunology Database and Analysis Portal (ImmPort)",
    "schema:url": "https://immport.org",
    "nde:versionDate": "2025-10-30T00:00:00"
  },
  "schema:infectiousAgent": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "miscellaneous nucleic acid",
        "none",
        "not shown",
        "not specified",
        "other",
        "sonstige nucleic acid",
        "unidentified organism",
        "unknown",
        "unknown organism",
        "unknwon",
        "unspecified",
        "unidentified root endophyte",
        "unclassified sequence"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2023-10-05",
        "schema:name": "PubTator",
        "schema:url": "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html"
      },
      "schema:identifier": "32644",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": true,
      "schema:name": "unidentified",
      "nde:originalName": "not specified",
      "schema:url": "https://www.uniprot.org/taxonomy/32644"
    }
  ],
  "schema:isAccessibleForFree": true,
  "prov:wasDerivedFrom": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://www.immport.org/browser/?path=SDY2580",
      "schema:name": "Eckshtain-Levi.pdf",
      "schema:description": "Methods associated with Metal-Organic Coordination Plymer for Delivery of a Subunit Broadly Acting Influenza Vaccine publication"
    }
  ],
  "schema:keywords": [
    "influenza",
    "PXRD, molecular modeling, endotoxin quantification assessment, scanning electron microscopy, zeta particle size analysis, high performance liquid chromatography, MTT assay, sandwich ELISA, nitride concentration assessment",
    "CIVICs Collaborative Influenza Vaccine Innovation Centers",
    {
      "schema:name": "infectiousAgent",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    },
    {
      "schema:name": "host",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:license": [
    "https://www.immport.org/agreement"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0000075",
      "schema:inDefinedTermSet": "MMO",
      "nde:isCurated": true,
      "schema:name": "enzyme linked immunosorbent assay",
      "nde:originalName": "ELISA",
      "schema:url": "http://purl.obolibrary.org/obo/MMO_0000075"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0000011",
      "schema:inDefinedTermSet": "OBI",
      "nde:isCurated": true,
      "schema:name": "planned process",
      "nde:originalName": "Other",
      "schema:url": "http://purl.obolibrary.org/obo/OBI_0000011"
    }
  ],
  "schema:name": "Polymer delivery of Influenza Vaccine",
  "schema:sameAs": [
    "https://doi.org/10.21430/m3c49tyd79"
  ],
  "nde:sample": {
    "@type": [
      "nde:Sample",
      "bios:Sample"
    ],
    "bios:sampleQuantity": {
      "@type": [
        "schema:QuantitativeValue"
      ],
      "schema:unitCode": "http://purl.obolibrary.org/obo/NCIT_C207572",
      "schema:unitText": "enrolled subjects",
      "schema:value": 61
    }
  },
  "schema:sourceOrganization": [
    {
      "@type": [
        "schema:ResearchProject"
      ],
      "schema:alternateName": [
        "CIVIC",
        "Collaborative Influenza Vaccine Innovation Centers",
        "CIVICs"
      ],
      "cdifniaid:correctionApproved": true,
      "schema:description": "Collaborative Influenza Vaccine Innovation Centers (CIVICs) is a network of research centers that will work together in a coordinated, multidisciplinary effort to develop more durable, broadly protective and longer-lasting influenza vaccines. For more information, visit the NIAID program page: https://www.niaid.nih.gov/research/civics\n\nCollaborative Influenza Vaccine Innovation Centers (CIVICs) is a network of research centers working collaboratively to develop next-generation influenza vaccines. Their goal is to create vaccines that provide broader, longer-lasting protection against influenza viruses.",
      "schema:name": "NIAID CIVICs Network",
      "schema:parentOrganization": [
        "NIAID"
      ],
      "schema:url": "https://www.niaidcivics.org/"
    }
  ],
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Mouse",
        "LK3 transgenic mice",
        "Mus musculus Linnaeus, 1758",
        "Mus sp. 129SV",
        "house mouse",
        "mice C57BL/6xCBA/CaJ hybrid",
        "mouse",
        "nude mice",
        "transgenic mice"
      ],
      "cdifniaid:commonName": "Mouse",
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2023-10-05",
        "schema:name": "PubTator",
        "schema:url": "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html"
      },
      "schema:identifier": "10090",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": true,
      "schema:name": "Mus musculus",
      "nde:originalName": "mus musculus",
      "schema:url": "https://www.uniprot.org/taxonomy/10090"
    }
  ],
  "schema:url": "https://immport.org/shared/study/SDY2580"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataset/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "time": "http://www.w3.org/2006/time#",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=sdy2580",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=sdy2580"
    },
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=sdy2580#metadata",
    "schema:name": "Metadata record for: Polymer delivery of Influenza Vaccine",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record sdy2580, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.",
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.identifiers.org/registry/doi"
    },
    "schema:value": "10.21430/m3c49tyd79",
    "schema:url": "https://doi.org/10.21430/m3c49tyd79"
  },
  "bios:alternateIdentifier": [
    "SDY2580"
  ],
  "schema:dateModified": "2025-10-30",
  "nde:date": "2025-10-30",
  "schema:alternateName": [
    "SDY2580",
    "10.21430/m3c49tyd79",
    "Polymer delivery of Influenza Vaccine"
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "University of North Carolina"
        },
        "schema:name": "Kristy Ainslie"
      }
    ]
  },
  "nde:citedBy": [
    {
      "@type": [
        "schema:ScholarlyArticle"
      ],
      "nde:doi": "10.1021/acsami.2c04671",
      "schema:name": "Metal-Organic Coordination Polymer for Delivery of a Subunit Broadly Acting Influenza Vaccine.",
      "nde:pmid": "35704854",
      "schema:url": "https://pubmed.ncbi.nlm.nih.gov/35704854"
    }
  ],
  "schema:conditionsOfAccess": [
    "Closed"
  ],
  "nde:curatedBy": {
    "@type": [
      "schema:DataCatalog"
    ],
    "schema:archivedAt": "https://immport.org/shared/study/SDY2580",
    "schema:name": "ImmPort",
    "schema:url": "https://immport.org",
    "nde:versionDate": "2025-10-30T00:00:00"
  },
  "schema:description": "Using polymers to deliver broadly reactive influenza subunit vaccines\n\nNot Provided",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:endDate": "2020-09-09",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "National Institute of Allergy & Infectious Diseases",
          "NIAID",
          "Instituto Nacional de Alergias y Enfermedades Infecciosas"
        ],
        "schema:identifier": "https://ror.org/043z4tv69",
        "schema:name": "National Institute of Allergy and Infectious Diseases",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "75N93019C00052-0-9999-1"
      },
      "schema:name": "CIVIC: University of Georgia Center for Influenza Vaccine Research in High Risk Populations",
      "schema:startDate": "2019-09-10",
      "schema:url": "https://reporter.nih.gov/project-details/10021763"
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "National Institute of Allergy & Infectious Diseases",
          "NIAID",
          "Instituto Nacional de Alergias y Enfermedades Infecciosas"
        ],
        "schema:identifier": "https://ror.org/043z4tv69",
        "schema:name": "National Institute of Allergy and Infectious Diseases",
        "schema:parentOrganization": "National Institutes of Health"
      }
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "ImmPort Curation",
        "schema:url": "https://www.immport.org"
      },
      "schema:identifier": "8469",
      "schema:inDefinedTermSet": "DOID",
      "nde:isCurated": true,
      "schema:name": "influenza",
      "nde:originalName": "influenza",
      "schema:url": "http://purl.obolibrary.org/obo/DOID_8469"
    }
  ],
  "schema:includedInDataCatalog": {
    "@type": [
      "schema:DataCatalog"
    ],
    "schema:archivedAt": "https://immport.org/shared/study/SDY2580",
    "schema:name": "Immunology Database and Analysis Portal (ImmPort)",
    "schema:url": "https://immport.org",
    "nde:versionDate": "2025-10-30T00:00:00"
  },
  "schema:infectiousAgent": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "miscellaneous nucleic acid",
        "none",
        "not shown",
        "not specified",
        "other",
        "sonstige nucleic acid",
        "unidentified organism",
        "unknown",
        "unknown organism",
        "unknwon",
        "unspecified",
        "unidentified root endophyte",
        "unclassified sequence"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2023-10-05",
        "schema:name": "PubTator",
        "schema:url": "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html"
      },
      "schema:identifier": "32644",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": true,
      "schema:name": "unidentified",
      "nde:originalName": "not specified",
      "schema:url": "https://www.uniprot.org/taxonomy/32644"
    }
  ],
  "schema:isAccessibleForFree": true,
  "prov:wasDerivedFrom": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://www.immport.org/browser/?path=SDY2580",
      "schema:name": "Eckshtain-Levi.pdf",
      "schema:description": "Methods associated with Metal-Organic Coordination Plymer for Delivery of a Subunit Broadly Acting Influenza Vaccine publication"
    }
  ],
  "schema:keywords": [
    "influenza",
    "PXRD, molecular modeling, endotoxin quantification assessment, scanning electron microscopy, zeta particle size analysis, high performance liquid chromatography, MTT assay, sandwich ELISA, nitride concentration assessment",
    "CIVICs Collaborative Influenza Vaccine Innovation Centers",
    {
      "schema:name": "infectiousAgent",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    },
    {
      "schema:name": "host",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:license": [
    "https://www.immport.org/agreement"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0000075",
      "schema:inDefinedTermSet": "MMO",
      "nde:isCurated": true,
      "schema:name": "enzyme linked immunosorbent assay",
      "nde:originalName": "ELISA",
      "schema:url": "http://purl.obolibrary.org/obo/MMO_0000075"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0000011",
      "schema:inDefinedTermSet": "OBI",
      "nde:isCurated": true,
      "schema:name": "planned process",
      "nde:originalName": "Other",
      "schema:url": "http://purl.obolibrary.org/obo/OBI_0000011"
    }
  ],
  "schema:name": "Polymer delivery of Influenza Vaccine",
  "schema:sameAs": [
    "https://doi.org/10.21430/m3c49tyd79"
  ],
  "nde:sample": {
    "@type": [
      "nde:Sample",
      "bios:Sample"
    ],
    "bios:sampleQuantity": {
      "@type": [
        "schema:QuantitativeValue"
      ],
      "schema:unitCode": "http://purl.obolibrary.org/obo/NCIT_C207572",
      "schema:unitText": "enrolled subjects",
      "schema:value": 61
    }
  },
  "schema:sourceOrganization": [
    {
      "@type": [
        "schema:ResearchProject"
      ],
      "schema:alternateName": [
        "CIVIC",
        "Collaborative Influenza Vaccine Innovation Centers",
        "CIVICs"
      ],
      "cdifniaid:correctionApproved": true,
      "schema:description": "Collaborative Influenza Vaccine Innovation Centers (CIVICs) is a network of research centers that will work together in a coordinated, multidisciplinary effort to develop more durable, broadly protective and longer-lasting influenza vaccines. For more information, visit the NIAID program page: https://www.niaid.nih.gov/research/civics\n\nCollaborative Influenza Vaccine Innovation Centers (CIVICs) is a network of research centers working collaboratively to develop next-generation influenza vaccines. Their goal is to create vaccines that provide broader, longer-lasting protection against influenza viruses.",
      "schema:name": "NIAID CIVICs Network",
      "schema:parentOrganization": [
        "NIAID"
      ],
      "schema:url": "https://www.niaidcivics.org/"
    }
  ],
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Mouse",
        "LK3 transgenic mice",
        "Mus musculus Linnaeus, 1758",
        "Mus sp. 129SV",
        "house mouse",
        "mice C57BL/6xCBA/CaJ hybrid",
        "mouse",
        "nude mice",
        "transgenic mice"
      ],
      "cdifniaid:commonName": "Mouse",
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2023-10-05",
        "schema:name": "PubTator",
        "schema:url": "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html"
      },
      "schema:identifier": "10090",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": true,
      "schema:name": "Mus musculus",
      "nde:originalName": "mus musculus",
      "schema:url": "https://www.uniprot.org/taxonomy/10090"
    }
  ],
  "schema:url": "https://immport.org/shared/study/SDY2580"
}
```

#### ttl
```ttl
@prefix bios: <https://bioschemas.org/> .
@prefix cdifniaid: <https://w3id.org/cdif/niaid/terms/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://data.niaid.nih.gov/resources?id=sdy2580> a schema1:Dataset ;
    schema1:alternateName "10.21430/m3c49tyd79",
        "Polymer delivery of Influenza Vaccine",
        "SDY2580" ;
    schema1:conditionsOfAccess "Closed" ;
    schema1:creator ( [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "University of North Carolina" ] ;
                schema1:name "Kristy Ainslie" ] ) ;
    schema1:dateModified "2025-10-30" ;
    schema1:description """Using polymers to deliver broadly reactive influenza subunit vaccines

Not Provided""" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:endDate "2020-09-09" ;
            schema1:funder [ a schema1:Organization ;
                    schema1:alternateName "Instituto Nacional de Alergias y Enfermedades Infecciosas",
                        "NIAID",
                        "National Institute of Allergy & Infectious Diseases" ;
                    schema1:identifier "https://ror.org/043z4tv69" ;
                    schema1:name "National Institute of Allergy and Infectious Diseases" ;
                    schema1:parentOrganization "National Institutes of Health" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:value "75N93019C00052-0-9999-1" ] ;
            schema1:name "CIVIC: University of Georgia Center for Influenza Vaccine Research in High Risk Populations" ;
            schema1:startDate "2019-09-10" ;
            schema1:url "https://reporter.nih.gov/project-details/10021763" ],
        [ a schema1:MonetaryGrant ;
            schema1:funder [ a schema1:Organization ;
                    schema1:alternateName "Instituto Nacional de Alergias y Enfermedades Infecciosas",
                        "NIAID",
                        "National Institute of Allergy & Infectious Diseases" ;
                    schema1:identifier "https://ror.org/043z4tv69" ;
                    schema1:name "National Institute of Allergy and Infectious Diseases" ;
                    schema1:parentOrganization "National Institutes of Health" ] ] ;
    schema1:healthCondition [ a schema1:DefinedTerm ;
            schema1:identifier "8469" ;
            schema1:inDefinedTermSet "DOID" ;
            schema1:name "influenza" ;
            schema1:url "http://purl.obolibrary.org/obo/DOID_8469" ;
            nde:curatedBy [ a schema1:Organization ;
                    schema1:name "ImmPort Curation" ;
                    schema1:url "https://www.immport.org" ] ;
            nde:isCurated true ;
            nde:originalName "influenza" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID <https://registry.identifiers.org/registry/doi> ;
            schema1:url "https://doi.org/10.21430/m3c49tyd79" ;
            schema1:value "10.21430/m3c49tyd79" ] ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:archivedAt "https://immport.org/shared/study/SDY2580" ;
            schema1:name "Immunology Database and Analysis Portal (ImmPort)" ;
            schema1:url "https://immport.org" ;
            nde:versionDate "2025-10-30T00:00:00" ] ;
    schema1:infectiousAgent [ a schema1:DefinedTerm ;
            schema1:alternateName "miscellaneous nucleic acid",
                "none",
                "not shown",
                "not specified",
                "other",
                "sonstige nucleic acid",
                "unclassified sequence",
                "unidentified organism",
                "unidentified root endophyte",
                "unknown",
                "unknown organism",
                "unknwon",
                "unspecified" ;
            schema1:identifier "32644" ;
            schema1:inDefinedTermSet "UniProt" ;
            schema1:name "unidentified" ;
            schema1:url "https://www.uniprot.org/taxonomy/32644" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:dateModified "2023-10-05" ;
                    schema1:name "PubTator" ;
                    schema1:url "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html" ] ;
            nde:isCurated true ;
            nde:originalName "not specified" ] ;
    schema1:isAccessibleForFree true ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:about "NIAID classification" ;
            schema1:name "infectiousAgent" ],
        [ a schema1:DefinedTerm ;
            schema1:about "NIAID classification" ;
            schema1:name "host" ],
        "CIVICs Collaborative Influenza Vaccine Innovation Centers",
        "PXRD, molecular modeling, endotoxin quantification assessment, scanning electron microscopy, zeta particle size analysis, high performance liquid chromatography, MTT assay, sandwich ELISA, nitride concentration assessment",
        "influenza" ;
    schema1:license "https://www.immport.org/agreement" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "0000075" ;
            schema1:inDefinedTermSet "MMO" ;
            schema1:name "enzyme linked immunosorbent assay" ;
            schema1:url "http://purl.obolibrary.org/obo/MMO_0000075" ;
            nde:isCurated true ;
            nde:originalName "ELISA" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "0000011" ;
            schema1:inDefinedTermSet "OBI" ;
            schema1:name "planned process" ;
            schema1:url "http://purl.obolibrary.org/obo/OBI_0000011" ;
            nde:isCurated true ;
            nde:originalName "Other" ] ;
    schema1:name "Polymer delivery of Influenza Vaccine" ;
    schema1:sameAs "https://doi.org/10.21430/m3c49tyd79" ;
    schema1:sourceOrganization [ a schema1:ResearchProject ;
            schema1:alternateName "CIVIC",
                "CIVICs",
                "Collaborative Influenza Vaccine Innovation Centers" ;
            schema1:description """Collaborative Influenza Vaccine Innovation Centers (CIVICs) is a network of research centers that will work together in a coordinated, multidisciplinary effort to develop more durable, broadly protective and longer-lasting influenza vaccines. For more information, visit the NIAID program page: https://www.niaid.nih.gov/research/civics

Collaborative Influenza Vaccine Innovation Centers (CIVICs) is a network of research centers working collaboratively to develop next-generation influenza vaccines. Their goal is to create vaccines that provide broader, longer-lasting protection against influenza viruses.""" ;
            schema1:name "NIAID CIVICs Network" ;
            schema1:parentOrganization "NIAID" ;
            schema1:url "https://www.niaidcivics.org/" ;
            cdifniaid:correctionApproved true ] ;
    schema1:subjectOf <https://data.niaid.nih.gov/resources?id=sdy2580#metadata> ;
    schema1:url "https://immport.org/shared/study/SDY2580" ;
    prov:wasDerivedFrom [ a schema1:CreativeWork ;
            schema1:description "Methods associated with Metal-Organic Coordination Plymer for Delivery of a Subunit Broadly Acting Influenza Vaccine publication" ;
            schema1:name "Eckshtain-Levi.pdf" ;
            schema1:url "https://www.immport.org/browser/?path=SDY2580" ] ;
    bios:alternateIdentifier "SDY2580" ;
    nde:citedBy [ a schema1:ScholarlyArticle ;
            schema1:name "Metal-Organic Coordination Polymer for Delivery of a Subunit Broadly Acting Influenza Vaccine." ;
            schema1:url "https://pubmed.ncbi.nlm.nih.gov/35704854" ;
            nde:doi "10.1021/acsami.2c04671" ;
            nde:pmid "35704854" ] ;
    nde:curatedBy [ a schema1:DataCatalog ;
            schema1:archivedAt "https://immport.org/shared/study/SDY2580" ;
            schema1:name "ImmPort" ;
            schema1:url "https://immport.org" ;
            nde:versionDate "2025-10-30T00:00:00" ] ;
    nde:date "2025-10-30" ;
    nde:sample [ a bios:Sample,
                nde:Sample ;
            bios:sampleQuantity [ a schema1:QuantitativeValue ;
                    schema1:unitCode "http://purl.obolibrary.org/obo/NCIT_C207572" ;
                    schema1:unitText "enrolled subjects" ;
                    schema1:value 61 ] ] ;
    nde:species [ a schema1:DefinedTerm ;
            schema1:alternateName "LK3 transgenic mice",
                "Mouse",
                "Mus musculus Linnaeus, 1758",
                "Mus sp. 129SV",
                "house mouse",
                "mice C57BL/6xCBA/CaJ hybrid",
                "mouse",
                "nude mice",
                "transgenic mice" ;
            schema1:identifier "10090" ;
            schema1:inDefinedTermSet "UniProt" ;
            schema1:name "Mus musculus" ;
            schema1:url "https://www.uniprot.org/taxonomy/10090" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:dateModified "2023-10-05" ;
                    schema1:name "PubTator" ;
                    schema1:url "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html" ] ;
            nde:isCurated true ;
            nde:originalName "mus musculus" ;
            cdifniaid:commonName "Mouse" ] .

<https://data.niaid.nih.gov/resources?id=sdy2580#metadata> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/discovery/1.1>,
        <https://w3id.org/cdif/niaid/1.0> ;
    schema1:about <https://data.niaid.nih.gov/resources?id=sdy2580> ;
    schema1:additionalType dcat:CatalogRecord ;
    schema1:description "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record sdy2580, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them." ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "NIAID Data Discovery Portal" ;
            schema1:url "https://data.niaid.nih.gov/" ] ;
    schema1:name "Metadata record for: Polymer delivery of Influenza Vaccine" ;
    schema1:sdDatePublished "2026-10-28" .


```


### Library of Integrated Network-based Cellular Signatures (LINCS) record lds-1224
Record lds-1224 from Library of Integrated Network-based Cellular Signatures (LINCS), as the NIAID Data Discovery Portal API returned it
(converters/NIAID/niaidExamples/lds-1224.json), converted by harvest_niaid_to_cdif.py.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "nde": "https://discovery.biothings.io/ns/nde/",
    "bios": "https://bioschemas.org/",
    "time": "http://www.w3.org/2006/time#",
    "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
  },
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=lds-1224",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=lds-1224"
    },
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record lds-1224, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.\n\nMetadata source from EXTRACT.",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=lds-1224#metadata",
    "schema:name": "Metadata record for: Synovial Fibroblast 3.1: Secretion response of seven primary human synovial fibroblast samples from healthy and rheumato",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": "LDS-1224",
  "schema:dateModified": "2017-09-19",
  "schema:datePublished": "2015-08-27",
  "nde:date": "2017-09-19",
  "cdifniaid:assayformat": "Cell based",
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "HMS LINCS (Harvard Medical School)"
        },
        "schema:name": "Douglas A. Lauffenburger",
        "schema:url": "http://lincs.hms.harvard.edu"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "HMS LINCS (Harvard Medical School)"
        },
        "schema:name": "Peter Sorger",
        "schema:url": "http://lincs.hms.harvard.edu"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Douglas S. Jones"
      }
    ]
  },
  "schema:description": "Supernatant levels of 51 cytokines, chemokines, growth factors, and proteases were measured using a multiplexed bead-based sandwich immunoassay to quantify the secretion response of 7 primary human synovial fibroblast samples from healthy and rheumatoid arthritis-diagnosed donors exposed to 3 different stimuli in the presence or absence of 1 of 5 small molecule kinase inhibitors. A full replicate of this experiment (including cell stimulation, supernatant recovery, and Luminex analysis) was conducted on a separate day and is available in HMS dataset #20235. A third, related dataset from the same project also is available: #20233.",
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentSize": "192635",
      "schema:contentUrl": "http://www.opengis.net/def/nil/OGC/0/missing"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "NIH 1U54HG006097-01; NIH 1U54HL127365-01"
      }
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Arthritis or polyarthritis, rheumatic",
        "atrophic Arthritis"
      ],
      "schema:identifier": "7148",
      "schema:inDefinedTermSet": "DOID",
      "nde:isCurated": true,
      "schema:name": "rheumatoid arthritis",
      "nde:originalName": "rheumatoid arthritis",
      "schema:url": "http://purl.obolibrary.org/obo/DOID_7148"
    }
  ],
  "schema:includedInDataCatalog": {
    "@type": [
      "schema:DataCatalog"
    ],
    "schema:archivedAt": "https://lincsportal.ccs.miami.edu/datasets/view/LDS-1224",
    "schema:name": "Library of Integrated Network-based Cellular Signatures (LINCS)",
    "schema:url": "https://lincsportal.ccs.miami.edu/datasets/",
    "nde:versionDate": "2026-10-24"
  },
  "prov:wasDerivedFrom": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "LDG-1218_Protocol.pdf",
      "schema:name": "protocol"
    }
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "related to",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:url": "https://lincsportal.ccs.miami.edu/datasets/view/LDG-1218"
      },
      "schema:name": "LDG-1218"
    }
  ],
  "schema:keywords": [
    "Bead-based immunoassay",
    "TNF-a",
    "Binding",
    "Post-translational protein modification, Signaling",
    "Protein profile",
    "IL-1 alpha",
    {
      "schema:name": "host",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:license": [
    "http://www.opengis.net/def/nil/OGC/0/missing"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0010050",
      "schema:inDefinedTermSet": "BAO",
      "nde:isCurated": true,
      "schema:name": "Bead-based immunoassay for protein state",
      "nde:originalName": "Bead-based immunoassay for protein state",
      "schema:url": "https://ontobee.org/ontology/BAO?iri=http://www.bioassayontology.org/bao#BAO_0010050"
    }
  ],
  "schema:name": "Synovial Fibroblast 3.1: Secretion response of seven primary human synovial fibroblast samples from healthy and rheumatoid arthritis donors to a panel of 3 stimuli and 5 small molecule inhibitors (replicate 1 of 2)",
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Humo sapiens",
        "Home sapiens",
        "Homo sapines",
        "Homo sapian",
        "Homo sapiens Linnaeus, 1758",
        "Homo sampiens",
        "Homo sapians",
        "Homo sapien",
        "Homo sapients",
        "Homo spaiens",
        "Homo spiens",
        "Human",
        "Homo sapeins",
        "Homo sapience",
        "Homo sapiense",
        "human"
      ],
      "cdifniaid:commonName": "Human",
      "schema:identifier": "9606",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": false,
      "schema:name": "Homo sapiens",
      "nde:originalName": "human",
      "schema:url": "https://www.uniprot.org/taxonomy/9606"
    }
  ],
  "schema:url": "https://lincsportal.ccs.miami.edu/datasets/view/LDS-1224",
  "schema:variableMeasured": [
    {
      "@type": [
        "schema:PropertyValue",
        "schema:DefinedTerm"
      ],
      "schema:name": "Fluorescence intensity"
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
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataset/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "time": "http://www.w3.org/2006/time#",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=lds-1224",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=lds-1224"
    },
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record lds-1224, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.\n\nMetadata source from EXTRACT.",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=lds-1224#metadata",
    "schema:name": "Metadata record for: Synovial Fibroblast 3.1: Secretion response of seven primary human synovial fibroblast samples from healthy and rheumato",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": "LDS-1224",
  "schema:dateModified": "2017-09-19",
  "schema:datePublished": "2015-08-27",
  "nde:date": "2017-09-19",
  "cdifniaid:assayformat": "Cell based",
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "HMS LINCS (Harvard Medical School)"
        },
        "schema:name": "Douglas A. Lauffenburger",
        "schema:url": "http://lincs.hms.harvard.edu"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "HMS LINCS (Harvard Medical School)"
        },
        "schema:name": "Peter Sorger",
        "schema:url": "http://lincs.hms.harvard.edu"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Douglas S. Jones"
      }
    ]
  },
  "schema:description": "Supernatant levels of 51 cytokines, chemokines, growth factors, and proteases were measured using a multiplexed bead-based sandwich immunoassay to quantify the secretion response of 7 primary human synovial fibroblast samples from healthy and rheumatoid arthritis-diagnosed donors exposed to 3 different stimuli in the presence or absence of 1 of 5 small molecule kinase inhibitors. A full replicate of this experiment (including cell stimulation, supernatant recovery, and Luminex analysis) was conducted on a separate day and is available in HMS dataset #20235. A third, related dataset from the same project also is available: #20233.",
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentSize": "192635",
      "schema:contentUrl": "http://www.opengis.net/def/nil/OGC/0/missing"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "NIH 1U54HG006097-01; NIH 1U54HL127365-01"
      }
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Arthritis or polyarthritis, rheumatic",
        "atrophic Arthritis"
      ],
      "schema:identifier": "7148",
      "schema:inDefinedTermSet": "DOID",
      "nde:isCurated": true,
      "schema:name": "rheumatoid arthritis",
      "nde:originalName": "rheumatoid arthritis",
      "schema:url": "http://purl.obolibrary.org/obo/DOID_7148"
    }
  ],
  "schema:includedInDataCatalog": {
    "@type": [
      "schema:DataCatalog"
    ],
    "schema:archivedAt": "https://lincsportal.ccs.miami.edu/datasets/view/LDS-1224",
    "schema:name": "Library of Integrated Network-based Cellular Signatures (LINCS)",
    "schema:url": "https://lincsportal.ccs.miami.edu/datasets/",
    "nde:versionDate": "2026-10-24"
  },
  "prov:wasDerivedFrom": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "LDG-1218_Protocol.pdf",
      "schema:name": "protocol"
    }
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "related to",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:url": "https://lincsportal.ccs.miami.edu/datasets/view/LDG-1218"
      },
      "schema:name": "LDG-1218"
    }
  ],
  "schema:keywords": [
    "Bead-based immunoassay",
    "TNF-a",
    "Binding",
    "Post-translational protein modification, Signaling",
    "Protein profile",
    "IL-1 alpha",
    {
      "schema:name": "host",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:license": [
    "http://www.opengis.net/def/nil/OGC/0/missing"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "0010050",
      "schema:inDefinedTermSet": "BAO",
      "nde:isCurated": true,
      "schema:name": "Bead-based immunoassay for protein state",
      "nde:originalName": "Bead-based immunoassay for protein state",
      "schema:url": "https://ontobee.org/ontology/BAO?iri=http://www.bioassayontology.org/bao#BAO_0010050"
    }
  ],
  "schema:name": "Synovial Fibroblast 3.1: Secretion response of seven primary human synovial fibroblast samples from healthy and rheumatoid arthritis donors to a panel of 3 stimuli and 5 small molecule inhibitors (replicate 1 of 2)",
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Humo sapiens",
        "Home sapiens",
        "Homo sapines",
        "Homo sapian",
        "Homo sapiens Linnaeus, 1758",
        "Homo sampiens",
        "Homo sapians",
        "Homo sapien",
        "Homo sapients",
        "Homo spaiens",
        "Homo spiens",
        "Human",
        "Homo sapeins",
        "Homo sapience",
        "Homo sapiense",
        "human"
      ],
      "cdifniaid:commonName": "Human",
      "schema:identifier": "9606",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": false,
      "schema:name": "Homo sapiens",
      "nde:originalName": "human",
      "schema:url": "https://www.uniprot.org/taxonomy/9606"
    }
  ],
  "schema:url": "https://lincsportal.ccs.miami.edu/datasets/view/LDS-1224",
  "schema:variableMeasured": [
    {
      "@type": [
        "schema:PropertyValue",
        "schema:DefinedTerm"
      ],
      "schema:name": "Fluorescence intensity"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdifniaid: <https://w3id.org/cdif/niaid/terms/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://data.niaid.nih.gov/resources?id=lds-1224> a schema1:Dataset ;
    schema1:creator ( [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "HMS LINCS (Harvard Medical School)" ] ;
                schema1:name "Douglas A. Lauffenburger" ;
                schema1:url "http://lincs.hms.harvard.edu" ] [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "HMS LINCS (Harvard Medical School)" ] ;
                schema1:name "Peter Sorger" ;
                schema1:url "http://lincs.hms.harvard.edu" ] [ a schema1:Person ;
                schema1:name "Douglas S. Jones" ] ) ;
    schema1:dateModified "2017-09-19" ;
    schema1:datePublished "2015-08-27" ;
    schema1:description "Supernatant levels of 51 cytokines, chemokines, growth factors, and proteases were measured using a multiplexed bead-based sandwich immunoassay to quantify the secretion response of 7 primary human synovial fibroblast samples from healthy and rheumatoid arthritis-diagnosed donors exposed to 3 different stimuli in the presence or absence of 1 of 5 small molecule kinase inhibitors. A full replicate of this experiment (including cell stimulation, supernatant recovery, and Luminex analysis) was conducted on a separate day and is available in HMS dataset #20235. A third, related dataset from the same project also is available: #20233." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentSize "192635" ;
            schema1:contentUrl "http://www.opengis.net/def/nil/OGC/0/missing" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:value "NIH 1U54HG006097-01; NIH 1U54HL127365-01" ] ] ;
    schema1:healthCondition [ a schema1:DefinedTerm ;
            schema1:alternateName "Arthritis or polyarthritis, rheumatic",
                "atrophic Arthritis" ;
            schema1:identifier "7148" ;
            schema1:inDefinedTermSet "DOID" ;
            schema1:name "rheumatoid arthritis" ;
            schema1:url "http://purl.obolibrary.org/obo/DOID_7148" ;
            nde:isCurated true ;
            nde:originalName "rheumatoid arthritis" ] ;
    schema1:identifier "LDS-1224" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:archivedAt "https://lincsportal.ccs.miami.edu/datasets/view/LDS-1224" ;
            schema1:name "Library of Integrated Network-based Cellular Signatures (LINCS)" ;
            schema1:url "https://lincsportal.ccs.miami.edu/datasets/" ;
            nde:versionDate "2026-10-24" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:about "NIAID classification" ;
            schema1:name "host" ],
        "Bead-based immunoassay",
        "Binding",
        "IL-1 alpha",
        "Post-translational protein modification, Signaling",
        "Protein profile",
        "TNF-a" ;
    schema1:license "http://www.opengis.net/def/nil/OGC/0/missing" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "0010050" ;
            schema1:inDefinedTermSet "BAO" ;
            schema1:name "Bead-based immunoassay for protein state" ;
            schema1:url "https://ontobee.org/ontology/BAO?iri=http://www.bioassayontology.org/bao#BAO_0010050" ;
            nde:isCurated true ;
            nde:originalName "Bead-based immunoassay for protein state" ] ;
    schema1:name "Synovial Fibroblast 3.1: Secretion response of seven primary human synovial fibroblast samples from healthy and rheumatoid arthritis donors to a panel of 3 stimuli and 5 small molecule inhibitors (replicate 1 of 2)" ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "related to" ;
            schema1:name "LDG-1218" ;
            schema1:target [ a schema1:EntryPoint ;
                    schema1:url "https://lincsportal.ccs.miami.edu/datasets/view/LDG-1218" ] ] ;
    schema1:subjectOf <https://data.niaid.nih.gov/resources?id=lds-1224#metadata> ;
    schema1:url "https://lincsportal.ccs.miami.edu/datasets/view/LDS-1224" ;
    schema1:variableMeasured [ a schema1:DefinedTerm,
                schema1:PropertyValue ;
            schema1:name "Fluorescence intensity" ] ;
    prov:wasDerivedFrom [ a schema1:CreativeWork ;
            schema1:name "protocol" ;
            schema1:url "LDG-1218_Protocol.pdf" ] ;
    nde:date "2017-09-19" ;
    nde:species [ a schema1:DefinedTerm ;
            schema1:alternateName "Home sapiens",
                "Homo sampiens",
                "Homo sapeins",
                "Homo sapian",
                "Homo sapians",
                "Homo sapien",
                "Homo sapience",
                "Homo sapiens Linnaeus, 1758",
                "Homo sapiense",
                "Homo sapients",
                "Homo sapines",
                "Homo spaiens",
                "Homo spiens",
                "Human",
                "Humo sapiens",
                "human" ;
            schema1:identifier "9606" ;
            schema1:inDefinedTermSet "UniProt" ;
            schema1:name "Homo sapiens" ;
            schema1:url "https://www.uniprot.org/taxonomy/9606" ;
            nde:isCurated false ;
            nde:originalName "human" ;
            cdifniaid:commonName "Human" ] ;
    cdifniaid:assayformat "Cell based" .

<https://data.niaid.nih.gov/resources?id=lds-1224#metadata> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/discovery/1.1>,
        <https://w3id.org/cdif/niaid/1.0> ;
    schema1:about <https://data.niaid.nih.gov/resources?id=lds-1224> ;
    schema1:additionalType dcat:CatalogRecord ;
    schema1:description """CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record lds-1224, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.

Metadata source from EXTRACT.""" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "NIAID Data Discovery Portal" ;
            schema1:url "https://data.niaid.nih.gov/" ] ;
    schema1:name "Metadata record for: Synovial Fibroblast 3.1: Secretion response of seven primary human synovial fibroblast samples from healthy and rheumato" ;
    schema1:sdDatePublished "2026-10-28" .


```


### Dryad Digital Repository (Dryad) record dryad_p79tm37
Record dryad_p79tm37 from Dryad Digital Repository (Dryad), as the NIAID Data Discovery Portal API returned it
(converters/NIAID/niaidExamples/dryad_p79tm37.json), converted by harvest_niaid_to_cdif.py.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "nde": "https://discovery.biothings.io/ns/nde/",
    "bios": "https://bioschemas.org/",
    "time": "http://www.w3.org/2006/time#",
    "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
  },
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=dryad_p79tm37",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=dryad_p79tm37"
    },
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record dryad_p79tm37, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.\n\nMetadata source from EXTRACT.\n\nMetadata source from GPT.",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=dryad_p79tm37#metadata",
    "schema:name": "Metadata record for: Ecology and evolution of blood oxygen-carrying capacity in birds",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.identifiers.org/registry/doi"
    },
    "schema:value": "10.5061/dryad.p79tm37",
    "schema:url": "https://doi.org/10.5061/dryad.p79tm37"
  },
  "schema:datePublished": "2022-04-26",
  "schema:dateModified": "2022-04-26",
  "nde:date": "2022-04-26",
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:identifier": "https://ror.org/05cq64r17",
          "schema:name": "University of Łódź",
          "schema:sameAs": [
            "https://ror.org/05cq64r17"
          ]
        },
        "schema:familyName": "Minias",
        "schema:givenName": "Piotr",
        "schema:identifier": "http://orcid.org/0000-0002-7742-6750",
        "schema:name": "Piotr Minias"
      }
    ]
  },
  "schema:citation": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "http://doi.org/10.1086/707720"
    }
  ],
  "schema:conditionsOfAccess": [
    "Open"
  ],
  "schema:description": "Blood oxygen-carrying capacity is one of important determinants of oxygen amounts supplied to the tissues per unit time and plays a key role in oxidative metabolism. In wild vertebrates, blood oxygen-carrying capacity is most commonly measured with the total blood haemoglobin concentration (Hb) and haematocrit (Hct), which is the volume percentage of red blood cells in blood. Here, I used published estimates of avian Hb and Hct (nearly one thousand estimates from 300 species) to examine macroevolutionary patterns in blood oxygen-carrying capacity of blood in birds. Phylogenetically-informed comparative analysis indicated that blood oxygen-carrying capacity was primarily determined by species distribution (latitude and elevation) and morphological constraints (body mass). I found little support for the effect of life history components on blood oxygen-carrying capacity, except for a positive association of Hct with clutch size. Hb was also positively associated with diving\nbehaviour, but I found no effect of migratoriness on either Hb or Hct. Fluctuating selection was identified as the major force shaping the evolution of blood oxygen-carrying capacity. The results offer novel insights into the evolution of Hb and Hct in birds, as well as they provide a general, phylogenetically-robust support for some long-standing hypotheses in avian ecophysiology.",
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "schema:Collection"
      ],
      "schema:contentUrl": "http://datadryad.org/api/v2/datasets/doi%253A10.5061%252Fdryad.p79tm37/download",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "schema:hasPart": [
        {
          "@type": [
            "schema:MediaObject"
          ],
          "schema:name": "Minias RAW DATARaw data for \"Ecology and evolution of blood oxygen-carrying capacity in birds\".",
          "schema:encodingFormat": [
            "application/octet-stream"
          ]
        }
      ]
    }
  ],
  "schema:includedInDataCatalog": [
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:archivedAt": "http://datadryad.org/dataset/doi%253A10.5061%252Fdryad.p79tm37",
      "schema:name": "Dryad Digital Repository (Dryad)",
      "schema:url": "https://datadryad.org",
      "nde:versionDate": "2026-10-01"
    },
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:archivedAt": "https://zenodo.org/records/6496349",
      "schema:name": "Zenodo",
      "schema:url": "https://zenodo.org/",
      "nde:versionDate": "2026-10-02"
    }
  ],
  "schema:isAccessibleForFree": true,
  "schema:keywords": [
    "Evolution: physiological",
    "Physiology: comparative",
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_0610",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Ecology",
      "schema:url": "http://edamontology.org/topic_0610",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_3500",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Zoology",
      "schema:url": "http://edamontology.org/topic_3500",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_3299",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Evolutionary biology",
      "schema:url": "http://edamontology.org/topic_3299",
      "schema:about": "topicCategory"
    },
    {
      "schema:name": "host",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:license": [
    "https://spdx.org/licenses/CC0-1.0.html"
  ],
  "schema:name": "Ecology and evolution of blood oxygen-carrying capacity in birds",
  "schema:spatialCoverage": [
    {
      "@type": [
        "schema:Place",
        "schema:AdministrativeArea"
      ],
      "schema:name": "Global"
    }
  ],
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "birds",
        "avian"
      ],
      "cdifniaid:commonName": "birds",
      "schema:identifier": "8782",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": false,
      "schema:name": "Aves",
      "nde:originalName": "birds",
      "schema:url": "https://www.uniprot.org/taxonomy/8782"
    }
  ],
  "schema:temporalCoverage": [
    "../2022-04-26"
  ],
  "schema:url": "http://datadryad.org/dataset/doi%253A10.5061%252Fdryad.p79tm37",
  "schema:hasPart": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "http://datadryad.org/downloads/file_stream/1462203"
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
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataset/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "time": "http://www.w3.org/2006/time#",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=dryad_p79tm37",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=dryad_p79tm37"
    },
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record dryad_p79tm37, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.\n\nMetadata source from EXTRACT.\n\nMetadata source from GPT.",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=dryad_p79tm37#metadata",
    "schema:name": "Metadata record for: Ecology and evolution of blood oxygen-carrying capacity in birds",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.identifiers.org/registry/doi"
    },
    "schema:value": "10.5061/dryad.p79tm37",
    "schema:url": "https://doi.org/10.5061/dryad.p79tm37"
  },
  "schema:datePublished": "2022-04-26",
  "schema:dateModified": "2022-04-26",
  "nde:date": "2022-04-26",
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:identifier": "https://ror.org/05cq64r17",
          "schema:name": "University of \u0141\u00f3d\u017a",
          "schema:sameAs": [
            "https://ror.org/05cq64r17"
          ]
        },
        "schema:familyName": "Minias",
        "schema:givenName": "Piotr",
        "schema:identifier": "http://orcid.org/0000-0002-7742-6750",
        "schema:name": "Piotr Minias"
      }
    ]
  },
  "schema:citation": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "http://doi.org/10.1086/707720"
    }
  ],
  "schema:conditionsOfAccess": [
    "Open"
  ],
  "schema:description": "Blood oxygen-carrying capacity is one of important determinants of oxygen amounts supplied to the tissues per unit time and plays a key role in oxidative metabolism. In wild vertebrates, blood oxygen-carrying capacity is most commonly measured with the total blood haemoglobin concentration (Hb) and haematocrit (Hct), which is the volume percentage of red blood cells in blood. Here, I used published estimates of avian Hb and Hct (nearly one thousand estimates from 300 species) to examine macroevolutionary patterns in blood oxygen-carrying capacity of blood in birds. Phylogenetically-informed comparative analysis indicated that blood oxygen-carrying capacity was primarily determined by species distribution (latitude and elevation) and morphological constraints (body mass). I found little support for the effect of life history components on blood oxygen-carrying capacity, except for a positive association of Hct with clutch size. Hb was also positively associated with diving\nbehaviour, but I found no effect of migratoriness on either Hb or Hct. Fluctuating selection was identified as the major force shaping the evolution of blood oxygen-carrying capacity. The results offer novel insights into the evolution of Hb and Hct in birds, as well as they provide a general, phylogenetically-robust support for some long-standing hypotheses in avian ecophysiology.",
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "schema:Collection"
      ],
      "schema:contentUrl": "http://datadryad.org/api/v2/datasets/doi%253A10.5061%252Fdryad.p79tm37/download",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "schema:hasPart": [
        {
          "@type": [
            "schema:MediaObject"
          ],
          "schema:name": "Minias RAW DATARaw data for \"Ecology and evolution of blood oxygen-carrying capacity in birds\".",
          "schema:encodingFormat": [
            "application/octet-stream"
          ]
        }
      ]
    }
  ],
  "schema:includedInDataCatalog": [
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:archivedAt": "http://datadryad.org/dataset/doi%253A10.5061%252Fdryad.p79tm37",
      "schema:name": "Dryad Digital Repository (Dryad)",
      "schema:url": "https://datadryad.org",
      "nde:versionDate": "2026-10-01"
    },
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:archivedAt": "https://zenodo.org/records/6496349",
      "schema:name": "Zenodo",
      "schema:url": "https://zenodo.org/",
      "nde:versionDate": "2026-10-02"
    }
  ],
  "schema:isAccessibleForFree": true,
  "schema:keywords": [
    "Evolution: physiological",
    "Physiology: comparative",
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_0610",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Ecology",
      "schema:url": "http://edamontology.org/topic_0610",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_3500",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Zoology",
      "schema:url": "http://edamontology.org/topic_3500",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:name": "GPT-4o-mini",
        "schema:url": "https://openai.com/index/chatgpt"
      },
      "schema:identifier": "topic_3299",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Evolutionary biology",
      "schema:url": "http://edamontology.org/topic_3299",
      "schema:about": "topicCategory"
    },
    {
      "schema:name": "host",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:license": [
    "https://spdx.org/licenses/CC0-1.0.html"
  ],
  "schema:name": "Ecology and evolution of blood oxygen-carrying capacity in birds",
  "schema:spatialCoverage": [
    {
      "@type": [
        "schema:Place",
        "schema:AdministrativeArea"
      ],
      "schema:name": "Global"
    }
  ],
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "birds",
        "avian"
      ],
      "cdifniaid:commonName": "birds",
      "schema:identifier": "8782",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": false,
      "schema:name": "Aves",
      "nde:originalName": "birds",
      "schema:url": "https://www.uniprot.org/taxonomy/8782"
    }
  ],
  "schema:temporalCoverage": [
    "../2022-04-26"
  ],
  "schema:url": "http://datadryad.org/dataset/doi%253A10.5061%252Fdryad.p79tm37",
  "schema:hasPart": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "http://datadryad.org/downloads/file_stream/1462203"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdifniaid: <https://w3id.org/cdif/niaid/terms/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://data.niaid.nih.gov/resources?id=dryad_p79tm37> a schema1:Dataset ;
    schema1:citation [ a schema1:CreativeWork ;
            schema1:url "http://doi.org/10.1086/707720" ] ;
    schema1:conditionsOfAccess "Open" ;
    schema1:creator ( [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:identifier "https://ror.org/05cq64r17" ;
                        schema1:name "University of Łódź" ;
                        schema1:sameAs "https://ror.org/05cq64r17" ] ;
                schema1:familyName "Minias" ;
                schema1:givenName "Piotr" ;
                schema1:identifier "http://orcid.org/0000-0002-7742-6750" ;
                schema1:name "Piotr Minias" ] ) ;
    schema1:dateModified "2022-04-26" ;
    schema1:datePublished "2022-04-26" ;
    schema1:description """Blood oxygen-carrying capacity is one of important determinants of oxygen amounts supplied to the tissues per unit time and plays a key role in oxidative metabolism. In wild vertebrates, blood oxygen-carrying capacity is most commonly measured with the total blood haemoglobin concentration (Hb) and haematocrit (Hct), which is the volume percentage of red blood cells in blood. Here, I used published estimates of avian Hb and Hct (nearly one thousand estimates from 300 species) to examine macroevolutionary patterns in blood oxygen-carrying capacity of blood in birds. Phylogenetically-informed comparative analysis indicated that blood oxygen-carrying capacity was primarily determined by species distribution (latitude and elevation) and morphological constraints (body mass). I found little support for the effect of life history components on blood oxygen-carrying capacity, except for a positive association of Hct with clutch size. Hb was also positively associated with diving
behaviour, but I found no effect of migratoriness on either Hb or Hct. Fluctuating selection was identified as the major force shaping the evolution of blood oxygen-carrying capacity. The results offer novel insights into the evolution of Hb and Hct in birds, as well as they provide a general, phylogenetically-robust support for some long-standing hypotheses in avian ecophysiology.""" ;
    schema1:distribution [ a schema1:Collection,
                schema1:DataDownload ;
            schema1:contentUrl "http://datadryad.org/api/v2/datasets/doi%253A10.5061%252Fdryad.p79tm37/download" ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart [ a schema1:MediaObject ;
                    schema1:encodingFormat "application/octet-stream" ;
                    schema1:name "Minias RAW DATARaw data for \"Ecology and evolution of blood oxygen-carrying capacity in birds\"." ] ] ;
    schema1:hasPart [ a schema1:DataDownload ;
            schema1:contentUrl "http://datadryad.org/downloads/file_stream/1462203" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID <https://registry.identifiers.org/registry/doi> ;
            schema1:url "https://doi.org/10.5061/dryad.p79tm37" ;
            schema1:value "10.5061/dryad.p79tm37" ] ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:archivedAt "https://zenodo.org/records/6496349" ;
            schema1:name "Zenodo" ;
            schema1:url "https://zenodo.org/" ;
            nde:versionDate "2026-10-02" ],
        [ a schema1:DataCatalog ;
            schema1:archivedAt "http://datadryad.org/dataset/doi%253A10.5061%252Fdryad.p79tm37" ;
            schema1:name "Dryad Digital Repository (Dryad)" ;
            schema1:url "https://datadryad.org" ;
            nde:versionDate "2026-10-01" ] ;
    schema1:isAccessibleForFree true ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:about "NIAID classification" ;
            schema1:name "host" ],
        [ a schema1:DefinedTerm ;
            schema1:about "topicCategory" ;
            schema1:identifier "topic_3500" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Zoology" ;
            schema1:url "http://edamontology.org/topic_3500" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:name "GPT-4o-mini" ;
                    schema1:url "https://openai.com/index/chatgpt" ] ],
        [ a schema1:DefinedTerm ;
            schema1:about "topicCategory" ;
            schema1:identifier "topic_3299" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Evolutionary biology" ;
            schema1:url "http://edamontology.org/topic_3299" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:name "GPT-4o-mini" ;
                    schema1:url "https://openai.com/index/chatgpt" ] ],
        [ a schema1:DefinedTerm ;
            schema1:about "topicCategory" ;
            schema1:identifier "topic_0610" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Ecology" ;
            schema1:url "http://edamontology.org/topic_0610" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:name "GPT-4o-mini" ;
                    schema1:url "https://openai.com/index/chatgpt" ] ],
        "Evolution: physiological",
        "Physiology: comparative" ;
    schema1:license "https://spdx.org/licenses/CC0-1.0.html" ;
    schema1:name "Ecology and evolution of blood oxygen-carrying capacity in birds" ;
    schema1:spatialCoverage [ a schema1:AdministrativeArea,
                schema1:Place ;
            schema1:name "Global" ] ;
    schema1:subjectOf <https://data.niaid.nih.gov/resources?id=dryad_p79tm37#metadata> ;
    schema1:temporalCoverage "../2022-04-26" ;
    schema1:url "http://datadryad.org/dataset/doi%253A10.5061%252Fdryad.p79tm37" ;
    nde:date "2022-04-26" ;
    nde:species [ a schema1:DefinedTerm ;
            schema1:alternateName "avian",
                "birds" ;
            schema1:identifier "8782" ;
            schema1:inDefinedTermSet "UniProt" ;
            schema1:name "Aves" ;
            schema1:url "https://www.uniprot.org/taxonomy/8782" ;
            nde:isCurated false ;
            nde:originalName "birds" ;
            cdifniaid:commonName "birds" ] .

<https://data.niaid.nih.gov/resources?id=dryad_p79tm37#metadata> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/discovery/1.1>,
        <https://w3id.org/cdif/manifest/1.1>,
        <https://w3id.org/cdif/niaid/1.0> ;
    schema1:about <https://data.niaid.nih.gov/resources?id=dryad_p79tm37> ;
    schema1:additionalType dcat:CatalogRecord ;
    schema1:description """CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record dryad_p79tm37, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.

Metadata source from EXTRACT.

Metadata source from GPT.""" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "NIAID Data Discovery Portal" ;
            schema1:url "https://data.niaid.nih.gov/" ] ;
    schema1:name "Metadata record for: Ecology and evolution of blood oxygen-carrying capacity in birds" ;
    schema1:sdDatePublished "2026-10-28" .


```


### COVID Rapid Acceleration of Diagnostics (RADx) Data Hub record phs003686
Record phs003686 from COVID Rapid Acceleration of Diagnostics (RADx) Data Hub, as the NIAID Data Discovery Portal API returned it
(converters/NIAID/niaidExamples/phs003686.json), converted by harvest_niaid_to_cdif.py.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "nde": "https://discovery.biothings.io/ns/nde/",
    "bios": "https://bioschemas.org/",
    "time": "http://www.w3.org/2006/time#",
    "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
  },
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=phs003686",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=phs003686"
    },
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=phs003686#metadata",
    "schema:name": "Metadata record for: CO-CREATE-Ex: Community-engaged Optimization of COVID-19 Rapid Evaluation And  TEsting Experiences",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record phs003686, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.",
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.identifiers.org/registry/doi"
    },
    "schema:value": "10.60773/gwn0-p070",
    "schema:url": "https://doi.org/10.60773/gwn0-p070"
  },
  "bios:alternateIdentifier": [
    "phs003686"
  ],
  "schema:dateModified": "2024-06-18",
  "schema:datePublished": "2024-09-13",
  "schema:dateCreated": "2024-06-27",
  "nde:date": "2024-09-13",
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "San Ysidro Health Centers"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:familyName": "Louise Laurent",
        "schema:name": "Louise Laurent, MD/PhD",
        "schema:givenName": "MD/PhD"
      }
    ]
  },
  "schema:conditionsOfAccess": [
    "Restricted",
    "IRB approval required"
  ],
  "schema:description": "The goal of this project was to use a flexible and sustainable approach that promotes responsiveness to both the needs of the community and the changing pandemic context while reducing COVID-19 testing disparities. This project refined, and tested three implementation strategies prioritized by the Community and Scientific Advisory Board (CSAB). These three strategies include: (1) current, walk-up free testing, (2) promotores-led COVID-19 test counseling and preventive care reminders, (3) vending machines that dispense FDA-authorized self-testing kits.",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "NIMHD"
      }
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "2019 novel coronavirus infection",
        "2019-nCoV infection",
        "coronavirus disease 2019",
        "severe acute respiratory syndrome coronavirus 2 infectious disease"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2025-01-15",
        "schema:name": "Biothings API",
        "schema:url": "https://biothings.io/"
      },
      "schema:identifier": "0100096",
      "schema:inDefinedTermSet": "MONDO",
      "nde:isCurated": true,
      "schema:name": "COVID-19",
      "nde:originalName": "COVID-19",
      "schema:url": "http://purl.obolibrary.org/obo/MONDO_0100096"
    }
  ],
  "schema:includedInDataCatalog": [
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:archivedAt": "https://radxdatahub.nih.gov/study/271",
      "schema:name": "COVID Rapid Acceleration of Diagnostics (RADx) Data Hub",
      "schema:url": "https://radxdatahub.nih.gov/",
      "nde:versionDate": "2025-03-26"
    },
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:archivedAt": "https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs003686.v1.p1",
      "schema:name": "NCBI Database of Genotypes and Phenotypes (NCBI dbGaP)",
      "schema:url": "https://www.ncbi.nlm.nih.gov/gap/",
      "nde:versionDate": "2026-10-14"
    }
  ],
  "schema:infectiousAgent": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "2019-nCoV",
        "Wuhan coronavirus",
        "SARS-2",
        "SARS-CoV2",
        "Wuhan seafood market pneumonia virus",
        "HCoV-19",
        "COVID19",
        "COVID-19 virus",
        "Human coronavirus 2019",
        "COVID-19"
      ],
      "cdifniaid:commonName": "2019-nCoV",
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2025-02-09",
        "schema:name": "Data Discovery Engine",
        "schema:url": "https://discovery.biothings.io/"
      },
      "schema:identifier": "2697049",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": true,
      "schema:name": "Severe acute respiratory syndrome coronavirus 2",
      "nde:originalName": "Severe acute respiratory syndrome coronavirus 2",
      "schema:url": "https://www.uniprot.org/taxonomy/2697049"
    }
  ],
  "prov:wasDerivedFrom": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://clinicaltrials.gov/study/NCT05894655"
    }
  ],
  "schema:keywords": [
    "Diagnostic Testing",
    "Community Outreach Programs",
    "Testing Rate or Uptake",
    "At-Home or Over-the-Counter (OTC) Self-Testing",
    {
      "schema:name": "infectiousAgent",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    },
    {
      "schema:name": "host",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:license": [
    "https://sharing.nih.gov/accessing-data/accessing-genomic-data/how-to-request-and-access-datasets-from-dbgap"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "C17176",
      "schema:inDefinedTermSet": "NCIT",
      "nde:isCurated": true,
      "schema:name": "survey",
      "nde:originalName": "Survey",
      "schema:url": "http://purl.obolibrary.org/obo/NCIT_C17176"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "C15208",
      "schema:inDefinedTermSet": "NCIT",
      "nde:isCurated": true,
      "schema:name": "Cohort Study",
      "nde:originalName": "Longitudinal Cohort",
      "schema:url": "http://purl.obolibrary.org/obo/NCIT_C15208"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "C17176",
      "schema:inDefinedTermSet": "NCIT",
      "nde:isCurated": true,
      "schema:name": "survey",
      "nde:originalName": "Questionnaire or Survey",
      "schema:url": "http://purl.obolibrary.org/obo/NCIT_C17176"
    }
  ],
  "schema:name": "CO-CREATE-Ex: Community-engaged Optimization of COVID-19 Rapid Evaluation And  TEsting Experiences",
  "schema:sdPublisher": {
    "@type": [
      "schema:DataCatalog"
    ],
    "schema:name": "RADx-UP"
  },
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Human",
        "Homo sapiens Linnaeus, 1758",
        "human",
        "Home sapiens",
        "Homo sampiens",
        "Homo sapeins",
        "Homo sapian",
        "Homo sapians",
        "Homo sapien",
        "Homo sapience",
        "Homo sapiense",
        "Homo sapients",
        "Homo sapines",
        "Homo spaiens",
        "Homo spiens",
        "Humo sapiens"
      ],
      "cdifniaid:commonName": "Human",
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2023-10-05",
        "schema:name": "PubTator",
        "schema:url": "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html"
      },
      "schema:identifier": "9606",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": true,
      "schema:name": "Homo sapiens",
      "nde:originalName": "homo sapiens",
      "schema:url": "https://www.uniprot.org/taxonomy/9606"
    }
  ],
  "schema:temporalCoverage": [
    {
      "@type": [
        "time:ProperInterval"
      ],
      "time:hasBeginning": {
        "@type": [
          "time:Instant"
        ],
        "time:inXSDDate": "2022-11-01"
      },
      "time:hasEnd": {
        "@type": [
          "time:Instant"
        ],
        "time:inXSDDate": "2024-10-31"
      },
      "schema:description": "nde:temporalType: study date"
    }
  ],
  "schema:url": "https://radxdatahub.nih.gov/study/271",
  "schema:variableMeasured": [
    {
      "@type": [
        "schema:PropertyValue",
        "schema:DefinedTerm"
      ],
      "schema:name": "COVID-19 Test Results"
    },
    {
      "@type": [
        "schema:PropertyValue",
        "schema:DefinedTerm"
      ],
      "schema:name": "Human Data"
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
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataset/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "time": "http://www.w3.org/2006/time#",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=phs003686",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=phs003686"
    },
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=phs003686#metadata",
    "schema:name": "Metadata record for: CO-CREATE-Ex: Community-engaged Optimization of COVID-19 Rapid Evaluation And  TEsting Experiences",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record phs003686, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.",
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.identifiers.org/registry/doi"
    },
    "schema:value": "10.60773/gwn0-p070",
    "schema:url": "https://doi.org/10.60773/gwn0-p070"
  },
  "bios:alternateIdentifier": [
    "phs003686"
  ],
  "schema:dateModified": "2024-06-18",
  "schema:datePublished": "2024-09-13",
  "schema:dateCreated": "2024-06-27",
  "nde:date": "2024-09-13",
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "San Ysidro Health Centers"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:familyName": "Louise Laurent",
        "schema:name": "Louise Laurent, MD/PhD",
        "schema:givenName": "MD/PhD"
      }
    ]
  },
  "schema:conditionsOfAccess": [
    "Restricted",
    "IRB approval required"
  ],
  "schema:description": "The goal of this project was to use a flexible and sustainable approach that promotes responsiveness to both the needs of the community and the changing pandemic context while reducing COVID-19 testing disparities. This project refined, and tested three implementation strategies prioritized by the Community and Scientific Advisory Board (CSAB). These three strategies include: (1) current, walk-up free testing, (2) promotores-led COVID-19 test counseling and preventive care reminders, (3) vending machines that dispense FDA-authorized self-testing kits.",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "NIMHD"
      }
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "2019 novel coronavirus infection",
        "2019-nCoV infection",
        "coronavirus disease 2019",
        "severe acute respiratory syndrome coronavirus 2 infectious disease"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2025-01-15",
        "schema:name": "Biothings API",
        "schema:url": "https://biothings.io/"
      },
      "schema:identifier": "0100096",
      "schema:inDefinedTermSet": "MONDO",
      "nde:isCurated": true,
      "schema:name": "COVID-19",
      "nde:originalName": "COVID-19",
      "schema:url": "http://purl.obolibrary.org/obo/MONDO_0100096"
    }
  ],
  "schema:includedInDataCatalog": [
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:archivedAt": "https://radxdatahub.nih.gov/study/271",
      "schema:name": "COVID Rapid Acceleration of Diagnostics (RADx) Data Hub",
      "schema:url": "https://radxdatahub.nih.gov/",
      "nde:versionDate": "2025-03-26"
    },
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:archivedAt": "https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs003686.v1.p1",
      "schema:name": "NCBI Database of Genotypes and Phenotypes (NCBI dbGaP)",
      "schema:url": "https://www.ncbi.nlm.nih.gov/gap/",
      "nde:versionDate": "2026-10-14"
    }
  ],
  "schema:infectiousAgent": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "2019-nCoV",
        "Wuhan coronavirus",
        "SARS-2",
        "SARS-CoV2",
        "Wuhan seafood market pneumonia virus",
        "HCoV-19",
        "COVID19",
        "COVID-19 virus",
        "Human coronavirus 2019",
        "COVID-19"
      ],
      "cdifniaid:commonName": "2019-nCoV",
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2025-02-09",
        "schema:name": "Data Discovery Engine",
        "schema:url": "https://discovery.biothings.io/"
      },
      "schema:identifier": "2697049",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": true,
      "schema:name": "Severe acute respiratory syndrome coronavirus 2",
      "nde:originalName": "Severe acute respiratory syndrome coronavirus 2",
      "schema:url": "https://www.uniprot.org/taxonomy/2697049"
    }
  ],
  "prov:wasDerivedFrom": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://clinicaltrials.gov/study/NCT05894655"
    }
  ],
  "schema:keywords": [
    "Diagnostic Testing",
    "Community Outreach Programs",
    "Testing Rate or Uptake",
    "At-Home or Over-the-Counter (OTC) Self-Testing",
    {
      "schema:name": "infectiousAgent",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    },
    {
      "schema:name": "host",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:license": [
    "https://sharing.nih.gov/accessing-data/accessing-genomic-data/how-to-request-and-access-datasets-from-dbgap"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "C17176",
      "schema:inDefinedTermSet": "NCIT",
      "nde:isCurated": true,
      "schema:name": "survey",
      "nde:originalName": "Survey",
      "schema:url": "http://purl.obolibrary.org/obo/NCIT_C17176"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "C15208",
      "schema:inDefinedTermSet": "NCIT",
      "nde:isCurated": true,
      "schema:name": "Cohort Study",
      "nde:originalName": "Longitudinal Cohort",
      "schema:url": "http://purl.obolibrary.org/obo/NCIT_C15208"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "C17176",
      "schema:inDefinedTermSet": "NCIT",
      "nde:isCurated": true,
      "schema:name": "survey",
      "nde:originalName": "Questionnaire or Survey",
      "schema:url": "http://purl.obolibrary.org/obo/NCIT_C17176"
    }
  ],
  "schema:name": "CO-CREATE-Ex: Community-engaged Optimization of COVID-19 Rapid Evaluation And  TEsting Experiences",
  "schema:sdPublisher": {
    "@type": [
      "schema:DataCatalog"
    ],
    "schema:name": "RADx-UP"
  },
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Human",
        "Homo sapiens Linnaeus, 1758",
        "human",
        "Home sapiens",
        "Homo sampiens",
        "Homo sapeins",
        "Homo sapian",
        "Homo sapians",
        "Homo sapien",
        "Homo sapience",
        "Homo sapiense",
        "Homo sapients",
        "Homo sapines",
        "Homo spaiens",
        "Homo spiens",
        "Humo sapiens"
      ],
      "cdifniaid:commonName": "Human",
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2023-10-05",
        "schema:name": "PubTator",
        "schema:url": "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html"
      },
      "schema:identifier": "9606",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": true,
      "schema:name": "Homo sapiens",
      "nde:originalName": "homo sapiens",
      "schema:url": "https://www.uniprot.org/taxonomy/9606"
    }
  ],
  "schema:temporalCoverage": [
    {
      "@type": [
        "time:ProperInterval"
      ],
      "time:hasBeginning": {
        "@type": [
          "time:Instant"
        ],
        "time:inXSDDate": "2022-11-01"
      },
      "time:hasEnd": {
        "@type": [
          "time:Instant"
        ],
        "time:inXSDDate": "2024-10-31"
      },
      "schema:description": "nde:temporalType: study date"
    }
  ],
  "schema:url": "https://radxdatahub.nih.gov/study/271",
  "schema:variableMeasured": [
    {
      "@type": [
        "schema:PropertyValue",
        "schema:DefinedTerm"
      ],
      "schema:name": "COVID-19 Test Results"
    },
    {
      "@type": [
        "schema:PropertyValue",
        "schema:DefinedTerm"
      ],
      "schema:name": "Human Data"
    }
  ]
}
```

#### ttl
```ttl
@prefix bios: <https://bioschemas.org/> .
@prefix cdifniaid: <https://w3id.org/cdif/niaid/terms/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://data.niaid.nih.gov/resources?id=phs003686> a schema1:Dataset ;
    schema1:conditionsOfAccess "IRB approval required",
        "Restricted" ;
    schema1:creator ( [ a schema1:Organization ;
                schema1:name "San Ysidro Health Centers" ] [ a schema1:Person ;
                schema1:familyName "Louise Laurent" ;
                schema1:givenName "MD/PhD" ;
                schema1:name "Louise Laurent, MD/PhD" ] ) ;
    schema1:dateCreated "2024-06-27" ;
    schema1:dateModified "2024-06-18" ;
    schema1:datePublished "2024-09-13" ;
    schema1:description "The goal of this project was to use a flexible and sustainable approach that promotes responsiveness to both the needs of the community and the changing pandemic context while reducing COVID-19 testing disparities. This project refined, and tested three implementation strategies prioritized by the Community and Scientific Advisory Board (CSAB). These three strategies include: (1) current, walk-up free testing, (2) promotores-led COVID-19 test counseling and preventive care reminders, (3) vending machines that dispense FDA-authorized self-testing kits." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:funder [ a schema1:Organization ;
                    schema1:name "NIMHD" ] ] ;
    schema1:healthCondition [ a schema1:DefinedTerm ;
            schema1:alternateName "2019 novel coronavirus infection",
                "2019-nCoV infection",
                "coronavirus disease 2019",
                "severe acute respiratory syndrome coronavirus 2 infectious disease" ;
            schema1:identifier "0100096" ;
            schema1:inDefinedTermSet "MONDO" ;
            schema1:name "COVID-19" ;
            schema1:url "http://purl.obolibrary.org/obo/MONDO_0100096" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:dateModified "2025-01-15" ;
                    schema1:name "Biothings API" ;
                    schema1:url "https://biothings.io/" ] ;
            nde:isCurated true ;
            nde:originalName "COVID-19" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID <https://registry.identifiers.org/registry/doi> ;
            schema1:url "https://doi.org/10.60773/gwn0-p070" ;
            schema1:value "10.60773/gwn0-p070" ] ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:archivedAt "https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs003686.v1.p1" ;
            schema1:name "NCBI Database of Genotypes and Phenotypes (NCBI dbGaP)" ;
            schema1:url "https://www.ncbi.nlm.nih.gov/gap/" ;
            nde:versionDate "2026-10-14" ],
        [ a schema1:DataCatalog ;
            schema1:archivedAt "https://radxdatahub.nih.gov/study/271" ;
            schema1:name "COVID Rapid Acceleration of Diagnostics (RADx) Data Hub" ;
            schema1:url "https://radxdatahub.nih.gov/" ;
            nde:versionDate "2025-03-26" ] ;
    schema1:infectiousAgent [ a schema1:DefinedTerm ;
            schema1:alternateName "2019-nCoV",
                "COVID-19",
                "COVID-19 virus",
                "COVID19",
                "HCoV-19",
                "Human coronavirus 2019",
                "SARS-2",
                "SARS-CoV2",
                "Wuhan coronavirus",
                "Wuhan seafood market pneumonia virus" ;
            schema1:identifier "2697049" ;
            schema1:inDefinedTermSet "UniProt" ;
            schema1:name "Severe acute respiratory syndrome coronavirus 2" ;
            schema1:url "https://www.uniprot.org/taxonomy/2697049" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:dateModified "2025-02-09" ;
                    schema1:name "Data Discovery Engine" ;
                    schema1:url "https://discovery.biothings.io/" ] ;
            nde:isCurated true ;
            nde:originalName "Severe acute respiratory syndrome coronavirus 2" ;
            cdifniaid:commonName "2019-nCoV" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:about "NIAID classification" ;
            schema1:name "infectiousAgent" ],
        [ a schema1:DefinedTerm ;
            schema1:about "NIAID classification" ;
            schema1:name "host" ],
        "At-Home or Over-the-Counter (OTC) Self-Testing",
        "Community Outreach Programs",
        "Diagnostic Testing",
        "Testing Rate or Uptake" ;
    schema1:license "https://sharing.nih.gov/accessing-data/accessing-genomic-data/how-to-request-and-access-datasets-from-dbgap" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "C17176" ;
            schema1:inDefinedTermSet "NCIT" ;
            schema1:name "survey" ;
            schema1:url "http://purl.obolibrary.org/obo/NCIT_C17176" ;
            nde:isCurated true ;
            nde:originalName "Survey" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "C15208" ;
            schema1:inDefinedTermSet "NCIT" ;
            schema1:name "Cohort Study" ;
            schema1:url "http://purl.obolibrary.org/obo/NCIT_C15208" ;
            nde:isCurated true ;
            nde:originalName "Longitudinal Cohort" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "C17176" ;
            schema1:inDefinedTermSet "NCIT" ;
            schema1:name "survey" ;
            schema1:url "http://purl.obolibrary.org/obo/NCIT_C17176" ;
            nde:isCurated true ;
            nde:originalName "Questionnaire or Survey" ] ;
    schema1:name "CO-CREATE-Ex: Community-engaged Optimization of COVID-19 Rapid Evaluation And  TEsting Experiences" ;
    schema1:sdPublisher [ a schema1:DataCatalog ;
            schema1:name "RADx-UP" ] ;
    schema1:subjectOf <https://data.niaid.nih.gov/resources?id=phs003686#metadata> ;
    schema1:temporalCoverage [ a time:ProperInterval ;
            schema1:description "nde:temporalType: study date" ;
            time:hasBeginning [ a time:Instant ;
                    time:inXSDDate "2022-11-01" ] ;
            time:hasEnd [ a time:Instant ;
                    time:inXSDDate "2024-10-31" ] ] ;
    schema1:url "https://radxdatahub.nih.gov/study/271" ;
    schema1:variableMeasured [ a schema1:DefinedTerm,
                schema1:PropertyValue ;
            schema1:name "Human Data" ],
        [ a schema1:DefinedTerm,
                schema1:PropertyValue ;
            schema1:name "COVID-19 Test Results" ] ;
    prov:wasDerivedFrom [ a schema1:CreativeWork ;
            schema1:url "https://clinicaltrials.gov/study/NCT05894655" ] ;
    bios:alternateIdentifier "phs003686" ;
    nde:date "2024-09-13" ;
    nde:species [ a schema1:DefinedTerm ;
            schema1:alternateName "Home sapiens",
                "Homo sampiens",
                "Homo sapeins",
                "Homo sapian",
                "Homo sapians",
                "Homo sapien",
                "Homo sapience",
                "Homo sapiens Linnaeus, 1758",
                "Homo sapiense",
                "Homo sapients",
                "Homo sapines",
                "Homo spaiens",
                "Homo spiens",
                "Human",
                "Humo sapiens",
                "human" ;
            schema1:identifier "9606" ;
            schema1:inDefinedTermSet "UniProt" ;
            schema1:name "Homo sapiens" ;
            schema1:url "https://www.uniprot.org/taxonomy/9606" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:dateModified "2023-10-05" ;
                    schema1:name "PubTator" ;
                    schema1:url "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html" ] ;
            nde:isCurated true ;
            nde:originalName "homo sapiens" ;
            cdifniaid:commonName "Human" ] .

<https://data.niaid.nih.gov/resources?id=phs003686#metadata> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/discovery/1.1>,
        <https://w3id.org/cdif/niaid/1.0> ;
    schema1:about <https://data.niaid.nih.gov/resources?id=phs003686> ;
    schema1:additionalType dcat:CatalogRecord ;
    schema1:description "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record phs003686, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them." ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "NIAID Data Discovery Portal" ;
            schema1:url "https://data.niaid.nih.gov/" ] ;
    schema1:name "Metadata record for: CO-CREATE-Ex: Community-engaged Optimization of COVID-19 Rapid Evaluation And  TEsting Experiences" ;
    schema1:sdDatePublished "2026-10-28" .


```


### Electron Microscopy Public Image Archive (EMPIAR) record empiar-10514
Record empiar-10514 from Electron Microscopy Public Image Archive (EMPIAR), as the NIAID Data Discovery Portal API returned it
(converters/NIAID/niaidExamples/empiar-10514.json), converted by harvest_niaid_to_cdif.py.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "nde": "https://discovery.biothings.io/ns/nde/",
    "bios": "https://bioschemas.org/",
    "time": "http://www.w3.org/2006/time#",
    "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
  },
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=empiar-10514",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=empiar-10514"
    },
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record empiar-10514, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.\n\nMetadata source from PMID.",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=empiar-10514#metadata",
    "schema:name": "Metadata record for: Cryo electron microscopy of SARS-CoV-2 stabilized spike in prefusion state",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.identifiers.org/registry/doi"
    },
    "schema:value": "10.6019/EMPIAR-10514",
    "schema:url": "https://doi.org/10.6019/EMPIAR-10514"
  },
  "bios:alternateIdentifier": [
    "EMPIAR-10514"
  ],
  "schema:dateModified": "2022-05-12",
  "schema:datePublished": "2020-09-28",
  "schema:dateCreated": "2020-09-22",
  "nde:date": "2022-05-12",
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Centro Nacional de Biotecnologia"
        },
        "schema:email": "carazo [at] cnb.csic.es",
        "schema:familyName": "Carazo",
        "schema:givenName": "Jose Maria",
        "schema:name": "Jose Maria Carazo"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Centro Nacional de Biotecnologia"
        },
        "schema:familyName": "Carazo",
        "schema:givenName": "Jose Maria",
        "schema:name": "Jose Maria Carazo"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:identifier": "0000-0001-9062-931X",
        "schema:name": "Carazo JM",
        "schema:url": "https://orcid.org/0000-0001-9062-931X"
      }
    ]
  },
  "schema:citation": [
    {
      "@type": [
        "schema:ScholarlyArticle"
      ],
      "schema:author": [
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Melero R"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Sorzano COS"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Foster B"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Vilas JL"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Martínez M"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Marabini R"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Ramírez-Aportela E"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Sanchez-Garcia R"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Herreros D"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Del Caño L"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Losana P"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Fonseca-Reyna YC"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Conesa P"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Wrapp D"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Chacon P"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "McLellan JS"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Tagare HD"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Carazo JM"
        }
      ],
      "schema:datePublished": "2020",
      "nde:doi": "10.1107/s2052252520012725",
      "schema:issueNumber": "Pt 6",
      "nde:journalName": "IUCrJ",
      "nde:journalNameAbbrev": "IUCrJ",
      "schema:name": "Continuous flexibility analysis of SARS-CoV-2 spike prefusion structures",
      "nde:pmid": "33063791",
      "schema:url": "https://doi.org/10.1107/s2052252520012725",
      "schema:volumeNumber": "7"
    },
    {
      "@type": [
        "schema:ScholarlyArticle"
      ],
      "schema:author": [
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Melero R"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Sorzano COS"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Foster B"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Vilas JL"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Martinez M"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Marabini R"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Ramirez-Aportela E"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Sanchez-Garcia R"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Herreros D"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Del Cano L"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Losana P"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Fonseca-Reyna YC"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Conesa P"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Wrapp D"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Chacon P"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "McLellan JS"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Tagare HD"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Carazo JM"
        }
      ],
      "schema:datePublished": "2020-09-29",
      "schema:identifier": "PMID:33063791",
      "nde:journalName": "IUCrJ",
      "schema:name": "Continuous flexibility analysis of SARS-CoV-2 spike prefusion structures.",
      "nde:pmid": "33063791",
      "schema:url": "https://pubmed.ncbi.nlm.nih.gov/33063791/"
    }
  ],
  "schema:conditionsOfAccess": [
    "Open"
  ],
  "schema:creativeWorkStatus": "Active",
  "schema:description": "302.outputMovies data/SARS-CoV-2-spike-prefusion/workflow.json",
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentSize": "865.0 GB",
      "schema:contentUrl": "http://www.opengis.net/def/nil/OGC/0/missing",
      "schema:encodingFormat": [
        "TIFF"
      ]
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:endDate": "2017-12-31",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "National Institute of Allergy & Infectious Diseases",
          "NIAID",
          "Instituto Nacional de Alergias y Enfermedades Infecciosas"
        ],
        "schema:employee": [
          {
            "@type": [
              "schema:Person"
            ],
            "schema:familyName": "PLIMACK",
            "schema:givenName": "MARY",
            "schema:name": "MARY PLIMACK"
          }
        ],
        "schema:identifier": "https://ror.org/043z4tv69",
        "schema:name": "National Institute of Allergy and Infectious Diseases",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "1R01AI127521-01A1"
      },
      "schema:name": "Structure, Function and Antigenicity of Coronavirus Spike Proteins",
      "schema:startDate": "2017-02-09",
      "schema:url": "https://reporter.nih.gov/project-details/9328799"
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:endDate": "2022-02-28",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "NIGMS",
          "U.S. National Institute of General Medical Sciences"
        ],
        "schema:employee": [
          {
            "@type": [
              "schema:Person"
            ],
            "schema:familyName": "SAMMAK",
            "schema:givenName": "PAUL",
            "schema:name": "PAUL SAMMAK"
          }
        ],
        "schema:identifier": "https://ror.org/04q48ey07",
        "schema:name": "National Institute of General Medical Sciences",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "1R01GM125769-01"
      },
      "schema:name": "Principal subspace analysis of cryo-EM heterogeneity",
      "schema:startDate": "2018-03-01",
      "schema:url": "https://reporter.nih.gov/project-details/9419436"
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "sarscov2",
        "sars-cov-2 measurement",
        "severe acute resp syndrome coronavirus 2",
        "severe acute respiratory syndrome coronavirus 2",
        "severe acute respiratory syndrome coronavirus 2 measurement",
        "sars-cov-2"
      ],
      "schema:identifier": "C171532",
      "schema:inDefinedTermSet": "NCIT",
      "nde:isCurated": false,
      "schema:name": "Severe Acute Respiratory Syndrome Coronavirus 2 Measurement",
      "schema:url": "http://purl.obolibrary.org/obo/NCIT_C171532"
    }
  ],
  "schema:inLanguage": "English",
  "schema:includedInDataCatalog": [
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:alternateName": "EMPIAR",
      "schema:archivedAt": "https://www.ebi.ac.uk/empiar/EMPIAR-10514/",
      "schema:identifier": "EMPIAR",
      "schema:name": "Electron Microscopy Public Image Archive (EMPIAR)",
      "schema:url": "https://www.ebi.ac.uk/empiar/"
    },
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:archivedAt": "https://www.omicsdi.org/dataset/biostudies-other/EMPIAR-10514",
      "schema:name": "Omics Discovery Index (OmicsDI)",
      "schema:url": "https://www.omicsdi.org/",
      "nde:versionDate": "2026-10-22"
    }
  ],
  "schema:infectiousAgent": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "2019-nCoV",
        "Wuhan coronavirus",
        "Human coronavirus 2019",
        "COVID-19 virus",
        "SARS-2",
        "HCoV-19",
        "SARS-CoV2",
        "Wuhan seafood market pneumonia virus",
        "COVID-19",
        "COVID19"
      ],
      "cdifniaid:commonName": "2019-nCoV",
      "schema:identifier": "2697049",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": false,
      "schema:name": "Severe acute respiratory syndrome coronavirus 2",
      "schema:url": "https://www.uniprot.org/taxonomy/2697049"
    }
  ],
  "schema:isAccessibleForFree": true,
  "prov:wasDerivedFrom": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ftp.ebi.ac.uk/empiar/world_availability/10514/data/SARS-CoV-2-spike-prefusion/workflow.json",
      "schema:name": "Workflow"
    }
  ],
  "nde:isBasisFor": [
    {
      "@type": [
        "schema:Thing"
      ],
      "schema:identifier": [
        "EMD-11341"
      ],
      "schema:includedInDataCatalog": {
        "@type": [
          "schema:DataCatalog"
        ],
        "schema:name": "Electron Microscopy Data Bank (EMDB)",
        "schema:url": "https://www.ebi.ac.uk/emdb"
      }
    }
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "related to",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:url": "https://doi.org/10.6019/EMPIAR-10514']"
      }
    }
  ],
  "schema:keywords": [
    "EMDB",
    "micrographs - multiframe",
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "topic_0611",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Electron microscopy",
      "schema:url": "http://edamontology.org/topic_0611",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "topic_1317",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Structural biology",
      "schema:url": "http://edamontology.org/topic_1317",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "topic_3383",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Bioimaging",
      "schema:url": "http://edamontology.org/topic_3383",
      "schema:about": "topicCategory"
    },
    {
      "schema:name": "infectiousAgent",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "CHMO_0000068",
      "schema:inDefinedTermSet": "CHMO",
      "schema:name": "electron microscopy",
      "schema:url": "http://purl.obolibrary.org/obo/CHMO_0000068"
    }
  ],
  "schema:name": "Cryo electron microscopy of SARS-CoV-2 stabilized spike in prefusion state",
  "schema:sameAs": [
    "https://doi.org/10.6019/EMPIAR-10514"
  ],
  "schema:sdPublisher": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "biostudies-other",
    "schema:url": "https://www.omicsdi.org/dataset/biostudies-other/EMPIAR-10514"
  },
  "schema:url": "https://www.ebi.ac.uk/empiar/EMPIAR-10514/"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataset/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "time": "http://www.w3.org/2006/time#",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=empiar-10514",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=empiar-10514"
    },
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record empiar-10514, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.\n\nMetadata source from PMID.",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=empiar-10514#metadata",
    "schema:name": "Metadata record for: Cryo electron microscopy of SARS-CoV-2 stabilized spike in prefusion state",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.identifiers.org/registry/doi"
    },
    "schema:value": "10.6019/EMPIAR-10514",
    "schema:url": "https://doi.org/10.6019/EMPIAR-10514"
  },
  "bios:alternateIdentifier": [
    "EMPIAR-10514"
  ],
  "schema:dateModified": "2022-05-12",
  "schema:datePublished": "2020-09-28",
  "schema:dateCreated": "2020-09-22",
  "nde:date": "2022-05-12",
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Centro Nacional de Biotecnologia"
        },
        "schema:email": "carazo [at] cnb.csic.es",
        "schema:familyName": "Carazo",
        "schema:givenName": "Jose Maria",
        "schema:name": "Jose Maria Carazo"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Centro Nacional de Biotecnologia"
        },
        "schema:familyName": "Carazo",
        "schema:givenName": "Jose Maria",
        "schema:name": "Jose Maria Carazo"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:identifier": "0000-0001-9062-931X",
        "schema:name": "Carazo JM",
        "schema:url": "https://orcid.org/0000-0001-9062-931X"
      }
    ]
  },
  "schema:citation": [
    {
      "@type": [
        "schema:ScholarlyArticle"
      ],
      "schema:author": [
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Melero R"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Sorzano COS"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Foster B"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Vilas JL"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Mart\u00ednez M"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Marabini R"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Ram\u00edrez-Aportela E"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Sanchez-Garcia R"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Herreros D"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Del Ca\u00f1o L"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Losana P"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Fonseca-Reyna YC"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Conesa P"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Wrapp D"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Chacon P"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "McLellan JS"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Tagare HD"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Carazo JM"
        }
      ],
      "schema:datePublished": "2020",
      "nde:doi": "10.1107/s2052252520012725",
      "schema:issueNumber": "Pt 6",
      "nde:journalName": "IUCrJ",
      "nde:journalNameAbbrev": "IUCrJ",
      "schema:name": "Continuous flexibility analysis of SARS-CoV-2 spike prefusion structures",
      "nde:pmid": "33063791",
      "schema:url": "https://doi.org/10.1107/s2052252520012725",
      "schema:volumeNumber": "7"
    },
    {
      "@type": [
        "schema:ScholarlyArticle"
      ],
      "schema:author": [
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Melero R"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Sorzano COS"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Foster B"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Vilas JL"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Martinez M"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Marabini R"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Ramirez-Aportela E"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Sanchez-Garcia R"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Herreros D"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Del Cano L"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Losana P"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Fonseca-Reyna YC"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Conesa P"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Wrapp D"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Chacon P"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "McLellan JS"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Tagare HD"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Carazo JM"
        }
      ],
      "schema:datePublished": "2020-09-29",
      "schema:identifier": "PMID:33063791",
      "nde:journalName": "IUCrJ",
      "schema:name": "Continuous flexibility analysis of SARS-CoV-2 spike prefusion structures.",
      "nde:pmid": "33063791",
      "schema:url": "https://pubmed.ncbi.nlm.nih.gov/33063791/"
    }
  ],
  "schema:conditionsOfAccess": [
    "Open"
  ],
  "schema:creativeWorkStatus": "Active",
  "schema:description": "302.outputMovies data/SARS-CoV-2-spike-prefusion/workflow.json",
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentSize": "865.0 GB",
      "schema:contentUrl": "http://www.opengis.net/def/nil/OGC/0/missing",
      "schema:encodingFormat": [
        "TIFF"
      ]
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:endDate": "2017-12-31",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "National Institute of Allergy & Infectious Diseases",
          "NIAID",
          "Instituto Nacional de Alergias y Enfermedades Infecciosas"
        ],
        "schema:employee": [
          {
            "@type": [
              "schema:Person"
            ],
            "schema:familyName": "PLIMACK",
            "schema:givenName": "MARY",
            "schema:name": "MARY PLIMACK"
          }
        ],
        "schema:identifier": "https://ror.org/043z4tv69",
        "schema:name": "National Institute of Allergy and Infectious Diseases",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "1R01AI127521-01A1"
      },
      "schema:name": "Structure, Function and Antigenicity of Coronavirus Spike Proteins",
      "schema:startDate": "2017-02-09",
      "schema:url": "https://reporter.nih.gov/project-details/9328799"
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:endDate": "2022-02-28",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "NIGMS",
          "U.S. National Institute of General Medical Sciences"
        ],
        "schema:employee": [
          {
            "@type": [
              "schema:Person"
            ],
            "schema:familyName": "SAMMAK",
            "schema:givenName": "PAUL",
            "schema:name": "PAUL SAMMAK"
          }
        ],
        "schema:identifier": "https://ror.org/04q48ey07",
        "schema:name": "National Institute of General Medical Sciences",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "1R01GM125769-01"
      },
      "schema:name": "Principal subspace analysis of cryo-EM heterogeneity",
      "schema:startDate": "2018-03-01",
      "schema:url": "https://reporter.nih.gov/project-details/9419436"
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "sarscov2",
        "sars-cov-2 measurement",
        "severe acute resp syndrome coronavirus 2",
        "severe acute respiratory syndrome coronavirus 2",
        "severe acute respiratory syndrome coronavirus 2 measurement",
        "sars-cov-2"
      ],
      "schema:identifier": "C171532",
      "schema:inDefinedTermSet": "NCIT",
      "nde:isCurated": false,
      "schema:name": "Severe Acute Respiratory Syndrome Coronavirus 2 Measurement",
      "schema:url": "http://purl.obolibrary.org/obo/NCIT_C171532"
    }
  ],
  "schema:inLanguage": "English",
  "schema:includedInDataCatalog": [
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:alternateName": "EMPIAR",
      "schema:archivedAt": "https://www.ebi.ac.uk/empiar/EMPIAR-10514/",
      "schema:identifier": "EMPIAR",
      "schema:name": "Electron Microscopy Public Image Archive (EMPIAR)",
      "schema:url": "https://www.ebi.ac.uk/empiar/"
    },
    {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:archivedAt": "https://www.omicsdi.org/dataset/biostudies-other/EMPIAR-10514",
      "schema:name": "Omics Discovery Index (OmicsDI)",
      "schema:url": "https://www.omicsdi.org/",
      "nde:versionDate": "2026-10-22"
    }
  ],
  "schema:infectiousAgent": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "2019-nCoV",
        "Wuhan coronavirus",
        "Human coronavirus 2019",
        "COVID-19 virus",
        "SARS-2",
        "HCoV-19",
        "SARS-CoV2",
        "Wuhan seafood market pneumonia virus",
        "COVID-19",
        "COVID19"
      ],
      "cdifniaid:commonName": "2019-nCoV",
      "schema:identifier": "2697049",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": false,
      "schema:name": "Severe acute respiratory syndrome coronavirus 2",
      "schema:url": "https://www.uniprot.org/taxonomy/2697049"
    }
  ],
  "schema:isAccessibleForFree": true,
  "prov:wasDerivedFrom": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ftp.ebi.ac.uk/empiar/world_availability/10514/data/SARS-CoV-2-spike-prefusion/workflow.json",
      "schema:name": "Workflow"
    }
  ],
  "nde:isBasisFor": [
    {
      "@type": [
        "schema:Thing"
      ],
      "schema:identifier": [
        "EMD-11341"
      ],
      "schema:includedInDataCatalog": {
        "@type": [
          "schema:DataCatalog"
        ],
        "schema:name": "Electron Microscopy Data Bank (EMDB)",
        "schema:url": "https://www.ebi.ac.uk/emdb"
      }
    }
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "related to",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:url": "https://doi.org/10.6019/EMPIAR-10514']"
      }
    }
  ],
  "schema:keywords": [
    "EMDB",
    "micrographs - multiframe",
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "topic_0611",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Electron microscopy",
      "schema:url": "http://edamontology.org/topic_0611",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "topic_1317",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Structural biology",
      "schema:url": "http://edamontology.org/topic_1317",
      "schema:about": "topicCategory"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "topic_3383",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Bioimaging",
      "schema:url": "http://edamontology.org/topic_3383",
      "schema:about": "topicCategory"
    },
    {
      "schema:name": "infectiousAgent",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "CHMO_0000068",
      "schema:inDefinedTermSet": "CHMO",
      "schema:name": "electron microscopy",
      "schema:url": "http://purl.obolibrary.org/obo/CHMO_0000068"
    }
  ],
  "schema:name": "Cryo electron microscopy of SARS-CoV-2 stabilized spike in prefusion state",
  "schema:sameAs": [
    "https://doi.org/10.6019/EMPIAR-10514"
  ],
  "schema:sdPublisher": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "biostudies-other",
    "schema:url": "https://www.omicsdi.org/dataset/biostudies-other/EMPIAR-10514"
  },
  "schema:url": "https://www.ebi.ac.uk/empiar/EMPIAR-10514/"
}
```

#### ttl
```ttl
@prefix bios: <https://bioschemas.org/> .
@prefix cdifniaid: <https://w3id.org/cdif/niaid/terms/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://data.niaid.nih.gov/resources?id=empiar-10514> a schema1:Dataset ;
    schema1:citation [ a schema1:ScholarlyArticle ;
            schema1:author [ a schema1:Person ;
                    schema1:name "McLellan JS" ],
                [ a schema1:Person ;
                    schema1:name "Fonseca-Reyna YC" ],
                [ a schema1:Person ;
                    schema1:name "Sorzano COS" ],
                [ a schema1:Person ;
                    schema1:name "Vilas JL" ],
                [ a schema1:Person ;
                    schema1:name "Wrapp D" ],
                [ a schema1:Person ;
                    schema1:name "Tagare HD" ],
                [ a schema1:Person ;
                    schema1:name "Herreros D" ],
                [ a schema1:Person ;
                    schema1:name "Marabini R" ],
                [ a schema1:Person ;
                    schema1:name "Ramírez-Aportela E" ],
                [ a schema1:Person ;
                    schema1:name "Chacon P" ],
                [ a schema1:Person ;
                    schema1:name "Sanchez-Garcia R" ],
                [ a schema1:Person ;
                    schema1:name "Melero R" ],
                [ a schema1:Person ;
                    schema1:name "Carazo JM" ],
                [ a schema1:Person ;
                    schema1:name "Del Caño L" ],
                [ a schema1:Person ;
                    schema1:name "Losana P" ],
                [ a schema1:Person ;
                    schema1:name "Foster B" ],
                [ a schema1:Person ;
                    schema1:name "Martínez M" ],
                [ a schema1:Person ;
                    schema1:name "Conesa P" ] ;
            schema1:datePublished "2020" ;
            schema1:issueNumber "Pt 6" ;
            schema1:name "Continuous flexibility analysis of SARS-CoV-2 spike prefusion structures" ;
            schema1:url "https://doi.org/10.1107/s2052252520012725" ;
            schema1:volumeNumber "7" ;
            nde:doi "10.1107/s2052252520012725" ;
            nde:journalName "IUCrJ" ;
            nde:journalNameAbbrev "IUCrJ" ;
            nde:pmid "33063791" ],
        [ a schema1:ScholarlyArticle ;
            schema1:author [ a schema1:Person ;
                    schema1:name "Tagare HD" ],
                [ a schema1:Person ;
                    schema1:name "Del Cano L" ],
                [ a schema1:Person ;
                    schema1:name "McLellan JS" ],
                [ a schema1:Person ;
                    schema1:name "Fonseca-Reyna YC" ],
                [ a schema1:Person ;
                    schema1:name "Wrapp D" ],
                [ a schema1:Person ;
                    schema1:name "Foster B" ],
                [ a schema1:Person ;
                    schema1:name "Melero R" ],
                [ a schema1:Person ;
                    schema1:name "Carazo JM" ],
                [ a schema1:Person ;
                    schema1:name "Marabini R" ],
                [ a schema1:Person ;
                    schema1:name "Conesa P" ],
                [ a schema1:Person ;
                    schema1:name "Chacon P" ],
                [ a schema1:Person ;
                    schema1:name "Martinez M" ],
                [ a schema1:Person ;
                    schema1:name "Losana P" ],
                [ a schema1:Person ;
                    schema1:name "Sanchez-Garcia R" ],
                [ a schema1:Person ;
                    schema1:name "Herreros D" ],
                [ a schema1:Person ;
                    schema1:name "Vilas JL" ],
                [ a schema1:Person ;
                    schema1:name "Ramirez-Aportela E" ],
                [ a schema1:Person ;
                    schema1:name "Sorzano COS" ] ;
            schema1:datePublished "2020-09-29" ;
            schema1:identifier "PMID:33063791" ;
            schema1:name "Continuous flexibility analysis of SARS-CoV-2 spike prefusion structures." ;
            schema1:url "https://pubmed.ncbi.nlm.nih.gov/33063791/" ;
            nde:journalName "IUCrJ" ;
            nde:pmid "33063791" ] ;
    schema1:conditionsOfAccess "Open" ;
    schema1:creativeWorkStatus "Active" ;
    schema1:creator ( [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "Centro Nacional de Biotecnologia" ] ;
                schema1:email "carazo [at] cnb.csic.es" ;
                schema1:familyName "Carazo" ;
                schema1:givenName "Jose Maria" ;
                schema1:name "Jose Maria Carazo" ] [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "Centro Nacional de Biotecnologia" ] ;
                schema1:familyName "Carazo" ;
                schema1:givenName "Jose Maria" ;
                schema1:name "Jose Maria Carazo" ] [ a schema1:Person ;
                schema1:identifier "0000-0001-9062-931X" ;
                schema1:name "Carazo JM" ;
                schema1:url "https://orcid.org/0000-0001-9062-931X" ] ) ;
    schema1:dateCreated "2020-09-22" ;
    schema1:dateModified "2022-05-12" ;
    schema1:datePublished "2020-09-28" ;
    schema1:description "302.outputMovies data/SARS-CoV-2-spike-prefusion/workflow.json" ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentSize "865.0 GB" ;
            schema1:contentUrl "http://www.opengis.net/def/nil/OGC/0/missing" ;
            schema1:encodingFormat "TIFF" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:endDate "2022-02-28" ;
            schema1:funder [ a schema1:Organization ;
                    schema1:alternateName "NIGMS",
                        "U.S. National Institute of General Medical Sciences" ;
                    schema1:employee [ a schema1:Person ;
                            schema1:familyName "SAMMAK" ;
                            schema1:givenName "PAUL" ;
                            schema1:name "PAUL SAMMAK" ] ;
                    schema1:identifier "https://ror.org/04q48ey07" ;
                    schema1:name "National Institute of General Medical Sciences" ;
                    schema1:parentOrganization "National Institutes of Health" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:value "1R01GM125769-01" ] ;
            schema1:name "Principal subspace analysis of cryo-EM heterogeneity" ;
            schema1:startDate "2018-03-01" ;
            schema1:url "https://reporter.nih.gov/project-details/9419436" ],
        [ a schema1:MonetaryGrant ;
            schema1:endDate "2017-12-31" ;
            schema1:funder [ a schema1:Organization ;
                    schema1:alternateName "Instituto Nacional de Alergias y Enfermedades Infecciosas",
                        "NIAID",
                        "National Institute of Allergy & Infectious Diseases" ;
                    schema1:employee [ a schema1:Person ;
                            schema1:familyName "PLIMACK" ;
                            schema1:givenName "MARY" ;
                            schema1:name "MARY PLIMACK" ] ;
                    schema1:identifier "https://ror.org/043z4tv69" ;
                    schema1:name "National Institute of Allergy and Infectious Diseases" ;
                    schema1:parentOrganization "National Institutes of Health" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:value "1R01AI127521-01A1" ] ;
            schema1:name "Structure, Function and Antigenicity of Coronavirus Spike Proteins" ;
            schema1:startDate "2017-02-09" ;
            schema1:url "https://reporter.nih.gov/project-details/9328799" ] ;
    schema1:healthCondition [ a schema1:DefinedTerm ;
            schema1:alternateName "sars-cov-2",
                "sars-cov-2 measurement",
                "sarscov2",
                "severe acute resp syndrome coronavirus 2",
                "severe acute respiratory syndrome coronavirus 2",
                "severe acute respiratory syndrome coronavirus 2 measurement" ;
            schema1:identifier "C171532" ;
            schema1:inDefinedTermSet "NCIT" ;
            schema1:name "Severe Acute Respiratory Syndrome Coronavirus 2 Measurement" ;
            schema1:url "http://purl.obolibrary.org/obo/NCIT_C171532" ;
            nde:isCurated false ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID <https://registry.identifiers.org/registry/doi> ;
            schema1:url "https://doi.org/10.6019/EMPIAR-10514" ;
            schema1:value "10.6019/EMPIAR-10514" ] ;
    schema1:inLanguage "English" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:archivedAt "https://www.omicsdi.org/dataset/biostudies-other/EMPIAR-10514" ;
            schema1:name "Omics Discovery Index (OmicsDI)" ;
            schema1:url "https://www.omicsdi.org/" ;
            nde:versionDate "2026-10-22" ],
        [ a schema1:DataCatalog ;
            schema1:alternateName "EMPIAR" ;
            schema1:archivedAt "https://www.ebi.ac.uk/empiar/EMPIAR-10514/" ;
            schema1:identifier "EMPIAR" ;
            schema1:name "Electron Microscopy Public Image Archive (EMPIAR)" ;
            schema1:url "https://www.ebi.ac.uk/empiar/" ] ;
    schema1:infectiousAgent [ a schema1:DefinedTerm ;
            schema1:alternateName "2019-nCoV",
                "COVID-19",
                "COVID-19 virus",
                "COVID19",
                "HCoV-19",
                "Human coronavirus 2019",
                "SARS-2",
                "SARS-CoV2",
                "Wuhan coronavirus",
                "Wuhan seafood market pneumonia virus" ;
            schema1:identifier "2697049" ;
            schema1:inDefinedTermSet "UniProt" ;
            schema1:name "Severe acute respiratory syndrome coronavirus 2" ;
            schema1:url "https://www.uniprot.org/taxonomy/2697049" ;
            nde:isCurated false ;
            cdifniaid:commonName "2019-nCoV" ] ;
    schema1:isAccessibleForFree true ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:about "topicCategory" ;
            schema1:identifier "topic_0611" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Electron microscopy" ;
            schema1:url "http://edamontology.org/topic_0611" ],
        [ a schema1:DefinedTerm ;
            schema1:about "topicCategory" ;
            schema1:identifier "topic_3383" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Bioimaging" ;
            schema1:url "http://edamontology.org/topic_3383" ],
        [ a schema1:DefinedTerm ;
            schema1:about "NIAID classification" ;
            schema1:name "infectiousAgent" ],
        [ a schema1:DefinedTerm ;
            schema1:about "topicCategory" ;
            schema1:identifier "topic_1317" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Structural biology" ;
            schema1:url "http://edamontology.org/topic_1317" ],
        "EMDB",
        "micrographs - multiframe" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "CHMO_0000068" ;
            schema1:inDefinedTermSet "CHMO" ;
            schema1:name "electron microscopy" ;
            schema1:url "http://purl.obolibrary.org/obo/CHMO_0000068" ] ;
    schema1:name "Cryo electron microscopy of SARS-CoV-2 stabilized spike in prefusion state" ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "related to" ;
            schema1:target [ a schema1:EntryPoint ;
                    schema1:url "https://doi.org/10.6019/EMPIAR-10514']" ] ] ;
    schema1:sameAs "https://doi.org/10.6019/EMPIAR-10514" ;
    schema1:sdPublisher [ a schema1:Organization ;
            schema1:name "biostudies-other" ;
            schema1:url "https://www.omicsdi.org/dataset/biostudies-other/EMPIAR-10514" ] ;
    schema1:subjectOf <https://data.niaid.nih.gov/resources?id=empiar-10514#metadata> ;
    schema1:url "https://www.ebi.ac.uk/empiar/EMPIAR-10514/" ;
    prov:wasDerivedFrom [ a schema1:CreativeWork ;
            schema1:name "Workflow" ;
            schema1:url "https://ftp.ebi.ac.uk/empiar/world_availability/10514/data/SARS-CoV-2-spike-prefusion/workflow.json" ] ;
    bios:alternateIdentifier "EMPIAR-10514" ;
    nde:date "2022-05-12" ;
    nde:isBasisFor [ a schema1:Thing ;
            schema1:identifier "EMD-11341" ;
            schema1:includedInDataCatalog [ a schema1:DataCatalog ;
                    schema1:name "Electron Microscopy Data Bank (EMDB)" ;
                    schema1:url "https://www.ebi.ac.uk/emdb" ] ] .

<https://data.niaid.nih.gov/resources?id=empiar-10514#metadata> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/discovery/1.1>,
        <https://w3id.org/cdif/niaid/1.0> ;
    schema1:about <https://data.niaid.nih.gov/resources?id=empiar-10514> ;
    schema1:additionalType dcat:CatalogRecord ;
    schema1:description """CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record empiar-10514, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.

Metadata source from PMID.""" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "NIAID Data Discovery Portal" ;
            schema1:url "https://data.niaid.nih.gov/" ] ;
    schema1:name "Metadata record for: Cryo electron microscopy of SARS-CoV-2 stabilized spike in prefusion state" ;
    schema1:sdDatePublished "2026-10-28" .


```


### Human Cell Atlas (HCA) record hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143
Record hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143 from Human Cell Atlas (HCA), as the NIAID Data Discovery Portal API returned it
(converters/NIAID/niaidExamples/hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143.json), converted by harvest_niaid_to_cdif.py.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "nde": "https://discovery.biothings.io/ns/nde/",
    "bios": "https://bioschemas.org/",
    "time": "http://www.w3.org/2006/time#",
    "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
  },
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143"
    },
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.\n\nMetadata source from PMID.",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143#metadata",
    "schema:name": "Metadata record for: Single Cell RNA-Sequencing of Human Limb Skeletal Muscle across Development and Myogenic Culture from Pluripotent Stem C",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": "https://data.niaid.nih.gov/resources?id=hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143",
  "schema:dateModified": "2025-02-14",
  "schema:datePublished": "2021-04-27",
  "nde:date": "2025-02-14",
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "University of California, Los Angeles, Pyle"
        },
        "schema:familyName": "Xi",
        "schema:givenName": "Haibin",
        "schema:name": "Haibin Xi"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "University of California, Santa Cruz, Human Cell Atlas Data Coordination Platform"
        },
        "schema:familyName": "Nejad",
        "schema:givenName": "Parisa",
        "schema:name": "Parisa Nejad"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "University of California, Santa Cruz, Human Cell Atlas Data Coordination Platform"
        },
        "schema:familyName": "Schwartz",
        "schema:givenName": "Rachel",
        "schema:name": "Rachel Schwartz"
      }
    ]
  },
  "schema:citation": [
    {
      "@type": [
        "schema:ScholarlyArticle"
      ],
      "nde:doi": "doi: 10.1016/j.stem.2020.06.006",
      "schema:name": "A Human Skeletal Muscle Atlas Identifies the Trajectories of Stem and Progenitor Cells across Development and from Human Pluripotent Stem Cells",
      "schema:url": "https://pubmed.ncbi.nlm.nih.gov/32619514/"
    },
    {
      "@type": [
        "schema:ScholarlyArticle"
      ],
      "schema:author": [
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Xi H"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Langerman J"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Sabri S"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Chien P"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Young CS"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Younesi S"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Hicks M"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Gonzalez K"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Fujiwara W"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Marzi J"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Liebscher S"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Spencer M"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Van Handel B"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Evseenko D"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Schenke-Layland K"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Plath K"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Pyle AD"
        }
      ],
      "schema:datePublished": "2020-07-02",
      "schema:identifier": "PMID:32619514",
      "nde:journalName": "Cell stem cell",
      "schema:name": "A Human Skeletal Muscle Atlas Identifies the Trajectories of Stem and Progenitor Cells across Development and from Human Pluripotent Stem Cells.",
      "nde:pmid": "32619514",
      "schema:url": "https://pubmed.ncbi.nlm.nih.gov/32619514/"
    }
  ],
  "schema:description": "The developmental trajectory of human skeletal myogenesis and the transition between progenitor and stem cell states are unclear. To address this, we employed single cell RNA-sequencing to profile human skeletal muscle tissues from embryonic, fetal and postnatal stages. In silico, we identified myogenic as well as other cell types and constructed a “roadmap” of human skeletal muscle ontogeny across development. In a similar fashion, we also profiled the heterogeneous cell cultures generated from multiple human pluripotent stem cell (hPSC) myogenic differentiation protocols, and mapped hPSC-derived myogenic progenitors to an embryonic-to-fetal transition period. Additionally, we found differentially enriched biological processes and discovered co-regulated gene networks and transcription factors present at distinct myogenic stages. In summary, this work serves as a resource for advancing our knowledge of human myogenesis. It also provides a tool for better characterization and understanding of hPSC-derived myogenic progenitors for translational applications in skeletal muscle based regenerative medicine.",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:endDate": "2018-08-31",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "NIAMS",
          "Instituto Nacional de Artritis y Enfermedades Musculoesqueléticas y de la Piel",
          "NIH/National Institute of Arthritis and Musculoskeletal and Skin Diseases",
          "National Institute of Arthritis & Musculoskeletal & Skin Diseases",
          "The National Institute of Arthritis and Musculoskeletal and Skin Diseases",
          "NIH National Institute of Arthritis and Musculoskeletal and Skin Diseases"
        ],
        "schema:identifier": "https://ror.org/006zn3t30",
        "schema:name": "National Institute of Arthritis and Musculoskeletal and Skin Diseases",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "1R01AR064327-01A1"
      },
      "schema:name": "Reprogramming and Directed Differentiation of Skeletal Muscle Cells from hPSCs.",
      "cdifniaid:projectNumSplit": {
        "cdifniaid:activityCode": "R01",
        "cdifniaid:applTypeCode": "1",
        "cdifniaid:fullSupportYear": "01A1",
        "cdifniaid:icCode": "AR",
        "cdifniaid:serialNum": "064327",
        "cdifniaid:suffixCode": "A1",
        "cdifniaid:supportYear": "01"
      },
      "schema:startDate": "2013-09-20",
      "schema:url": "https://reporter.nih.gov/project-details/8632903"
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:endDate": "2021-04-30",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "NIAMS",
          "Instituto Nacional de Artritis y Enfermedades Musculoesqueléticas y de la Piel",
          "NIH/National Institute of Arthritis and Musculoskeletal and Skin Diseases",
          "National Institute of Arthritis & Musculoskeletal & Skin Diseases",
          "The National Institute of Arthritis and Musculoskeletal and Skin Diseases",
          "NIH National Institute of Arthritis and Musculoskeletal and Skin Diseases"
        ],
        "schema:identifier": "https://ror.org/006zn3t30",
        "schema:name": "National Institute of Arthritis and Musculoskeletal and Skin Diseases",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "1T32AR065972-01A1"
      },
      "schema:name": "Muscle Cell Biology, Pathophysiology, and Therapeutics",
      "cdifniaid:projectNumSplit": {
        "cdifniaid:activityCode": "T32",
        "cdifniaid:applTypeCode": "1",
        "cdifniaid:fullSupportYear": "01A1",
        "cdifniaid:icCode": "AR",
        "cdifniaid:serialNum": "065972",
        "cdifniaid:suffixCode": "A1",
        "cdifniaid:supportYear": "01"
      },
      "schema:startDate": "2016-05-01",
      "schema:url": "https://reporter.nih.gov/project-details/9074322"
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "healthy",
        "well"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2023-10-05",
        "schema:name": "Biothings API",
        "schema:url": "https://biothings.io/"
      },
      "schema:identifier": "C115935",
      "schema:inDefinedTermSet": "NCIT",
      "nde:isCurated": true,
      "schema:name": "Healthy",
      "nde:originalName": "healthy",
      "schema:url": "http://purl.obolibrary.org/obo/NCIT_C115935"
    }
  ],
  "schema:includedInDataCatalog": {
    "@type": [
      "schema:DataCatalog"
    ],
    "schema:archivedAt": "https://data.humancellatlas.org/explore/projects/4037007b-0eff-4e6d-b7bd-8dd8eec80143",
    "schema:name": "Human Cell Atlas (HCA)",
    "schema:url": "https://data.humancellatlas.org/",
    "nde:versionDate": "2026-10-24"
  },
  "schema:isAccessibleForFree": true,
  "schema:keywords": [
    "muscle",
    "hindlimb",
    "muscle organ",
    "whole hindlimb",
    "quadriceps femoris",
    "gastrocnemius",
    "hindlimb muscle",
    {
      "schema:name": "host",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:license": [
    "http://www.opengis.net/def/nil/OGC/0/missing"
  ],
  "schema:name": "Single Cell RNA-Sequencing of Human Limb Skeletal Muscle across Development and Myogenic Culture from Pluripotent Stem Cells",
  "schema:sameAs": [
    "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE147457"
  ],
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Human",
        "Homo sapiens Linnaeus, 1758",
        "human",
        "Home sapiens",
        "Homo sampiens",
        "Homo sapeins",
        "Homo sapian",
        "Homo sapians",
        "Homo sapien",
        "Homo sapience",
        "Homo sapiense",
        "Homo sapients",
        "Homo sapines",
        "Homo spaiens",
        "Homo spiens",
        "Humo sapiens"
      ],
      "cdifniaid:commonName": "Human",
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2023-10-05",
        "schema:name": "PubTator",
        "schema:url": "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html"
      },
      "schema:identifier": "9606",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": true,
      "schema:name": "Homo sapiens",
      "nde:originalName": "homo sapiens",
      "schema:url": "https://www.uniprot.org/taxonomy/9606"
    }
  ],
  "schema:url": "https://data.humancellatlas.org/explore/projects/4037007b-0eff-4e6d-b7bd-8dd8eec80143",
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "experimental scientist",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "University of California, Los Angeles, Pyle"
        },
        "schema:familyName": "Xi",
        "schema:givenName": "Haibin",
        "schema:name": "Haibin Xi"
      }
    },
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "data curator",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "University of California, Santa Cruz, Human Cell Atlas Data Coordination Platform"
        },
        "schema:familyName": "Nejad",
        "schema:givenName": "Parisa",
        "schema:name": "Parisa Nejad"
      }
    },
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "data curator",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "University of California, Santa Cruz, Human Cell Atlas Data Coordination Platform"
        },
        "schema:familyName": "Schwartz",
        "schema:givenName": "Rachel",
        "schema:name": "Rachel Schwartz"
      }
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
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataset/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "time": "http://www.w3.org/2006/time#",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:Dataset"
  ],
  "@id": "https://data.niaid.nih.gov/resources?id=hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143",
  "schema:subjectOf": {
    "schema:about": {
      "@id": "https://data.niaid.nih.gov/resources?id=hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143"
    },
    "schema:description": "CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.\n\nMetadata source from PMID.",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "https://data.niaid.nih.gov/resources?id=hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143#metadata",
    "schema:name": "Metadata record for: Single Cell RNA-Sequencing of Human Limb Skeletal Muscle across Development and Myogenic Culture from Pluripotent Stem C",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/niaid/1.0"
      }
    ],
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "NIAID Data Discovery Portal",
      "schema:url": "https://data.niaid.nih.gov/"
    },
    "schema:sdDatePublished": "2026-10-28"
  },
  "schema:identifier": "https://data.niaid.nih.gov/resources?id=hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143",
  "schema:dateModified": "2025-02-14",
  "schema:datePublished": "2021-04-27",
  "nde:date": "2025-02-14",
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "University of California, Los Angeles, Pyle"
        },
        "schema:familyName": "Xi",
        "schema:givenName": "Haibin",
        "schema:name": "Haibin Xi"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "University of California, Santa Cruz, Human Cell Atlas Data Coordination Platform"
        },
        "schema:familyName": "Nejad",
        "schema:givenName": "Parisa",
        "schema:name": "Parisa Nejad"
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "University of California, Santa Cruz, Human Cell Atlas Data Coordination Platform"
        },
        "schema:familyName": "Schwartz",
        "schema:givenName": "Rachel",
        "schema:name": "Rachel Schwartz"
      }
    ]
  },
  "schema:citation": [
    {
      "@type": [
        "schema:ScholarlyArticle"
      ],
      "nde:doi": "doi: 10.1016/j.stem.2020.06.006",
      "schema:name": "A Human Skeletal Muscle Atlas Identifies the Trajectories of Stem and Progenitor Cells across Development and from Human Pluripotent Stem Cells",
      "schema:url": "https://pubmed.ncbi.nlm.nih.gov/32619514/"
    },
    {
      "@type": [
        "schema:ScholarlyArticle"
      ],
      "schema:author": [
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Xi H"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Langerman J"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Sabri S"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Chien P"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Young CS"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Younesi S"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Hicks M"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Gonzalez K"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Fujiwara W"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Marzi J"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Liebscher S"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Spencer M"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Van Handel B"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Evseenko D"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Schenke-Layland K"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Plath K"
        },
        {
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Pyle AD"
        }
      ],
      "schema:datePublished": "2020-07-02",
      "schema:identifier": "PMID:32619514",
      "nde:journalName": "Cell stem cell",
      "schema:name": "A Human Skeletal Muscle Atlas Identifies the Trajectories of Stem and Progenitor Cells across Development and from Human Pluripotent Stem Cells.",
      "nde:pmid": "32619514",
      "schema:url": "https://pubmed.ncbi.nlm.nih.gov/32619514/"
    }
  ],
  "schema:description": "The developmental trajectory of human skeletal myogenesis and the transition between progenitor and stem cell states are unclear. To address this, we employed single cell RNA-sequencing to profile human skeletal muscle tissues from embryonic, fetal and postnatal stages. In silico, we identified myogenic as well as other cell types and constructed a \u201croadmap\u201d of human skeletal muscle ontogeny across development. In a similar fashion, we also profiled the heterogeneous cell cultures generated from multiple human pluripotent stem cell (hPSC) myogenic differentiation protocols, and mapped hPSC-derived myogenic progenitors to an embryonic-to-fetal transition period. Additionally, we found differentially enriched biological processes and discovered co-regulated gene networks and transcription factors present at distinct myogenic stages. In summary, this work serves as a resource for advancing our knowledge of human myogenesis. It also provides a tool for better characterization and understanding of hPSC-derived myogenic progenitors for translational applications in skeletal muscle based regenerative medicine.",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:endDate": "2018-08-31",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "NIAMS",
          "Instituto Nacional de Artritis y Enfermedades Musculoesquel\u00e9ticas y de la Piel",
          "NIH/National Institute of Arthritis and Musculoskeletal and Skin Diseases",
          "National Institute of Arthritis & Musculoskeletal & Skin Diseases",
          "The National Institute of Arthritis and Musculoskeletal and Skin Diseases",
          "NIH National Institute of Arthritis and Musculoskeletal and Skin Diseases"
        ],
        "schema:identifier": "https://ror.org/006zn3t30",
        "schema:name": "National Institute of Arthritis and Musculoskeletal and Skin Diseases",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "1R01AR064327-01A1"
      },
      "schema:name": "Reprogramming and Directed Differentiation of Skeletal Muscle Cells from hPSCs.",
      "cdifniaid:projectNumSplit": {
        "cdifniaid:activityCode": "R01",
        "cdifniaid:applTypeCode": "1",
        "cdifniaid:fullSupportYear": "01A1",
        "cdifniaid:icCode": "AR",
        "cdifniaid:serialNum": "064327",
        "cdifniaid:suffixCode": "A1",
        "cdifniaid:supportYear": "01"
      },
      "schema:startDate": "2013-09-20",
      "schema:url": "https://reporter.nih.gov/project-details/8632903"
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:endDate": "2021-04-30",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:alternateName": [
          "NIAMS",
          "Instituto Nacional de Artritis y Enfermedades Musculoesquel\u00e9ticas y de la Piel",
          "NIH/National Institute of Arthritis and Musculoskeletal and Skin Diseases",
          "National Institute of Arthritis & Musculoskeletal & Skin Diseases",
          "The National Institute of Arthritis and Musculoskeletal and Skin Diseases",
          "NIH National Institute of Arthritis and Musculoskeletal and Skin Diseases"
        ],
        "schema:identifier": "https://ror.org/006zn3t30",
        "schema:name": "National Institute of Arthritis and Musculoskeletal and Skin Diseases",
        "schema:parentOrganization": "National Institutes of Health"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "1T32AR065972-01A1"
      },
      "schema:name": "Muscle Cell Biology, Pathophysiology, and Therapeutics",
      "cdifniaid:projectNumSplit": {
        "cdifniaid:activityCode": "T32",
        "cdifniaid:applTypeCode": "1",
        "cdifniaid:fullSupportYear": "01A1",
        "cdifniaid:icCode": "AR",
        "cdifniaid:serialNum": "065972",
        "cdifniaid:suffixCode": "A1",
        "cdifniaid:supportYear": "01"
      },
      "schema:startDate": "2016-05-01",
      "schema:url": "https://reporter.nih.gov/project-details/9074322"
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "healthy",
        "well"
      ],
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2023-10-05",
        "schema:name": "Biothings API",
        "schema:url": "https://biothings.io/"
      },
      "schema:identifier": "C115935",
      "schema:inDefinedTermSet": "NCIT",
      "nde:isCurated": true,
      "schema:name": "Healthy",
      "nde:originalName": "healthy",
      "schema:url": "http://purl.obolibrary.org/obo/NCIT_C115935"
    }
  ],
  "schema:includedInDataCatalog": {
    "@type": [
      "schema:DataCatalog"
    ],
    "schema:archivedAt": "https://data.humancellatlas.org/explore/projects/4037007b-0eff-4e6d-b7bd-8dd8eec80143",
    "schema:name": "Human Cell Atlas (HCA)",
    "schema:url": "https://data.humancellatlas.org/",
    "nde:versionDate": "2026-10-24"
  },
  "schema:isAccessibleForFree": true,
  "schema:keywords": [
    "muscle",
    "hindlimb",
    "muscle organ",
    "whole hindlimb",
    "quadriceps femoris",
    "gastrocnemius",
    "hindlimb muscle",
    {
      "schema:name": "host",
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:about": "NIAID classification"
    }
  ],
  "schema:license": [
    "http://www.opengis.net/def/nil/OGC/0/missing"
  ],
  "schema:name": "Single Cell RNA-Sequencing of Human Limb Skeletal Muscle across Development and Myogenic Culture from Pluripotent Stem Cells",
  "schema:sameAs": [
    "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE147457"
  ],
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:alternateName": [
        "Human",
        "Homo sapiens Linnaeus, 1758",
        "human",
        "Home sapiens",
        "Homo sampiens",
        "Homo sapeins",
        "Homo sapian",
        "Homo sapians",
        "Homo sapien",
        "Homo sapience",
        "Homo sapiense",
        "Homo sapients",
        "Homo sapines",
        "Homo spaiens",
        "Homo spiens",
        "Humo sapiens"
      ],
      "cdifniaid:commonName": "Human",
      "nde:curatedBy": {
        "@type": [
          "schema:SoftwareApplication"
        ],
        "schema:dateModified": "2023-10-05",
        "schema:name": "PubTator",
        "schema:url": "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html"
      },
      "schema:identifier": "9606",
      "schema:inDefinedTermSet": "UniProt",
      "nde:isCurated": true,
      "schema:name": "Homo sapiens",
      "nde:originalName": "homo sapiens",
      "schema:url": "https://www.uniprot.org/taxonomy/9606"
    }
  ],
  "schema:url": "https://data.humancellatlas.org/explore/projects/4037007b-0eff-4e6d-b7bd-8dd8eec80143",
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "experimental scientist",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "University of California, Los Angeles, Pyle"
        },
        "schema:familyName": "Xi",
        "schema:givenName": "Haibin",
        "schema:name": "Haibin Xi"
      }
    },
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "data curator",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "University of California, Santa Cruz, Human Cell Atlas Data Coordination Platform"
        },
        "schema:familyName": "Nejad",
        "schema:givenName": "Parisa",
        "schema:name": "Parisa Nejad"
      }
    },
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "data curator",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "University of California, Santa Cruz, Human Cell Atlas Data Coordination Platform"
        },
        "schema:familyName": "Schwartz",
        "schema:givenName": "Rachel",
        "schema:name": "Rachel Schwartz"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix cdifniaid: <https://w3id.org/cdif/niaid/terms/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://data.niaid.nih.gov/resources?id=hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143> a schema1:Dataset ;
    schema1:citation [ a schema1:ScholarlyArticle ;
            schema1:author [ a schema1:Person ;
                    schema1:name "Plath K" ],
                [ a schema1:Person ;
                    schema1:name "Spencer M" ],
                [ a schema1:Person ;
                    schema1:name "Fujiwara W" ],
                [ a schema1:Person ;
                    schema1:name "Hicks M" ],
                [ a schema1:Person ;
                    schema1:name "Xi H" ],
                [ a schema1:Person ;
                    schema1:name "Pyle AD" ],
                [ a schema1:Person ;
                    schema1:name "Liebscher S" ],
                [ a schema1:Person ;
                    schema1:name "Sabri S" ],
                [ a schema1:Person ;
                    schema1:name "Gonzalez K" ],
                [ a schema1:Person ;
                    schema1:name "Langerman J" ],
                [ a schema1:Person ;
                    schema1:name "Younesi S" ],
                [ a schema1:Person ;
                    schema1:name "Van Handel B" ],
                [ a schema1:Person ;
                    schema1:name "Schenke-Layland K" ],
                [ a schema1:Person ;
                    schema1:name "Evseenko D" ],
                [ a schema1:Person ;
                    schema1:name "Marzi J" ],
                [ a schema1:Person ;
                    schema1:name "Young CS" ],
                [ a schema1:Person ;
                    schema1:name "Chien P" ] ;
            schema1:datePublished "2020-07-02" ;
            schema1:identifier "PMID:32619514" ;
            schema1:name "A Human Skeletal Muscle Atlas Identifies the Trajectories of Stem and Progenitor Cells across Development and from Human Pluripotent Stem Cells." ;
            schema1:url "https://pubmed.ncbi.nlm.nih.gov/32619514/" ;
            nde:journalName "Cell stem cell" ;
            nde:pmid "32619514" ],
        [ a schema1:ScholarlyArticle ;
            schema1:name "A Human Skeletal Muscle Atlas Identifies the Trajectories of Stem and Progenitor Cells across Development and from Human Pluripotent Stem Cells" ;
            schema1:url "https://pubmed.ncbi.nlm.nih.gov/32619514/" ;
            nde:doi "doi: 10.1016/j.stem.2020.06.006" ] ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor [ a schema1:Person ;
                    schema1:affiliation [ a schema1:Organization ;
                            schema1:name "University of California, Santa Cruz, Human Cell Atlas Data Coordination Platform" ] ;
                    schema1:familyName "Schwartz" ;
                    schema1:givenName "Rachel" ;
                    schema1:name "Rachel Schwartz" ] ;
            schema1:roleName "data curator" ],
        [ a schema1:Role ;
            schema1:contributor [ a schema1:Person ;
                    schema1:affiliation [ a schema1:Organization ;
                            schema1:name "University of California, Santa Cruz, Human Cell Atlas Data Coordination Platform" ] ;
                    schema1:familyName "Nejad" ;
                    schema1:givenName "Parisa" ;
                    schema1:name "Parisa Nejad" ] ;
            schema1:roleName "data curator" ],
        [ a schema1:Role ;
            schema1:contributor [ a schema1:Person ;
                    schema1:affiliation [ a schema1:Organization ;
                            schema1:name "University of California, Los Angeles, Pyle" ] ;
                    schema1:familyName "Xi" ;
                    schema1:givenName "Haibin" ;
                    schema1:name "Haibin Xi" ] ;
            schema1:roleName "experimental scientist" ] ;
    schema1:creator ( [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "University of California, Los Angeles, Pyle" ] ;
                schema1:familyName "Xi" ;
                schema1:givenName "Haibin" ;
                schema1:name "Haibin Xi" ] [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "University of California, Santa Cruz, Human Cell Atlas Data Coordination Platform" ] ;
                schema1:familyName "Nejad" ;
                schema1:givenName "Parisa" ;
                schema1:name "Parisa Nejad" ] [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "University of California, Santa Cruz, Human Cell Atlas Data Coordination Platform" ] ;
                schema1:familyName "Schwartz" ;
                schema1:givenName "Rachel" ;
                schema1:name "Rachel Schwartz" ] ) ;
    schema1:dateModified "2025-02-14" ;
    schema1:datePublished "2021-04-27" ;
    schema1:description "The developmental trajectory of human skeletal myogenesis and the transition between progenitor and stem cell states are unclear. To address this, we employed single cell RNA-sequencing to profile human skeletal muscle tissues from embryonic, fetal and postnatal stages. In silico, we identified myogenic as well as other cell types and constructed a “roadmap” of human skeletal muscle ontogeny across development. In a similar fashion, we also profiled the heterogeneous cell cultures generated from multiple human pluripotent stem cell (hPSC) myogenic differentiation protocols, and mapped hPSC-derived myogenic progenitors to an embryonic-to-fetal transition period. Additionally, we found differentially enriched biological processes and discovered co-regulated gene networks and transcription factors present at distinct myogenic stages. In summary, this work serves as a resource for advancing our knowledge of human myogenesis. It also provides a tool for better characterization and understanding of hPSC-derived myogenic progenitors for translational applications in skeletal muscle based regenerative medicine." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:endDate "2021-04-30" ;
            schema1:funder [ a schema1:Organization ;
                    schema1:alternateName "Instituto Nacional de Artritis y Enfermedades Musculoesqueléticas y de la Piel",
                        "NIAMS",
                        "NIH National Institute of Arthritis and Musculoskeletal and Skin Diseases",
                        "NIH/National Institute of Arthritis and Musculoskeletal and Skin Diseases",
                        "National Institute of Arthritis & Musculoskeletal & Skin Diseases",
                        "The National Institute of Arthritis and Musculoskeletal and Skin Diseases" ;
                    schema1:identifier "https://ror.org/006zn3t30" ;
                    schema1:name "National Institute of Arthritis and Musculoskeletal and Skin Diseases" ;
                    schema1:parentOrganization "National Institutes of Health" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:value "1T32AR065972-01A1" ] ;
            schema1:name "Muscle Cell Biology, Pathophysiology, and Therapeutics" ;
            schema1:startDate "2016-05-01" ;
            schema1:url "https://reporter.nih.gov/project-details/9074322" ;
            cdifniaid:projectNumSplit [ cdifniaid:activityCode "T32" ;
                    cdifniaid:applTypeCode "1" ;
                    cdifniaid:fullSupportYear "01A1" ;
                    cdifniaid:icCode "AR" ;
                    cdifniaid:serialNum "065972" ;
                    cdifniaid:suffixCode "A1" ;
                    cdifniaid:supportYear "01" ] ],
        [ a schema1:MonetaryGrant ;
            schema1:endDate "2018-08-31" ;
            schema1:funder [ a schema1:Organization ;
                    schema1:alternateName "Instituto Nacional de Artritis y Enfermedades Musculoesqueléticas y de la Piel",
                        "NIAMS",
                        "NIH National Institute of Arthritis and Musculoskeletal and Skin Diseases",
                        "NIH/National Institute of Arthritis and Musculoskeletal and Skin Diseases",
                        "National Institute of Arthritis & Musculoskeletal & Skin Diseases",
                        "The National Institute of Arthritis and Musculoskeletal and Skin Diseases" ;
                    schema1:identifier "https://ror.org/006zn3t30" ;
                    schema1:name "National Institute of Arthritis and Musculoskeletal and Skin Diseases" ;
                    schema1:parentOrganization "National Institutes of Health" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:value "1R01AR064327-01A1" ] ;
            schema1:name "Reprogramming and Directed Differentiation of Skeletal Muscle Cells from hPSCs." ;
            schema1:startDate "2013-09-20" ;
            schema1:url "https://reporter.nih.gov/project-details/8632903" ;
            cdifniaid:projectNumSplit [ cdifniaid:activityCode "R01" ;
                    cdifniaid:applTypeCode "1" ;
                    cdifniaid:fullSupportYear "01A1" ;
                    cdifniaid:icCode "AR" ;
                    cdifniaid:serialNum "064327" ;
                    cdifniaid:suffixCode "A1" ;
                    cdifniaid:supportYear "01" ] ] ;
    schema1:healthCondition [ a schema1:DefinedTerm ;
            schema1:alternateName "healthy",
                "well" ;
            schema1:identifier "C115935" ;
            schema1:inDefinedTermSet "NCIT" ;
            schema1:name "Healthy" ;
            schema1:url "http://purl.obolibrary.org/obo/NCIT_C115935" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:dateModified "2023-10-05" ;
                    schema1:name "Biothings API" ;
                    schema1:url "https://biothings.io/" ] ;
            nde:isCurated true ;
            nde:originalName "healthy" ] ;
    schema1:identifier "https://data.niaid.nih.gov/resources?id=hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:archivedAt "https://data.humancellatlas.org/explore/projects/4037007b-0eff-4e6d-b7bd-8dd8eec80143" ;
            schema1:name "Human Cell Atlas (HCA)" ;
            schema1:url "https://data.humancellatlas.org/" ;
            nde:versionDate "2026-10-24" ] ;
    schema1:isAccessibleForFree true ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:about "NIAID classification" ;
            schema1:name "host" ],
        "gastrocnemius",
        "hindlimb",
        "hindlimb muscle",
        "muscle",
        "muscle organ",
        "quadriceps femoris",
        "whole hindlimb" ;
    schema1:license "http://www.opengis.net/def/nil/OGC/0/missing" ;
    schema1:name "Single Cell RNA-Sequencing of Human Limb Skeletal Muscle across Development and Myogenic Culture from Pluripotent Stem Cells" ;
    schema1:sameAs "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE147457" ;
    schema1:subjectOf <https://data.niaid.nih.gov/resources?id=hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143#metadata> ;
    schema1:url "https://data.humancellatlas.org/explore/projects/4037007b-0eff-4e6d-b7bd-8dd8eec80143" ;
    nde:date "2025-02-14" ;
    nde:species [ a schema1:DefinedTerm ;
            schema1:alternateName "Home sapiens",
                "Homo sampiens",
                "Homo sapeins",
                "Homo sapian",
                "Homo sapians",
                "Homo sapien",
                "Homo sapience",
                "Homo sapiens Linnaeus, 1758",
                "Homo sapiense",
                "Homo sapients",
                "Homo sapines",
                "Homo spaiens",
                "Homo spiens",
                "Human",
                "Humo sapiens",
                "human" ;
            schema1:identifier "9606" ;
            schema1:inDefinedTermSet "UniProt" ;
            schema1:name "Homo sapiens" ;
            schema1:url "https://www.uniprot.org/taxonomy/9606" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:dateModified "2023-10-05" ;
                    schema1:name "PubTator" ;
                    schema1:url "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html" ] ;
            nde:isCurated true ;
            nde:originalName "homo sapiens" ;
            cdifniaid:commonName "Human" ] .

<https://data.niaid.nih.gov/resources?id=hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143#metadata> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/niaid/1.0> ;
    schema1:about <https://data.niaid.nih.gov/resources?id=hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143> ;
    schema1:additionalType dcat:CatalogRecord ;
    schema1:description """CDIF metadata harvested from the NIAID Data Discovery Portal API (index build 2026-10-28), record hca_4037007b-0eff-4e6d-b7bd-8dd8eec80143, and converted by harvest_niaid_to_cdif.py. The portal aggregates this record from the repositories named in schema:includedInDataCatalog; nde: properties, including the portal's term annotations, are as the portal publishes them.

Metadata source from PMID.""" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "NIAID Data Discovery Portal" ;
            schema1:url "https://data.niaid.nih.gov/" ] ;
    schema1:name "Metadata record for: Single Cell RNA-Sequencing of Human Limb Skeletal Muscle across Development and Myogenic Culture from Pluripotent Stem C" ;
    schema1:sdDatePublished "2026-10-28" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: NIAID dataset properties
description: 'The properties NIAID Data Discovery Portal records add to a CDIF dataset
  (composed with cdifCore and cdifDiscovery by the cdifNIAID profile; this module
  does NOT re-embed them). nde: terms are NIAID''s (https://discovery.biothings.io/ns/nde/),
  bios: terms Bioschemas'' (from the bioschemasSample block), and cdifniaid: terms
  the ones the portal uses that neither vocabulary declares. The properties NIAID
  adds to a DefinedTerm, a MonetaryGrant, a cited work, a Place and a DataCatalog
  are defined by the niaidDefinedTerm, niaidMonetaryGrant, niaidCreativeWork, niaidPlace
  and niaidDataCatalog blocks, which require those types. Every property accepts one
  value or an array, because framing collapses a one-element array to its value.'
type: object
required:
- schema:includedInDataCatalog
properties:
  '@context':
    type: object
    properties:
      nde:
        const: https://discovery.biothings.io/ns/nde/
      bios:
        const: https://bioschemas.org/
      cdifniaid:
        const: https://w3id.org/cdif/niaid/terms/
  schema:subjectOf:
    properties:
      dcterms:conformsTo:
        type: array
        items:
          description: uri for specifications that this metadata record conforms to
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        minItems: 1
        contains:
          type: object
          required:
          - '@id'
          additionalProperties: false
          properties:
            '@id':
              const: https://w3id.org/cdif/niaid/1.0
        x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-id: http://schema.org/subjectOf
  schema:includedInDataCatalog:
    description: The repositories holding the dataset, which the portal aggregates
      from.
    anyOf:
    - $ref: '#/$defs/catalog'
    - type: array
      minItems: 1
      items:
        $ref: '#/$defs/catalog'
    x-jsonld-id: http://schema.org/includedInDataCatalog
  nde:date:
    description: The portal's summary date for the record.
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/bioschemasSample/schema.yaml#/$defs/date
    x-jsonld-id: https://discovery.biothings.io/ns/nde/date
  nde:species:
    description: Host organisms associated with the dataset, e.g. Homo sapiens (the
      NIAID Blueprint's host); the pathogen is in schema:infectiousAgent.
    $ref: '#/$defs/terms'
    x-jsonld-id: https://discovery.biothings.io/ns/nde/species
  schema:keywords:
    description: NIAID's annotations on keyword terms, such as the dataset's EDAM
      topic categories.
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: http://schema.org/keywords
  schema:infectiousAgent:
    description: Infectious agents the dataset is about.
    $ref: '#/$defs/terms'
    x-jsonld-id: http://schema.org/infectiousAgent
  schema:healthCondition:
    description: Health conditions the dataset is about.
    $ref: '#/$defs/terms'
    x-jsonld-id: http://schema.org/healthCondition
  schema:measurementTechnique:
    description: NIAID's annotations on the measurement techniques CDIF discovery
      describes.
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: http://schema.org/measurementTechnique
  schema:variableMeasured:
    description: NIAID's annotations on the variables CDIF discovery describes.
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: http://schema.org/variableMeasured
  nde:nctid:
    description: ClinicalTrials.gov identifier of the study.
    anyOf:
    - $ref: '#/$defs/nctid'
    - type: array
      items:
        $ref: '#/$defs/nctid'
    x-jsonld-id: https://discovery.biothings.io/ns/nde/nctid
  nde:citedBy:
    description: Works that cite the dataset.
    $ref: '#/$defs/works'
    x-jsonld-id: https://discovery.biothings.io/ns/nde/citedBy
  schema:citation:
    description: NIAID's journal and PubMed details on CDIF's citations.
    $ref: '#/$defs/works'
    x-jsonld-id: http://schema.org/citation
  nde:curatedBy:
    description: Who curated the record, and from which version of their catalog.
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDefinedTerm/schema.yaml#/$defs/curator
    x-jsonld-id: https://discovery.biothings.io/ns/nde/curatedBy
  nde:isBasisFor:
    description: Resources based on this dataset.
    $ref: '#/$defs/relatedResources'
    x-jsonld-id: https://discovery.biothings.io/ns/nde/isBasisFor
  nde:sample:
    description: The samples used to generate the dataset, or a collection of them.
    anyOf:
    - $ref: '#/$defs/sample'
    - $ref: '#/$defs/sampleCollection'
    - type: array
      items:
        anyOf:
        - $ref: '#/$defs/sample'
        - $ref: '#/$defs/sampleCollection'
    x-jsonld-id: https://discovery.biothings.io/ns/nde/sample
  schema:funding:
    description: NIAID's grant details on CDIF's funding.
    anyOf:
    - $ref: '#/$defs/grant'
    - type: array
      items:
        $ref: '#/$defs/grant'
    x-jsonld-id: http://schema.org/funding
  schema:spatialCoverage:
    description: NIAID's administrative type on CDIF's spatial coverage.
    anyOf:
    - $ref: '#/$defs/place'
    - type: array
      items:
        $ref: '#/$defs/place'
    x-jsonld-id: http://schema.org/spatialCoverage
  schema:sourceOrganization:
    description: Projects and programs the dataset comes from.
    anyOf:
    - $ref: '#/$defs/sourceOrganization'
    - type: array
      items:
        $ref: '#/$defs/sourceOrganization'
    x-jsonld-id: http://schema.org/sourceOrganization
  bios:alternateIdentifier:
    description: Identifiers beyond the one CDIF's schema:identifier holds.
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/bioschemasSample/schema.yaml#/$defs/texts
    x-jsonld-id: https://bioschemas.org/alternateIdentifier
  cdifniaid:assayformat:
    description: The assay format, as the portal gives it.
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/bioschemasSample/schema.yaml#/$defs/texts
    x-jsonld-id: https://w3id.org/cdif/niaid/terms/assayformat
  cdifniaid:publication:
    description: PubMed identifiers of publications about the dataset.
    anyOf:
    - $ref: '#/$defs/pmid'
    - type: array
      items:
        $ref: '#/$defs/pmid'
    x-jsonld-id: https://w3id.org/cdif/niaid/terms/publication
$defs:
  types:
    anyOf:
    - type: string
    - type: array
      items:
        type: string
  reference:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
  catalog:
    anyOf:
    - $ref: '#/$defs/reference'
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataCatalog/schema.yaml
  terms:
    description: NIAID's annotated terms; each must be a schema:DefinedTerm.
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDefinedTerm/schema.yaml
    - type: array
      items:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDefinedTerm/schema.yaml
  annotated:
    description: An object carrying one of NIAID's term annotations, which must then
      be a NIAID defined term. Other objects are left to CDIF's own rules.
    type: object
    if:
      anyOf:
      - required:
        - nde:isCurated
      - required:
        - nde:originalName
      - required:
        - nde:curatedBy
      - required:
        - cdifniaid:commonName
    then:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDefinedTerm/schema.yaml
  termsOrText:
    anyOf:
    - type: string
    - $ref: '#/$defs/annotated'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/annotated'
  nctid:
    type: string
    pattern: ^NCT\d{8}$
  pmid:
    type: string
    pattern: ^\d+$
  work:
    description: A cited or citing work. One carrying NIAID's PubMed id, DOI or journal
      names must be a NIAID creative work; a string or any other object is left to
      CDIF's own rules.
    anyOf:
    - type: string
    - type: object
      if:
        anyOf:
        - required:
          - nde:pmid
        - required:
          - nde:doi
        - required:
          - nde:journalName
        - required:
          - nde:journalNameAbbrev
      then:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidCreativeWork/schema.yaml
  works:
    anyOf:
    - $ref: '#/$defs/work'
    - type: array
      items:
        $ref: '#/$defs/work'
  relatedResource:
    type: object
    properties:
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
      nde:relationship:
        description: How the resource is related, e.g. "has part" or "is part of".
        type: string
        x-jsonld-id: https://discovery.biothings.io/ns/nde/relationship
      nde:doi:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/bioschemasSample/schema.yaml#/$defs/texts
        x-jsonld-id: https://discovery.biothings.io/ns/nde/doi
  relatedResources:
    anyOf:
    - $ref: '#/$defs/relatedResource'
    - type: array
      items:
        $ref: '#/$defs/relatedResource'
  grant:
    anyOf:
    - $ref: '#/$defs/reference'
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidMonetaryGrant/schema.yaml
  place:
    anyOf:
    - $ref: '#/$defs/reference'
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidPlace/schema.yaml
  sourceOrganization:
    type: object
    properties:
      cdifniaid:correctionApproved:
        description: A correction to the portal's record of the project has been approved.
        type: boolean
        x-jsonld-id: https://w3id.org/cdif/niaid/terms/correctionApproved
  sample:
    description: A sample; nde:Sample is NIAID's subclass of the Bioschemas sample.
    allOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/bioschemasSample/schema.yaml
    - type: object
      properties:
        nde:cellType:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/bioschemasSample/schema.yaml#/$defs/termsOrText
          x-jsonld-id: https://discovery.biothings.io/ns/nde/cellType
        nde:associatedGenotype:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/bioschemasSample/schema.yaml#/$defs/termsOrText
          x-jsonld-id: https://discovery.biothings.io/ns/nde/associatedGenotype
        nde:species:
          $ref: '#/$defs/terms'
          x-jsonld-id: https://discovery.biothings.io/ns/nde/species
        schema:aggregateElement:
          $ref: '#/$defs/sample'
          x-jsonld-id: http://schema.org/aggregateElement
  sampleCollection:
    description: A collection of samples, typed nde:SampleCollection. The type is
      required, so that a sample is not taken for a collection.
    type: object
    required:
    - '@type'
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: nde:SampleCollection
      schema:numberOfItems:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/bioschemasSample/schema.yaml#/$defs/quantity
        x-jsonld-id: http://schema.org/numberOfItems
      schema:aggregateElement:
        $ref: '#/$defs/sample'
        x-jsonld-id: http://schema.org/aggregateElement
      schema:itemListElement:
        anyOf:
        - $ref: '#/$defs/sample'
        - type: array
          items:
            $ref: '#/$defs/sample'
        x-jsonld-id: http://schema.org/itemListElement
x-jsonld-prefixes:
  schema: http://schema.org/
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  prov: http://www.w3.org/ns/prov#
  nde: https://discovery.biothings.io/ns/nde/
  bios: https://bioschemas.org/
  cdifniaid: https://w3id.org/cdif/niaid/terms/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.niaidProperties.niaidDataset
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '1.0'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataset/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataset/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "nde": "https://discovery.biothings.io/ns/nde/",
    "bios": "https://bioschemas.org/",
    "cdifniaid": "https://w3id.org/cdif/niaid/terms/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataset/context.jsonld)

## Sources

* [NIAID Data Ecosystem schemas](https://github.com/NIAID-Data-Ecosystem/nde-schemas)
* [NIAID Data Discovery Portal](https://data.niaid.nih.gov/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/niaidProperties/niaidDataset`

