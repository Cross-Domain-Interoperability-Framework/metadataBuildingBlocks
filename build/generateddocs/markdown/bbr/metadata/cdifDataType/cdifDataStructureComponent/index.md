
# CDIF Data Structure Component (Schema)

`cdif.bbr.metadata.cdifDataType.cdifDataStructureComponent` *v0.1*

Role given to a represented variable in the context of a long or wide data structure to identify the units associated to data points, and in dimensional and key value data structures to provide identifying fields for the instance values.

[*Status*](http://www.opengis.net/def/status): Under development

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
  cdifConceptOrTerm:
    anyOf:
    - type: object
      properties:
        '@id':
          type: string
          description: reference to a skos concept for the data type
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifConceptScheme/schema.yaml#/$defs/cdifConcept
  id-reference:
    type: object
    description: Reference to a node defined elsewhere in the document via its @id.
    properties:
      '@id':
        type: string
    required:
    - '@id'
  IdentifierComponent:
    type: object
    description: Role given to a represented variable in the context of a long or
      wide data structure to identify the units associated to data points, and in
      dimensional and key value data structures to provide identifying fields for
      the instance values.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:IdentifierComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this IdentifierComponent node
      cdif:isDefinedBy_RepresentedVariable:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifRepresentedVariable/schema.yaml
        - $ref: '#/$defs/id-reference'
        x-jsonld-id: https://w3id.org/cdif/isDefinedBy_RepresentedVariable
    required:
    - '@type'
    - cdif:isDefinedBy_RepresentedVariable
  MeasureComponent:
    type: object
    description: Role given to a represented variable in the context of a data structure
      to hold the observed/derived values.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:MeasureComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this MeasureComponent node
      cdif:name:
        type: array
        items:
          type: string
        minItems: 1
        description: Human understandable name (liguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: https://w3id.org/cdif/name
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdif:isDefinedBy_RepresentedVariable:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifRepresentedVariable/schema.yaml
        - $ref: '#/$defs/id-reference'
        x-jsonld-id: https://w3id.org/cdif/isDefinedBy_RepresentedVariable
      cdi:semantic:
        type: array
        items:
          anyOf:
          - type: string
          - $ref: '#/$defs/cdifConceptOrTerm'
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/semantic
    required:
    - '@type'
  AttributeComponent:
    type: object
    description: Role given to a represented variable in the context of a data structure
      to qualify observations or provide other types of supplementary information.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:AttributeComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this AttributeComponent node
      cdi:qualifies:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/DataStructureComponent'
          - $ref: '#/$defs/id-reference'
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/qualifies
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdif:isDefinedBy_RepresentedVariable:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifRepresentedVariable/schema.yaml
        - $ref: '#/$defs/id-reference'
        x-jsonld-id: https://w3id.org/cdif/isDefinedBy_RepresentedVariable
      cdi:semantic:
        type: array
        items:
          anyOf:
          - type: string
          - $ref: '#/$defs/cdifConceptOrTerm'
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/semantic
    required:
    - '@type'
  DimensionComponent:
    type: object
    description: 'Role given to a represented variable in the context of a dimensional
      data structure to identify the universes associated with data points. The variable
      acts as a field in the compound identifier (the key structure) to disambiguate
      the cells in the multi-dimensional "cube".  AG: references to the variables
      which are the components of a compound identifier, in which each variable is
      a single field - an axis - in a coordinate system addressing a location in a
      matrix. These variables are often categorical, but also commonly include time.
      Unlike other Components, they may be ordered using instances of cdi:ComponentPosition.'
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DimensionComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DimensionComponent node
      cdif:isDefinedBy_RepresentedVariable:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifRepresentedVariable/schema.yaml
        - $ref: '#/$defs/id-reference'
        x-jsonld-id: https://w3id.org/cdif/isDefinedBy_RepresentedVariable
    required:
    - '@type'
    - cdif:isDefinedBy_RepresentedVariable
  VariableValueComponent:
    type: object
    description: Role given to a represented variable in the context of a data structure
      to record values of multiple variables.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:VariableValueComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this VariableValueComponent node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdif:isDefinedBy_RepresentedVariable:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifRepresentedVariable/schema.yaml
        - $ref: '#/$defs/id-reference'
        x-jsonld-id: https://w3id.org/cdif/isDefinedBy_RepresentedVariable
      cdi:semantic:
        type: array
        items:
          anyOf:
          - type: string
          - $ref: '#/$defs/cdifConceptOrTerm'
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/semantic
    required:
    - '@type'
  VariableDescriptorComponent:
    type: object
    description: Role given to a represented variable in the context of a data structure
      to provide codes for variable identification.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:VariableDescriptorComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this VariableDescriptorComponent node
      cdif:isDefinedBy_DescriptorVariable:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDescriptorVariable/schema.yaml
        x-jsonld-id: https://w3id.org/cdif/isDefinedBy_DescriptorVariable
      cdi:refersTo:
        $ref: '#/$defs/id-reference'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/refersTo
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:semantic:
        type: array
        items:
          anyOf:
          - type: string
          - $ref: '#/$defs/cdifConceptOrTerm'
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/semantic
    required:
    - '@type'
    - cdif:isDefinedBy_DescriptorVariable
  DataStructureComponent:
    type: object
    description: Role given to a represented variable in the context of a data structure.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DataStructureComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DataStructureComponent node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdif:isDefinedBy_RepresentedVariable:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifRepresentedVariable/schema.yaml
        - $ref: '#/$defs/id-reference'
        x-jsonld-id: https://w3id.org/cdif/isDefinedBy_RepresentedVariable
      cdi:semantic:
        type: array
        items:
          anyOf:
          - type: string
          - $ref: '#/$defs/cdifConceptOrTerm'
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/semantic
    required:
    - '@type'
x-jsonld-prefixes:
  cdif: https://w3id.org/cdif/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdif": "https://w3id.org/cdif/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
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

