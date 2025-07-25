---
sidebar_label: schemas
title: bedrock_ge.gi.ags.schemas
prev: false
next: false
---

## Ags3HOLE

```python
class Ags3HOLE(pa.DataFrameModel)
```

#### HOLE\_ID

#### HOLE\_TYPE

#### HOLE\_NATE

#### HOLE\_NATN

#### HOLE\_GL

#### HOLE\_FDEP

## BaseSAMP

```python
class BaseSAMP(pa.DataFrameModel)
```

#### SAMP\_REF

#### SAMP\_TYPE

#### SAMP\_TOP

#### SAMP\_BASE

## Ags3SAMP

```python
class Ags3SAMP(BaseSAMP)
```

#### sample\_id

#### HOLE\_ID

## Ags4SAMP

```python
class Ags4SAMP(BaseSAMP)
```

#### SAMP\_ID

#### LOCA\_ID

## BaseGEOL

```python
class BaseGEOL(pa.DataFrameModel)
```

#### GEOL\_TOP

#### GEOL\_BASE

#### GEOL\_DESC

#### GEOL\_LEG

#### GEOL\_GEOL

#### GEOL\_GEO2

## Ags3GEOL

```python
class Ags3GEOL(BaseGEOL)
```

#### HOLE\_ID

## Ags4GEOL

```python
class Ags4GEOL(BaseGEOL)
```

#### LOCA\_ID

## BaseISPT

```python
class BaseISPT(pa.DataFrameModel)
```

#### ISPT\_TOP

#### ISPT\_NVAL

## Ags3ISPT

```python
class Ags3ISPT(BaseISPT)
```

#### HOLE\_ID

## Ags4ISPT

```python
class Ags4ISPT(BaseISPT)
```

#### LOCA\_ID

## BaseCORE

```python
class BaseCORE(pa.DataFrameModel)
```

#### CORE\_TOP

#### CORE\_PREC

#### CORE\_SREC

#### CORE\_RQD

## Ags3CORE

```python
class Ags3CORE(BaseCORE)
```

#### HOLE\_ID

#### CORE\_BOT

## Ags4CORE

```python
class Ags4CORE(BaseCORE)
```

#### LOCA\_ID

#### CORE\_BASE

## BaseWETH

```python
class BaseWETH(pa.DataFrameModel)
```

#### WETH\_TOP

#### WETH\_BASE

## Ags3WETH

```python
class Ags3WETH(BaseWETH)
```

#### HOLE\_ID

#### WETH\_GRAD

## Ags4WETH

```python
class Ags4WETH(BaseWETH)
```

#### LOCA\_ID

#### WETH\_WETH

