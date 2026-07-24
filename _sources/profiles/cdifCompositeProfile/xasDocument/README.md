# CDIF XAS document profile

Document-level CDIF profile for **X-ray Absorption Spectroscopy (XAS)** datasets.
It assembles the four base CDIF 1.1 profiles with the two XAS conformance
tiers into a single schema.org / JSON-LD document profile.

Supersedes the earlier five-profile `XASdata` composite (now in
[`archive/`](../../../../archive/profiles/cdifCompositeProfile/XASdata/)).
The difference is that this profile also composes `cdifDataStructure`,
so a conforming XAS document has to describe the byte-level layout of
its distribution as well as its measured variables.

## Composition

```
allOf:
  - cdifCore              (profiles/cdifProfile/cdifCore)
  - cdifDiscovery         (profiles/cdifProfile/cdifDiscovery)
  - cdifDataDescription   (profiles/cdifProfile/cdifDataDescription)
  - cdifDataStructure     (profiles/cdifProfile/cdifDataStructure)
  - xasCore               (xasProperties/xasCore)      # XAS mandatory tier
  - xasOptional           (xasProperties/xasOptional)  # XAS optional tier
```

Each component is composed **once**; no component re-embeds another.

## Conformance

The composite has its own conformance URI:
`https://w3id.org/cdif/xasDocument/1.0`.

A conforming XAS metadata record declares all six URIs in its
`schema:subjectOf / dcterms:conformsTo`:

```
https://w3id.org/cdif/core/1.1
https://w3id.org/cdif/discovery/1.1
https://w3id.org/cdif/data_description/1.1
https://w3id.org/cdif/data_structure/1.1
https://w3id.org/cdif/xasCore/1.0
https://w3id.org/cdif/xasOptional/1.0
```

`xasOptional/1.0` is present even when none of its optional content is
used — the URI declares "these vocabularies are understood", not
"at least one is used".

## What each component contributes

**`cdifCore` (required)** — dataset discovery mandatory content
(identifier, name, license, dateModified, url-or-distribution, catalog
record).

**`cdifDiscovery` (required)** — optional discovery content (creator,
contributor, spatial / temporal coverage, keywords, etc.).

**`cdifDataDescription` (required)** — `schema:variableMeasured` items
describing what was measured (energy, i0, itrans, etc.).

**`cdifDataStructure` (required)** — `cdi:isStructuredBy` DataStructure
plus `cdif:hasPhysicalMapping` on the distribution: columns ↔ variables
and the byte-level layout needed to parse the payload deterministically.

**`xasCore` (required)** — `@type` requires `schema:Dataset`
(`schema:Product` optional); a `prov:wasGeneratedBy` analysis activity
whose `prov:used` carries the peer instrument wrappers (source,
beamline, monochromator, monitor) with their required
`schema:additionalProperty` entries; an XDI-conformant
`schema:distribution`; required XAS `schema:measurementTechnique`
DefinedTerms; required element / edge `schema:keywords`; and the
`schema:object` material sample.

**`xasOptional` (optional)** — optional `schema:variableMeasured` XAS
data-array variables (mu*, norm*, chi*, k, r, angle …), plus documented
beamline-operational and sample physico-chemical
`schema:additionalProperty` vocabularies. Imposes no requirements.

## Files

| File | Role |
|------|------|
| `schema.yaml` | Profile schema (the `allOf` composition) |
| `xasDocumentSchema.json` | Generated JSON Schema (compact, with `$ref`s) |
| `resolvedSchema.json` | Generated JSON Schema (all `$ref`s inlined) — used for validation |
| `rules.shacl` | Aggregated SHACL shapes across the six components |
| `context.jsonld` | JSON-LD prefixes |
| `exampleCDIFxas.json` | Reference XAS example (Fe metal) |
| `example_dds_framed.json` | UKDS-adapted Se_Na2SeO4 example (see `CHANGES-from-UKDS.md`) |
| `CDIF-XAS-Full.json` | Full-coverage example exercising every enum |
| `CHANGES-from-UKDS.md` | Transformation log for `example_dds_framed.json` |
| `tests/` + `tests.yaml` | Negative test cases (JSON instances expected to fail) |

Release artifacts (implementation guide, `FrameAndValidate.py`, etc.) live
on the `cdifxasRelease` branch of
[smrgeoinfo/XAS-CDIF](https://github.com/smrgeoinfo/XAS-CDIF/tree/cdifxasRelease/release).

**Version:** 1.0 · **Maturity:** development
