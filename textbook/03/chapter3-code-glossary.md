## Arithmetic Operators
- `+` : Addition  
- `-` : Subtraction  
- `*` : Multiplication  
- `/` : Division (always returns a float)  
- `//` : Floor Division (rounded down to nearest whole number)  
- `%` : Modulus (remainder after division)  
- `**` : Exponentiation (power)  

## Comparison Operators
- `==` : Equal  
- `!=` : Not equal  
- `<` : Less than  
- `<=` : Less than or equal  
- `>` : Greater than  
- `>=` : Greater than or equal  

## Assignment Operator
- `=` : Assigns a value to a variable  

## Logical (Boolean) Operators
- `and` : True if both are true  
- `or` : True if at least one is true  
- `not` : True if input is false  

## float()
Converts a value into a float (decimal number).  

```python
float(7)   # 7.0
```

## int()
Converts a value into an integer (whole number).  

```python
int(7.9)   # 7
```

## bool()
Converts a value into a boolean (True or False).  

```python
bool(0)    # False
bool(5)    # True
```

## NameError
Error raised when you try to use a variable or function name that has not been defined.  

```python
print(x)   # NameError: name 'x' is not defined
```

## SyntaxError
Error raised when Python code is written incorrectly and does not follow Python’s rules.  

```python
if True print("hi")   # SyntaxError
```

## TypeError
Error raised when an operation or function is applied to a value of the wrong type.  

```python
"5" + 2   # TypeError
```

## ValueError
Error raised when a function receives an argument of the right type but an inappropriate value.  

```python
int("hello")   # ValueError
```

## Escape Sequences
- `\'` : Inserts a single quote in a string  
- `\"` : Inserts a double quote in a string  
- `\n` : Newline (starts a new line)  
- `\t` : Tab (inserts horizontal spacing)  

```python
print("Line 1\nLine 2")
# Line 1
# Line 2
```

## str()
Converts a value into a string.  

```python
str(123)   # '123'
```

## max(...)
Returns the maximum (largest) value from the given inputs.  

```python
max(3, 9, 5)   # 9
```

## min(...)   
Returns the minimum (smallest) value from the given inputs.  

```python
min(3, 9, 5)   # 3
```

## sum(...)      
Returns the sum of all values in a given iterable (like a list).  

```python
sum([1, 2, 3])   # 6
```

## abs(...)     
Returns the absolute value of the given number.  

```python
abs(-7)   # 7
```

## round(...)   
Rounds a number to the nearest integer (or to a specified number of decimal places if given).  

```python
round(3.14159, 2)   # 3.14
```

## len(...)   
Returns the length (number of items) of the given input.  

```python
len("hello")   # 5
```

## type(...)   
Returns the data type of the input.  

```python
type(3.14)   # <class 'float'>
```

## print(...)   
Displays the input on the console.  

```python
print("hello")   # hello
```

## help()
Displays documentation about functions, objects, or modules.  

```python
help(len)
```

## math library
A standard Python library that provides mathematical functions and constants.  

```python
import math
```

## math.log(...)      
Returns the logarithm of a number. Uses base e (natural log) if no base is specified.  

```python
import math
math.log(8, 2)   # 3.0
```

## math.exp(...)   
Returns e to the power of the given number.  

```python
import math
math.exp(2)   # 7.389...
```

## math.sqrt(...)     
Returns the square root of the input.  

```python
import math
math.sqrt(16)   # 4.0
```

## math.floor(...)   
Rounds the input down to the nearest whole number.  

```python
import math
math.floor(3.9)   # 3
```

## math.ceil(...)   
Rounds the input up to the nearest whole number.  

```python
import math
math.ceil(3.1)   # 4
```

## math.factorial(...)   
Returns the factorial of the input.  

```python
import math
math.factorial(5)   # 120
```

## math.pi   
The constant $\pi$ (pi ≈ 3.14159).  

```python
import math
math.pi   # 3.14159...
```

## math.e   
The constant $e$ (Euler’s number ≈ 2.71828).  

```python
import math
math.e   # 2.71828...
```

## string.replace('old', 'new')      
Returns a copy of the string with all 'old' substrings replaced by 'new'.  

```python
"hello world".replace("world", "Python")
# 'hello Python'
```

## string.upper() 
Returns the string in all uppercase letters.  

```python
"hello".upper()   # 'HELLO'
```

## string.lower()    
Returns the string in all lowercase letters.  

```python
"HELLO".lower()   # 'hello'
```

## string.strip() 
Returns the string with whitespace removed from the beginning and end.  

```python
"  hello  ".strip()   # 'hello'
```

## Function Definition
```python
def function_name(input_arguments):
    """ Docstring """
    
    # body of function
    return output
```

## Comment Character
- `#` : Signals to Python that anything written after it should be ignored  

```python
# This is a comment
```