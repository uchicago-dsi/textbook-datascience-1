## np.mean() 
Calculates the mean of elements in an array.

```python
a = [10,20,30,40,50]
np.mean([a])   # 30
```

## np.std() 
Calculates the standard deviation of elements in an array.

```python
a = [10,20,30,40,50]
np.std([a])   #14.14
```

## .sample()
Samples one or more rows from a dataframe. `.sample()` can take in multiple arguments, including `n` (number of rows to sample; defaults to 1), `random_state` (the initial state of the pseudo-random generator; defaults to None), and `replace` (whether we want to "replace" rows for re-sampling; defaults to False)

```python
DataFrame.sample(n = 1, random_state = None, replace = False)
```

## np.random.uniform()
A function that randomly generates continuous values from a uniform distribution. The function takes in a value for `low` and `high` as well as `size` (the number of samples to draw) and draws from the continuous uniform probability distribution on the interval [`low` to `high`). 

```python
np.random.uniform(low = 1, high = 6, size = 10)
```

## stats.norm()
Generates a normal continuous distribution with mean (`loc`) and standard deviation (`scale`)

```python
stats.norm(loc, scale)
```