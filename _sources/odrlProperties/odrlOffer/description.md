## ODRL Offer

A [W3C ODRL 2.2](https://www.w3.org/TR/odrl-model/) Offer: the access and usage conditions a data provider sets for a digital object. Draft for the CDIF Access profile ([cdifAccess](../../profiles/cdifProfile/cdifAccess/)).

- **permission**: what a user may do (e.g. `cdifa1:download`), optionally scoped by constraints (e.g. users located in the UK).
- **duty** on a permission, constrained by `event lt policyUsage`: an **access condition**, done before retrieval (e.g. assent to a licence).
- **obligation**: what every user must do (e.g. destroy the data by a date).
- **prohibition**: what a user must not do (e.g. share TRE credentials).

The policy uses ODRL's own compact keys and carries the ODRL context plus the `cdifa1` prefix.

### Open questions

- The `cdifa1` action vocabulary and the ODRL profile at `https://w3id.org/cdif/access/profile1/` do not exist yet.
- Constraint operand values and the constraint `@type` are unspecified; LogicalConstraint is not modelled.
- Scoping users by constraint (the spreadsheet) or by assignee PartyCollection with refinement (the book).
- AssetCollection targets for a policy covering several assets.
- What an assent duty assents to.

### Dependencies

- [objectReference](../../cdifDataType/objectReference/) - `{@id}` for the `rdf:value` of a refined action
