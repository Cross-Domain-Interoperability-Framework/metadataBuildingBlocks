## XAS Analysis Event Activity

Extends the [cdifProvActivity](../../cdifProperties/cdifProvActivity/) building block with X-ray Absorption Spectroscopy (XAS)-specific provenance activity typing and properties.

### Key features

- **Activity typing** — requires `@type` of `xas:AnalysisEvent` to distinguish XAS analysis activities from generic provenance.
- **XAS facility location** — `schema:location` references an [xasFacility](../xasFacility/) describing the synchrotron or laboratory where the analysis was performed.
- **Sample object** — `schema:object` references an [xasSample](../xasSample/) describing the sample being analyzed (following the Ocean Info Hub recommendation to use `schema:object` rather than `schema:mainEntity`).
- **XAS-specific instruments** — `prov:used` items accept [xasInstrument](../xasInstrument/) wrappers via `schema:instrument` sub-keys with hierarchical `hasPart` structure for beamline components (source, monochromator, detector).
- **XAS additional properties** — `schema:additionalProperty` supports XAS-specific property IDs: `xas:edge_energy`, `calibration method`, `Instrument configuration`, and `xas:installedOptions`.
