# Backlog

- [ ] Update [ddi-cdi-sample-generator](https://github.com/ddialliance/ddi-cdi-sample-generator) to work with current cdifDataDescription
- [ ] Update [DDICDI_generator](https://github.com/benjaminbeuster/DDICDI_generator) to use current cdifDataDescription

## Open follow-ups from recent work

- [ ] Author the cross-cutting Dataset SHACL rule that requires `cdi:isBasedOn` on each `schema:variableMeasured` when the Dataset has `cdi:isStructuredBy`. The rule belongs on the Dataset side (likely `cdif-core` in the sibling repo), not on `ddicdiInstanceVariable`.
- [ ] Decide whether DataStructure ref sites currently pinned to `ddicdiRepresentedVariable/schema.yaml` should accept `ddicdiInstanceVariable` too (`anyOf [InstanceVariable, RepresentedVariable, id-ref]`). Sites: 7 `cdi:isDefinedBy` occurrences in `_sources/ddiProperties/ddicdiDataStructure/schema.yaml` plus 1 inside the inlined `DataStructureComponent` $def of `ddicdiInstanceVariable/schema.yaml`.
- [ ] `cdi:isBasedOn` between `cdi:InstanceVariable` and `cdi:DataStructureComponent` is a CDIF-side extension not present in DDI-CDI's canonical XMI. Either document the deviation in `ddicdiInstanceVariable/description.md` / `bblock.json`, or raise the model gap with DDI-CDI maintainers.
- [ ] Regenerate `ddicdiRepresentedVariable` BB so that `cdi:uses` (Concept) auto-discovers and `$ref`s the sibling `skosConcept` BB instead of inlining Concept locally. The newer `ddicdiInstanceVariable` already does this; the two BBs diverge on convention.
- [ ] `ddicdiDataTypes` is flagged by `tools/audit_building_blocks.py` for missing examples, but it is a shared `$defs` library by design. Either teach the audit to skip type-library BBs, or add an opt-out marker.
