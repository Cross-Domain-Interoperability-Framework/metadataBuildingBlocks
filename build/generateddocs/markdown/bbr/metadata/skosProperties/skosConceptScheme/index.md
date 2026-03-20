
# SKOS Concept Scheme (Schema)

`cdif.bbr.metadata.skosProperties.skosConceptScheme` *v0.1*

JSON Schema for validating a SKOS ConceptScheme in native JSON-LD form. Validates skos:ConceptScheme root with prefLabel, hasTopConcept, and nested skos:Concept items with labels, notations, broader/narrower/related relations, mapping properties, documentary notes, and Collection/OrderedCollection groupings. Defines $defs: Concept, ConceptReference, LanguageTaggedValue, Collection, OrderedCollection.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## SKOS Concept Scheme

JSON Schema for validating a [SKOS ConceptScheme](https://www.w3.org/TR/skos-reference/#schemes) in native JSON-LD form, based on the [W3C SKOS vocabulary](https://www.w3.org/2004/02/skos/core.rdf).

### Root object (skos:ConceptScheme)

The root object must have `@type` including `skos:ConceptScheme`, a `skos:prefLabel`, and at least one `skos:hasTopConcept`. An `@id` or `skos:notation` is required for identification.

Optional scheme-level properties include `skos:definition`, `skos:notation`, documentary notes (`skos:scopeNote`, `skos:historyNote`, `skos:changeNote`, `skos:editorialNote`, `skos:example`), and Dublin Core metadata (`dcterms:creator`, `dcterms:created`, `dcterms:modified`, `dcterms:license`).

### Nested concepts (skos:Concept)

Concepts within `skos:hasTopConcept` (and recursively in `skos:narrower`) must have `@type` including `skos:Concept` and a `skos:prefLabel`. Concepts support:

- **Labels**: `skos:prefLabel`, `skos:altLabel`, `skos:hiddenLabel` (strings or language-tagged values)
- **Notations**: `skos:notation` (classification codes)
- **Hierarchy**: `skos:broader`, `skos:narrower` (inline concepts or `@id` references)
- **Association**: `skos:related`
- **Mapping**: `skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch` (cross-scheme `@id` references)
- **Scheme membership**: `skos:inScheme`, `skos:topConceptOf`
- **Notes**: all documentary note properties

### Collections

The schema also defines `skos:Collection` (unordered groupings with `skos:member`) and `skos:OrderedCollection` (ordered groupings with `skos:memberList` using the JSON-LD `@list` construct).

### Language-tagged values

Labels and notes can be simple strings or JSON-LD value objects with `@value` and `@language` for multilingual support.

## Examples

### SKOS Concept Scheme example
Earth Science Topics vocabulary with multilingual labels, hierarchical
concepts (broader/narrower), associative relations, cross-scheme mappings,
notations, and documentary notes.
#### json
```json
{
  "@context": {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dcterms": "http://purl.org/dc/terms/",
    "schema": "http://schema.org/",
    "mat": "https://w3id.org/isample/vocabulary/material/"
  },
  "@id": "mat:materialsvocabulary",
  "@type": ["skos:ConceptScheme"],
  "skos:prefLabel": {"@value": "iSamples Materials Vocabulary", "@language": "en"},
  "skos:definition": {"@value": "High level vocabulary to specify the kind of material that constitutes a physical sample", "@language": "en"},
  "dcterms:created": "2021-03-24",
  "dcterms:modified": "2024-08-14",
  "dcterms:creator": {"@id": "https://orcid.org/0000-0001-6041-5302"},
  "dcterms:license": {"@id": "https://creativecommons.org/licenses/by/4.0/legalcode"},
  "skos:historyNote": [
    {"@value": "2022-01-05 SMR version 0.9, change base uri to https://w3id.org/isample/vocabulary/material/0.9/ for testing with ESIP COR and w3id uri resolution", "@language": "en"},
    {"@value": "2022-03-11 SMR change definitions from rdfs:comment to skos:definition. Minor fixes to some definitions.  Add skos matches to URIs from other vocabularies; 2023-11-05 version 1.0, in preparation for release.", "@language": "en"},
    {"@value": "2024-08-14 SMR, various updates since 2023-12:  change seeAlso to closeMatch for Rock mapping to http://resource.geosciml.org/classifier/cgi/lithology/rock; minor edits to align with manuscript about the metadata schema; update vocabularies to use 'material sample' instead of 'specimen'; update schema.org namespace to http://; add provider and codeRepository in conceptScheme metadata; minor typo fixes and definition edits.", "@language": "en"},
    {"@value": "2024-09-13 remove version numbers from URI", "@language": "en"}
  ],
  "skos:hasTopConcept": [
    {
      "@id": "mat:material",
      "@type": ["skos:Concept"],
      "skos:prefLabel": {"@value": "Material", "@language": "en"},
      "skos:definition": {"@value": "Top Concept in iSamples Material Category scheme", "@language": "en"},
      "skos:inScheme": {"@id": "mat:materialsvocabulary"},
      "skos:topConceptOf": {"@id": "mat:materialsvocabulary"},
      "skos:closeMatch": [
        {"@id": "http://purl.obolibrary.org/obo/ENVO_00010483"},
        {"@id": "https://www.wikidata.org/wiki/Q214609"}
      ],
      "skos:narrower": [
        {
          "@id": "mat:anyanthropogenicmaterial",
          "@type": ["skos:Concept"],
          "skos:prefLabel": {"@value": "Anthropogenic material", "@language": "en"},
          "skos:definition": {"@value": "Material produced by human activity.", "@language": "en"},
          "skos:inScheme": {"@id": "mat:materialsvocabulary"},
          "skos:broader": [{"@id": "mat:material"}],
          "skos:exactMatch": [
            {"@id": "http://resource.geosciml.org/classifier/cgi/lithology/anthropogenic_material"},
            {"@id": "https://www.wikidata.org/wiki/Q116074152"}
          ],
          "skos:relatedMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_0010001"}],
          "skos:scopeNote": {"@value": "Material that would not be found in nature without human intervention. Thus clay would be a 'Mineral' material, but fired clay in a brick or ceramic would be an 'Anthropogenic material'.   Native copper would be a Mineral, but smelted copper, extracted from ore that might include native copper (among other sulfide and oxide minerals) would be 'Anthropogenic metal material'.", "@language": "en"},
          "skos:narrower": [
            {
              "@id": "mat:anthropogenicmetal",
              "@type": ["skos:Concept"],
              "skos:prefLabel": {"@value": "Anthropogenic metal material", "@language": "en"},
              "skos:definition": {"@value": "Metal that has been produced or used by humans. Samples of naturally occurring metallic material (e.g. native copper, gold nuggets) should be considered mineral material. Metallic material is material that when polished or fractured, shows a lustrous appearance, and conducts electricity and heat relatively well. Metals are typically malleable (they can be hammered into thin sheets) or ductile (can be drawn into wires). The boundaries between metals, nonmetals, and metalloids fluctuate slightly due to a lack of universally accepted definitions of the categories involved. (https://en.wikipedia.org/wiki/Metal, c.f. http://purl.obolibrary.org/obo/ENVO_01001069)", "@language": "en"},
              "skos:inScheme": {"@id": "mat:materialsvocabulary"},
              "skos:broader": [{"@id": "mat:anyanthropogenicmaterial"}],
              "skos:closeMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_01001069"}]
            },
            {
              "@id": "mat:otheranthropogenicmaterial",
              "@type": ["skos:Concept"],
              "skos:prefLabel": {"@value": "Other anthropogenic material", "@language": "en"},
              "skos:definition": {"@value": "Non-metallic material produced by human activity. Organic products of agricultural activity are both anthropogenic and organic. Include lab preparations like XRF pellet and rock powders. Examples: ceramics, concrete, slag, (anthropogenic) glass, mine tailing, plaster, waste.", "@language": "en"},
              "skos:inScheme": {"@id": "mat:materialsvocabulary"},
              "skos:broader": [{"@id": "mat:anyanthropogenicmaterial"}],
              "skos:relatedMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_0010001"}]
            }
          ]
        },
        {
          "@id": "mat:anyice",
          "@type": ["skos:Concept"],
          "skos:prefLabel": {"@value": "Any ice", "@language": "en"},
          "skos:definition": {"@value": "a material that is in a solid state under the temperature and pressure conditions of the preserved sample, but is a liquid or gas at Standard Temperature and Pressure (STP).", "@language": "en"},
          "skos:inScheme": {"@id": "mat:materialsvocabulary"},
          "skos:broader": [{"@id": "mat:material"}],
          "skos:closeMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_01001125"}],
          "skos:note": {"@value": "The US National Institute of Standards and Technology (NIST) standard temperature and pressure (STP) is 20 degrees C (68 degrees F) and 1 atm (14.696 psi, 101.325 kPa). This standard is also known as normal temperature and pressure (NTP).", "@language": "en"},
          "skos:scopeNote": {"@value": "Samples of non-aqueous ice should be classified as 'Any ice', based on decision that distinguishing 'ice that might or might not be aqueous' from 'non-aqueous ice' does not merit adding another class to the scheme.", "@language": "en"},
          "skos:narrower": [
            {
              "@id": "mat:waterice",
              "@type": ["skos:Concept"],
              "skos:prefLabel": {"@value": "Frozen water", "@language": "en"},
              "skos:altLabel": {"@value": "Water ice", "@language": "en"},
              "skos:definition": {"@value": "Water that is in a solid state.", "@language": "en"},
              "skos:inScheme": {"@id": "mat:materialsvocabulary"},
              "skos:broader": [{"@id": "mat:anyice"}],
              "skos:exactMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_01000277"}]
            }
          ]
        },
        {
          "@id": "mat:biogenicnonorganicmaterial",
          "@type": ["skos:Concept"],
          "skos:prefLabel": {"@value": "Biogenic non-organic material", "@language": "en"},
          "skos:definition": {"@value": "Material produced by an organism but not composed of 'very large molecules of biological origin.' E.g. bone, tooth, shell, coral skeleton,", "@language": "en"},
          "skos:inScheme": {"@id": "mat:materialsvocabulary"},
          "skos:broader": [{"@id": "mat:material"}],
          "skos:narrowMatch": [
            {"@id": "http://purl.obolibrary.org/obo/CHEBI_64389"},
            {"@id": "http://purl.obolibrary.org/obo/ENVO_01001644"},
            {"@id": "http://purl.obolibrary.org/obo/UBERON_0002481"}
          ],
          "skos:note": {"@value": "Include ash from burned biogenic material. Biogenic non-organic material is intended to cover biogenic products consisting of mineral or mineraloid substance, e.g. apatite (or other Ca phosphates), aragonite (or other Ca carbonate) typical of shells, bone, teeth.", "@language": "en"}
        },
        {
          "@id": "mat:dispersedmedia",
          "@type": ["skos:Concept"],
          "skos:prefLabel": {"@value": "Dispersed media", "@language": "en"},
          "skos:definition": {"@value": "Material that contains discrete elements of some material dispersed in a continuous fluid medium.  The dispersed component can be a gas, a liquid or a solid (based on https://en.wikipedia.org/wiki/Dispersed_media). Does not include mixtures of granular material like soil, sediment, particulate, or solids that would be considered  rock material.", "@language": "en"},
          "skos:inScheme": {"@id": "mat:materialsvocabulary"},
          "skos:broader": [{"@id": "mat:material"}],
          "skos:narrowMatch": [
            {"@id": "http://purl.obolibrary.org/obo/ENVO_00010506"},
            {"@id": "http://purl.obolibrary.org/obo/ENVO_01001560"},
            {"@id": "https://www.wikidata.org/wiki/Q181780"}
          ]
        },
        {
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
              "skos:definition": {"@value": "Material consists of microscopic particulate material derived by precipitation, filtering, or settling from suspension in a fluid, e.g. filtrate from water, deposition from atmosphere, astro material particles. Might include mineral, organic, or biological material.", "@language": "en"},
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
        },
        {
          "@id": "mat:fluid",
          "@type": ["skos:Concept"],
          "skos:prefLabel": {"@value": "Fluid material", "@language": "en"},
          "skos:definition": {"@value": "Substance that continually deforms (flows) under an applied shear stress, or external force. Fluids are a phase of matter and include liquids, gases and plasmas. They are substances with zero or small shear modulus, and flow at a perceptible rate under any shear force applied to them. (https://en.wikipedia.org/wiki/Fluid)", "@language": "en"},
          "skos:inScheme": {"@id": "mat:materialsvocabulary"},
          "skos:broader": [{"@id": "mat:material"}],
          "skos:closeMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_02000140"}],
          "skos:narrower": [
            {
              "@id": "mat:gas",
              "@type": ["skos:Concept"],
              "skos:prefLabel": {"@value": "Gaseous material", "@language": "en"},
              "skos:definition": {"@value": "Material composed of one or more chemical entities that has neither independent shape nor volume but tends to expand indefinitely (http://purl.obolibrary.org/obo/ENVO_01000797). Infer that the sample is curated in some kind of container.", "@language": "en"},
              "skos:inScheme": {"@id": "mat:materialsvocabulary"},
              "skos:broader": [{"@id": "mat:fluid"}],
              "skos:exactMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_01000797"}]
            },
            {
              "@id": "mat:liquidwater",
              "@type": ["skos:Concept"],
              "skos:prefLabel": {"@value": "Liquid water", "@language": "en"},
              "skos:definition": {"@value": "A material primarily composed of dihydrogen oxide in its liquid form; infer that the sample is curated in some kind of container.", "@language": "en"},
              "skos:inScheme": {"@id": "mat:materialsvocabulary"},
              "skos:broader": [{"@id": "mat:fluid"}],
              "skos:exactMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_00002006"}]
            },
            {
              "@id": "mat:nonaqueousliquid",
              "@type": ["skos:Concept"],
              "skos:prefLabel": {"@value": "Non-aqueous liquid material", "@language": "en"},
              "skos:definition": {"@value": "Liquid composed dominantly of material other than water. Includes liquids that do not fit in any other category. E.g. alcohol, petroleum.", "@language": "en"},
              "skos:inScheme": {"@id": "mat:materialsvocabulary"},
              "skos:broader": [{"@id": "mat:fluid"}],
              "skos:narrowMatch": [
                {"@id": "http://purl.bioontology.org/ontology/PDQ/CDR0000446576"},
                {"@id": "http://purl.obolibrary.org/obo/ENVO_00002984"}
              ],
              "skos:scopeNote": {"@value": "Fluids like blood, urine, mucus are problematic. Suggest categorizing as 'Non-aqueous liquid material' and 'Organic material'. Need example use cases.", "@language": "en"}
            }
          ]
        },
        {
          "@id": "mat:organicmaterial",
          "@type": ["skos:Concept"],
          "skos:prefLabel": {"@value": "Organic material", "@language": "en"},
          "skos:definition": {"@value": "Material derived from living organisms and composed primarily of one or more very large molecules of biological origin. Examples: body (animal or plant), body part, fecal matter, seeds, wood, tissue, biological fluids, biological waste, algal material, biofilm, necromass, plankton. source: http://purl.obolibrary.org/obo/ENVO_01000155", "@language": "en"},
          "skos:inScheme": {"@id": "mat:materialsvocabulary"},
          "skos:broader": [{"@id": "mat:material"}],
          "skos:closeMatch": [{"@id": "http://purl.obolibrary.org/obo/ENVO_01000155"}],
          "skos:scopeNote": {"@value": "Distinction from 'Biogenic non-organic material' is fuzzy. Biogenic non-organic material is intended to cover biogenic products consisting of mineral or mineraloid substance, e.g. apatite (or other Ca phosphates), aragonite (or other Ca carbonate) typical of shells, bone, teeth.", "@language": "en"}
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConceptScheme/context.jsonld",
    {
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "dcterms": "http://purl.org/dc/terms/",
      "schema": "http://schema.org/",
      "mat": "https://w3id.org/isample/vocabulary/material/"
    }
  ],
  "@id": "mat:materialsvocabulary",
  "@type": [
    "skos:ConceptScheme"
  ],
  "skos:prefLabel": {
    "@value": "iSamples Materials Vocabulary",
    "@language": "en"
  },
  "skos:definition": {
    "@value": "High level vocabulary to specify the kind of material that constitutes a physical sample",
    "@language": "en"
  },
  "dcterms:created": "2021-03-24",
  "dcterms:modified": "2024-08-14",
  "dcterms:creator": {
    "@id": "https://orcid.org/0000-0001-6041-5302"
  },
  "dcterms:license": {
    "@id": "https://creativecommons.org/licenses/by/4.0/legalcode"
  },
  "skos:historyNote": [
    {
      "@value": "2022-01-05 SMR version 0.9, change base uri to https://w3id.org/isample/vocabulary/material/0.9/ for testing with ESIP COR and w3id uri resolution",
      "@language": "en"
    },
    {
      "@value": "2022-03-11 SMR change definitions from rdfs:comment to skos:definition. Minor fixes to some definitions.  Add skos matches to URIs from other vocabularies; 2023-11-05 version 1.0, in preparation for release.",
      "@language": "en"
    },
    {
      "@value": "2024-08-14 SMR, various updates since 2023-12:  change seeAlso to closeMatch for Rock mapping to http://resource.geosciml.org/classifier/cgi/lithology/rock; minor edits to align with manuscript about the metadata schema; update vocabularies to use 'material sample' instead of 'specimen'; update schema.org namespace to http://; add provider and codeRepository in conceptScheme metadata; minor typo fixes and definition edits.",
      "@language": "en"
    },
    {
      "@value": "2024-09-13 remove version numbers from URI",
      "@language": "en"
    }
  ],
  "skos:hasTopConcept": [
    {
      "@id": "mat:material",
      "@type": [
        "skos:Concept"
      ],
      "skos:prefLabel": {
        "@value": "Material",
        "@language": "en"
      },
      "skos:definition": {
        "@value": "Top Concept in iSamples Material Category scheme",
        "@language": "en"
      },
      "skos:inScheme": {
        "@id": "mat:materialsvocabulary"
      },
      "skos:topConceptOf": {
        "@id": "mat:materialsvocabulary"
      },
      "skos:closeMatch": [
        {
          "@id": "http://purl.obolibrary.org/obo/ENVO_00010483"
        },
        {
          "@id": "https://www.wikidata.org/wiki/Q214609"
        }
      ],
      "skos:narrower": [
        {
          "@id": "mat:anyanthropogenicmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": {
            "@value": "Anthropogenic material",
            "@language": "en"
          },
          "skos:definition": {
            "@value": "Material produced by human activity.",
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
          "skos:exactMatch": [
            {
              "@id": "http://resource.geosciml.org/classifier/cgi/lithology/anthropogenic_material"
            },
            {
              "@id": "https://www.wikidata.org/wiki/Q116074152"
            }
          ],
          "skos:relatedMatch": [
            {
              "@id": "http://purl.obolibrary.org/obo/ENVO_0010001"
            }
          ],
          "skos:scopeNote": {
            "@value": "Material that would not be found in nature without human intervention. Thus clay would be a 'Mineral' material, but fired clay in a brick or ceramic would be an 'Anthropogenic material'.   Native copper would be a Mineral, but smelted copper, extracted from ore that might include native copper (among other sulfide and oxide minerals) would be 'Anthropogenic metal material'.",
            "@language": "en"
          },
          "skos:narrower": [
            {
              "@id": "mat:anthropogenicmetal",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": {
                "@value": "Anthropogenic metal material",
                "@language": "en"
              },
              "skos:definition": {
                "@value": "Metal that has been produced or used by humans. Samples of naturally occurring metallic material (e.g. native copper, gold nuggets) should be considered mineral material. Metallic material is material that when polished or fractured, shows a lustrous appearance, and conducts electricity and heat relatively well. Metals are typically malleable (they can be hammered into thin sheets) or ductile (can be drawn into wires). The boundaries between metals, nonmetals, and metalloids fluctuate slightly due to a lack of universally accepted definitions of the categories involved. (https://en.wikipedia.org/wiki/Metal, c.f. http://purl.obolibrary.org/obo/ENVO_01001069)",
                "@language": "en"
              },
              "skos:inScheme": {
                "@id": "mat:materialsvocabulary"
              },
              "skos:broader": [
                {
                  "@id": "mat:anyanthropogenicmaterial"
                }
              ],
              "skos:closeMatch": [
                {
                  "@id": "http://purl.obolibrary.org/obo/ENVO_01001069"
                }
              ]
            },
            {
              "@id": "mat:otheranthropogenicmaterial",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": {
                "@value": "Other anthropogenic material",
                "@language": "en"
              },
              "skos:definition": {
                "@value": "Non-metallic material produced by human activity. Organic products of agricultural activity are both anthropogenic and organic. Include lab preparations like XRF pellet and rock powders. Examples: ceramics, concrete, slag, (anthropogenic) glass, mine tailing, plaster, waste.",
                "@language": "en"
              },
              "skos:inScheme": {
                "@id": "mat:materialsvocabulary"
              },
              "skos:broader": [
                {
                  "@id": "mat:anyanthropogenicmaterial"
                }
              ],
              "skos:relatedMatch": [
                {
                  "@id": "http://purl.obolibrary.org/obo/ENVO_0010001"
                }
              ]
            }
          ]
        },
        {
          "@id": "mat:anyice",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": {
            "@value": "Any ice",
            "@language": "en"
          },
          "skos:definition": {
            "@value": "a material that is in a solid state under the temperature and pressure conditions of the preserved sample, but is a liquid or gas at Standard Temperature and Pressure (STP).",
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
              "@id": "http://purl.obolibrary.org/obo/ENVO_01001125"
            }
          ],
          "skos:note": {
            "@value": "The US National Institute of Standards and Technology (NIST) standard temperature and pressure (STP) is 20 degrees C (68 degrees F) and 1 atm (14.696 psi, 101.325 kPa). This standard is also known as normal temperature and pressure (NTP).",
            "@language": "en"
          },
          "skos:scopeNote": {
            "@value": "Samples of non-aqueous ice should be classified as 'Any ice', based on decision that distinguishing 'ice that might or might not be aqueous' from 'non-aqueous ice' does not merit adding another class to the scheme.",
            "@language": "en"
          },
          "skos:narrower": [
            {
              "@id": "mat:waterice",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": {
                "@value": "Frozen water",
                "@language": "en"
              },
              "skos:altLabel": {
                "@value": "Water ice",
                "@language": "en"
              },
              "skos:definition": {
                "@value": "Water that is in a solid state.",
                "@language": "en"
              },
              "skos:inScheme": {
                "@id": "mat:materialsvocabulary"
              },
              "skos:broader": [
                {
                  "@id": "mat:anyice"
                }
              ],
              "skos:exactMatch": [
                {
                  "@id": "http://purl.obolibrary.org/obo/ENVO_01000277"
                }
              ]
            }
          ]
        },
        {
          "@id": "mat:biogenicnonorganicmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": {
            "@value": "Biogenic non-organic material",
            "@language": "en"
          },
          "skos:definition": {
            "@value": "Material produced by an organism but not composed of 'very large molecules of biological origin.' E.g. bone, tooth, shell, coral skeleton,",
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
          "skos:narrowMatch": [
            {
              "@id": "http://purl.obolibrary.org/obo/CHEBI_64389"
            },
            {
              "@id": "http://purl.obolibrary.org/obo/ENVO_01001644"
            },
            {
              "@id": "http://purl.obolibrary.org/obo/UBERON_0002481"
            }
          ],
          "skos:note": {
            "@value": "Include ash from burned biogenic material. Biogenic non-organic material is intended to cover biogenic products consisting of mineral or mineraloid substance, e.g. apatite (or other Ca phosphates), aragonite (or other Ca carbonate) typical of shells, bone, teeth.",
            "@language": "en"
          }
        },
        {
          "@id": "mat:dispersedmedia",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": {
            "@value": "Dispersed media",
            "@language": "en"
          },
          "skos:definition": {
            "@value": "Material that contains discrete elements of some material dispersed in a continuous fluid medium.  The dispersed component can be a gas, a liquid or a solid (based on https://en.wikipedia.org/wiki/Dispersed_media). Does not include mixtures of granular material like soil, sediment, particulate, or solids that would be considered  rock material.",
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
          "skos:narrowMatch": [
            {
              "@id": "http://purl.obolibrary.org/obo/ENVO_00010506"
            },
            {
              "@id": "http://purl.obolibrary.org/obo/ENVO_01001560"
            },
            {
              "@id": "https://www.wikidata.org/wiki/Q181780"
            }
          ]
        },
        {
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
                "@value": "Material consists of microscopic particulate material derived by precipitation, filtering, or settling from suspension in a fluid, e.g. filtrate from water, deposition from atmosphere, astro material particles. Might include mineral, organic, or biological material.",
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
        },
        {
          "@id": "mat:fluid",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": {
            "@value": "Fluid material",
            "@language": "en"
          },
          "skos:definition": {
            "@value": "Substance that continually deforms (flows) under an applied shear stress, or external force. Fluids are a phase of matter and include liquids, gases and plasmas. They are substances with zero or small shear modulus, and flow at a perceptible rate under any shear force applied to them. (https://en.wikipedia.org/wiki/Fluid)",
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
              "@id": "http://purl.obolibrary.org/obo/ENVO_02000140"
            }
          ],
          "skos:narrower": [
            {
              "@id": "mat:gas",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": {
                "@value": "Gaseous material",
                "@language": "en"
              },
              "skos:definition": {
                "@value": "Material composed of one or more chemical entities that has neither independent shape nor volume but tends to expand indefinitely (http://purl.obolibrary.org/obo/ENVO_01000797). Infer that the sample is curated in some kind of container.",
                "@language": "en"
              },
              "skos:inScheme": {
                "@id": "mat:materialsvocabulary"
              },
              "skos:broader": [
                {
                  "@id": "mat:fluid"
                }
              ],
              "skos:exactMatch": [
                {
                  "@id": "http://purl.obolibrary.org/obo/ENVO_01000797"
                }
              ]
            },
            {
              "@id": "mat:liquidwater",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": {
                "@value": "Liquid water",
                "@language": "en"
              },
              "skos:definition": {
                "@value": "A material primarily composed of dihydrogen oxide in its liquid form; infer that the sample is curated in some kind of container.",
                "@language": "en"
              },
              "skos:inScheme": {
                "@id": "mat:materialsvocabulary"
              },
              "skos:broader": [
                {
                  "@id": "mat:fluid"
                }
              ],
              "skos:exactMatch": [
                {
                  "@id": "http://purl.obolibrary.org/obo/ENVO_00002006"
                }
              ]
            },
            {
              "@id": "mat:nonaqueousliquid",
              "@type": [
                "skos:Concept"
              ],
              "skos:prefLabel": {
                "@value": "Non-aqueous liquid material",
                "@language": "en"
              },
              "skos:definition": {
                "@value": "Liquid composed dominantly of material other than water. Includes liquids that do not fit in any other category. E.g. alcohol, petroleum.",
                "@language": "en"
              },
              "skos:inScheme": {
                "@id": "mat:materialsvocabulary"
              },
              "skos:broader": [
                {
                  "@id": "mat:fluid"
                }
              ],
              "skos:narrowMatch": [
                {
                  "@id": "http://purl.bioontology.org/ontology/PDQ/CDR0000446576"
                },
                {
                  "@id": "http://purl.obolibrary.org/obo/ENVO_00002984"
                }
              ],
              "skos:scopeNote": {
                "@value": "Fluids like blood, urine, mucus are problematic. Suggest categorizing as 'Non-aqueous liquid material' and 'Organic material'. Need example use cases.",
                "@language": "en"
              }
            }
          ]
        },
        {
          "@id": "mat:organicmaterial",
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": {
            "@value": "Organic material",
            "@language": "en"
          },
          "skos:definition": {
            "@value": "Material derived from living organisms and composed primarily of one or more very large molecules of biological origin. Examples: body (animal or plant), body part, fecal matter, seeds, wood, tissue, biological fluids, biological waste, algal material, biofilm, necromass, plankton. source: http://purl.obolibrary.org/obo/ENVO_01000155",
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
              "@id": "http://purl.obolibrary.org/obo/ENVO_01000155"
            }
          ],
          "skos:scopeNote": {
            "@value": "Distinction from 'Biogenic non-organic material' is fuzzy. Biogenic non-organic material is intended to cover biogenic products consisting of mineral or mineraloid substance, e.g. apatite (or other Ca phosphates), aragonite (or other Ca carbonate) typical of shells, bone, teeth.",
            "@language": "en"
          }
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix mat: <https://w3id.org/isample/vocabulary/material/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

mat:anthropogenicmetal a skos:Concept ;
    skos:broader mat:anyanthropogenicmaterial ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_01001069> ;
    skos:definition "Metal that has been produced or used by humans. Samples of naturally occurring metallic material (e.g. native copper, gold nuggets) should be considered mineral material. Metallic material is material that when polished or fractured, shows a lustrous appearance, and conducts electricity and heat relatively well. Metals are typically malleable (they can be hammered into thin sheets) or ductile (can be drawn into wires). The boundaries between metals, nonmetals, and metalloids fluctuate slightly due to a lack of universally accepted definitions of the categories involved. (https://en.wikipedia.org/wiki/Metal, c.f. http://purl.obolibrary.org/obo/ENVO_01001069)"@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Anthropogenic metal material"@en .

mat:biogenicnonorganicmaterial a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "Material produced by an organism but not composed of 'very large molecules of biological origin.' E.g. bone, tooth, shell, coral skeleton,"@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:narrowMatch <http://purl.obolibrary.org/obo/CHEBI_64389>,
        <http://purl.obolibrary.org/obo/ENVO_01001644>,
        <http://purl.obolibrary.org/obo/UBERON_0002481> ;
    skos:note "Include ash from burned biogenic material. Biogenic non-organic material is intended to cover biogenic products consisting of mineral or mineraloid substance, e.g. apatite (or other Ca phosphates), aragonite (or other Ca carbonate) typical of shells, bone, teeth."@en ;
    skos:prefLabel "Biogenic non-organic material"@en .

mat:dispersedmedia a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "Material that contains discrete elements of some material dispersed in a continuous fluid medium.  The dispersed component can be a gas, a liquid or a solid (based on https://en.wikipedia.org/wiki/Dispersed_media). Does not include mixtures of granular material like soil, sediment, particulate, or solids that would be considered  rock material."@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:narrowMatch <http://purl.obolibrary.org/obo/ENVO_00010506>,
        <http://purl.obolibrary.org/obo/ENVO_01001560>,
        <https://www.wikidata.org/wiki/Q181780> ;
    skos:prefLabel "Dispersed media"@en .

mat:gas a skos:Concept ;
    skos:broader mat:fluid ;
    skos:definition "Material composed of one or more chemical entities that has neither independent shape nor volume but tends to expand indefinitely (http://purl.obolibrary.org/obo/ENVO_01000797). Infer that the sample is curated in some kind of container."@en ;
    skos:exactMatch <http://purl.obolibrary.org/obo/ENVO_01000797> ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Gaseous material"@en .

mat:liquidwater a skos:Concept ;
    skos:broader mat:fluid ;
    skos:definition "A material primarily composed of dihydrogen oxide in its liquid form; infer that the sample is curated in some kind of container."@en ;
    skos:exactMatch <http://purl.obolibrary.org/obo/ENVO_00002006> ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Liquid water"@en .

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

mat:nonaqueousliquid a skos:Concept ;
    skos:broader mat:fluid ;
    skos:definition "Liquid composed dominantly of material other than water. Includes liquids that do not fit in any other category. E.g. alcohol, petroleum."@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:narrowMatch <http://purl.bioontology.org/ontology/PDQ/CDR0000446576>,
        <http://purl.obolibrary.org/obo/ENVO_00002984> ;
    skos:prefLabel "Non-aqueous liquid material"@en ;
    skos:scopeNote "Fluids like blood, urine, mucus are problematic. Suggest categorizing as 'Non-aqueous liquid material' and 'Organic material'. Need example use cases."@en .

mat:organicmaterial a skos:Concept ;
    skos:broader mat:material ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_01000155> ;
    skos:definition "Material derived from living organisms and composed primarily of one or more very large molecules of biological origin. Examples: body (animal or plant), body part, fecal matter, seeds, wood, tissue, biological fluids, biological waste, algal material, biofilm, necromass, plankton. source: http://purl.obolibrary.org/obo/ENVO_01000155"@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Organic material"@en ;
    skos:scopeNote "Distinction from 'Biogenic non-organic material' is fuzzy. Biogenic non-organic material is intended to cover biogenic products consisting of mineral or mineraloid substance, e.g. apatite (or other Ca phosphates), aragonite (or other Ca carbonate) typical of shells, bone, teeth."@en .

mat:otheranthropogenicmaterial a skos:Concept ;
    skos:broader mat:anyanthropogenicmaterial ;
    skos:definition "Non-metallic material produced by human activity. Organic products of agricultural activity are both anthropogenic and organic. Include lab preparations like XRF pellet and rock powders. Examples: ceramics, concrete, slag, (anthropogenic) glass, mine tailing, plaster, waste."@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Other anthropogenic material"@en ;
    skos:relatedMatch <http://purl.obolibrary.org/obo/ENVO_0010001> .

mat:particulate a skos:Concept ;
    skos:broader mat:earthmaterial ;
    skos:definition "Material consists of microscopic particulate material derived by precipitation, filtering, or settling from suspension in a fluid, e.g. filtrate from water, deposition from atmosphere, astro material particles. Might include mineral, organic, or biological material."@en ;
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

mat:waterice a skos:Concept ;
    skos:altLabel "Water ice"@en ;
    skos:broader mat:anyice ;
    skos:definition "Water that is in a solid state."@en ;
    skos:exactMatch <http://purl.obolibrary.org/obo/ENVO_01000277> ;
    skos:inScheme mat:materialsvocabulary ;
    skos:prefLabel "Frozen water"@en .

mat:anyice a skos:Concept ;
    skos:broader mat:material ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_01001125> ;
    skos:definition "a material that is in a solid state under the temperature and pressure conditions of the preserved sample, but is a liquid or gas at Standard Temperature and Pressure (STP)."@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:narrower mat:waterice ;
    skos:note "The US National Institute of Standards and Technology (NIST) standard temperature and pressure (STP) is 20 degrees C (68 degrees F) and 1 atm (14.696 psi, 101.325 kPa). This standard is also known as normal temperature and pressure (NTP)."@en ;
    skos:prefLabel "Any ice"@en ;
    skos:scopeNote "Samples of non-aqueous ice should be classified as 'Any ice', based on decision that distinguishing 'ice that might or might not be aqueous' from 'non-aqueous ice' does not merit adding another class to the scheme."@en .

mat:anyanthropogenicmaterial a skos:Concept ;
    skos:broader mat:material ;
    skos:definition "Material produced by human activity."@en ;
    skos:exactMatch <http://resource.geosciml.org/classifier/cgi/lithology/anthropogenic_material>,
        <https://www.wikidata.org/wiki/Q116074152> ;
    skos:inScheme mat:materialsvocabulary ;
    skos:narrower mat:anthropogenicmetal,
        mat:otheranthropogenicmaterial ;
    skos:prefLabel "Anthropogenic material"@en ;
    skos:relatedMatch <http://purl.obolibrary.org/obo/ENVO_0010001> ;
    skos:scopeNote "Material that would not be found in nature without human intervention. Thus clay would be a 'Mineral' material, but fired clay in a brick or ceramic would be an 'Anthropogenic material'.   Native copper would be a Mineral, but smelted copper, extracted from ore that might include native copper (among other sulfide and oxide minerals) would be 'Anthropogenic metal material'."@en .

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

mat:fluid a skos:Concept ;
    skos:broader mat:material ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_02000140> ;
    skos:definition "Substance that continually deforms (flows) under an applied shear stress, or external force. Fluids are a phase of matter and include liquids, gases and plasmas. They are substances with zero or small shear modulus, and flow at a perceptible rate under any shear force applied to them. (https://en.wikipedia.org/wiki/Fluid)"@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:narrower mat:gas,
        mat:liquidwater,
        mat:nonaqueousliquid ;
    skos:prefLabel "Fluid material"@en .

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

mat:material a skos:Concept ;
    skos:closeMatch <http://purl.obolibrary.org/obo/ENVO_00010483>,
        <https://www.wikidata.org/wiki/Q214609> ;
    skos:definition "Top Concept in iSamples Material Category scheme"@en ;
    skos:inScheme mat:materialsvocabulary ;
    skos:narrower mat:anyanthropogenicmaterial,
        mat:anyice,
        mat:biogenicnonorganicmaterial,
        mat:dispersedmedia,
        mat:earthmaterial,
        mat:fluid,
        mat:organicmaterial ;
    skos:prefLabel "Material"@en ;
    skos:topConceptOf mat:materialsvocabulary .

mat:materialsvocabulary a skos:ConceptScheme ;
    dcterms:created "2021-03-24" ;
    dcterms:creator <https://orcid.org/0000-0001-6041-5302> ;
    dcterms:license <https://creativecommons.org/licenses/by/4.0/legalcode> ;
    dcterms:modified "2024-08-14" ;
    skos:definition "High level vocabulary to specify the kind of material that constitutes a physical sample"@en ;
    skos:hasTopConcept mat:material ;
    skos:historyNote "2022-01-05 SMR version 0.9, change base uri to https://w3id.org/isample/vocabulary/material/0.9/ for testing with ESIP COR and w3id uri resolution"@en,
        "2022-03-11 SMR change definitions from rdfs:comment to skos:definition. Minor fixes to some definitions.  Add skos matches to URIs from other vocabularies; 2023-11-05 version 1.0, in preparation for release."@en,
        "2024-08-14 SMR, various updates since 2023-12:  change seeAlso to closeMatch for Rock mapping to http://resource.geosciml.org/classifier/cgi/lithology/rock; minor edits to align with manuscript about the metadata schema; update vocabularies to use 'material sample' instead of 'specimen'; update schema.org namespace to http://; add provider and codeRepository in conceptScheme metadata; minor typo fixes and definition edits."@en,
        "2024-09-13 remove version numbers from URI"@en ;
    skos:prefLabel "iSamples Materials Vocabulary"@en .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SKOS Concept Scheme
description: JSON Schema for a SKOS ConceptScheme in JSON-LD form. Validates the root
  object as a skos:ConceptScheme with prefLabel, hasTopConcept, and nested skos:Concept
  items. References the skosConcept and skosCollection building blocks. Based on the
  W3C SKOS Reference (https://www.w3.org/TR/skos-reference/) and the SKOS RDF vocabulary
  (https://www.w3.org/2004/02/skos/core.rdf).
type: object
properties:
  '@context':
    description: JSON-LD context declaring the skos namespace prefix and any additional
      prefixes used in concept URIs. May be a single object or an array of strings
      and objects.
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
    description: URI identifier for this concept scheme.
  '@type':
    type: array
    items:
      type: string
    contains:
      const: skos:ConceptScheme
    minItems: 1
  skos:prefLabel:
    description: Preferred lexical label for the concept scheme. A single string,
      a single language-tagged value, or an array of language-tagged values. Each
      language should appear at most once.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        $ref: '#/$defs/LanguageTaggedValue'
  skos:altLabel:
    description: Alternative lexical labels (acronyms, abbreviations, spelling variants).
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
  skos:definition:
    description: Formal explanation of the meaning or purpose of this concept scheme.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:notation:
    description: Classification code or notation for this concept scheme.
    anyOf:
    - type: string
    - type: array
      items:
        type: string
  skos:note:
    description: General note about the concept scheme.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:scopeNote:
    description: Note clarifying the intended scope of the concept scheme.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:historyNote:
    description: Note about the history of the concept scheme.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:changeNote:
    description: Note documenting a change to the concept scheme.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:editorialNote:
    description: Note for editors, translators, and maintainers.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:example:
    description: Example of the use of this concept scheme.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
    - type: array
      items:
        anyOf:
        - type: string
        - $ref: '#/$defs/LanguageTaggedValue'
  skos:hasTopConcept:
    description: Top-level concepts in this scheme. Each item is a skos:Concept (inline
      or @id reference).
    type: array
    minItems: 1
    items:
      anyOf:
      - $ref: '#/$defs/Concept'
      - type: object
        properties:
          '@id':
            type: string
            description: URI reference to a concept defined elsewhere
        required:
        - '@id'
  dcterms:creator:
    description: Agent(s) who created this concept scheme.
    anyOf:
    - type: string
    - type: object
      properties:
        '@id':
          type: string
        schema:name:
          type: string
    - type: array
      items:
        anyOf:
        - type: string
        - type: object
          properties:
            '@id':
              type: string
            schema:name:
              type: string
  dcterms:created:
    type: string
    description: Date the concept scheme was created (ISO 8601).
  dcterms:modified:
    type: string
    description: Date the concept scheme was last modified (ISO 8601).
  dcterms:title:
    description: Title of the concept scheme (Dublin Core). Prefer skos:prefLabel
      for the SKOS label; dcterms:title may be used for additional metadata.
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
  dcterms:description:
    description: Description of the concept scheme (Dublin Core).
    anyOf:
    - type: string
    - $ref: '#/$defs/LanguageTaggedValue'
  dcterms:license:
    description: License for the concept scheme.
    anyOf:
    - type: string
    - type: object
      properties:
        '@id':
          type: string
  dcterms:rights:
    description: Rights statement for the concept scheme.
    type: string
  schema:version:
    description: Version identifier for the concept scheme.
    type:
    - string
    - number
required:
- '@type'
- skos:prefLabel
$defs:
  Concept:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
  LanguageTaggedValue:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml#/$defs/LanguageTaggedValue
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  dcterms: http://purl.org/dc/terms/
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConceptScheme/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConceptScheme/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConceptScheme/context.jsonld)

## Sources

* [W3C SKOS Reference](https://www.w3.org/TR/skos-reference/)
* [SKOS Core Vocabulary (RDF)](https://www.w3.org/2004/02/skos/core.rdf)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/skosProperties/skosConceptScheme`

