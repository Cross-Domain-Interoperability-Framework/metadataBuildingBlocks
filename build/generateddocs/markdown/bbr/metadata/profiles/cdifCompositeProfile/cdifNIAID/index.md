
# CDIF NIAID profile (Schema)

`cdif.bbr.metadata.profiles.cdifCompositeProfile.cdifNIAID` *v1.0*

Document-level CDIF profile for dataset records from the NIAID Data Discovery Portal: composes cdifCore with niaidDataset. Records that also carry discovery content claim and are validated against cdifDiscovery separately. Conformance URI https://w3id.org/cdif/niaid/1.0.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### A NIAID Data Discovery Portal record conforming to cdifNIAID.
A real record from the NIAID Data Discovery Portal API (index build 2026-10-28),
converted by converters/NIAID/harvest_niaid_to_cdif.py. It claims core,
discovery and cdifNIAID.
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/cdifNIAID/context.jsonld",
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
                    schema1:name "Saito MA" ],
                [ a schema1:Person ;
                    schema1:name "McIlvin MR" ] ;
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
            schema1:about "NIAID classification" ;
            schema1:name "host" ],
        [ a schema1:DefinedTerm ;
            schema1:about "NIAID classification" ;
            schema1:name "infectiousAgent" ],
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
            schema1:about "topicCategory" ;
            schema1:identifier "topic_0121" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Proteomics" ;
            schema1:url "http://edamontology.org/topic_0121" ;
            nde:curatedBy [ a schema1:SoftwareApplication ;
                    schema1:name "GPT-4o-mini" ;
                    schema1:url "https://openai.com/index/chatgpt" ] ],
        [ a schema1:DefinedTerm ;
            schema1:about "topicCategory" ;
            schema1:identifier "topic_3174" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Metagenomics" ;
            schema1:url "http://edamontology.org/topic_3174" ;
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
            nde:originalName "Shotgun proteomics" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "0000534" ;
            schema1:inDefinedTermSet "MMO" ;
            schema1:name "mass spectrometry" ;
            schema1:url "http://purl.obolibrary.org/obo/MMO_0000534" ;
            nde:isCurated true ;
            nde:originalName "Mass Spectrometry" ] ;
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

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: CDIF NIAID profile
description: 'CDIF profile for dataset records from the NIAID Data Discovery Portal.
  Composes cdifCore with niaidDataset, which constrains the NIAID (nde:), Bioschemas
  (bios:) and cdifniaid: properties those records carry. cdifDiscovery is not composed:
  about one record in six from the portal has no discovery content, so a record that
  has it claims and is validated against cdifDiscovery as well, as its own conformsTo
  entry.'
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifCore/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataset/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  cdif: https://w3id.org/cdif/
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  prov: http://www.w3.org/ns/prov#
  nde: https://discovery.biothings.io/ns/nde/
  bios: https://bioschemas.org/
  cdifniaid: https://w3id.org/cdif/niaid/terms/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.profiles.cdifCompositeProfile.cdifNIAID
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '1.0'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/cdifNIAID/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/cdifNIAID/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "cdif": "https://w3id.org/cdif/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "nde": "https://discovery.biothings.io/ns/nde/",
    "bios": "https://bioschemas.org/",
    "cdifniaid": "cdif:niaid/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/cdifNIAID/context.jsonld)

## Sources

* [CDIF book](https://cross-domain-interoperability-framework.github.io/cdifbook/)
* [NIAID Data Discovery Portal](https://data.niaid.nih.gov/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifCompositeProfile/cdifNIAID`

