---
redirect_from:
  - "/04/dataframes"
interact_link: content/04/DataFrames.ipynb
kernel_name: python3
has_widgets: false
title: 'DataFrames'
prev_page:
  url: /03/6/Functions.html
  title: 'Functions'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# DataFrames

The `DataFrame` is a type of data structure in Python which is widely-used in Data Science, and provided by the <a href="https://pandas.pydata.org/" rel="noopener" target="_blank">`pandas`</a> data analysis and manipulation library.

`DataFrames` are *collections* like `lists`. But, while `lists` *allow* you to collect elements which are themselves `lists`, `DataFrames` are built expressly for the purpose of manipulating such data easily and efficiently. This structure is "tabular" – like a spreadsheet – and also considered "two-dimensional." Its dimensions are commonly:

**a sequence of *columns***:
: each column represents the values of a single *feature* of our data set

**a sequence of *rows***:
: each row represents the values of all of the features of a single *individual* element of our data



## Construction

We began to consider this sort of data in [Sequences](/03/3/3/Sequences.html#other-lists), with the distances of planets from our sun. Let's expand on this example with the below data, adding the planets' masses, densities and gravities.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets_features = [
    'name',                # familiar name
    'solar_distance_km_6', # distance from sun: 10**6 km
    'mass_kg_24',          # absolute mass: 10**24 kg
    'density_kg_m3',       # density: kg/m**3
    'gravity_m_s2',        # gravity: m/s**2
]

planets_data = [
    ['Mercury', 57.9, 0.33, 5427.0, 3.7],
    ['Venus', 108.2, 4.87, 5243.0, 8.9],
    ['Earth', 149.6, 5.97, 5514.0, 9.8],
    ['Mars', 227.9, 0.642, 3933.0, 3.7],
    ['Jupiter', 778.6, 1898.0, 1326.0, 23.1],
    ['Saturn', 1433.5, 568.0, 687.0, 9.0],
    ['Uranus', 2872.5, 86.8, 1271.0, 8.7],
    ['Neptune', 4495.1, 102.0, 1638.0, 11.0]
]

planets_data

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[['Mercury', 57.9, 0.33, 5427.0, 3.7],
 ['Venus', 108.2, 4.87, 5243.0, 8.9],
 ['Earth', 149.6, 5.97, 5514.0, 9.8],
 ['Mars', 227.9, 0.642, 3933.0, 3.7],
 ['Jupiter', 778.6, 1898.0, 1326.0, 23.1],
 ['Saturn', 1433.5, 568.0, 687.0, 9.0],
 ['Uranus', 2872.5, 86.8, 1271.0, 8.7],
 ['Neptune', 4495.1, 102.0, 1638.0, 11.0]]
```


</div>
</div>
</div>



Now let's construct a `DataFrame` for these data.

First, we'll have to ensure that the <a href="https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html" target="_blank" rel="noopener">pandas library is installed</a>.

Then, we can tell Python to make `pandas` available to us using an `import` statement. For example:

    import pandas

Having done so, the `DataFrame` type would be available as: `pandas.DataFrame`.

That is, unlike with the built-in `list`, we would refer to it as "under" the name `pandas`, with a dot between the two names.

Or, we could import just `DataFrame`, such that it's available as just `DataFrame`, without the rigmarole:

    from pandas import DataFrame

However, we'll be using `pandas` a lot! And not *just* `DataFrame`. Following a common convention, we'll tell Python to assign the library module the name `pd`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import pandas as pd

planets = pd.DataFrame(planets_data)

planets

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Mercury</td>
      <td>57.9</td>
      <td>0.330</td>
      <td>5427.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>4.870</td>
      <td>5243.0</td>
      <td>8.9</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.970</td>
      <td>5514.0</td>
      <td>9.8</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Mars</td>
      <td>227.9</td>
      <td>0.642</td>
      <td>3933.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Jupiter</td>
      <td>778.6</td>
      <td>1898.000</td>
      <td>1326.0</td>
      <td>23.1</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>568.000</td>
      <td>687.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>86.800</td>
      <td>1271.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>102.000</td>
      <td>1638.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



Above, we've:

* imported the `pandas` library under the name `pd`
* constructed a new `DataFrame` from our list-of-list data
* assigned to the `DataFrame` the name `planets`

And this presentation of our data is already looking more like a spreadsheet.

However, there's something odd about the above. We're accustomed now to numbering elements of a sequence by their *offset* – 0, 1, 2, 3, … – and this works in this case for numbering our rows. But this isn't a useful scheme for labeling our columns. We'll make manipulation of this data easier, and avoid confusion about what these values represent, by defining useful column labels.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets = pd.DataFrame(planets_data, columns=planets_features)

planets

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Mercury</td>
      <td>57.9</td>
      <td>0.330</td>
      <td>5427.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>4.870</td>
      <td>5243.0</td>
      <td>8.9</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.970</td>
      <td>5514.0</td>
      <td>9.8</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Mars</td>
      <td>227.9</td>
      <td>0.642</td>
      <td>3933.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Jupiter</td>
      <td>778.6</td>
      <td>1898.000</td>
      <td>1326.0</td>
      <td>23.1</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>568.000</td>
      <td>687.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>86.800</td>
      <td>1271.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>102.000</td>
      <td>1638.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



That's better!

As we've seen with the `list`, (and the string), the `DataFrame` can be manipulated by functions and built-in operators. Moreover, these offer special-purpose functions which have been *bound* to their types – that is, *methods* – which are invoked with expressions of the form below:

    name_of_dataframe.name_of_method(argument0, argument1, ..., keyword0=value0, ...)

And, similar to methods, there are *attributes* and *properties*. These are values which are similarly bound to the `DataFrame`, but which need not be called:

    name_of_dataframe.name_of_property

Now we're ready to explore the dimensions our data.



## Features

We assigned the following column names:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.columns

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
Index(['name', 'solar_distance_km_6', 'mass_kg_24', 'density_kg_m3',
       'gravity_m_s2'],
      dtype='object')
```


</div>
</div>
</div>



`pandas` has constructed an `Index` for our columns. But we can get back our column list with the method `tolist()`:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.columns.tolist()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['name', 'solar_distance_km_6', 'mass_kg_24', 'density_kg_m3', 'gravity_m_s2']
```


</div>
</div>
</div>



So let's take a look at the first dimension of our data, the *features*, such as `name`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.name

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0    Mercury
1      Venus
2      Earth
3       Mars
4    Jupiter
5     Saturn
6     Uranus
7    Neptune
Name: name, dtype: object
```


</div>
</div>
</div>



Above, we've extracted from our data a one-dimensional sequence of the names of the planets in our solar system – (even though there was no such list in our initial input data `planets_data`).

This sequence is of another data type provided by `pandas`: the `Series`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
type(planets.name)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
pandas.core.series.Series
```


</div>
</div>
</div>



We can do the same for the next column, representing the distances of these planets from the sun, in 10<sup>6</sup> km.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.solar_distance_km_6

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0      57.9
1     108.2
2     149.6
3     227.9
4     778.6
5    1433.5
6    2872.5
7    4495.1
Name: solar_distance_km_6, dtype: float64
```


</div>
</div>
</div>



And we can compute aggregates of this data, such as the average or *mean*.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.solar_distance_km_6.mean()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
1265.4125000000001
```


</div>
</div>
</div>



## Individuals

The second dimension of our data consists of its rows or *individuals*.

As with the columns, `pandas` has constructed an index for our rows. By default, this is the familiar `0, 1, 2, …`, and represented by the `RangeIndex` type.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.index

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
RangeIndex(start=0, stop=8, step=1)
```


</div>
</div>
</div>



And, as with the `list`, we can use the built-in function `len` to see that there are eight planets.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(planets)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
8
```


</div>
</div>
</div>



We can also *slice* the `DataFrame`, for example to extract only its first three rows.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets[:3]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Mercury</td>
      <td>57.9</td>
      <td>0.33</td>
      <td>5427.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>4.87</td>
      <td>5243.0</td>
      <td>8.9</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.97</td>
      <td>5514.0</td>
      <td>9.8</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



Above, our slice has constructed a new `DataFrame`, consisting of only the data for the first three planets.

**However**: you *can't* access *individual* rows or elements in the same manner as with a `list`:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets[2]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    /opt/conda/lib/python3.7/site-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
       2896             try:
    -> 2897                 return self._engine.get_loc(key)
       2898             except KeyError:


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()


    KeyError: 2

    
    During handling of the above exception, another exception occurred:


    KeyError                                  Traceback (most recent call last)

    <ipython-input-13-e3d749a015ed> in <module>
    ----> 1 planets[2]
    

    /opt/conda/lib/python3.7/site-packages/pandas/core/frame.py in __getitem__(self, key)
       2978             if self.columns.nlevels > 1:
       2979                 return self._getitem_multilevel(key)
    -> 2980             indexer = self.columns.get_loc(key)
       2981             if is_integer(indexer):
       2982                 indexer = [indexer]


    /opt/conda/lib/python3.7/site-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
       2897                 return self._engine.get_loc(key)
       2898             except KeyError:
    -> 2899                 return self._engine.get_loc(self._maybe_cast_indexer(key))
       2900         indexer = self.get_indexer([key], method=method, tolerance=tolerance)
       2901         if indexer.ndim > 1 or indexer.size > 1:


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()


    KeyError: 2


```
</div>
</div>
</div>



After all, the `DataFrame` is a more complex structure than the `list` – the above reference to the offset `2` was treated as a reference to a column!

Indeed, this is an alternate syntax *for extracting columns*, and which is useful and necessary when columns are given complex names. (Complex names are any including characters which are part of Python's syntax, and therefore invalid names of assignment, such as spaces, quotes, brackets, *etc.*)



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets['name']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0    Mercury
1      Venus
2      Earth
3       Mars
4    Jupiter
5     Saturn
6     Uranus
7    Neptune
Name: name, dtype: object
```


</div>
</div>
</div>



Instead, `DataFrame` offers the properties `iloc` and `loc`, which may themselves be queried with a syntax similar to that of retrieving elements from a `list`.

`iloc` is intended for *integer-location* based look-up of elements by their position in the index.

We can reproduce our slice explicitly using `iloc`:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.iloc[:3]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Mercury</td>
      <td>57.9</td>
      <td>0.33</td>
      <td>5427.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>4.87</td>
      <td>5243.0</td>
      <td>8.9</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.97</td>
      <td>5514.0</td>
      <td>9.8</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



We can also do something new – construct a new `DataFrame` consisting of only the rows at the specified offsets.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.iloc[[0, 7]]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Mercury</td>
      <td>57.9</td>
      <td>0.33</td>
      <td>5427.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>102.00</td>
      <td>1638.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



Above, we've specified to our `iloc`-based look-up a `list` – `[0, 7]` – indicating that we are interested in selecting out the rows at those offsets.

Note that in the new `DataFrame`, the planets' row index values have been preserved. This is highly useful – indeed, Neptune is still the same planet as it was before. But `iloc` is **strictly** intended for offsets, like in a `list`. If we were to repeat our selection of `[0, 7]` on the above, this would fail. Rather, the offset references for these two planets in the new `DataFrame` are now given by `[0, 1]`. According to `iloc` in this new `DataFrame`, Neptune will now be available at offset `1`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
bookends = planets.iloc[[0, 7]]

bookends.iloc[1]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
name                   Neptune
solar_distance_km_6     4495.1
mass_kg_24                 102
density_kg_m3             1638
gravity_m_s2                11
Name: 7, dtype: object
```


</div>
</div>
</div>



In the next section, we will explore selection of elements by index value or label.

But now we can retrieve the features of another individual of our data set – Earth, the third planet from the sun.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
earth = planets.iloc[2]

earth

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
name                   Earth
solar_distance_km_6    149.6
mass_kg_24              5.97
density_kg_m3           5514
gravity_m_s2             9.8
Name: 2, dtype: object
```


</div>
</div>
</div>



We can further extract from this just the Earth's distance from the Sun.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
earth.solar_distance_km_6

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
149.6
```


</div>
</div>
</div>



And we can get an idea from the above of how spread out the planets are.

The Earth is the third of eight planets, yet its distance from the sun is less than 12% their average.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
earth.solar_distance_km_6 / planets.solar_distance_km_6.mean()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.11822231880908397
```


</div>
</div>
</div>



Generally, we might note that the median distance of planets from the sun is less than half their mean.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.solar_distance_km_6.median() / planets.solar_distance_km_6.mean()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.39769640334673473
```


</div>
</div>
</div>



`pandas` supports a number of statistical methods, such as standard deviation `std`, mean absolute deviation `mad`, and more.

We know that the planets are spread out. Let's take a look at simply how their distances increase.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.solar_distance_km_6.diff()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0       NaN
1      50.3
2      41.4
3      78.3
4     550.7
5     654.9
6    1439.0
7    1622.6
Name: solar_distance_km_6, dtype: float64
```


</div>
</div>
</div>



The above `Series` tells us that Venus is 50.3 million kilometers farther from the sun than Mercury, Earth is 41.4 million kilometers farther than Venus, *etc.* (The first value, for Mercury, is `NaN` – "not a number" – because there is no planet closer than it to the sun, with which to compare its distance.)

And, indeed, the distances between the planets increase dramatically.

We can see roughly that the first big jump is in the distance between Mars and Jupiter. The distances between the outer planets then continue to be greater than those between the inner planets, and continue to increase. But there's another big intermediate jump, between Saturn and Uranus.

We can express the above quantitatively as well:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
distance_rel_change = planets.solar_distance_km_6.pct_change()

distance_rel_change

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0         NaN
1    0.868739
2    0.382625
3    0.523396
4    2.416411
5    0.841125
6    1.003837
7    0.564874
Name: solar_distance_km_6, dtype: float64
```


</div>
</div>
</div>



In preceding examples, we've used the built-in operator for division against two numeric arguments of type `float`. The result of each of these operations was appropriately also a `float`.

We can also apply this operator to divide each of an entire `Series` of `float` values by a single `float`, and in so doing produce a new `Series`.

Many built-in operators are supported. For clarity, let's map our percent-change values to conventional percentages, using the operator for multiplication.

The `pct_change` method returns these values as ratios, comparing the distance of each planet from the sun, $distance_1$, to the distance of the planet preceding it, $distance_0$, according to:

\begin{align\*}
\frac{distance_1 - distance_0}{distance_0}
\end{align\*}

We can represent these as conventional percentages by simply multiplying them by `100`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
distance_pct_change = distance_rel_change * 100

distance_pct_change

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0           NaN
1     86.873921
2     38.262477
3     52.339572
4    241.641071
5     84.112510
6    100.383676
7     56.487380
Name: solar_distance_km_6, dtype: float64
```


</div>
</div>
</div>



And while we all have in mind the order of the planets, it would be more meaningful to see the above values in context, along with our other planetary data.

We can use the `assign` method to construct a new `DataFrame`, one which begins with the data from `planets`, and which adds to this our new column.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.assign(distance_pct_change=distance_pct_change)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
      <th>distance_pct_change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Mercury</td>
      <td>57.9</td>
      <td>0.330</td>
      <td>5427.0</td>
      <td>3.7</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>4.870</td>
      <td>5243.0</td>
      <td>8.9</td>
      <td>86.873921</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.970</td>
      <td>5514.0</td>
      <td>9.8</td>
      <td>38.262477</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Mars</td>
      <td>227.9</td>
      <td>0.642</td>
      <td>3933.0</td>
      <td>3.7</td>
      <td>52.339572</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Jupiter</td>
      <td>778.6</td>
      <td>1898.000</td>
      <td>1326.0</td>
      <td>23.1</td>
      <td>241.641071</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>568.000</td>
      <td>687.0</td>
      <td>9.0</td>
      <td>84.112510</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>86.800</td>
      <td>1271.0</td>
      <td>8.7</td>
      <td>100.383676</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>102.000</td>
      <td>1638.0</td>
      <td>11.0</td>
      <td>56.487380</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



As you can see, the `assign` method accepts *only* named keyword arguments. Notably, these can be *any* syntactically-valid name – `pandas` adds the sequence of values you specify to the existing data as a new column, and *assigns* to the new column this name.

Arguably, of course, our multiplication by 100 was only an aesthetic change. We might instead preserve the output of our `pct_change` calculation, and merely adjust the presentation of our `DataFrame`.

`pandas` offers the `DataFrame` property `style`, whose `format` method accepts either functions or strings, with which it determines how to present its data. String arguments to this `format` method follow Python's standard form for indicating how a value should be presented as text.

Python's strings offer their own `format` method. And, for example, we might construct a string presenting the `float` value `0.868739` as a conventional percentage, as follows.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
'{:.2%}'.format(0.868739)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'86.87%'
```


</div>
</div>
</div>



In a similar manner we can apply this formatting to our column, without altering the underlying values.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets_rel_change = planets.assign(distance_rel_change=distance_rel_change)

planets_rel_change

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
      <th>distance_rel_change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Mercury</td>
      <td>57.9</td>
      <td>0.330</td>
      <td>5427.0</td>
      <td>3.7</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>4.870</td>
      <td>5243.0</td>
      <td>8.9</td>
      <td>0.868739</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.970</td>
      <td>5514.0</td>
      <td>9.8</td>
      <td>0.382625</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Mars</td>
      <td>227.9</td>
      <td>0.642</td>
      <td>3933.0</td>
      <td>3.7</td>
      <td>0.523396</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Jupiter</td>
      <td>778.6</td>
      <td>1898.000</td>
      <td>1326.0</td>
      <td>23.1</td>
      <td>2.416411</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>568.000</td>
      <td>687.0</td>
      <td>9.0</td>
      <td>0.841125</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>86.800</td>
      <td>1271.0</td>
      <td>8.7</td>
      <td>1.003837</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>102.000</td>
      <td>1638.0</td>
      <td>11.0</td>
      <td>0.564874</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets_rel_change.style.format({
    'distance_rel_change': '{:.2%}',
})

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<style  type="text/css" >
</style><table id="T_e75a3ae8_59a5_11ea_8552_0242ac130003" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >name</th>        <th class="col_heading level0 col1" >solar_distance_km_6</th>        <th class="col_heading level0 col2" >mass_kg_24</th>        <th class="col_heading level0 col3" >density_kg_m3</th>        <th class="col_heading level0 col4" >gravity_m_s2</th>        <th class="col_heading level0 col5" >distance_rel_change</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_e75a3ae8_59a5_11ea_8552_0242ac130003level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row0_col0" class="data row0 col0" >Mercury</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row0_col1" class="data row0 col1" >57.9</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row0_col2" class="data row0 col2" >0.33</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row0_col3" class="data row0 col3" >5427</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row0_col4" class="data row0 col4" >3.7</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row0_col5" class="data row0 col5" >nan%</td>
            </tr>
            <tr>
                        <th id="T_e75a3ae8_59a5_11ea_8552_0242ac130003level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row1_col0" class="data row1 col0" >Venus</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row1_col1" class="data row1 col1" >108.2</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row1_col2" class="data row1 col2" >4.87</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row1_col3" class="data row1 col3" >5243</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row1_col4" class="data row1 col4" >8.9</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row1_col5" class="data row1 col5" >86.87%</td>
            </tr>
            <tr>
                        <th id="T_e75a3ae8_59a5_11ea_8552_0242ac130003level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row2_col0" class="data row2 col0" >Earth</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row2_col1" class="data row2 col1" >149.6</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row2_col2" class="data row2 col2" >5.97</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row2_col3" class="data row2 col3" >5514</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row2_col4" class="data row2 col4" >9.8</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row2_col5" class="data row2 col5" >38.26%</td>
            </tr>
            <tr>
                        <th id="T_e75a3ae8_59a5_11ea_8552_0242ac130003level0_row3" class="row_heading level0 row3" >3</th>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row3_col0" class="data row3 col0" >Mars</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row3_col1" class="data row3 col1" >227.9</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row3_col2" class="data row3 col2" >0.642</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row3_col3" class="data row3 col3" >3933</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row3_col4" class="data row3 col4" >3.7</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row3_col5" class="data row3 col5" >52.34%</td>
            </tr>
            <tr>
                        <th id="T_e75a3ae8_59a5_11ea_8552_0242ac130003level0_row4" class="row_heading level0 row4" >4</th>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row4_col0" class="data row4 col0" >Jupiter</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row4_col1" class="data row4 col1" >778.6</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row4_col2" class="data row4 col2" >1898</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row4_col3" class="data row4 col3" >1326</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row4_col4" class="data row4 col4" >23.1</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row4_col5" class="data row4 col5" >241.64%</td>
            </tr>
            <tr>
                        <th id="T_e75a3ae8_59a5_11ea_8552_0242ac130003level0_row5" class="row_heading level0 row5" >5</th>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row5_col0" class="data row5 col0" >Saturn</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row5_col1" class="data row5 col1" >1433.5</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row5_col2" class="data row5 col2" >568</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row5_col3" class="data row5 col3" >687</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row5_col4" class="data row5 col4" >9</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row5_col5" class="data row5 col5" >84.11%</td>
            </tr>
            <tr>
                        <th id="T_e75a3ae8_59a5_11ea_8552_0242ac130003level0_row6" class="row_heading level0 row6" >6</th>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row6_col0" class="data row6 col0" >Uranus</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row6_col1" class="data row6 col1" >2872.5</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row6_col2" class="data row6 col2" >86.8</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row6_col3" class="data row6 col3" >1271</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row6_col4" class="data row6 col4" >8.7</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row6_col5" class="data row6 col5" >100.38%</td>
            </tr>
            <tr>
                        <th id="T_e75a3ae8_59a5_11ea_8552_0242ac130003level0_row7" class="row_heading level0 row7" >7</th>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row7_col0" class="data row7 col0" >Neptune</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row7_col1" class="data row7 col1" >4495.1</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row7_col2" class="data row7 col2" >102</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row7_col3" class="data row7 col3" >1638</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row7_col4" class="data row7 col4" >11</td>
                        <td id="T_e75a3ae8_59a5_11ea_8552_0242ac130003row7_col5" class="data row7 col5" >56.49%</td>
            </tr>
    </tbody></table>
</div>


</div>
</div>
</div>



Note, in the above, we made use of another collection built into Python: the `dict`, or "dictionary." The syntax of `dict` construction is simply:

    {KEY0: VALUE0, …}

Dictionaries are widely useful; but, here, you'll only see them as another means of associating keyword arguments with their values, analogous to how `assign` is called.

We can also rename columns, in this case also for clarity, and again making use of a `dict`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets_rel_change = planets_rel_change.rename(
    columns={
        'distance_rel_change': 'distance relative change',
    }
)

planets_rel_change.style.format({
    'distance relative change': '{:.2%}',
})

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<style  type="text/css" >
</style><table id="T_e75f984e_59a5_11ea_8552_0242ac130003" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >name</th>        <th class="col_heading level0 col1" >solar_distance_km_6</th>        <th class="col_heading level0 col2" >mass_kg_24</th>        <th class="col_heading level0 col3" >density_kg_m3</th>        <th class="col_heading level0 col4" >gravity_m_s2</th>        <th class="col_heading level0 col5" >distance relative change</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_e75f984e_59a5_11ea_8552_0242ac130003level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row0_col0" class="data row0 col0" >Mercury</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row0_col1" class="data row0 col1" >57.9</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row0_col2" class="data row0 col2" >0.33</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row0_col3" class="data row0 col3" >5427</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row0_col4" class="data row0 col4" >3.7</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row0_col5" class="data row0 col5" >nan%</td>
            </tr>
            <tr>
                        <th id="T_e75f984e_59a5_11ea_8552_0242ac130003level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row1_col0" class="data row1 col0" >Venus</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row1_col1" class="data row1 col1" >108.2</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row1_col2" class="data row1 col2" >4.87</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row1_col3" class="data row1 col3" >5243</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row1_col4" class="data row1 col4" >8.9</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row1_col5" class="data row1 col5" >86.87%</td>
            </tr>
            <tr>
                        <th id="T_e75f984e_59a5_11ea_8552_0242ac130003level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row2_col0" class="data row2 col0" >Earth</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row2_col1" class="data row2 col1" >149.6</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row2_col2" class="data row2 col2" >5.97</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row2_col3" class="data row2 col3" >5514</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row2_col4" class="data row2 col4" >9.8</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row2_col5" class="data row2 col5" >38.26%</td>
            </tr>
            <tr>
                        <th id="T_e75f984e_59a5_11ea_8552_0242ac130003level0_row3" class="row_heading level0 row3" >3</th>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row3_col0" class="data row3 col0" >Mars</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row3_col1" class="data row3 col1" >227.9</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row3_col2" class="data row3 col2" >0.642</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row3_col3" class="data row3 col3" >3933</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row3_col4" class="data row3 col4" >3.7</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row3_col5" class="data row3 col5" >52.34%</td>
            </tr>
            <tr>
                        <th id="T_e75f984e_59a5_11ea_8552_0242ac130003level0_row4" class="row_heading level0 row4" >4</th>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row4_col0" class="data row4 col0" >Jupiter</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row4_col1" class="data row4 col1" >778.6</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row4_col2" class="data row4 col2" >1898</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row4_col3" class="data row4 col3" >1326</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row4_col4" class="data row4 col4" >23.1</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row4_col5" class="data row4 col5" >241.64%</td>
            </tr>
            <tr>
                        <th id="T_e75f984e_59a5_11ea_8552_0242ac130003level0_row5" class="row_heading level0 row5" >5</th>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row5_col0" class="data row5 col0" >Saturn</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row5_col1" class="data row5 col1" >1433.5</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row5_col2" class="data row5 col2" >568</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row5_col3" class="data row5 col3" >687</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row5_col4" class="data row5 col4" >9</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row5_col5" class="data row5 col5" >84.11%</td>
            </tr>
            <tr>
                        <th id="T_e75f984e_59a5_11ea_8552_0242ac130003level0_row6" class="row_heading level0 row6" >6</th>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row6_col0" class="data row6 col0" >Uranus</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row6_col1" class="data row6 col1" >2872.5</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row6_col2" class="data row6 col2" >86.8</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row6_col3" class="data row6 col3" >1271</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row6_col4" class="data row6 col4" >8.7</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row6_col5" class="data row6 col5" >100.38%</td>
            </tr>
            <tr>
                        <th id="T_e75f984e_59a5_11ea_8552_0242ac130003level0_row7" class="row_heading level0 row7" >7</th>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row7_col0" class="data row7 col0" >Neptune</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row7_col1" class="data row7 col1" >4495.1</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row7_col2" class="data row7 col2" >102</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row7_col3" class="data row7 col3" >1638</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row7_col4" class="data row7 col4" >11</td>
                        <td id="T_e75f984e_59a5_11ea_8552_0242ac130003row7_col5" class="data row7 col5" >56.49%</td>
            </tr>
    </tbody></table>
</div>


</div>
</div>
</div>



Because we've added spaces to our column name, it's no longer valid in the syntax of Python, and so we can no longer refer to it as we have the other columns, such as `solar_distance_km_6`:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets_rel_change.solar_distance_km_6

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0      57.9
1     108.2
2     149.6
3     227.9
4     778.6
5    1433.5
6    2872.5
7    4495.1
Name: solar_distance_km_6, dtype: float64
```


</div>
</div>
</div>



But, we can still refer to it using the alternate syntax mentioned above:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets_rel_change['distance relative change']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0         NaN
1    0.868739
2    0.382625
3    0.523396
4    2.416411
5    0.841125
6    1.003837
7    0.564874
Name: distance relative change, dtype: float64
```


</div>
</div>
</div>



## Selection by label

With `iloc`, we were able to slice rows of our data, selecting out individuals, according to their numeric position in the index. We can also select rows *and* columns, selecting subsets of features, (and much more!), thanks to `loc`.

Let's begin by providing our `DataFrame` a more natural row index for the planets. Indexes may be modified after the fact or provided during construction.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets = pd.DataFrame(planets_data,
                       columns=planets_features,
                       index=pd.RangeIndex(1, 9, name='number'))

planets

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
    <tr>
      <th>number</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Mercury</td>
      <td>57.9</td>
      <td>0.330</td>
      <td>5427.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>4.870</td>
      <td>5243.0</td>
      <td>8.9</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.970</td>
      <td>5514.0</td>
      <td>9.8</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Mars</td>
      <td>227.9</td>
      <td>0.642</td>
      <td>3933.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Jupiter</td>
      <td>778.6</td>
      <td>1898.000</td>
      <td>1326.0</td>
      <td>23.1</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>568.000</td>
      <td>687.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>86.800</td>
      <td>1271.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>102.000</td>
      <td>1638.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



With `iloc`, we retrieve the third individual from this `DataFrame` by specifying the offset `2`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.iloc[2]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
name                   Earth
solar_distance_km_6    149.6
mass_kg_24              5.97
density_kg_m3           5514
gravity_m_s2             9.8
Name: 3, dtype: object
```


</div>
</div>
</div>



But with `loc`, we can retrieve this individual – Earth – by its index value or row label – now `3`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.loc[3]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
name                   Earth
solar_distance_km_6    149.6
mass_kg_24              5.97
density_kg_m3           5514
gravity_m_s2             9.8
Name: 3, dtype: object
```


</div>
</div>
</div>



While numeric indexes are often more practical, we can further distinguish these individuals' labels in the row index by using familiar strings instead.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ordinals = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth']

planet_ordinals = pd.DataFrame(planets_data,
                               columns=planets_features,
                               index=pd.Index(ordinals, name='ordinal'))

planet_ordinals

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
    <tr>
      <th>ordinal</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>first</td>
      <td>Mercury</td>
      <td>57.9</td>
      <td>0.330</td>
      <td>5427.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>second</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>4.870</td>
      <td>5243.0</td>
      <td>8.9</td>
    </tr>
    <tr>
      <td>third</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.970</td>
      <td>5514.0</td>
      <td>9.8</td>
    </tr>
    <tr>
      <td>fourth</td>
      <td>Mars</td>
      <td>227.9</td>
      <td>0.642</td>
      <td>3933.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>fifth</td>
      <td>Jupiter</td>
      <td>778.6</td>
      <td>1898.000</td>
      <td>1326.0</td>
      <td>23.1</td>
    </tr>
    <tr>
      <td>sixth</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>568.000</td>
      <td>687.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <td>seventh</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>86.800</td>
      <td>1271.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <td>eighth</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>102.000</td>
      <td>1638.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



`loc` supports the same selection features as `iloc`, such as slicing, even as it considers labels rather than offsets.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
middle_planets = planet_ordinals.loc['third':'sixth']

middle_planets

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
    <tr>
      <th>ordinal</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>third</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.970</td>
      <td>5514.0</td>
      <td>9.8</td>
    </tr>
    <tr>
      <td>fourth</td>
      <td>Mars</td>
      <td>227.9</td>
      <td>0.642</td>
      <td>3933.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>fifth</td>
      <td>Jupiter</td>
      <td>778.6</td>
      <td>1898.000</td>
      <td>1326.0</td>
      <td>23.1</td>
    </tr>
    <tr>
      <td>sixth</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>568.000</td>
      <td>687.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



**But watch out!** In the above example, `loc` interpreted our slice differently than `iloc` – *both* the elements at the slice `start` and `stop` were included in the results. This is convenient, because labels aren't necessarily incremental; we may not have in mind the label *following* the last one we want. Nonetheless, this is an inconsistency.

That said, `loc` resolves the inconsistency of the reference used in selecting out individuals from slices of the original `DataFrame`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
middle_planets.iloc[0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
name                   Earth
solar_distance_km_6    149.6
mass_kg_24              5.97
density_kg_m3           5514
gravity_m_s2             9.8
Name: third, dtype: object
```


</div>
</div>
</div>



Using `iloc` we must refer to Earth as the "zeroeth" (zero-offset or "first") in the above data subset named `middle_planets`…



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
middle_planets.loc['third']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
name                   Earth
solar_distance_km_6    149.6
mass_kg_24              5.97
density_kg_m3           5514
gravity_m_s2             9.8
Name: third, dtype: object
```


</div>
</div>
</div>



…but using `loc`, we may continue to refer to Earth as the "third" planet from the sun.



In addition to selecting out individuals by row label, `loc` also allows us to select features by column label.

Say we wanted to contextualize `distance_pct_change`, reproducing that `DataFrame`, but this time with only the most-relevant columns, `name` and `solar_distance_km_6`. Bear in mind that there are many ways about this! But the `assign` method, at least, enables us to create a new `DataFrame` from an existing one; while, our existing `DataFrame` of the planets contains the "offending" columns. To start, we want a `DataFrame` containing only those two columns.

When we've focused on singular features before, such as the `name` data, it hasn't been a `DataFrame` – it's a `Series`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.name

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
number
1    Mercury
2      Venus
3      Earth
4       Mars
5    Jupiter
6     Saturn
7     Uranus
8    Neptune
Name: name, dtype: object
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
type(planets.name)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
pandas.core.series.Series
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.name.assign(distance_pct_change=distance_pct_change)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-41-6e505a852e2e> in <module>
    ----> 1 planets.name.assign(distance_pct_change=distance_pct_change)
    

    /opt/conda/lib/python3.7/site-packages/pandas/core/generic.py in __getattr__(self, name)
       5177             if self._info_axis._can_hold_identifiers_and_holds_name(name):
       5178                 return self[name]
    -> 5179             return object.__getattribute__(self, name)
       5180 
       5181     def __setattr__(self, name, value):


    AttributeError: 'Series' object has no attribute 'assign'


```
</div>
</div>
</div>



Well, *that* didn't work….

Instead, let's use `loc` to slice our `DataFrame` along its columns – and create a `DataFrame` with only the features we want.

Unlike what we've seen so far, element retrieval from the `loc` property can accept multiple arguments.

1. The first argument indicates row(s) to select – as above, by label, rather than offset.
1. The second argument does the same, but for column(s).

Because these arguments are positional, we can't provide the second argument without also providing the first. Luckily, we needn't supply arguments to the slice itself, so indicating that a new sequence should be constructed from the same elements. With `loc` that looks like:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.loc[:, :]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
    <tr>
      <th>number</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Mercury</td>
      <td>57.9</td>
      <td>0.330</td>
      <td>5427.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>4.870</td>
      <td>5243.0</td>
      <td>8.9</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.970</td>
      <td>5514.0</td>
      <td>9.8</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Mars</td>
      <td>227.9</td>
      <td>0.642</td>
      <td>3933.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Jupiter</td>
      <td>778.6</td>
      <td>1898.000</td>
      <td>1326.0</td>
      <td>23.1</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>568.000</td>
      <td>687.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>86.800</td>
      <td>1271.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>102.000</td>
      <td>1638.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



Further, we can supply just a column label. If our row slice is empty, then this is yet another way to retrieve the complete `Series` of data for this feature:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.loc[:, 'name']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
number
1    Mercury
2      Venus
3      Earth
4       Mars
5    Jupiter
6     Saturn
7     Uranus
8    Neptune
Name: name, dtype: object
```


</div>
</div>
</div>



More relevant, we can suply a `list` of the features to select.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.loc[:, ['name']]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
    </tr>
    <tr>
      <th>number</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Mercury</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Venus</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Earth</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Mars</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Jupiter</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Saturn</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Uranus</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Neptune</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



And now we know how to produce the two-feature `DataFrame` we were looking for.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planet_distances = planets.loc[:, ['name', 'solar_distance_km_6']]

planet_distances.assign(distance_pct_change=distance_pct_change)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>distance_pct_change</th>
    </tr>
    <tr>
      <th>number</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Mercury</td>
      <td>57.9</td>
      <td>86.873921</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>38.262477</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>52.339572</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Mars</td>
      <td>227.9</td>
      <td>241.641071</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Jupiter</td>
      <td>778.6</td>
      <td>84.112510</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>100.383676</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>56.487380</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



**But that's not right!** Let's take another look at `distance_pct_change`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
distance_pct_change

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0           NaN
1     86.873921
2     38.262477
3     52.339572
4    241.641071
5     84.112510
6    100.383676
7     56.487380
Name: solar_distance_km_6, dtype: float64
```


</div>
</div>
</div>



Indeed, we've changed the index of our `DataFrame` – now it's 1 through 8, rather than the 0 through 7 of `distance_pct_change`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
distance_pct_change.index

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
RangeIndex(start=0, stop=8, step=1)
```


</div>
</div>
</div>



Luckily, there's more than one resolution. Let's tell the index of `distance_pct_change` to increase all of its values by `1`, using the `+=` operator.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
distance_pct_change.index += 1

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
distance_pct_change.index

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
RangeIndex(start=1, stop=9, step=1)
```


</div>
</div>
</div>



Now we're set.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planet_distances.assign(distance_pct_change=distance_pct_change)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>distance_pct_change</th>
    </tr>
    <tr>
      <th>number</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Mercury</td>
      <td>57.9</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>86.873921</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>38.262477</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Mars</td>
      <td>227.9</td>
      <td>52.339572</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Jupiter</td>
      <td>778.6</td>
      <td>241.641071</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>84.112510</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>100.383676</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>56.487380</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



In fact, `pandas` often offers more than one way to achieve the same, or a similar, result. We can also select rows and columns – in this case less succinctly – by specifying what labeled elements we *don't* want, using `drop`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.drop(columns=['mass_kg_24', 'density_kg_m3', 'gravity_m_s2'])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
    </tr>
    <tr>
      <th>number</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Mercury</td>
      <td>57.9</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Venus</td>
      <td>108.2</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Earth</td>
      <td>149.6</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Mars</td>
      <td>227.9</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Jupiter</td>
      <td>778.6</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Saturn</td>
      <td>1433.5</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Uranus</td>
      <td>2872.5</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Neptune</td>
      <td>4495.1</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



## Selection by condition

So far we've selected individuals based on their position in the row index and based on their row index value or label. But particularly in larger data sets, this may not be practical.

To begin, we might sort our data by a column or a set of columns. Say we were having trouble finding Earth – we could produce a new `DataFrame`, sorted by the `name` feature.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.sort_values('name')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
    <tr>
      <th>number</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.970</td>
      <td>5514.0</td>
      <td>9.8</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Jupiter</td>
      <td>778.6</td>
      <td>1898.000</td>
      <td>1326.0</td>
      <td>23.1</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Mars</td>
      <td>227.9</td>
      <td>0.642</td>
      <td>3933.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Mercury</td>
      <td>57.9</td>
      <td>0.330</td>
      <td>5427.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>102.000</td>
      <td>1638.0</td>
      <td>11.0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>568.000</td>
      <td>687.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>86.800</td>
      <td>1271.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>4.870</td>
      <td>5243.0</td>
      <td>8.9</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



By default, this sorts individuals in "ascending" order – from alphabetical "first" to "last" and numerical smallest to greatest.

If instead we wanted to see the most massive planets, we would sort by the `mass_kg_24` feature, but in "descending" order.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets_massive = planets.sort_values('mass_kg_24', ascending=False)

planets_massive

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
    <tr>
      <th>number</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5</td>
      <td>Jupiter</td>
      <td>778.6</td>
      <td>1898.000</td>
      <td>1326.0</td>
      <td>23.1</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>568.000</td>
      <td>687.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>102.000</td>
      <td>1638.0</td>
      <td>11.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>86.800</td>
      <td>1271.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.970</td>
      <td>5514.0</td>
      <td>9.8</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>4.870</td>
      <td>5243.0</td>
      <td>8.9</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Mars</td>
      <td>227.9</td>
      <td>0.642</td>
      <td>3933.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Mercury</td>
      <td>57.9</td>
      <td>0.330</td>
      <td>5427.0</td>
      <td>3.7</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



In both cases, we are interested in the first-listed rows. For example, we can extract the most massive planet, Jupiter, from the sorted `DataFrame`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets_massive.iloc[0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
name                   Jupiter
solar_distance_km_6      778.6
mass_kg_24                1898
density_kg_m3             1326
gravity_m_s2              23.1
Name: 5, dtype: object
```


</div>
</div>
</div>



Sorting in this way can get you pretty far. But more powerfully, you can specify a *condition* or a set of conditions which individuals must pass in order to be selected.

Again, the `DataFrame` property `loc` does the job for us. It supports the output of a `DataFrame` with the same features as the original but only the individuals whose features satisfy the condition.

Rather than using an offset, label or slice, this is specified to `loc` using a *boolean* sequence, which itself indicates the rows satisfying our condition, such as:

    [True, False, True]

But don't worry! We needn't produce this `list` ourselves. We can generate it from a simple conditional expression in Python, applied to the `Series` of data underlying the feature itself.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.mass_kg_24

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
number
1       0.330
2       4.870
3       5.970
4       0.642
5    1898.000
6     568.000
7      86.800
8     102.000
Name: mass_kg_24, dtype: float64
```


</div>
</div>
</div>



Our solar system's inner planets never get any more massive than Earth – less than 6 x 10<sup>24</sup> kilograms in mass. We can exclude such lightweights with the *mask* produced by the following comparison expression.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.mass_kg_24 > 6

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
number
1    False
2    False
3    False
4    False
5     True
6     True
7     True
8     True
Name: mass_kg_24, dtype: bool
```


</div>
</div>
</div>



As you can see, we've produced a new `Series`, populated by Boolean values which reflect that the "statement" of our comparison – that the planets' masses are "greater than 6" thousand yottagrams – is `False` for the first four planets, but `True` for the remainder.

We can specify to `loc` this mask – if we like, of course, the expression itself – and produce our new `DataFrame` of individuals satisfying our condition.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.loc[planets.mass_kg_24 > 6]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
    <tr>
      <th>number</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5</td>
      <td>Jupiter</td>
      <td>778.6</td>
      <td>1898.0</td>
      <td>1326.0</td>
      <td>23.1</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>568.0</td>
      <td>687.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>86.8</td>
      <td>1271.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>102.0</td>
      <td>1638.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



Or, even simpler, we can construct the same sort of look-up to find Earth.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.loc[planets.name == 'Earth']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
    <tr>
      <th>number</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.97</td>
      <td>5514.0</td>
      <td>9.8</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



Above we built our conditions from a known value, such as `6`. We can build a value look-up into our comparison as well.

Another look-up property, `at`, provides a shortcut to scalar values.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.at[3, 'mass_kg_24']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
5.97
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.loc[
    planets.mass_kg_24 > planets.at[3, 'mass_kg_24']
]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
    <tr>
      <th>number</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5</td>
      <td>Jupiter</td>
      <td>778.6</td>
      <td>1898.0</td>
      <td>1326.0</td>
      <td>23.1</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>568.0</td>
      <td>687.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>86.8</td>
      <td>1271.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>102.0</td>
      <td>1638.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



We can also select individuals that satisfy multiple conditions.

Let's compare the planets of our solar system to the Earth. We can begin by selecting only those planets whose gravity is within approximately 50% of Earth's – less than $14.8\frac{m}{s^2}$ and more than $4.8\frac{m}{s^2}$.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
not_too_much_gravity = planets.gravity_m_s2 < planets.at[3, 'gravity_m_s2'] + 5

not_too_much_gravity

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
number
1     True
2     True
3     True
4     True
5    False
6     True
7     True
8     True
Name: gravity_m_s2, dtype: bool
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
not_too_little_gravity = planets.gravity_m_s2 > planets.at[3, 'gravity_m_s2'] - 5

not_too_little_gravity

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
number
1    False
2     True
3     True
4    False
5     True
6     True
7     True
8     True
Name: gravity_m_s2, dtype: bool
```


</div>
</div>
</div>



We might simply invoke `loc` twice, once for each condition.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.loc[not_too_much_gravity].loc[not_too_little_gravity]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
    <tr>
      <th>number</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>4.87</td>
      <td>5243.0</td>
      <td>8.9</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.97</td>
      <td>5514.0</td>
      <td>9.8</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>568.00</td>
      <td>687.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>86.80</td>
      <td>1271.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>102.00</td>
      <td>1638.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



Or, more powerfully, we can combine our conditions into a single conditional mask. In this case, we want *both* conditions to be satisfied, and so we'll combine them using the *bitwise AND* operator: `&`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
not_too_much_gravity & not_too_little_gravity

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
number
1    False
2     True
3     True
4    False
5    False
6     True
7     True
8     True
Name: gravity_m_s2, dtype: bool
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.loc[not_too_much_gravity & not_too_little_gravity]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
    <tr>
      <th>number</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>4.87</td>
      <td>5243.0</td>
      <td>8.9</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.97</td>
      <td>5514.0</td>
      <td>9.8</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Saturn</td>
      <td>1433.5</td>
      <td>568.00</td>
      <td>687.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Uranus</td>
      <td>2872.5</td>
      <td>86.80</td>
      <td>1271.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Neptune</td>
      <td>4495.1</td>
      <td>102.00</td>
      <td>1638.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



We're left with the majority of the planets. Only Mercury, Mars and Jupiter have been excluded – Mercury and Mars for having too little gravity, and Jupiter for having too much.

In fact, we know that Saturn is a gas giant, consisting almost entirely of hydrogen gas – nothing at all like Earth! This fact is indirectly evident from its density: less than 13% of the density of the Earth.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.density_kg_m3 / planets.at[3, 'density_kg_m3']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
number
1    0.984222
2    0.950852
3    1.000000
4    0.713275
5    0.240479
6    0.124592
7    0.230504
8    0.297062
Name: density_kg_m3, dtype: float64
```


</div>
</div>
</div>



We can exclude the gas giants as well by combining our gravity-based conditions with a density-based condition: that the planets' densities are at least 50% of Earth's.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
dense_enough = planets.density_kg_m3 >= planets.at[3, 'density_kg_m3'] * 0.5

dense_enough

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
number
1     True
2     True
3     True
4     True
5    False
6    False
7    False
8    False
Name: density_kg_m3, dtype: bool
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets.loc[not_too_much_gravity & not_too_little_gravity & dense_enough]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>solar_distance_km_6</th>
      <th>mass_kg_24</th>
      <th>density_kg_m3</th>
      <th>gravity_m_s2</th>
    </tr>
    <tr>
      <th>number</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>Venus</td>
      <td>108.2</td>
      <td>4.87</td>
      <td>5243.0</td>
      <td>8.9</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Earth</td>
      <td>149.6</td>
      <td>5.97</td>
      <td>5514.0</td>
      <td>9.8</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



Now we're left with only Venus and Earth.

And, we're given an excellent example of the danger of drawing conclusions from too-small a data set. The two planets appear similar, judging by the above. Venus *is* considerably closer to the sun – 41.4 million kilometers closer than the Earth; but, as we saw, this is the *smallest* distance between any of the planets, and it's difficult to gauge the significance of this feature with regard to its similarity to Earth … at least, this feature on its own.

That said, if our data included a feature like `average_temperature_celsius` – for which Venus would be 462&deg; – then we'd know why Mars is considered the most likely habitable planet in our solar system, outside of the Earth … never mind *its* average temperature of -63&deg; Celsius, and its much lower gravity!



In conclusion, `pandas` and its `DataFrame` offer a great many additions to the data structures, functions and methods of Python, in support of processing and analyzing data. This introduction only covers some of the basic ways in which `pandas` builds upon and differs from what we've seen so far. But don't be overwhelmed! The best way to learn is to dive in. Apply what you've learned here, consult the <a href="https://pandas.pydata.org/docs/" target="_blank" rel="noopener">pandas documentation</a> (and the <a href="https://en.wikipedia.org/wiki/Internet" target="_blank" rel="noopener">Internet</a>) &hellip; and read on!

