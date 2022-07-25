---
layout: post
title: Quicksort in One Line of Python
date: '2020-01-05T00:00:00.000-00:00'
author: Chris Oates
tags:
- python
- algorithm
modified_time: '2019-01-05T00:00:00.000-00:00'
---

```python
qs = lambda l: l and qs([x for x in l[:1] if x <= l[0]]) + [l[0]] + qs([x for x in l[:1] if x > l[0]])
```

# Quick Sort

This is based off an implementation I saw in haskell, it went something like

```haskell
qsort :: (Ord a) => [a] -> [a]
qsort [] = []
qsort (x:xs) =
    qsort [a | a <- xs, a <= x] ++
    [x] ++
    qsort [a | a <- xs, a > x]
```

Before I explain what's going on, it might help to expand it out a bit

```python
def quicksort(lst):
    if len(lst) == 0:
        return []

    pivot = lst[0]
    rest = lst[1:]

    lower = [x for x in rest if x <= pivot]
    upper = [x for x in rest if x > pivot]

    return quicksort(lower) + [pivot] + quicksort(upper)
```

The basic idea is, first we pick a 'pivot'. Here we've used the first entry in the list for simplicity. In a proper [quicksort](https://en.wikipedia.org/wiki/Quicksort) you would make a more ['nuanced'](https://en.wikipedia.org/wiki/Quicksort#Choice_of_pivot) choice.

Then we split the remaining entries into two lists - those values that are less than (or equal to) the pivot, and those which are greater than the pivot. We then repeat the process recursively for those two lists, and finally concatenate the results.

Think of it like this - after the first iteration, all the entries in the first half of the list are less than all the entries in the right half of the list.

```
[5, 2, 1, 8, 6, 3, 4, 7, 9] -> [2, 1, 3, 4] + [5] + [8, 6, 7, 9]
```

If we repeat the process on the first half of the list, now all the entries in the first quarter of the list are less than all the entries in the second quarter, are less than all the entries in the 3rd and 4th quarters.

```
[2, 1, 3, 4] -> [1] + [2] + [3, 4]

=> [1] + [2] + [3, 4] + [5] + [8, 6, 7, 9]
```

If we keep repeating this process, eventually we reach a point where the first single entry is less than the second entry, is less than the third entry, ... In other words, the entries have been sorted.

I should say that this isn't an especially efficient implementation of quicksort. As mentioned, we're making a naive choice of pivot. Besides that, a proper quicksort sorts the list 'in place' - that is, by moving around values in the input list. This implementation, instead, creates a load of new lists at each level of recursion.

But efficient or not, this is a single line of code which can sort a list, and that's pretty cool. And aside from that, it makes use of some interesting feature of python. So, let's step through it.


# Recursion and Late Binding

The first thing to note is that we're defining a variable (`qs`) which refers to itself. If you're familiar with recursion, this won't seem so weird.

In python, a function can happily refer to a variable that isn't defined, and it won't complain until you try to call the function

```python
>>> def hello():
...     print(f"hello {name}")
...
>>> hello()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in hello
NameError: name 'name' is not defined
```

This is called ['late binding'](https://en.wikipedia.org/wiki/Late_binding). It can be a source of errors, but a linter will usually catch it.

What's interesting is you can define the missing variable after the fact

```python
>>>
>>> name = "world"
>>> hello()
hello world
```

Basically, when you call the function, if first looks for `name` in the function's local [scope](https://www.geeksforgeeks.org/global-local-variables-python/), and if it isn't found there, it looks in the global scope (or any outer scopes if the function is inside another function).

So going back to recursion, we can call `qs` from inside `qs` because when we come to call it, the `qs` variable (function) exists in the global scope.


# Lambda

[Lambdas](https://realpython.com/python-lambda/), also known as 'anonymous functions' are an alternative way of declaring a function.

```python
double = lambda x: 2 * x

# is equivalent to
def double(x):
    return 2 * x
```

Unlike regular functions, lambdas can only contain a single 'expression' - a statement which returns a value. This means they can't include multiple statements, assignments. In python 2, they can't even call `print`.

Most linters will tell you to replace lambda assignments with normal function definitions, which is reasonable. It's clearer for one, especially if the person reading it doesn't know about lambdas.

We could just as easily have written a normal function definition for quicksort on a single line

```python
def qs(l): l and ...
```

Tho, that doesn't 'feel' quite right. And linters would probably tell you to insert a line break anyway.

Really, lambdas should only be [used](https://www.scaler.com/topics/python/lambda-and-anonymous-function-in-python/) for defining a function that you're directly passing to another function e.g.

```python
sorted(lst, key=lambda x: x.lower())
```

This saves having to define a separate function like

```python
def lower(s):
    return s.lower()

sorted(lst, key=lower)
```

tho, in this particular case, you could even do

```python
sorted(lst, key=str.lower)
```


# Lazy Booleans and Truthiness

This is maybe the weirdest part. First of all, lets talk about the boolean operators `and` and `or`

If you have a logical statement like `a and b or c`, python will only evaluate terms up until it can say for sure what the result will be - the statement is 'lazy' or ['short circuit'](https://en.wikipedia.org/wiki/Short-circuit_evaluation) evaluated

Take `a and b` - if `a` is True then we don't know what the result is until we check `b`. However, if `a` is False, then the result will be False regardless of what `b` is, so we don't need to check it.

This feature is useful if, instead of variables, you have functions, and especially if those functions are slow or memory heavy.

```python
def a():
    print("checked a")
    return False

def b():
    print("checked b")
    return True

>>> a() and b()
checked a
False

>>> b() and a()
checked b
checked a
False
```

Similarly, for `a or b`, if `a` is True, then the result is always True, so we don't need to check `b`, and if `a` is False then we do need to check `b`

```python
>>> a() or b()
checked a
checked b
True

>>> b() or a()
checked b
True
```

Now, lets talk about 'truthiness'. In python, values can be evaluated as booleans - for example

```python
>>> x = 5

>>> if x:
...     print(f"{x} is truthy")
5 is truthy
```

Values are said to be either 'truthy' or 'falsey'

For numbers (integers, floats) 0 is falsey, and all non-zero values are truthy (including negative values). Similarly, for collections like lists, strings, and dicts, an empty container is falsey. If the collection has any members (if it's non-empty) it is truthy. `None` is always falsey.

(If you're creating your own class, you can define its truthiness with the `__nonzero__` [magic method](https://rszalski.github.io/magicmethods/#representations)).

In the expanded version of quicksort above, I did `if len(lst) == 0`. This was mostly so it was clear what was being checked. The 'idiomatic' way of doing this check (which some linters will suggest) is `if not lst`. If the list is empty, then `not lst` will by True, otherwise it will be False.


Going back to the boolean operators, what is the result of the following?

```python
>>> a = 5
>>> b = 7
>>>
>>> result = a or b
```

Our intuition might be that, since `and` is a boolean operation, the result will be a boolean

```python
>>> print(result)
5
```

What happened? Well `a = 5` is truthy. And we know from before that if `a` is True then we don't evaluate `b` - we just return `a`

What about this

```python
>>> result = a and b
```

This time we have to evaluate `b` also. Since `a` is truthy, its exact value doesn't actually matter, so we just return `b = 7`

```python
>>> print(result)
7
```

Which finally brings us back to the one line quicksort - `l and qs(...`

Here, `l` is a list. If it's empty then it is falsey, so we don't have to evaluate whatever is on the other side of `and`, we just return it as is (we return the empty list). If the list isn't empty then its truthy, so we evaluate and return whatever is on the other side of `and`, which in this case is a sorted copy of the input list.


I wouldn't advise doing this in practice. Even if you know all of the above, the statement isn't very intuitive. Tho I do sometimes use the `or` version for assigning a default to a possibly None value - `value = value or default` - I think that's fine, so long as you're sure value won't have a valid falsey value (like 0).

# List Comprehension

Next we have so called [list comprehension](https://realpython.com/list-comprehension-python/). List comprehension is a way of constructing a list from another iterable (list, string), e.g.

```python
numbers = [1, 2, 3, 4]

doubles = [n * 2 for n in numbers]
```

This is somewhat nicer, and more compact than, say

```python
doubles = []
for n in numbers:
    doubles.append(n * 2)
```

Another way of looking at it is as an alternative to `map` and `filter`

```python
map(lambda n: n * 2, numbers) == [n * 2 for n in numbers]

filter(lambda n: n % 2 == 0, numbers) == [n for n in numbers if n % 2 == 0]

map(lambda n: n * 2, filter(lambda n: n % 2 == 0, numbers)) == [n * 2 for n in numbers if n % 2 == 0]

```

`map`/`filter` are quite common in more functional languages, but list comprehensions are more idiomatic in python (again, the linter will suggest changing it). I think it's fair to say the list comprehensions are easier to read in the above.

You can also use 'comprehensions' to build dicts and sets. You can even do nested loops in comprehensions (but probably shouldn't)


# Slices

On to [slices](https://stackoverflow.com/a/509295). Slices are essentially a subset of a collection (list, string).

The syntax is `list[start:end:step]`. If any of the parameters are missing, the defaults are `list[0:len(list):1]`.

In our quicksort, we have `l[1:]` - which is taking a slice from index 1 (inclusive) to the end of the list. In other words, we're taking everything except the first (index 0) element, since we're dealing with that first element - our pivot - separately.

In the expanded version, as of python 3 we could get rid of the slices by changing

```python
# python 2
pivot = lst[0]
rest = lst[1:]

# python 3
pivot, *rest = lst
```


# Concatenation

Finally, concatenation. Python has overloaded the `+` symbol to support lists. In this case, it concatenates the lists

```python
>>> [1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
```

An alternative method for combining lists is `extend`

```python
>>> l = [1, 2, 3]
>>> l.extend([4, 5, 6])
>>> print(l)
[1, 2, 3, 4, 5, 6]
```
But this wouldn't have worked for our purposes, since we can't do assignments in lambdas and `extend` returns `None`

# Conclusion

So yeah, there's a surprising amount going on in that 1 line, ~100 characters.

For those into [code golf](https://en.wikipedia.org/wiki/Code_golf), if we know in advance that there won't be any duplicate entries in the input list, then we can make it even shorter

```python
def s(l):l and s([x for x in l if x<l[0]])+[l[0]]+s([x for x in l if x>l[0]])
```

That's 77 characters. I can't think how it might be made shorted than that...

Of course, there is one way to sort a list with even fewer character than that

```python
l.sort()
```


Chris.
