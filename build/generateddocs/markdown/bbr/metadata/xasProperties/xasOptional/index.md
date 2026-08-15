
# Optional Fields for XAS data (Schema)

`cdif.bbr.metadata.xasProperties.xasOptional` *v1.0*

Genuinely-optional XAS fields layered on cdifCore (no requirements). Permits and documents optional XAS content: schema:variableMeasured XAS data-array InstanceVariables, plus the optional beamline-operational and sample physico-chemical additionalProperty vocabularies (see description.md). Defines properties: schema:variableMeasured. Uses building blocks: cdifInstanceVariable (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Stable

## Description

## Optional XAS metadata fields

Genuinely-optional X-ray absorption spectroscopy (XAS) properties layered on `cdifCore`.
This module adds **no requirements** — it documents and permits optional XAS content that
appears only when the corresponding measurements exist. It is composed once by the `xasDocument`
profile alongside the required-constraints module `xasCore`.

### 1. Data-array variables (`schema:variableMeasured`)

Optional `cdi:InstanceVariable` / `schema:PropertyValue` items describing the columns of an
XDI data array. Enforced by this schema when present (as `schema:variableMeasured` items):

`energy`, `i0`, `itrans`, `ifluor`, `irefer`, `mutrans`, `mufluor`, `murefer`,
`normtrans`, `normfluor`, `normrefer`, `chi`, `chi_re`, `chi_im`, `chi_mag`, `chi_pha`,
`k`, `r`, `angle`.

### 2. Beamline-operational parameters (`schema:additionalProperty` on the `xas:Beamline` entity)

Optional `schema:PropertyValue` entries carried on the beamline entity nested inside
`prov:wasGeneratedBy → prov:used[schema:instrument … xas:Beamline]`. Permitted `schema:propertyID`
values (open-world — other propertyIDs are also allowed):

`xas:flux`, `xas:spot_size`, `xas:website`, `xas:energy_range`, `xas:energy_resolution`,
`xas:scan_mode`.

### 3. Sample physico-chemical parameters (`schema:additionalProperty` on the `schema:object` sample)

Optional `schema:PropertyValue` entries carried on the material sample
(`prov:wasGeneratedBy → schema:object`, an `xasSample`). Permitted `schema:propertyID` values
(open-world):

`xas:temperature`, `xas:pressure`, `xas:ph`, `xas:eh`, `xas:concentration`, `xas:density`,
`xas:viscosity`, `xas:porosity`, `xas:opacity`, `xas:resistivity`, `xas:magnetic_field`,
`xas:magnetic_moment`, `xas:electric_field`, `xas:electrochemical_potential`, `xas:volume`.

> Groups 2 and 3 are documented here rather than constrained in the schema: CDIF is open-world,
> so these optional `additionalProperty` entries are already permitted, and a hard schema
> constraint on their `propertyID` would either be a no-op or wrongly reject other valid
> additional properties. The vocabularies above are the recommended XAS `propertyID`s.

## Examples

### Example XAS optional metadata with beamline instrument, measurement technique, and sample.
XAS dataset with NXsource and NXmonochromator instrument components, XAS measurement technique keywords, and sample description.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "time": "http://www.w3.org/2006/time#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://w3id.org/cdif/xas/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "prov": "http://www.w3.org/ns/prov#",
    "csvw": "http://www.w3.org/ns/csvw#",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "xas:exampleOptionalFields",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:variableMeasured": [
    {
      "@id": "xas:monochromatorenergy",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:name": "energy",
      "schema:alternateName": [
        "Monochromator energy"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
      "schema:propertyID": [
        {
          "@id": "xas:monochromatorenergy"
        }
      ],
      "schema:unitText": "eV",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:simpleUnitOfMeasure": "eV",
      "cdi:uses": "xas:monochromatorenergy",
      "cdi:name": "energy",
      "cdi:displayLabel": "monochromator energy"
    },
    {
      "@id": "xas:incidentintensity",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:name": "i0 monitory intensity",
      "schema:alternateName": [
        "Monitor intensity"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description)",
      "schema:propertyID": [
        {
          "@id": "xas:incidentintensity"
        }
      ],
      "schema:unitText": "counts",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:uses": "xas:incidentintensity",
      "cdi:name": "i0",
      "cdi:displayLabel": "monitor intensity"
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
      "prov": "http://www.w3.org/ns/prov#",
      "nxs": "https://manual.nexusformat.org/classes/",
      "xas": "https://w3id.org/cdif/xas/",
      "dcat": "http://www.w3.org/ns/dcat#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasOptional/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "spdx": "http://spdx.org/rdf/terms#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "time": "http://www.w3.org/2006/time#",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "xas": "https://w3id.org/cdif/xas/",
      "nxs": "https://manual.nexusformat.org/classes/",
      "prov": "http://www.w3.org/ns/prov#",
      "csvw": "http://www.w3.org/ns/csvw#",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "xas:exampleOptionalFields",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:variableMeasured": [
    {
      "@id": "xas:monochromatorenergy",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:name": "energy",
      "schema:alternateName": [
        "Monochromator energy"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
      "schema:propertyID": [
        {
          "@id": "xas:monochromatorenergy"
        }
      ],
      "schema:unitText": "eV",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:simpleUnitOfMeasure": "eV",
      "cdi:uses": "xas:monochromatorenergy",
      "cdi:name": "energy",
      "cdi:displayLabel": "monochromator energy"
    },
    {
      "@id": "xas:incidentintensity",
      "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
      ],
      "schema:name": "i0 monitory intensity",
      "schema:alternateName": [
        "Monitor intensity"
      ],
      "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description)",
      "schema:propertyID": [
        {
          "@id": "xas:incidentintensity"
        }
      ],
      "schema:unitText": "counts",
      "cdi:identifier": "should be URI from nexusFormat organization",
      "cdi:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:uses": "xas:incidentintensity",
      "cdi:name": "i0",
      "cdi:displayLabel": "monitor intensity"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .
@prefix xas: <https://w3id.org/cdif/xas/> .

xas:exampleOptionalFields a schema1:Dataset,
        schema1:Product ;
    schema1:variableMeasured xas:incidentintensity,
        xas:monochromatorenergy .

xas:incidentintensity a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "monitor intensity" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "i0" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:uses "xas:incidentintensity" ;
    schema1:alternateName "Monitor intensity" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description)" ;
    schema1:name "i0 monitory intensity" ;
    schema1:propertyID xas:incidentintensity ;
    schema1:unitText "counts" .

xas:monochromatorenergy a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "monochromator energy" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "energy" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:simpleUnitOfMeasure "eV" ;
    cdi:uses "xas:monochromatorenergy" ;
    schema1:alternateName "Monochromator energy" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description" ;
    schema1:name "energy" ;
    schema1:propertyID xas:monochromatorenergy ;
    schema1:unitText "eV" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Optional XAS metadata fields
description: 'Genuinely-optional XAS properties layered on cdifCore. Adds NO requirements.
  Documents and permits optional XAS content: (a) XAS data-array variables as schema:variableMeasured
  cdi:InstanceVariable items, and (b) optional beamline-operational and sample physico-chemical
  parameters carried as schema:additionalProperty entries (on the prov:used xas:beamline
  entity and the schema:object sample respectively; see description.md for the propertyID
  vocabularies). Present only when the corresponding measurements exist.'
type: object
properties:
  '@context':
    type: object
    description: JSON-LD prefixes used by optional XAS fields.
    properties:
      xas:
        const: https://w3id.org/cdif/xas/
      nxs:
        const: https://manual.nexusformat.org/classes/
  schema:variableMeasured:
    description: Optional XAS data-array variables (energy, i0, itrans, ifluor, irefer,
      mutrans, mufluor, murefer, normtrans, normfluor, normrefer, chi, chi_re, chi_im,
      chi_mag, chi_pha, k, r, angle), each a cdi:InstanceVariable / schema:PropertyValue.
      Not required. The XDI variable propertyID enum is layered on in xasCore; this
      profile only enforces the base cdifInstanceVariable shape.
    type: array
    items:
      $ref: '#/$defs/InstanceVariable'
    x-jsonld-id: http://schema.org/variableMeasured
  prov:wasGeneratedBy:
    type: array
    description: Optional-vocabulary layer on the XAS analysis activity. Adds propertyID
      enums for (a) activity-level additionalProperty entries, (b) the sample (schema:object)
      additionalProperty entries, and (c) the beamline peer instrument's additionalProperty
      entries. Enum arms are additive over the base propertyID_item shape.
    items:
      properties:
        schema:additionalProperty:
          description: XAS activity-level additionalProperty vocabulary. All entries
            resolve to SKOS concepts in the XAS-CDIF glossary.
          type: array
          items:
            allOf:
            - $ref: '#/$defs/AdditionalProperty'
            - properties:
                schema:propertyID:
                  type: array
                  minItems: 1
                  items:
                    anyOf:
                    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml#/$defs/propertyID_item
                    - enum:
                      - xas:edgeenergy
                      - xas:calibrationmethod
                      - xas:experimentdocumentation
                      - xas:installedoptions
                  x-jsonld-id: http://schema.org/propertyID
          x-jsonld-id: http://schema.org/additionalProperty
        schema:object:
          description: Sample additionalProperty entries. XDI Sample.* vocabulary
            (XDI-CDIF-Mapping.xlsx rows 47-64) plus legacy xas:* names and NEXUS NXsample
            fields.
          properties:
            schema:additionalProperty:
              type: array
              items:
                allOf:
                - $ref: '#/$defs/AdditionalProperty'
                - properties:
                    schema:propertyID:
                      type: array
                      minItems: 1
                      items:
                        anyOf:
                        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml#/$defs/propertyID_item
                        - enum:
                          - xas:concentration
                          - xas:samplecrystalstructure
                          - xas:density
                          - xas:eh
                          - xas:electricfield
                          - xas:electrochemicalpotential
                          - xas:magneticfield
                          - xas:magneticmoment
                          - xas:opacity
                          - xas:parentsample
                          - xas:ph
                          - xas:porosity
                          - xas:pressure
                          - xas:resistivity
                          - xas:samplechemicalcomposition
                          - xas:samplematerial
                          - xas:samplepreparation
                          - xas:temperature
                          - xas:viscosity
                          - xas:volume
                          - nxs:Field/NXsample/mass
                          - nxs:Field/NXsample/point_group
                          - nxs:Field/NXsample/unit_cell
                      x-jsonld-id: http://schema.org/propertyID
              x-jsonld-id: http://schema.org/additionalProperty
          x-jsonld-id: http://schema.org/object
        prov:used:
          type: array
          items:
            if:
              description: When this peer prov:used entry's instrument is a beamline
                (schema:additionalType contains xas:beamline), its schema:additionalProperty
                entries SHOULD use the XDI Beamline vocabulary (XDI-CDIF-Mapping.xlsx
                rows 10-20, excluding Beamline.name which maps to schema:name).
              properties:
                schema:instrument:
                  type: array
                  contains:
                    type: object
                    properties:
                      schema:additionalType:
                        anyOf:
                        - type: object
                          additionalProperties: false
                          required:
                          - '@id'
                          properties:
                            '@id':
                              const: xas:beamline
                        - type: array
                          contains:
                            type: object
                            additionalProperties: false
                            required:
                            - '@id'
                            properties:
                              '@id':
                                const: xas:beamline
            then:
              properties:
                schema:instrument:
                  type: array
                  contains:
                    type: object
                    properties:
                      schema:additionalProperty:
                        type: array
                        items:
                          allOf:
                          - $ref: '#/$defs/AdditionalProperty'
                          - properties:
                              schema:propertyID:
                                type: array
                                minItems: 1
                                items:
                                  anyOf:
                                  - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml#/$defs/propertyID_item
                                  - enum:
                                    - xas:collimation
                                    - xas:detectortype
                                    - xas:energyrange
                                    - xas:energyresolution
                                    - xas:flux
                                    - xas:focusing
                                    - xas:harmonicrejection
                                    - xas:scanmode
                                    - xas:spotsize
                                    - xas:website
                                x-jsonld-id: http://schema.org/propertyID
                        x-jsonld-id: http://schema.org/additionalProperty
                  x-jsonld-id: http://schema.org/instrument
          x-jsonld-id: http://www.w3.org/ns/prov#used
    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
$defs:
  InstanceVariable:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/schema.yaml
  AdditionalProperty:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  dcat: http://www.w3.org/ns/dcat#
  dcterms: http://purl.org/dc/terms/
  nxs: https://manual.nexusformat.org/classes/
  prov: http://www.w3.org/ns/prov#
  spdx: http://spdx.org/rdf/terms#
  xas: https://w3id.org/cdif/xas/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasOptional/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasOptional/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdif": "https://w3id.org/cdif/",
    "schema": "http://schema.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "cdif:xas/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "prov": "http://www.w3.org/ns/prov#",
    "dcat": "http://www.w3.org/ns/dcat#",
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasOptional/context.jsonld)

## Sources

* [CDIF-4-XAS OSCARS Project](https://doi.org/10.5281/zenodo.17421917)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/xasProperties/xasOptional`

