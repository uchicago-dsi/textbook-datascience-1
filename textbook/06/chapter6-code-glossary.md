## pandas library
The pandas library is a Python package built on top of `numpy` for data analysis and manipulation.

```python
import pandas as pd
```

## pd.DataFrame(...)
Creates a 2D tabular data structure in pandas from data like arrays, lists, or dictionaries, with labeled rows and columns.

```python
import pandas as pd

Students = pd.DataFrame({'Name':["Alice", "Bob", "Eve"], 'Major':["Math", "Music", "History"]}) # creates a DataFrame with two columns containing information about student's names and majors. 
```

## pd.Series(...)
Creates a one-dimensional labeled array in pandas. It can be made from a list, array, or dictionary.

```python
import pandas as pd

Even_numbers = pd.Series([2,4,6,8]) # creates a Series object consisting of the integers 2, 4, 6, 8.
```

## pd.read_csv(file_path)
Reads data from a CSV file, either stored on your computer or accessible via a URL, into a pandas DataFrame.

```python
import pandas as pd

planets_df = pd.read_csv("planets.csv")  # reads the CSV file 'planets.csv' into a DataFrame.
```

## pd.RangeIndex(start=0, stop, step=1)
Creates a sequence of integers to be used as a default index in a pandas DataFrame or Series.

```python
import pandas as pd

index = pd.RangeIndex(start=5, stop=10, step=2)  # creates an index: 5, 7, 9
```

## pd.Index(...)
Creates an immutable, ordered collection of labels used as the index of a pandas Series or DataFrame.

```python
import pandas as pd

index = pd.Index([10, 20, 30])  # creates an Index with labels 10, 20, 30
```

## df.set_index(column_name)
Sets one or more columns of a DataFrame as the new index, replacing the existing index.

```python
import pandas as pd

df = pd.DataFrame({'Name': ["Alice", "Bob"], 'Age': [24, 22]})
df = df.set_index('Name')  # sets the 'Name' column as the index
```

## df.index
Returns the index (row labels) of a DataFrame or Series.

```python
import pandas as pd

df = pd.DataFrame({'Name': ["Alice", "Bob"], 'Age': [24, 22]})
df.index  # shows the row labels (default RangeIndex in this case)
```

## df.columns
Returns the column labels of a DataFrame as an Index object.

```python
import pandas as pd

df = pd.DataFrame({'Name': ["Alice", "Bob"], 'Age': [24, 22]})
print(df.columns)  # Output: Index(['Name', 'Age'], dtype='object')
```

## obj.tolist()
Converts a pandas Series, Index, or a NumPy array into a regular Python list.

```python
import pandas as pd

df = pd.DataFrame({'Name': ["Alice", "Bob"], 'Age': [24, 22]})
obj = df.columns
obj.tolist()  # ['Name', 'Age']
```

## df['column_name']
Selects a single column from a DataFrame as a Series, or multiple columns as a DataFrame when given a list of column names.

```python
import pandas as pd

df = pd.DataFrame({'Name': ["Alice", "Bob"], 'Age': [24, 22], 'Interest': ['Music', 'Dance']})

# Single column as Series
df['Name'] # Outputs the Name column as a pandas Series.

# Multiple columns as DataFrame
df[['Name', 'Age']] # Outputs the Name and Age columns from the DataFrame.
```

## df['column_name'].diff()
Calculates the difference between consecutive values in a Series, useful for computing changes over time.

```python
import pandas as pd

df = pd.DataFrame({'Item': ['A', 'B', 'C'], 'Value': [10, 15, 20]})
df['Value'].diff() # Outputs a Series showing differences between consecutive values: [NaN, 5.0, 5.0]
```

## df['column_name'].mean()
Calculates the mean of a Series (a particular column of the DataFrame).

## df['column_name'].median()
Calculates the median of a Series.

## df['column_name'].mode()
Calculates the mode of a Series.

## df['column_name'].std()
Calculates the standard deviation of a Series.

## df['column_name'].sum()
Calculates the sum of all values in a Series.

## df['column_name'].min()
Finds the minimum value in a Series.

## df['column_name'].max()
Finds the maximum value in a Series.

## df['column_name'].count()
Counts the number of non-NA values in a Series.

## df['column_name'].var()
Calculates the variance of a Series.

## df['column_name'].quantile(q)
Returns the value at the q-th quantile of a Series.

## df['column_name'].cumsum()
Computes the cumulative sum of a Series.

## df['column_name'].cumprod()
Computes the cumulative product of a Series.

## df['column_name'].rename(new_name)
Renames a Series or DataFrame column to the specified new name.

## df['column_name'].pct_change()
Calculates the percentage change between consecutive values in a Series, useful for analyzing relative changes over time.

## df.assign(new_column = expression)
Adds a new column to a DataFrame or modifies existing columns by evaluating the given expression, returning a new DataFrame without modifying the original.

```python
df.assign(NewAge = df['Age'] + 5)  # creates a new column 'NewAge' with values 5 more than 'Age'
```

## df.copy()
Creates and returns a copy of the DataFrame (or Series).

## df.drop(labels, axis)
Removes specified rows or columns from a DataFrame, returning a new DataFrame by default.

```python
import pandas as pd

df = pd.DataFrame({'Name': ["Alice", "Bob"], 'Age': [24, 22]})
print(df)

# Drop a column
print(df.drop('Age', axis=1))

# Drop a row
print(df.drop(0, axis=0))
```

## df[n:m]
Selects rows from index `n` up to (but not including) index `m` of the DataFrame, similar to Python list slicing.

```python
import pandas as pd

df = pd.DataFrame({'Name': ["Alice", "Bob", "Charlie"], 'Age': [24, 22, 30]})
print(df[0:2])  # selects the first two rows (indices 0 and 1)
```

## df.head(n)
Returns the first `n` rows of the DataFrame (default is 5).

```python
import pandas as pd

df = pd.DataFrame({'Name': ["Alice", "Bob", "Charlie", "David"], 'Age': [24, 22, 30, 28]})
print(df.head(2))  # first 2 rows
```

## df.tail(n)
Returns the first `n` rows of the DataFrame (default is 5).

```python
import pandas as pd

df = pd.DataFrame({'Name': ["Alice", "Bob", "Charlie", "David"], 'Age': [24, 22, 30, 28]})
print(df.tail(2))  # last 2 rows
```

## df.iloc[row_index, column_index]
Selects rows and columns from a DataFrame by integer position (0-based indexing).

```python
import pandas as pd

df = pd.DataFrame({'Name': ["Alice", "Bob", "Charlie"], 'Age': [24, 22, 30]})

print(df.iloc[0, 0])   # element at first row, first column ('Alice')
print(df.iloc[0:2, 1]) # 'Age' values of the first two rows
```

## df.reset_index()
Resets the index of the DataFrame to the default integer index, moving the old index to a column unless `drop=True` is specified.

```python
import pandas as pd

df = pd.DataFrame({'Name': ["Alice", "Bob"]}, index=['a', 'b'])
print(df)

print(df.reset_index())        # Outputs a DataFrame with the old index as a new column
print(df.reset_index(drop=True)) # Outputs a DataFrame with a default integer index, old index removed
```

## df.loc[row_labels, column_labels]
Selects rows and columns from a DataFrame by **label** (row/column names) rather than integer position.

```python
import pandas as pd

df = pd.DataFrame({'Name': ["Alice", "Bob"], 'Age': [24, 22]}, index=['a', 'b'])

print(df.loc['a', 'Name'])         # Outputs the value at row 'a' and column 'Name' ('Alice')
print(df.loc['a':'b', 'Age'])      # Outputs the 'Age' column for rows 'a' through 'b'
```

## df.sort_values(by, ascending=True)
Sorts the DataFrame by the values of one or more columns. By default, sorts in ascending order.

```python
import pandas as pd

df = pd.DataFrame({'Name': ["Alice", "Bob", "Charlie"], 'Age': [24, 22, 30]})

print(df.sort_values(by='Age'))           # Outputs the DataFrame sorted by 'Age' in ascending order
print(df.sort_values(by='Age', ascending=False))  # Outputs the DataFrame sorted by 'Age' in descending order
```