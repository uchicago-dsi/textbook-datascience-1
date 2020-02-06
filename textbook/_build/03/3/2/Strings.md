---
redirect_from:
  - "/03/3/2/strings"
interact_link: content/03/3/2/Strings.ipynb
kernel_name: python3
has_widgets: false
title: 'Strings'
prev_page:
  url: /03/3/1/Numbers.html
  title: 'Numbers'
next_page:
  url: /03/3/3/Sequences.html
  title: 'Sequences'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Strings

Much of the world's data is text. In many programming languages, text is referred to as a *string*, as in "a string of characters." A string can represent a single character, a word, a sentence, or even the contents of every book in a library. Since text can include characters representing numbers (such as `"5"`), a string can be used to describe that as well.

The result of an expression depends both upon its structure and the types of values that are being combined. So, for instance, combining two strings produces another string. In Python, this is still an *addition expression*; but, it is combining a different type of value – strings rather than numbers.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"data" + "science"

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'datascience'
```


</div>
</div>
</div>



Addition is completely literal – it combines these two strings without regard for their contents. It doesn't add a space because these are different words; that's up to the programmer (you) to specify.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"data" + " " + "science"

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'data science'
```


</div>
</div>
</div>



Either single or double quotes can be used to define a string: `'hi'` and `"hi"` are identical expressions. Double quotes are often preferred for human language, because they allow you to include apostrophes inside of strings, (without additional work).



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"This won't work with a single-quoted string!"

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
"This won't work with a single-quoted string!"
```


</div>
</div>
</div>



Why not? Try it out.



The `str` function returns a standard string representation of any value. Using this function, strings can be constructed that have embedded values.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"That's " + str(1 + 1) + ' ' + str(True)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
"That's 2 True"
```


</div>
</div>
</div>



There's a lot more you can do with strings, as we'll see in [String Methods](/03/5/1/String_Methods.html).

