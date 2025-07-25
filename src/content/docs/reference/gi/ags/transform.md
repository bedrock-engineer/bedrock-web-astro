---
sidebar_label: transform
title: bedrock_ge.gi.ags.transform
prev: false
next: false
---

Transforms, i.e. maps, AGS data to Bedrock&#x27;s schema.

## Ags3HOLE

## Ags3SAMP

## BaseSAMP

## BaseInSitu

## BaseLocation

## BaseSample

## Project

## check\_foreign\_key

#### ags3\_db\_to\_no\_gis\_brgi\_db

```python
def ags3_db_to_no_gis_brgi_db(ags3_db: Dict[str, pd.DataFrame],
                              crs: CRS) -> Dict[str, pd.DataFrame]
```

Maps a database with GI data from a single AGS 3 file to a database with Bedrock&#x27;s schema.

This function converts an AGS 3 formatted geotechnical database into Bedrock&#x27;s
internal database format, maintaining data relationships and structure. It handles
various types of geotechnical data including project information, locations,
samples, lab tests, and in-situ measurements.

The mapping process:
1. Project Data: Converts AGS 3 &#x27;PROJ&#x27; group to Bedrock&#x27;s &#x27;Project&#x27; table
2. Location Data: Converts AGS 3 &#x27;HOLE&#x27; group to Bedrock&#x27;s &#x27;Location&#x27; table
3. Sample Data: Converts AGS 3 &#x27;SAMP&#x27; group to Bedrock&#x27;s &#x27;Sample&#x27; table
4. Other Data: Handles lab tests, in-situ measurements, and miscellaneous tables

**Arguments**:

- `ags3_db` _Dict[str, pd.DataFrame]_ - A dictionary containing AGS 3 data tables,
  where keys are table names and values are pandas DataFrames.
- `crs` _CRS_ - Coordinate Reference System for the project data.
  

**Returns**:

  Dict[str, pd.DataFrame]: A dictionary containing Bedrock GI database tables,
  where keys are table names and values are transformed pandas DataFrames.
  

**Notes**:

  The function creates a copy of the input database to avoid modifying the original data.
  It performs foreign key checks to maintain data integrity during the mapping.

#### ags\_proj\_to\_brgi\_project

```python
@pa.check_types(lazy=True)
def ags_proj_to_brgi_project(ags_proj: pd.DataFrame,
                             crs: CRS) -> DataFrame[Project]
```

Maps the AGS 3 &#x27;PROJ&#x27; group to a Bedrock GI &#x27;Project&#x27; table.

**Arguments**:

- `ags_proj` _pd.DataFrame_ - The AGS 3 &#x27;PROJ&#x27; group.
- `crs` _CRS_ - The coordinate reference system of the project.
  

**Returns**:

- `DataFrame[Project]` - The Bedrock GI &#x27;Project&#x27; table.

#### ags3\_hole\_to\_brgi\_location

```python
@pa.check_types(lazy=True)
def ags3_hole_to_brgi_location(ags3_hole: DataFrame[Ags3HOLE],
                               project_uid: str) -> DataFrame[BaseLocation]
```

#### ags3\_samp\_to\_brgi\_sample

```python
@pa.check_types(lazy=True)
def ags3_samp_to_brgi_sample(ags3_samp: DataFrame[Ags3SAMP],
                             project_uid: str) -> DataFrame[BaseSample]
```

#### ags3\_in\_situ\_to\_brgi\_in\_situ

```python
@pa.check_types(lazy=True)
def ags3_in_situ_to_brgi_in_situ(group_name: str, ags3_in_situ: pd.DataFrame,
                                 project_uid: str) -> DataFrame[BaseInSitu]
```

Maps AGS 3 in-situ measurement data to Bedrock&#x27;s in-situ data schema.

**Arguments**:

- `group_name` _str_ - The AGS 3 group name.
- `ags3_data` _pd.DataFrame_ - The AGS 3 data.
- `project_uid` _str_ - The project uid.
  

**Returns**:

- `DataFrame[BaseInSitu]` - The Bedrock in-situ data.

#### generate\_sample\_ids\_for\_ags3

```python
@pa.check_types(lazy=True)
def generate_sample_ids_for_ags3(
        ags3_with_samp: DataFrame[BaseSAMP]) -> DataFrame[Ags3SAMP]
```

