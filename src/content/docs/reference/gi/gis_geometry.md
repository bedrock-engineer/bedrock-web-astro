---
sidebar_label: gis_geometry
title: bedrock_ge.gi.gis_geometry
prev: false
next: false
---

#### calculate\_gis\_geometry

```python
def calculate_gis_geometry(
        no_gis_brgi_db: Dict[str, Union[pd.DataFrame, gpd.GeoDataFrame]],
        verbose: bool = True) -> Dict[str, gpd.GeoDataFrame]
```

Calculates GIS geometry for tables in a Bedrock Ground Investigation database.

This function processes a dictionary of DataFrames containing Ground Investigation (GI) data,
adding appropriate GIS geometry to each table. It handles both 2D and 3D geometries,
including vertical boreholes and sampling locations.

**Arguments**:

- `no_gis_brgi_db` _Dict[str, Union[pd.DataFrame, gpd.GeoDataFrame]]_ - Dictionary containing
  the Bedrock GI database tables without GIS geometry. Keys are table names,
  values are either pandas DataFrames or GeoDataFrames.
- `verbose` _bool, optional_ - Whether to print progress information. Defaults to True.
  

**Returns**:

  Dict[str, gpd.GeoDataFrame]: Dictionary containing the Bedrock GI database tables
  with added GIS geometry. All tables are converted to GeoDataFrames with
  appropriate CRS and geometry columns.
  

**Raises**:

- `ValueError` - If the projects in the database use different Coordinate Reference Systems (CRS).
  

**Notes**:

  The function performs the following operations:
  
  1. Verifies all projects use the same CRS
  2. Calculates GIS geometry for the &#x27;Location&#x27; table
  3. Creates a &#x27;LonLatHeight&#x27; table for 2D visualization
  4. Processes &#x27;Sample&#x27; table if present
  5. Processes all tables starting with &quot;InSitu_&quot;

#### calculate\_location\_gis\_geometry

```python
def calculate_location_gis_geometry(brgi_location: Union[pd.DataFrame,
                                                         gpd.GeoDataFrame],
                                    crs: CRS) -> gpd.GeoDataFrame
```

Calculates GIS geometry for a set of Ground Investigation locations.

**Arguments**:

- `brgi_location` _Union[pd.DataFrame, gpd.GeoDataFrame]_ - The GI locations to calculate GIS geometry for.
- `crs` _pyproj.CRS_ - The Coordinate Reference System (CRS) to use for the GIS geometry.
  

**Returns**:

- `gpd.GeoDataFrame` - The GIS geometry for the given GI locations, with additional columns:
  - longitude: The longitude of the location in the WGS84 CRS.
  - latitude: The latitude of the location in the WGS84 CRS.
  - wgs84_ground_level_height: The height of the ground level of the location in the WGS84 CRS.
  - elevation_at_base: The elevation at the base of the location.
  - geometry: The GIS geometry of the location.

#### calculate\_wgs84\_coordinates

```python
def calculate_wgs84_coordinates(
    from_crs: CRS,
    easting: float,
    northing: float,
    elevation: Union[float,
                     None] = None) -> Tuple[float, float, (float | None)]
```

Transforms coordinates from an arbitrary Coordinate Reference System (CRS) to the WGS84 CRS, which is the standard for geodetic coordinates.

**Arguments**:

- `from_crs` _pyproj.CRS_ - The pyproj.CRS object of the CRS to transform from.
- `easting` _float_ - The easting coordinate of the point to transform.
- `northing` _float_ - The northing coordinate of the point to transform.
- `elevation` _float or None, optional_ - The elevation of the point to
  transform. Defaults to None.
  

**Returns**:

  Tuple[float, float, (float | None)]: A tuple containing the longitude, latitude
  and WGS84 height of the transformed point, in that order.
  The height is None if no elevation was given, or if the provided CRS doesn&#x27;t
  have a proper datum defined.

#### create\_lon\_lat\_height\_table

```python
def create_lon_lat_height_table(brgi_location: gpd.GeoDataFrame,
                                crs: CRS) -> gpd.GeoDataFrame
```

Creates a GeoDataFrame with GI locations in WGS84 (lon, lat, height) coordinates.

The &#x27;LonLatHeight&#x27; table makes it easier to visualize the GIS geometry on 2D maps,
because vertical lines are often very small or completely hidden in 2D. This table
only contains the 3D point of the GI locations at ground level, in WGS84 (Longitude,
Latitude, Height) coordinates. Other attributes, such as the location type, sample
type, geology description, etc., can be attached to this table by joining, i.e.
merging those tables on the location_uid key.

**Arguments**:

- `brgi_location` _GeoDataFrame_ - The GeoDataFrame with the GI locations.
- `crs` _CRS_ - The Coordinate Reference System of the GI locations.
  

**Returns**:

- `gpd.GeoDataFrame` - The &#x27;LonLatHeight&#x27; GeoDataFrame.

#### calculate\_in\_situ\_gis\_geometry

```python
def calculate_in_situ_gis_geometry(brgi_in_situ: Union[pd.DataFrame,
                                                       gpd.GeoDataFrame],
                                   brgi_location: Union[pd.DataFrame,
                                                        gpd.GeoDataFrame],
                                   crs: CRS) -> gpd.GeoDataFrame
```

Calculates GIS geometry for a set of Ground Investigation in-situ data.

**Arguments**:

- `brgi_in_situ` _Union[pd.DataFrame, gpd.GeoDataFrame]_ - The in-situ data to calculate GIS geometry for.
- `brgi_location` _Union[pd.DataFrame, gpd.GeoDataFrame]_ - The location data to merge with the in-situ data.
- `crs` _CRS_ - The Coordinate Reference System of the in-situ data.
  

**Returns**:

- `gpd.GeoDataFrame` - The GIS geometry for the given in-situ data, with additional columns:
  - elevation_at_top: The elevation at the top of the in-situ data.
  - elevation_at_base: The elevation at the base of the in-situ data.
  - geometry: The GIS geometry of the in-situ data.

