---
sidebar_label: validate
title: bedrock_ge.gi.ags.validate
prev: false
next: false
---

#### check\_ags\_proj\_group

```python
def check_ags_proj_group(ags_proj: pd.DataFrame) -> bool
```

Checks if the AGS 3 or AGS 4 PROJ group is correct.

**Arguments**:

- `ags_proj` _pd.DataFrame_ - The DataFrame with the PROJ group.
  

**Raises**:

- `ValueError` - If AGS 3 of AGS 4 PROJ group is not correct.
  

**Returns**:

- `bool` - Returns True if the AGS 3 or AGS 4 PROJ group is correct.

