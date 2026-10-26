## ODRL Offer

A [W3C ODRL 2.2](https://www.w3.org/TR/odrl-model/) Offer: the access and usage conditions a data provider sets for a digital object. Draft for the CDIF Access profile ([cdifAccess](../../profiles/cdifProfile/cdifAccess/)).

- **odrl:permission**: what a user may do (e.g. `cdifa1:download`), optionally scoped by constraints (e.g. users located in the UK).
- **odrl:duty** on a permission, constrained by `odrl:event odrl:lt odrl:policyUsage`: an **access condition**, done before retrieval (e.g. assent to a licence).
- **odrl:obligation**: what every user must do (e.g. destroy the data by a date).
- **odrl:prohibition**: what a user must not do (e.g. share TRE credentials).
- **odrl:assigner** / **odrl:assignee**: the parties. `odrl:assigner` is the provider (a reference or an `odrl:Party`); `odrl:assignee` on a rule is a reference, an `odrl:Party`, or an `odrl:PartyCollection`. A collection can be narrowed with `odrl:source` (the collection) plus `odrl:refinement` (e.g. registered users located in the UK).

Keys carry the `odrl:` prefix, and the `@context` declares the `odrl`, `cdifa1` and `rdf` prefixes. The ODRL JSON-LD context is not used, so IRI values (targets, actions, parties, operands) are written as `{"@id": ...}` objects.

### Open questions

- The `cdifa1` action vocabulary and the ODRL profile at `https://w3id.org/cdif/access/profile1/` do not exist yet.
- Constraint operand values and the constraint `@type` are unspecified by the spreadsheet. (LogicalConstraint and AssetCollection are available through the generic blocks.)
- Scoping users by constraint (the spreadsheet) or by assignee PartyCollection with refinement (the book); both are allowed. No shared vocabulary of PartyCollection IRIs exists yet.
- What an assent duty assents to.

### Dependencies

- [odrlPolicy](../odrlPolicy/) - the generic ODRL policy, which brings in odrlRule, odrlAction, odrlConstraint, odrlParty, odrlAsset and odrlTerms
