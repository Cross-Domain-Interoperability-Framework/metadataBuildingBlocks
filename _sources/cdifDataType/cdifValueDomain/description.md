# CDIF Value Domain

A **CDIF Value Domain** describes the set of values a variable may take — either *substantive* (subject-matter values of interest) or *sentinel* (processing or missing-value codes like SAS `.R`, SPSS `999`, "not applicable", etc.).

This is a CDIF profile of the DDI-CDI `ValueDomain` family. A single node is **one of**:

- `cdif:SubstantiveValueDomain` — the real values a variable measures.
- `cdif:SentinelValueDomain` — codes that flag missing, refused, not-applicable, or otherwise non-substantive observations.

The schema discriminates the two via `@type` (a `oneOf` over the two `$defs`). The two branches carry
an identical property set, so the type token is the only thing that selects between them.

## Structure

Each subclass carries the same shape:

| Property | Type | Notes |
|---|---|---|
| `@type` | array | Required. Must contain `cdif:SubstantiveValueDomain` or `cdif:SentinelValueDomain` |
| `@id` | string | Optional IRI for the domain node |
| `cdif:takesValuesFrom` | anyOf | Inline [cdifEnumerationDomain](../cdifEnumerationDomain/) or `{@id}` reference. The *extensional* specification: the values are the members of a codelist |
| `cdi:isDescribedBy` | anyOf | Inline `cdi:ValueAndConceptDescription` (see below) or `{@id}` reference. The *intensional* specification: ranges, patterns, classification level, expressions |
| `cdif:displayLabel` | string | Short human-readable label (multilingual via repeat) |
| `cdif:recommendedDataType` | array | One or more `xsd:` type tokens (e.g. `xsd:decimal`, `xsd:date`) drawn from the enum in `$defs/xsdDataType` |

`@type` is required, plus **at least one of** `cdif:takesValuesFrom` or `cdif:recommendedDataType` — a value domain that pins neither an enumeration nor a recommended data type is not informative. Note that `cdi:isDescribedBy` does **not** satisfy that choice on its own.

### `cdi:ValueAndConceptDescription`

The target of `cdi:isDescribedBy`, defined in this block's `$defs`. `@type` (containing
`cdi:ValueAndConceptDescription`) is the only required property; all of the following are optional.

| Property | Type | Notes |
|---|---|---|
| `cdi:classificationLevel` | string | One of `Continuous`, `Interval`, `Nominal`, `Ordinal`, `Ratio` |
| `cdi:description` | string | Formal description of the value set in human-readable language |
| `cdif:formatPattern` | string | Unicode LDML number or date pattern, e.g. `#,##0.###` or `yyyy.MM.dd` |
| `cdif:logicalExpression` | string | Expression whose satisfying values are the valid ones |
| `cdi:minimumValueInclusive` | string | Lower bound, inclusive. Mutually exclusive with `cdi:minimumValueExclusive` |
| `cdi:minimumValueExclusive` | string | Lower bound, exclusive. Mutually exclusive with `cdi:minimumValueInclusive` |
| `cdi:maximumValueInclusive` | string | Upper bound, inclusive. Mutually exclusive with `cdi:maximumValueExclusive` |
| `cdi:maximumValueExclusive` | string | Upper bound, exclusive. Mutually exclusive with `cdi:maximumValueInclusive` |
| `cdif:regularExpression` | string | Regular expression matching the valid values |

The bounds are typed `string`, not number, following the wording of the W3C *Metadata Vocabulary for
Tabular Data* quoted in the schema.

An inclusive and an exclusive bound on the **same side** may not both be present. Tabular-metadata
5.11.2, the source of these four properties, treats stating both as an error: the pair states one
limit twice with nothing checking that the two agree. The JSON Schema refuses it for an inline
description — `$defs/ValueAndConceptDescription` carries an `if`/`not`/`then` per side — and
`rules.shacl` refuses it at `sh:Violation` (`cdifd:cdifValueAndConceptDescriptionBoundsShape`) for a
description supplied as an `{@id}` reference, which JSON Schema cannot follow. A `minimum` greater
than its `maximum` is deliberately **not** checked at either layer: the bounds are strings, so the
comparison would be lexical and would reject `"9"` against `"10"`.

## Combining the two specifications

`cdif:takesValuesFrom` and `cdi:isDescribedBy` may both be present. It is coherent when the
description carries **scale or annotation** properties — `cdi:classificationLevel` and
`cdi:description` — because an enumerated domain may still be ordinal, and the classification level
has nowhere else to live. A syntactic `cdif:formatPattern` or `cdif:regularExpression` alongside a
codelist is redundant but not contradictory; both are exempt from the advisory below on purpose,
since they constrain the *form* of a value rather than which values exist and so stay useful as a
check a consumer can apply without dereferencing the codelist.

It is *not* coherent when the description also **defines the value set** — the four bounds or
`cdif:logicalExpression` — because the codelist already does that, leaving two independent
specifications with nothing checking they agree. `rules.shacl` reports this at `sh:Warning`
(`cdifd:cdifValueDomainEnumerationRedundancyShape`) rather than as a violation: a record stating the
set twice is not invalid, and whether a given bound annotates an enumeration or redefines it is a
judgement SHACL cannot make.

A `cdi:classificationLevel` of `Continuous` together with `cdif:takesValuesFrom` is a contradiction
rather than a redundancy — a continuous scale has uncountably many values — and is an `sh:Violation`
(`cdifd:cdifValueDomainContinuousNotEnumerableShape`). `Ratio` and `Interval` are deliberately **not**
treated the same way, though an earlier draft of this page called them equally contradictory: both
are weaker claims, since a specimen count is ratio-scaled and a short codelist of counts is
defensible, and a codelist of calendar years is interval-scaled. They are left to the advisory
above, which fires on the bounds rather than on the classification.

Every check that spans the two properties lives in SHACL rather than the JSON Schema, because
`cdi:isDescribedBy` and `cdif:takesValuesFrom` both accept a sealed `{@id}` reference. JSON Schema
sees one document, so a rule written there would police the inline spelling and pass the referenced
one — and a rule that reports nothing is indistinguishable from a rule that passes.

## Relationship to other BBs

- **[cdifEnumerationDomain](../cdifEnumerationDomain/)** — `cdif:takesValuesFrom` refs this BB when the value set is a controlled vocabulary, codelist, or classification.
- **[cdifInstanceVariable](../cdifInstanceVariable/)** — references a CDIF Value Domain to describe permissible values for the variable.
- **[cdifRepresentedVariable](../cdifRepresentedVariable/)** — `$ref`s `$defs/SubstantiveValueDomain` from this block directly.
- **[ddicdiValueDomain](../../../archive/ddiProperties/ddicdiValueDomain/)** — the native DDI-CDI transcription, **archived** since 2026-10-05 and referenced by no active schema. It covers `cdi:takesConceptsFrom` and `cdi:platformType`, which this CDIF profile omits, and spells the shared properties `cdi:takesValuesFrom` / `cdi:displayLabel` / `cdi:recommendedDataType` rather than `cdif:`.

## Notes

- The `cdif:` spelling of `takesValuesFrom`, `displayLabel` and `recommendedDataType` is deliberate: by the repository's namespace rule, a property whose value type diverges from the canonical DDI-CDI XMI is renamed to `cdif:` so the divergence is visible. `cdi:isDescribedBy` keeps the `cdi:` prefix because its value *is* a `cdi:ValueAndConceptDescription`.
- The `xsdDataType` enum is the same fixed list of 35 tokens used elsewhere in CDIF for advertising recommended XML Schema datatypes.
- `rules.shacl` holds five shapes. Two restate the `takesValuesFrom`/`recommendedDataType` choice as an `sh:or` at `sh:Violation`, one per branch, and recommend `cdif:displayLabel` at `sh:Warning` — an advisory with no JSON Schema counterpart. The other three are the coherence rules described above: `cdifd:cdifValueDomainContinuousNotEnumerableShape`, `cdifd:cdifValueDomainEnumerationRedundancyShape` and `cdifd:cdifValueAndConceptDescriptionBoundsShape`. The negative cases under `tests/` cover the JSON Schema half only; the three SHACL rules are exercised by probe instances rather than by test fixtures, because a `tests/*-fail.json` that fails SHACL but passes JSON Schema would register as asserting nothing under `test_fail_cases.py --strict`.
