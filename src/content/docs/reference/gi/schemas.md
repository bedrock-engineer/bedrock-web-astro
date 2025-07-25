---
sidebar_label: schemas
title: bedrock_ge.gi.schemas
prev: false
next: false
editUrl: false
---

pandera schemas for Bedrock GI data. Base schemas refer to schemas that have no calculated GIS geometry or values.

## GeoSeries

## Project

```python
class Project(pa.DataFrameModel)
```

#### project\_uid

#### crs\_wkt

## BaseLocation

```python
class BaseLocation(pa.DataFrameModel)
```

#### location\_uid

#### project\_uid

#### location\_source\_id

#### location\_type

#### easting

#### northing

#### ground\_level\_elevation

#### depth\_to\_base

## Location

```python
class Location(BaseLocation)
```

#### elevation\_at\_base

#### longitude

#### latitude

#### wgs84\_ground\_level\_height

#### geometry

## BaseInSitu

```python
class BaseInSitu(pa.DataFrameModel)
```

#### project\_uid

#### location\_uid

#### depth\_to\_top

#### depth\_to\_base

## BaseSample

```python
class BaseSample(BaseInSitu)
```

#### sample\_uid

#### sample\_source\_id

## Sample

```python
class Sample(BaseSample)
```

#### elevation\_at\_top

#### elevation\_at\_base

#### geometry

## InSitu

```python
class InSitu(BaseInSitu)
```

#### elevation\_at\_top

#### elevation\_at\_base

#### geometry

## BaseLab

```python
class BaseLab(pa.DataFrameModel)
```

#### project\_uid

#### location\_uid

#### sample\_uid

## Lab

```python
class Lab(BaseLab)
```

#### geometry

