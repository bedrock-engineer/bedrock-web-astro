---
sidebar_label: read
title: bedrock_ge.gi.ags.read
prev: false
next: false
---

## check\_ags\_proj\_group

#### ags\_to\_dfs

```python
def ags_to_dfs(ags_data: str) -> Dict[str, pd.DataFrame]
```

Converts AGS 3 or AGS 4 data to a dictionary of pandas DataFrames.

**Arguments**:

- `ags_data` _str_ - The AGS data as a string.
  

**Raises**:

- `ValueError` - If the data does not match AGS 3 or AGS 4 format.
  

**Returns**:

  Dict[str, pd.DataFrame]]: A dictionary where keys represent AGS group
  names with corresponding DataFrames for the corresponding group data.

#### ags3\_to\_dfs

```python
def ags3_to_dfs(ags3_data: str) -> Dict[str, pd.DataFrame]
```

Converts AGS 3 data to a dictionary of pandas DataFrames.

**Arguments**:

- `ags3_data` _str_ - The AGS 3 data as a string.
  

**Returns**:

  Dict[str, pd.DataFrame]: A dictionary of pandas DataFrames, where each key
  represents a group name from AGS 3 data, and the corresponding value is a
  pandas DataFrame containing the data for that group.

#### ags4\_to\_dfs

```python
def ags4_to_dfs(ags4_data: str) -> Dict[str, pd.DataFrame]
```

Converts AGS 4 data to a dictionary of pandas DataFrames.

**Arguments**:

- `ags4_data` _str_ - The AGS 4 data as a string.
  

**Returns**:

  Dict[str, pd.DataFrame]: A dictionary of pandas DataFrames, where each key
  represents a group name from AGS 4 data, and the corresponding value is a
  pandas DataFrame containing the data for that group.

#### coerce\_string

```python
def coerce_string(string: str) -> Union[None, bool, float, str]
```

