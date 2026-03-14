
# Optional Fields for XAS data (Schema)

`cdif.bbr.metadata.xasProperties.xasOptional` *v0.1*

Optional XAS metadata extending CDIF mandatory with cdifProvActivity-based provenance. Includes XAS subject descriptors, instrument wrappers, XDI-conformant distribution, measurement technique DefinedTerms, and element/edge keywords. Defines properties: schema:subjectOf, prov:wasGeneratedBy, schema:distribution, schema:measurementTechnique, schema:keywords. Uses building blocks: cdifMandatory (cdifProperties), cdifProvActivity (cdifProperties), definedTerm (schemaorgProperties), additionalProperty (schemaorgProperties), dataDownload (schemaorgProperties), xasSample (xasProperties), xasSubject (xasProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Optional Fields for XAS data

Extends CDIF mandatory metadata with optional XAS-specific properties. Composes cdifMandatory with cdifProvActivity-based provenance (via xasGeneratedBy pattern), XAS subject descriptors, data distribution with XDI conformance, measurement technique DefinedTerms, and element/edge keywords.

### Key properties

- **schema:subjectOf** — XAS subject descriptors (element, edge)
- **prov:wasGeneratedBy** — cdifProvActivity activity extended with XAS instrument wrappers (source, monochromator with d-spacing/reflection), sample object, and facility
- **schema:distribution** — data download with XDI specification conformance
- **schema:measurementTechnique** — DefinedTerms for XAS technique and measurement mode
- **schema:keywords** — DefinedTerms for absorption edge (XDI dictionary) and target element (SWEET ontology)

## Examples

### Example XAS metadata conforms to extension.
Import base schema.org SubjectOf, add requiremnet that dcterms:conformsTo has XAS profile URI.
## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: '#/$defs/CdifMandatory'
- type: object
  properties:
    schema:subjectOf:
      $ref: '#/$defs/XasSubject'
    prov:wasGeneratedBy:
      type: array
      items:
        allOf:
        - $ref: '#/$defs/CdifProvActivity'
        - type: object
          properties:
            prov:used:
              type: array
              description: Array of used entities. Must contain an instrument wrapper
                with schema:hasPart sub-components. The x-ray source type and probe,
                and monochromator properties type, d-spacing and reflection plane
                are required.
              contains:
                type: object
                required:
                - schema:instrument
                properties:
                  schema:instrument:
                    type: object
                    properties:
                      schema:hasPart:
                        type: array
                        minItems: 2
                        allOf:
                        - contains:
                            type: object
                            properties:
                              '@type':
                                type: array
                                items:
                                  type: string
                                minItems: 2
                                allOf:
                                - contains:
                                    const: schema:Thing
                                - contains:
                                    const: schema:Product
                              schema:additionalType:
                                const: nxs:BaseClass/NXsource
                              schema:additionalProperty:
                                type: array
                                minItems: 2
                                items:
                                  $ref: '#/$defs/AdditionalProperty'
                                allOf:
                                - contains:
                                    type: object
                                    properties:
                                      schema:propertyID:
                                        type: array
                                        contains:
                                          const: nxs:Field/NXsource/type
                                      schema:value:
                                        type: string
                                    required:
                                    - schema:propertyID
                                    - schema:value
                                - contains:
                                    type: object
                                    properties:
                                      schema:propertyID:
                                        type: array
                                        contains:
                                          const: nxs:Field/NXsource/probe
                                      schema:name:
                                        const: Probe
                                      schema:value:
                                        type: string
                                    required:
                                    - schema:name
                                    - schema:propertyID
                                    - schema:value
                            required:
                            - '@type'
                            - schema:additionalType
                            - schema:additionalProperty
                        - contains:
                            type: object
                            properties:
                              '@type':
                                type: array
                                items:
                                  type: string
                                minItems: 2
                                allOf:
                                - contains:
                                    const: schema:Thing
                                - contains:
                                    const: schema:Product
                              schema:additionalType:
                                const: nxs:BaseClass/NXmonochromator
                              schema:name:
                                type: string
                              schema:additionalProperty:
                                description: Require additional properties for monochromator,
                                  requires d-space, crystal type, reflection plane.
                                type: array
                                minItems: 3
                                items:
                                  $ref: '#/$defs/AdditionalProperty'
                                contains:
                                  type: object
                                  properties:
                                    schema:propertyID:
                                      type: array
                                      contains:
                                        const: nxs:Field/NXcrystal/type
                                    schema:value:
                                      type: string
                                  required:
                                  - schema:value
                                  - schema:propertyID
                                allOf:
                                - contains:
                                    type: object
                                    properties:
                                      schema:propertyID:
                                        type: array
                                        contains:
                                          const: nxs:Field/NXcrystal/d_spacing
                                      schema:value:
                                        type: string
                                      schema:unitText:
                                        type: string
                                    required:
                                    - schema:propertyID
                                    - schema:value
                                    - schema:unitText
                                - contains:
                                    type: object
                                    properties:
                                      schema:propertyID:
                                        type: array
                                        contains:
                                          const: nxs:Field/NXcrystal/reflection
                                      schema:value:
                                        type: string
                                    required:
                                    - schema:value
                                    - schema:propertyID
                            required:
                            - '@type'
                            - schema:additionalType
                            - schema:additionalProperty
                    required:
                    - schema:hasPart
            schema:object:
              $ref: '#/$defs/XasSample'
    schema:distribution:
      type: array
      items:
        $ref: '#/$defs/DataDownload'
      contains:
        type: object
        properties:
          '@type':
            type: array
            items:
              type: string
            minItems: 2
            allOf:
            - contains:
                const: schema:DataDownload
            - contains:
                const: cdi:PhysicalDataset
          dcterms:conformsTo:
            type: array
            contains:
              type: object
              properties:
                '@id':
                  const: https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md
              required:
              - '@id'
        required:
        - '@type'
        - dcterms:conformsTo
    schema:measurementTechnique:
      type: array
      description: 'Require DefinedTerms for both: absorption edge (XDI dict) and
        target element (SWEET).'
      minItems: 2
      items:
        $ref: '#/$defs/DefinedTerm'
      allOf:
      - contains:
          type: object
          properties:
            schema:name:
              const: X-Ray Absorption Spectroscopy
            schema:termCode:
              const: XAS
            schema:identifier:
              const: http://purl.org/pan-science/PaNET/PaNET01196
            schema:inDefinedTermSet:
              const: http://purl.org/pan-science/PaNET/PaNET.owl
          required:
          - schema:name
          - schema:termCode
          - schema:identifier
          - schema:inDefinedTermSet
      - contains:
          type: object
          properties:
            schema:name:
              type: string
            schema:inDefinedTermSet:
              const: nxs:Field/NXxas/ENTRY/DATA/mode
          required:
          - schema:name
          - schema:inDefinedTermSet
    schema:keywords:
      type: array
      description: extends base CDIF keyword schema to require defined terms for the
        absorption edge and the target element for the analysis
      minItems: 2
      items:
        type: object
        properties:
          '@type':
            anyOf:
            - type: string
              const: schema:DefinedTerm
            - type: array
              items:
                type: string
              contains:
                const: schema:DefinedTerm
          schema:name:
            type: string
          schema:identifier:
            type: string
          schema:inDefinedTermSet:
            type: string
            description: need to include this to tag what the keyword is about; we're
              using the keywords as soft-typed properties
        required:
        - '@type'
        - schema:name
        - schema:inDefinedTermSet
        additionalProperties: true
      allOf:
      - contains:
          type: object
          properties:
            schema:inDefinedTermSet:
              const: https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md
          required:
          - schema:inDefinedTermSet
      - contains:
          type: object
          properties:
            schema:inDefinedTermSet:
              const: http://sweetontology.net/matrElement
          required:
          - schema:inDefinedTermSet
$defs:
  CdifMandatory:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifMandatory/schema.yaml
  CdifProvActivity:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvActivity/schema.yaml
  DefinedTerm:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  AdditionalProperty:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
  DataDownload:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.yaml
  XasSample:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasSample/schema.yaml
  XasSubject:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasSubject/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasOptional/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasOptional/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasOptional/context.jsonld)

## Sources

* [CDIF-4-XAS OSCARS Project](https://doi.org/10.5281/zenodo.17421917)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/xasProperties/xasOptional`

