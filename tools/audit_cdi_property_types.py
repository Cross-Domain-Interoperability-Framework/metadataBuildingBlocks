"""One-shot audit: for each cdi:X property in cdifProperties schemas, compare
the value type it allows against the XMI's UML attribute definition.

Output format: per cdi:X property, list each cdifProperties usage with its
allowed value type, paired with the XMI-declared target class(es) for that
attribute. Flag obvious mismatches (e.g., scalar string in cdifProperties when
XMI says target is a class).
"""
import re
import sys
import yaml
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
XMI = Path(r'C:/Users/smrTu/OneDrive/Documents/GithubC/CDIF/to-canonical-xmi/ddi-cdi_canonical-unique-names.xmi')

XT = '{http://www.omg.org/spec/XMI/20131001}type'
XID = '{http://www.omg.org/spec/XMI/20131001}id'
XREF = '{http://www.omg.org/spec/XMI/20131001}idref'


def parse_xmi():
    """Build {attr_name: [{owner, target_type, lower, upper}]} and id->name map."""
    tree = ET.parse(XMI)
    m = tree.getroot().find('{http://www.omg.org/spec/UML/20131001}Model')
    id_to_name = {}
    for el in m.iter():
        if el.tag == 'packagedElement':
            xid = el.attrib.get(XID)
            n = el.find('name')
            if xid and n is not None and n.text:
                id_to_name[xid] = n.text
    # Primitives like String/Integer/Boolean live in PrimitiveType
    # uml:DataType, uml:Enumeration also tracked

    attrs = defaultdict(list)
    # Pass 1: class-owned ownedAttribute (composition / scalar attrs)
    for cls in m.iter():
        if cls.tag != 'packagedElement':
            continue
        if cls.attrib.get(XT) not in ('uml:Class', 'uml:DataType'):
            continue
        cls_name_el = cls.find('name')
        cls_name = cls_name_el.text if cls_name_el is not None else '?'
        for oa in cls.findall('ownedAttribute'):
            name_el = oa.find('name')
            type_el = oa.find('type')
            lower_el = oa.find('lowerValue')
            upper_el = oa.find('upperValue')
            attr_name = name_el.text if name_el is not None and name_el.text else None
            type_id = type_el.attrib.get(XREF) if type_el is not None else None
            target = id_to_name.get(type_id, type_id) if type_id else None
            lower = lower_el.attrib.get('value', '1') if lower_el is not None else '1'
            upper = upper_el.attrib.get('value', '1') if upper_el is not None else '1'
            if attr_name:
                attrs[attr_name].append({
                    'owner': cls_name,
                    'target': target,
                    'lower': lower,
                    'upper': upper,
                    'kind': 'attr',
                })
    # Pass 1b: recover role names from association names <owner>_<role>_<target>.
    # In this XMI the role-named end is an unnamed ownedAttribute on the owning
    # class; the association name carries the actual role name.
    # Find each Association and pair its name with its memberEnd→type pointers.
    for assoc in m.iter():
        if assoc.tag != 'packagedElement':
            continue
        if assoc.attrib.get(XT) != 'uml:Association':
            continue
        a_name_el = assoc.find('name')
        a_name = a_name_el.text if a_name_el is not None else None
        if not a_name or a_name.count('_') < 2:
            continue
        # Split <owner>_<role>_<target> (greedy — first '_' splits owner, last '_' splits target)
        first_us = a_name.find('_')
        last_us = a_name.rfind('_')
        owner_name = a_name[:first_us]
        target_name = a_name[last_us + 1:]
        role = a_name[first_us + 1:last_us]
        # Find the owned-attribute (on owner class) end that references this association
        # to recover multiplicity.
        ends = assoc.findall('ownedEnd')
        member_refs = [me.attrib.get(XREF) for me in assoc.findall('memberEnd')]
        lower, upper = '0', '*'
        for ref in member_refs:
            for el in m.iter():
                if el.attrib.get(XID) == ref:
                    lo = el.find('lowerValue')
                    up = el.find('upperValue')
                    if lo is not None or up is not None:
                        lower = lo.attrib.get('value', '0') if lo is not None else '0'
                        upper = up.attrib.get('value', '*') if up is not None else '*'
                    break
        attrs[role].append({
            'owner': owner_name,
            'target': target_name,
            'lower': lower,
            'upper': upper,
            'kind': 'assoc-role',
        })
    # Pass 2: uml:Association ownedEnd pairs (binary associations).
    # Each association has two ownedEnd entries; the "source" of an association
    # end is the OTHER end's type (i.e. the class on the other side owns the
    # role-named end). We treat both directions.
    for assoc in m.iter():
        if assoc.tag != 'packagedElement':
            continue
        if assoc.attrib.get(XT) != 'uml:Association':
            continue
        ends = assoc.findall('ownedEnd')
        # Build (name, type_id, lower, upper) for each end
        end_info = []
        for e in ends:
            n_el = e.find('name')
            t_el = e.find('type')
            lo_el = e.find('lowerValue')
            up_el = e.find('upperValue')
            end_info.append({
                'name': n_el.text if n_el is not None else None,
                'type_id': t_el.attrib.get(XREF) if t_el is not None else None,
                'lower': lo_el.attrib.get('value', '1') if lo_el is not None else '1',
                'upper': up_el.attrib.get('value', '1') if up_el is not None else '1',
            })
        # For each named end, the *owner* is the OTHER end's type, the *target*
        # is the named end's own type. Multiplicity refers to the named end.
        if len(end_info) == 2:
            for i, end in enumerate(end_info):
                if not end['name']:
                    continue
                other = end_info[1 - i]
                owner = id_to_name.get(other['type_id'], other['type_id']) or '?'
                target = id_to_name.get(end['type_id'], end['type_id']) or '?'
                attrs[end['name']].append({
                    'owner': owner,
                    'target': target,
                    'lower': end['lower'],
                    'upper': end['upper'],
                    'kind': 'assoc',
                })
    return attrs


def find_cdi_property_value(node, key):
    """Yield (path, value_schema_dict) for each cdi:KEY property in a nested YAML schema."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k == key:
                yield v
            else:
                yield from find_cdi_property_value(v, key)
    elif isinstance(node, list):
        for item in node:
            yield from find_cdi_property_value(item, key)


def describe_value_schema(v):
    """One-line summary of what a JSON Schema value definition allows."""
    if not isinstance(v, dict):
        return repr(v)
    if 'enum' in v:
        return f"enum({len(v['enum'])} values)"
    if '$ref' in v:
        return f"$ref->{Path(v['$ref'].split('#')[0]).name}{('#'+v['$ref'].split('#')[1]) if '#' in v['$ref'] else ''}"
    parts = []
    if 'type' in v:
        parts.append(f"type={v['type']}")
    if 'items' in v and isinstance(v['items'], dict):
        inner = describe_value_schema(v['items'])
        parts.append(f"items[{inner}]")
    if 'anyOf' in v:
        opts = [describe_value_schema(x) for x in v['anyOf']]
        parts.append(f"anyOf[{' | '.join(opts)}]")
    if 'oneOf' in v:
        opts = [describe_value_schema(x) for x in v['oneOf']]
        parts.append(f"oneOf[{' | '.join(opts)}]")
    if 'allOf' in v:
        parts.append(f"allOf({len(v['allOf'])})")
    if 'contains' in v:
        c = v['contains']
        if isinstance(c, dict) and 'const' in c:
            parts.append(f"contains={c['const']}")
    if 'const' in v:
        parts.append(f"const={v['const']}")
    if 'properties' in v:
        parts.append(f"props={sorted(v['properties'].keys())[:3]}...")
    return ', '.join(parts) if parts else 'object'


def classify_mismatch(value_desc, xmi_target):
    """Heuristic mismatch flag."""
    if xmi_target is None:
        return None  # no XMI info
    # Common primitive-class names in DDI-CDI XMI
    primitives = {'String', 'Integer', 'Boolean', 'Date', 'DateTime'}
    if xmi_target in primitives:
        # XMI says primitive scalar; cdifProperties allowing complex object is a mismatch
        if 'type=object' in value_desc or 'props=' in value_desc:
            return 'XMI primitive but cdif allows object'
        return None
    # XMI says a class (e.g. InternationalString, Identifier, Reference)
    # cdif allowing 'type=string' standalone is a structural mismatch
    if value_desc.strip().startswith('type=string') and 'items' not in value_desc:
        return f'XMI target={xmi_target} (class) but cdif allows plain string'
    return None


def main():
    print('Loading XMI...', file=sys.stderr)
    xmi_attrs = parse_xmi()
    print(f'  {len(xmi_attrs)} distinct attribute names in XMI', file=sys.stderr)

    # Find every cdi:X usage in CDIF schemas (data types + profile modules)
    schemas = sorted(ROOT.glob('_sources/cdifDataType/*/schema.yaml'))
    schemas += sorted(ROOT.glob('_sources/profiles/cdifProfile/*/schema.yaml'))
    findings = defaultdict(list)  # property_name -> list of (bb_name, value_desc)
    cdi_re = re.compile(r"^cdi:([A-Za-z_]+)$")

    for s in schemas:
        bb = s.parent.name
        try:
            data = yaml.safe_load(s.read_text(encoding='utf-8'))
        except Exception as e:
            print(f'  WARN: cant parse {s}: {e}', file=sys.stderr)
            continue
        # Walk to find every dict key that matches cdi:X
        def walk(node):
            if isinstance(node, dict):
                for k, v in node.items():
                    if isinstance(k, str):
                        m = cdi_re.match(k)
                        if m:
                            findings[k].append((bb, describe_value_schema(v)))
                    walk(v)
            elif isinstance(node, list):
                for item in node:
                    walk(item)
        walk(data)

    # Report
    print('\n# cdi:X property audit — cdifProperties vs XMI')
    print(f'# {len(findings)} distinct cdi: properties used in cdifProperties\n')
    for prop in sorted(findings):
        local_name = prop.split(':', 1)[1]
        xmi_defs = xmi_attrs.get(local_name, [])
        # Fallback: disambiguated role pattern "role_TargetClass"
        if not xmi_defs and '_' in local_name:
            last_us = local_name.rfind('_')
            base = local_name[:last_us]
            target_filter = local_name[last_us + 1:]
            base_defs = xmi_attrs.get(base, [])
            xmi_defs = [d for d in base_defs if d.get('target') == target_filter]
        print(f'\n## {prop}')
        if not xmi_defs:
            print(f'  XMI: (no attribute named {local_name!r} found)')
        else:
            for d in xmi_defs:
                print(f'  XMI: {d["owner"]}.{local_name} -> {d["target"]} (mult {d["lower"]}..{d["upper"]})')
        print('  cdifProperties usages:')
        seen = set()
        for bb, desc in findings[prop]:
            key = (bb, desc)
            if key in seen:
                continue
            seen.add(key)
            flag = ''
            if xmi_defs:
                # Use first target type as canonical for the heuristic
                m = classify_mismatch(desc, xmi_defs[0]['target'])
                if m:
                    flag = f'  !! {m}'
            print(f'    [{bb}] {desc}{flag}')


if __name__ == '__main__':
    main()
