# CDIF XASdata profile

Composite CDIF profile for **X-ray Absorption Spectroscopy (XAS)** datasets. It assembles the
CDIF base profiles with the two XAS conformance tiers into a single schema.org / JSON-LD
implementation profile.

## Composition

```
allOf:
  - cdifCore              (profiles/cdifProfile/cdifCore)
  - cdifDiscovery         (profiles/cdifProfile/cdifDiscovery)
  - cdifDataDescription   (profiles/cdifProfile/cdifDataDescription)
  - xasCore               (xasProperties/xasCore)      # XAS mandatory tier
  - xasOptional           (xasProperties/xasOptional)  # XAS optional tier
```

Each component is composed **once**; no component re-embeds another.

## Two-tier conformance model

XAS conformance is declared through two tier URIs (there is no separate composite-profile
conformance URI):

| Tier | Conformance URI | Required? |
|------|-----------------|-----------|
| **Mandatory** (`xasCore`) | `https://w3id.org/cdif/xasCore/1.0` | yes |
| **Optional** (`xasOptional`) | `https://w3id.org/cdif/xasOptional/1.0` | only when optional XAS fields are present |

A conformant XAS metadata record therefore declares, in its
`schema:subjectOf / dcterms:conformsTo`:

```
https://w3id.org/cdif/core/1.1
https://w3id.org/cdif/discovery/1.1
https://w3id.org/cdif/data_description/1.1
https://w3id.org/cdif/xasCore/1.0
https://w3id.org/cdif/xasOptional/1.0   (optional)
```

The `metadataProfileProperty` SHACL shape (`rules.shacl`) requires the first four; the optional
tier is advisory (`sh:Warning` in `xasOptional/rules.shacl`).

## What each tier contributes

**`xasCore` (required)** — `@type` requires `schema:Dataset` (`schema:Product` optional); a
`prov:wasGeneratedBy` analysis activity whose `prov:used` carries the instrument wrapper
(`NXsource` + `NXmonochromator` sub-components with required type / probe / d-spacing /
reflection); an XDI-conformant `schema:distribution`; required XAS `schema:measurementTechnique`
DefinedTerms; required element / edge `schema:keywords`; and the `schema:object` material sample.

**`xasOptional` (optional)** — optional `schema:variableMeasured` XAS data-array variables
(energy, i0, itrans, mu*, norm*, chi*, k, r, angle …), plus documented beamline-operational and
sample physico-chemical `schema:additionalProperty` vocabularies. Imposes no requirements.

## Files

| File | Role |
|------|------|
| `schema.yaml` | Profile schema (the `allOf` composition) |
| `XASdataSchema.json` | Generated JSON Schema (compact, with `$ref`s) |
| `resolvedSchema.json` | Generated JSON Schema (all `$ref`s inlined) — used for validation |
| `rules.shacl` | Profile-level SHACL (conformance + complete-dataset shapes) |
| `context.jsonld` | JSON-LD prefixes |
| `exampleCDIFxas.json` | Worked example (validates against `resolvedSchema.json`) |

**Version:** 1.0 · **Maturity:** stable
