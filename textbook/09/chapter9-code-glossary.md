## pandas.DataFrame.groupby()
Helps with groupby operations on dataframes that involves grouping records based on one or more criteria such that different aggregate functions can be applied on the groups.  

```python
import pandas as pd
# Create a sample dataframe
data = {
    'Course Name': ['CS120', 'DATA118', 'CS221', 'DATA211', 'DATA259', 'CS340'],
    'Level': ['I', 'I', 'II', 'II', 'II', 'III', ],
    'Size' : [54, 29, 35, 55, 118, 67]
}
course_df = pd.DataFrame(data)

# Group courses by level
level_groups = course_df.groupby('Level')

# Print the average size for Level I courses
print(level_groups.get_group('I')[['Size']].mean()) #Size  41.5
```

## np.random.choice()
Allows for random sampling from a given array of items. Can also be used to take in an integer argument, `a`, and randomly sample integers from within the range given by `np.arange(a)`. By default, the sampling is with replacement. But this can be altered by setting the parameter `replace` to `False`.

```python
import numpy as np

letters = ['a', 'b', 'c', 'd', 'e']
random_letters_with_replacement = np.random.choice(letters, size=3)
print(f"Randomly chosen letters with replacement: {random_letters_with_replacement}") # Randomly chosen letters with replacement: ['a' 'c' 'c']

random_letters_without_replacement = np.random.choice(letters, size=3, replace=False)
print(f"Randomly chosen letters without replacement: {random_letters_without_replacement}") # Randomly chosen letters without replacement: ['e' 'd' 'b']

# Choose 5 random integers from 0 up to (but not including) 5
random_integers = np.random.choice(5, size=5)
print(f"Random integers up to 5: {random_integers}") # Random integers up to 5: [1 4 2 0 1]
```

## np.random.seed()
In order to get reproducible results out of functions that utilizes the `np.random` module in different executions, it is advisable to set a seed. This is done to initialize the pseudo-random number generator algorithm, ensuring that a 'randomized' generation of numbers within `numpy`'s random functions is ultimately reproducible when using the same seed value.

```python
# Set a specific seed value
np.random.seed(42)

# Generates the same random numbers between 0 to 5 in different runs
print(f"Five random numbers between 0 to 5: {np.random.choice(5, size=5)}") # Five random numbers between 0 to 5: [3 4 2 4 4]
```