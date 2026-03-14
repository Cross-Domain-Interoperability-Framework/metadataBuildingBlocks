
# Analytical instrument properties for x-ray absorption spectroscopy (Schema)

`cdif.bbr.metadata.xasProperties.xasInstrument` *v0.1*

Schema defining properties for documenting instrumentation used in XAS analysis. Extends the generic instrument building block with required wd:Q3099911 (scientific instrument) additionalType. Supports hierarchical instrument systems via schema:hasPart referencing the generic instrument for sub-components. Defines properties: @type, schema:additionalType, schema:name, schema:identifier, schema:description, schema:additionalProperty, schema:hasPart. Uses building blocks: identifier (schemaorgProperties), additionalProperty (schemaorgProperties), instrument (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## XAS Instrument properties

XAS-specific instrument definition requiring schema:Product + schema:Thing typing and Wikidata scientific instrument additionalType (wd:Q3099911). Supports hierarchical sub-components via schema:hasPart for beamline elements (source, monochromator, detector).

### Defined properties

- **@type** — must include both schema:Product and schema:Thing
- **schema:additionalType** — must include wd:Q3099911 (scientific instrument)
- **schema:name** — name of the instrument
- **schema:identifier** — identifier for the instrument (string or Identifier object)
- **schema:description** — description of the instrument
- **schema:additionalProperty** — domain-specific properties (varies by instrument type)
- **schema:hasPart** — sub-components of the instrument system

### Dependencies

- [identifier](../../schemaorgProperties/identifier/) — structured identifier pattern
- [additionalProperty](../../schemaorgProperties/additionalProperty/) — PropertyValue for extension properties
- [instrument](../../schemaorgProperties/instrument/) — base generic instrument schema

## Examples

### Example instrument description.
Example use wikidata id for additionalType scientific equipment , schema.org Product and Thing
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "xas": "https://xas.org/dictionary/",
        "nxs": "http://purl.org/nexusformat/definitions/",
        "wd": "https://www.wikidata.org/entity/"
    },
    "@id": "ex:exampleWebAPI_354btrh",
    "@type": [
        "schema:Thing",
        "schema:Product"
    ],
    "schema:additionalType": [
        "xas:Beamline",
        "wd:Q3099911"
    ],
    "schema:name": "13-BM-D",
    "schema:description":"wikidata 3099911 is scientific instrument",
    "schema:identifier": "should have a registry with URIs",
    "schema:additionalProperty": [
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": ["xas:collimation"],
            "schema:name": "collimation technique",
            "schema:value": "none"
        },
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": ["xas:focusing"],
            "schema:name": "focusing",
            "schema:value": "unknown"
        },
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": ["xas:harmonic_rejection"],
            "schema:name": "harmonic_rejection",
            "schema:value": "Rh-coated mirror, detuned"
        }
    ]
}
```

#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "dcterms": "http://purl.org/dc/terms/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "xas": "https://xas.org/dictionary/",
        "nxs": "http://purl.org/nexusformat/definitions/",
        "prov": "http://www.w3.org/ns/prov#",
        "wd": "https://www.wikidata.org/entity/"
    },
    "@id": "xas:487y54",
    "@type": [
        "schema:Thing",
        "schema:Product"
    ],
    "schema:additionalType": ["wd:Q3099911"],
    "schema:name":"x-ray absorption analysis system",
    "description": "use wikidata scientificInstruments (wd:Q3099911). In the future use wd:Q1584378 (measuring eq1upment because instrument likely includes various parts that are not strictly measureing instruments.   Wikidata measuringSystem (wd:Q1372376) might be an alternative.",
    "schema:hasPart": [
        {
            "@type": [
                "schema:Thing",
                "schema:Product"
            ],
            "schema:additionalType": ["nxs:BaseClass/NXsource","wd:Q3099911"],
            "schema:name": "source of x-ray excitation for analysis. Made up for this example",
            "schema:identifier": "should have a registry with URIs",
            "schema:additionalProperty": [
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": ["nxs:Field/NXsource/type"],
                    "schema:name":"X-ray source",
                    "schema:value": "Synchrotron X-ray Source"
                },
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": ["nxs:Field/NXsource/probe"],
                    "schema:name": "Probe",
                    "schema:value": "x-ray"
                }
            ]
        },
        {
            "@type": [
                "schema:Thing",
                "schema:Product"
            ],
            "schema:additionalType": ["xas:Beamline","wd:Q3099911"],
            "schema:name": "13-BM-D",
            "schema:identifier": "should have a registry with URIs",
            "schema:additionalProperty": [
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": ["xas:collimation"],
                    "schema:name": "collimation technique",
                    "schema:value": "none"
                },
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": ["xas:focusing"],
                    "schema:name": "focusing",
                    "schema:value": "???"
                },
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": ["xas:harmonic_rejection"],
                    "schema:name": "harmonic_rejection",
                    "schema:value": "Rh-coated mirror, detuned"
                }
            ]
        },
        {
            "@type": [
                "schema:Thing",
                "schema:Product"
            ],
            "schema:additionalType": ["nxs:BaseClass/NXmonochromator","wd:Q3099911"],
            "schema:name": "Si 111",
            "schema:additionalProperty": [
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": ["nxs:Field/NXcrystal/d_spacing"],
                    "schema:name": "d-spacing",
                    "schema:value": "3.13550",
                    "schema:unitText": "Angstrom"
                },
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": ["nxs:Field/NXcrystal/chemical_formula"],
                    "schema:name": "chemical formula",
                    "schema:value": "Si"
                },
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": ["nxs:Field/NXcrystal/type"],
                    "schema:name": "crystal type",
                    "schema:value": "channel-cut"
                },
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": ["nxs:Field/NXcrystal/reflection"],
                    "schema:name": "reflection plane (hkl)",
                    "schema:value": "1,1,1"
                }
            ]
        },
        {
            "@type": [
                "schema:Thing",
                "schema:Product"
            ],
            "schema:additionalType": "nxs:BaseClass/NXmonitor",
            "schema:additionalProperty": [
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": "nxs:Field/NXmonitor/mode",
                    "schema:name": "monitor mode",
                    "schema:value": "monitor"
                },
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": "nxs:Field/NXmonitor/preset",
                    "schema:name": "monitor preset",
                    "schema:value": "N.A."
                },
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": "xas:detector.i0",
                    "schema:name": "detector mode i0",
                    "schema:alternateName": "incident flux measurement method",
                    "schema:value": "10cm  N2"
                },
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": "xas:detector.it",
                    "schema:name": "detector mode it",
                    "schema:alternateName": "transmitted flux measurement method",
                    "schema:value": "10cm  N2"
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
      "xas": "https://xas.org/dictionary/",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "wd": "https://www.wikidata.org/entity/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasInstrument/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "xas": "https://xas.org/dictionary/",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "prov": "http://www.w3.org/ns/prov#",
      "wd": "https://www.wikidata.org/entity/"
    }
  ],
  "@id": "xas:487y54",
  "@type": [
    "schema:Thing",
    "schema:Product"
  ],
  "schema:additionalType": [
    "wd:Q3099911"
  ],
  "schema:name": "x-ray absorption analysis system",
  "description": "use wikidata scientificInstruments (wd:Q3099911). In the future use wd:Q1584378 (measuring eq1upment because instrument likely includes various parts that are not strictly measureing instruments.   Wikidata measuringSystem (wd:Q1372376) might be an alternative.",
  "schema:hasPart": [
    {
      "@type": [
        "schema:Thing",
        "schema:Product"
      ],
      "schema:additionalType": [
        "nxs:BaseClass/NXsource",
        "wd:Q3099911"
      ],
      "schema:name": "source of x-ray excitation for analysis. Made up for this example",
      "schema:identifier": "should have a registry with URIs",
      "schema:additionalProperty": [
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "nxs:Field/NXsource/type"
          ],
          "schema:name": "X-ray source",
          "schema:value": "Synchrotron X-ray Source"
        },
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "nxs:Field/NXsource/probe"
          ],
          "schema:name": "Probe",
          "schema:value": "x-ray"
        }
      ]
    },
    {
      "@type": [
        "schema:Thing",
        "schema:Product"
      ],
      "schema:additionalType": [
        "xas:Beamline",
        "wd:Q3099911"
      ],
      "schema:name": "13-BM-D",
      "schema:identifier": "should have a registry with URIs",
      "schema:additionalProperty": [
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "xas:collimation"
          ],
          "schema:name": "collimation technique",
          "schema:value": "none"
        },
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "xas:focusing"
          ],
          "schema:name": "focusing",
          "schema:value": "???"
        },
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "xas:harmonic_rejection"
          ],
          "schema:name": "harmonic_rejection",
          "schema:value": "Rh-coated mirror, detuned"
        }
      ]
    },
    {
      "@type": [
        "schema:Thing",
        "schema:Product"
      ],
      "schema:additionalType": [
        "nxs:BaseClass/NXmonochromator",
        "wd:Q3099911"
      ],
      "schema:name": "Si 111",
      "schema:additionalProperty": [
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "nxs:Field/NXcrystal/d_spacing"
          ],
          "schema:name": "d-spacing",
          "schema:value": "3.13550",
          "schema:unitText": "Angstrom"
        },
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "nxs:Field/NXcrystal/chemical_formula"
          ],
          "schema:name": "chemical formula",
          "schema:value": "Si"
        },
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "nxs:Field/NXcrystal/type"
          ],
          "schema:name": "crystal type",
          "schema:value": "channel-cut"
        },
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "nxs:Field/NXcrystal/reflection"
          ],
          "schema:name": "reflection plane (hkl)",
          "schema:value": "1,1,1"
        }
      ]
    },
    {
      "@type": [
        "schema:Thing",
        "schema:Product"
      ],
      "schema:additionalType": "nxs:BaseClass/NXmonitor",
      "schema:additionalProperty": [
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": "nxs:Field/NXmonitor/mode",
          "schema:name": "monitor mode",
          "schema:value": "monitor"
        },
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": "nxs:Field/NXmonitor/preset",
          "schema:name": "monitor preset",
          "schema:value": "N.A."
        },
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": "xas:detector.i0",
          "schema:name": "detector mode i0",
          "schema:alternateName": "incident flux measurement method",
          "schema:value": "10cm  N2"
        },
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": "xas:detector.it",
          "schema:name": "detector mode it",
          "schema:alternateName": "transmitted flux measurement method",
          "schema:value": "10cm  N2"
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .
@prefix xas: <https://xas.org/dictionary/> .

xas:487y54 a schema1:Product,
        schema1:Thing ;
    schema1:additionalType "wd:Q3099911" ;
    schema1:hasPart [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty [ a schema1:PropertyValue ;
                    schema1:name "d-spacing" ;
                    schema1:propertyID "nxs:Field/NXcrystal/d_spacing" ;
                    schema1:unitText "Angstrom" ;
                    schema1:value "3.13550" ],
                [ a schema1:PropertyValue ;
                    schema1:name "chemical formula" ;
                    schema1:propertyID "nxs:Field/NXcrystal/chemical_formula" ;
                    schema1:value "Si" ],
                [ a schema1:PropertyValue ;
                    schema1:name "crystal type" ;
                    schema1:propertyID "nxs:Field/NXcrystal/type" ;
                    schema1:value "channel-cut" ],
                [ a schema1:PropertyValue ;
                    schema1:name "reflection plane (hkl)" ;
                    schema1:propertyID "nxs:Field/NXcrystal/reflection" ;
                    schema1:value "1,1,1" ] ;
            schema1:additionalType "nxs:BaseClass/NXmonochromator",
                "wd:Q3099911" ;
            schema1:name "Si 111" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty [ a schema1:PropertyValue ;
                    schema1:name "Probe" ;
                    schema1:propertyID "nxs:Field/NXsource/probe" ;
                    schema1:value "x-ray" ],
                [ a schema1:PropertyValue ;
                    schema1:name "X-ray source" ;
                    schema1:propertyID "nxs:Field/NXsource/type" ;
                    schema1:value "Synchrotron X-ray Source" ] ;
            schema1:additionalType "nxs:BaseClass/NXsource",
                "wd:Q3099911" ;
            schema1:identifier "should have a registry with URIs" ;
            schema1:name "source of x-ray excitation for analysis. Made up for this example" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty [ a schema1:PropertyValue ;
                    schema1:name "harmonic_rejection" ;
                    schema1:propertyID "xas:harmonic_rejection" ;
                    schema1:value "Rh-coated mirror, detuned" ],
                [ a schema1:PropertyValue ;
                    schema1:name "focusing" ;
                    schema1:propertyID "xas:focusing" ;
                    schema1:value "???" ],
                [ a schema1:PropertyValue ;
                    schema1:name "collimation technique" ;
                    schema1:propertyID "xas:collimation" ;
                    schema1:value "none" ] ;
            schema1:additionalType "wd:Q3099911",
                "xas:Beamline" ;
            schema1:identifier "should have a registry with URIs" ;
            schema1:name "13-BM-D" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty [ a schema1:PropertyValue ;
                    schema1:alternateName "transmitted flux measurement method" ;
                    schema1:name "detector mode it" ;
                    schema1:propertyID "xas:detector.it" ;
                    schema1:value "10cm  N2" ],
                [ a schema1:PropertyValue ;
                    schema1:alternateName "incident flux measurement method" ;
                    schema1:name "detector mode i0" ;
                    schema1:propertyID "xas:detector.i0" ;
                    schema1:value "10cm  N2" ],
                [ a schema1:PropertyValue ;
                    schema1:name "monitor preset" ;
                    schema1:propertyID "nxs:Field/NXmonitor/preset" ;
                    schema1:value "N.A." ],
                [ a schema1:PropertyValue ;
                    schema1:name "monitor mode" ;
                    schema1:propertyID "nxs:Field/NXmonitor/mode" ;
                    schema1:value "monitor" ] ;
            schema1:additionalType "nxs:BaseClass/NXmonitor" ] ;
    schema1:name "x-ray absorption analysis system" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: definitions for roles used in XAS profile
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    minItems: 2
    uniqueItems: true
    description: Product and Thing are dummy place holders to get schema.org properties
      to validate
    allOf:
    - contains:
        const: schema:Product
      minContains: 1
    - contains:
        const: schema:Thing
      minContains: 1
  schema:additionalType:
    type: array
    items:
      type: string
    minItems: 1
    uniqueItems: true
    allOf:
    - contains:
        const: wd:Q3099911
      description: '3099911 is ''scientific instrument'', use this a flag for instruments.
        Have to declare prefix wd: https://www.wikidata.org/entity/'
      minContains: 1
  schema:name:
    type: string
  schema:identifier:
    anyOf:
    - type: string
    - $ref: '#/$defs/Identifier'
  schema:description:
    type: string
  schema:additionalProperty:
    type: array
    description: AdditionalProperty propertyID will depend on the kind of instrument;
      validation in that detail is a future project
    items:
      $ref: '#/$defs/AdditionalProperty'
  schema:hasPart:
    type: array
    description: Sub-components of the instrument system
    items:
      anyOf:
      - $ref: '#/$defs/Instrument'
      - type: object
        properties:
          '@id':
            type: string
required:
- '@type'
- schema:additionalType
- schema:name
$defs:
  Identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
  AdditionalProperty:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
  Instrument:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasInstrument/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasInstrument/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasInstrument/context.jsonld)

## Sources

* [schema.org](https://schema.org/Thing)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/xasProperties/xasInstrument`

