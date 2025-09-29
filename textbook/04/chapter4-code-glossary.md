## `numpy` library
A popular Python library for numerical computing. Provides arrays, mathematical functions, and tools for linear algebra, statistics, and more. Often imported as `import numpy as np`.

## `NoneType`
The data type of the special value `None`, which represents “nothing” or “no value.”  

## `list.insert()`
Inserts an element at a specified position in a list.  

```python
nums = [1, 2, 3]
nums.insert(1, 10)  # insert 10 at index 1
print(nums)  # [1, 10, 2, 3]
```

## `list.append()`
Adds an element to the end of a list.  

```python
nums = [1, 2, 3]
nums.append(4)
print(nums)  # [1, 2, 3, 4]
```

## `list.index()`
Returns the index of the first occurrence of a value in a list.  

```python
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # 1
```

## `list.pop()`
Removes and returns an element from a list (last by default, or a specified index).  

```python
nums = [1, 2, 3]
nums.pop()      # removes 3
nums.pop(0)     # removes 1
```

## `list.copy()`
Creates a shallow copy of a list.  

```python
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]
```

## `key`:`value` pair
A pair used in dictionaries where a key is mapped to a value.  

```python
student = {"name": "Alice", "age": 20}
# "name" is the key, "Alice" is the value
```

## `dict()`
Creates a dictionary object.  

```python
d = dict(name="Alice", age=20)
print(d)  # {'name': 'Alice', 'age': 20}
```

## `list()`
Creates a list object, often by converting another sequence.  

```python
chars = list("hello")
print(chars)  # ['h', 'e', 'l', 'l', 'o']
```

## `del`
Deletes a variable, list element, or dictionary entry.  

```python
nums = [1, 2, 3]
del nums[1]
print(nums)  # [1, 3]
```

## Membership Operators
Check whether an element is in a sequence.  

- `in`: Returns True if an element exists.  
- `not in`: Returns True if an element does not exist.  

```python
fruits = ["apple", "banana"]
print("apple" in fruits)     # True
print("cherry" not in fruits)  # True
```

## `np.array()`
Creates a `numpy` array from a list (or other sequence).  

```python
import numpy as np
arr = np.array([1, 2, 3])
```

## `np.arange()`
Creates an array with evenly spaced values, similar to `range()`.  

```python
np.arange(0, 10, 2)  # array([0, 2, 4, 6, 8])
```

## `range()`
Creates a sequence of numbers, typically used in loops.  

```python
for i in range(3):
    print(i)  # 0, 1, 2
```

## `array.shape`
An attribute of a `numpy` array showing its dimensions.  

```python
arr = np.array([[1, 2], [3, 4]])
print(arr.shape)  # (2, 2)
```

## `np.reshape()`
Reshapes an array without changing its data.  

```python
arr = np.arange(6)
print(np.reshape(arr, (2, 3)))
```

## `np.row_stack()`
Stacks arrays vertically (row by row).  

```python
a = np.array([1, 2])
b = np.array([3, 4])
print(np.row_stack((a, b)))
```

## `np.column_stack()`
Stacks arrays as columns into a 2D array.  

```python
a = np.array([1, 2])
b = np.array([3, 4])
print(np.column_stack((a, b)))
```

## `np.max()`
Returns the maximum value in an array.  

```python
arr = np.array([1, 5, 3])
print(np.max(arr))  # 5
```

## `np.min()`
Returns the minimum value in an array.  

```python
arr = np.array([1, 5, 3])
print(np.min(arr))  # 1
```

## `np.sum()`
Returns the sum of array elements.  

```python
arr = np.array([1, 2, 3])
print(np.sum(arr))  # 6
```

## `np.average()`
Returns the average (mean) of array elements.  

```python
arr = np.array([1, 2, 3])
print(np.average(arr))  # 2.0
```

## `np.sqrt()`
Returns the square root of array elements.  

```python
arr = np.array([1, 4, 9])
print(np.sqrt(arr))  # [1. 2. 3.]
```

## `np.power()`
Raises array elements to a power.  

```python
arr = np.array([1, 2, 3])
print(np.power(arr, 2))  # [1 4 9]
```

## `np.log()`
Computes the natural logarithm (log with base *e*) of array elements.  

```python
arr = np.array([1, np.e, np.e**2])
print(np.log(arr))  # [0. 1. 2.]
```

## `list.sort()`
Sorts a list in place.  

```python
nums = [3, 1, 2]
nums.sort()
print(nums)  # [1, 2, 3]
```

## `list.reverse()`
Reverses the elements of a list in place.  

```python
nums = [1, 2, 3]
nums.reverse()
print(nums)  # [3, 2, 1]
```

## `np.zeros`
Creates an array filled with zeros.  

```python
print(np.zeros((2, 3)))
```

## `np.ones`
Creates an array filled with ones.  

```python
print(np.ones((2, 3)))
```

## `array.astype()`
Converts the elements of an array to a different data type.  

```python
arr = np.array([1.5, 2.8, 3.2])
print(arr.astype(int))  # [1 2 3]
```

## `array.flatten`
Returns a **copy** of the array collapsed into one dimension. Useful for turning a multi-dimensional array into a simple list-like array.  

```python
arr = np.array([[1, 2], [3, 4]])
print(arr.flatten())  # [1 2 3 4]
```

## `np.sort()`
Returns a sorted copy of an array. By default, it sorts in *ascending order* along the last axis. For descending order, reverse the result with slicing (`[::-1]`).  

```python
arr = np.array([3, 1, 2])
print(np.sort(arr))        # [1 2 3]
print(np.sort(arr)[::-1])  # [3 2 1]
```

## `dict.keys()`
A method that returns a view object containing all the keys in a dictionary.  

```python
student = {"name": "Alice", "age": 20}
print(student.keys())  # dict_keys(['name', 'age'])
```

## `dict.values()`
A method that returns a view object containing all the values in a dictionary.  

```python
student = {"name": "Alice", "age": 20}
print(student.values())  # dict_values(['Alice', 20])
```

## `dict.items()`
A method that returns a view object of the dictionary’s key–value pairs as tuples.  

```python
student = {"name": "Alice", "age": 20}
print(student.items())  # dict_items([('name', 'Alice'), ('age', 20)])
```

## `dict.update()`
A method that updates a dictionary with key–value pairs from another dictionary (or from keyword arguments). Existing keys are overwritten.  

```python
student = {"name": "Alice", "age": 20}
student.update({"age": 21, "major": "Data Science"})
print(student)  # {'name': 'Alice', 'age': 21, 'major': 'Data Science'}
```

## View Object
A special object returned by certain dictionary methods such as `.keys()`, `.values()`, and `.items()`.  
A view object acts like a dynamic “window” into the dictionary’s contents:  

- It automatically updates if the dictionary is changed.  
- It is iterable, meaning you can loop over it just like a list.  
- If you need a fixed snapshot of the contents, you can convert it into a list with `list()`.  

```python
student = {"name": "Alice", "age": 20}
keys_view = student.keys()
print(keys_view)  # dict_keys(['name', 'age'])

student["major"] = "Data Science"
print(keys_view)  # dict_keys(['name', 'age', 'major'])  # updated automatically

print(list(keys_view))  # ['name', 'age', 'major']
```
