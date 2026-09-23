# Link Role

A typed link. `schema:linkRelationship` names how the target relates to the
subject; `schema:target` carries the `schema:EntryPoint` being linked to.

## When to use this, and when not to

Use `linkRole` where the **relationship is the point** -- "the canonical version
of this", "the download endpoint for this". Use
[`labeledLink`](../labeledLink/) where the value is simply **a work at a URL**:
a license, a terms-of-service document, a manual. A license is a work, not a
role, and wrapping one in a Role forces every consumer through an indirection to
reach the document itself.

That division is why this block does not replace `labeledLink`. In the corpus,
`schema:license` and `schema:conditionsOfAccess` appear 36 times as plain strings
or `CreativeWork`s and never as a `LinkRole`.

## History

Until 2026-09-23 this shape was defined inline inside the `cdifCore` profile, so
nothing else could reuse it. `schemaorgProperties/instrument` consequently
defined `schema:relatedLink` as a labeled link instead -- the same property
carrying two different shapes depending on which node held it. Both now
reference this block.
