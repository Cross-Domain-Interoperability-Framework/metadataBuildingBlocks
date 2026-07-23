# cdif_dds_framed.jsonld — updates from the UKDS reference

Log of substantive changes applied to `cdif_dds_framed.jsonld` when adapting
the UKDS reference file at
<https://github.com/UKDSResearch/cdif-xas/blob/main/resources/cdif_dds_framed.jsonld>
to validate against the current CDIF XASdata composite profile
(cdifCore/1.1 + cdifDiscovery/1.1 + cdifDataDescription/1.1 +
cdifDataStructure/1.1 + xasCore/1.0 + xasOptional/1.0).

Grouped by cause. Line numbers refer to the mBB copy of the file.


## 1. `@context` — authoritative XAS glossary base moved to w3id

- Upstream: `"xas": "https://ada.astromat.org/metadata/xas/"`
- Now:      `"xas": "https://w3id.org/cdif/xas/"`

The XAS SKOS glossary is the authoritative concept URI source. Its permanent
IRI base is <https://w3id.org/cdif/xas/> (a w3id PURL that resolves to
<https://smrgeoinfo.github.io/XAS-CDIF/>). Every `xas:*` local name below
follows the v2 glossary naming convention: lowercase, no spaces, no
underscores, no other punctuation.


## 2. Concept URI renames (v1 → v2 glossary local names)

All references to XAS glossary concepts were normalized. Local names lost
spaces, underscores, and mixed case:

| Upstream local name              | Current local name           |
|----------------------------------|------------------------------|
| `xas:mono energy`                | `xas:monochromatorenergy`    |
| `xas:monitor intensity`          | `xas:incidentintensity`      |
| `xas:transmission intensity`     | `xas:transmittedintensity`   |
| `xas:edge_energy`                | `xas:edgeenergy`             |
| `xas:d_spacing`                  | `xas:dspacing`               |
| `xas:harmonic_rejection`         | `xas:harmonicrejection`      |
| `xas:I0`                         | `xas:detectori0`             |
| `xas:I1`                         | `xas:detectorit`             |

`xas:time`, `xas:collimation`, `xas:focusing`, `xas:probe` were retained
verbatim (already conform to the naming convention).


## 3. JSON-LD IRI-reference serialization policy

CDIF profiles now enforce a semantic-clarity rule: any value on
`schema:propertyID` or `schema:additionalType` whose lexical form matches a
URI or CURIE (`scheme:localname`) MUST be serialized as a JSON-LD IRI
reference — `{"@id": "..."}` — rather than a plain string literal. Free-label
strings ("Selenium", "APS", "Author") remain valid as strings.

Applied throughout the file. Notable examples:

- Every `schema:propertyID` entry on `schema:variableMeasured` and on
  `schema:additionalProperty` is now an `{"@id": "..."}` object.
- `schema:subjectOf.schema:additionalType` catalog-record marker:
  `"dcat:CatalogRecord"` → `{"@id": "dcat:CatalogRecord"}`.
- Every instrument `schema:additionalType` XAS classification is
  `{"@id": "xas:..."}`.

The policy is enforced by SHACL shapes
`cdifd:PropertyIDUriShouldBeIRIShape` and
`cdifd:AdditionalTypeUriShouldBeIRIShape` in
`_sources/schemaorgProperties/additionalProperty/rules.shacl`.


## 4. `schema:subjectOf.dcterms:conformsTo` — declare XAS profile conformance

Upstream declared conformance only to the four base CDIF 1.1 profiles.
Added:

- `https://w3id.org/cdif/xasCore/1.0`
- `https://w3id.org/cdif/xasOptional/1.0`

These are what make the file exercise the XAS extension. Without them the
XAS-specific `additionalType`, `propertyID`, and instrument enumerations do
not participate in the profile-fitness contract.


## 5. `schema:keywords` — enriched DefinedTerm entries

- The K-edge entry gained `"schema:about": "element.edge"` — this is a
  local marker used by the mBB glossary tooling to signal the semantic
  slot the term fills (edge type vs. element symbol).
- The Selenium entry, which had only a `schema:termCode: "Se"`, now
  carries `schema:name: "Selenium"`, an authoritative
  `schema:identifier: "http://sweetontology.net/matrElement/Selenium"`,
  its `schema:inDefinedTermSet` set to
  `"http://sweetontology.net/matrElement"`, and
  `"schema:about": "element.symbol"`.
- The "Earth and Environmental Sciences" keyword, which upstream was a
  bare string, is now a full `schema:DefinedTerm` object with
  `schema:name` and
  `schema:inDefinedTermSet: "https://data.crossref.org/reports/schemes.html"`.


## 6. `prov:wasGeneratedBy` — restructured to the peer prov:used instrument model

### 6a. Activity typing + additionalType

- `@type` on the wasGeneratedBy activity: `[schema:Event, prov:Activity]`
  → `[schema:Action, prov:Activity]`. `schema:Action` is what current CDIF
  data-generation activities use.
- Added `schema:additionalType: [{"@id": "xas:analysisevent"}]` on the
  activity, per the xasGeneratedBy building block requirement.

### 6b. Activity-level additionalProperty (edge energy)

- Added `schema:name: "Edge energy"` (was absent).
- Added `schema:unitText: "eV"` (was absent).
- propertyID renamed as noted in §2.

### 6c. `prov:used` — one instrument per wrapper (was: single wrapper with array)

Upstream had **one** `prov:used` entry (`_:b17`) whose `schema:instrument`
was an **array** of three instrument descriptions (Beamline, Detector,
Monochromator).

Now: `prov:used` is an array with **one wrapper per instrument**, each
wrapper carrying a single `schema:instrument`. This is the peer prov:used
model established during the CDIF XAS profile revision — every instrument
is discoverable as its own prov:used entity, not as a sub-element of an
aggregate.

Four peer wrappers, in provenance order:

| # | Instrument (@id in file) | `schema:additionalType`   | Origin                             |
|---|--------------------------|---------------------------|------------------------------------|
| 1 | (blank node)             | `xas:source`              | **NEW** — was not present upstream |
| 2 | `_:b4`                   | `xas:beamline`            | reworked from upstream `_:b4`      |
| 3 | `_:b13`                  | `xas:xraymonochromator`   | reworked from upstream `_:b13`     |
| 4 | `_:b8`                   | `xas:xraymonitor`         | reworked from upstream `_:b8`      |

### 6d. New source-instrument entity

A dedicated wrapper for the APS bending-magnet X-ray source was added. It
carries `xas:xraysourcetype` = "Synchrotron X-ray Source" and
`xas:probe` = "x-ray". Motivation: the current xasCore profile requires
that the X-ray source be reported as its own instrument, not folded into
the beamline description.

### 6e. Per-instrument changes

**Beamline** (`_:b4`, `xas:Beamline/13-BM-D`):

- Added `@type: [schema:Thing, schema:Product]`.
- Added `schema:additionalType: [{"@id": "xas:beamline"}]`.
- `schema:name`: `"Beamline/13-BM-D"` → `"13-BM-D"` (the identifier already
  provides the beamline prefix).
- Property "harmonic_rejection" → "harmonic rejection"
  (`xas:harmonicrejection`).

**Monochromator** (`_:b13`, `xas:Mono/Si 111`):

- Added `@type: [schema:Thing, schema:Product]`.
- Added `schema:additionalType: [{"@id": "xas:xraymonochromator"}]`.
- `schema:name`: `"Mono/Si 111"` → `"Si 111"`.
- Existing d-spacing property: `schema:name` `"d_spacing"` → `"d-spacing"`,
  propertyID renamed (§2), unit `Angstrom` added.
- Added two new additionalProperty entries required by xasCore:
  - `"crystal type"` with propertyID `xas:monochromatortype` = `"Si"`.
  - `"reflection plane"` with propertyID `xas:reflectionplane`
    = `"1,1,1"`.

**X-ray monitor / detectors** (`_:b8`, `xas:Detector`):

- Added `@type: [schema:Thing, schema:Product]`.
- Added `schema:additionalType: [{"@id": "xas:xraymonitor"}]`.
- `schema:name`: `"Detector"` → `"x-ray intensity monitor"`.
- Existing detector properties renamed for semantic clarity:
  - `"I0"` → `"incident-flux detection method"`
    (propertyID `xas:detectori0`).
  - `"I1"` → `"transmitted-flux detection method"`
    (propertyID `xas:detectorit`).


## 7. `schema:subjectOf` — catalog-record completeness

The `ex:dataset/DV/BYSPHH/metadata` catalog record inside `schema:subjectOf`
now carries its own descriptive metadata, distinct from the outer dataset
(a catalog record IS metadata about the dataset — it needs its own name,
identifier, license, etc.). Added:

- `schema:name`: `"CDIF metadata catalog record for Se_Na2SeO4_rt_01 (DV/BYSPHH)"`
- `schema:identifier`: `"http://localhost:8080/api/dataset/DV/BYSPHH/metadata"`
- `schema:dateModified`: `"2026-06-24"`
- `schema:license`: `["https://creativecommons.org/licenses/by/4.0/"]`
  (CDIF metadata is CC-BY-4.0 by project standard, distinct from the CC0
  license on the payload data)
- `schema:url`: `"http://localhost:8080/dataset.xhtml?persistentId=perma:DV/BYSPHH"`

Deirdre should replace the placeholder `http://localhost:8080/...` URIs
with the real Dataverse endpoints when this is regenerated from the
production installation.


## Notes on validation state

- **JSON Schema** (against `resolvedSchema.json` for XASdata composite):
  passes with 0 errors.
- **SHACL** (all rules bundled by the XASdata composite): 0 violations
  on `cdif_dds_framed.jsonld`. The remaining 18 warnings and 4 info
  results are standard schema.org catalog-record advisories (informational
  only, not fitness failures).
