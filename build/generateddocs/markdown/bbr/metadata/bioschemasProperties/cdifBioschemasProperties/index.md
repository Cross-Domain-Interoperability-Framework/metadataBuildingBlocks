
# CDIF Bioschemas Properties (Schema)

`cdif.bbr.metadata.bioschemasProperties.cdifBioschemasProperties` *v0.1*

Bioschemas classes and properties for describing laboratory workflow provenance in CDIF metadata. Defines types from the Bioschemas and ARC Workflow Run RO-Crate profiles: bios:LabProcess (lab process execution), bios:LabProtocol (lab methodology), bios:Sample (physical sample), bios:FormalParameter (workflow parameter definition), bios:ComputationalWorkflow (computational workflow definition). Properties: bios:executesLabProtocol (link process to protocol), bios:parameterValue (actual parameter settings), bios:labEquipment (lab instruments on protocol), bios:computationalTool (software tools on protocol), bios:reagent (materials used). Based on the ARC Workflow Run RO-Crate profile (https://github.com/nfdi4plants/arc-wr-ro-crate-profile).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Bioschemas Properties

This building block defines Bioschemas classes and properties for describing laboratory workflow provenance within the CDIF metadata framework. It draws from the [Bioschemas](https://bioschemas.org/) vocabulary and the [ARC Workflow Run RO-Crate profile](https://github.com/nfdi4plants/arc-wr-ro-crate-profile).

### Namespace

All Bioschemas types and properties use the `bios:` prefix:

```
bios: https://bioschemas.org/
```

### Classes

| Class | Description | cdifProvActivity Mapping |
|---|---|---|
| `bios:LabProcess` | A laboratory process execution | `schema:additionalType` on `["schema:Action", "prov:Activity"]` |
| `bios:LabProtocol` | Methodology describing how a lab process should be carried out | `schema:HowTo` via `schema:actionProcess` |
| `bios:Sample` | A physical or material sample | `schema:Thing` with `schema:additionalType: ["bios:Sample"]` |
| `bios:FormalParameter` | Expected input/output definition for a workflow | `schema:MediaObject` with `schema:additionalType: ["bios:FormalParameter"]` |
| `bios:ComputationalWorkflow` | A computational workflow definition | `schema:SoftwareApplication` with `schema:additionalType: ["bios:ComputationalWorkflow"]` |

### Properties

| Property | Domain | Range | Description |
|---|---|---|---|
| `bios:executesLabProtocol` | `bios:LabProcess` | `bios:LabProtocol` | Links a process execution to the protocol it follows |
| `bios:parameterValue` | `bios:LabProcess` | `schema:PropertyValue` | Actual parameter settings used during execution |
| `bios:labEquipment` | `bios:LabProtocol` | `schema:DefinedTerm` | Laboratory instruments and equipment |
| `bios:computationalTool` | `bios:LabProtocol` | `schema:SoftwareApplication` | Software tools used in the protocol |
| `bios:reagent` | `bios:LabProtocol` | `schema:Thing` | Materials or chemical substances used |

### Relationship to cdifProvActivity

This building block extends cdifProvActivity for laboratory analytical workflows. A cdifProvActivity activity node with Bioschemas extensions looks like:

```json
{
  "@type": ["schema:Action", "prov:Activity"],
  "schema:additionalType": ["schema:CreateAction", "bios:LabProcess"],
  "schema:name": "Flash pyrolysis at 600°C",
  "bios:executesLabProtocol": {
    "@type": ["schema:HowTo"],
    "schema:additionalType": ["bios:LabProtocol"],
    "schema:name": "Flash pyrolysis protocol",
    "bios:labEquipment": [...]
  },
  "schema:actionProcess": {"@id": "#protocol-ref"},
  "bios:parameterValue": [
    {
      "@type": "schema:PropertyValue",
      "schema:name": "Target temperature",
      "schema:value": 600,
      "schema:unitText": "°C"
    }
  ],
  "schema:additionalProperty": [...]
}
```

The `bios:executesLabProtocol` property parallels `schema:actionProcess` — both point to the methodology, but the Bioschemas property preserves the specific lab protocol semantics from the ARC profile.

### Sources

- [ARC Workflow Run RO-Crate Profile](https://github.com/nfdi4plants/arc-wr-ro-crate-profile)
- [Bioschemas LabProcess Profile](https://bioschemas.org/profiles/LabProcess)
- [Bioschemas LabProtocol Profile](https://bioschemas.org/profiles/LabProtocol)
- [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/)

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Bioschemas Properties
description: Bioschemas classes and properties for laboratory workflow provenance
  in CDIF. Defines types and properties from the Bioschemas vocabulary and the ARC
  Workflow Run RO-Crate profile for describing lab processes, protocols, samples,
  parameters, equipment, and computational tools.
type: object
properties:
  bios:executesLabProtocol:
    description: The laboratory protocol executed by this process. Links a LabProcess
      activity to the LabProtocol it follows. In cdifProvActivity, also mapped to
      schema:actionProcess for compatibility.
    anyOf:
    - $ref: '#/$defs/LabProtocol'
    - type: object
      properties:
        '@id':
          type: string
          description: reference to a LabProtocol defined elsewhere
      required:
      - '@id'
  bios:parameterValue:
    description: Actual parameter values used during a lab process execution. Each
      entry is a schema:PropertyValue recording a specific instrument setting or measurement
      condition (temperature, flow rate, scan range, etc.).
    type: array
    items:
      $ref: '#/$defs/ParameterValue'
  bios:labEquipment:
    description: Laboratory equipment used in a protocol. Instruments, devices, and
      apparatus employed during the process.
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/LabEquipment'
      - type: object
        properties:
          '@id':
            type: string
            description: reference to equipment defined elsewhere
        required:
        - '@id'
  bios:computationalTool:
    description: Software or computational tool used as part of a lab protocol to
      complete a part of it.
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/ComputationalTool'
      - type: object
        properties:
          '@id':
            type: string
            description: reference to a software tool defined elsewhere
        required:
        - '@id'
  bios:reagent:
    description: Materials or chemical substances used in protocol execution.
    type: array
    items:
      anyOf:
      - type: string
        description: name or URI of the reagent
      - type: object
        properties:
          '@id':
            type: string
          schema:name:
            type: string
          schema:description:
            type: string
$defs:
  LabProcess:
    type: object
    description: "A Bioschemas LabProcess \u2014 a laboratory process execution. Used
      as an additionalType on a cdifProvActivity activity ([\"schema:Action\", \"prov:Activity\"])
      to indicate that the activity represents a lab process. Carries bios:executesLabProtocol
      to link to the protocol followed and bios:parameterValue for actual instrument
      settings."
    properties:
      '@type':
        type: array
        items:
          type: string
        description: Must include bios:LabProcess as additionalType on the activity
      '@id':
        type: string
      schema:name:
        type: string
        description: Short human-readable description of the execution
      schema:description:
        type: string
        description: Details of the execution, e.g. command line arguments or notes
      bios:executesLabProtocol:
        description: The executed protocol
        anyOf:
        - $ref: '#/$defs/LabProtocol'
        - type: object
          properties:
            '@id':
              type: string
          required:
          - '@id'
      bios:parameterValue:
        type: array
        items:
          $ref: '#/$defs/ParameterValue'
    required:
    - '@type'
    - schema:name
  LabProtocol:
    type: object
    description: A Bioschemas LabProtocol describing how a lab process should be carried
      out. Includes equipment, reagents, computational tools, and expected parameters.
      Maps to schema:HowTo in the cdifProvActivity context.
    properties:
      '@type':
        anyOf:
        - type: string
          const: bios:LabProtocol
        - type: array
          items:
            type: string
          contains:
            const: bios:LabProtocol
      '@id':
        type: string
      schema:name:
        type: string
        description: Name of the protocol
      schema:description:
        type: string
        description: Description of the protocol
      schema:url:
        type: string
        format: uri
        description: URL to a published protocol document
      bios:labEquipment:
        description: Equipment used in this protocol
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/LabEquipment'
          - type: object
            properties:
              '@id':
                type: string
            required:
            - '@id'
      bios:computationalTool:
        description: Software tools used in this protocol
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ComputationalTool'
          - type: object
            properties:
              '@id':
                type: string
            required:
            - '@id'
      bios:reagent:
        description: Reagents or materials used
        type: array
        items:
          anyOf:
          - type: string
          - type: object
            properties:
              '@id':
                type: string
              schema:name:
                type: string
      schema:intendedUse:
        type: string
        description: The protocol type or intended use as an ontology term or text
      schema:measurementMethod:
        type: string
        description: The analytical method implemented by this protocol
      schema:object:
        description: Expected input parameters (FormalParameter references)
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/FormalParameter'
          - type: object
            properties:
              '@id':
                type: string
            required:
            - '@id'
      schema:result:
        description: Expected output parameters (FormalParameter references)
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/FormalParameter'
          - type: object
            properties:
              '@id':
                type: string
            required:
            - '@id'
    required:
    - '@type'
    - schema:name
  Sample:
    type: object
    description: A Bioschemas Sample representing a physical or material entity used
      or produced by lab processes. In cdifProvActivity output, typed as schema:Thing
      with schema:additionalType bios:Sample.
    properties:
      '@type':
        type: array
        items:
          type: string
        description: Should include schema:Thing with additionalType bios:Sample
      '@id':
        type: string
      schema:name:
        type: string
        description: Name or label of the sample
      schema:description:
        type: string
        description: Description of the sample
      schema:identifier:
        description: Formal sample identifier
        anyOf:
        - type: string
        - type: object
          properties:
            '@type':
              type: string
            schema:propertyID:
              type: string
            schema:value:
              type: string
      schema:additionalProperty:
        type: array
        description: Sample-specific metadata (mass, preparation method, container,
          etc.)
        items:
          $ref: '#/$defs/ParameterValue'
    required:
    - schema:name
  FormalParameter:
    type: object
    description: A Bioschemas FormalParameter describing the shape and type of inputs
      and outputs of a workflow protocol. Values are realized in process executions
      through bios:parameterValue PropertyValue objects. In cdifProvActivity output,
      mapped to schema:MediaObject with additionalType bios:FormalParameter.
    properties:
      '@type':
        type: array
        items:
          type: string
        description: Should include schema:MediaObject with additionalType bios:FormalParameter
      '@id':
        type: string
      schema:name:
        type: string
        description: Name matching the corresponding workflow parameter slot
      schema:description:
        type: string
        description: Description of what this parameter represents
      schema:additionalType:
        description: Further type classification (e.g. File, Dataset, PropertyValue,
          DataType)
        anyOf:
        - type: string
        - type: array
          items:
            type: string
      schema:encodingFormat:
        description: MIME type or URL for expected data format
        anyOf:
        - type: string
        - type: array
          items:
            type: string
      schema:defaultValue:
        description: Default value for this parameter
    required:
    - schema:name
  ComputationalWorkflow:
    type: object
    description: A Bioschemas ComputationalWorkflow representing the prospective provenance
      of a computational or hybrid lab-computational workflow. Combined with LabProtocol
      in ARC profiles to bridge computational and laboratory domains. In cdifProvActivity
      output, mapped to schema:SoftwareApplication with additionalType bios:ComputationalWorkflow.
    properties:
      '@type':
        type: array
        items:
          type: string
        description: Should include schema:SoftwareApplication with additionalType
          bios:ComputationalWorkflow
      '@id':
        type: string
      schema:name:
        type: string
        description: Descriptive title of the workflow
      schema:description:
        type: string
        description: Textual explanation of the workflow
      schema:version:
        type: string
        description: Version identifier
      schema:programmingLanguage:
        description: Language or engine for the workflow
        anyOf:
        - type: string
        - type: object
          properties:
            '@type':
              type: string
            schema:name:
              type: string
            schema:url:
              type: string
              format: uri
      schema:object:
        description: Input FormalParameters
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/FormalParameter'
          - type: object
            properties:
              '@id':
                type: string
            required:
            - '@id'
      schema:result:
        description: Output FormalParameters
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/FormalParameter'
          - type: object
            properties:
              '@id':
                type: string
            required:
            - '@id'
      schema:hasPart:
        description: Sub-workflows, sub-protocols, or component tools
        type: array
        items:
          anyOf:
          - type: object
            properties:
              '@id':
                type: string
            required:
            - '@id'
          - type: object
    required:
    - '@type'
    - schema:name
  LabEquipment:
    type: object
    description: "Laboratory equipment or instrument described as a schema:DefinedTerm.
      Physical instruments that don't have software versions \u2014 pyrolysis ovens,
      chromatographs, mass spectrometers, etc."
    properties:
      '@type':
        type: array
        items:
          type: string
        minItems: 1
        contains:
          const: schema:Thing
        description: Must include schema:Thing. Typically also includes schema:DefinedTerm.
      '@id':
        type: string
      schema:name:
        type: string
        description: Name of the equipment
      schema:description:
        type: string
        description: Description including capabilities and specifications
      schema:identifier:
        description: Serial number or other formal identifier
        anyOf:
        - type: string
        - type: object
      schema:url:
        type: string
        format: uri
        description: URL to manufacturer or equipment documentation
    required:
    - schema:name
  ComputationalTool:
    type: object
    description: A software application used as part of a lab protocol.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:SoftwareApplication
      '@id':
        type: string
      schema:name:
        type: string
      schema:description:
        type: string
      schema:url:
        type: string
        format: uri
      schema:version:
        type: string
    required:
    - schema:name
  ParameterValue:
    type: object
    description: A schema:PropertyValue recording an actual parameter setting used
      during a lab process execution. Contains the measured or configured value, units,
      and optionally a link back to the FormalParameter definition via schema:propertyID.
    properties:
      '@type':
        anyOf:
        - type: string
          const: schema:PropertyValue
        - type: array
          items:
            type: string
          contains:
            const: schema:PropertyValue
      '@id':
        type: string
      schema:name:
        type: string
        description: Name of the parameter
      schema:value:
        description: The actual value (string, number, or boolean)
        anyOf:
        - type: string
        - type: number
        - type: boolean
      schema:unitText:
        type: string
        description: Unit of measurement (e.g. degrees C, mL/min, mg)
      schema:propertyID:
        description: Link to the FormalParameter definition this value realizes
        anyOf:
        - type: string
        - type: object
          properties:
            '@id':
              type: string
    required:
    - '@type'
    - schema:name
x-jsonld-prefixes:
  schema: http://schema.org/
  prov: http://www.w3.org/ns/prov#
  bios: https://bioschemas.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/cdifBioschemasProperties/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/cdifBioschemasProperties/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "bios": "https://bioschemas.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/cdifBioschemasProperties/context.jsonld)

## Sources

* [ARC Workflow Run RO-Crate Profile](https://github.com/nfdi4plants/arc-wr-ro-crate-profile)
* [Bioschemas LabProcess](https://bioschemas.org/profiles/LabProcess)
* [Bioschemas LabProtocol](https://bioschemas.org/profiles/LabProtocol)
* [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/bioschemasProperties/cdifBioschemasProperties`

