## Quality annotation properties

Defines a set of properties for attaching a **quality annotation** to a resource in the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.

A quality annotation is a *narrative or categorical* quality statement — a standards-compliance note, a rating, or a quality certificate — as distinct from a `dqv:QualityMeasurement`, which reports a *quantitative* value against a named metric. Use a quality **measure** when there is a metric and a measured result (e.g. positional accuracy = 4.2 m); use a quality **annotation** when the quality assertion is a statement or a categorical outcome that does not reduce to a metric/value pair (e.g. "compliant with ISO 19115", or a certification level).

`dqv:QualityAnnotation` is a subclass of the [Web Annotation](https://www.w3.org/TR/annotation-model/) `oa:Annotation`, so this building block follows the DQV pattern rather than inventing new terms:

- **`oa:hasBody`** *(required)* — the content of the annotation: a free-text statement, a `schema:DefinedTerm` for a categorical outcome (a certification level, a pass/fail rating from a controlled vocabulary), or an `@id` reference to a separate body resource.
- **`oa:motivatedBy`** *(recommended)* — why the annotation was made. For quality annotations this is normally the DQV instance `dqv:qualityAssessment`; any motivation IRI or Defined Term is accepted.
- **`oa:hasTarget`** *(optional)* — the resource the annotation is about. When omitted, the annotation is about the resource that carries it (typically the `schema:Dataset`).

The annotation is attached to the described resource with `dqv:hasQualityAnnotation`.

### Relationship to DDI Codebook

DDI Codebook 2.5 `stdyInfo/qualityStatement` maps here: `standardsCompliance/complianceDescription` and `otherQualityStatement` become the `oa:hasBody` of a quality annotation, while `standardsCompliance/standard/standardName` — a machine-actionable claim of conformance to a named standard — is better expressed as `dcterms:conformsTo` on the dataset than as a free-text annotation.
