---
redirect_from:
  - "/03/1/expressions"
interact_link: content/03/1/Expressions.ipynb
kernel_name: python3
has_widgets: false
title: 'Expressions'
prev_page:
  url: /03/programming-in-python.html
  title: 'Programming in Python'
next_page:
  url: /03/2/Names.html
  title: 'Names'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# 3.1 Expressions

Programming languages are simpler than human languages. Nonetheless, there are rules of grammar to learn in any language. In this text, we will use the <a href="https://www.python.org/" target="_blank" rel="noopener">Python</a> programming language. It's essential to learn its grammatical rules &ndash; the same rules governing the most basic programs are also central to the most sophisticated.

Computer programs are fundamentally constituted by *expressions*, which instruct the computer how to manipulate pieces of data.

For example, a multiplication expression consists of a `*` symbol written between two numerical expressions. The expression `3 * 4` may be *evaluated* by the computer, via Python. The value of the expression &ndash; the result of its evaluation &ndash; is `12`.

In fact, the page you're reading was generated from a <a href="https://jupyter.org/" target="_blank" rel="noopener">Jupyter Notebook</a>. Notebooks record programming expressions input into "cells" – such as the one below – _and_ evaluate these and record their results.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
3 * 4

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
12
```


</div>
</div>
</div>



Note that the grammar rules of a programming language are rigid. In Python, the `*` symbol cannot appear twice in a row. The computer will not try to interpret an expression that differs from its prescribed expression structures. Instead, it will show a `SyntaxError` error. The *syntax* of a language is its set of grammar rules, and a `SyntaxError` indicates that the structure of an expression doesn't match any of the rules of the language.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
3 * * 4

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

      File "<ipython-input-2-012ea60b41dd>", line 1
        3 * * 4
            ^
    SyntaxError: invalid syntax



```
</div>
</div>
</div>



Small changes to an expression can change its meaning entirely. Below, the space between the `*`s has been removed. Because `**` appears between two numerical expressions, the expression is a well-formed *exponentiation* expression (the first number raised to the power of the second: 3 times 3 times 3 times 3). The symbols `*` and `**` are called *operators*, and the values they combine are called *operands*.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
3 ** 4

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
81
```


</div>
</div>
</div>



**Common Operators.** Data science often involves combining numerical values, and the set of operators in a programming language are designed to so that expressions can be used to express any sort of arithmetic. In Python, the following operators are essential.

| Expression Type | Operator | Example    | Value     |
|-----------------|----------|------------|-----------|
| Addition        | `+`      | `2 + 3`    | `5`       |
| Subtraction     | `-`      | `2 - 3`    | `-1`      |
| Multiplication  | `*`      | `2 * 3`    | `6`       |
| Division        | `/`      | `7 / 3`    | `2.66667` |
| Remainder       | `%`      | `7 % 3`    | `1`       |
| Exponentiation  | `**`     | `2 ** 0.5` | `1.41421` |



Python expressions obey the same familiar rules of *precedence* as in algebra: multiplication and division occur before addition and subtraction. Parentheses can be used to group together smaller expressions within a larger expression.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
1 + 2 * 3 * 4 * 5 / 6 ** 3 + 7 + 8 - 9 + 10

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
17.555555555555557
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
1 + 2 * (3 * 4 * 5 / 6) ** 3 + 7 + 8 - 9 + 10

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
2017.0
```


</div>
</div>
</div>



This chapter introduces many types of expressions. Learning to program involves trying out everything you learn in combination, investigating the behavior of the computer. What happens if you divide by zero? What happens if you divide twice in a row? You don't always need to ask an expert (or the Internet); many of these details can be discovered by trying them out yourself. 



**Did you know?** You can interact with the Jupyter Notebook for this page, and try out Python! See the [top of the page](#3.1-Expressions) for enabled buttons, such as **Download** and **Interact**.

