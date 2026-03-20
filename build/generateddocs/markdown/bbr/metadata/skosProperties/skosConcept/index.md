
# SKOS Concept (Schema)

`cdif.bbr.metadata.skosProperties.skosConcept` *v0.1*

JSON Schema for validating a SKOS Concept in native JSON-LD form. Validates skos:Concept with prefLabel, notations, broader/narrower/related hierarchical relations, cross-scheme mapping properties, scheme membership, and documentary notes. Defines $defs: ConceptRef, LanguageTaggedValue.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## SKOS Concept

JSON Schema for validating a [SKOS Concept](https://www.w3.org/TR/skos-reference/#concepts) in native JSON-LD form.

A concept must have `@type` including `skos:Concept` and a `skos:prefLabel`. An `@id` or `skos:notation` is required for identification.

### Labels
- `skos:prefLabel` — preferred label (one per language)
- `skos:altLabel` — alternative labels (acronyms, abbreviations)
- `skos:hiddenLabel` — labels for search, not display

Labels can be simple strings or language-tagged JSON-LD value objects (`@value`/`@language`).

### Hierarchy and relations
- `skos:broader`, `skos:narrower` — hierarchical relations (inline concepts or `@id` references, recursive)
- `skos:related` — associative relations

### Cross-scheme mappings
- `skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch` — `@id` references to concepts in other schemes

### Scheme membership
- `skos:inScheme` — concept scheme(s) this concept belongs to
- `skos:topConceptOf` — scheme(s) for which this is a top concept

### Documentary notes
- `skos:definition`, `skos:scopeNote`, `skos:note`, `skos:historyNote`, `skos:changeNote`, `skos:editorialNote`, `skos:example`

## Examples

### SKOS Concept example
Petrology concept with multilingual labels, notations, hierarchical
narrower concepts, associative relations, and cross-scheme mappings.
#### json
```json
{
  "@context": {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "mat": "https://w3id.org/isample/vocabulary/material/"
  },
  "@id": "mat:earthmaterial",
  "@type": ["skos:Concept"],
  "skos:prefLabel": {"@value": "Natural Solid Material", "@language": "en"},
  "skos:definition": {"@value": "A naturally occurring solid material that is not anthropogenic, biogenic, or ice.", "@language": "en"},
  "skos:inScheme": {"@id": "mat:materialsvocabulary"},
  "skos:broader": [{"@id": "mat:material"}],
  "skos:closeMatch": [
    {"@id": "http://resource.geosciml.org/classifier/cgi/lithology/compound_material"},
    {"@id": "https://w3id.org/gso/geology/Solid_Geologic_Material"}
  ],
  "skos:narrower": [
    {
      "@id": "mat:mineral",
      "@type": ["skos:Concept"],
      "skos:prefLabel": {"@value": "Mineral", "@language": "en"},
      "skos:definition": {"@value": "Material consists of a single mineral or mineraloid phase.  'A mineral is an element or chemical compound that is normally crystalline and that has been formed as a result of geological processes.' (Nickel, Ernest H. (1995), The definition of a mineral, The Canadian Mineralogist. 33 (3): 689-90). Include mineraloids. ... A material primarily composed of some substance that is naturally occurring, solid and stable at room temperature, representable by a chemical formula, usually abiogenic, and that has an ordered atomic structure. (http://purl.obolibrary.org/obo/ENVO_01000256). The identity of a mineral species is defined by a crystal structure and a chemical composition that might include various specific elemental substitutions in that structure. Mineraloid: A naturally occurring mineral-like substance that does not demonstrate crystallinity. Mineraloids possess chemical compositions that vary beyond the generally accepted ranges for specific minerals. Examples: obsidian, Opal. (https://en.wikipedia.org/wiki/Mineraloid)", "@language": "en"},
      "skos:inScheme": {"@id": "mat:materialsvocabulary"},
      "skos:broader": [{"@id": "mat:earthmaterial"}],
      "skos:exactMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_01000256"}]
    },
    {
      "@id": "mat:mixedsoilsedimentrock",
      "@type": ["skos:Concept"],
      "skos:prefLabel": {"@value": "Mixed soil sediment or rock", "@language": "en"},
      "skos:definition": {"@value": "Material is mixed aggregation of fragments of undifferentiated soil, sediment or rock origin. e.g. cuttings from some boreholes (rock fragments and caved soil or sediment).", "@language": "en"},
      "skos:inScheme": {"@id": "mat:materialsvocabulary"},
      "skos:broader": [{"@id": "mat:earthmaterial"}],
      "skos:note": {"@value": "This class is for samples that are solid Earth materials but known not to be mineral or particulate samples.", "@language": "en"}
    },
    {
      "@id": "mat:rockorsediment",
      "@type": ["skos:Concept"],
      "skos:prefLabel": {"@value": "Rock or sediment", "@language": "en"},
      "skos:definition": {"@value": "Material is rock or sediment.  For example core from boreholes that likely penetrate sediment near the surface and rock at greater depth, with descriptions that do not clearly distinguish non-consolidated sediment from rock.", "@language": "en"},
      "skos:inScheme": {"@id": "mat:materialsvocabulary"},
      "skos:broader": [{"@id": "mat:earthmaterial"}],
      "skos:note": [
        {"@value": "Use for samples described as rock>sedimentary AND sediment, where it is unclear whether the sample is a consolidated 'rock' object, or loose disaggregated material in a bag.", "@language": "en"},
        {"@value": "Use for samples like dredge hauls and ROV scoops that mix rock and sediment from a water body bottom.", "@language": "en"}
      ],
      "skos:scopeNote": {"@value": "Distinct from 'Mixed soil, sediment or rock' that represents samples known to have components of all these materials.", "@language": "en"},
      "skos:narrower": [
        {
          "@id": "mat:rock",
          "@type": ["skos:Concept"],
          "skos:prefLabel": {"@value": "Rock", "@language": "en"},
          "skos:definition": {"@value": "Consolidated aggregate of particles (grains) of rock, mineral (including native elements), mineraloid, or solid organic material. Includes mineral aggregates such as granite, shale, marble; natural glass such as obsidian; organic material formed by geologic processes such a coal;  extraterrestrial material in meteorites; and  crushed rock fragments like drill cuttings from rock.  (based on http://resource.geosciml.org/classifier/cgi/lithology/rock, same as http://purl.obolibrary.org/obo/ENVO_00001995)", "@language": "en"},
          "skos:inScheme": {"@id": "mat:materialsvocabulary"},
          "skos:broader": [{"@id": "mat:rockorsediment"}],
          "skos:closeMatch": [
            {"@id": "http://purl.obolibrary.org/obo/ENVO_00001995"},
            {"@id": "http://resource.geosciml.org/classifier/cgi/lithology/rock"}
          ]
        },
        {
          "@id": "mat:sediment",
          "@type": ["skos:Concept"],
          "skos:prefLabel": {"@value": "Sediment", "@language": "en"},
          "skos:definition": {"@value": "Solid granular material transported by wind, water, or gravity, not modified by interaction with biosphere or atmosphere (to differentiate from soil). Particles might be derived by erosion of pre-existing rock, from shell or other body parts from organisms, precipitated chemically in the surficial environment, or generated by explosive volcanic activity. (http://resource.geosciml.org/classifier/cgi/lithology/sediment). Sediment is not consolidated, i.e. the particulate constituents do not adhere to each other strongly enough that the aggregate can be considered a solid material in its own right. Similar to http://purl.obolibrary.org/obo/ENVO_00002007", "@language": "en"},
          "skos:inScheme": {"@id": "mat:materialsvocabulary"},
          "skos:broader": [{"@id": "mat:rockorsediment"}],
          "skos:closeMatch": [
            {"@id": "http://purl.obolibrary.org/obo/ENVO_00002007"},
            {"@id": "http://resource.geosciml.org/classifier/cgi/lithology/sediment"}
          ],
          "skos:note": [
            {"@value": "Note that this category includes chemical sediments that might preciptate to form a solid mass, e.g. preciptitates forming vents at submarine hot springs, or gypsum and halite deposites formed by evaporation in hypersaline lakes. (http://resource.geosciml.org/classifier/cgi/consolidationdegree/consolidated).", "@language": "en"},
            {"@value": "Tephra is subclass of sediment because it is generally not lithified, in which case it would be considered Rock.", "@language": "en"}
          ]
        }
      ]
    },
    {
      "@id": "mat:particulate",
      "@type": ["skos:Concept"],
      "skos:prefLabel": {"@value": "Particulate", "@language": "en"},
      "skos:definition": {"@value": "Material consists of microscopic particulate material derived by precipitation, filtering, or settling from suspension in a fluid, e.g. filtrate from water, deposition from atmosphere, astro material particles. Might include mineral, organic, or biological material. ENVO definition (ENVO_01000060) has \"composed of microscopic portions of solid or liquid material suspended in another environmental material.\" Refine here to define as the solid particles, distinct from a material in which they are suspended. A material that includes solid or liquid particles suspended in another material would be a dispersed_media in this scheme, not defined in ENVO. Human manufactured particulates (e.g. rock powder) should be categorized as 'Anthropogenic material' as well as 'Particulate'", "@language": "en"},
      "skos:inScheme": {"@id": "mat:materialsvocabulary"},
      "skos:broader": [{"@id": "mat:earthmaterial"}],
      "skos:narrowMatch": [
        {"@id": "http://purl.bioontology.org/ontology/MESH/D052638"},
        {"@id": "http://purl.obolibrary.org/obo/NCIT_C1709"}
      ],
      "skos:relatedMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_01000060"}]
    },
    {
      "@id": "mat:soil",
      "@type": ["skos:Concept"],
      "skos:prefLabel": {"@value": "Soil", "@language": "en"},
      "skos:definition": {"@value": "Mixed granular mineral and organic matter modified by interaction between earth material, biosphere, and atmosphere, consisting of varying proportions of sand, silt, and clay, organic material such as humus, gases, liquids, and a broad range of resident micro- and macroorganisms. (https://en.wikipedia.org/wiki/Soil) Soil consists of horizons near the Earth's surface that, in contrast to the underlying parent material, have been altered by the interactions of climate, relief, and living organisms over time. (http://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280) (http://purl.obolibrary.org/obo/ENVO_00001998)", "@language": "en"},
      "skos:inScheme": {"@id": "mat:materialsvocabulary"},
      "skos:broader": [{"@id": "mat:earthmaterial"}],
      "skos:closeMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_00001998"}]
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/context.jsonld",
    {
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "mat": "https://w3id.org/isample/vocabulary/material/"
    }
  ],
  "@id": "mat:earthmaterial",
  "@type": [
    "skos:Concept"
  ],
  "skos:prefLabel": {
    "@value": "Natural Solid Material",
    "@language": "en"
  },
  "skos:definition": {
    "@value": "A naturally occurring solid material that is not anthropogenic, biogenic, or ice.",
    "@language": "en"
  },
  "skos:inScheme": {
    "@id": "mat:materialsvocabulary"
  },
  "skos:broader": [
    {
      "@id": "mat:material"
    }
  ],
  "skos:closeMatch": [
    {
      "@id": "http://resource.geosciml.org/classifier/cgi/lithology/compound_material"
    },
    {
      "@id": "https://w3id.org/gso/geology/Solid_Geologic_Material"
    }
  ],
  "skos:narrower": [
    {
      "@id": "mat:mineral",
      "@type": [
        "skos:Concept"
      ],
      "skos:prefLabel": {
        "@value": "Mineral",
        "@language": "en"
      },
      "skos:definition": {
        "@value": "Material consists of a single mineral or mineraloid phase.  'A mineral is an element or chemical compound that is normally crystalline and that has been formed as a result of geological processes.' (Nickel, Ernest H. (1995), The definition of a mineral, The Canadian Mineralogist. 33 (3): 689-90). Include mineraloids. ... A material primarily composed of some substance that is naturally occurring, solid and stable at room temperature, representable by a chemical formula, usually abiogenic, and that has an ordered atomic structure. (http://purl.obolibrary.org/obo/ENVO_01000256). The identity of a mineral species is defined by a crystal structure and a chemical composition that might include various specific elemental substitutions in that structure. Mineraloid: A naturally occurring mineral-like substance that does not demonstrate crystallinity. Mineraloids possess chemical compositions that vary beyond the generally accepted ranges for specific minerals. Examples: obsidian, Opal. (https://en.wikipedia.org/wiki/Mineraloid)",
        "@language": "en"
      },
      "skos:inScheme": {
        "@id": "mat:materialsvocabulary"
      },
      "skos:broader": [
        {
          "@id": "mat:earthmaterial"
        }
      ],
      "skos:exactMatch": [
        {
          "@id": "http://purl.obolibrary.org/obo/ENVO_01000256"
        }
      ]
    },
    {
      "@id": "mat:mixedsoilsedimentrock",
      "@type": [
        "skos:Concept"
      ],
      "skos:prefLabel": {
        "@value": "Mixed soil sediment or rock",
        "@language": "en"
      },
      "skos:definition": {
        "@value": "Material is mixed aggregation of fragments of undifferentiated soil, sediment or rock origin. e.g. cuttings from some boreholes (rock fragments and caved soil or sediment).",
        "@language": "en"
      },
      "skos:inScheme": {
        "@id": "mat:materialsvocabulary"
      },
      "skos:broader": [
        {
          "@id": "mat:earthmaterial"
        }
      ],
      "skos:note": {
        "@value": "This class is for samples that are solid Earth materials but known not to be mineral or particulate samples.",
        "@language": "en"
      }
    },
    {
      "@id": "mat:rockorsediment",
      "@type": [
        "skos:Concept"
      ],
      "skos:prefLabel": {
        "@value": "Rock or sediment",
        "@language": "en"
      },
      "skos:definition": {
        "@value": "Material is rock or sediment.  For example core from boreholes that likely penetrate sediment near the surface and rock at greater depth, with descriptions that do not clearly distinguish non-consolidated sediment from rock.",
        "@language": "en"
      },
      "skos:inScheme": {
        "@id": "mat:materialsvocabulary"
      },
      "skos:broader": [
        {
          "@id": "mat:earthmaterial"
        }
      ],
      "skos:note": [
        {
          "@value": "Use for samples described as rock>sedimentary AND sediment, where it is unclear whether the sample is a consolidated 'rock' object, or loose disaggregated material in a bag.",
          "@language": "en"
        },
        {
          "@value": "Use for samples like dredge hauls and ROV scoops that mix rock and sediment from a water body bottom.",
          "@language": "en"
        }
      ],
      "skos:scopeNote": {
        "@value": "Distinct from 'Mixed soil, sediment or rock' that represents samples known to have components of all these materials.",
        "@language": "en"
      },
      "skos:narrower": [
        {
          "@id": "mat:rock",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": {
            "@value": "Rock",
            "@language": "en"
          },
          "skos:definition": {
            "@value": "Consolidated aggregate of particles (grains) of rock, mineral (including native elements), mineraloid, or solid organic material. Includes mineral aggregates such as granite, shale, marble; natural glass such as obsidian; organic material formed by geologic processes such a coal;  extraterrestrial material in meteorites; and  crushed rock fragments like drill cuttings from rock.  (based on http://resource.geosciml.org/classifier/cgi/lithology/rock, same as http://purl.obolibrary.org/obo/ENVO_00001995)",
            "@language": "en"
          },
          "skos:inScheme": {
            "@id": "mat:materialsvocabulary"
          },
          "skos:broader": [
            {
              "@id": "mat:rockorsediment"
            }
          ],
          "skos:closeMatch": [
            {
              "@id": "http://purl.obolibrary.org/obo/ENVO_00001995"
            },
            {
              "@id": "http://resource.geosciml.org/classifier/cgi/lithology/rock"
            }
          ]
        },
        {
          "@id": "mat:sediment",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": {
            "@value": "Sediment",
            "@language": "en"
          },
          "skos:definition": {
            "@value": "Solid granular material transported by wind, water, or gravity, not modified by interaction with biosphere or atmosphere (to differentiate from soil). Particles might be derived by erosion of pre-existing rock, from shell or other body parts from organisms, precipitated chemically in the surficial environment, or generated by explosive volcanic activity. (http://resource.geosciml.org/classifier/cgi/lithology/sediment). Sediment is not consolidated, i.e. the particulate constituents do not adhere to each other strongly enough that the aggregate can be considered a solid material in its own right. Similar to http://purl.obolibrary.org/obo/ENVO_00002007",
            "@language": "en"
          },
          "skos:inScheme": {
            "@id": "mat:materialsvocabulary"
          },
          "skos:broader": [
            {
              "@id": "mat:rockorsediment"
            }
          ],
          "skos:closeMatch": [
            {
              "@id": "http://purl.obolibrary.org/obo/ENVO_00002007"
            },
            {
              "@id": "http://resource.geosciml.org/classifier/cgi/lithology/sediment"
            }
          ],
          "skos:note": [
            {
              "@value": "Note that this category includes chemical sediments that might preciptate to form a solid mass, e.g. preciptitates forming vents at submarine hot springs, or gypsum and halite deposites formed by evaporation in hypersaline lakes. (http://resource.geosciml.org/classifier/cgi/consolidationdegree/consolidated).",
              "@language": "en"
            },
            {
              "@value": "Tephra is subclass of sediment because it is generally not lithified, in which case it would be considered Rock.",
              "@language": "en"
            }
          ]
        }
      ]
    },
    {
      "@id": "mat:particulate",
      "@type": [
        "skos:Concept"
      ],
      "skos:prefLabel": {
        "@value": "Particulate",
        "@language": "en"
      },
      "skos:definition": {
        "@value": "Material consists of microscopic particulate material derived by precipitation, filtering, or settling from suspension in a fluid, e.g. filtrate from water, deposition from atmosphere, astro material particles. Might include mineral, organic, or biological material. ENVO definition (ENVO_01000060) has \"composed of microscopic portions of solid or liquid material suspended in another environmental material.\" Refine here to define as the solid particles, distinct from a material in which they are suspended. A material that includes solid or liquid particles suspended in another material would be a dispersed_media in this scheme, not defined in ENVO. Human manufactured particulates (e.g. rock powder) should be categorized as 'Anthropogenic material' as well as 'Particulate'",
        "@language": "en"
      },
      "skos:inScheme": {
        "@id": "mat:materialsvocabulary"
      },
      "skos:broader": [
        {
          "@id": "mat:earthmaterial"
        }
      ],
      "skos:narrowMatch": [
        {
          "@id": "http://purl.bioontology.org/ontology/MESH/D052638"
        },
        {
          "@id": "http://purl.obolibrary.org/obo/NCIT_C1709"
        }
      ],
      "skos:relatedMatch": [
        {
          "@id": "http://purl.obolibrary.org/obo/ENVO_01000060"
        }
      ]
    },
    {
      "@id": "mat:soil",
      "@type": [
        "skos:Concept"
      ],
      "skos:prefLabel": {
        "@value": "Soil",
        "@language": "en"
      },
      "skos:definition": {
        "@value": "Mixed granular mineral and organic matter modified by interaction between earth material, biosphere, and atmosphere, consisting of varying proportions of sand, silt, and clay, organic material such as humus, gases, liquids, and a broad range of resident micro- and macroorganisms. (https://en.wikipedia.org/wiki/Soil) Soil consists of horizons near the Earth's surface that, in contrast to the underlying parent material, have been altered by the interactions of climate, relief, and living organisms over time. (http://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280) (http://purl.obolibrary.org/obo/ENVO_00001998)",
        "@language": "en"
      },
      "skos:inScheme": {
        "@id": "mat:materialsvocabulary"
      },
      "skos:broader": [
        {
          "@id": "mat:earthmaterial"
        }
      ],
      "skos:closeMatch": [
        {
          "@id": "http://purl.obolibrary.org/obo/ENVO_00001998"
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

mat:mineral a skos:Concept ;
    skos:broader mat:earthmaterial ;
    skos:definition "Material consists of a single mineral or mineraloid phase.  'A mineral is an element or chemical compound that is normally crystalline and that has been formed as a result of geological processes.' (Nickel, Ernest H. (1995), The definition of a mineral, The Canadian Mineralogist. 33 (3): 689-90). Include mineraloids. ... A material primarily composed of some substance that is naturally occurring, solid and stable at room temperature, representable by a chemical formula, usually abiogenic, and that has an ordered atomic structure. (http://purl.obolibrary.org/obo/ENVO_01000256). The identity of a mineral species is defined by a crystal structure and a chemical composition that might include various specific elemental substitutions in that structure. Mineraloid: A naturally occurring mineral-like substance that does not demonstrate crystallinity. Mineraloids possess chemical compositions that vary beyond the generally accepted ranges for specific minerals. Examples: obsidian, Opal. (https://en.wikipedia.org/wiki/Mineraloid)"@en ;
    skos:exactMatch <http://purl.obolibrary.org/obo/ENVO_01000256> ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Mineral"@en .

mat:mixedsoilsedimentrock a skos:Concept ;
    skos:broader mat:earthmaterial ;
    skos:definition "Material is mixed aggregation of fragments of undifferentiated soil, sediment or rock origin. e.g. cuttings from some boreholes (rock fragments and caved soil or sediment)."@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:note "This class is for samples that are solid Earth materials but known not to be mineral or particulate samples."@en ;
    skos:prefLabel "Mixed soil sediment or rock"@en .

mat:particulate a skos:Concept ;
    skos:broader mat:earthmaterial ;
    skos:definition "Material consists of microscopic particulate material derived by precipitation, filtering, or settling from suspension in a fluid, e.g. filtrate from water, deposition from atmosphere, astro material particles. Might include mineral, organic, or biological material. ENVO definition (ENVO_01000060) has \"composed of microscopic portions of solid or liquid material suspended in another environmental material.\" Refine here to define as the solid particles, distinct from a material in which they are suspended. A material that includes solid or liquid particles suspended in another material would be a dispersed_media in this scheme, not defined in ENVO. Human manufactured particulates (e.g. rock powder) should be categorized as 'Anthropogenic material' as well as 'Particulate'"@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:narrowMatch <http://purl.bioontology.org/ontology/MESH/D052638>,
        <http://purl.obolibrary.org/obo/NCIT_C1709> ;
    skos:prefLabel "Particulate"@en ;
    skos:relatedMatch <http://purl.obolibrary.org/obo/ENVO_01000060> .

mat:rock a skos:Concept ;
    skos:broader mat:rockorsediment ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_00001995>,
        <http://resource.geosciml.org/classifier/cgi/lithology/rock> ;
    skos:definition "Consolidated aggregate of particles (grains) of rock, mineral (including native elements), mineraloid, or solid organic material. Includes mineral aggregates such as granite, shale, marble; natural glass such as obsidian; organic material formed by geologic processes such a coal;  extraterrestrial material in meteorites; and  crushed rock fragments like drill cuttings from rock.  (based on http://resource.geosciml.org/classifier/cgi/lithology/rock, same as http://purl.obolibrary.org/obo/ENVO_00001995)"@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Rock"@en .

mat:sediment a skos:Concept ;
    skos:broader mat:rockorsediment ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_00002007>,
        <http://resource.geosciml.org/classifier/cgi/lithology/sediment> ;
    skos:definition "Solid granular material transported by wind, water, or gravity, not modified by interaction with biosphere or atmosphere (to differentiate from soil). Particles might be derived by erosion of pre-existing rock, from shell or other body parts from organisms, precipitated chemically in the surficial environment, or generated by explosive volcanic activity. (http://resource.geosciml.org/classifier/cgi/lithology/sediment). Sediment is not consolidated, i.e. the particulate constituents do not adhere to each other strongly enough that the aggregate can be considered a solid material in its own right. Similar to http://purl.obolibrary.org/obo/ENVO_00002007"@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:note "Note that this category includes chemical sediments that might preciptate to form a solid mass, e.g. preciptitates forming vents at submarine hot springs, or gypsum and halite deposites formed by evaporation in hypersaline lakes. (http://resource.geosciml.org/classifier/cgi/consolidationdegree/consolidated)."@en,
        "Tephra is subclass of sediment because it is generally not lithified, in which case it would be considered Rock."@en ;
    skos:prefLabel "Sediment"@en .

mat:soil a skos:Concept ;
    skos:broader mat:earthmaterial ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_00001998> ;
    skos:definition "Mixed granular mineral and organic matter modified by interaction between earth material, biosphere, and atmosphere, consisting of varying proportions of sand, silt, and clay, organic material such as humus, gases, liquids, and a broad range of resident micro- and macroorganisms. (https://en.wikipedia.org/wiki/Soil) Soil consists of horizons near the Earth's surface that, in contrast to the underlying parent material, have been altered by the interactions of climate, relief, and living organisms over time. (http://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280) (http://purl.obolibrary.org/obo/ENVO_00001998)"@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Soil"@en .

mat:rockorsediment a skos:Concept ;
    skos:broader mat:earthmaterial ;
    skos:definition "Material is rock or sediment.  For example core from boreholes that likely penetrate sediment near the surface and rock at greater depth, with descriptions that do not clearly distinguish non-consolidated sediment from rock."@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:narrower mat:rock,
        mat:sediment ;
    skos:note "Use for samples described as rock>sedimentary AND sediment, where it is unclear whether the sample is a consolidated 'rock' object, or loose disaggregated material in a bag."@en,
        "Use for samples like dredge hauls and ROV scoops that mix rock and sediment from a water body bottom."@en ;
    skos:prefLabel "Rock or sediment"@en ;
    skos:scopeNote "Distinct from 'Mixed soil, sediment or rock' that represents samples known to have components of all these materials."@en .

mat:earthmaterial a skos:Concept ;
    skos:broader mat:material ;
    skos:closeMatch <http://resource.geosciml.org/classifier/cgi/lithology/compound_material>,
        <https://w3id.org/gso/geology/Solid_Geologic_Material> ;
    skos:definition "A naturally occurring solid material that is not anthropogenic, biogenic, or ice."@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:narrower mat:mineral,
        mat:mixedsoilsedimentrock,
        mat:particulate,
        mat:rockorsediment,
        mat:soil ;
    skos:prefLabel "Natural Solid Material"@en .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SKOS Concept
description: JSON Schema for a SKOS Concept in JSON-LD form. A unit of thought within
  a concept scheme. Supports labels (prefLabel, altLabel, hiddenLabel), notations,
  hierarchical relations (broader/narrower), associative relations (related), cross-scheme
  mapping properties, scheme membership, and documentary notes. Based on the W3C SKOS
  Reference (https://www.w3.org/TR/skos-reference/).
type: object
properties:
  '@context':
    description: JSON-LD context declaring the skos namespace prefix. May be a single
      object or an array of strings and objects.
    anyOf:
    - type: object
      properties:
        skos:
          const: http://www.w3.org/2004/02/skos/core#
      required:
      - skos
    - type: array
      items:
        anyOf:
        - type: string
        - type: object
      contains:
        type: object
        properties:
          skos:
            const: http://www.w3.org/2004/02/skos/core#
        required:
        - skos
  '@id':
    type: string
    description: URI identifier for this concept.
  '@type':
    type: array
    items:
      type: string
    contains:
      const: skos:Concept
    minItems: 1
  skos:prefLabel:
    description: Preferred lexical label for this concept. A single string, a single
      language-tagged value, or an array of language-tagged values. Each language
      should appear at most once.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        $ref: '#/$defs/LanguageTaggedValue'
  skos:altLabel:
    description: Alternative lexical labels (acronyms, abbreviations, variants).
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:hiddenLabel:
    description: Labels accessible to free-text search but not displayed.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:notation:
    description: Classification code for this concept within a scheme.
    anyOf:
    - type: string
    - type: array
      items:
        type: string
  skos:definition:
    description: Formal explanation of the meaning of this concept.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:scopeNote:
    description: Note clarifying meaning and/or intended use.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:note:
    description: General note about this concept.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:historyNote:
    description: Note about past state or use.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:changeNote:
    description: Note documenting a change.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:editorialNote:
    description: Note for editors and maintainers.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:example:
    description: Example of use of this concept.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:inScheme:
    description: Concept scheme(s) this concept belongs to.
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
  skos:topConceptOf:
    description: Concept scheme(s) for which this is a top concept.
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
  skos:broader:
    description: Broader (parent) concepts in the hierarchy. Items are inline concept
      objects or @id references.
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/ConceptRef'
      - $ref: '#'
  skos:narrower:
    description: Narrower (child) concepts in the hierarchy. Items are inline concept
      objects or @id references.
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/ConceptRef'
      - $ref: '#'
  skos:related:
    description: Associatively related concepts.
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/ConceptRef'
      - $ref: '#'
  skos:exactMatch:
    description: Concepts in other schemes with equivalent meaning.
    type: array
    items:
      $ref: '#/$defs/ConceptRef'
  skos:closeMatch:
    description: Concepts in other schemes with similar meaning.
    type: array
    items:
      $ref: '#/$defs/ConceptRef'
  skos:broadMatch:
    description: Broader concepts in other schemes.
    type: array
    items:
      $ref: '#/$defs/ConceptRef'
  skos:narrowMatch:
    description: Narrower concepts in other schemes.
    type: array
    items:
      $ref: '#/$defs/ConceptRef'
  skos:relatedMatch:
    description: Related concepts in other schemes.
    type: array
    items:
      $ref: '#/$defs/ConceptRef'
required:
- '@type'
- skos:prefLabel
$defs:
  ConceptRef:
    type: object
    description: A reference to a SKOS Concept by URI.
    properties:
      '@id':
        type: string
        description: URI of the referenced concept.
    required:
    - '@id'
  LanguageTaggedValue:
    type: object
    description: An RDF literal value with a language tag, serialized as a JSON-LD
      value object.
    properties:
      '@value':
        type: string
        description: The text content.
      '@language':
        type: string
        description: BCP 47 language tag (e.g. en, fr, de).
    required:
    - '@value'
    - '@language'
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/context.jsonld)

## Sources

* [W3C SKOS Reference](https://www.w3.org/TR/skos-reference/)
* [SKOS Core Vocabulary (RDF)](https://www.w3.org/2004/02/skos/core.rdf)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/skosProperties/skosConcept`

