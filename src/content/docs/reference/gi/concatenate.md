---
sidebar_label: concatenate
title: bedrock_ge.gi.concatenate
prev: false
next: false
---

#### concatenate\_databases

```python
def concatenate_databases(
    db1: Dict[str, Union[pd.DataFrame, gpd.GeoDataFrame]],
    db2: Dict[str, Union[pd.DataFrame, gpd.GeoDataFrame]]
) -> Dict[str, pd.DataFrame]
```

Concatenates two dictionaries of DataFrames into one dict of DataFrames.

The function concatenates the pandas DataFrames of the second dict of
DataFrames to the first dict of DataFrames for the keys they have in common.
Keys that are unique to either dictionary will be included in the final
concatenated dictionary.

**Arguments**:

- `db1` _Dict[str, pd.DataFrame]_ - A dictionary of pandas DataFrames, i.e. a database.
- `db2` _Dict[str, pd.DataFrame]_ - A dictionary of pandas DataFrames, i.e. a database.
  

**Returns**:

- `concatenated_dict` _Dict[str, pd.DataFrame]_ - A dictionary of concatenated pandas DataFrames.

