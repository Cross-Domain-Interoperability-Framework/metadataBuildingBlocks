#!/usr/bin/env python3
"""Audit the release-repo Implementation Guides against the schemas they describe.

Phase 1 of the IG generator work: this tool *detects* drift, it never rewrites a
guide. The guides were produced once by ``generate_ig_draft.py`` and hand-edited
thereafter, so nothing has connected them to their schema since. Three failure
modes follow from that, and this checks for all three:

  undeclared   a guide documents a property that appears nowhere in the profile
               schema. The profiles are open-world, so a record copied from the
               guide validates green while the property carries no meaning --
               the defect is invisible to every validator CDIF runs.
  cardinality  a guide states Required for a property the schema never requires,
               or Optional for one it always requires. The second direction
               fails records outright.
  divergence   the same property documented at materially different depth in two
               guides, or carrying a Cardinality bullet with no Description.

What it deliberately does NOT check: the free-text **Content:** bullet. The
guides describe content in a prose vocabulary ("string, object reference, or
DefinedTerm") that does not map onto JSON Schema types without a translation
table, and a check that guesses would report noise rather than defects.

Property blocks are located with ``clean_ig.py``'s parser so this tool and the
cleaner agree on what a property block is; the guide/profile mapping is taken
from ``sync_release_repos.py`` so there is one table, not two.

Usage:
    python tools/audit_ig_consistency.py                  # all guides, all checks
    python tools/audit_ig_consistency.py -c undeclared    # one check
    python tools/audit_ig_consistency.py -g profile-core  # one guide
    python tools/audit_ig_consistency.py --strict         # exit 1 on any finding
    python tools/audit_ig_consistency.py --self-test      # prove the checks fire
"""
import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

MBB_ROOT = Path(__file__).resolve().parent.parent
CDIF_ROOT = MBB_ROOT.parent
CHECKS = ("undeclared", "cardinality", "divergence")


def _load(name):
    spec = importlib.util.spec_from_file_location(name, MBB_ROOT / "tools" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


clean_ig = _load("clean_ig")
sync_release_repos = _load("sync_release_repos")

FIELD_RE = re.compile(r"^\s*[-*]?\s*\*\*([A-Za-z][A-Za-z /]*?)\s*:?\*\*\s*(.*)$")


def guide_path(repo_rel):
    """The single *ImplementationGuide.md in a release repo, or None."""
    d = CDIF_ROOT / repo_rel
    hits = sorted(p for p in d.glob("*ImplementationGuide.md") if p.is_file())
    return hits[0] if hits else None


def prop_name(title):
    """Property name from a heading: drop anchors and markdown emphasis.

    Underscores are preserved -- cdi:has_DataStructureComponent is a real DDI-CDI
    name, and stripping `_` as emphasis turns it into a phantom missing property.
    """
    t = re.sub(r"\{#[^}]+\}", "", title or "")
    t = t.replace("\\", "").replace('"', "").replace("'", "")
    t = re.sub(r"\*\*|\*|`", "", t)
    # `prov: wasGeneratedBy` is a heading typo for a real property, not a
    # different property -- normalise so it resolves instead of reporting a
    # phantom missing one.
    t = re.sub(r"\s*:\s*", ":", t)
    return t.strip().rstrip(":").strip()


# A property heading is a single token, optionally prefixed. clean_ig.is_property
# also accepts any lowercase-initial heading, which sweeps in narrative titles
# ("identifier and version identify different things"); those are not properties
# and reporting them as undeclared is noise, not a finding.
PROP_TOKEN_RE = re.compile(r"^@?[A-Za-z][\w.\-]*(?::[A-Za-z_@][\w.\-]*)?$")


def parse_fields(body_text):
    """The **Label:** bullets of a property block, lowercased keys."""
    out, cur = {}, None
    for ln in body_text.splitlines():
        m = FIELD_RE.match(ln)
        if m:
            cur = m.group(1).strip().lower()
            out[cur] = m.group(2).strip()
        elif cur and ln.strip():
            out[cur] += " " + ln.strip()
    return out


def read_guide(path):
    """[{name, line, fields, body}] for each property block in a guide."""
    text = path.read_text(encoding="utf-8", errors="replace")
    blocks = clean_ig.parse_blocks(text)
    # parse_blocks drops line numbers; recover them by walking headings in order.
    heading_lines = [i + 1 for i, l in enumerate(text.splitlines())
                     if clean_ig.HEADING_RE.match(l)]
    out, hi = [], 0
    for b in blocks:
        if b["level"] == 0:
            continue
        line = heading_lines[hi] if hi < len(heading_lines) else 0
        hi += 1
        if not clean_ig.is_property(b):
            continue
        body = "".join(b["body"])
        name = prop_name(b["title"])
        if not name or name in ("@type", "@id", "@context"):
            continue
        if not PROP_TOKEN_RE.match(name):
            continue
        out.append({"name": name, "line": line, "fields": parse_fields(body), "body": body})
    return out


def _is_sealed_ref(branch):
    """The `{'@id': ...}` reference form: sealed, and requiring only @id."""
    return (isinstance(branch, dict)
            and branch.get("additionalProperties") is False
            and list(branch.get("required") or []) == ["@id"])


def _inline_of_ref_idiom(branches):
    """For `anyOf: [inline class, sealed @id reference]`, return the inline branch.

    Returns None when this is a genuine choice between alternatives, in which
    case no branch's `required` holds unconditionally.
    """
    if len(branches) != 2:
        return None
    sealed = [b for b in branches if _is_sealed_ref(b)]
    others = [b for b in branches if not _is_sealed_ref(b)]
    if len(sealed) == 1 and len(others) == 1 and isinstance(others[0], dict):
        return others[0]
    return None


def resolve_bare(name, declared):
    """Which declared property an UNPREFIXED guide heading means.

    The guides write schema.org properties bare (`name`, `identifier`, `url`)
    and give everything else an explicit prefix: measured across the 12 guides,
    352 bare headings resolve to exactly one `schema:` property and 4 to
    `dcterms:`. So `schema:<name>` wins whenever it is declared.

    This matters more than it looks. 53 bare headings have several candidates
    (`name` is both `cdif:name` and `schema:name`), and picking by sort order
    chose `cdif:name` -- never required -- and reported `schema:name`, required
    in two scopes, as a property "the schema never requires". Sorting had fixed
    an earlier non-determinism here, which made the wrong answer a *stable*
    wrong answer rather than a correct one.

    Where `schema:` is not among the candidates and there is more than one, the
    heading is genuinely ambiguous and this returns None rather than guessing.
    """
    cands = [d for d in declared if d.split(":")[-1] == name]
    if not cands:
        return None
    if len(cands) == 1:
        return cands[0]
    return next((d for d in cands if d.startswith("schema:")), None)


def index_schema(schema):
    """Every property the profile declares, and where it is required.

    Returns (declared, required_scopes, property_scopes, repeatable) where
    required_scopes[prop] is the set of scope ids requiring it and
    property_scopes[prop] the set declaring it. A property may be required in one
    class and optional in another, so 'required' is only meaningful per scope.
    """
    declared, required_scopes, property_scopes, repeatable = set(), {}, {}, set()
    required_anywhere = set()
    choice_groups = {}          # prop -> {frozenset of the 'at least one of' group}

    def note(scope, props, required, conditional_required=()):
        for name, spec in (props or {}).items():
            declared.add(name)
            property_scopes.setdefault(name, set()).add(scope)
            if isinstance(spec, dict) and spec.get("type") == "array":
                repeatable.add(name)
        for name in (required or []):
            required_scopes.setdefault(name, set()).add(scope)
        required_anywhere.update(required or ())
        required_anywhere.update(conditional_required)

    def walk(node, scope, unconditional=True):
        """`unconditional` is False inside anyOf/oneOf/if/then/else/not.

        Only the node itself and its allOf chain impose requirements that always
        hold. An anyOf of required-branches is a CHOICE -- `anyOf: [{required:
        [license]}, {required: [conditionsOfAccess]}]` requires neither on its
        own, and counting both as mandatory turns every choice group into a
        phantom "the guide is wrong" finding. Properties named anywhere still
        count as declared; only their requiredness is scoped.
        """
        if isinstance(node, dict):
            # A branch may carry `required` with no `properties` of its own --
            # cdifCore's real required list lives in allOf[1] exactly that way.
            # Keying this off `properties` made every such requirement invisible.
            if isinstance(node.get("properties"), dict) or node.get("required"):
                note(scope, node.get("properties"),
                     node.get("required") if unconditional else None,
                     () if unconditional else (node.get("required") or ()))
            for br in node.get("allOf", []) or []:
                walk(br, scope, unconditional)
            for key in ("anyOf", "oneOf"):
                branches = node.get(key, []) or []
                reqs = [set(b.get("required") or ())
                        for b in branches if isinstance(b, dict)]
                if len(reqs) >= 2 and all(reqs):
                    common = set.intersection(*reqs)
                    union = set.union(*reqs)
                    if common and unconditional:
                        # Required by EVERY branch, so required outright however
                        # the choice resolves -- e.g. @type across a subclass union.
                        for n in common:
                            required_scopes.setdefault(n, set()).add(scope)
                        required_anywhere.update(common)
                    elif not common and all(len(r) == 1 for r in reqs):
                        # The "at least one of" idiom, and ONLY this shape: every
                        # branch requires exactly one property. A branch requiring
                        # several means "this whole set, or that whole set" --
                        # schema:distribution is `[[@type], [potentialAction,
                        # serviceType, termsOfService]]`, where the second branch
                        # needs all three together. Taking the union across
                        # branches called that "at least one of the three" and
                        # produced 12 confidently wrong findings.
                        members = frozenset(next(iter(r)) for r in reqs)
                        # A branch satisfied by @id/@type alone is an escape
                        # hatch: the group can be met without any real member, so
                        # it constrains none of them.
                        if not (members & {"@id", "@type"}) and len(members) >= 2:
                            for n in members:
                                choice_groups.setdefault(n, set()).add((scope, members))
                inline = _inline_of_ref_idiom(branches)
                if inline is not None:
                    # `anyOf: [inline class, sealed {@id} reference]` is a CONTENT
                    # alternative, not a cardinality choice: whichever form you
                    # use, the inline branch's required list is the class's real
                    # contract. Treating it as conditional made every class whose
                    # body sits behind the idiom -- GeoCoordinates, the DDI-CDI
                    # components -- look like it required nothing.
                    walk(inline, scope, unconditional)
                    continue
                for br in branches:
                    walk(br, scope, False)
            for key in ("if", "then", "else", "not"):
                if isinstance(node.get(key), dict):
                    walk(node[key], scope, False)
            if isinstance(node.get("items"), dict):
                walk(node["items"], scope, unconditional)
            for name, sub in (node.get("properties") or {}).items():
                if isinstance(sub, dict):
                    walk(sub, f"{scope}/{name}", unconditional)
        elif isinstance(node, list):
            for v in node:
                walk(v, scope, unconditional)

    walk({k: v for k, v in schema.items() if k != "$defs"}, "$root")
    for cls, sub in (schema.get("$defs") or {}).items():
        walk(sub, f"$defs.{cls}")
    return (declared, required_scopes, property_scopes, repeatable,
            required_anywhere, choice_groups)


def states_required(card):
    c = (card or "").lower()
    return "required" in c and "if no" not in c and "if " not in c


def states_optional(card):
    return (card or "").lower().strip().startswith("optional")


def audit(selected_checks, only_guide):
    findings = []
    descriptions = {}          # prop -> {guide: description}

    for repo_rel, src_rel, schema_name, _shacl in sync_release_repos.REPOS:
        repo_key = repo_rel.split("/")[0]
        if only_guide and only_guide not in repo_rel:
            continue
        gp = guide_path(repo_rel)
        if gp is None:
            findings.append(("missing-guide", repo_key, 0, "", "no *ImplementationGuide.md in this repo"))
            continue
        schema_file = CDIF_ROOT / repo_rel / schema_name
        if not schema_file.exists():
            findings.append(("missing-schema", repo_key, 0, "", f"{schema_name} not found"))
            continue
        schema = json.loads(schema_file.read_text(encoding="utf-8"))
        (declared, required_scopes, property_scopes, repeatable,
         required_anywhere, choice_groups) = index_schema(schema)

        for blk in read_guide(gp):
            name, line, f = blk["name"], blk["line"], blk["fields"]
            desc = f.get("description", "")
            if desc:
                descriptions.setdefault(name, {})[repo_key] = desc

            # An explicit prefix is a claim about the exact property IRI, so only
            # an unprefixed heading ("name", "identifier") may match on the local
            # name. Matching `schema:identifier` against any declared *:identifier
            # made the undeclared check unable to fail -- it reported zero on a
            # corpus known to contain documented-but-undeclared properties.
            if name in declared:
                hit = name
            elif ":" in name:
                hit = None
            else:
                hit = resolve_bare(name, declared)

            if hit is None and ":" not in name and any(
                    d.split(":")[-1] == name for d in declared):
                # Declared under several prefixes, none of them schema: -- the
                # heading is ambiguous, not missing. Reporting it as undeclared
                # would be false; judging its cardinality would be a guess.
                continue
            if "undeclared" in selected_checks and hit is None:
                findings.append(("undeclared", repo_key, line, name,
                                 f"documented but absent from {schema_name}"))
                continue
            if hit is None:
                continue

            if "cardinality" in selected_checks and "cardinality" in f:
                card = f["cardinality"]
                req_in = required_scopes.get(hit, set())
                decl_in = property_scopes.get(hit, set())
                # Only a property required NOWHERE -- not even inside one branch
                # of a subclass union -- contradicts a Required claim. Guides
                # document per class, and cdi:has_DataStructureComponent is
                # genuinely required by three of four DataStructure subclasses.
                # Only report a choice group when the class is unambiguous: the
                # property is declared in exactly one scope and belongs to exactly
                # one group there. Guides document per class, and a name like
                # schema:name is required outright on the root Dataset while also
                # being one alternative inside a nested DefinedTerm -- without a
                # guide-block -> schema-class mapping, judging the ambiguous ones
                # produces noise, not findings.
                groups = choice_groups.get(hit) or set()
                unambiguous = (len(groups) == 1
                               and len(property_scopes.get(hit, ())) == 1
                               and next(iter(groups))[0] in property_scopes.get(hit, ()))
                if unambiguous:
                    groups = {next(iter(groups))[1]}
                    # "at least one of" -- the group is mandatory, no member is.
                    # A conditional phrasing ("Required if no X") states this
                    # correctly and states_required/states_optional both reject it.
                    others = sorted(n for g in groups for n in g if n != hit)
                    alts = ", ".join(others)
                    if states_required(card):
                        findings.append(("cardinality", repo_key, line, name,
                                         f"guide says Required flatly; schema requires at least "
                                         f"one of this and {alts} -- phrase it "
                                         f"'Required if no {others[0]}'"))
                    elif states_optional(card):
                        findings.append(("cardinality", repo_key, line, name,
                                         f"guide says Optional; schema requires at least one of "
                                         f"this and {alts}, so omitting them all FAILS the record"))
                elif states_required(card) and hit not in required_anywhere:
                    findings.append(("cardinality", repo_key, line, name,
                                     "guide says Required; schema never requires it, "
                                     "in any class or branch"))
                elif states_optional(card) and decl_in and req_in >= decl_in:
                    findings.append(("cardinality", repo_key, line, name,
                                     "guide says Optional; schema requires it wherever declared "
                                     "-- records following the guide will FAIL"))

            if "divergence" in selected_checks and "cardinality" in f and not desc:
                findings.append(("divergence", repo_key, line, name,
                                 "has a Cardinality bullet but no Description"))

    if "divergence" in selected_checks:
        for prop, by_guide in sorted(descriptions.items()):
            if len(by_guide) < 2:
                continue
            lens = sorted(len(v) for v in by_guide.values())
            if lens[-1] >= 40 and lens[-1] >= 3 * max(lens[0], 1):
                spread = ", ".join(f"{g}:{len(v)}" for g, v in
                                   sorted(by_guide.items(), key=lambda kv: -len(kv[1])))
                findings.append(("divergence", "(cross-guide)", 0, prop,
                                 f"description depth varies {lens[0]}->{lens[-1]} chars [{spread}]"))
    return findings


CHECK_BLURB = {
    "undeclared": "The guide documents a property the profile schema does not declare. "
                  "The profiles are open-world, so a record copied from the guide validates "
                  "green while the property carries no meaning. Either the guide is stale "
                  "(a rename it never received) or the schema is missing something the "
                  "guide promises -- which of the two is a spec decision, not a doc fix.",
    "cardinality": "A Required/Optional claim the schema contradicts. 'Optional; schema "
                   "requires it wherever declared' is the direction that FAILS records: an "
                   "author following the guide omits the property and validation rejects "
                   "the result. 'Required; schema never requires it' over-promises instead, "
                   "which is harmless to validation but misleads implementers.",
    "divergence": "Either the same property documented at very different length in two "
                  "guides, or a property with a Cardinality bullet and no Description at "
                  "all. Some depth difference is legitimate -- a composite guide reasonably "
                  "says more than a module guide -- so this check needs human triage more "
                  "than the other two.",
}


def write_markdown(findings, path):
    """A grouped report for reading, rather than the flat stdout list."""
    from collections import defaultdict
    import datetime
    by_check = defaultdict(list)
    for kind, guide, line, name, msg in findings:
        by_check[kind].append((guide, line, name, msg))

    out = ["# Implementation guide consistency report", "",
           f"Generated {datetime.date.today().isoformat()} by `tools/audit_ig_consistency.py`.",
           "", f"**{len(findings)} findings** across {len(by_check)} checks.", "",
           "| check | findings | ", "|---|---|"]
    for kind in sorted(by_check):
        out.append(f"| [{kind}](#{kind}) | {len(by_check[kind])} |")
    out.append("")
    out.append("This tool detects; it does not rewrite. Every finding below is a place where "
               "a guide and the schema it describes disagree, or where two guides disagree "
               "with each other.")
    out.append("")

    for kind in sorted(by_check):
        rows = by_check[kind]
        out += [f"## {kind}", "", CHECK_BLURB.get(kind, ""), "",
                f"{len(rows)} findings.", ""]
        per_guide = defaultdict(list)
        for guide, line, name, msg in rows:
            per_guide[guide].append((line, name, msg))
        for guide in sorted(per_guide):
            out += [f"### {guide}", "", "| line | property | finding |", "|---|---|---|"]
            for line, name, msg in sorted(per_guide[guide]):
                loc = str(line) if line else "--"
                out.append(f"| {loc} | `{name}` | {msg} |")
            out.append("")
    Path(path).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {path} ({len(findings)} findings)")


def write_json(findings, path):
    rows = [{"check": k, "guide": g, "line": l, "property": n, "message": m}
            for k, g, l, n, m in findings]
    Path(path).write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(f"Wrote {path} ({len(rows)} findings)")


def report(findings):
    if not findings:
        print("No findings.")
        return
    by_check = {}
    for kind, guide, line, name, msg in findings:
        by_check.setdefault(kind, []).append((guide, line, name, msg))
    for kind in sorted(by_check):
        rows = by_check[kind]
        print(f"\n== {kind}  ({len(rows)})")
        for guide, line, name, msg in rows:
            loc = f"{guide}:{line}" if line else guide
            print(f"   {loc:34s} {name:38s} {msg}")
    print(f"\n{len(findings)} finding(s) across {len(by_check)} check(s).")


SELF_TEST_GUIDE = """# Fixture

## schema:Dataset

### schema:realProp

- **Cardinality:** Optional
- **Content:** string
- **Description:** A property the schema declares and does not require.

### schema:phantomProp

- **Cardinality:** Optional
- **Content:** string
- **Description:** A property no schema declares.

### schema:neverRequired

- **Cardinality:** Required
- **Content:** string
- **Description:** Guide claims required; schema never requires it.

### schema:alwaysRequired

- **Cardinality:** Optional
- **Content:** string
- **Description:** Guide claims optional; schema always requires it.

### schema:noDescription

- **Cardinality:** Optional
- **Content:** string

### name

- **Cardinality:** Required
- **Content:** string
- **Description:** Bare heading: means schema:name, which is required.
  cdif:name also exists and is never required.

### schema:sameLocalName

- **Cardinality:** Optional
- **Content:** string
- **Description:** Only cdif:sameLocalName exists; the prefix makes these different IRIs.

### schema:choiceMember

- **Cardinality:** Optional
- **Content:** string
- **Description:** Required only inside an anyOf branch, so genuinely optional.

### schema:inlineRequired

- **Cardinality:** Required
- **Content:** string
- **Description:** Required by a class sitting behind the sealed-reference idiom.

### schema:unionDiscriminator

- **Cardinality:** Required
- **Content:** string
- **Description:** Required by every branch of the union, so required outright.

### schema:choiceOther

- **Cardinality:** Required
- **Content:** string
- **Description:** Required by one branch of a union; documenting it as Required
  under that branch's class is correct and must not be reported.
"""

SELF_TEST_SCHEMA = {
    "type": "object",
    "properties": {
        "schema:realProp": {"type": "string"},
        "schema:phantomPropNOT": {"type": "string"},
        "schema:neverRequired": {"type": "string"},
        "schema:alwaysRequired": {"type": "string"},
        "schema:noDescription": {"type": "string"},
        "cdif:sameLocalName": {"type": "string"},
        "cdif:name": {"type": "string"},
        "schema:name": {"type": "string"},
        "schema:unionDiscriminator": {"type": "string"},
        "schema:choiceMember": {"type": "string"},
        "schema:choiceOther": {"type": "string"},
        "schema:multiA": {"type": "string"},
        "schema:multiB": {"type": "string"},
        "schema:escapeHatch": {"type": "string"},
    },
    "allOf": [
        {"required": ["schema:alwaysRequired", "schema:name"]},
        {"anyOf": [{"required": ["schema:choiceMember"]},
                   {"required": ["schema:choiceOther"]}]},
        # a branch requiring SEVERAL properties is not "at least one of"
        {"anyOf": [{"required": ["@type"]},
                   {"required": ["schema:multiA", "schema:multiB"]}]},
        # a branch satisfied by @id alone constrains nothing
        {"anyOf": [{"required": ["@id"]},
                   {"required": ["schema:escapeHatch"]}]},
        # every branch requires the discriminator -> unconditional
        {"anyOf": [{"required": ["schema:unionDiscriminator", "schema:realProp"]},
                   {"required": ["schema:unionDiscriminator", "schema:noDescription"]}]},
    ],
    "$defs": {
        "Thing": {
            "anyOf": [
                {"type": "object",
                 "properties": {"schema:inlineRequired": {"type": "string"}},
                 "required": ["schema:inlineRequired"]},
                {"type": "object", "additionalProperties": False,
                 "properties": {"@id": {"type": "string"}}, "required": ["@id"]},
            ]
        }
    },
}


def self_test():
    """Prove each check rejects a case it should. A check that has stopped
    matching reports zero findings, which is indistinguishable from a clean
    run -- so the tool must demonstrate it still fires."""
    import tempfile
    ok = True
    with tempfile.TemporaryDirectory() as td:
        gp = Path(td) / "XImplementationGuide.md"
        gp.write_text(SELF_TEST_GUIDE, encoding="utf-8")
        (declared, required_scopes, property_scopes, _rep,
         required_anywhere, choice_groups) = index_schema(SELF_TEST_SCHEMA)
        blocks = {b["name"]: b for b in read_guide(gp)}

        expectations = [
            ("schema:phantomProp", "undeclared",
             lambda n: n not in declared and not any(
                 d.split(":")[-1] == n.split(":")[-1] for d in declared)),
            ("schema:neverRequired", "cardinality-required",
             lambda n: states_required(blocks[n]["fields"]["cardinality"])
                       and n not in required_anywhere),
            ("schema:alwaysRequired", "cardinality-optional",
             lambda n: states_optional(blocks[n]["fields"]["cardinality"])
                       and required_scopes.get(n, set()) >= property_scopes.get(n, set())),
            ("schema:noDescription", "missing-description",
             lambda n: "cardinality" in blocks[n]["fields"]
                       and not blocks[n]["fields"].get("description")),
            ("schema:realProp", "clean (must NOT fire)",
             lambda n: not (states_required(blocks[n]["fields"]["cardinality"])
                            and n not in required_anywhere)
                       and bool(blocks[n]["fields"].get("description"))),
            # A prefixed name must not match a different prefix's local name,
            # or the undeclared check silently stops being able to fail.
            ("schema:sameLocalName", "undeclared despite local-name twin",
             lambda n: n not in declared),
            # Required inside an anyOf branch is a choice, not a mandate.
            ("schema:choiceMember", "anyOf choice is NOT mandatory",
             lambda n: not (required_scopes.get(n, set())
                            >= property_scopes.get(n, set()))),
            # ...but the sealed-reference idiom is a content alternative, so the
            # inline branch's requirements are real. "Required" here is correct
            # and must not be reported.
            ("schema:inlineRequired", "ref-idiom inline requirement is real",
             lambda n: bool(required_scopes.get(n))),
            # Required in one branch of a subclass union: a guide documenting it
            # as Required under that subclass is correct, so nothing may fire.
            ("schema:choiceOther", "branch requirement counts as required-somewhere",
             lambda n: n in required_anywhere),
            # `anyOf: [{required:[a]}, {required:[b]}]` is "at least one of": the
            # GROUP is mandatory even though neither member is. Documenting a
            # member as plain "Optional" is wrong -- omit them all and the record
            # fails -- and the tool was silent on every phrasing until 2026-09-24.
            ("schema:choiceMember", "'at least one of' group is detected",
             lambda n: {m for _scope, m in choice_groups.get(n, set())}
                       == {frozenset({"schema:choiceMember", "schema:choiceOther"})}),
            # The correct phrasing states the disjunction and must stay silent.
            ("schema:choiceMember", "conditional phrasing accepted",
             lambda n: not states_required("Required if no schema:choiceOther")
                       and not states_optional("Required if no schema:choiceOther")),
            # A name required by EVERY branch is required however the choice
            # resolves -- @type across a subclass union.
            ("schema:unionDiscriminator", "required in all branches => unconditional",
             lambda n: bool(required_scopes.get(n))),
            # A bare heading means the schema.org property. Resolving "name"
            # to cdif:name (alphabetically first) reported schema:name --
            # required in two scopes -- as never required.
            # union-across-branches wrongly read "@type OR (a AND b)" as
            # "at least one of @type, a, b" -- 12 confident false findings.
            ("schema:choiceMember", "multi-property branch is NOT a choice group",
             lambda n: not any("schema:multiA" in m
                               for _s, m in choice_groups.get("schema:multiA", set()))),
            ("schema:choiceMember", "@id escape hatch is NOT a choice group",
             lambda n: not choice_groups.get("schema:escapeHatch")),
            ("name", "bare heading resolves to schema:, not the first prefix",
             lambda n: resolve_bare(n, declared) == "schema:name"
                       and not (states_required(blocks[n]["fields"]["cardinality"])
                                and resolve_bare(n, declared) not in required_anywhere)),
        ]
        for name, label, pred in expectations:
            if name not in blocks:
                print(f"  FAIL  {label}: fixture block {name} not parsed"); ok = False; continue
            fired = pred(name)
            print(f"  {'ok  ' if fired else 'FAIL'}  {label:28s} {name}")
            ok = ok and fired
    print("\nself-test PASSED" if ok else "\nself-test FAILED")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-c", "--check", action="append", choices=CHECKS,
                    help="run only this check (repeatable); default is all")
    ap.add_argument("-g", "--guide", help="limit to one release repo, e.g. profile-core")
    ap.add_argument("--strict", action="store_true", help="exit 1 if anything is found")
    ap.add_argument("--self-test", action="store_true",
                    help="prove each check still fires on a case it must reject")
    ap.add_argument("-o", "--out", help="write a grouped report to this path "
                                        "(.md for markdown, .json for JSON)")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    findings = audit(set(args.check or CHECKS), args.guide)
    if args.out:
        if args.out.endswith(".json"):
            write_json(findings, args.out)
        else:
            write_markdown(findings, args.out)
    else:
        report(findings)
    return 1 if (args.strict and findings) else 0


if __name__ == "__main__":
    sys.exit(main())
