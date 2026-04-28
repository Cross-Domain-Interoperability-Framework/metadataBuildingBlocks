## DefinedTermSet properties

Defines a set of properties for use describing a schema.org DefinedTermSet for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.

A DefinedTermSet is a named container of schema:DefinedTerm objects — a controlled vocabulary, code list, or term collection. Each term in `schema:hasDefinedTerm` is validated against the DefinedTerm building block. The set itself must carry at least one identifier (any of `@id`, `schema:name`, or `schema:identifier`) so it can be referenced from `schema:inDefinedTermSet` or other links.
