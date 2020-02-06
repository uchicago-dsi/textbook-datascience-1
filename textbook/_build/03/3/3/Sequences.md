---
redirect_from:
  - "/03/3/3/sequences"
interact_link: content/03/3/3/Sequences.ipynb
kernel_name: python3
has_widgets: false
title: 'Sequences'
prev_page:
  url: /03/3/2/Strings.html
  title: 'Strings'
next_page:
  url: /03/4/Comparison.html
  title: 'Comparisons'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
Modern computing would be inconceivable without the ability to interact with a *collection* of multiple values at once, and more specifically the ordered *sequence* of values. In Python, the most common of these data types is called the `list`.

Lists are syntactically defined using commas to separate their constituent elements, and enclosed by square brackets.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
primes_abridged = [2, 3, 5, 7, 11, 13, 17, 19, 23]

primes_abridged

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[2, 3, 5, 7, 11, 13, 17, 19, 23]
```


</div>
</div>
</div>



Lists not only enable us to address a sequence of values at once. They also permit us to refer to their elements:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
primes_abridged[0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
2
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
primes_abridged[5]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
13
```


</div>
</div>
</div>



Above, we retrieved individual elements from our list, by indicating the *index* of the element to retrieve – after the name assigned to the list, and with the index itself enclosed in square brackets.

**Note!** We referred to the *first* element of our list using the index `0`, and to the *sixth* with the index `5`. In computer programming, you can think of this reference not as the "number" or the "count" of the element, but rather as an "offset" from the beginning of the list.

Even the index, or offset, `-1` is valid, and this is the general way to refer to the last element of the list:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
primes_abridged[-1]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
23
```


</div>
</div>
</div>



We can also retrieve a subset of the elements of our list, for example using the *slice*.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
primes_really_abridged = primes_abridged[2:5]

primes_really_abridged

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[5, 7, 11]
```


</div>
</div>
</div>



In the syntax of the slice, we indicated that we would like to construct a new list, consisting of the elements at indices `2` through 4, ending *before* index `5`.

A slice can also indicate a *step* other than `1`, such that some elements are stepped over, or skipped. And, a slice can omit either the element to start with, or the element to stop with, or both:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
every_other_prime_abridged = primes_abridged[::2]

every_other_prime_abridged

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[2, 5, 11, 17, 23]
```


</div>
</div>
</div>



Most important, lists enable us to instruct the computer to apply an operation to each element of the list in sequence.

Most simply, we can count the number of elements in our list.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(primes_abridged)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
9
```


</div>
</div>
</div>



Better yet, we can `sum` the elements.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sum(primes_abridged)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
100
```


</div>
</div>
</div>



Combining the two of these, we can compute an average or mean.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sum(primes_abridged) / len(primes_abridged)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
11.11111111111111
```


</div>
</div>
</div>



In the above, we computed *aggregates* of our data. But we can also process our data to make a new list, or *mapping*.

Consider the following expression, which creates a (partial) mapping of `primes_abridged`, with its elements doubled:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
primes_doubled = [
    2 * primes_abridged[0],
    2 * primes_abridged[1],
]

primes_doubled

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[4, 6]
```


</div>
</div>
</div>



The above form *works*, strictly speaking; but, it would require a lot of typing to process all the elements of `primes_abridged`! Moreover, an expression of the above form requires that there are a certain set number of elements – the expression will fail if there are too few elements, and it will ignore any more elements.

We can instead write the following:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
primes_doubled = []

for prime in primes_abridged:
    primes_doubled.append(2 * prime)
    
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



In the above cell:

1. First, we initialized an *empty* list, and assigned to this the name, `primes_doubled`
1. Then, using the control structure of the "for loop," we considered the elements of `primes_abridged` sequentially, in each "loop" assigning one of its elements the name, `prime`
1. Finally, in each loop, we multipled the value of the element by two, and added the value of this expression to the end of the list, `primes_doubled`, using the *list method* `append`. (More on *methods* later!)

This is a fundamental pattern in the majority of programming languages; and, one which doesn't apply only to lists.

That said, there are other ways to instruct the computer to do the same – and which you may find are either **more succinct** (linguistically), **more efficient** (computationally), or both.

The most "Pythonic" way of producing `primes_doubled` involves the *list comprehension*.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
primes_doubled = [2 * prime for prime in primes_abridged]

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



In the list comprehension, we again used the keywords `for` and `in`, in order to consider the elements of `primes_abridged` sequentially, under the name `prime`. But in this case, we were able to construct `primes_doubled` with a single, clear expression of our *mapping* from one set of data to another.

Later, we'll explore other efficient methods of processing collections.



So far we've only considered lists of numbers, but in fact a list element may refer to a value of any type.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune',
]

```
</div>

</div>



In the above, we've constructed a list of the `planets`, whose elements are, of course, strings.

And, as with numbers and strings, lists also support "addition," also known as *concatenation*.

Depending on when you attended grade school, you may prefer the following planetary listing:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets + ['Pluto']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['Mercury',
 'Venus',
 'Earth',
 'Mars',
 'Jupiter',
 'Saturn',
 'Uranus',
 'Neptune',
 'Pluto']
```


</div>
</div>
</div>



But this needn't worry the International Astronomical Union! We didn't use `append()`, so the `planets` are safe.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
planets

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```


</div>
</div>
</div>



Lists can even contain other lists of data.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# distances from the sun, millions of miles:
planetary_distances = [
    ['Mercury', 36],
    ['Venus', 67.2],
    ['Earth', 93],
    ['Mars', 141.6],
    ['Jupiter', 483.6],
    ['Saturn', 886.7],
    ['Uranus', 1_784.0],
    ['Neptune', 2_794.4],
]

planetary_distances

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[['Mercury', 36],
 ['Venus', 67.2],
 ['Earth', 93],
 ['Mars', 141.6],
 ['Jupiter', 483.6],
 ['Saturn', 886.7],
 ['Uranus', 1784.0],
 ['Neptune', 2794.4]]
```


</div>
</div>
</div>



In the above collection, we've combined lists, strings, integers and floats!

This kind of structure, if constructed *arbitrarily*, can be difficult to use; but, constructed consistently, this is the basis of computational data and data science.



But lists are not the only kind of useful collection available to us in Python, and we'll explore a few!

