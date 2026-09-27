## Optional XAS metadata fields

Genuinely-optional X-ray absorption spectroscopy (XAS) properties layered on `cdifCore`.
This module adds **no requirements** — it documents and permits optional XAS content that
appears only when the corresponding measurements exist. It is composed once by the `xasDocument`
profile alongside the required-constraints module `xasCore`.

### 1. Data-array variables (`schema:variableMeasured`)

Optional `cdi:InstanceVariable` / `schema:PropertyValue` items describing the columns of an
XDI data array. Enforced by this schema when present (as `schema:variableMeasured` items):

`energy`, `i0`, `itrans`, `ifluor`, `irefer`, `mutrans`, `mufluor`, `murefer`,
`normtrans`, `normfluor`, `normrefer`, `chi`, `chi_re`, `chi_im`, `chi_mag`, `chi_pha`,
`k`, `r`, `angle`.

### 2. Beamline-operational parameters (`schema:additionalProperty` on the `xas:Beamline` entity)

Optional `schema:PropertyValue` entries carried on the beamline entity nested inside
`prov:wasGeneratedBy → prov:used[schema:instrument … xas:Beamline]`. Permitted `schema:propertyID`
values (open-world — other propertyIDs are also allowed):

`xas:flux`, `xas:spot_size`, `xas:website`, `xas:energy_range`, `xas:energy_resolution`,
`xas:scan_mode`.

### 3. Sample physico-chemical parameters (`schema:additionalProperty` on the `schema:object` sample)

Optional `schema:PropertyValue` entries carried on the material sample
(`prov:wasGeneratedBy → schema:object`, an `xasSample`). Permitted `schema:propertyID` values
(open-world):

the NeXus `NXsample/temperature` field, `xas:pressure`, `xas:ph`, `xas:eh`, `xas:concentration`, `xas:density`,
`xas:viscosity`, `xas:porosity`, `xas:opacity`, `xas:resistivity`, `xas:magnetic_field`,
`xas:magnetic_moment`, `xas:electric_field`, `xas:electrochemical_potential`, `xas:volume`.

> Groups 2 and 3 are documented here rather than constrained in the schema: CDIF is open-world,
> so these optional `additionalProperty` entries are already permitted, and a hard schema
> constraint on their `propertyID` would either be a no-op or wrongly reject other valid
> additional properties. The vocabularies above are the recommended XAS `propertyID`s.
