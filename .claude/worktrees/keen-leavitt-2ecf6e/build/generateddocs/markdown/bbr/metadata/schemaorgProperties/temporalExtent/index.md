
# Temporal Extent properites (Schema)

`cdif.bbr.metadata.schemaorgProperties.temporalExtent` *v0.1*

Schema defining metadata elements to document the temporal extent applicable to the described resource. Defines properties: @type, schema:description, time:intervalStartedBy, time:intervalFinishedBy, @context, time:hasBeginning, time:hasEnd.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Temporal extent properties

Defines a set of properties for use describing a the temporal extent related to a resource, for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile. The schema allows a string value (consistent with expected type for schema.org temporalCoverage), or use of w3c time temporalInterval. The temporalInterval implemenation adds a schema:description property to allow text description of the interval, including information about determination method and uncertainty. 

If a document declares conformance with a profile that includes a schema:temporalCoverage property, and a schema:temporalCoverage property is present in the document, the processor should look for an ISO8601 string value, or a  time:ProperInterval object, and if that's present, then look for a description (string), or either time:intervalStartedBy/intervalEndedBy (with URIs that mean something) or time:hasBeginning/hasEnd, with numeric values and a reference system so they know how to interpret the values.  Lots of other owl time elements might be floating around, and if the processor is inclined, they might try and do something with those, but by default they just ignore them. If a temporalCoverage value object is not rdf:typed time:ProperInterval, the json validator will throw an error. Currently there isn't a regex in the schema to test ISO8601 conformance for the string, so any string will validate.
## Examples

### Example Temporal extent.
Example temporal extent instance, interval defined by time positions in m.y.b.p.
#### json
```json
{
  "@context": {
    "time": "http://www.w3.org/2006/time#",
    "schema": "http://schema.org/"
  },
  "@type": [
    "time:ProperInterval"
  ],
  "schema:description": "Description of the time interval",
  "time:hasBeginning": {
    "@type": [
      "time:Instant"
    ],
    "time:inTimePosition": {
      "@type": [
        "time:TimePosition"
      ],
      "time:hasTRS": "http://www.opengis.net/def/crs/OGC/0/ChronometricGeologicTime",
      "time:numericPosition": 52
    }
  },
  "time:hasEnd": {
    "@type": [
      "time:Instant"
    ],
    "time:inTimePosition": {
      "@type": [
        "time:TimePosition"
      ],
      "time:hasTRS": "http://www.opengis.net/def/crs/OGC/0/ChronometricGeologicTime",
      "time:numericPosition": 29
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org",
      "time": "http://www.w3.org/2006/time#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/temporalExtent/context.jsonld",
    {
      "time": "http://www.w3.org/2006/time#",
      "schema": "http://schema.org/"
    }
  ],
  "@type": [
    "time:ProperInterval"
  ],
  "schema:description": "Description of the time interval",
  "time:hasBeginning": {
    "@type": [
      "time:Instant"
    ],
    "time:inTimePosition": {
      "@type": [
        "time:TimePosition"
      ],
      "time:hasTRS": "http://www.opengis.net/def/crs/OGC/0/ChronometricGeologicTime",
      "time:numericPosition": 52
    }
  },
  "time:hasEnd": {
    "@type": [
      "time:Instant"
    ],
    "time:inTimePosition": {
      "@type": [
        "time:TimePosition"
      ],
      "time:hasTRS": "http://www.opengis.net/def/crs/OGC/0/ChronometricGeologicTime",
      "time:numericPosition": 29
    }
  }
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a time:ProperInterval ;
    schema1:description "Description of the time interval" ;
    time:hasBeginning [ a time:Instant ;
            time:inTimePosition [ a time:TimePosition ;
                    time:hasTRS "http://www.opengis.net/def/crs/OGC/0/ChronometricGeologicTime" ;
                    time:numericPosition 52 ] ] ;
    time:hasEnd [ a time:Instant ;
            time:inTimePosition [ a time:TimePosition ;
                    time:hasTRS "http://www.opengis.net/def/crs/OGC/0/ChronometricGeologicTime" ;
                    time:numericPosition 29 ] ] .


```


### Complete temporal extent example.
Temporal extent instance exercising all properties across the ordinal era
and numeric age options: description, intervalStartedBy, intervalFinishedBy,
hasBeginning/hasEnd with TimePosition (hasTRS, numericPosition).
#### json
```json
{
  "@context": {
    "time": "http://www.w3.org/2006/time#",
    "schema": "http://schema.org/"
  },
  "@type": ["time:ProperInterval"],
  "schema:description": "Late Cretaceous to early Paleogene interval, approximately 72 to 56 million years before present",
  "time:intervalStartedBy": "http://resource.geosciml.org/classifier/ics/ischart/Maastrichtian",
  "time:intervalFinishedBy": "http://resource.geosciml.org/classifier/ics/ischart/Thanetian",
  "time:hasBeginning": {
    "@type": ["time:Instant"],
    "time:inTimePosition": {
      "@type": ["time:TimePosition"],
      "time:hasTRS": "http://www.opengis.net/def/crs/OGC/0/ChronometricGeologicTime",
      "time:numericPosition": 72.1
    }
  },
  "time:hasEnd": {
    "@type": ["time:Instant"],
    "time:inTimePosition": {
      "@type": ["time:TimePosition"],
      "time:hasTRS": "http://www.opengis.net/def/crs/OGC/0/ChronometricGeologicTime",
      "time:numericPosition": 56.0
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "time": "http://www.w3.org/2006/time#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/temporalExtent/context.jsonld",
    {
      "time": "http://www.w3.org/2006/time#",
      "schema": "http://schema.org/"
    }
  ],
  "@type": [
    "time:ProperInterval"
  ],
  "schema:description": "Late Cretaceous to early Paleogene interval, approximately 72 to 56 million years before present",
  "time:intervalStartedBy": "http://resource.geosciml.org/classifier/ics/ischart/Maastrichtian",
  "time:intervalFinishedBy": "http://resource.geosciml.org/classifier/ics/ischart/Thanetian",
  "time:hasBeginning": {
    "@type": [
      "time:Instant"
    ],
    "time:inTimePosition": {
      "@type": [
        "time:TimePosition"
      ],
      "time:hasTRS": "http://www.opengis.net/def/crs/OGC/0/ChronometricGeologicTime",
      "time:numericPosition": 72.1
    }
  },
  "time:hasEnd": {
    "@type": [
      "time:Instant"
    ],
    "time:inTimePosition": {
      "@type": [
        "time:TimePosition"
      ],
      "time:hasTRS": "http://www.opengis.net/def/crs/OGC/0/ChronometricGeologicTime",
      "time:numericPosition": 56.0
    }
  }
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a time:ProperInterval ;
    schema1:description "Late Cretaceous to early Paleogene interval, approximately 72 to 56 million years before present" ;
    time:hasBeginning [ a time:Instant ;
            time:inTimePosition [ a time:TimePosition ;
                    time:hasTRS "http://www.opengis.net/def/crs/OGC/0/ChronometricGeologicTime" ;
                    time:numericPosition 7.21e+01 ] ] ;
    time:hasEnd [ a time:Instant ;
            time:inTimePosition [ a time:TimePosition ;
                    time:hasTRS "http://www.opengis.net/def/crs/OGC/0/ChronometricGeologicTime" ;
                    time:numericPosition 5.6e+01 ] ] ;
    time:intervalFinishedBy "http://resource.geosciml.org/classifier/ics/ischart/Thanetian" ;
    time:intervalStartedBy "http://resource.geosciml.org/classifier/ics/ischart/Maastrichtian" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'The time interval during which data was collected or observations were
  made; or a time period that an activity or collection is linked to intellectually
  or thematically (for example, 1997 to 1998; the 18th century) (see https://documentation.ardc.edu.au/display/DOC/Temporal+coverage).
  For documentation of Earth Science, Paleobiology or Paleontology datasets, we are
  interested in the second case-- the time period that data are linked to thematically.
  NOTE-- context must include "time": "http://www.w3.org/2006/time#"}'
anyOf:
- type: object
  description: a w3c time proper interval with bounds that are named time ordinal
    eras with identifier, e.g. geologic age. This is a SOSO schema.org extension
  properties:
    '@type':
      default: time:ProperInterval
      type: array
      items:
        type: string
      contains:
        const: time:ProperInterval
      minItems: 1
    schema:description:
      type: string
      description: free text description of the temporal interval
    time:intervalStartedBy:
      type: string
      format: uri
      description: 'identifier for a named time ordinal era that is older bound of
        time interval, e.g. ''isc:LowerDevonian'' '
    time:intervalFinishedBy:
      type: string
      format: uri
      description: 'identifier for a named time ordinal era that is younger bound
        of time interval, e.g. ''isc:LowerDevonian'' '
  anyOf:
  - required:
    - time:intervalStartedBy
  - required:
    - time:intervalFinishedBy
- type: object
  description: a w3c time proper interval with bounds that numeric ages.
  properties:
    '@context':
      type: object
      properties:
        time:
          type: string
          const: http://www.w3.org/2006/time#
        schema:
          type: string
          const: http://schema.org/
      required:
      - time
      - schema
      additionalProperties: true
      description: Must exactly match the specified @context object.
    '@type':
      default: time:ProperInterval
      type: array
      items:
        type: string
      contains:
        const: time:ProperInterval
      minItems: 1
    schema:description:
      type: string
      description: free text description of the temporal interval
    time:hasBeginning:
      type: object
      properties:
        '@type':
          type: array
          items:
            type: string
          contains:
            const: time:Instant
          minItems: 1
        time:inTimePosition:
          $ref: '#/$defs/timePosition_type'
    time:hasEnd:
      type: object
      properties:
        '@type':
          type: array
          items:
            type: string
          contains:
            const: time:Instant
          minItems: 1
        time:inTimePosition:
          $ref: '#/$defs/timePosition_type'
  anyOf:
  - required:
    - time:hasBeginning
  - required:
    - time:hasEnd
- type: string
  description: Simple ISO8601 encoding of calendar date, dateTime, or time interval
    with calendar date bounds
$defs:
  timePosition_type:
    type: object
    properties:
      '@type':
        default: time:TimePosition
        type: array
        items:
          type: string
        contains:
          const: time:TimePosition
        minItems: 1
      time:hasTRS:
        type: string
        description: identifier for a temporal reference system; default is million
          years before prsent as a decimal number
        default: http://www.opengis.net/def/crs/OGC/0/ChronometricGeologicTime
      time:numericPosition:
        type: number
    required:
    - '@type'
    - time:hasTRS
    - time:numericPosition
x-jsonld-prefixes:
  schema: http://schema.org/
  time: http://www.w3.org/2006/time#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/temporalExtent/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/temporalExtent/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "time": "http://www.w3.org/2006/time#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/temporalExtent/context.jsonld)

## Sources

* [schema.org](https://schema.org/Person)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/temporalExtent`

