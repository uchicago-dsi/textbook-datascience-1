## Modulo / Mod / Modulus
The modulo operation (`%` in Python) finds the remainder after division of one number by another.  
```python
    7 % 3  # returns 1 because 7 divided by 3 is 2 with a remainder of 1
```

## Floor Division
Division where the result is rounded down to the nearest whole number.  
```python
    7 // 3  # returns 2 because 7 divided by 3 is 2.3, which is rounded down to 2
```

## Syntax
The rules that define how Python code must be written so that the computer can understand it. Incorrect syntax usually causes an error.

## Mutable Data Types
Data types whose values can be changed after creation. Examples: lists, dictionaries, sets.

## Immutable Data Types
Data types whose values cannot be changed after they are created. Examples: integers, floats, strings, tuples.

## Integer
A whole number (positive, negative, or zero) without a decimal point. Example: `-5`, `0`, `42`.

## Float
A number with a decimal point. Example: `3.14`, `-0.001`.

## Boolean
A data type with only two possible values: `True` or `False`.

## String
A sequence of characters, such as letters, numbers, or symbols, enclosed in quotation marks. Example: `"hello"`.

## Concatenate
To link strings together using the `+` operator.  
```python
    "Hello" + " " + "world"  # "Hello world"
```

## Escape Sequence
A special character combination used inside strings to represent things like newlines (`\n`) or tabs (`\t`).  
```python
    "Line 1\nLine 2"
```

## Lexicographic
Ordering of strings based on the alphabetical order of characters, using their underlying ASCII or Unicode values.

## Call (a function)
To execute a function by writing its name followed by parentheses.  
```python
    print("Hello")
```

## Library 
A collection of modules that provide useful tools for programming (e.g., `NumPy`, `pandas`).

## Module
A single Python file that contains functions, classes, and variables related to a specific task (e.g., the `math` module).

## Object
A piece of data in Python that has a type and associated methods. Everything in Python is an object.

## Method
A function that is attached to an object and called with dot notation.  
```python
    "hello".upper()
```

## Function (built-in, user-defined)
A reusable block of code that performs a task.  
- **Built-in function:** provided by Python (e.g., `len()`).  
- **User-defined function:** written by the programmer with `def`.

## docstring
A special string inside a function, class, or module that describes what it does. Typically written inside triple quotes.  

## Argument
The value you pass into a function when you call it.  
```python
    len("hello")  # "hello" is the argument
```

## Output
The result a program or function produces.

## Function Definition
The part of the code where a function is created, starting with the `def` keyword.

## Function Body
The indented code block inside a function that runs when the function is called.

## Scope
Where a variable is visible in code.  
- Variables defined inside a function have **local scope**.  
- Variables defined outside functions have **global scope**.

## Optional Argument
A function argument that you don’t have to provide when calling the function.

## Default Value
The value an optional argument takes if no value is provided.  
```python
    def greet(name="world"):
        print("Hello", name)
```

## Binary
A concept meaning "two possible values" or "two categories."  
For example, a binary variable can only be `True` or `False`, or "yes" or "no."

Can also refer to a number system that uses only `0` and `1`. Computers store and process all data in binary.

## Expression
Any piece of code that Python can evaluate to a value. Example: `2 + 3`, `"hi" * 2`.

## Assignment Statement
A statement that stores a value in a variable using `=`.  
```python
    x = 5
```

## Variable / Variable Name
A name that refers to a value stored in memory. Example: `x = 10`.

## Reserved Words
Special words in Python that should never be used as variable names because they have specific meanings (e.g., `if`, `for`, `while`).

## Comment
Text in code that Python ignores. Used for notes or explanations.  
```python
    # This is a comment
```
