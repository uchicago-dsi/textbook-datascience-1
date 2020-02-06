---
redirect_from:
  - "/03/5/1/string-methods"
interact_link: content/03/5/1/String_Methods.ipynb
kernel_name: python3
has_widgets: false
title: 'String Methods'
prev_page:
  url: /03/5/Calls.html
  title: 'Call Expressions'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# String Methods

In addition to standard operators and functions, values can be manipulated using *methods*. In the case of strings, a transformed string can be constructed from an existing string using a *string method*. A string method is a function which operates on a string, and which is invoked differently from a regular function – in Python, methods are called by placing a period after their target, and then calling the method function.

For example, the `upper` method generates an uppercased version of a string.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"loud".upper()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'LOUD'
```


</div>
</div>
</div>



Perhaps the most important method is `replace`, which replaces all instances of a substring within the string. The `replace` method takes two arguments: the text to be replaced and its replacement.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
'hitchhiker'.replace('hi', 'ma')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'matchmaker'
```


</div>
</div>
</div>



String methods can also be invoked using assigned names, as long as those names are assigned to strings. So, for instance, the following two-step process generates the word "degrade" starting from "train", by first creating "ingrain" and then applying a second replacement.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
text0 = "train"
text1 = text0.replace('t', 'ing')
text1.replace('in', 'de')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'degrade'
```


</div>
</div>
</div>



Note that the line –

    text1 = text0.replace('t', 'ing')

– doesn't change the string `text0`, which is still `"train"`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
text0

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'train'
```


</div>
</div>
</div>



The method invocation (repeated below) merely produces a value, which is the string "ingrain".



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
text0.replace('t', 'ing')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'ingrain'
```


</div>
</div>
</div>



This may be the first time you've seen methods, but methods are not unique to strings.  As we will see shortly, other types of objects can have them.

