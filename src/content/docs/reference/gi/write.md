---
sidebar_label: write
title: bedrock_ge.gi.write
prev: false
next: false
---

#### write\_gi\_db\_to\_gpkg

```python
def write_gi_db_to_gpkg(brgi_db: Dict[str, gpd.GeoDataFrame],
                        gpkg_path: Union[str, Path]) -> None
```

Writes a database with Bedrock Ground Investigation data to a GeoPackage file.

Writes a dictionary of DataFrames containing Bedrock Ground Investigation data to a
[GeoPackage file](https://www.geopackage.org/). Each DataFrame will be saved in a
separate table named by the keys of the dictionary.

**Arguments**:

- `brgi_db` _Dict[str, Union[pd.DataFrame, gpd.GeoDataFrame]]_ - A dictionary where
  keys are brgi table names and values are pandas DataFrames or GeoDataFrames
  with brgi data.
- `gpkg_path` _str_ - The name of the output GeoPackage file.
  

**Returns**:

  None

#### write\_gi\_db\_to\_excel

```python
def write_gi_db_to_excel(gi_dfs: Dict[str, Union[pd.DataFrame,
                                                 gpd.GeoDataFrame]],
                         excel_path: Union[str, Path]) -> None
```

Writes a database with Ground Investigation data to an Excel file.

Each DataFrame in the database dictionary will be saved in a separate Excel sheet named
after the dictionary keys. This function can be used on any GI database, whether in
AGS, Bedrock, or another format.

**Arguments**:

- `gi_dfs` _Dict[str, Union[pd.DataFrame, gpd.GeoDataFrame]]_ - A dictionary where
  keys are GI table names and values are DataFrames with GI data.
- `excel_path` _Union[str, Path]_ - Path to the output Excel file. Can be provided as a
  string or Path object.
  

**Returns**:

  None

#### sanitize\_table\_name

```python
def sanitize_table_name(sheet_name)
```

Replaces invalid characters and spaces in GI table names with underscores and truncates to 31 characters.

Makes table names consistent with SQL, GeoPackage and Excel naming conventions by
replacing invalid characters and spaces with underscores.

**Arguments**:

- `sheet_name` _str_ - The original sheet name.
  

**Returns**:

- `sanitized_name` _str_ - A sanitized sheet name with invalid characters and spaces replaced.

