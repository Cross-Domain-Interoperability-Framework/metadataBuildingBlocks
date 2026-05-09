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
