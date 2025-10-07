## df.apply(given_function)
The .apply method is used to execute a function on a DataFrame or subsets of a DataFrame. Note, the given_function can be a built-in or user defined function.


## df.applymap(given_function) 
The .applymap method is used to execute a function on every element of a DataFrame. Note, df is a DataFrame and given_function can be a built-in or user defined function.


## pd.merge(df_left, df_right)
combines common column names and takes all common rows of two DataFrames, df_left and df_right, to make a new DataFrame. The order of df_left is preserved. 

## df.drop()
The .drop() method is used to delete specific rows or columns from a DataFrame, df.

## df.groupby()
The .groupby() method is applied to a DataFrame, df, to group data based on one or more criteria. Note an aggregate function is typically applied and calculate for each group. 

## df.groupby().first
The `.first() method returns the first row, if it exists, of each group.

## df.pivot_table()
There are two general format for *pivot_table*;

```python
df.pivot_table(data, index='group_1', columns='group_2', aggfunc='function')
```
or alternately, dependent on preference, the below format from directly from a pandas method can be used.

```python
pd.pivot_table(df, values='data', index='group_1', columns = 'group_2', aggfunc='function').
```

In both formats, we have, df is the the given DataFrame, each unique value in `index` gets its own row, each unique value in `columns` gets its own column, and `data` specifies the value in the DataFrame to which we want to apply `aggfunc`
