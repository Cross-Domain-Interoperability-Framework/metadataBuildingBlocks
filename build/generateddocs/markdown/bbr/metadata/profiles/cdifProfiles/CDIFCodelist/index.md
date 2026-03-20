
# CDIF Codelist (Schema)

`cdif.bbr.metadata.profiles.cdifProfiles.CDIFCodelist` *v0.1*

CDIF profile for controlled vocabulary codelists as SKOS ConceptSchemes. Requires concepts to have resolvable @id identifiers, skos:inScheme, skos:definition, and skos:prefLabel. Scheme must declare skos:hasTopConcept. Includes SHACL validation shapes.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Codelist Profile

A CDIF profile for controlled vocabulary codelists implemented as SKOS ConceptSchemes.

### ConceptScheme requirements
- Must have a globally unique, resolvable `@id` URI
- Must have at least one `skos:prefLabel`
- Must declare top concepts via `skos:hasTopConcept`

### Concept requirements (beyond base SKOS)
- Must have a globally unique, resolvable `@id` URI
- Must have `skos:inScheme` linking to the containing ConceptScheme
- Must have at least one `skos:prefLabel` (at most one per language)
- Must have at least one `skos:definition`
- Must declare `skos:broader` if the concept is not a top concept in a hierarchical scheme
- `skos:notation` is optional but must be unique within the scheme if used
- `skos:altLabel`, `skos:narrower`, and other SKOS properties are optional

### Validation
- JSON Schema validates structure and required properties
- SHACL shapes validate RDF constraints including `sh:uniqueLang` on `skos:prefLabel` and `sh:class skos:ConceptScheme` on `skos:inScheme` targets

This profile aligns with the approach described in ['Modelling of Eurostat's Statistical Classifications in ShowVoc'](https://cros.ec.europa.eu/book-page/modeling-eurostats-statistical-classifications-showvoc).

## Examples

### CDIF Codelist example
Rock Type Classification codelist with three top concepts (igneous,
sedimentary, metamorphic) and nested specific rock types. Demonstrates
all required CDIF codelist properties: @id, prefLabel, definition,
inScheme, broader, notation, and cross-references via related.
#### json
```json
{
  "@context": {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dcterms": "http://purl.org/dc/terms/",
    "schema": "http://schema.org/",
    "sf": "https://w3id.org/isample/vocabulary/sampledfeature/"
  },
  "@id": "sf:sampledfeaturevocabulary",
  "@type": ["skos:ConceptScheme"],
  "skos:prefLabel": {"@value": "Sampled Feature Type vocabulary", "@language": "en"},
  "skos:definition": {"@value": "Categories to specify the broad context that a sample is intended to represent.", "@language": "en"},
  "dcterms:created": "2021-03-17",
  "dcterms:modified": "2024-04-19",
  "dcterms:creator": {"@id": "https://orcid.org/0000-0001-6041-5302"},
  "dcterms:license": {"@id": "https://creativecommons.org/licenses/by/4.0/legalcode"},
  "skos:historyNote": [
    {"@value": "2021-07-09  Remove Marine biome, Subaerial terrestrial environment, Subaqueous terrestrial environment per github issue https://github.com/isamplesorg/metadata/issues/41. Make Experiment setting and Laboratory or curatorial environment subclasses of Active human occupation site.", "@language": "en"},
    {"@value": "2021-12-10 SMR add missing skos:inScheme statements", "@language": "en"},
    {"@value": "2022-01-07 SMR change to https://w3id.org/isample/ uri base, make the ConceptScheme an ontology as well. For uploading to ESIP COR and w3id resolution redirect set up. Add some mappings to other ontologies using seeAlso, closeMatch, narrowMatch.", "@language": "en"},
    {"@value": "2022-03-11 SMR change definitions from rdfs:comment to skos:definition. Minor fixes in definitions. Add skos matches to URIs from other vocabularies. Fix typo in glacierenvrionment URI (changed the URI to glacierenvironment)", "@language": "en"},
    {"@value": "2022-09-07 SMR update some of the skos mappings to other vocabularies; remove references to other vocabularies as NamedIndividual. Remove rocksample class, it was not linked in hierarchy and inconsistent with design.", "@language": "en"},
    {"@value": "2022-09-30 add biological entity as sampled feature, per issue https://github.com/isamplesorg/metadata/issues/107. This update was lost at some point and added back in 2022-12-09.", "@language": "en"},
    {"@value": "2023-11-05 SMR update version to 1.0, prep for release", "@language": "en"},
    {"@value": "2024-04-19 SMR update definitions to remove use of 'specimen'. Edit some definitions for better clarity", "@language": "en"},
    {"@value": "2024-09-13 remove version numbers from URI", "@language": "en"}
  ],
  "skos:hasTopConcept": [
    {
      "@id": "sf:anysampledfeature",
      "@type": ["skos:Concept"],
      "skos:prefLabel": {"@value": "Any sampled feature", "@language": "en"},
      "skos:definition": {"@value": "Any thing that can be sampled. Top concept in sampled feature type vocabulary.", "@language": "en"},
      "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
      "skos:topConceptOf": {"@id": "sf:sampledfeaturevocabulary"},
      "skos:narrower": [
        {
          "@id": "sf:anthropogenicenvironment",
          "@type": ["skos:Concept"],
          "skos:prefLabel": {"@value": "Anthropogenic environment", "@language": "en"},
          "skos:definition": {"@value": "Sampled feature is produced by or related to human activity past or present.", "@language": "en"},
          "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
          "skos:broader": [{"@id": "sf:anysampledfeature"}],
          "skos:closeMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_01000313"}],
          "skos:narrower": [
            {
              "@id": "sf:activehumanoccupationsite",
              "@type": ["skos:Concept"],
              "skos:prefLabel": {"@value": "Active human occupation site", "@language": "en"},
              "skos:definition": {"@value": "sampled feature is a site at which there are ongoing human activities", "@language": "en"},
              "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
              "skos:broader": [{"@id": "sf:anthropogenicenvironment"}],
              "skos:narrower": [
                {
                  "@id": "sf:experimentsetting",
                  "@type": ["skos:Concept"],
                  "skos:prefLabel": {"@value": "Experiment setting", "@language": "en"},
                  "skos:definition": {"@value": "Sampled feature is an experimental set up that produced the sample; the sample is the product of the experiment.", "@language": "en"},
                  "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
                  "skos:broader": [{"@id": "sf:activehumanoccupationsite"}]
                },
                {
                  "@id": "sf:laboratorycuratorialenvironment",
                  "@type": ["skos:Concept"],
                  "skos:prefLabel": {"@value": "Laboratory or curatorial environment", "@language": "en"},
                  "skos:definition": {"@value": "Sampled feature is a laboratory or other research site, collected with intention of characterizing the environment in which data are collected or other research conducted, that might affect results or safety; e.g. lab blank measurements.", "@language": "en"},
                  "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
                  "skos:broader": [{"@id": "sf:activehumanoccupationsite"}],
                  "skos:closeMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_01001405"}]
                }
              ]
            },
            {
              "@id": "sf:pasthumanoccupationsite",
              "@type": ["skos:Concept"],
              "skos:prefLabel": {"@value": "Site of past human activities", "@language": "en"},
              "skos:definition": {"@value": "sampled feature is a place where humans have been and left evidence of their activity. Includes prehistoric and paleo hominid sites", "@language": "en"},
              "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
              "skos:broader": [{"@id": "sf:anthropogenicenvironment"}]
            }
          ]
        },
        {
          "@id": "sf:biologicalentity",
          "@type": ["skos:Concept"],
          "skos:prefLabel": {"@value": "Biological entity", "@language": "en"},
          "skos:definition": {"@value": "Sampled feature is an organism. Use for samples that represent some species of organism as the proximate sampled feature, not the environment that the organism inhabits.", "@language": "en"},
          "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
          "skos:broader": [{"@id": "sf:anysampledfeature"}],
          "skos:note": {"@value": "domain specific vocabulary extensions will be useful to distinguish samples from different phyla/order/class...", "@language": "en"}
        },
        {
          "@id": "sf:earthenvironment",
          "@type": ["skos:Concept"],
          "skos:prefLabel": {"@value": "Earth environment", "@language": "en"},
          "skos:definition": {"@value": "Sampled feature is the natural Earth environment", "@language": "en"},
          "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
          "skos:broader": [{"@id": "sf:anysampledfeature"}],
          "skos:narrower": [
            {
              "@id": "sf:atmosphere",
              "@type": ["skos:Concept"],
              "skos:prefLabel": {"@value": "Atmosphere", "@language": "en"},
              "skos:definition": {"@value": "Sampled feature is the Earth's atmosphere", "@language": "en"},
              "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
              "skos:broader": [{"@id": "sf:earthenvironment"}]
            },
            {
              "@id": "sf:earthinterior",
              "@type": ["skos:Concept"],
              "skos:prefLabel": {"@value": "Earth interior", "@language": "en"},
              "skos:definition": {"@value": "Sampled feature is solid material from within the Earth", "@language": "en"},
              "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
              "skos:broader": [{"@id": "sf:earthenvironment"}],
              "skos:note": {"@value": "fluids in pore space in earth interior sample 'Subsurface fluid reservoir'", "@language": "en"}
            },
            {
              "@id": "sf:earthsurface",
              "@type": ["skos:Concept"],
              "skos:prefLabel": {"@value": "Earth surface", "@language": "en"},
              "skos:definition": {"@value": "Sampled feature is the interface between solid earth and hydrosphere or atmosphere. Includes samples representing things collected on the surface, in the uppermost part of the material below the surface, or air or water directly at the contact with the Earth surface.", "@language": "en"},
              "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
              "skos:broader": [{"@id": "sf:earthenvironment"}],
              "skos:narrowMatch": [{"@id": "http://purl.obolibrary.org/obo/RBO_00000017"}],
              "skos:narrower": [
                {
                  "@id": "sf:lakeriverstreambottom",
                  "@type": ["skos:Concept"],
                  "skos:prefLabel": {"@value": "Lake river or stream bottom", "@language": "en"},
                  "skos:definition": {"@value": "Sampled feature is the interface between the solid Earth interface and a lake or flowing water body.", "@language": "en"},
                  "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
                  "skos:broader": [{"@id": "sf:earthsurface"}],
                  "skos:narrowMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_00000384"}]
                },
                {
                  "@id": "sf:marinewaterbodybottom",
                  "@type": ["skos:Concept"],
                  "skos:prefLabel": {"@value": "Marine water body bottom", "@language": "en"},
                  "skos:altLabel": {"@value": "Sea floor", "@language": "en"},
                  "skos:definition": {"@value": "Sampled feature is the interface between the solid Earth and a marine or brackish water body. Includes benthic boundary layer:  the bottom layer of water and the uppermost layer of sediment directly influenced by the overlying water.", "@language": "en"},
                  "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
                  "skos:broader": [{"@id": "sf:earthsurface"}],
                  "skos:narrowMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_00000482"}]
                },
                {
                  "@id": "sf:subaerialsurfaceenvironment",
                  "@type": ["skos:Concept"],
                  "skos:prefLabel": {"@value": "Subaerial surface environment", "@language": "en"},
                  "skos:definition": {"@value": "sampled feature is the interface between solid Earth and atmosphere.  Sample is collected on the surface, or immediately below surface (zone of bioturbation). Include soil and recently deposited subaerial sediment at the surface.", "@language": "en"},
                  "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
                  "skos:broader": [{"@id": "sf:earthsurface"}],
                  "skos:closeMatch": [{"@id": "http://purl.obolibrary.org/obo/RBO_00000017"}]
                }
              ]
            },
            {
              "@id": "sf:glacierenvironment",
              "@type": ["skos:Concept"],
              "skos:prefLabel": {"@value": "Glacier environment", "@language": "en"},
              "skos:definition": {"@value": "Sampled feature is a glacier, ice sheet, ice shelf, iceberg, or rock or water directly under or on top of such ice.", "@language": "en"},
              "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
              "skos:broader": [{"@id": "sf:earthenvironment"}],
              "skos:narrowMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_00000133"}]
            },
            {
              "@id": "sf:subsurfacefluidreservoir",
              "@type": ["skos:Concept"],
              "skos:prefLabel": {"@value": "Subsurface fluid reservoir", "@language": "en"},
              "skos:definition": {"@value": "Sampled feature is fluid that resides in fractures, intergranular porosity or other open space in the solid earth.", "@language": "en"},
              "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
              "skos:broader": [{"@id": "sf:earthenvironment"}],
              "skos:narrowMatch": [
                {"@id": "http://purl.jp/bio/11/meo/MEO_0000326"},
                {"@id": "http://purl.obolibrary.org/obo/ENVO_00012408"}
              ]
            },
            {
              "@id": "sf:waterbody",
              "@type": ["skos:Concept"],
              "skos:prefLabel": {"@value": "Water body", "@language": "en"},
              "skos:definition": {"@value": "Sampled feature is the Earth's hydrosphere.", "@language": "en"},
              "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
              "skos:broader": [{"@id": "sf:earthenvironment"}],
              "skos:closeMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_00000063"}],
              "skos:narrower": [
                {
                  "@id": "sf:marinewaterbody",
                  "@type": ["skos:Concept"],
                  "skos:prefLabel": {"@value": "Marine environment", "@language": "en"},
                  "skos:definition": {"@value": "Sampled feature is the marine hydrosphere.", "@language": "en"},
                  "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
                  "skos:broader": [{"@id": "sf:waterbody"}],
                  "skos:closeMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_00001999"}]
                },
                {
                  "@id": "sf:terrestrialwaterbody",
                  "@type": ["skos:Concept"],
                  "skos:prefLabel": {"@value": "Terrestrial water body", "@language": "en"},
                  "skos:definition": {"@value": "Sampled feature is terrestrial hydrosphere-- lake, other standing water, or a flowing water body (river, stream..). Include saline water in terrestrial evaporite environments.", "@language": "en"},
                  "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
                  "skos:broader": [{"@id": "sf:waterbody"}]
                }
              ]
            }
          ]
        },
        {
          "@id": "sf:extraterrestrialenvironment",
          "@type": ["skos:Concept"],
          "skos:prefLabel": {"@value": "Extraterrestrial environment", "@language": "en"},
          "skos:definition": {"@value": "Sampled feature is the environment outside of solid earth, hydrosphere, or atmosphere.", "@language": "en"},
          "skos:inScheme": {"@id": "sf:sampledfeaturevocabulary"},
          "skos:broader": [{"@id": "sf:anysampledfeature"}],
          "skos:closeMatch": [{"@id": "http://purl.bioontology.org/ontology/MESH/D005118"}]
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
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "dcterms": "http://purl.org/dc/terms/",
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFCodelist/context.jsonld",
    {
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "dcterms": "http://purl.org/dc/terms/",
      "schema": "http://schema.org/",
      "sf": "https://w3id.org/isample/vocabulary/sampledfeature/"
    }
  ],
  "@id": "sf:sampledfeaturevocabulary",
  "@type": [
    "skos:ConceptScheme"
  ],
  "skos:prefLabel": {
    "@value": "Sampled Feature Type vocabulary",
    "@language": "en"
  },
  "skos:definition": {
    "@value": "Categories to specify the broad context that a sample is intended to represent.",
    "@language": "en"
  },
  "dcterms:created": "2021-03-17",
  "dcterms:modified": "2024-04-19",
  "dcterms:creator": {
    "@id": "https://orcid.org/0000-0001-6041-5302"
  },
  "dcterms:license": {
    "@id": "https://creativecommons.org/licenses/by/4.0/legalcode"
  },
  "skos:historyNote": [
    {
      "@value": "2021-07-09  Remove Marine biome, Subaerial terrestrial environment, Subaqueous terrestrial environment per github issue https://github.com/isamplesorg/metadata/issues/41. Make Experiment setting and Laboratory or curatorial environment subclasses of Active human occupation site.",
      "@language": "en"
    },
    {
      "@value": "2021-12-10 SMR add missing skos:inScheme statements",
      "@language": "en"
    },
    {
      "@value": "2022-01-07 SMR change to https://w3id.org/isample/ uri base, make the ConceptScheme an ontology as well. For uploading to ESIP COR and w3id resolution redirect set up. Add some mappings to other ontologies using seeAlso, closeMatch, narrowMatch.",
      "@language": "en"
    },
    {
      "@value": "2022-03-11 SMR change definitions from rdfs:comment to skos:definition. Minor fixes in definitions. Add skos matches to URIs from other vocabularies. Fix typo in glacierenvrionment URI (changed the URI to glacierenvironment)",
      "@language": "en"
    },
    {
      "@value": "2022-09-07 SMR update some of the skos mappings to other vocabularies; remove references to other vocabularies as NamedIndividual. Remove rocksample class, it was not linked in hierarchy and inconsistent with design.",
      "@language": "en"
    },
    {
      "@value": "2022-09-30 add biological entity as sampled feature, per issue https://github.com/isamplesorg/metadata/issues/107. This update was lost at some point and added back in 2022-12-09.",
      "@language": "en"
    },
    {
      "@value": "2023-11-05 SMR update version to 1.0, prep for release",
      "@language": "en"
    },
    {
      "@value": "2024-04-19 SMR update definitions to remove use of 'specimen'. Edit some definitions for better clarity",
      "@language": "en"
    },
    {
      "@value": "2024-09-13 remove version numbers from URI",
      "@language": "en"
    }
  ],
  "skos:hasTopConcept": [
    {
      "@id": "sf:anysampledfeature",
      "@type": [
        "skos:Concept"
      ],
      "skos:prefLabel": {
        "@value": "Any sampled feature",
        "@language": "en"
      },
      "skos:definition": {
        "@value": "Any thing that can be sampled. Top concept in sampled feature type vocabulary.",
        "@language": "en"
      },
      "skos:inScheme": {
        "@id": "sf:sampledfeaturevocabulary"
      },
      "skos:topConceptOf": {
        "@id": "sf:sampledfeaturevocabulary"
      },
      "skos:narrower": [
        {
          "@id": "sf:anthropogenicenvironment",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": {
            "@value": "Anthropogenic environment",
            "@language": "en"
          },
          "skos:definition": {
            "@value": "Sampled feature is produced by or related to human activity past or present.",
            "@language": "en"
          },
          "skos:inScheme": {
            "@id": "sf:sampledfeaturevocabulary"
          },
          "skos:broader": [
            {
              "@id": "sf:anysampledfeature"
            }
          ],
          "skos:closeMatch": [
            {
              "@id": "http://purl.obolibrary.org/obo/ENVO_01000313"
            }
          ],
          "skos:narrower": [
            {
              "@id": "sf:activehumanoccupationsite",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": {
                "@value": "Active human occupation site",
                "@language": "en"
              },
              "skos:definition": {
                "@value": "sampled feature is a site at which there are ongoing human activities",
                "@language": "en"
              },
              "skos:inScheme": {
                "@id": "sf:sampledfeaturevocabulary"
              },
              "skos:broader": [
                {
                  "@id": "sf:anthropogenicenvironment"
                }
              ],
              "skos:narrower": [
                {
                  "@id": "sf:experimentsetting",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": {
                    "@value": "Experiment setting",
                    "@language": "en"
                  },
                  "skos:definition": {
                    "@value": "Sampled feature is an experimental set up that produced the sample; the sample is the product of the experiment.",
                    "@language": "en"
                  },
                  "skos:inScheme": {
                    "@id": "sf:sampledfeaturevocabulary"
                  },
                  "skos:broader": [
                    {
                      "@id": "sf:activehumanoccupationsite"
                    }
                  ]
                },
                {
                  "@id": "sf:laboratorycuratorialenvironment",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": {
                    "@value": "Laboratory or curatorial environment",
                    "@language": "en"
                  },
                  "skos:definition": {
                    "@value": "Sampled feature is a laboratory or other research site, collected with intention of characterizing the environment in which data are collected or other research conducted, that might affect results or safety; e.g. lab blank measurements.",
                    "@language": "en"
                  },
                  "skos:inScheme": {
                    "@id": "sf:sampledfeaturevocabulary"
                  },
                  "skos:broader": [
                    {
                      "@id": "sf:activehumanoccupationsite"
                    }
                  ],
                  "skos:closeMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/ENVO_01001405"
                    }
                  ]
                }
              ]
            },
            {
              "@id": "sf:pasthumanoccupationsite",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": {
                "@value": "Site of past human activities",
                "@language": "en"
              },
              "skos:definition": {
                "@value": "sampled feature is a place where humans have been and left evidence of their activity. Includes prehistoric and paleo hominid sites",
                "@language": "en"
              },
              "skos:inScheme": {
                "@id": "sf:sampledfeaturevocabulary"
              },
              "skos:broader": [
                {
                  "@id": "sf:anthropogenicenvironment"
                }
              ]
            }
          ]
        },
        {
          "@id": "sf:biologicalentity",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": {
            "@value": "Biological entity",
            "@language": "en"
          },
          "skos:definition": {
            "@value": "Sampled feature is an organism. Use for samples that represent some species of organism as the proximate sampled feature, not the environment that the organism inhabits.",
            "@language": "en"
          },
          "skos:inScheme": {
            "@id": "sf:sampledfeaturevocabulary"
          },
          "skos:broader": [
            {
              "@id": "sf:anysampledfeature"
            }
          ],
          "skos:note": {
            "@value": "domain specific vocabulary extensions will be useful to distinguish samples from different phyla/order/class...",
            "@language": "en"
          }
        },
        {
          "@id": "sf:earthenvironment",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": {
            "@value": "Earth environment",
            "@language": "en"
          },
          "skos:definition": {
            "@value": "Sampled feature is the natural Earth environment",
            "@language": "en"
          },
          "skos:inScheme": {
            "@id": "sf:sampledfeaturevocabulary"
          },
          "skos:broader": [
            {
              "@id": "sf:anysampledfeature"
            }
          ],
          "skos:narrower": [
            {
              "@id": "sf:atmosphere",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": {
                "@value": "Atmosphere",
                "@language": "en"
              },
              "skos:definition": {
                "@value": "Sampled feature is the Earth's atmosphere",
                "@language": "en"
              },
              "skos:inScheme": {
                "@id": "sf:sampledfeaturevocabulary"
              },
              "skos:broader": [
                {
                  "@id": "sf:earthenvironment"
                }
              ]
            },
            {
              "@id": "sf:earthinterior",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": {
                "@value": "Earth interior",
                "@language": "en"
              },
              "skos:definition": {
                "@value": "Sampled feature is solid material from within the Earth",
                "@language": "en"
              },
              "skos:inScheme": {
                "@id": "sf:sampledfeaturevocabulary"
              },
              "skos:broader": [
                {
                  "@id": "sf:earthenvironment"
                }
              ],
              "skos:note": {
                "@value": "fluids in pore space in earth interior sample 'Subsurface fluid reservoir'",
                "@language": "en"
              }
            },
            {
              "@id": "sf:earthsurface",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": {
                "@value": "Earth surface",
                "@language": "en"
              },
              "skos:definition": {
                "@value": "Sampled feature is the interface between solid earth and hydrosphere or atmosphere. Includes samples representing things collected on the surface, in the uppermost part of the material below the surface, or air or water directly at the contact with the Earth surface.",
                "@language": "en"
              },
              "skos:inScheme": {
                "@id": "sf:sampledfeaturevocabulary"
              },
              "skos:broader": [
                {
                  "@id": "sf:earthenvironment"
                }
              ],
              "skos:narrowMatch": [
                {
                  "@id": "http://purl.obolibrary.org/obo/RBO_00000017"
                }
              ],
              "skos:narrower": [
                {
                  "@id": "sf:lakeriverstreambottom",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": {
                    "@value": "Lake river or stream bottom",
                    "@language": "en"
                  },
                  "skos:definition": {
                    "@value": "Sampled feature is the interface between the solid Earth interface and a lake or flowing water body.",
                    "@language": "en"
                  },
                  "skos:inScheme": {
                    "@id": "sf:sampledfeaturevocabulary"
                  },
                  "skos:broader": [
                    {
                      "@id": "sf:earthsurface"
                    }
                  ],
                  "skos:narrowMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/ENVO_00000384"
                    }
                  ]
                },
                {
                  "@id": "sf:marinewaterbodybottom",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": {
                    "@value": "Marine water body bottom",
                    "@language": "en"
                  },
                  "skos:altLabel": {
                    "@value": "Sea floor",
                    "@language": "en"
                  },
                  "skos:definition": {
                    "@value": "Sampled feature is the interface between the solid Earth and a marine or brackish water body. Includes benthic boundary layer:  the bottom layer of water and the uppermost layer of sediment directly influenced by the overlying water.",
                    "@language": "en"
                  },
                  "skos:inScheme": {
                    "@id": "sf:sampledfeaturevocabulary"
                  },
                  "skos:broader": [
                    {
                      "@id": "sf:earthsurface"
                    }
                  ],
                  "skos:narrowMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/ENVO_00000482"
                    }
                  ]
                },
                {
                  "@id": "sf:subaerialsurfaceenvironment",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": {
                    "@value": "Subaerial surface environment",
                    "@language": "en"
                  },
                  "skos:definition": {
                    "@value": "sampled feature is the interface between solid Earth and atmosphere.  Sample is collected on the surface, or immediately below surface (zone of bioturbation). Include soil and recently deposited subaerial sediment at the surface.",
                    "@language": "en"
                  },
                  "skos:inScheme": {
                    "@id": "sf:sampledfeaturevocabulary"
                  },
                  "skos:broader": [
                    {
                      "@id": "sf:earthsurface"
                    }
                  ],
                  "skos:closeMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/RBO_00000017"
                    }
                  ]
                }
              ]
            },
            {
              "@id": "sf:glacierenvironment",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": {
                "@value": "Glacier environment",
                "@language": "en"
              },
              "skos:definition": {
                "@value": "Sampled feature is a glacier, ice sheet, ice shelf, iceberg, or rock or water directly under or on top of such ice.",
                "@language": "en"
              },
              "skos:inScheme": {
                "@id": "sf:sampledfeaturevocabulary"
              },
              "skos:broader": [
                {
                  "@id": "sf:earthenvironment"
                }
              ],
              "skos:narrowMatch": [
                {
                  "@id": "http://purl.obolibrary.org/obo/ENVO_00000133"
                }
              ]
            },
            {
              "@id": "sf:subsurfacefluidreservoir",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": {
                "@value": "Subsurface fluid reservoir",
                "@language": "en"
              },
              "skos:definition": {
                "@value": "Sampled feature is fluid that resides in fractures, intergranular porosity or other open space in the solid earth.",
                "@language": "en"
              },
              "skos:inScheme": {
                "@id": "sf:sampledfeaturevocabulary"
              },
              "skos:broader": [
                {
                  "@id": "sf:earthenvironment"
                }
              ],
              "skos:narrowMatch": [
                {
                  "@id": "http://purl.jp/bio/11/meo/MEO_0000326"
                },
                {
                  "@id": "http://purl.obolibrary.org/obo/ENVO_00012408"
                }
              ]
            },
            {
              "@id": "sf:waterbody",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": {
                "@value": "Water body",
                "@language": "en"
              },
              "skos:definition": {
                "@value": "Sampled feature is the Earth's hydrosphere.",
                "@language": "en"
              },
              "skos:inScheme": {
                "@id": "sf:sampledfeaturevocabulary"
              },
              "skos:broader": [
                {
                  "@id": "sf:earthenvironment"
                }
              ],
              "skos:closeMatch": [
                {
                  "@id": "http://purl.obolibrary.org/obo/ENVO_00000063"
                }
              ],
              "skos:narrower": [
                {
                  "@id": "sf:marinewaterbody",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": {
                    "@value": "Marine environment",
                    "@language": "en"
                  },
                  "skos:definition": {
                    "@value": "Sampled feature is the marine hydrosphere.",
                    "@language": "en"
                  },
                  "skos:inScheme": {
                    "@id": "sf:sampledfeaturevocabulary"
                  },
                  "skos:broader": [
                    {
                      "@id": "sf:waterbody"
                    }
                  ],
                  "skos:closeMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/ENVO_00001999"
                    }
                  ]
                },
                {
                  "@id": "sf:terrestrialwaterbody",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": {
                    "@value": "Terrestrial water body",
                    "@language": "en"
                  },
                  "skos:definition": {
                    "@value": "Sampled feature is terrestrial hydrosphere-- lake, other standing water, or a flowing water body (river, stream..). Include saline water in terrestrial evaporite environments.",
                    "@language": "en"
                  },
                  "skos:inScheme": {
                    "@id": "sf:sampledfeaturevocabulary"
                  },
                  "skos:broader": [
                    {
                      "@id": "sf:waterbody"
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "@id": "sf:extraterrestrialenvironment",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": {
            "@value": "Extraterrestrial environment",
            "@language": "en"
          },
          "skos:definition": {
            "@value": "Sampled feature is the environment outside of solid earth, hydrosphere, or atmosphere.",
            "@language": "en"
          },
          "skos:inScheme": {
            "@id": "sf:sampledfeaturevocabulary"
          },
          "skos:broader": [
            {
              "@id": "sf:anysampledfeature"
            }
          ],
          "skos:closeMatch": [
            {
              "@id": "http://purl.bioontology.org/ontology/MESH/D005118"
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
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sf: <https://w3id.org/isample/vocabulary/sampledfeature/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

sf:atmosphere a skos:Concept ;
    skos:broader sf:earthenvironment ;
    skos:definition "Sampled feature is the Earth's atmosphere"@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:prefLabel "Atmosphere"@en .

sf:biologicalentity a skos:Concept ;
    skos:broader sf:anysampledfeature ;
    skos:definition "Sampled feature is an organism. Use for samples that represent some species of organism as the proximate sampled feature, not the environment that the organism inhabits."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:note "domain specific vocabulary extensions will be useful to distinguish samples from different phyla/order/class..."@en ;
    skos:prefLabel "Biological entity"@en .

sf:earthinterior a skos:Concept ;
    skos:broader sf:earthenvironment ;
    skos:definition "Sampled feature is solid material from within the Earth"@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:note "fluids in pore space in earth interior sample 'Subsurface fluid reservoir'"@en ;
    skos:prefLabel "Earth interior"@en .

sf:experimentsetting a skos:Concept ;
    skos:broader sf:activehumanoccupationsite ;
    skos:definition "Sampled feature is an experimental set up that produced the sample; the sample is the product of the experiment."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:prefLabel "Experiment setting"@en .

sf:extraterrestrialenvironment a skos:Concept ;
    skos:broader sf:anysampledfeature ;
    skos:closeMatch <http://purl.bioontology.org/ontology/MESH/D005118> ;
    skos:definition "Sampled feature is the environment outside of solid earth, hydrosphere, or atmosphere."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:prefLabel "Extraterrestrial environment"@en .

sf:glacierenvironment a skos:Concept ;
    skos:broader sf:earthenvironment ;
    skos:definition "Sampled feature is a glacier, ice sheet, ice shelf, iceberg, or rock or water directly under or on top of such ice."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrowMatch <http://purl.obolibrary.org/obo/ENVO_00000133> ;
    skos:prefLabel "Glacier environment"@en .

sf:laboratorycuratorialenvironment a skos:Concept ;
    skos:broader sf:activehumanoccupationsite ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_01001405> ;
    skos:definition "Sampled feature is a laboratory or other research site, collected with intention of characterizing the environment in which data are collected or other research conducted, that might affect results or safety; e.g. lab blank measurements."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:prefLabel "Laboratory or curatorial environment"@en .

sf:lakeriverstreambottom a skos:Concept ;
    skos:broader sf:earthsurface ;
    skos:definition "Sampled feature is the interface between the solid Earth interface and a lake or flowing water body."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrowMatch <http://purl.obolibrary.org/obo/ENVO_00000384> ;
    skos:prefLabel "Lake river or stream bottom"@en .

sf:marinewaterbody a skos:Concept ;
    skos:broader sf:waterbody ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_00001999> ;
    skos:definition "Sampled feature is the marine hydrosphere."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:prefLabel "Marine environment"@en .

sf:marinewaterbodybottom a skos:Concept ;
    skos:altLabel "Sea floor"@en ;
    skos:broader sf:earthsurface ;
    skos:definition "Sampled feature is the interface between the solid Earth and a marine or brackish water body. Includes benthic boundary layer:  the bottom layer of water and the uppermost layer of sediment directly influenced by the overlying water."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrowMatch <http://purl.obolibrary.org/obo/ENVO_00000482> ;
    skos:prefLabel "Marine water body bottom"@en .

sf:pasthumanoccupationsite a skos:Concept ;
    skos:broader sf:anthropogenicenvironment ;
    skos:definition "sampled feature is a place where humans have been and left evidence of their activity. Includes prehistoric and paleo hominid sites"@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:prefLabel "Site of past human activities"@en .

sf:subaerialsurfaceenvironment a skos:Concept ;
    skos:broader sf:earthsurface ;
    skos:closeMatch <http://purl.obolibrary.org/obo/RBO_00000017> ;
    skos:definition "sampled feature is the interface between solid Earth and atmosphere.  Sample is collected on the surface, or immediately below surface (zone of bioturbation). Include soil and recently deposited subaerial sediment at the surface."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:prefLabel "Subaerial surface environment"@en .

sf:subsurfacefluidreservoir a skos:Concept ;
    skos:broader sf:earthenvironment ;
    skos:definition "Sampled feature is fluid that resides in fractures, intergranular porosity or other open space in the solid earth."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrowMatch <http://purl.jp/bio/11/meo/MEO_0000326>,
        <http://purl.obolibrary.org/obo/ENVO_00012408> ;
    skos:prefLabel "Subsurface fluid reservoir"@en .

sf:terrestrialwaterbody a skos:Concept ;
    skos:broader sf:waterbody ;
    skos:definition "Sampled feature is terrestrial hydrosphere-- lake, other standing water, or a flowing water body (river, stream..). Include saline water in terrestrial evaporite environments."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:prefLabel "Terrestrial water body"@en .

sf:activehumanoccupationsite a skos:Concept ;
    skos:broader sf:anthropogenicenvironment ;
    skos:definition "sampled feature is a site at which there are ongoing human activities"@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrower sf:experimentsetting,
        sf:laboratorycuratorialenvironment ;
    skos:prefLabel "Active human occupation site"@en .

sf:anthropogenicenvironment a skos:Concept ;
    skos:broader sf:anysampledfeature ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_01000313> ;
    skos:definition "Sampled feature is produced by or related to human activity past or present."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrower sf:activehumanoccupationsite,
        sf:pasthumanoccupationsite ;
    skos:prefLabel "Anthropogenic environment"@en .

sf:waterbody a skos:Concept ;
    skos:broader sf:earthenvironment ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_00000063> ;
    skos:definition "Sampled feature is the Earth's hydrosphere."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrower sf:marinewaterbody,
        sf:terrestrialwaterbody ;
    skos:prefLabel "Water body"@en .

sf:earthsurface a skos:Concept ;
    skos:broader sf:earthenvironment ;
    skos:definition "Sampled feature is the interface between solid earth and hydrosphere or atmosphere. Includes samples representing things collected on the surface, in the uppermost part of the material below the surface, or air or water directly at the contact with the Earth surface."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrowMatch <http://purl.obolibrary.org/obo/RBO_00000017> ;
    skos:narrower sf:lakeriverstreambottom,
        sf:marinewaterbodybottom,
        sf:subaerialsurfaceenvironment ;
    skos:prefLabel "Earth surface"@en .

sf:anysampledfeature a skos:Concept ;
    skos:definition "Any thing that can be sampled. Top concept in sampled feature type vocabulary."@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrower sf:anthropogenicenvironment,
        sf:biologicalentity,
        sf:earthenvironment,
        sf:extraterrestrialenvironment ;
    skos:prefLabel "Any sampled feature"@en ;
    skos:topConceptOf sf:sampledfeaturevocabulary .

sf:earthenvironment a skos:Concept ;
    skos:broader sf:anysampledfeature ;
    skos:definition "Sampled feature is the natural Earth environment"@en ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrower sf:atmosphere,
        sf:earthinterior,
        sf:earthsurface,
        sf:glacierenvironment,
        sf:subsurfacefluidreservoir,
        sf:waterbody ;
    skos:prefLabel "Earth environment"@en .

sf:sampledfeaturevocabulary a skos:ConceptScheme ;
    dcterms:created "2021-03-17" ;
    dcterms:creator <https://orcid.org/0000-0001-6041-5302> ;
    dcterms:license <https://creativecommons.org/licenses/by/4.0/legalcode> ;
    dcterms:modified "2024-04-19" ;
    skos:definition "Categories to specify the broad context that a sample is intended to represent."@en ;
    skos:hasTopConcept sf:anysampledfeature ;
    skos:historyNote "2021-07-09  Remove Marine biome, Subaerial terrestrial environment, Subaqueous terrestrial environment per github issue https://github.com/isamplesorg/metadata/issues/41. Make Experiment setting and Laboratory or curatorial environment subclasses of Active human occupation site."@en,
        "2021-12-10 SMR add missing skos:inScheme statements"@en,
        "2022-01-07 SMR change to https://w3id.org/isample/ uri base, make the ConceptScheme an ontology as well. For uploading to ESIP COR and w3id resolution redirect set up. Add some mappings to other ontologies using seeAlso, closeMatch, narrowMatch."@en,
        "2022-03-11 SMR change definitions from rdfs:comment to skos:definition. Minor fixes in definitions. Add skos matches to URIs from other vocabularies. Fix typo in glacierenvrionment URI (changed the URI to glacierenvironment)"@en,
        "2022-09-07 SMR update some of the skos mappings to other vocabularies; remove references to other vocabularies as NamedIndividual. Remove rocksample class, it was not linked in hierarchy and inconsistent with design."@en,
        "2022-09-30 add biological entity as sampled feature, per issue https://github.com/isamplesorg/metadata/issues/107. This update was lost at some point and added back in 2022-12-09."@en,
        "2023-11-05 SMR update version to 1.0, prep for release"@en,
        "2024-04-19 SMR update definitions to remove use of 'specimen'. Edit some definitions for better clarity"@en,
        "2024-09-13 remove version numbers from URI"@en ;
    skos:prefLabel "Sampled Feature Type vocabulary"@en .


```


### CDIF Codelist minimal example
iSamples Materials vocabulary with only mandatory properties:
@id, @type, prefLabel, definition, inScheme, broader, hasTopConcept.
No optional properties (notation, altLabel, mappings, notes, DC metadata).
#### json
```json
{
  "@context": {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "mat": "https://w3id.org/isample/vocabulary/material/"
  },
  "@id": "mat:materialsvocabulary",
  "@type": ["skos:ConceptScheme"],
  "skos:prefLabel": "iSamples Materials Vocabulary",
  "skos:hasTopConcept": [
    {
      "@id": "mat:material",
      "@type": ["skos:Concept"],
      "skos:prefLabel": "Material",
      "skos:definition": "Top Concept in iSamples Material Category scheme",
      "skos:inScheme": {"@id": "mat:materialsvocabulary"},
      "skos:narrower": [
        {
          "@id": "mat:anyanthropogenicmaterial",
          "@type": ["skos:Concept"],
          "skos:prefLabel": "Anthropogenic material",
          "skos:definition": "Material produced by human activity.",
          "skos:inScheme": {"@id": "mat:materialsvocabulary"},
          "skos:broader": [{"@id": "mat:material"}]
        },
        {
          "@id": "mat:anyice",
          "@type": ["skos:Concept"],
          "skos:prefLabel": "Any ice",
          "skos:definition": "A material that is in a solid state under the temperature and pressure conditions of the preserved sample, but is a liquid or gas at Standard Temperature and Pressure.",
          "skos:inScheme": {"@id": "mat:materialsvocabulary"},
          "skos:broader": [{"@id": "mat:material"}]
        },
        {
          "@id": "mat:biogenicnonorganicmaterial",
          "@type": ["skos:Concept"],
          "skos:prefLabel": "Biogenic non-organic material",
          "skos:definition": "Material produced by an organism but not composed of very large molecules of biological origin.",
          "skos:inScheme": {"@id": "mat:materialsvocabulary"},
          "skos:broader": [{"@id": "mat:material"}]
        },
        {
          "@id": "mat:earthmaterial",
          "@type": ["skos:Concept"],
          "skos:prefLabel": "Natural Solid Material",
          "skos:definition": "A naturally occurring solid material that is not anthropogenic, biogenic, or ice.",
          "skos:inScheme": {"@id": "mat:materialsvocabulary"},
          "skos:broader": [{"@id": "mat:material"}]
        },
        {
          "@id": "mat:fluid",
          "@type": ["skos:Concept"],
          "skos:prefLabel": "Fluid material",
          "skos:definition": "Substance that continually deforms (flows) under an applied shear stress, or external force.",
          "skos:inScheme": {"@id": "mat:materialsvocabulary"},
          "skos:broader": [{"@id": "mat:material"}]
        },
        {
          "@id": "mat:organicmaterial",
          "@type": ["skos:Concept"],
          "skos:prefLabel": "Organic material",
          "skos:definition": "Material derived from living organisms and composed primarily of one or more very large molecules of biological origin.",
          "skos:inScheme": {"@id": "mat:materialsvocabulary"},
          "skos:broader": [{"@id": "mat:material"}]
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
      "skos": "http://www.w3.org/2004/02/skos/core#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFCodelist/context.jsonld",
    {
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "mat": "https://w3id.org/isample/vocabulary/material/"
    }
  ],
  "@id": "mat:materialsvocabulary",
  "@type": [
    "skos:ConceptScheme"
  ],
  "skos:prefLabel": "iSamples Materials Vocabulary",
  "skos:hasTopConcept": [
    {
      "@id": "mat:material",
      "@type": [
        "skos:Concept"
      ],
      "skos:prefLabel": "Material",
      "skos:definition": "Top Concept in iSamples Material Category scheme",
      "skos:inScheme": {
        "@id": "mat:materialsvocabulary"
      },
      "skos:narrower": [
        {
          "@id": "mat:anyanthropogenicmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Anthropogenic material",
          "skos:definition": "Material produced by human activity.",
          "skos:inScheme": {
            "@id": "mat:materialsvocabulary"
          },
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ]
        },
        {
          "@id": "mat:anyice",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Any ice",
          "skos:definition": "A material that is in a solid state under the temperature and pressure conditions of the preserved sample, but is a liquid or gas at Standard Temperature and Pressure.",
          "skos:inScheme": {
            "@id": "mat:materialsvocabulary"
          },
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ]
        },
        {
          "@id": "mat:biogenicnonorganicmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Biogenic non-organic material",
          "skos:definition": "Material produced by an organism but not composed of very large molecules of biological origin.",
          "skos:inScheme": {
            "@id": "mat:materialsvocabulary"
          },
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ]
        },
        {
          "@id": "mat:earthmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Natural Solid Material",
          "skos:definition": "A naturally occurring solid material that is not anthropogenic, biogenic, or ice.",
          "skos:inScheme": {
            "@id": "mat:materialsvocabulary"
          },
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ]
        },
        {
          "@id": "mat:fluid",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Fluid material",
          "skos:definition": "Substance that continually deforms (flows) under an applied shear stress, or external force.",
          "skos:inScheme": {
            "@id": "mat:materialsvocabulary"
          },
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ]
        },
        {
          "@id": "mat:organicmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Organic material",
          "skos:definition": "Material derived from living organisms and composed primarily of one or more very large molecules of biological origin.",
          "skos:inScheme": {
            "@id": "mat:materialsvocabulary"
          },
          "skos:broader": [
            {
              "@id": "mat:material"
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
@prefix mat: <https://w3id.org/isample/vocabulary/material/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

mat:anyanthropogenicmaterial a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "Material produced by human activity." ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Anthropogenic material" .

mat:anyice a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "A material that is in a solid state under the temperature and pressure conditions of the preserved sample, but is a liquid or gas at Standard Temperature and Pressure." ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Any ice" .

mat:biogenicnonorganicmaterial a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "Material produced by an organism but not composed of very large molecules of biological origin." ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Biogenic non-organic material" .

mat:earthmaterial a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "A naturally occurring solid material that is not anthropogenic, biogenic, or ice." ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Natural Solid Material" .

mat:fluid a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "Substance that continually deforms (flows) under an applied shear stress, or external force." ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Fluid material" .

mat:organicmaterial a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "Material derived from living organisms and composed primarily of one or more very large molecules of biological origin." ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Organic material" .

mat:material a skos:Concept ;
    skos:definition "Top Concept in iSamples Material Category scheme" ;
    skos:inScheme mat:materialsvocabulary ;
    skos:narrower mat:anyanthropogenicmaterial,
        mat:anyice,
        mat:biogenicnonorganicmaterial,
        mat:earthmaterial,
        mat:fluid,
        mat:organicmaterial ;
    skos:prefLabel "Material" .

mat:materialsvocabulary a skos:ConceptScheme ;
    skos:hasTopConcept mat:material ;
    skos:prefLabel "iSamples Materials Vocabulary" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: CDIF Codelist profile
description: 'CDIF profile for controlled vocabulary codelists implemented as SKOS
  ConceptSchemes. Composes skosConceptScheme and skosConcept building blocks with
  additional constraints: concepts must have resolvable @id identifiers, skos:inScheme,
  and skos:definition; the scheme must identify top concepts via skos:hasTopConcept;
  hierarchical concepts must declare skos:broader.'
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConceptScheme/schema.yaml
- type: object
  properties:
    '@id':
      type: string
      description: Globally unique, resolvable URI for the concept scheme.
    skos:hasTopConcept:
      description: Top-level concepts that have no skos:broader in this scheme. Required
        for hierarchical codelists.
      type: array
      minItems: 1
      items:
        anyOf:
        - $ref: '#/$defs/CdifCodelistConcept'
        - type: object
          properties:
            '@id':
              type: string
          required:
          - '@id'
  required:
  - '@id'
  - skos:hasTopConcept
$defs:
  CdifCodelistConcept:
    description: A SKOS Concept constrained for CDIF codelist use. Must have a resolvable
      @id, skos:inScheme, skos:definition, and skos:prefLabel.
    allOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
    - type: object
      properties:
        '@id':
          type: string
          description: Globally unique, resolvable URI for this concept.
        skos:inScheme:
          description: The concept scheme this concept belongs to. Required for CDIF
            codelist concepts.
          anyOf:
          - type: object
            properties:
              '@id':
                type: string
            required:
            - '@id'
          - type: array
            items:
              type: object
              properties:
                '@id':
                  type: string
              required:
              - '@id'
        skos:definition:
          description: Formal definition of this concept. Required for CDIF codelist
            concepts. String or language-tagged values.
          anyOf:
          - type: string
          - type: array
            items:
              anyOf:
              - type: string
              - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml#/$defs/LanguageTaggedValue
        skos:narrower:
          description: Narrower (child) concepts. If present, items must also conform
            to CdifCodelistConcept constraints.
          type: array
          items:
            anyOf:
            - type: object
              properties:
                '@id':
                  type: string
              required:
              - '@id'
            - $ref: '#/$defs/CdifCodelistConcept'
      required:
      - '@id'
      - skos:inScheme
      - skos:definition
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  dcterms: http://purl.org/dc/terms/
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFCodelist/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFCodelist/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dcterms": "http://purl.org/dc/terms/",
    "schema": "http://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFCodelist/context.jsonld)

## Sources

* [W3C SKOS Reference](https://www.w3.org/TR/skos-reference/)
* [CDIF Codelist specification](https://github.com/Cross-Domain-Interoperability-Framework/codelist)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifProfiles/CDIFCodelist`

