## Quality measure properties

Defines a set of properties for use describing a data quality measurement for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.

A quality measurement pairs the measure that was applied (`dqv:isMeasurementOf`) with the result it produced (`dqv:value`). The measure may be named as a string, referenced by IRI, or given as a `schema:DefinedTerm` from a quality-measure vocabulary such as ISO 19157. The result may be a string, a number, or a `schema:DefinedTerm` — a number carries a quantity such as a distance or a percentage, a Defined Term a categorical outcome such as pass or fail.
