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
- **`_sources/ddiProperties/ddicdi*/example*.json` are not in use.** Several fail validation and are
  not worth conforming — judge a validation run by *which* examples fail, not the total.
