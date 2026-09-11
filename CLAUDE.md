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

**Validation:**

```bash
python tools/validate_examples.py                        # JSON Schema gate, all examples (~10 min)
python tools/validate_examples.py -f spatialExtent       # single block / substring filter
python tools/validate_shacl.py <profile-name> --strict   # opt-in SHACL, one target
python tools/audit_building_blocks.py                    # files, freshness, examples, SHACL coverage
python tools/audit_building_blocks.py -c type-enum       # @type enum vs the SHACL list restating it
```

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

**Building block trees** under `_sources/`: `schemaorgProperties/`, `cdifDataType/`,
`ddiProperties/` (canonical DDI-CDI), `provProperties/`, `skosProperties/`, `xasProperties/`,
`bioschemasProperties/`, `qualityProperties/`. Profiles are split in two:
`profiles/cdifProfile/` holds **modules** (each adds one slice, e.g. `cdifCore`, `cdifDiscovery`,
`cdifProvenance`); `profiles/cdifCompositeProfile/` holds **composites** that are thin `allOf`s over
modules (`CoreDiscovery`, `cdifComplete`, `xasDocument`, …).

**Composition rules** (violating these is the usual cause of a confusing validation error):
- Profiles are pure `allOf` of BB `$ref`s — no inline properties.
- BBs reference BBs; profiles never reference profiles; BBs never reference profiles.
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
- **The JSON Schema gate is now clean: `validate_examples.py` should report 150 passed, 0 failed.**
  A failure means you broke something — this is no longer a run with expected noise to squint past.
  `cdifDataType/cdifLongData` was retired on 2026-09-05, taking its two examples with it (152 -> 150): nothing referenced it and its `cdif:isStructuredBy` was drift for `cdi:isStructuredBy`. The five long-failing `ddicdi*` examples were retired to `archive/` on 2026-09-02 (synthetic
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
