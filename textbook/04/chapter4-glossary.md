## List
An ordered, mutable collection in Python that can hold elements of different types.  
Defined with square brackets, e.g. `[1, 2, 3]`.

## Tuple
An ordered, immutable collection in Python. Once created, its elements cannot be changed.  
Defined with parentheses, e.g. `(1, 2, 3)`.

## Set
An unordered collection of unique elements in Python.  
Defined with curly braces, e.g. `{1, 2, 3}`.

## Dictionary
A collection of key–value pairs in Python. Keys must be unique and immutable.  
Defined with curly braces and colons, e.g. `{"a": 1, "b": 2}`.

## Array
A structured, ordered collection of elements of the same type. In Python, often created with `numpy` for numerical data and efficient elementwise operations.

## DataFrame
A two-dimensional, labeled data structure from the `pandas` library, similar to a table or spreadsheet. Rows and columns can have labels, and each column can hold a different data type.

## Index
A numeric or labeled position used to access elements in a sequence (like a list or array) or rows/columns in a DataFrame. Python uses 0-based indexing.

## Mutation
A change to a mutable object (such as a list or dictionary) after it has been created. Mutating an object modifies it in place.

## 0-Indexed
The convention that counting positions in a sequence starts at 0 rather than 1. For example, in `[10, 20, 30]`, the first element `10` is at index `0`.

## Slice
A portion of a sequence selected by specifying a start, stop, and step.  

```python
my_list = [0, 1, 2, 3, 4, 5]
print(my_list[1:4:2])  # [1, 3]
```

## Unpacking (a tuple)
Assigning elements of a tuple (or other iterable) to individual variables in a single statement.  

```python
x, y = (1, 2)
print(x)  # 1
print(y)  # 2
```

## Dot Operator
The `.` used in Python to access attributes and methods of objects.  

```python
my_list = [1, 2, 3]
my_list.append(4)  # uses the dot operator
```

## Aliasing

In Python, *aliasing* can refer to two related but different ideas:

1. **Import aliasing**  
   Using the `as` keyword to give a shorter or alternate name to a module or object when importing.  
   This is often used to make code more concise and to follow conventions.  

   ```python
   import numpy as np
   arr = np.array([1, 2, 3])
   ```

   Here, `np` is an alias for the `numpy` library.

2. **Variable aliasing**  
   When two variables refer to the same underlying object in memory.  
   Changing the object through one variable will affect the other.  

   ```python
   a = [1, 2, 3]
   b = a       # b is an alias for the same list as a
   b.append(4)
   print(a)    # [1, 2, 3, 4]
   ```

In both cases, aliasing means you have more than one “name” that refers to the same thing.

## Elementwise (calculations)
Operations that are applied independently to each element of a collection (like a `numpy` array).  

```python
import numpy as np
arr = np.array([1, 2, 3])
print(arr + 5)  # [6, 7, 8]
```

## Attribute
A value or property stored inside an object that can be accessed using the dot operator.  

```python
import pandas as pd
df = pd.DataFrame({"a": [1, 2, 3]})
print(df.shape)  # (3, 1)
```

## Broadcasting
A set of rules in `numpy` that allow arrays of different shapes to be combined in arithmetic operations by “stretching” one to match the other.  

```python
import numpy as np
arr = np.array([1, 2, 3])
print(arr + 10)  # [11, 12, 13]
```

## Type-Casting
Converting a value from one data type to another.  

```python
print(float(3))   # 3.0
print(int("7"))   # 7
```

## Shallow Copy
A new object that contains references to the elements of the original object rather than fully duplicating them. Nested objects remain shared.  

```python
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]]
```

## Deep Copy
A fully independent copy of an object and all objects nested within it. Changes to the original will not affect the deep copy.  

```python
import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
original[0][0] = 99
print(deep)  # [[1, 2], [3, 4]]
```

## Flatten (an array)

The process of converting a multi-dimensional array into a one-dimensional array. In `numpy`, this can be done with the `.flatten()` method, which returns a **copy** of the data in a single dimension.  

