
# Spatial Extent (Schema)

`cdif.bbr.metadata.schemaorgProperties.spatialExtent` *v0.1*

Schema defining properties for documenting the spatial extent of a resource; based on science on schema.org. Defines properties: @type, schema:name, schema:geo, geosparql:hasGeometry. Uses building blocks: definedTerm (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Spatial Extent properties

Defines a set of properties for use describing the spatial extent of a resource for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile. Based on [ESIP science on schema.org recommendations](https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Dataset.md#spatial-coverage), with [option from Ocean Info Hub](https://book.oceaninfohub.org/thematics/spatial/README.html#simple-geosparql-wkt).

### Defined properties

- **@type** — must be schema:Place
- **schema:name** — place names or DefinedTerms with place name and URI
- **schema:geo** — point location (schema:GeoCoordinates with latitude/longitude), bounding box (schema:GeoShape with box), or curvilinear trace (schema:GeoShape with line)
- **geosparql:hasGeometry** — geographic extent using WKT geometry (geosparql:asWKT with optional coordinate reference system)

### Dependencies

- [definedTerm](../definedTerm/) — controlled vocabulary term for place names

## Examples

### Example spatial extent by point.
Example point location spatial extent instance.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "geosparql": "http://www.opengis.net/ont/geosparql#"
  },
  "@id": "ex:SpatialExtentPoint_mdfd8",
  "@type": "schema:Place",
  "schema:geo": {
    "@type": "schema:GeoCoordinates",
    "schema:latitude": 39.3280,
    "schema:longitude": 120.1633
  }
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "geosparql": "http://www.opengis.net/ont/geosparql#,",
      "sf": "http://www.opengis.net/ont/sf#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "geosparql": "http://www.opengis.net/ont/geosparql#"
    }
  ],
  "@id": "ex:SpatialExtentPoint_mdfd8",
  "@type": "schema:Place",
  "schema:geo": {
    "@type": "schema:GeoCoordinates",
    "schema:latitude": 39.328,
    "schema:longitude": 120.1633
  }
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:SpatialExtentPoint_mdfd8 a schema1:Place ;
    schema1:geo [ a schema1:GeoCoordinates ;
            schema1:latitude 3.9328e+01 ;
            schema1:longitude 1.201633e+02 ] .


```


### Example spatial extent by place names.
Example place names spatial extent instance.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "geosparql": "http://www.opengis.net/ont/geosparql#"
  },
  "@id": "ex:SpatialExtentPlaceName_45hwe6",
  "@type": "schema:Place",
  "schema:name": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Harquahala Mountains",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID":"http uri",
        "schema:url": "https://edits.nationalmap.gov/apps/gaz-domestic/public/gaz-record/5573"
      },
      "schema:inDefinedTermSet": "https://www.usgs.gov/us-board-on-geographic-names/domestic-names"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Socorro Peak",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID":"http uri",
        "schema:url": "https://edits.nationalmap.gov/apps/gaz-domestic/public/gaz-record/11520"
      },
      "schema:inDefinedTermSet": "https://www.usgs.gov/us-board-on-geographic-names/domestic-names"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Hidden Treasure Mine",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID":"http uri",
        "schema:url": "https://www.mindat.org/loc-33505.html"
      },
      "schema:inDefinedTermSet": "https://www.mindat.org/"
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "geosparql": "http://www.opengis.net/ont/geosparql#,",
      "sf": "http://www.opengis.net/ont/sf#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "geosparql": "http://www.opengis.net/ont/geosparql#"
    }
  ],
  "@id": "ex:SpatialExtentPlaceName_45hwe6",
  "@type": "schema:Place",
  "schema:name": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Harquahala Mountains",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "http uri",
        "schema:url": "https://edits.nationalmap.gov/apps/gaz-domestic/public/gaz-record/5573"
      },
      "schema:inDefinedTermSet": "https://www.usgs.gov/us-board-on-geographic-names/domestic-names"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Socorro Peak",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "http uri",
        "schema:url": "https://edits.nationalmap.gov/apps/gaz-domestic/public/gaz-record/11520"
      },
      "schema:inDefinedTermSet": "https://www.usgs.gov/us-board-on-geographic-names/domestic-names"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Hidden Treasure Mine",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "http uri",
        "schema:url": "https://www.mindat.org/loc-33505.html"
      },
      "schema:inDefinedTermSet": "https://www.mindat.org/"
    }
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:SpatialExtentPlaceName_45hwe6 a schema1:Place ;
    schema1:name [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "http uri" ;
                    schema1:url "https://www.mindat.org/loc-33505.html" ] ;
            schema1:inDefinedTermSet "https://www.mindat.org/" ;
            schema1:name "Hidden Treasure Mine" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "http uri" ;
                    schema1:url "https://edits.nationalmap.gov/apps/gaz-domestic/public/gaz-record/5573" ] ;
            schema1:inDefinedTermSet "https://www.usgs.gov/us-board-on-geographic-names/domestic-names" ;
            schema1:name "Harquahala Mountains" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "http uri" ;
                    schema1:url "https://edits.nationalmap.gov/apps/gaz-domestic/public/gaz-record/11520" ] ;
            schema1:inDefinedTermSet "https://www.usgs.gov/us-board-on-geographic-names/domestic-names" ;
            schema1:name "Socorro Peak" ] .


```


### Example spatial extent by line.
Example curvilinear trace spatial extent instance.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "geosparql": "http://www.opengis.net/ont/geosparql#"
  },
  "@id": "ex:SpatialExtentBox_my8",
  "@type": "schema:Place",
  "schema:geo": {
    "@type": "schema:GeoShape",
    "schema:line": "39.33 120.77 40.44 123.96 41.00 121.34"
  }
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "geosparql": "http://www.opengis.net/ont/geosparql#,",
      "sf": "http://www.opengis.net/ont/sf#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "geosparql": "http://www.opengis.net/ont/geosparql#"
    }
  ],
  "@id": "ex:SpatialExtentBox_my8",
  "@type": "schema:Place",
  "schema:geo": {
    "@type": "schema:GeoShape",
    "schema:line": "39.33 120.77 40.44 123.96 41.00 121.34"
  }
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:SpatialExtentBox_my8 a schema1:Place ;
    schema1:geo [ a schema1:GeoShape ;
            schema1:line "39.33 120.77 40.44 123.96 41.00 121.34" ] .


```


### Example spatial extent by bounding box.
Example bounding box spatial extent instance.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "geosparql": "http://www.opengis.net/ont/geosparql#"
  },
  "@id": "ex:SpatialExtentBox_my8",
  "@type": "schema:Place",
  "schema:geo": {
    "@type": "schema:GeoShape",
    "schema:box": "39.3280 120.1633 40.445 123.7878"
  }
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "geosparql": "http://www.opengis.net/ont/geosparql#,",
      "sf": "http://www.opengis.net/ont/sf#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "geosparql": "http://www.opengis.net/ont/geosparql#"
    }
  ],
  "@id": "ex:SpatialExtentBox_my8",
  "@type": "schema:Place",
  "schema:geo": {
    "@type": "schema:GeoShape",
    "schema:box": "39.3280 120.1633 40.445 123.7878"
  }
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:SpatialExtentBox_my8 a schema1:Place ;
    schema1:geo [ a schema1:GeoShape ;
            schema1:box "39.3280 120.1633 40.445 123.7878" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Spatial Extent description for CDIF discovery profile.  Note required
  prefix declaration for geoSparql ( http://www.opengis.net/ont/geosparql#) and OGC
  simple features (sf: http://www.opengis.net/ont/sf#)'
type: object
properties:
  '@type':
    default: schema:Place
    anyOf:
    - type: string
      const: schema:Place
    - type: array
      items:
        type: string
      contains:
        const: schema:Place
  schema:name:
    description: multiple place names or DefinedTerms that have a place name and URI
      for the location
    type: array
    items:
      anyOf:
      - type: string
      - $ref: '#/$defs/DefinedTerm'
  schema:geo:
    description: Either a bounding box or a point location.
    anyOf:
    - type: object
      description: A point location. Point locations are recommended for data that
        is associated with specific sample locations, particularly if these are widely
        spaced such that an enclosing bounding box would be a misleading representation
        of the spatial location. Be aware that some client applications might only
        index or display bounding box extents or a single point location.
      properties:
        '@type':
          default: schema:GeoCoordinates
          anyOf:
          - type: string
            const: schema:GeoCoordinates
          - type: array
            items:
              type: string
            contains:
              const: schema:GeoCoordinates
        schema:latitude:
          type: number
          minimum: -90
          maximum: 90
        schema:longitude:
          type: number
          minimum: -180
          maximum: 180
      required:
      - '@type'
      - schema:latitude
      - schema:longitude
    - type: object
      description: A schema:GeoShape bounding box. The geometry is described with
        a set of latitude/longitude pairs (in that order).The documentation for schema:GeoShape
        states 'Either whitespace or commas can be used to separate latitude and longitude;
        whitespace should be used when writing a list of several such points.'
      properties:
        '@type':
          default: schema:GeoShape
          anyOf:
          - type: string
            const: schema:GeoShape
          - type: array
            items:
              type: string
            contains:
              const: schema:GeoShape
        schema:box:
          type: string
          description: A GeoShape box defines an area on the surface of the earth
            defined by point locations of the southwest corner and northeast corner
            of the rectangle in latitude-longitude coordinates. A space should be
            used to separate the latitude and longitude values. The two corner coordinate
            points are separated by a space. 'East longitude' means positive longitude
            values are east of the prime (Greenwich) meridian.
      required:
      - '@type'
      - schema:box
    - type: object
      description: A schema:GeoShape curvilinear trace, for resource related to a
        linear trace like a ship track or airplane flight line
      properties:
        '@type':
          default: schema:GeoShape
          anyOf:
          - type: string
            const: schema:GeoShape
          - type: array
            items:
              type: string
            contains:
              const: schema:GeoShape
        schema:line:
          type: string
          description: 'A GeoShape box defines a curvilinear geometry as a string
            of latitude-longitude coordinates. A space should be used to separate
            the latitude and longitude values. The coordinate point pairs are also
            separated by a space. ''East longitude'' means positive longitude values
            are east of the prime (Greenwich) meridian. e.g. ''39.33 120.77 40.44
            123.96 41.00 121.34'' '
      required:
      - '@type'
      - schema:line
  geosparql:hasGeometry:
    type: object
    description: Optional geographic extent using wkt geometry, see Ocean InfoHub
      (https://book.oceaninfohub.org/thematics/spatial/README.html#simple-geosparql-wkt).
      Other geometry schemes might be specified in a specific domain profile, e.g.
      for atmospheric, subsurface data, or local coordinate systems. NOTE that the
      location specified here should be the same as the schema.org point or contained
      within the specified bounding box.
    properties:
      '@type':
        anyOf:
        - type: string
        - type: array
          items:
            type: string
        description: 'MUST be sf: (<http://www.opengis.net/ont/sf#>) SimpleFeature
          geometry type. See https://opengeospatial.github.io/ogc-geosparql/geosparql11/sf_geometries.ttl'
      geosparql:asWKT:
        type: object
        properties:
          '@type':
            anyOf:
            - type: string
              const: geosparql:wktLiteral
            - type: array
              items:
                type: string
              contains:
                const: geosparql:wktLiteral
          '@value':
            type: string
            description: a WKT geometry description string, e.g. 'POINT(-76 -18)'
      geosparql:crs:
        type: object
        properties:
          '@id':
            type: string
            description: identifier string for coordinate reference system, e.g.,
              'CRS84'
$defs:
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/context.jsonld)

## Sources

* [ESIP Science on Schema.org](https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Dataset.md#spatial-coverage)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/spatialExtent`

