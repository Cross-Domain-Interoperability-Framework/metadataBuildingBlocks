
# Material Sample for x-ray absorption study (Schema)

`cdif.bbr.metadata.xasProperties.xasSample` *v1.0*

Schema defining properties for documenting a material sample that is the schema:object (target) of an XAS analysis (replacing the deprecated schema:mainEntity, per the Ocean Info Hub recommendation). Defines properties: @type, schema:additionalType, schema:name, schema:identifier, schema:description, schema:additionalProperty. Uses building blocks: identifier (schemaorgProperties), additionalProperty (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Stable

## Description

## Material sample properties

Defines a set of properties for describing a material sample that is the `schema:object` (target) of an X-ray absorption spectroscopy (XAS) analysis, for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) XAS profile. The sample is typed `schema:Thing` + `schema:Product` with `schema:additionalType` including `MaterialSample` and the iSample material-sample-object-type URI.
## Examples

### Example X-ray absorption sample description.
Example sample documentation, for use in XAS profile, use as value for schema:MainEntity
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "xas": "https://w3id.org/cdif/xas/",
    "nxs": "https://manual.nexusformat.org/classes/"
  },
  "@id": "ex:exampleSampel_357h",
  "@type": [
    "schema:Thing",
    "schema:Product"
  ],
  "schema:additionalType": [
    "MaterialSample",
    {
      "@id": "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
    },
    {
      "@id": "https://www.wikidata.org/wiki/Q485146"
    }
  ],
  "schema:name": "Na2SeO4",
  "schema:identifier": "igsn:10.6620/357lkj",
  "schema:description": "physical properties of sample: ph, eh, volume, porosity, density, concentration, resistivity, viscosity, crystal structure, opacity from xdi list...",
  "schema:additionalProperty": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:porosity"
        }
      ],
      "schema:name": "porosity",
      "schema:value": "27",
      "schema:unitText": "percent"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:samplechemicalcomposition"
        }
      ],
      "schema:name": "stoichiometry",
      "schema:value": "Na2SeO4"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:samplepreparation"
        }
      ],
      "schema:name": "samplePreparation",
      "schema:value": "powder on tape, 6 layers"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:samplemass"
        }
      ],
      "schema:value": "10",
      "schema:name": "sample mass",
      "schema:unitText": "mg"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:pointgroup"
        }
      ],
      "schema:name": "crystal point group",
      "schema:value": "mm2"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:sampleunitcell"
        }
      ],
      "schema:name": "crystal unit cell",
      "schema:value": "cubic; Z = 4; a = 5.46; V = 162.77"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:parentsample"
        }
      ],
      "schema:name": "Parent sample",
      "schema:value": "igsn:10.3476/342573"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:samplematerial"
        }
      ],
      "schema:name": "sample material state",
      "schema:value": "solid metal foil"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "xas": "https://w3id.org/cdif/xas/",
      "nxs": "https://manual.nexusformat.org/classes/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasSample/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "xas": "https://w3id.org/cdif/xas/",
      "nxs": "https://manual.nexusformat.org/classes/"
    }
  ],
  "@id": "ex:exampleSampel_357h",
  "@type": [
    "schema:Thing",
    "schema:Product"
  ],
  "schema:additionalType": [
    "MaterialSample",
    {
      "@id": "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
    },
    {
      "@id": "https://www.wikidata.org/wiki/Q485146"
    }
  ],
  "schema:name": "Na2SeO4",
  "schema:identifier": "igsn:10.6620/357lkj",
  "schema:description": "physical properties of sample: ph, eh, volume, porosity, density, concentration, resistivity, viscosity, crystal structure, opacity from xdi list...",
  "schema:additionalProperty": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:porosity"
        }
      ],
      "schema:name": "porosity",
      "schema:value": "27",
      "schema:unitText": "percent"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:samplechemicalcomposition"
        }
      ],
      "schema:name": "stoichiometry",
      "schema:value": "Na2SeO4"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:samplepreparation"
        }
      ],
      "schema:name": "samplePreparation",
      "schema:value": "powder on tape, 6 layers"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:samplemass"
        }
      ],
      "schema:value": "10",
      "schema:name": "sample mass",
      "schema:unitText": "mg"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:pointgroup"
        }
      ],
      "schema:name": "crystal point group",
      "schema:value": "mm2"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:sampleunitcell"
        }
      ],
      "schema:name": "crystal unit cell",
      "schema:value": "cubic; Z = 4; a = 5.46; V = 162.77"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:parentsample"
        }
      ],
      "schema:name": "Parent sample",
      "schema:value": "igsn:10.3476/342573"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "xas:samplematerial"
        }
      ],
      "schema:name": "sample material state",
      "schema:value": "solid metal foil"
    }
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xas: <https://w3id.org/cdif/xas/> .

ex:exampleSampel_357h a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Parent sample" ;
            schema1:propertyID xas:parentsample ;
            schema1:value "igsn:10.3476/342573" ],
        [ a schema1:PropertyValue ;
            schema1:name "sample mass" ;
            schema1:propertyID xas:samplemass ;
            schema1:unitText "mg" ;
            schema1:value "10" ],
        [ a schema1:PropertyValue ;
            schema1:name "crystal point group" ;
            schema1:propertyID xas:pointgroup ;
            schema1:value "mm2" ],
        [ a schema1:PropertyValue ;
            schema1:name "sample material state" ;
            schema1:propertyID xas:samplematerial ;
            schema1:value "solid metal foil" ],
        [ a schema1:PropertyValue ;
            schema1:name "porosity" ;
            schema1:propertyID xas:porosity ;
            schema1:unitText "percent" ;
            schema1:value "27" ],
        [ a schema1:PropertyValue ;
            schema1:name "samplePreparation" ;
            schema1:propertyID xas:samplepreparation ;
            schema1:value "powder on tape, 6 layers" ],
        [ a schema1:PropertyValue ;
            schema1:name "stoichiometry" ;
            schema1:propertyID xas:samplechemicalcomposition ;
            schema1:value "Na2SeO4" ],
        [ a schema1:PropertyValue ;
            schema1:name "crystal unit cell" ;
            schema1:propertyID xas:sampleunitcell ;
            schema1:value "cubic; Z = 4; a = 5.46; V = 162.77" ] ;
    schema1:additionalType <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample>,
        <https://www.wikidata.org/wiki/Q485146>,
        "MaterialSample" ;
    schema1:description "physical properties of sample: ph, eh, volume, porosity, density, concentration, resistivity, viscosity, crystal structure, opacity from xdi list..." ;
    schema1:identifier "igsn:10.6620/357lkj" ;
    schema1:name "Na2SeO4" .


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
      anyOf:
      - type: string
      - type: object
        additionalProperties: false
        required:
        - '@id'
        properties:
          '@id':
            type: string
    minItems: 2
    uniqueItems: true
    allOf:
    - contains:
        const: MaterialSample
      minContains: 1
    - contains:
        type: object
        additionalProperties: false
        required:
        - '@id'
        properties:
          '@id':
            const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
      minContains: 1
    x-jsonld-id: http://schema.org/additionalType
  schema:name:
    type: string
    x-jsonld-id: http://schema.org/name
  schema:identifier:
    anyOf:
    - type: string
    - $ref: '#/$defs/Identifier'
    x-jsonld-id: http://schema.org/identifier
  schema:description:
    type: string
    x-jsonld-id: http://schema.org/description
  schema:additionalProperty:
    type: array
    description: Sample additionalProperty entries (base AdditionalProperty shape).
      The XDI Sample.* propertyID vocabulary enum is layered on in xasOptional, so
      it applies at the profile level, not this shape.
    items:
      $ref: '#/$defs/AdditionalProperty'
    x-jsonld-id: http://schema.org/additionalProperty
required:
- '@type'
- schema:additionalType
- schema:name
$defs:
  Identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
  AdditionalProperty:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  nxs: https://manual.nexusformat.org/classes/
  xas: https://w3id.org/cdif/xas/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasSample/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasSample/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "xas": "https://w3id.org/cdif/xas/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasSample/context.jsonld)

## Sources

* [schema.org](https://schema.org/object)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/xasProperties/xasSample`

