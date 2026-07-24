# CDIF XAS document profile

Document-level CDIF profile for X-ray Absorption Spectroscopy datasets.

## Composition

| Component | Role | Conformance URI |
|-----------|------|-----------------|
| cdifCore | dataset discovery mandatory content | `https://w3id.org/cdif/core/1.1` |
| cdifDiscovery | dataset discovery optional content | `https://w3id.org/cdif/discovery/1.1` |
| cdifDataDescription | measured variables and their semantics | `https://w3id.org/cdif/data_description/1.1` |
| cdifDataStructure | physical / logical / tabular data structure | `https://w3id.org/cdif/data_structure/1.1` |
| xasCore | XAS-mandatory instrument + sample metadata | `https://w3id.org/cdif/xasCore/1.0` |
| xasOptional | XAS-recommended metadata (calibration, edge, etc.) | `https://w3id.org/cdif/xasOptional/1.0` |

## Conformance URI

`https://w3id.org/cdif/xasDocument/1.0`

## Release

Release artifacts (resolved schema, aggregated SHACL, implementation guide,
frame, examples) are built into the `cdifxasRelease` branch of the
[XAS-CDIF](https://github.com/smrgeoinfo/XAS-CDIF) repository.
