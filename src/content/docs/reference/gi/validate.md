---
sidebar_label: validate
title: bedrock_ge.gi.validate
prev: false
next: false
---

## BaseInSitu

## BaseLocation

## BaseSample

## InSitu

## Location

## Project

## Sample

#### check\_brgi\_database

```python
def check_brgi_database(brgi_db: Dict[str, Union[pd.DataFrame,
                                                 gpd.GeoDataFrame]])
```

Validates the structure and relationships of a &#x27;Bedrock Ground Investigation&#x27; (BRGI) database (which is a dictionary of DataFrames).

This function checks that all tables in the BRGI database conform to their respective schemas
and that all foreign key relationships are properly maintained. It validates the following tables:
- Project
- Location
- Sample
- InSitu_TESTX
- Lab_TESTY (not yet implemented)

**Arguments**:

- `brgi_db` _Dict[str, Union[pd.DataFrame, gpd.GeoDataFrame]]_ - A dictionary
  containing the BRGI database tables, where keys are table names and
  values are the corresponding data tables (DataFrame or GeoDataFrame).
  

**Returns**:

- `is_valid` _bool_ - True if all tables are valid and relationships are properly maintained.
  

**Example**:

    ```python
    brgi_db = {
        "Project": project_df,
        "Location": location_gdf,
        "Sample": sample_gdf,
        "InSitu_ISPT": in_situ_ispt_gdf,
    }
    check_brgi_database(brgi_db)
    ```

#### check\_no\_gis\_brgi\_database

```python
def check_no_gis_brgi_database(brgi_db: Dict[str, Union[pd.DataFrame,
                                                        gpd.GeoDataFrame]])
```

Validates the structure and relationships of a &#x27;Bedrock Ground Investigation&#x27; (BGI) database without GIS geometry.

This function performs the same validation as `check_brgi_database` but uses schemas
that don&#x27;t require GIS geometry. It validates the following tables:
- Project (never has GIS geometry)
- Location (without GIS geometry)
- Sample (without GIS geometry)
- InSitu_TESTX (without GIS geometry)
- Lab_TESTY (not yet implemented)

**Arguments**:

- `brgi_db` _Dict[str, Union[pd.DataFrame, gpd.GeoDataFrame]]_ - A dictionary
  containing the Bedrock GI database tables, where keys are table names
  and values are the corresponding data tables (DataFrame or GeoDataFrame).
  

**Returns**:

- `bool` - True if all tables are valid and relationships are properly maintained.
  

**Example**:

    ```python
    brgi_db = {
        "Project": projects_df,
        "Location": locations_df,
        "Sample": samples_df,
        "InSitu_measurements": insitu_df,
    }
    check_no_gis_brgi_database(brgi_db)
    ```

#### check\_foreign\_key

```python
def check_foreign_key(
        foreign_key: str, parent_table: Union[pd.DataFrame, gpd.GeoDataFrame],
        table_with_foreign_key: Union[pd.DataFrame, gpd.GeoDataFrame]) -> bool
```

Validates referential integrity between two tables by checking foreign key relationships.

This function ensures that all foreign key values in a child table exist in the corresponding
parent table, maintaining data integrity in the GIS database.

**Arguments**:

- `foreign_key` _str_ - The name of the column that serves as the foreign key.
- `parent_table` _Union[pd.DataFrame, gpd.GeoDataFrame]_ - The parent table containing the primary keys.
- `table_with_foreign_key` _Union[pd.DataFrame, gpd.GeoDataFrame]_ - The child table containing the foreign keys.
  

**Returns**:

- `bool` - True if all foreign keys exist in the parent table.
  

**Raises**:

- `ValueError` - If any foreign key values in the child table do not exist in the parent table.
  

**Example**:

    ```python
    check_foreign_key("project_uid", projects_df, locations_df)
    ```

