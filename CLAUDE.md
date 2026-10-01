# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Read first

**`agents.md` (~1100 lines) is the authoritative reference** — repository structure, every tool's
CLI, composition rules, namespace policy, conformance URIs, OGC-vs-this-repo deltas. Read the
relevant section before non-trivial work, and update it when you change a convention or a tool.
`README.md` documents the schema pipeline and the JSON Forms conversion.

This file covers only what those two don't: the commands you'll actually run, and the handful of
project-specific traps that cost real time.

## Commands

```bash
pip install -r requirements.txt          # jsonschema, PyYAML (+ optional pyshacl)
```

**Regeneration — run both, always, in the same commit as the source edit:**

```bash
python tools/resolve_schema.py --all      # -> resolvedSchema.json (92 blocks, ~11 min)
python tools/regenerate_schema_json.py    # -> *Schema.json (93 blocks, seconds)
```

Locally, `--all` is still the honest thing to run before a commit. To regenerate only what your
edit can reach — what CI now does on a pull request — ask which blocks those are:

```bash
python tools/affected_blocks.py --base origin/main    # prints schema.yaml paths, or ALL
```

**Validation:**

```bash
python tools/validate_examples.py                        # JSON Schema gate, all examples (~10 min)
python tools/validate_examples.py -f spatialExtent       # single block / substring filter
python tools/validate_shacl.py <profile-name> --strict   # opt-in SHACL, one target
python tools/audit_building_blocks.py                    # files, freshness, examples, SHACL coverage
python tools/audit_building_blocks.py -c type-enum       # @type enum vs the SHACL list restating it
python tools/test_fail_cases.py --strict                 # negative tests fail for their NAMED reason
python tools/audit_cdif_vocabulary.py --self-test         # then -o to inventory every cdif: term
```

**`cdif:` terms are minted and defined nowhere.** Measured 2026-09-28: `https://w3id.org/cdif/`
returns 200 only because it redirects to the book, while `https://w3id.org/cdif/Key` returns 404 —
47 live terms (8 classes, 39 properties), no `model` block, no `ontology.ttl`.
`audit_cdif_vocabulary.py` produces the annotatable inventory an ontology would be written from,
and its outputs are gitignored like `ig_audit.*`. Authoring that ontology is **not scheduled work**.

**Implementation-guide consistency — the annotate / implement / re-run loop:**

```bash
python tools/audit_ig_consistency.py --self-test         # run FIRST: proves each check still fires
python tools/audit_ig_consistency.py -o ig_audit.json    # findings, each with an empty "fix" field
#   a reviewer writes into "fix" on the rows they have decided; implement those; then
python tools/audit_ig_consistency.py -o ig_audit.json    # re-run: annotations CARRY FORWARD
```

Fixes are matched on `(check, guide, property)`, never on `line` — line numbers move as soon as
anything above them is edited. The run prints how many carried and how many no longer have a
finding; the second number is the useful one. **The register is at 0 findings as of 2026-09-27**
(from 108), so a non-zero result means something new drifted. `ig_audit.json`, `ig_audit.md` and
`ig_audit.*.json` are gitignored.

A mismatch tells you the guide and the schema disagree, **not which is wrong.** Three of the
cardinality findings settled in that pass were fixed on the *schema* side.

**The authoritative check is the OGC postprocessor, not the local tools** — it runs JSON Schema,
then JSON-LD uplift, then SHACL. `validate_examples.py` covers only the first step, and
`validate_shacl.py` rebuilds the rule bundle from the `$ref` graph rather than the postprocessor's,
so it can disagree. Reproduce CI locally with Docker:

```bash
./build.sh                               # full validate + build, writes build/ and register.json
./view.sh                                # bblocks-viewer at http://localhost:9090
```

## Architecture

**One source of truth, two generated layers.** `schema.yaml` is authoritative. From it:
`resolvedSchema.json` (standalone, external `$ref`s resolved into `$defs` + internal refs, recursive
types left as cycles) and `<dirname>Schema.json` (a JSON mirror with `$ref` extensions rewritten).
CI then generates `build/` via the OGC postprocessor. Editing a `schema.yaml` without regenerating
leaves the change in the source and in nothing that validates against it — the
`check-schema-drift.yml` workflow fails on exactly that, on push to `main` as well as PRs.

**The drift check is incremental on a PR and exhaustive on `main`, and that split is the design.**
Since 2026-09-28 a pull request regenerates only the reverse-`$ref` closure of its change set
(`tools/affected_blocks.py`) — 4 blocks and 4.5 s for a `xasFacility` edit, against ~11 min. It is
sound because a block's output depends only on its own `$ref` closure, which is a property of
`resolve_schema.py` that was measured rather than assumed, and could stop being true. **The
unconditional `--all` on push to `main` is what would catch that, so do not make `main`
incremental as well** — and note what a green incremental run does *not* claim: a stale artifact in
a block the change set cannot reach was never regenerated on that run. The saving also varies
hugely with position in the graph (`xasFacility` 4% of `--all`, `skosConcept` 65%), so a hub edit
buys almost nothing. `regenerate_schema_json.py` stays full everywhere: 93 blocks in ~1.3 s.

**Building block trees** under `_sources/`: `schemaorgProperties/`, `cdifDataType/`,
`ddiProperties/` (canonical DDI-CDI), `provProperties/`, `skosProperties/`, `xasProperties/`,
`bioschemasProperties/`, `qualityProperties/`. Profiles are split in two:
`profiles/cdifProfile/` holds **modules** (each adds one slice, e.g. `cdifCore`, `cdifDiscovery`,
`cdifProvenance`); `profiles/cdifCompositeProfile/` holds **composites** that are thin `allOf`s over
modules (`CoreDiscovery`, `cdifComplete`, `xasDocument`, …).

**Composition rules** (violating these is the usual cause of a confusing validation error):
- **Composites** (`profiles/cdifCompositeProfile/`) are pure `allOf` of module `$ref`s, with no
  inline properties. Measured 2026-09-11: true of all five.
- **Modules** (`profiles/cdifProfile/`) are *not* — every one carries inline properties
  (`cdifCore` 27, `cdifDiscovery` 7), and `cdifCodelist` and `cdifConceptScheme` are fully
  self-contained, with no external `$ref` at all. Those two are building blocks that happen to
  live under `profiles/`. The older blanket claim that "profiles are pure `allOf` of BB `$ref`s"
  describes composites only; do not read it as a rule modules are breaking.
- A BB may therefore reference a module's schema, and two do: `cdifEnumerationDomain` →
  `cdifCodelist`, and (until 2026-09-11) `cdifConceptOrTerm` → `cdifConceptScheme`, now repointed
  at the canonical `skosProperties/skosConcept`. Note that swap **tightened** validation —
  `skosConcept`'s `Concept` requires `skos:definition` and `skos:inScheme`, the profile's
  `cdifConcept` required neither.
- **Two link blocks, with a clean division.** `schemaorgProperties/labeledLink` is **a work at a
  URL** — a licence, a terms-of-service document, a manual; the value *is* the thing pointed at,
  and it optionally carries `dcat:hadRole`/`dcterms:relation`.
  `schemaorgProperties/linkRole` is **a typed relationship to a target** —
  `schema:linkRelationship` names the relation, `schema:target` is a `schema:EntryPoint`. The test
  is whether the relationship carries information: a licence needs no role, a related resource is
  meaningless without one. `cdifDataType/cdifReference` was folded into `labeledLink` on
  2026-09-23 (it added two optional properties and nothing else) and is in `archive/`; `linkRole`
  was inline in `cdifCore` until the same date, which is why `instrument` had defined
  `schema:relatedLink` with a different shape. `ddiProperties` keeps its own canonical
  `dt-Reference` and is not part of this.
- A BB schema is a single node, no `@graph` wrapper. Class targets default to
  `anyOf [inline class, {@id} reference]`, and a reference is **sealed**
  (`additionalProperties: false`, `required: ['@id']`).
- Item-level BBs (a provenance activity, an archive distribution item) need a **wrapper BB** to
  supply the root property — otherwise their constraints land on the root object.

**`cdi:` vs `cdif:`** — `cdi:` is reserved for properties whose value types match the canonical
DDI-CDI XMI. Any CDIF simplification or divergence is renamed to `cdif:` so it is namespace-visible.
Check with `tools/audit_cdif_vs_ddi.py`.

**`schema` binds to `http://schema.org/`, not https** — `https://schema.org/Dataset` is a different
IRI that denotes nothing here.

**Domain repos** (`usgin/{dde,ecrr,geochem}BuildingBlocks`) reference this repo's blocks by absolute
`https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/...` URL,
and receive shared tools via `tools/sync_resolve_schema.py`. A rename here silently breaks them —
their refs are resolved over the network at their build time, not ours.

## Traps

- **Regeneration is slow.** `resolve_schema.py --all` is ~11 min and `validate_examples.py` ~10 min.
  Run them in the background; don't chain both in one foreground command.
- **An unresolvable `$ref` is fatal and nothing is written.** Use `--allow-unresolved` only to
  inspect damage in a repo whose refs are already broken.
- **Windows hides case bugs.** A `$ref` whose case doesn't match the file resolves here and 404s on
  Linux, and the generator will overwrite a differently-cased tracked file in place while reporting
  "unchanged". Test filename case against `git ls-files` (which stores exact case), and existence
  with an explicit case-sensitive check — `Path.exists()` will lie.
- **CI auto-commits `build/` after every push** ("Building blocks postprocessing", "Generate JSON
  Forms schemas"), so `origin/main` moves on its own. Always `git fetch` and rebase before a
  follow-up push.
- **Stage explicit paths, not `-A`.** Tracked-but-transient files at the root (`redirectTest.txt`,
  `output.json`, `expanded.ttl`) show as modified constantly; `audit_full.txt`, `audit_check.txt`
  and `resolve_run.log` are untracked tool output. None of them should ride along in a commit.
- **Commit regenerated artifacts separately** from unrelated changes. When a regeneration sweeps up
  pre-existing drift, split it: revert your source edit, regenerate, commit the catch-up alone, then
  restore and commit your actual change.
- **The JSON Schema gate is now clean: `validate_examples.py` should report 152 passed, 0 failed.**
  A failure means you broke something — this is no longer a run with expected noise to squint past.
  The count tracks the corpus, so treat it as "0 failed" rather than a fixed number: it was 152 before 2026-09-05, 150 after, and 152 again as of 2026-09-25. `cdifDataType/cdifLongData` was retired on 2026-09-05, taking its two examples with it: nothing referenced it and its `cdif:isStructuredBy` was drift for `cdi:isStructuredBy`. The five long-failing `ddicdi*` examples were retired to `archive/` on 2026-09-02 (synthetic
  fixtures never referenced by their own `examples.yaml`, so nothing was validating them into
  conformance), and `ddicdiDataStructure` / `ddicdiRepresentedVariable` got fresh, validating
  replacements.
- **An `example*.json` must be referenced from its block's `examples.yaml`**, as
  `snippets: [{language: json, ref: <file>}]` — that is what the OGC postprocessor publishes and
  validates. `validate_examples.py` finds examples by globbing `example*.json`, so an unreferenced
  file still passes locally while being invisible to CI and to the published block. Every block now
  wires its examples and **no `TODO: replace with a JSON-LD example` placeholder remains**; keep it
  that way when adding a block.
- **SHACL severity is not uniform, and the JSON Schema twin of a rule may be stricter.**
  "A record must declare conformance to <profile>" is `sh:Warning` — SHACL cannot tell
  whether a record meets a profile, so it does not fail one for not saying it does. The
  structural half (a `conformsTo` is present and is an IRI) is `cdifd:metadataConformsToPresent`
  and stays a Violation. The JSON Schema `contains` for the same constraint is still a hard
  failure, because JSON Schema has no advisory severity.
- **A JSON Forms `defaults.json` is the only source of its records' conformance, and nothing
  checks it.** `convert_for_jsonforms.py` copies `defaults.json` and `uischema.json` into `build/`
  verbatim — no generator. Most of a defaults file exists to give form controls a shape to bind to
  (`"schema:name": ""`, empty arrays), so it is deliberately not a valid record. But neither
  uischema exposes `schema:subjectOf`'s `dcterms:conformsTo` or its `schema:additionalType`, so an
  author can never reach them, and the generated form schema drops the `contains` constraint (JSON
  Forms does not support it). Whatever the file says ships unedited and unflagged. Both files were
  wrong until 2026-09-04: three different stale URI forms between them, one referencing a `cdif:`
  prefix its own `@context` never declared, and neither carrying
  `schema:additionalType: dcat:CatalogRecord` — without which `ConformanceValidate.extract_conforms_to`
  skips the node and reads the record as declaring nothing. Both now default to `core/1.1`, the one
  profile `cdifCore` requires by a hard `contains` and the most a blank record can honestly claim.

- **A profile-conformance advisory belongs in `conformance.shacl`, not `rules.shacl`.**
  `rules.shacl` travels with the `$ref` graph, which is right for structural shapes — a
  codelist's required properties apply wherever a codelist appears. It is wrong for "your
  catalog record should declare *this* profile", which is true of one profile only.
  `cdifEnumerationDomain` references `cdifCodelist`, so `CDIFCodelistConformsToShape` was landing
  in the `data_description` and `data_structure` bundles, advising records about a profile they
  were not using. `validate_shacl.py` now also collects `conformance.shacl` **from the target
  block only**, never through the graph (`gather_conformance_file`). `cdifCodelist` and
  `cdifConceptScheme` use it. The equivalents in `cdifCore`, `cdifManifest`, `cdifProvenance` and
  `cdifDataDescription` have not been migrated — `cdifCore`'s in particular cannot simply move,
  because `metadataProfileProperty` is referenced by a NodeShape in the same file and splitting it
  would leave a dangling reference in every consumer's bundle.

- **Whether a `conformsTo` is *correct* is checked in `CDIF/validation`, not here.**
  `detect_conformance` derives conformance from content; `ConformanceValidate` and
  `FrameAndValidate -v` compare it against what the record declares and **fail an
  over-claim**. Only the six detectable profiles are compared, and both halves are read
  from the source document — framing drops evidence below `schema:distribution`.
- **`ddiProperties` examples use the canonical DDI-CDI datatypes, not CDIF's simplifications** —
  `cdi:name` is an `ObjectName` (`{@type, cdi:name}`), `cdi:definition` an `InternationalString`
  wrapping a `LanguageString`, `cdi:encoding`/`cdi:physicalDataType` a `ControlledVocabularyEntry`.
  Arity is per-block, not per-property: `cdi:name` is an array on most blocks but a single object on
  `TabularTextDataSet`. Union blocks pick a branch by `@type` and the branches differ in more than
  the type — `cdi:isStructuredBy` is on `WideDataSet` while a `TabularTextDataSet` uses
  `cdi:correspondsTo`, and an abstract type such as `cdi:DataStructureComponent` is never a valid
  choice. Check the target `$defs` rather than copying a sibling example.

- **A negative test that fails for the wrong reason asserts nothing.** The OGC layout puts
  `tests/*-fail.json` beside each block, meaning "this must NOT validate". `tools/test_fail_cases.py`
  (added 2026-09-11) checks *why* each one fails, not just that it does. **This has since been
  fixed and must stay fixed: as of 2026-09-25 it reports 125 of 125 cases failing on the
  constraint their filename names, 0 asserting nothing, 0 byte-identical copies.** It was far
  worse when the tool was written -- 34 cases of which only 5 asserted their own constraint, 20
  byte-identical copies (`affiliation-fail.json` appeared verbatim in eight blocks, including
  `spatialExtent` and `xasDocument`, where affiliation means nothing), and 70 of 93 blocks with no
  `tests/` at all. **23 of 93 blocks still have none.** Run it with `--strict` to fail on a case
  that asserts nothing, `--coverage` to list untested blocks. Note the matcher's own limits: an error on `@type` and an
  `anyOf` message (which prints the whole instance, so every token "matches") are both
  discounted, while the error *path* counts as strong evidence.

- **A rule that stops working looks exactly like a rule that passes.** This is the failure mode
  that cost the most time on 2026-09-08, in five different disguises. `sh:targetObjectsOf` on a
  property that was renamed matches nothing and reports zero violations. A SPARQL target selecting
  `schema:additionalType "dcat:CatalogRecord"` as a **string literal** stopped matching the moment
  records switched to `{"@id": …}`, silently retiring the advisory that used it. An `if:
  required: [schema:variableMeasured]` guard is *always* true, because `cdifDataDescription`
  requires that property unconditionally — so a "conditional" pin was mandatory for every record.
  A frame sub-frame that names an inner property is a **match filter**, so a component lacking it
  was discarded and three data-structure components became one, with no warning. And
  `sync_frameandvalidate.py`'s regression gate reported "N examples ok" when *no* example passed
  under either side, so nothing could regress. When you change a property name, a marker's
  serialization, or a frame, grep for every rule that mentions it and prove the rule still fires on
  a case it should reject — a green result from an unfired rule is the default, not the exception.

- **A `const` on a compact IRI only works if the *output context* declares that prefix.** The
  schema and the context are different artifacts and nothing checks them against each other.
  `xasInstrument` pins `{"@id": {"const": "wd:Q3099911"}}`, and the profiles validate the **framed**
  document; the xasDocument frame did not declare `wd`, so framing expanded the value to
  `https://www.wikidata.org/entity/Q3099911` and could not compact it back. Every emitted document
  failed once per instrument on a value it carried correctly. Fixed by declaring `wd` in the frame,
  but prefer matching the full IRI when writing a new one.

- **`validate_examples.py` checks the raw example; `FrameAndValidate` checks the framed tree.**
  The collapse happens in between, so this repo can report a clean 150/150 while every downstream
  release example is broken. `ARRAY_PROPERTIES` in `validation/tools/FrameAndValidate.py` exists to
  restore what compaction flattens; `cdif:name`, `schema:instrument`, an instrument's
  `schema:identifier` and a DefinedTerm's `schema:about` were all added there on 2026-09-08 after
  documents failed schemas they actually satisfied. A property that is an array in the schema and a
  scalar after framing belongs in that list — but it is keyed on name alone, so a property that is
  an array in one place and a scalar in another (`schema:identifier` on an instrument vs on a
  Person) has to be keyed on `parent_key` or `type_list` instead.

- **Renaming a property breaks emitters, not just schemas.** `cdif:isDefinedBy_RepresentedVariable`
  → `cdif:isDefinedBy_Variable` reached the release SHACL the same day and `cdifnexmetadata` did
  not, so every document it produced failed a rule that had not existed that morning — and its own
  test suite stayed green because a test asserted the old key. Downstream *writers* are as exposed
  as downstream *readers*; check `CDIF/cdifnexmetadata` and the converters under
  `validation/converters/` alongside the profile repos.

- **Deleting a block from a `schema.yaml` by cutting to end-of-file will take `$defs` with it.**
  `$defs` is conventionally last. `resolve_schema.py` refuses to write anything when a `$ref` goes
  unresolved, so the damage surfaces immediately rather than shipping — but a verification that
  only checks for what you meant to remove will not notice what else went. Cut by explicit line
  boundaries and diff the top-level keys before and after.

- **Release repos: `main` is the current release, and it is protected.** Since 2026-09-10 each
  `profile-*` / `doc-*` repo serves GitHub Pages from `main`, work happens on an `updates`
  branch, and `main` only advances by pull request (PR required, `enforce_admins: true` — with
  admins excluded the protection is decorative, since an admin just pushes past it). So the
  **merge is the release**: Pages republishes at merge time, before the tag exists. Local clones
  are on `updates`, and `tools/sync_release_repos.py --apply` writes into whichever branch is
  checked out — check first. The old `reviewRevision202606` branches are now `archive202609`.
  `profile-provenance` is the exception: still in review, untagged, still on the old branch with
  Pages sourced from it.

- **A versioned conformance URI points at Pages only while that version is current.** Pages
  serves `main`, and `main` is always the newest release — so when a newer minor version ships,
  the outgoing version's `w3id` rules must be repointed to its release tag. Miss it and
  `core/1.1/schema` silently serves 1.2: no build fails, because a 1.2 schema is a perfectly
  valid schema. `raw.githubusercontent.com` serves `text/plain`, which was measured harmless for
  every consumer CDIF has (the JSON Schema and SHACL loaders name the format rather than sniffing,
  and records carry an inline `@context`) — so **do not "fix" a tag-pointing rule back to Pages**.
  Rules live in a fork of `perma-id/w3id.org` and reach production by PR on that project's
  schedule. **Upstream moved every rule directory under `ids/` on 2026-09-04**, so a PR must
  target `ids/cdif/`; a fork that has not synced still shows the old top-level `cdif/`, and a
  PR against that path re-creates a directory upstream deleted while leaving the live rules
  untouched. The checklist is in `w3id.org/ids/cdif/CLAUDE.md` and the guard is
  `validation/tools/check_w3id_redirects.py` (weekly workflow). Two details that are easy to
  get wrong: repoint to the **last** patch tag of the outgoing series (`v1.1.1`, not `v1.1.0`
  — the first one archives a spec nobody shipped), and a *patch* release requires no
  `.htaccess` edit at all, because every release-repo rule targets a Pages base and Pages
  serves `main`.

- **The CDIF book pins its artifact links to release tags, so every patch release leaves them a
  version behind.** Pinning is deliberate — a reader gets the spec the prose was written
  against — and it is why the pins need a guard: a stale tag does not 404, it serves a
  correct-looking page for a superseded release, and the book's own build cannot notice
  because every link still resolves. `check_w3id_redirects.py` also scans cdifbook's source
  tarball (every tracked file, so a link in a new chapter is covered the day it lands) and
  reports `STALE`, or `MIXED` when a sweep was only partly applied. The 2026-09-10 v1.1.1 sweep
  moved 82 links across 11 files.

- **A key names variables by reference only, and there is one key class.** Settled 2026-09-25.
  `cdi:indexes` is an `objectReference` (sealed `{@id}`) at all three CDIF sites -- `cdifKey`, and
  `ForeignKey` / `PrimaryKey` in `cdifDataStructure` -- because a key's variables are declared once
  in `schema:variableMeasured` and referenced from each `cdi:ComponentPosition`. An inline variable
  there was a second copy of an existing node, and framing's embedded copy could not be told apart
  from authored content. That uniformity is what makes `cdi:indexes` safe in
  `FrameAndValidate.REFERENCE_ONLY_KEYS`, which matches on **property name alone**: all 14
  definitions of the name now permit a bare reference (the eleven canonical `ddiProperties` ones
  via `ddicdiDataTypes#/$defs/id-reference`, which is exactly `{@id}`). Narrow any new
  `cdi:indexes` the same way or that collapse starts destroying data.
  `$defs/PrimaryKey` in `cdifDataStructure` is now a `$ref` to `cdifKey`: the two were structurally
  identical apart from the type token and a `cdi:value` minimum, and **`cdif:PrimaryKey` no longer
  exists as a class** -- nodes are `cdif:Key`, so a dataset-level and a structure-level key can be
  one node referenced twice. `cdifKey` is the survivor because five `ddiProperties` blocks `$ref`
  it. `cdif:ForeignKey` stays separate: `cdif:references` is a real difference, and it is now
  required, as are `cdi:indexes` and `cdi:value` on its wrappers (until 2026-09-25 only `@type`
  was, so a wrapper naming no variable and no position validated). `cdi:value` is `minimum: 1,
  default: 1` everywhere; the "0- or 1-based" latitude `cdifKey` used to document was never
  accepted by either structure-level definition.
  The properties are `cdif:has_PrimaryKey` / `cdif:has_ForeignKey`, **not** `cdi:`, by the
  namespace rule at the top of this file -- their values diverge from the DDI-CDI XMI. The
  canonical `cdi:has_*` in `ddiProperties` are correct as they stand.

- **A guide is checked against its COMPOSITE, not its module — and `contains` is walked.** Both
  landed in `audit_ig_consistency.py` on 2026-09-26. A release guide describes a conforming
  record, so `profile-datastructure` legitimately documents the catalog record even though
  `schema:about`, `schema:sdDatePublished` and `schema:encodingFormat` come from `cdifCore` and
  `dataDownload`; judging it against `cdifDataStructure` alone reported three phantom
  "undeclared" and one phantom "never requires it". Measured: a record whose catalog record omits
  `schema:about` **fails the composite and passes the module.** Each module resolves against the
  narrowest composite containing it, derived from the composites' own `allOf`.
  That change then exposed an older hole: **`contains` was never walked**, though it appears in
  76 schema files — every `@type` token check is one. It hid because a *root* schema's `$defs` are
  enumerated directly, so anything reachable only through `contains` was indexed anyway while
  that file was the root, and vanished the moment it became a `$ref` target. Adding composite
  resolution alone made `cdi:isStructuredBy` look *not* required — inverting the finding it was
  meant to clear. If you add an applicator keyword to a schema here, check the walker handles it;
  `contains` is the only one this register uses beyond `allOf`/`anyOf`/`oneOf`/`if`/`items`.

- **A SHACL target selected by the property under test cannot fail.** `xasFacility`'s shape
  targeted Places *by* their `schema:additionalType`, then asserted that same property — so every
  node reaching the constraint already satisfied it. Measured 2026-09-27: a facility with
  `schema:additionalType` removed entirely conformed with **zero violations**, because it was
  never selected. The fix is a second shape whose target establishes context *without reading the
  property under test* — `cdifd:xasAnalysisLocationClassified` selects Places reached as the
  `schema:location` of an activity classified `xas:analysisevent`. When you write a shape, ask
  what instance it is supposed to reject and check that it does; a target that names the
  constraint's own property makes the rule decorative.

- **The four retired XAS terms accept BOTH spellings, on purpose.** `xas:beamline`,
  `xas:xraysourcetype`, `xas:probe` and `xas:temperature` were retired onto NeXus base classes on
  2026-09-27 (`nxs:` = `https://manual.nexusformat.org/classes/`), and seven constraint sites are
  an `enum` of the NeXus form plus the old one. A hard swap would have broken 73 files in
  `cdifnexmetadata` — including `emit.py` and the concept maps of a package on PyPI — and 68 in
  `XAS-CDIF`, while `cdifnexmetadata`'s own tests stayed green because they assert the old tokens.
  The `xas:` alternatives can only come out once those two emit the NeXus form. **`xas:facility`
  was deliberately NOT retired**: it covers a synchrotron, an XFEL *or a laboratory* facility,
  while `NXsource` is the storage ring — the narrower `xas:synchrotonfacility` is what corresponds
  to `NXsource`, and the glossary now records it as `skos:narrower`. Do not "finish the job" by
  mapping `xas:facility` onto `NXsource`.

- **`resolve_schema.py` is the canonical copy the domain repos receive, and the geochem fork has
  diverged in BOTH directions.** A wholesale sync either way breaks something: geochem's copy
  carries `bb_locate` (which resolves names under a `techniqueProfile/` layout this repo does not
  have, so `resolve_schema.py <blockName>` raises `ModuleNotFoundError`) and a `vendor/remote/`
  pinning mechanism that is inert here, since no source declares a URL `$ref` — the drift workflow
  depends on that being true. Meanwhile this copy has the unresolved-ref reporting that geochem
  merged *from* here. Cherry-pick per feature. `prune_noop_allof` came across that way on
  2026-09-27 and is worth **36 bytes** in this register — one husk in
  `xasGeneratedBy/resolvedSchema.json` out of 8.7 MB — because its motivating case, `adaProduct`,
  is a geochem block. It is carried for de-divergence, not for size.

- **`generate_shacl_shapes.py` output depends on your checkout's line endings, and the symptom
  points at the wrong culprit.** A Windows working copy has CRLF in 39 of 81 `rules.shacl` files
  (`core.autocrlf=true` overriding the repo's own `* text=auto eol=lf`), which puts CR *inside* the
  SPARQL string literals of `sh:select`. rdflib keeps those CRs in the literal **value** and
  re-emits them escaped, so a regenerated bundle differed from the committed one by 120-162 lines
  per file with no semantic change. In a diff those look like line-ending noise, and "fixing" the
  output encoding changes nothing -- `cat -A` is what distinguishes a real CR (`^M`) from the
  two-character escape rdflib writes. Every committed `rules.shacl` blob is pure LF; only working
  copies differ. Fixed 2026-09-25 by normalizing CR on read, so output no longer depends on the
  consumer's git config; the same commit stopped the header stamping `--bb-dir` verbatim (it could
  bake a local absolute path into a committed artifact) and pinned the output to LF. Before
  trusting a regenerated bundle, check the per-file diff is single digits, not three.

- **An `@id` that is not a usable IRI silently deletes the triple, and the JSON Schema gate
  cannot see it.** Settled 2026-10-01 in `profile-provenance`. Galaxy writes RO-Crate `@id`s
  containing spaces and pipes (`#input-Sn Foil`, `output-plot_collection|0_flat`); a JSON-LD
  parser cannot resolve those, so it drops the node **and the incoming triple with it**. In
  `Paper_1_Pt3Sn.actions.cdifprov.json` 28 `prov:used` keys became **6 subjects** in the graph,
  so 22 activities that do name their inputs looked like activities naming none, and the
  `cdifProvActivity` `minCount` fired on all of them. 170 spaces and 31 pipes across 96 distinct
  `@id`s in 6 files. The loss happens *after* the JSON Schema gate, during RDF expansion, which
  is why the corpus reported a clean 17/17 schema run while 12 examples failed conformance --
  the same split as `validate_examples.py` vs `FrameAndValidate`, one layer down. Percent-encode,
  and encode definitions and references alike: doing one side breaks the join instead. The check
  that catches it is graph-level -- parse the example and compare the triple count for a property
  against the number of keys in the JSON; equal counts are the invariant.

- **An over-claimed profile is not always a wrong declaration.** `detect_conformance` declares a
  class iff presence AND its content SHACL raises no Violation, so a *content* defect reports as
  `DECLARED BUT NOT DETECTED: <profile>` -- the identical message a genuinely false claim gives.
  Measured 2026-10-01: 12 of `profile-provenance`'s 17 examples over-claimed `provenance/1.1`
  while declaring it **correctly**; presence was true in all 12 and one `prov:used` Violation was
  suppressing the class. Run the detection with `verbose=True` and read which half failed before
  touching a `conformsTo` -- `presence False` is a declaration problem, `presence True` then
  `-> N SHACL violation(s)` is a content problem, and "fixing" the declaration there deletes a
  true claim to silence a real defect. The same pass found the cause was a modelling error rather
  than a missing value: both Galaxy converters swept `{CreateAction, OrganizeAction}` into the
  activity list, making "Run of Galaxy workflow engine" an object of `prov:wasGeneratedBy`, which
  no crate says -- across all eight, the root's `mentions` names the `CreateAction` every time and
  the `OrganizeAction` never. **Do not satisfy that rule by giving the engine run a `prov:used`**;
  it has no `object` and no `result` to map, so the only available value is its own
  `schema:instrument` restated as an input.

- **`raw.githubusercontent.com` is Fastly-cached, so a consumer's drift check can fail on content
  that is already correct.** The `check-frameandvalidate` workflow in each release repo curls the
  normative `FrameAndValidate.py` from `validation/main` over raw, and on 2026-10-01 three
  consecutive runs across six minutes read the superseded blob while a local curl of the same URL
  returned the new one -- a stale POP, with origin and every local copy byte-identical (`diff`
  over the canonical bodies: 0 lines). **Push `validation` BEFORE the repos that are synced from
  it**, or every consumer goes red for a cache window; and when it does go red, diff the bodies
  before touching anything, because the error message names hand-editing as the cause and it is
  the one cause that has never been it yet.
