## DDE Imagery Properties

Conditional extension for imagery resources. Implements the MD_Imagery entity from DDE spec Table 3 / XSD. This building block is composed into the DDEImage profile when describing remote sensing or other imagery datasets.

All properties are optional. Value types are constrained per the XSD type definitions.

### Properties via `schema:additionalProperty`

Each item is a typed `schema:PropertyValue` with a DDE `propertyID`:

- **`dde:sensorType`**: Type of sensor (e.g., "Multispectral", "SAR", "LiDAR"). Value: string.
- **`dde:platform`**: Platform carrying the sensor (e.g., "Landsat-8", "Sentinel-2A"). Value: string.
- **`dde:equipment`**: Equipment used for acquisition. Value: string.
- **`dde:collector`**: Person or organization that collected the imagery. Value: string. (Not in XSD MD_Imagery; included from spec table.)
- **`dde:signalGenerator`**: Type of signal used (e.g., "Passive solar", "Active radar"). Value: string.
- **`dde:wavelength`**: Wavelength range (e.g., "0.45-0.52 micrometers"). Value: string.
- **`dde:processedLevel`**: Processing level. Value from `ProcessingLevelCode` enum: Level0, Level1, Level2, Level3, Level4.

### Direct properties

- **`schema:startTime`**: Start time of acquisition (ISO 8601). Not in XSD; from spec table.
- **`schema:endTime`**: End time of acquisition (ISO 8601). Not in XSD; from spec table.
