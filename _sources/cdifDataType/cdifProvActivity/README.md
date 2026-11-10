# Representing the responsible agent (`schema:agent`)

Implementation guidance for the `schema:agent` property of a cdifProvActivity
(the value of `prov:wasGeneratedBy`). It records the agent primarily
responsible for the activity and maps to PROV `prov:wasAssociatedWith`.

## Accepted value forms

`schema:agent` accepts any one of four forms. Both the JSON Schema
(`schema.yaml` / `cdifProvActivitySchema.json`, as an `anyOf`) and the SHACL
(`rules.shacl`, as an `sh:or`) accept the same set:

| Form | Use when | Serialization |
|------|----------|---------------|
| **Person** | A named individual is responsible | inline `schema:Person` object |
| **Organization** | An organization/lab/facility is responsible | inline `schema:Organization` object |
| **Role** (`AgentInRole`) | The responsible party's *role* in the activity matters | inline `schema:Role` object (see below) |
| **IRI reference** | The agent is defined elsewhere in the graph or by a resolvable URI | `{ "@id": "..." }` |

Prefer a plain `Person`, `Organization`, or `@id` reference for a simple
responsible agent. Reach for the Role wrapper only when the role itself must be
carried on the provenance link.

## The `AgentInRole` (`schema:Role`) pattern

`AgentInRole` is the [schema.org Role](http://blog.schema.org/2014/06/introducing-role.html)
idiom for attaching a role to an agent. The node is typed `schema:Role` and
**requires**:

- `@type` — must contain `schema:Role`
- `schema:roleName` — the role (a concept, DefinedTerm, or string)
- `schema:contributor` — the actual agent (a `Person`/`Organization`, or an
  `{ "@id": ... }` reference to one)

```json
"schema:agent": {
    "@type": ["schema:Role"],
    "schema:roleName": "Principal Investigator",
    "schema:contributor": {
        "@type": ["schema:Person"],
        "schema:name": "Jane Doe",
        "schema:identifier": "https://orcid.org/0000-0002-1825-0097"
    }
}
```

**Note on the schema.org idiom.** The strict schema.org Role pattern repeats the
*same* property across the Role wrapper (`agent → Role → agent`). CDIF instead
reaches the real agent through `schema:contributor` on the Role. This keeps the
Role shape uniform with CDIF's other `AgentInRole` uses (creator/contributor),
at the cost of departing from the literal schema.org round-trip. Consumers that
expect the strict idiom should resolve the agent via `schema:contributor`.

For richer role modeling (several contributors, ordered roles) prefer
`schema:participant` over overloading `schema:agent`.

## Validation severity

A missing or unrecognized agent is a **Warning** (`sh:Warning`), not a
Violation — provenance is still useful without a declared agent, and the
property is optional in the JSON Schema. The SHACL and JSON Schema are kept in
lockstep: when the accepted set changes in `schema.yaml`, mirror it in the
`schema:agent` `sh:or` of `rules.shacl` and regenerate the composite shapes
(`CDIF-Complete-Shapes.ttl`, `CDIF-Provenance-Shapes.ttl`) with
`ShaclValidation/generate_shacl_shapes.py` in the validation repo.

## See also

- [description.md](description.md) — full property list for cdifProvActivity
- [agentInRole](../../schemaorgProperties/agentInRole/) — the Role building block
- [person](../../schemaorgProperties/person/), [organization](../../schemaorgProperties/organization/) — plain agent building blocks
