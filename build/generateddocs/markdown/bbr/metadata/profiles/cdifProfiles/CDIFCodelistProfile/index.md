
# CDIF Codelist (Schema)

`cdif.bbr.metadata.profiles.cdifProfiles.CDIFCodelistProfile` *v0.1*

CDIF profile for controlled vocabulary codelists as SKOS ConceptSchemes. Requires concepts to have resolvable @id identifiers, skos:inScheme, skos:definition, and skos:prefLabel. Scheme must declare skos:hasTopConcept. Includes SHACL validation shapes.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Codelist Profile

A CDIF profile for controlled vocabulary codelists implemented as SKOS ConceptSchemes.

### ConceptScheme requirements
- Must have a globally unique, resolvable `@id` URI
- Must have at least one `skos:prefLabel`
- Must declare top concepts via `skos:hasTopConcept`
- Must have `schema:identifier`, `schema:dateModified`, and either `schema:license` or `schema:conditionsOfAccess` (CDIF Core metadata properties take precedence over equivalent dcterms properties)

### Concept requirements (beyond base SKOS)
- Must have a globally unique, resolvable `@id` URI
- Must have `skos:inScheme` linking to the containing ConceptScheme
- Must have at least one `skos:prefLabel` (at most one per language)
- Must have at least one `skos:definition`
- `skos:notation` is optional but must be unique within the scheme if used
- `skos:altLabel` and other SKOS properties are optional

### Bidirectional hierarchy requirement

CDIF codelists require concept hierarchies to be expressed in **both directions** — `skos:narrower` and `skos:broader` must both be explicit:

- **`skos:narrower`** is needed because the JSON-LD tree structure is rooted at `skos:hasTopConcept`. Without `skos:narrower`, child concepts cannot be reached by traversing the JSON document tree from the root. This is the property used to build the inline hierarchy in the JSON serialization.

- **`skos:broader`** is needed for upward navigation and for building display trees in applications. Many SKOS consumers (vocabulary browsers, classification tools, thesaurus managers) expect `skos:broader` to be present and use it as the primary hierarchy traversal property.

Any concept that appears as a value of `skos:narrower` on another concept **must** also declare `skos:broader` pointing back to its parent. Top concepts (those listed in `skos:hasTopConcept`) should not have `skos:broader` within the scheme.

This constraint is enforced by:
- **JSON Schema**: inline concepts within `skos:narrower` require `skos:broader` (via `allOf` with `required`)
- **SHACL**: `narrowerImpliesBroaderShape` uses a SPARQL target to find concepts that are objects of `skos:narrower` and requires `skos:broader` with `minCount 1`

### Array convention for repeatable properties

The CDIF convention that properties with repeating values (0..* or 1..* cardinality) are always serialized as JSON arrays, even when there is only a single value is not followed in this profile. This recognizes standard SKOS practice that allows either a single string or an array of strings for literal values. Consumers will need to test whether a value is a string or an array before iterating.

### Validation
- JSON Schema validates structure and required properties (including bidirectional hierarchy and array types)
- SHACL shapes validate RDF constraints including `sh:uniqueLang` on `skos:prefLabel`, `sh:class skos:ConceptScheme` on `skos:inScheme` targets, and the `skos:narrower` implies `skos:broader` rule

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
  "@type": [
    "skos:ConceptScheme"
  ],
  "skos:prefLabel": "Sampled Feature Type vocabulary",
  "skos:definition": "Categories to specify the broad context that a sample is intended to represent.",
  "schema:identifier": "https://w3id.org/isample/vocabulary/sampledfeature/",
  "schema:dateModified": "2024-04-19",
  "schema:url": "https://w3id.org/isample/vocabulary/sampledfeature/",
  "schema:license": [
    {
      "@id": "https://creativecommons.org/licenses/by/4.0/legalcode"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://orcid.org/0000-0001-6041-5302"
      }
    ]
  },
  "dcterms:created": "2021-03-17",
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
      "skos:prefLabel": "Any sampled feature",
      "skos:definition": "Any thing that can be sampled. Top concept in sampled feature type vocabulary.",
      "skos:inScheme": [
        {
          "@id": "sf:sampledfeaturevocabulary"
        }
      ],
      "skos:topConceptOf": {
        "@id": "sf:sampledfeaturevocabulary"
      },
      "skos:narrower": [
        {
          "@id": "sf:anthropogenicenvironment",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Anthropogenic environment",
          "skos:definition": "Sampled feature is produced by or related to human activity past or present.",
          "skos:inScheme": [
            {
              "@id": "sf:sampledfeaturevocabulary"
            }
          ],
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
              "skos:prefLabel": "Active human occupation site",
              "skos:definition": "sampled feature is a site at which there are ongoing human activities",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
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
                  "skos:prefLabel": "Experiment setting",
                  "skos:definition": "Sampled feature is an experimental set up that produced the sample; the sample is the product of the experiment.",
                  "skos:inScheme": [
                    {
                      "@id": "sf:sampledfeaturevocabulary"
                    }
                  ],
                  "skos:broader": [
                    {
                      "@id": "sf:activehumanoccupationsite"
                    }
                  ],
                  "skos:notation": "experimentsetting"
                },
                {
                  "@id": "sf:laboratorycuratorialenvironment",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": "Laboratory or curatorial environment",
                  "skos:definition": "Sampled feature is a laboratory or other research site, collected with intention of characterizing the environment in which data are collected or other research conducted, that might affect results or safety; e.g. lab blank measurements.",
                  "skos:inScheme": [
                    {
                      "@id": "sf:sampledfeaturevocabulary"
                    }
                  ],
                  "skos:broader": [
                    {
                      "@id": "sf:activehumanoccupationsite"
                    }
                  ],
                  "skos:closeMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/ENVO_01001405"
                    }
                  ],
                  "skos:notation": "laboratorycuratorialenvironment"
                }
              ],
              "skos:notation": "activehumanoccupationsite"
            },
            {
              "@id": "sf:pasthumanoccupationsite",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": "Site of past human activities",
              "skos:definition": "sampled feature is a place where humans have been and left evidence of their activity. Includes prehistoric and paleo hominid sites",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
              "skos:broader": [
                {
                  "@id": "sf:anthropogenicenvironment"
                }
              ],
              "skos:notation": "pasthumanoccupationsite"
            }
          ],
          "skos:notation": "anthropogenicenvironment"
        },
        {
          "@id": "sf:biologicalentity",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Biological entity",
          "skos:definition": "Sampled feature is an organism. Use for samples that represent some species of organism as the proximate sampled feature, not the environment that the organism inhabits.",
          "skos:inScheme": [
            {
              "@id": "sf:sampledfeaturevocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "sf:anysampledfeature"
            }
          ],
          "skos:note": {
            "@value": "domain specific vocabulary extensions will be useful to distinguish samples from different phyla/order/class...",
            "@language": "en"
          },
          "skos:notation": "biologicalentity"
        },
        {
          "@id": "sf:earthenvironment",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Earth environment",
          "skos:definition": "Sampled feature is the natural Earth environment",
          "skos:inScheme": [
            {
              "@id": "sf:sampledfeaturevocabulary"
            }
          ],
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
              "skos:prefLabel": "Atmosphere",
              "skos:definition": "Sampled feature is the Earth's atmosphere",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
              "skos:broader": [
                {
                  "@id": "sf:earthenvironment"
                }
              ],
              "skos:notation": "atmosphere"
            },
            {
              "@id": "sf:earthinterior",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": "Earth interior",
              "skos:definition": "Sampled feature is solid material from within the Earth",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
              "skos:broader": [
                {
                  "@id": "sf:earthenvironment"
                }
              ],
              "skos:note": {
                "@value": "fluids in pore space in earth interior sample 'Subsurface fluid reservoir'",
                "@language": "en"
              },
              "skos:notation": "earthinterior"
            },
            {
              "@id": "sf:earthsurface",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": "Earth surface",
              "skos:definition": "Sampled feature is the interface between solid earth and hydrosphere or atmosphere. Includes samples representing things collected on the surface, in the uppermost part of the material below the surface, or air or water directly at the contact with the Earth surface.",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
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
                  "skos:prefLabel": "Lake river or stream bottom",
                  "skos:definition": "Sampled feature is the interface between the solid Earth interface and a lake or flowing water body.",
                  "skos:inScheme": [
                    {
                      "@id": "sf:sampledfeaturevocabulary"
                    }
                  ],
                  "skos:broader": [
                    {
                      "@id": "sf:earthsurface"
                    }
                  ],
                  "skos:narrowMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/ENVO_00000384"
                    }
                  ],
                  "skos:notation": "lakeriverstreambottom"
                },
                {
                  "@id": "sf:marinewaterbodybottom",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": "Marine water body bottom",
                  "skos:altLabel": {
                    "@value": "Sea floor",
                    "@language": "en"
                  },
                  "skos:definition": "Sampled feature is the interface between the solid Earth and a marine or brackish water body. Includes benthic boundary layer:  the bottom layer of water and the uppermost layer of sediment directly influenced by the overlying water.",
                  "skos:inScheme": [
                    {
                      "@id": "sf:sampledfeaturevocabulary"
                    }
                  ],
                  "skos:broader": [
                    {
                      "@id": "sf:earthsurface"
                    }
                  ],
                  "skos:narrowMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/ENVO_00000482"
                    }
                  ],
                  "skos:notation": "marinewaterbodybottom"
                },
                {
                  "@id": "sf:subaerialsurfaceenvironment",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": "Subaerial surface environment",
                  "skos:definition": "sampled feature is the interface between solid Earth and atmosphere.  Sample is collected on the surface, or immediately below surface (zone of bioturbation). Include soil and recently deposited subaerial sediment at the surface.",
                  "skos:inScheme": [
                    {
                      "@id": "sf:sampledfeaturevocabulary"
                    }
                  ],
                  "skos:broader": [
                    {
                      "@id": "sf:earthsurface"
                    }
                  ],
                  "skos:closeMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/RBO_00000017"
                    }
                  ],
                  "skos:notation": "subaerialsurfaceenvironment"
                }
              ],
              "skos:notation": "earthsurface"
            },
            {
              "@id": "sf:glacierenvironment",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": "Glacier environment",
              "skos:definition": "Sampled feature is a glacier, ice sheet, ice shelf, iceberg, or rock or water directly under or on top of such ice.",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
              "skos:broader": [
                {
                  "@id": "sf:earthenvironment"
                }
              ],
              "skos:narrowMatch": [
                {
                  "@id": "http://purl.obolibrary.org/obo/ENVO_00000133"
                }
              ],
              "skos:notation": "glacierenvironment"
            },
            {
              "@id": "sf:subsurfacefluidreservoir",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": "Subsurface fluid reservoir",
              "skos:definition": "Sampled feature is fluid that resides in fractures, intergranular porosity or other open space in the solid earth.",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
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
              ],
              "skos:notation": "subsurfacefluidreservoir"
            },
            {
              "@id": "sf:waterbody",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": "Water body",
              "skos:definition": "Sampled feature is the Earth's hydrosphere.",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
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
                  "skos:prefLabel": "Marine environment",
                  "skos:definition": "Sampled feature is the marine hydrosphere.",
                  "skos:inScheme": [
                    {
                      "@id": "sf:sampledfeaturevocabulary"
                    }
                  ],
                  "skos:broader": [
                    {
                      "@id": "sf:waterbody"
                    }
                  ],
                  "skos:closeMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/ENVO_00001999"
                    }
                  ],
                  "skos:notation": "marinewaterbody"
                },
                {
                  "@id": "sf:terrestrialwaterbody",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": "Terrestrial water body",
                  "skos:definition": "Sampled feature is terrestrial hydrosphere-- lake, other standing water, or a flowing water body (river, stream..). Include saline water in terrestrial evaporite environments.",
                  "skos:inScheme": [
                    {
                      "@id": "sf:sampledfeaturevocabulary"
                    }
                  ],
                  "skos:broader": [
                    {
                      "@id": "sf:waterbody"
                    }
                  ],
                  "skos:notation": "terrestrialwaterbody"
                }
              ],
              "skos:notation": "waterbody"
            }
          ],
          "skos:notation": "earthenvironment"
        },
        {
          "@id": "sf:extraterrestrialenvironment",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Extraterrestrial environment",
          "skos:definition": "Sampled feature is the environment outside of solid earth, hydrosphere, or atmosphere.",
          "skos:inScheme": [
            {
              "@id": "sf:sampledfeaturevocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "sf:anysampledfeature"
            }
          ],
          "skos:closeMatch": [
            {
              "@id": "http://purl.bioontology.org/ontology/MESH/D005118"
            }
          ],
          "skos:notation": "extraterrestrialenvironment"
        }
      ],
      "skos:notation": "anysampledfeature"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFCodelistProfile/context.jsonld",
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
  "skos:prefLabel": "Sampled Feature Type vocabulary",
  "skos:definition": "Categories to specify the broad context that a sample is intended to represent.",
  "schema:identifier": "https://w3id.org/isample/vocabulary/sampledfeature/",
  "schema:dateModified": "2024-04-19",
  "schema:url": "https://w3id.org/isample/vocabulary/sampledfeature/",
  "schema:license": [
    {
      "@id": "https://creativecommons.org/licenses/by/4.0/legalcode"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://orcid.org/0000-0001-6041-5302"
      }
    ]
  },
  "dcterms:created": "2021-03-17",
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
      "skos:prefLabel": "Any sampled feature",
      "skos:definition": "Any thing that can be sampled. Top concept in sampled feature type vocabulary.",
      "skos:inScheme": [
        {
          "@id": "sf:sampledfeaturevocabulary"
        }
      ],
      "skos:topConceptOf": {
        "@id": "sf:sampledfeaturevocabulary"
      },
      "skos:narrower": [
        {
          "@id": "sf:anthropogenicenvironment",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Anthropogenic environment",
          "skos:definition": "Sampled feature is produced by or related to human activity past or present.",
          "skos:inScheme": [
            {
              "@id": "sf:sampledfeaturevocabulary"
            }
          ],
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
              "skos:prefLabel": "Active human occupation site",
              "skos:definition": "sampled feature is a site at which there are ongoing human activities",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
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
                  "skos:prefLabel": "Experiment setting",
                  "skos:definition": "Sampled feature is an experimental set up that produced the sample; the sample is the product of the experiment.",
                  "skos:inScheme": [
                    {
                      "@id": "sf:sampledfeaturevocabulary"
                    }
                  ],
                  "skos:broader": [
                    {
                      "@id": "sf:activehumanoccupationsite"
                    }
                  ],
                  "skos:notation": "experimentsetting"
                },
                {
                  "@id": "sf:laboratorycuratorialenvironment",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": "Laboratory or curatorial environment",
                  "skos:definition": "Sampled feature is a laboratory or other research site, collected with intention of characterizing the environment in which data are collected or other research conducted, that might affect results or safety; e.g. lab blank measurements.",
                  "skos:inScheme": [
                    {
                      "@id": "sf:sampledfeaturevocabulary"
                    }
                  ],
                  "skos:broader": [
                    {
                      "@id": "sf:activehumanoccupationsite"
                    }
                  ],
                  "skos:closeMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/ENVO_01001405"
                    }
                  ],
                  "skos:notation": "laboratorycuratorialenvironment"
                }
              ],
              "skos:notation": "activehumanoccupationsite"
            },
            {
              "@id": "sf:pasthumanoccupationsite",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": "Site of past human activities",
              "skos:definition": "sampled feature is a place where humans have been and left evidence of their activity. Includes prehistoric and paleo hominid sites",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
              "skos:broader": [
                {
                  "@id": "sf:anthropogenicenvironment"
                }
              ],
              "skos:notation": "pasthumanoccupationsite"
            }
          ],
          "skos:notation": "anthropogenicenvironment"
        },
        {
          "@id": "sf:biologicalentity",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Biological entity",
          "skos:definition": "Sampled feature is an organism. Use for samples that represent some species of organism as the proximate sampled feature, not the environment that the organism inhabits.",
          "skos:inScheme": [
            {
              "@id": "sf:sampledfeaturevocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "sf:anysampledfeature"
            }
          ],
          "skos:note": {
            "@value": "domain specific vocabulary extensions will be useful to distinguish samples from different phyla/order/class...",
            "@language": "en"
          },
          "skos:notation": "biologicalentity"
        },
        {
          "@id": "sf:earthenvironment",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Earth environment",
          "skos:definition": "Sampled feature is the natural Earth environment",
          "skos:inScheme": [
            {
              "@id": "sf:sampledfeaturevocabulary"
            }
          ],
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
              "skos:prefLabel": "Atmosphere",
              "skos:definition": "Sampled feature is the Earth's atmosphere",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
              "skos:broader": [
                {
                  "@id": "sf:earthenvironment"
                }
              ],
              "skos:notation": "atmosphere"
            },
            {
              "@id": "sf:earthinterior",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": "Earth interior",
              "skos:definition": "Sampled feature is solid material from within the Earth",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
              "skos:broader": [
                {
                  "@id": "sf:earthenvironment"
                }
              ],
              "skos:note": {
                "@value": "fluids in pore space in earth interior sample 'Subsurface fluid reservoir'",
                "@language": "en"
              },
              "skos:notation": "earthinterior"
            },
            {
              "@id": "sf:earthsurface",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": "Earth surface",
              "skos:definition": "Sampled feature is the interface between solid earth and hydrosphere or atmosphere. Includes samples representing things collected on the surface, in the uppermost part of the material below the surface, or air or water directly at the contact with the Earth surface.",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
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
                  "skos:prefLabel": "Lake river or stream bottom",
                  "skos:definition": "Sampled feature is the interface between the solid Earth interface and a lake or flowing water body.",
                  "skos:inScheme": [
                    {
                      "@id": "sf:sampledfeaturevocabulary"
                    }
                  ],
                  "skos:broader": [
                    {
                      "@id": "sf:earthsurface"
                    }
                  ],
                  "skos:narrowMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/ENVO_00000384"
                    }
                  ],
                  "skos:notation": "lakeriverstreambottom"
                },
                {
                  "@id": "sf:marinewaterbodybottom",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": "Marine water body bottom",
                  "skos:altLabel": {
                    "@value": "Sea floor",
                    "@language": "en"
                  },
                  "skos:definition": "Sampled feature is the interface between the solid Earth and a marine or brackish water body. Includes benthic boundary layer:  the bottom layer of water and the uppermost layer of sediment directly influenced by the overlying water.",
                  "skos:inScheme": [
                    {
                      "@id": "sf:sampledfeaturevocabulary"
                    }
                  ],
                  "skos:broader": [
                    {
                      "@id": "sf:earthsurface"
                    }
                  ],
                  "skos:narrowMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/ENVO_00000482"
                    }
                  ],
                  "skos:notation": "marinewaterbodybottom"
                },
                {
                  "@id": "sf:subaerialsurfaceenvironment",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": "Subaerial surface environment",
                  "skos:definition": "sampled feature is the interface between solid Earth and atmosphere.  Sample is collected on the surface, or immediately below surface (zone of bioturbation). Include soil and recently deposited subaerial sediment at the surface.",
                  "skos:inScheme": [
                    {
                      "@id": "sf:sampledfeaturevocabulary"
                    }
                  ],
                  "skos:broader": [
                    {
                      "@id": "sf:earthsurface"
                    }
                  ],
                  "skos:closeMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/RBO_00000017"
                    }
                  ],
                  "skos:notation": "subaerialsurfaceenvironment"
                }
              ],
              "skos:notation": "earthsurface"
            },
            {
              "@id": "sf:glacierenvironment",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": "Glacier environment",
              "skos:definition": "Sampled feature is a glacier, ice sheet, ice shelf, iceberg, or rock or water directly under or on top of such ice.",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
              "skos:broader": [
                {
                  "@id": "sf:earthenvironment"
                }
              ],
              "skos:narrowMatch": [
                {
                  "@id": "http://purl.obolibrary.org/obo/ENVO_00000133"
                }
              ],
              "skos:notation": "glacierenvironment"
            },
            {
              "@id": "sf:subsurfacefluidreservoir",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": "Subsurface fluid reservoir",
              "skos:definition": "Sampled feature is fluid that resides in fractures, intergranular porosity or other open space in the solid earth.",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
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
              ],
              "skos:notation": "subsurfacefluidreservoir"
            },
            {
              "@id": "sf:waterbody",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": "Water body",
              "skos:definition": "Sampled feature is the Earth's hydrosphere.",
              "skos:inScheme": [
                {
                  "@id": "sf:sampledfeaturevocabulary"
                }
              ],
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
                  "skos:prefLabel": "Marine environment",
                  "skos:definition": "Sampled feature is the marine hydrosphere.",
                  "skos:inScheme": [
                    {
                      "@id": "sf:sampledfeaturevocabulary"
                    }
                  ],
                  "skos:broader": [
                    {
                      "@id": "sf:waterbody"
                    }
                  ],
                  "skos:closeMatch": [
                    {
                      "@id": "http://purl.obolibrary.org/obo/ENVO_00001999"
                    }
                  ],
                  "skos:notation": "marinewaterbody"
                },
                {
                  "@id": "sf:terrestrialwaterbody",
                  "@type": [
                    "skos:Concept"
                  ],
                  "skos:prefLabel": "Terrestrial water body",
                  "skos:definition": "Sampled feature is terrestrial hydrosphere-- lake, other standing water, or a flowing water body (river, stream..). Include saline water in terrestrial evaporite environments.",
                  "skos:inScheme": [
                    {
                      "@id": "sf:sampledfeaturevocabulary"
                    }
                  ],
                  "skos:broader": [
                    {
                      "@id": "sf:waterbody"
                    }
                  ],
                  "skos:notation": "terrestrialwaterbody"
                }
              ],
              "skos:notation": "waterbody"
            }
          ],
          "skos:notation": "earthenvironment"
        },
        {
          "@id": "sf:extraterrestrialenvironment",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Extraterrestrial environment",
          "skos:definition": "Sampled feature is the environment outside of solid earth, hydrosphere, or atmosphere.",
          "skos:inScheme": [
            {
              "@id": "sf:sampledfeaturevocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "sf:anysampledfeature"
            }
          ],
          "skos:closeMatch": [
            {
              "@id": "http://purl.bioontology.org/ontology/MESH/D005118"
            }
          ],
          "skos:notation": "extraterrestrialenvironment"
        }
      ],
      "skos:notation": "anysampledfeature"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix sf: <https://w3id.org/isample/vocabulary/sampledfeature/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

sf:atmosphere a skos:Concept ;
    skos:broader sf:earthenvironment ;
    skos:definition "Sampled feature is the Earth's atmosphere" ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:notation "atmosphere" ;
    skos:prefLabel "Atmosphere" .

sf:biologicalentity a skos:Concept ;
    skos:broader sf:anysampledfeature ;
    skos:definition "Sampled feature is an organism. Use for samples that represent some species of organism as the proximate sampled feature, not the environment that the organism inhabits." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:notation "biologicalentity" ;
    skos:note "domain specific vocabulary extensions will be useful to distinguish samples from different phyla/order/class..."@en ;
    skos:prefLabel "Biological entity" .

sf:earthinterior a skos:Concept ;
    skos:broader sf:earthenvironment ;
    skos:definition "Sampled feature is solid material from within the Earth" ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:notation "earthinterior" ;
    skos:note "fluids in pore space in earth interior sample 'Subsurface fluid reservoir'"@en ;
    skos:prefLabel "Earth interior" .

sf:experimentsetting a skos:Concept ;
    skos:broader sf:activehumanoccupationsite ;
    skos:definition "Sampled feature is an experimental set up that produced the sample; the sample is the product of the experiment." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:notation "experimentsetting" ;
    skos:prefLabel "Experiment setting" .

sf:extraterrestrialenvironment a skos:Concept ;
    skos:broader sf:anysampledfeature ;
    skos:closeMatch <http://purl.bioontology.org/ontology/MESH/D005118> ;
    skos:definition "Sampled feature is the environment outside of solid earth, hydrosphere, or atmosphere." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:notation "extraterrestrialenvironment" ;
    skos:prefLabel "Extraterrestrial environment" .

sf:glacierenvironment a skos:Concept ;
    skos:broader sf:earthenvironment ;
    skos:definition "Sampled feature is a glacier, ice sheet, ice shelf, iceberg, or rock or water directly under or on top of such ice." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrowMatch <http://purl.obolibrary.org/obo/ENVO_00000133> ;
    skos:notation "glacierenvironment" ;
    skos:prefLabel "Glacier environment" .

sf:laboratorycuratorialenvironment a skos:Concept ;
    skos:broader sf:activehumanoccupationsite ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_01001405> ;
    skos:definition "Sampled feature is a laboratory or other research site, collected with intention of characterizing the environment in which data are collected or other research conducted, that might affect results or safety; e.g. lab blank measurements." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:notation "laboratorycuratorialenvironment" ;
    skos:prefLabel "Laboratory or curatorial environment" .

sf:lakeriverstreambottom a skos:Concept ;
    skos:broader sf:earthsurface ;
    skos:definition "Sampled feature is the interface between the solid Earth interface and a lake or flowing water body." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrowMatch <http://purl.obolibrary.org/obo/ENVO_00000384> ;
    skos:notation "lakeriverstreambottom" ;
    skos:prefLabel "Lake river or stream bottom" .

sf:marinewaterbody a skos:Concept ;
    skos:broader sf:waterbody ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_00001999> ;
    skos:definition "Sampled feature is the marine hydrosphere." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:notation "marinewaterbody" ;
    skos:prefLabel "Marine environment" .

sf:marinewaterbodybottom a skos:Concept ;
    skos:altLabel "Sea floor"@en ;
    skos:broader sf:earthsurface ;
    skos:definition "Sampled feature is the interface between the solid Earth and a marine or brackish water body. Includes benthic boundary layer:  the bottom layer of water and the uppermost layer of sediment directly influenced by the overlying water." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrowMatch <http://purl.obolibrary.org/obo/ENVO_00000482> ;
    skos:notation "marinewaterbodybottom" ;
    skos:prefLabel "Marine water body bottom" .

sf:pasthumanoccupationsite a skos:Concept ;
    skos:broader sf:anthropogenicenvironment ;
    skos:definition "sampled feature is a place where humans have been and left evidence of their activity. Includes prehistoric and paleo hominid sites" ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:notation "pasthumanoccupationsite" ;
    skos:prefLabel "Site of past human activities" .

sf:subaerialsurfaceenvironment a skos:Concept ;
    skos:broader sf:earthsurface ;
    skos:closeMatch <http://purl.obolibrary.org/obo/RBO_00000017> ;
    skos:definition "sampled feature is the interface between solid Earth and atmosphere.  Sample is collected on the surface, or immediately below surface (zone of bioturbation). Include soil and recently deposited subaerial sediment at the surface." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:notation "subaerialsurfaceenvironment" ;
    skos:prefLabel "Subaerial surface environment" .

sf:subsurfacefluidreservoir a skos:Concept ;
    skos:broader sf:earthenvironment ;
    skos:definition "Sampled feature is fluid that resides in fractures, intergranular porosity or other open space in the solid earth." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrowMatch <http://purl.jp/bio/11/meo/MEO_0000326>,
        <http://purl.obolibrary.org/obo/ENVO_00012408> ;
    skos:notation "subsurfacefluidreservoir" ;
    skos:prefLabel "Subsurface fluid reservoir" .

sf:terrestrialwaterbody a skos:Concept ;
    skos:broader sf:waterbody ;
    skos:definition "Sampled feature is terrestrial hydrosphere-- lake, other standing water, or a flowing water body (river, stream..). Include saline water in terrestrial evaporite environments." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:notation "terrestrialwaterbody" ;
    skos:prefLabel "Terrestrial water body" .

sf:activehumanoccupationsite a skos:Concept ;
    skos:broader sf:anthropogenicenvironment ;
    skos:definition "sampled feature is a site at which there are ongoing human activities" ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrower sf:experimentsetting,
        sf:laboratorycuratorialenvironment ;
    skos:notation "activehumanoccupationsite" ;
    skos:prefLabel "Active human occupation site" .

sf:anthropogenicenvironment a skos:Concept ;
    skos:broader sf:anysampledfeature ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_01000313> ;
    skos:definition "Sampled feature is produced by or related to human activity past or present." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrower sf:activehumanoccupationsite,
        sf:pasthumanoccupationsite ;
    skos:notation "anthropogenicenvironment" ;
    skos:prefLabel "Anthropogenic environment" .

sf:waterbody a skos:Concept ;
    skos:broader sf:earthenvironment ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_00000063> ;
    skos:definition "Sampled feature is the Earth's hydrosphere." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrower sf:marinewaterbody,
        sf:terrestrialwaterbody ;
    skos:notation "waterbody" ;
    skos:prefLabel "Water body" .

sf:earthsurface a skos:Concept ;
    skos:broader sf:earthenvironment ;
    skos:definition "Sampled feature is the interface between solid earth and hydrosphere or atmosphere. Includes samples representing things collected on the surface, in the uppermost part of the material below the surface, or air or water directly at the contact with the Earth surface." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrowMatch <http://purl.obolibrary.org/obo/RBO_00000017> ;
    skos:narrower sf:lakeriverstreambottom,
        sf:marinewaterbodybottom,
        sf:subaerialsurfaceenvironment ;
    skos:notation "earthsurface" ;
    skos:prefLabel "Earth surface" .

sf:anysampledfeature a skos:Concept ;
    skos:definition "Any thing that can be sampled. Top concept in sampled feature type vocabulary." ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrower sf:anthropogenicenvironment,
        sf:biologicalentity,
        sf:earthenvironment,
        sf:extraterrestrialenvironment ;
    skos:notation "anysampledfeature" ;
    skos:prefLabel "Any sampled feature" ;
    skos:topConceptOf sf:sampledfeaturevocabulary .

sf:earthenvironment a skos:Concept ;
    skos:broader sf:anysampledfeature ;
    skos:definition "Sampled feature is the natural Earth environment" ;
    skos:inScheme sf:sampledfeaturevocabulary ;
    skos:narrower sf:atmosphere,
        sf:earthinterior,
        sf:earthsurface,
        sf:glacierenvironment,
        sf:subsurfacefluidreservoir,
        sf:waterbody ;
    skos:notation "earthenvironment" ;
    skos:prefLabel "Earth environment" .

sf:sampledfeaturevocabulary a skos:ConceptScheme ;
    dcterms:created "2021-03-17" ;
    schema1:creator ( <https://orcid.org/0000-0001-6041-5302> ) ;
    schema1:dateModified "2024-04-19" ;
    schema1:identifier "https://w3id.org/isample/vocabulary/sampledfeature/" ;
    schema1:license <https://creativecommons.org/licenses/by/4.0/legalcode> ;
    schema1:url "https://w3id.org/isample/vocabulary/sampledfeature/" ;
    skos:definition "Categories to specify the broad context that a sample is intended to represent." ;
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
    skos:prefLabel "Sampled Feature Type vocabulary" .


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
    "schema": "http://schema.org/",
    "mat": "https://w3id.org/isample/vocabulary/material/"
  },
  "@id": "mat:materialsvocabulary",
  "@type": [
    "skos:ConceptScheme"
  ],
  "skos:prefLabel": "iSamples Materials Vocabulary",
  "schema:identifier": "https://w3id.org/isample/vocabulary/material/",
  "schema:dateModified": "2024-01-01",
  "schema:url": "https://w3id.org/isample/vocabulary/material/",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "skos:hasTopConcept": [
    {
      "@id": "mat:material",
      "@type": [
        "skos:Concept"
      ],
      "skos:prefLabel": "Material",
      "skos:definition": "Top Concept in iSamples Material Category scheme",
      "skos:inScheme": [
        {
          "@id": "mat:materialsvocabulary"
        }
      ],
      "skos:narrower": [
        {
          "@id": "mat:anyanthropogenicmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Anthropogenic material",
          "skos:definition": "Material produced by human activity.",
          "skos:inScheme": [
            {
              "@id": "mat:materialsvocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ],
          "skos:notation": "anyanthropogenicmaterial"
        },
        {
          "@id": "mat:anyice",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Any ice",
          "skos:definition": "A material that is in a solid state under the temperature and pressure conditions of the preserved sample, but is a liquid or gas at Standard Temperature and Pressure.",
          "skos:inScheme": [
            {
              "@id": "mat:materialsvocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ],
          "skos:notation": "anyice"
        },
        {
          "@id": "mat:biogenicnonorganicmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Biogenic non-organic material",
          "skos:definition": "Material produced by an organism but not composed of very large molecules of biological origin.",
          "skos:inScheme": [
            {
              "@id": "mat:materialsvocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ],
          "skos:notation": "biogenicnonorganicmaterial"
        },
        {
          "@id": "mat:earthmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Natural Solid Material",
          "skos:definition": "A naturally occurring solid material that is not anthropogenic, biogenic, or ice.",
          "skos:inScheme": [
            {
              "@id": "mat:materialsvocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ],
          "skos:notation": "earthmaterial"
        },
        {
          "@id": "mat:fluid",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Fluid material",
          "skos:definition": "Substance that continually deforms (flows) under an applied shear stress, or external force.",
          "skos:inScheme": [
            {
              "@id": "mat:materialsvocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ],
          "skos:notation": "fluid"
        },
        {
          "@id": "mat:organicmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Organic material",
          "skos:definition": "Material derived from living organisms and composed primarily of one or more very large molecules of biological origin.",
          "skos:inScheme": [
            {
              "@id": "mat:materialsvocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ],
          "skos:notation": "organicmaterial"
        }
      ],
      "skos:notation": "material"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFCodelistProfile/context.jsonld",
    {
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "schema": "http://schema.org/",
      "mat": "https://w3id.org/isample/vocabulary/material/"
    }
  ],
  "@id": "mat:materialsvocabulary",
  "@type": [
    "skos:ConceptScheme"
  ],
  "skos:prefLabel": "iSamples Materials Vocabulary",
  "schema:identifier": "https://w3id.org/isample/vocabulary/material/",
  "schema:dateModified": "2024-01-01",
  "schema:url": "https://w3id.org/isample/vocabulary/material/",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "skos:hasTopConcept": [
    {
      "@id": "mat:material",
      "@type": [
        "skos:Concept"
      ],
      "skos:prefLabel": "Material",
      "skos:definition": "Top Concept in iSamples Material Category scheme",
      "skos:inScheme": [
        {
          "@id": "mat:materialsvocabulary"
        }
      ],
      "skos:narrower": [
        {
          "@id": "mat:anyanthropogenicmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Anthropogenic material",
          "skos:definition": "Material produced by human activity.",
          "skos:inScheme": [
            {
              "@id": "mat:materialsvocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ],
          "skos:notation": "anyanthropogenicmaterial"
        },
        {
          "@id": "mat:anyice",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Any ice",
          "skos:definition": "A material that is in a solid state under the temperature and pressure conditions of the preserved sample, but is a liquid or gas at Standard Temperature and Pressure.",
          "skos:inScheme": [
            {
              "@id": "mat:materialsvocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ],
          "skos:notation": "anyice"
        },
        {
          "@id": "mat:biogenicnonorganicmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Biogenic non-organic material",
          "skos:definition": "Material produced by an organism but not composed of very large molecules of biological origin.",
          "skos:inScheme": [
            {
              "@id": "mat:materialsvocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ],
          "skos:notation": "biogenicnonorganicmaterial"
        },
        {
          "@id": "mat:earthmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Natural Solid Material",
          "skos:definition": "A naturally occurring solid material that is not anthropogenic, biogenic, or ice.",
          "skos:inScheme": [
            {
              "@id": "mat:materialsvocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ],
          "skos:notation": "earthmaterial"
        },
        {
          "@id": "mat:fluid",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Fluid material",
          "skos:definition": "Substance that continually deforms (flows) under an applied shear stress, or external force.",
          "skos:inScheme": [
            {
              "@id": "mat:materialsvocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ],
          "skos:notation": "fluid"
        },
        {
          "@id": "mat:organicmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Organic material",
          "skos:definition": "Material derived from living organisms and composed primarily of one or more very large molecules of biological origin.",
          "skos:inScheme": [
            {
              "@id": "mat:materialsvocabulary"
            }
          ],
          "skos:broader": [
            {
              "@id": "mat:material"
            }
          ],
          "skos:notation": "organicmaterial"
        }
      ],
      "skos:notation": "material"
    }
  ]
}
```

#### ttl
```ttl
@prefix mat: <https://w3id.org/isample/vocabulary/material/> .
@prefix schema1: <http://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

mat:anyanthropogenicmaterial a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "Material produced by human activity." ;
    skos:inScheme mat:materialsvocabulary ;
    skos:notation "anyanthropogenicmaterial" ;
    skos:prefLabel "Anthropogenic material" .

mat:anyice a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "A material that is in a solid state under the temperature and pressure conditions of the preserved sample, but is a liquid or gas at Standard Temperature and Pressure." ;
    skos:inScheme mat:materialsvocabulary ;
    skos:notation "anyice" ;
    skos:prefLabel "Any ice" .

mat:biogenicnonorganicmaterial a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "Material produced by an organism but not composed of very large molecules of biological origin." ;
    skos:inScheme mat:materialsvocabulary ;
    skos:notation "biogenicnonorganicmaterial" ;
    skos:prefLabel "Biogenic non-organic material" .

mat:earthmaterial a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "A naturally occurring solid material that is not anthropogenic, biogenic, or ice." ;
    skos:inScheme mat:materialsvocabulary ;
    skos:notation "earthmaterial" ;
    skos:prefLabel "Natural Solid Material" .

mat:fluid a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "Substance that continually deforms (flows) under an applied shear stress, or external force." ;
    skos:inScheme mat:materialsvocabulary ;
    skos:notation "fluid" ;
    skos:prefLabel "Fluid material" .

mat:organicmaterial a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "Material derived from living organisms and composed primarily of one or more very large molecules of biological origin." ;
    skos:inScheme mat:materialsvocabulary ;
    skos:notation "organicmaterial" ;
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
    skos:notation "material" ;
    skos:prefLabel "Material" .

mat:materialsvocabulary a skos:ConceptScheme ;
    schema1:dateModified "2024-01-01" ;
    schema1:identifier "https://w3id.org/isample/vocabulary/material/" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:url "https://w3id.org/isample/vocabulary/material/" ;
    skos:hasTopConcept mat:material ;
    skos:prefLabel "iSamples Materials Vocabulary" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Codelist profile
description: 'CDIF profile for controlled-vocabulary codelists. Composes the cdifCodelist
  building block: a skos:ConceptScheme constrained for CDIF codelist use (resolvable
  @id; each concept requires @id, skos:inScheme, skos:prefLabel, skos:notation; both
  skos:narrower and skos:broader required where there is hierarchy). schema: metadata
  properties (schema:identifier, schema:dateModified, schema:license or schema:conditionsOfAccess)
  take precedence over the equivalent dcterms properties from the base skos:ConceptScheme.'
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCodelist/schema.yaml
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  dcterms: http://purl.org/dc/terms/
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFCodelistProfile/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFCodelistProfile/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFCodelistProfile/context.jsonld)

## Sources

* [W3C SKOS Reference](https://www.w3.org/TR/skos-reference/)
* [CDIF Codelist specification](https://github.com/Cross-Domain-Interoperability-Framework/codelist)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifProfiles/CDIFCodelistProfile`

