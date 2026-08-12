## Object Reference

The canonical strict reference to a node defined elsewhere in the graph, carried as an object with only an `@id` (and optionally an `@type`). Because it sets `additionalProperties: false`, it stops a lenient reference branch from swallowing inline objects that happen to also carry an `@id`. Use it wherever a slot must hold a pointer to another node rather than an inline definition.
