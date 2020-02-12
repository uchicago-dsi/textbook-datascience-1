---
redirect_from:
  - "/03/6/functions"
interact_link: content/03/6/Functions.ipynb
kernel_name: python3
has_widgets: false
title: 'Functions'
prev_page:
  url: /03/5/1/String_Methods.html
  title: 'String Methods'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Functions

Python provides a great many built-in functions for processing and analyzing data; but, these are finite. Before long you'll find need to define your own functions.

Functions essentially enable you to assign a name to an *expression* – (really to an entire block of code) – facilitating the re-use of complex code and the organization of code. And, as important, this allows for the evaluation of your code by another function, such that you may customize how another function operates!



In our exploration of [list mappings](/03/3/3/Sequences.html#mappings), we considered the none-too-complex expression `2 * prime`, where `prime` referred to a prime number, and an element of an abridged list of these.

We might encapsulate this expression by a function as follows.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def double(num):
    return 2 * num

```
</div>

</div>



As you can see, the syntax of a function definition requires:

1. the keyword `def`
1. followed by the name to assign to the function – in this case `double`
1. in parentheses, names to assign to any values expected as input to the function, when it is called – in this case the single argument `num`
1. a colon to finalize this first line

With the above *signature* line complete, the *body* of the function consists of the expression(s) we'd like to be evaluated whenever the function is called.

Note: the body of the function – every line of its code – must be indented. Conventionally, this indentation is by **four spaces**.

Finally, the keyword `return` indicates that execution of the function should **stop** with that line. And, the value of whatever expression follows `return` will be the value of the function's *call expression*, and "returned" to where the function was called.

The function signature and body are required; however, the `return` keyword is not required. Moreover, not all functions will have any particular value to return, and may therefore omit this.



Having defined `double`, it is now available to us to use no differently from a built-in function.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
double(2)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
4
```


</div>
</div>
</div>



This works no matter what input `num` we provide – that is, `num` is reassigned, and our expression reevaluated, every time.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
double(55)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
110
```


</div>
</div>
</div>



And though the name `num` is assigned *within* the body of the function, for evaluation by the expressions it contains, `num` *is not* assigned elsewhere.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
num

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-c774dac2b598> in <module>
    ----> 1 num
    

    NameError: name 'num' is not defined


```
</div>
</div>
</div>



To wit, if we were to assign `num`, it would be safe from reassignment by `double`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
num = 2015

double(99)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
198
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
num

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
2015
```


</div>
</div>
</div>



However trivial the code, being able to assign a callable name to it can be fantastically useful – for you and for anyone else who might review your code or collaborate with you.

In Python it is also therefore conventional to assign descriptions to functions, in the form of "documentation strings," or *docstrings*.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def double(num):
    """Multiply any number by `2`
    
    "…Why?" you might ask – it's FUNdamental!
    
    """
    return 2 * num

```
</div>

</div>



Above we've redefined `double` with a docstring.

Syntactically, a docstring is _any_ string which immediately follows the function definition's signature. Conventionally, rather than either a single-quoted or double-quoted string, a *triple-quoted* string is used – either `'''` or `"""` – (though technically you might consider the latter a *sextuple-quote*!). This is so that you needn't worry about using either a `'` or a `"` within your text; and, as above, your triple-quoted string may span multiple lines.

Docstrings are supremely useful for explaining the intent and features of a function. You might also have seen *comments* in Python code:

    # The below computes a number's double

And, comments serve a similar and complementary purpose. However, docstrings receive special handling in Python.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(double)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on function double in module __main__:

double(num)
    Multiply any number by `2`
    
    "…Why?" you might ask – it's FUNdamental!

```
</div>
</div>
</div>



Above, Python reproduced our docstring as part of its "help" document for the function.



Of course, functions aren't just about reuse, organization and clarity. As we'll see in later chapters, they're hugely important in Data Science, for specifying arbitrary expressions as arguments to another function. This form is slightly less conventional in Python, but still supported and widely-used.

We can now extend our toolkit of ways of mapping a sequence of input data to a desired output. Remember the list comprehension:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
primes_abridged = [2, 3, 5, 7, 11, 13, 17, 19, 23]

[2 * prime for prime in primes_abridged]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[4, 6, 10, 14, 22, 26, 34, 38, 46]
```


</div>
</div>
</div>



While the list comprehension is useful, it is not always applicable. A *functional* way of achieving the same might involve the type `map`.

`map` is built into Python, like `list`; however, unlike `list`, `map` doesn't have a syntax dedicated to its construction. Instead, it can be called by name – no different from a function – to construct maps.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
doubled_map = map(double, primes_abridged)

```
</div>

</div>



In fact, the *call signature* of `map` isn't *so* different from the syntax of the list comprehension. But, we've *factored* our expression `2 * prime` into our function under the name `double`; and, `map` handles the logic of calling `double` sequentially, for each element contained by `primes_abridged`.

**However**: Depending on your version of Python, `doubled_map` might not yet be quite what you want!



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
doubled_map

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
<map at 0x7ae09853fb70>
```


</div>
</div>
</div>



After all, it's not really a `list`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
type(doubled_map)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
map
```


</div>
</div>
</div>



However, a `map` is *like* a sequence, (if an opaque one). **And** we're free to convert it into a list for our purposes here.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
primes_doubled = list(doubled_map)

primes_doubled

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[4, 6, 10, 14, 22, 26, 34, 38, 46]
```


</div>
</div>
</div>



Therefore, our full functional equivalent of the list comprehension may be expressed as follows:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
list(map(double, primes_abridged))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[4, 6, 10, 14, 22, 26, 34, 38, 46]
```


</div>
</div>
</div>



While you'll find that the Data Science toolkit often doesn't look quite like the above, these are nonetheless its fundamentals. And you are now ready to proceed!

