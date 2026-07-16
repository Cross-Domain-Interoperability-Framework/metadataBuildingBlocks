# xasProperties

Building blocks for describing **X-ray Absorption Spectroscopy (XAS)** datasets in the CDIF
schema.org / JSON-LD implementation. These compose into the
[`XASdata`](../profiles/cdifCompositeProfile/XASdata/) composite profile.

## Building blocks

| Block | Role |
|-------|------|
| [`xasCore`](xasCore/) | **XAS mandatory tier.** Required XAS constraints layered on `cdifCore`: dual `@type` (Dataset + Product), the `prov:wasGeneratedBy` analysis activity with the `NXsource`+`NXmonochromator` instrument wrapper, XDI-conformant distribution, required measurementTechnique DefinedTerms, required element/edge keywords, and the `schema:object` sample. |
| [`xasOptional`](xasOptional/) | **XAS optional tier.** Genuinely-optional XAS fields — data-array `schema:variableMeasured` InstanceVariables plus documented beamline-operational and sample physico-chemical `additionalProperty` vocabularies. No requirements. |
| [`xasSample`](xasSample/) | Material sample that is the `schema:object` (target) of an XAS analysis; `schema:Thing`+`schema:Product` typed with `MaterialSample` + iSample `additionalType`. |
| [`xasInstrument`](xasInstrument/) | XAS instrument / instrument system (extends the generic `instrument` block; requires `wd:Q3099911` scientific-instrument `additionalType`). |
| [`xasFacility`](xasFacility/) | The facility (a `schema:Place` typed `xas:Facility`, e.g. a synchrotron) where data is acquired; carried as `schema:location` on the analysis event. |
| [`xasGeneratedBy`](xasGeneratedBy/) | XAS analysis activity — triple-typed `["schema:Action","xas:AnalysisEvent","prov:Activity"]`, extends `cdifProvActivity` with the facility, sample object, and instrument wrappers. |

> `xasXdiTabularTextDataset` was retired to [`../../archive/`](../../archive/) — it was unwired
> from any profile and modeled data structure with the DDI-CDI `cdi:` vocabulary rather than the
> CDIF `cdif:hasPhysicalMapping` convention.

## Conformance tiers

XAS defines two conformance tiers (there is no "discovery" tier):

| Tier | Block | URI |
|------|-------|-----|
| Mandatory | `xasCore` | `https://w3id.org/cdif/xasCore/1.0` |
| Optional | `xasOptional` | `https://w3id.org/cdif/xasOptional/1.0` |

Both resolve through w3id (see the [CDIF w3id redirects](https://github.com/perma-id/w3id.org/tree/master/cdif))
to these live `_sources` files.

## Namespaces

| Prefix | IRI |
|--------|-----|
| `xas` | `https://xas.org/dictionary/` |
| `nxs` | `https://manual.nexusformat.org/classes/` |
| `wd` | `https://www.wikidata.org/entity/` |

**Version:** 1.0 · **Maturity:** stable
