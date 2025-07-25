---
sidebar_label: sqlmodels
title: bedrock_ge.gi.sqlmodels
prev: false
next: false
---

## Project

```python
class Project(SQLModel)
```

#### project\_uid

#### crs

## Location

```python
class Location(SQLModel)
```

#### location\_uid

#### project\_uid

#### source\_id

#### location\_type

#### easting

#### northing

#### ground\_level

#### depth\_to\_base

#### elevation\_at\_base

#### latitude

#### longitude

## DepthInformation

```python
class DepthInformation(SQLModel)
```

#### depth\_to\_top

#### depth\_to\_base

#### elevation\_at\_top

#### elevation\_at\_base

## Sample

```python
class Sample(DepthInformation)
```

#### sample\_uid

#### project\_uid

#### location\_uid

#### source\_id

## InSitu

```python
class InSitu(DepthInformation)
```

#### project\_uid

#### location\_uid

## Lab

```python
class Lab(SQLModel)
```

#### project\_uid

#### location\_uid

#### sample\_uid

## Material

```python
class Material(InSitu)
```

Material descriptions from the field. GEOL group in AGS 3 and AGS 4.

#### id

#### material\_name

#### material\_description

## SPT

```python
class SPT(InSitu)
```

#### id

#### spt\_count

## RockCore

```python
class RockCore(InSitu)
```

#### id

#### tcr

#### scr

#### rqd

## Weathering

```python
class Weathering(InSitu)
```

#### id

#### weathering

