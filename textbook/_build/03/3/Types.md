---
redirect_from:
  - "/03/3/types"
interact_link: content/03/3/Types.ipynb
kernel_name: python3
has_widgets: false
title: 'Data Types'
prev_page:
  url: /03/2/1/Growth.html
  title: 'Example: Growth Rates'
next_page:
  url: /03/3/1/Numbers.html
  title: 'Numbers'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Data Types

Every value has a _type_. So far we've dealt mainly with numbers, such as `12`. You may also have seen text, which is represented in Python with either single or double quotes:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('this is known as a "string" of text')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
this is known as a "string" of text
```
</div>
</div>
</div>



In fact, there are more types than that. Above we also used the built-in function `print`, to display the underlying value of our string.

On the other hand, the built-in function `type` returns the type of the result of any expression. Python indicates that the type of `print` is a `builtin_function_or_method`. (The distinction between a *function* and a *method* is not important at this stage.)



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
type(print)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
builtin_function_or_method
```


</div>
</div>
</div>



This chapter will explore many useful types of data.

