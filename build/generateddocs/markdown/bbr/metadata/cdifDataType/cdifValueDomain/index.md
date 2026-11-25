
# CDIF Value Domain (Schema)

`cdif.bbr.metadata.cdifDataType.cdifValueDomain` *v0.1*

CDIF profile of the DDI-CDI ValueDomain. A single node is either a cdif:SubstantiveValueDomain (subject-matter values) or a cdif:SentinelValueDomain (processing/missing-value codes). Each carries cdif:takesValuesFrom (refs cdifEnumerationDomain), cdif:displayLabel, and an array cdif:recommendedDataType of xsd: type tokens; at least one of takesValuesFrom or recommendedDataType is required.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### Minimal CDIF Value Domain
A bare cdif:SubstantiveValueDomain that recommends a single xsd:nonNegativeInteger
data type for an age-in-years variable. Schema requires @type plus at least one of
cdif:takesValuesFrom or cdif:recommendedDataType; this example satisfies the latter.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdif": "https://w3id.org/cdif/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:SubstantiveValueDomain"],
  "@id": "ex:vd/age-years",
  "cdif:recommendedDataType": ["xsd:nonNegativeInteger"]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifValueDomain/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:SubstantiveValueDomain"
  ],
  "@id": "ex:vd/age-years",
  "cdif:recommendedDataType": [
    "xsd:nonNegativeInteger"
  ]
}
```

#### ttl
```ttl
@prefix cdif: <https://w3id.org/cdif/> .

<https://example.org/vd/age-years> a cdif:SubstantiveValueDomain ;
    cdif:recommendedDataType "xsd:nonNegativeInteger" .


```


### Complete CDIF Value Domain
A cdif:SubstantiveValueDomain for ISO 3166-1 alpha-2 country codes — exercises
every property: cdif:takesValuesFrom (inline cdifEnumerationDomain),
cdif:displayLabel, and cdif:recommendedDataType (two xsd: types).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:SubstantiveValueDomain"],
  "@id": "ex:vd/country-iso3166",
  "cdif:displayLabel": "ISO 3166-1 alpha-2 country code",
  "cdif:takesValuesFrom": {
    "@type": ["cdif:EnumerationDomain"],
    "@id": "ex:enum-domain/iso3166",
    "schema:name": "ISO 3166-1 alpha-2 country codes",
    "cdif:references": {
      "@id": "https://www.iso.org/obp/ui/#iso:pub:PUB500001"
    }
  },
  "cdif:recommendedDataType": ["xsd:string", "xsd:token"]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifValueDomain/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:SubstantiveValueDomain"
  ],
  "@id": "ex:vd/country-iso3166",
  "cdif:displayLabel": "ISO 3166-1 alpha-2 country code",
  "cdif:takesValuesFrom": {
    "@type": [
      "cdif:EnumerationDomain"
    ],
    "@id": "ex:enum-domain/iso3166",
    "schema:name": "ISO 3166-1 alpha-2 country codes",
    "cdif:references": {
      "@id": "https://www.iso.org/obp/ui/#iso:pub:PUB500001"
    }
  },
  "cdif:recommendedDataType": [
    "xsd:string",
    "xsd:token"
  ]
}
```

#### ttl
```ttl
@prefix cdif: <https://w3id.org/cdif/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/vd/country-iso3166> a cdif:SubstantiveValueDomain ;
    cdif:displayLabel "ISO 3166-1 alpha-2 country code" ;
    cdif:recommendedDataType "xsd:string",
        "xsd:token" ;
    cdif:takesValuesFrom <https://example.org/enum-domain/iso3166> .

<https://example.org/enum-domain/iso3166> a cdif:EnumerationDomain ;
    schema1:name "ISO 3166-1 alpha-2 country codes" ;
    cdif:references <https://www.iso.org/obp/ui/#iso:pub:PUB500001> .


```


### Continuous domain with a full value description
A cdif:SubstantiveValueDomain for air temperature. Satisfies the root choice through
cdif:recommendedDataType alone — no codelist is cited — and carries an inline
cdi:isDescribedBy whose cdi:ValueAndConceptDescription states the classification level,
a prose description, an LDML number pattern, a logical expression, inclusive bounds and
a regular expression.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:SubstantiveValueDomain"],
  "@id": "ex:vd/air-temperature-degc",
  "cdif:displayLabel": "Air temperature (degrees Celsius)",
  "cdif:recommendedDataType": ["xsd:double", "xsd:decimal"],
  "cdi:isDescribedBy": {
    "@type": ["cdi:ValueAndConceptDescription"],
    "@id": "ex:vacd/air-temperature-degc",
    "cdi:classificationLevel": "Continuous",
    "cdi:description": "Near-surface air temperature in degrees Celsius, reported to two decimal places, bounded by the range of values observed in the terrestrial record.",
    "cdif:formatPattern": "#,##0.0#",
    "cdif:logicalExpression": "(all reals x such that -90.0 <= x <= 60.0)",
    "cdi:minimumValueInclusive": "-90.0",
    "cdi:maximumValueInclusive": "60.0",
    "cdif:regularExpression": "^-?\\d{1,2}(\\.\\d{1,2})?$"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifValueDomain/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:SubstantiveValueDomain"
  ],
  "@id": "ex:vd/air-temperature-degc",
  "cdif:displayLabel": "Air temperature (degrees Celsius)",
  "cdif:recommendedDataType": [
    "xsd:double",
    "xsd:decimal"
  ],
  "cdi:isDescribedBy": {
    "@type": [
      "cdi:ValueAndConceptDescription"
    ],
    "@id": "ex:vacd/air-temperature-degc",
    "cdi:classificationLevel": "Continuous",
    "cdi:description": "Near-surface air temperature in degrees Celsius, reported to two decimal places, bounded by the range of values observed in the terrestrial record.",
    "cdif:formatPattern": "#,##0.0#",
    "cdif:logicalExpression": "(all reals x such that -90.0 <= x <= 60.0)",
    "cdi:minimumValueInclusive": "-90.0",
    "cdi:maximumValueInclusive": "60.0",
    "cdif:regularExpression": "^-?\\d{1,2}(\\.\\d{1,2})?$"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .

<https://example.org/vd/air-temperature-degc> a cdif:SubstantiveValueDomain ;
    cdi:isDescribedBy <https://example.org/vacd/air-temperature-degc> ;
    cdif:displayLabel "Air temperature (degrees Celsius)" ;
    cdif:recommendedDataType "xsd:decimal",
        "xsd:double" .

<https://example.org/vacd/air-temperature-degc> a cdi:ValueAndConceptDescription ;
    cdi:classificationLevel "Continuous" ;
    cdi:description "Near-surface air temperature in degrees Celsius, reported to two decimal places, bounded by the range of values observed in the terrestrial record." ;
    cdi:maximumValueInclusive "60.0" ;
    cdi:minimumValueInclusive "-90.0" ;
    cdif:formatPattern "#,##0.0#" ;
    cdif:logicalExpression "(all reals x such that -90.0 <= x <= 60.0)" ;
    cdif:regularExpression "^-?\\d{1,2}(\\.\\d{1,2})?$" .


```


### Substantive domain by reference
A cdif:SubstantiveValueDomain whose cdif:takesValuesFrom and cdi:isDescribedBy are both
@id references to nodes declared elsewhere in the graph, exercising the sealed
objectReference branch of each property. The root choice is satisfied by
cdif:takesValuesFrom, with no cdif:recommendedDataType present.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:SubstantiveValueDomain"],
  "@id": "ex:vd/lithology",
  "cdif:displayLabel": "Lithology",
  "cdif:takesValuesFrom": {
    "@id": "ex:enum-domain/cgi-simple-lithology"
  },
  "cdi:isDescribedBy": {
    "@id": "ex:vacd/lithology"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifValueDomain/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:SubstantiveValueDomain"
  ],
  "@id": "ex:vd/lithology",
  "cdif:displayLabel": "Lithology",
  "cdif:takesValuesFrom": {
    "@id": "ex:enum-domain/cgi-simple-lithology"
  },
  "cdi:isDescribedBy": {
    "@id": "ex:vacd/lithology"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .

<https://example.org/vd/lithology> a cdif:SubstantiveValueDomain ;
    cdi:isDescribedBy <https://example.org/vacd/lithology> ;
    cdif:displayLabel "Lithology" ;
    cdif:takesValuesFrom <https://example.org/enum-domain/cgi-simple-lithology> .


```


### Ordinal domain enumerated in prose
A cdif:SubstantiveValueDomain for a five-point Likert scale. The inline
cdif:EnumerationDomain cites no cdif:references, so it must carry schema:description —
the conditional branch of that block's if/then rule — and also shows cdif:purpose and a
cdif:identifier in schema:PropertyValue form.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:SubstantiveValueDomain"],
  "@id": "ex:vd/agreement-likert5",
  "cdif:displayLabel": "Level of agreement (five-point Likert scale)",
  "cdif:recommendedDataType": ["xsd:token"],
  "cdif:takesValuesFrom": {
    "@type": ["cdif:EnumerationDomain"],
    "@id": "ex:enum-domain/agreement-likert5",
    "schema:name": "Five-point agreement scale",
    "schema:description": "The ordered categories strongly disagree, disagree, neither agree nor disagree, agree, strongly agree. No external codelist is cited, so the admitted values are stated here in prose.",
    "cdif:purpose": "Record ordered attitudinal responses without committing the survey to an external code register.",
    "cdif:identifier": {
      "@type": ["schema:PropertyValue"],
      "schema:propertyID": "local",
      "schema:value": "agreement-likert5"
    }
  },
  "cdi:isDescribedBy": {
    "@type": ["cdi:ValueAndConceptDescription"],
    "@id": "ex:vacd/agreement-likert5",
    "cdi:classificationLevel": "Ordinal",
    "cdi:description": "Five ordered response categories. The order of the categories is meaningful but the intervals between them are not."
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifValueDomain/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:SubstantiveValueDomain"
  ],
  "@id": "ex:vd/agreement-likert5",
  "cdif:displayLabel": "Level of agreement (five-point Likert scale)",
  "cdif:recommendedDataType": [
    "xsd:token"
  ],
  "cdif:takesValuesFrom": {
    "@type": [
      "cdif:EnumerationDomain"
    ],
    "@id": "ex:enum-domain/agreement-likert5",
    "schema:name": "Five-point agreement scale",
    "schema:description": "The ordered categories strongly disagree, disagree, neither agree nor disagree, agree, strongly agree. No external codelist is cited, so the admitted values are stated here in prose.",
    "cdif:purpose": "Record ordered attitudinal responses without committing the survey to an external code register.",
    "cdif:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "local",
      "schema:value": "agreement-likert5"
    }
  },
  "cdi:isDescribedBy": {
    "@type": [
      "cdi:ValueAndConceptDescription"
    ],
    "@id": "ex:vacd/agreement-likert5",
    "cdi:classificationLevel": "Ordinal",
    "cdi:description": "Five ordered response categories. The order of the categories is meaningful but the intervals between them are not."
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/vd/agreement-likert5> a cdif:SubstantiveValueDomain ;
    cdi:isDescribedBy <https://example.org/vacd/agreement-likert5> ;
    cdif:displayLabel "Level of agreement (five-point Likert scale)" ;
    cdif:recommendedDataType "xsd:token" ;
    cdif:takesValuesFrom <https://example.org/enum-domain/agreement-likert5> .

<https://example.org/enum-domain/agreement-likert5> a cdif:EnumerationDomain ;
    schema1:description "The ordered categories strongly disagree, disagree, neither agree nor disagree, agree, strongly agree. No external codelist is cited, so the admitted values are stated here in prose." ;
    schema1:name "Five-point agreement scale" ;
    cdif:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "local" ;
            schema1:value "agreement-likert5" ] ;
    cdif:purpose "Record ordered attitudinal responses without committing the survey to an external code register." .

<https://example.org/vacd/agreement-likert5> a cdi:ValueAndConceptDescription ;
    cdi:classificationLevel "Ordinal" ;
    cdi:description "Five ordered response categories. The order of the categories is meaningful but the intervals between them are not." .


```


### Interval domain with exclusive bounds
A cdif:SubstantiveValueDomain for a four-digit collection year, bounded by
cdi:minimumValueExclusive and cdi:maximumValueExclusive and formatted by an LDML date
pattern. The inclusive bounds appear in the continuous-domain example instead; stating
both pairs on one domain would be contradictory.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:SubstantiveValueDomain"],
  "@id": "ex:vd/collection-year",
  "cdif:displayLabel": "Year of collection",
  "cdif:recommendedDataType": ["xsd:gYear"],
  "cdi:isDescribedBy": {
    "@type": ["cdi:ValueAndConceptDescription"],
    "@id": "ex:vacd/collection-year",
    "cdi:classificationLevel": "Interval",
    "cdi:description": "Four-digit calendar year in which the specimen was collected. Bounds are stated exclusively: the collection postdates 1799 and precedes 2101.",
    "cdif:formatPattern": "yyyy",
    "cdi:minimumValueExclusive": "1799",
    "cdi:maximumValueExclusive": "2101"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifValueDomain/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:SubstantiveValueDomain"
  ],
  "@id": "ex:vd/collection-year",
  "cdif:displayLabel": "Year of collection",
  "cdif:recommendedDataType": [
    "xsd:gYear"
  ],
  "cdi:isDescribedBy": {
    "@type": [
      "cdi:ValueAndConceptDescription"
    ],
    "@id": "ex:vacd/collection-year",
    "cdi:classificationLevel": "Interval",
    "cdi:description": "Four-digit calendar year in which the specimen was collected. Bounds are stated exclusively: the collection postdates 1799 and precedes 2101.",
    "cdif:formatPattern": "yyyy",
    "cdi:minimumValueExclusive": "1799",
    "cdi:maximumValueExclusive": "2101"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .

<https://example.org/vd/collection-year> a cdif:SubstantiveValueDomain ;
    cdi:isDescribedBy <https://example.org/vacd/collection-year> ;
    cdif:displayLabel "Year of collection" ;
    cdif:recommendedDataType "xsd:gYear" .

<https://example.org/vacd/collection-year> a cdi:ValueAndConceptDescription ;
    cdi:classificationLevel "Interval" ;
    cdi:description "Four-digit calendar year in which the specimen was collected. Bounds are stated exclusively: the collection postdates 1799 and precedes 2101." ;
    cdi:maximumValueExclusive "2101" ;
    cdi:minimumValueExclusive "1799" ;
    cdif:formatPattern "yyyy" .


```


### Ratio domain
A cdif:SubstantiveValueDomain for a specimen count, classified Ratio with a single
inclusive lower bound of zero.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:SubstantiveValueDomain"],
  "@id": "ex:vd/specimen-count",
  "cdif:displayLabel": "Number of specimens",
  "cdif:recommendedDataType": ["xsd:nonNegativeInteger"],
  "cdi:isDescribedBy": {
    "@type": ["cdi:ValueAndConceptDescription"],
    "@id": "ex:vacd/specimen-count",
    "cdi:classificationLevel": "Ratio",
    "cdi:description": "A count of physical specimens. Zero is meaningful and denotes absence, so ratios between values are interpretable.",
    "cdi:minimumValueInclusive": "0"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifValueDomain/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:SubstantiveValueDomain"
  ],
  "@id": "ex:vd/specimen-count",
  "cdif:displayLabel": "Number of specimens",
  "cdif:recommendedDataType": [
    "xsd:nonNegativeInteger"
  ],
  "cdi:isDescribedBy": {
    "@type": [
      "cdi:ValueAndConceptDescription"
    ],
    "@id": "ex:vacd/specimen-count",
    "cdi:classificationLevel": "Ratio",
    "cdi:description": "A count of physical specimens. Zero is meaningful and denotes absence, so ratios between values are interpretable.",
    "cdi:minimumValueInclusive": "0"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .

<https://example.org/vd/specimen-count> a cdif:SubstantiveValueDomain ;
    cdi:isDescribedBy <https://example.org/vacd/specimen-count> ;
    cdif:displayLabel "Number of specimens" ;
    cdif:recommendedDataType "xsd:nonNegativeInteger" .

<https://example.org/vacd/specimen-count> a cdi:ValueAndConceptDescription ;
    cdi:classificationLevel "Ratio" ;
    cdi:description "A count of physical specimens. Zero is meaningful and denotes absence, so ratios between values are interpretable." ;
    cdi:minimumValueInclusive "0" .


```


### Sentinel domain with coded missing values
A cdif:SentinelValueDomain — the other branch of this block's root oneOf — for negative
integer codes marking non-substantive responses. Carries every property the branch
defines: cdif:displayLabel, cdif:recommendedDataType, an inline cdif:EnumerationDomain
that does cite cdif:references, and an inline cdi:ValueAndConceptDescription.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:SentinelValueDomain"],
  "@id": "ex:vd/missing-value-codes",
  "cdif:displayLabel": "Missing and below-detection codes",
  "cdif:recommendedDataType": ["xsd:int"],
  "cdif:takesValuesFrom": {
    "@type": ["cdif:EnumerationDomain"],
    "@id": "ex:enum-domain/missing-value-codes",
    "schema:name": "Survey missing-value codes",
    "cdif:purpose": "Distinguish the reasons a substantive value is absent so that analysis can treat them differently.",
    "cdif:references": {
      "@id": "ex:codelist/missing-value-codes"
    }
  },
  "cdi:isDescribedBy": {
    "@type": ["cdi:ValueAndConceptDescription"],
    "@id": "ex:vacd/missing-value-codes",
    "cdi:classificationLevel": "Nominal",
    "cdi:description": "Negative integer codes reserved for non-substantive responses: -97 below detection limit, -98 refused, -99 not applicable. These values are never measurements and must be excluded before any arithmetic.",
    "cdif:regularExpression": "^-9[789]$"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifValueDomain/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:SentinelValueDomain"
  ],
  "@id": "ex:vd/missing-value-codes",
  "cdif:displayLabel": "Missing and below-detection codes",
  "cdif:recommendedDataType": [
    "xsd:int"
  ],
  "cdif:takesValuesFrom": {
    "@type": [
      "cdif:EnumerationDomain"
    ],
    "@id": "ex:enum-domain/missing-value-codes",
    "schema:name": "Survey missing-value codes",
    "cdif:purpose": "Distinguish the reasons a substantive value is absent so that analysis can treat them differently.",
    "cdif:references": {
      "@id": "ex:codelist/missing-value-codes"
    }
  },
  "cdi:isDescribedBy": {
    "@type": [
      "cdi:ValueAndConceptDescription"
    ],
    "@id": "ex:vacd/missing-value-codes",
    "cdi:classificationLevel": "Nominal",
    "cdi:description": "Negative integer codes reserved for non-substantive responses: -97 below detection limit, -98 refused, -99 not applicable. These values are never measurements and must be excluded before any arithmetic.",
    "cdif:regularExpression": "^-9[789]$"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/vd/missing-value-codes> a cdif:SentinelValueDomain ;
    cdi:isDescribedBy <https://example.org/vacd/missing-value-codes> ;
    cdif:displayLabel "Missing and below-detection codes" ;
    cdif:recommendedDataType "xsd:int" ;
    cdif:takesValuesFrom <https://example.org/enum-domain/missing-value-codes> .

<https://example.org/enum-domain/missing-value-codes> a cdif:EnumerationDomain ;
    schema1:name "Survey missing-value codes" ;
    cdif:purpose "Distinguish the reasons a substantive value is absent so that analysis can treat them differently." ;
    cdif:references <https://example.org/codelist/missing-value-codes> .

<https://example.org/vacd/missing-value-codes> a cdi:ValueAndConceptDescription ;
    cdi:classificationLevel "Nominal" ;
    cdi:description "Negative integer codes reserved for non-substantive responses: -97 below detection limit, -98 refused, -99 not applicable. These values are never measurements and must be excluded before any arithmetic." ;
    cdif:regularExpression "^-9[789]$" .


```


### Minimal sentinel domain
The smallest valid cdif:SentinelValueDomain: @type plus cdif:recommendedDataType. The
mirror of the minimal substantive example, and the case that proves the root oneOf
selects on the type token alone.
#### json
```json
{
  "@context": {
    "cdif": "https://w3id.org/cdif/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:SentinelValueDomain"],
  "@id": "ex:vd/not-reported",
  "cdif:recommendedDataType": ["xsd:string"]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifValueDomain/context.jsonld",
    {
      "cdif": "https://w3id.org/cdif/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:SentinelValueDomain"
  ],
  "@id": "ex:vd/not-reported",
  "cdif:recommendedDataType": [
    "xsd:string"
  ]
}
```

#### ttl
```ttl
@prefix cdif: <https://w3id.org/cdif/> .

<https://example.org/vd/not-reported> a cdif:SentinelValueDomain ;
    cdif:recommendedDataType "xsd:string" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Value Domain
description: "Value domain for substantive or sentinel values for a variable. Typically
  a description and/or enumeration of allowed values of interest. CDIF profile of
  the DDI-CDI ValueDomain \u2014 a single node is either a cdif:SubstantiveValueDomain
  (subject-matter values) or a cdif:SentinelValueDomain (processing/missing-value
  codes)."
oneOf:
- $ref: '#/$defs/SubstantiveValueDomain'
- $ref: '#/$defs/SentinelValueDomain'
$defs:
  SubstantiveValueDomain:
    type: object
    description: Value domain for a substantive conceptual domain. Typically a description
      and/or enumeration of allowed values of interest.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdif:SubstantiveValueDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this SubstantiveValueDomain node
      cdif:takesValuesFrom:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifEnumerationDomain/schema.yaml
        - description: JSON-LD @id reference to a node defined elsewhere in the graph
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        x-jsonld-id: https://w3id.org/cdif/takesValuesFrom
      cdif:displayLabel:
        type: string
        description: 'A human-readable display label for the object. '
        x-jsonld-id: https://w3id.org/cdif/displayLabel
      cdif:recommendedDataType:
        type: array
        description: The data types that are recommended for use with this domain.
        items:
          $ref: '#/$defs/xsdDataType'
        minItems: 1
        x-jsonld-id: https://w3id.org/cdif/recommendedDataType
      cdi:isDescribedBy:
        description: A ValueAndConceptDescription giving the formal description (ranges,
          patterns, classification level, expressions) of the values this domain admits.
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - description: JSON-LD @id reference to a node defined elsewhere in the graph
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDescribedBy
    required:
    - '@type'
    anyOf:
    - required:
      - cdif:takesValuesFrom
    - required:
      - cdif:recommendedDataType
  SentinelValueDomain:
    type: object
    description: Specification of possible sentinel values used by a variable. Sentinel
      values are special values used to indicate various invalid conditions for a
      variable, e.g. below detection, missing value.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdif:SentinelValueDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this SentinelValueDomain node
      cdif:takesValuesFrom:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifEnumerationDomain/schema.yaml
        - description: JSON-LD @id reference to a node defined elsewhere in the graph
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        x-jsonld-id: https://w3id.org/cdif/takesValuesFrom
      cdif:displayLabel:
        type: string
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: https://w3id.org/cdif/displayLabel
      cdif:recommendedDataType:
        type: array
        description: The data types that are recommended for use with this domain.
        items:
          $ref: '#/$defs/xsdDataType'
        minItems: 1
        x-jsonld-id: https://w3id.org/cdif/recommendedDataType
      cdi:isDescribedBy:
        description: A ValueAndConceptDescription giving the formal description (ranges,
          patterns, classification level, expressions) of the values this domain admits.
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - description: JSON-LD @id reference to a node defined elsewhere in the graph
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDescribedBy
    required:
    - '@type'
    anyOf:
    - required:
      - cdif:takesValuesFrom
    - required:
      - cdif:recommendedDataType
  ValueAndConceptDescription:
    type: object
    description: Formal description of a set of values.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ValueAndConceptDescription
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ValueAndConceptDescription node
      cdi:classificationLevel:
        type: string
        enum:
        - Continuous
        - Interval
        - Nominal
        - Ordinal
        - Ratio
        description: Indicates the type of relationship, nominal, ordinal, interval,
          ratio, or continuous. Use where appropriate for the representation type.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/classificationLevel
      cdi:description:
        type: string
        description: A formal description of the set of values in human-readable language.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/description
      cdif:formatPattern:
        type: string
        description: 'A pattern for a number as described in Unicode Locale Data Markup
          Language (LDML) (http://www.unicode.org/reports/tr35/tr35.html) Part 3:
          Numbers (http://www.unicode.org/reports/tr35/tr35-numbers.html#Number_Format_Patterns)
          and Part 4. Dates (http://www.unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns)
          . Examples would be #,##0.### to describe the pattern for a decimal number,
          or yyyy.MM.dd G ''at'' HH:mm:ss zzz for a datetime pattern.'
        x-jsonld-id: https://w3id.org/cdif/formatPattern
      cdif:logicalExpression:
        type: string
        description: A logical expression where the values of "x" making the expression
          true are the members of the set of valid values. For example, "(all reals
          x such that x > 0)" describes the real numbers greater than 0.
        x-jsonld-id: https://w3id.org/cdif/logicalExpression
      cdi:maximumValueExclusive:
        type: string
        description: 'A string denoting the maximum possible value (excluding this
          value). From the W3C Recommendation "Metadata Vocabulary for Tabular Data"
          (https://www.w3.org/TR/tabular-metadata/) 5.11.2: "maxExclusive: An atomic
          property that contains a single number or string that is the maximum valid
          value (exclusive). The value of this property becomes the maximum exclusive
          annotation for the described datatype. See Value Constraints in [tabular-data-model]
          for details."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/maximumValueExclusive
      cdi:maximumValueInclusive:
        type: string
        description: 'A string denoting the maximum possible value. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.11.2: "maximum: An atomic property that contains a single number or string
          that is the maximum valid value (inclusive); equivalent to maxInclusive.
          The value of this property becomes the maximum annotation for the described
          datatype. See Value Constraints in [tabular-data-model] for details."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/maximumValueInclusive
      cdi:minimumValueExclusive:
        type: string
        description: 'A string denoting the minimum possible value (excluding this
          value). From the W3C Recommendation "Metadata Vocabulary for Tabular Data"
          (https://www.w3.org/TR/tabular-metadata/) 5.11.2: "minExclusive: An atomic
          property that contains a single number or string that is the minimum valid
          value (exclusive). The value of this property becomes the minimum exclusive
          annotation for the described datatype. See Value Constraints in [tabular-data-model]
          for details."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/minimumValueExclusive
      cdi:minimumValueInclusive:
        type: string
        description: 'A string denoting the minimum possible value. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.11.2: "minimum: An atomic property that contains a single number or string
          that is the minimum valid value (inclusive); equivalent to minInclusive.
          The value of this property becomes the minimum annotation for the described
          datatype. See Value Constraints in [tabular-data-model] for details."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/minimumValueInclusive
      cdif:regularExpression:
        type: string
        description: A regular expression where strings matching the expression belong
          to the set of valid values.
        x-jsonld-id: https://w3id.org/cdif/regularExpression
    required:
    - '@type'
    allOf:
    - if:
        required:
        - cdi:maximumValueInclusive
      then:
        not:
          required:
          - cdi:maximumValueExclusive
    - if:
        required:
        - cdi:minimumValueInclusive
      then:
        not:
          required:
          - cdi:minimumValueExclusive
  xsdDataType:
    type: string
    enum:
    - xsd:anyURI
    - xsd:base64Binary
    - xsd:boolean
    - xsd:byte
    - xsd:date
    - xsd:dateTime
    - xsd:decimal
    - xsd:double
    - xsd:float
    - xsd:gDay
    - xsd:gMonth
    - xsd:gMonthDay
    - xsd:gYear
    - xsd:gYearMonth
    - xsd:hexBinary
    - xsd:int
    - xsd:integer
    - xsd:language
    - xsd:long
    - xsd:Name
    - xsd:NCName
    - xsd:NMTOKEN
    - xsd:negativeInteger
    - xsd:nonNegativeInteger
    - xsd:nonPositiveInteger
    - xsd:normalizedString
    - xsd:positiveInteger
    - xsd:short
    - xsd:string
    - xsd:time
    - xsd:token
    - xsd:unsignedByte
    - xsd:unsignedInt
    - xsd:unsignedLong
    - xsd:unsignedShort
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  cdif: https://w3id.org/cdif/
  skos: http://www.w3.org/2004/02/skos/core#
  xsd: http://www.w3.org/2001/XMLSchema#
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.cdifDataType.cdifValueDomain
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-25'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifValueDomain/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifValueDomain/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifValueDomain/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifValueDomain`

