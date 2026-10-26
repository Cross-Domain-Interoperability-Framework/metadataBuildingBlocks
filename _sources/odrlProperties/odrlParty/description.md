## ODRL Party

W3C ODRL 2.2 Party (a person, organization or agent identified by IRI) or PartyCollection (a group of parties, identified by @id, or by odrl:source narrowed with odrl:refinement). A Party may be typed odrl:Party, schema:Person or schema:Organization (ODRL declares Party a subclass of these), and a schema.org-typed party is validated by the person or organization block. Used for the assigner and assignee of ODRL rules and policies.

Generic W3C ODRL; CDIF-specific rules belong in profile blocks such as [odrlOffer](../odrlOffer/).

### Dependencies

- [person](../../schemaorgProperties/person/)
- [organization](../../schemaorgProperties/organization/)
- [odrlConstraint](../odrlConstraint/)
- [objectReference](../../cdifDataType/objectReference/)
