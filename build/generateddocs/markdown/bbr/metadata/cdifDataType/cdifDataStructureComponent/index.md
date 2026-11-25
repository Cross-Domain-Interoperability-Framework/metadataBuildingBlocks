
# CDIF Data Structure Component (Schema)

`cdif.bbr.metadata.cdifDataType.cdifDataStructureComponent` *v0.1*

Role given to a represented variable in the context of a long or wide data structure to identify the units associated to data points, and in dimensional and key value data structures to provide identifying fields for the instance values.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Measure component defined by a represented variable
A cdi:MeasureComponent — the role a variable takes in a data structure to hold the
observed or derived values. Its cdif:isDefinedBy_Variable carries an inline
cdi:RepresentedVariable, exercising the first branch of that property's anyOf; the
alternatives are an inline cdi:InstanceVariable or an @id reference. MeasureComponent
requires only @type, so every property shown beneath it is optional. This block's root
anyOf offers six component types and this example covers one of them.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@type": [
    "cdi:MeasureComponent"
  ],
  "@id": "ex:struct/vitalsWide/comp/systolicBP",
  "cdif:isDefinedBy_Variable": {
    "@type": [
      "cdi:RepresentedVariable"
    ],
    "@id": "ex:struct/vitalsWide/rv/systolicBP",
    "cdif:name": [
      "systolic_bp"
    ],
    "cdi:simpleUnitOfMeasure": "mmHg",
    "cdif:hasIntendedDataType": "xsd:integer"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:MeasureComponent"
  ],
  "@id": "ex:struct/vitalsWide/comp/systolicBP",
  "cdif:isDefinedBy_Variable": {
    "@type": [
      "cdi:RepresentedVariable"
    ],
    "@id": "ex:struct/vitalsWide/rv/systolicBP",
    "cdif:name": [
      "systolic_bp"
    ],
    "cdi:simpleUnitOfMeasure": "mmHg",
    "cdif:hasIntendedDataType": "xsd:integer"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .

<https://example.org/struct/vitalsWide/comp/systolicBP> a cdi:MeasureComponent ;
    cdif:isDefinedBy_Variable <https://example.org/struct/vitalsWide/rv/systolicBP> .

<https://example.org/struct/vitalsWide/rv/systolicBP> a cdi:RepresentedVariable ;
    cdi:simpleUnitOfMeasure "mmHg" ;
    cdif:hasIntendedDataType "xsd:integer" ;
    cdif:name "systolic_bp" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Data Structure Component
description: Role given to a represented variable in the context of a long or wide
  data structure to identify the units associated to data points, and in dimensional
  and key value data structures to provide identifying fields for the instance values.
anyOf:
- $ref: '#/$defs/IdentifierComponent'
- $ref: '#/$defs/MeasureComponent'
- $ref: '#/$defs/AttributeComponent'
- $ref: '#/$defs/DimensionComponent'
- $ref: '#/$defs/VariableValueComponent'
- $ref: '#/$defs/VariableDescriptorComponent'
$defs:
  cdifConceptOrTermOrString:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTermOrString/schema.yaml
  cdifConceptOrTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTerm/schema.yaml
  DataStructureComponent:
    type: object
    description: Members common to every data structure component. Composed into each
      component below with allOf; not a component type in its own right, and not a
      branch of this schema's root anyOf.
    properties:
      '@id':
        type: string
        description: Identifier for this DataStructureComponent node
      cdif:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: https://w3id.org/cdif/identifier
      cdif:isDefinedBy_Variable:
        description: The variable this component is a role of -- a RepresentedVariable
          or an InstanceVariable, inline or by @id reference. See the note above $defs.
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifRepresentedVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        x-jsonld-id: https://w3id.org/cdif/isDefinedBy_Variable
      cdif:semantic:
        type: array
        items:
          $ref: '#/$defs/cdifConceptOrTermOrString'
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
        x-jsonld-id: https://w3id.org/cdif/semantic
  IdentifierComponent:
    description: Role given to a represented variable in the context of a long or
      wide data structure to identify the units associated to data points, and in
      dimensional and key value data structures to provide identifying fields for
      the instance values.
    allOf:
    - $ref: '#/$defs/DataStructureComponent'
    - type: object
      properties:
        '@type':
          type: array
          items:
            type: string
          contains:
            const: cdi:IdentifierComponent
          minItems: 1
      required:
      - '@type'
      - cdif:isDefinedBy_Variable
  MeasureComponent:
    description: Role given to a represented variable in the context of a data structure
      to hold the observed/derived values.
    allOf:
    - $ref: '#/$defs/DataStructureComponent'
    - type: object
      properties:
        '@type':
          type: array
          items:
            type: string
          contains:
            const: cdi:MeasureComponent
          minItems: 1
        cdif:name:
          anyOf:
          - type: string
          - type: array
            items:
              type: string
            minItems: 1
          description: Human understandable name (linguistic signifier, word, phrase,
            or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
            provided to specify usage.
          x-jsonld-id: https://w3id.org/cdif/name
      required:
      - '@type'
  AttributeComponent:
    description: Role given to a represented variable in the context of a data structure
      to qualify observations or provide other types of supplementary information.
    allOf:
    - $ref: '#/$defs/DataStructureComponent'
    - type: object
      properties:
        '@type':
          type: array
          items:
            type: string
          contains:
            const: cdi:AttributeComponent
          minItems: 1
        cdif:qualifies:
          type: array
          description: The data structure components whose observations this attribute
            qualifies. Any component except another AttributeComponent, inline or
            by @id reference.
          items:
            anyOf:
            - $ref: '#/$defs/IdentifierComponent'
            - $ref: '#/$defs/MeasureComponent'
            - $ref: '#/$defs/DimensionComponent'
            - $ref: '#/$defs/VariableValueComponent'
            - $ref: '#/$defs/VariableDescriptorComponent'
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
          minItems: 1
          x-jsonld-id: https://w3id.org/cdif/qualifies
      required:
      - '@type'
  DimensionComponent:
    description: 'Role given to a represented variable in the context of a dimensional
      data structure to identify the universes associated with data points. The variable
      acts as a field in the compound identifier (the key structure) to disambiguate
      the cells in the multi-dimensional "cube".  AG: references to the variables
      which are the components of a compound identifier, in which each variable is
      a single field - an axis - in a coordinate system addressing a location in a
      matrix. These variables are often categorical, but also commonly include time.
      Unlike other Components, they may be ordered using instances of cdi:ComponentPosition.'
    allOf:
    - $ref: '#/$defs/DataStructureComponent'
    - type: object
      properties:
        '@type':
          type: array
          items:
            type: string
          contains:
            const: cdi:DimensionComponent
          minItems: 1
        cdif:categoricalAdditivity:
          type: boolean
          default: false
          description: 'Indicates whether categories at a specific level can be combined
            to provide the value for their shared parent category. Value is True if
            categories can be added together (collapsed) to create higher-level categories.
            An example would be age categories: five-year age categories can be collapsed
            into 10-year age categories.'
          x-jsonld-id: https://w3id.org/cdif/categoricalAdditivity
      required:
      - '@type'
      - cdif:isDefinedBy_Variable
  VariableValueComponent:
    description: Role given to a represented variable in the context of a data structure
      to record values of multiple variables.
    allOf:
    - $ref: '#/$defs/DataStructureComponent'
    - type: object
      properties:
        '@type':
          type: array
          items:
            type: string
          contains:
            const: cdi:VariableValueComponent
          minItems: 1
      required:
      - '@type'
  VariableDescriptorComponent:
    description: Role given to a represented variable in the context of a data structure
      to provide codes for variable identification.
    allOf:
    - $ref: '#/$defs/DataStructureComponent'
    - type: object
      properties:
        '@type':
          type: array
          items:
            type: string
          contains:
            const: cdi:VariableDescriptorComponent
          minItems: 1
        cdif:isDefinedBy_DescriptorVariable:
          description: 'Variable that provides codes for variable identification in
            the context of a data structure. Descriptor Variables hold values which
            reference the logical variables in the data set, indicating which one
            the associated value in the corresponding Reference Variable is a measure/value
            for. Descriptor Variables are presentational variables found only in Long
            Data Sets. EA models this as its own association (connector 345) rather
            than a formal redefinition of the inherited isDefinedBy (connector 429),
            but CDIF treats it as a redefinition: the variable a VariableDescriptorComponent
            is a role of IS its DescriptorVariable, so the inherited property is disallowed
            below rather than left available.'
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDescriptorVariable/schema.yaml
          x-jsonld-id: https://w3id.org/cdif/isDefinedBy_DescriptorVariable
        cdif:isDefinedBy_Variable:
          not: {}
          x-jsonld-id: https://w3id.org/cdif/isDefinedBy_Variable
        cdi:refersTo:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
          x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/refersTo
      required:
      - '@type'
      - cdif:isDefinedBy_DescriptorVariable
x-jsonld-prefixes:
  cdif: https://w3id.org/cdif/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.cdifDataType.cdifDataStructureComponent
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-25'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdif": "https://w3id.org/cdif/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "spdx": "http://spdx.org/rdf/terms#",
    "xas": "cdif:xas/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "prov": "http://www.w3.org/ns/prov#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifDataStructureComponent`

