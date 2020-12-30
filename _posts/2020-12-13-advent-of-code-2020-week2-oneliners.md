---
layout: post
title: Advent of Code 2020 (Week 2+) - Python One-Liners
date: '2020-12-13T18:40:00.000-00:00'
author: Chris Oates
tags:
- coding
- python
- advent of code
modified_time: '2020-12-13T18:40:00.000-00:00'
---

As expected, as the puzzles get harder, it's not so easy to solve them with one-liners. So unlike week 1, I don't have one-liners for every day.

If you haven't read it already, you can find week 1 [here](https://oatzy.github.io/2020/12/06/advent-of-code-2020-python-oneliners.html).
I may refer back to things discussed in that post.

# Day 10

By this point, you've seen all these tricks before

```python
print((lambda x: x[1] * x[3])(reduce(lambda a, x: (x, a[1] + (x - a[0] == 1), a[2] + (x - a[0] == 2), a[3] + (x - a[0] == 3)), sorted(map(int, open('day10.txt'))), (0, 0, 0, 1))))
```

In the main section, we're using a `reduce` to count the number of differences of size 1, 2, 3. The first value of the tuple is the previous value in the list. We can do this, because we start at the 'outlet' (0), which isn't included in the puzzle input. Similarly, our input doesn't include the 'device', which is 3 greater than the largest value in the input. This means we can just start our 3 count at 1.

We also have another instance of boolean arithmetic - `int + bool` == `x + (1 if True else 0)`

Finally, we pass that to a function which multiplies the 1 and 3 counts - the puzzle output.

# Day 13

The input for this puzzle is two lines - the first is a single integer, the second is a comma-separated list of integers and placeholders (`x`).

```python
print((lambda t, ids: min(((i - int(t) % i, i*(i - int(t) % i)) for i in (int(i) for i in ids.split(',') if i != 'x')), key=lambda x: x[0]))(*open('day13.txt'))[1])
```

In the inner loop we're parsing lines two (the list of integers). Then we're iterating over tuples, where the first value is what we're trying to minimise, and the second is our puzzle output.

The only really new thing here is that we're using the 'splat' (unpacking) operator `*` to pass the input lines a separate valiables. This saves us a few characters, and makes things a bit more readable (to the extent any of this can be considered readable ;) )

Also, a handy thing to know - the `int` function will ignore leading and trailing whitespace, i.e. `int("1\n") == 1`


# Game Over

I couldn't think up any one-liners for the remaining puzzles. Thanks for reading...


Chris.


