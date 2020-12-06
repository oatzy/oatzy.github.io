---
layout: post
title: Advent of Code 2020 (Week 1) - Python One-Liners
date: '2020-12-06T15:39:00.000-00:00'
author: Chris Oates
tags:
- coding
- python
- advent of code
modified_time: '2020-12-06T19:03:00.000-00:00'
---
This is my third year doing [Advent of Code](https://adventofcode.com/2020). As with last year, I'm primarily solving the puzzles with rust. But in this first week, there were a couple of puzzle where I could think of python one-liner solutions. And then I wanted to try and come up with one-liners for the other days.

This lead to me using some dirty tricks, which I want to share with you, dear reader.

You can see all my solutions on [my github](https://github.com/oatzy/advent_of_code_2020), including both the rust code and the python one-liners.

For brevity, I won't go over the problem descriptions (except where pertinent) - you can read them on the official website (linked above)

Also, these aren't trying to be the shortest solutions possible, tho they could form the basis of such.

# Day 1

We want to find two numbers in a list which add to 2020. The obvious way to do this is with a nested loop

```python
for x in input:
    for y in input:
        if x + y == 2020:
            return x * y
```

But we can actually do this as a single loop - if we keep track of the values we've already seen, we can just check if we've already seen `2020 - x`

```python
seen = set()

for x in input:
    if (2020 - x) in seen:
        return x * (2020 - x)
    else:
        seen.add(x)
```

Now, the `seen.add` call returns `None`, so if we do this as a list comprehension, we'll get a load of `None`s, and our solution somewhere in the middle. So if we filter out the `None`s, we can easily grab the solution.

The first version I did looked like this

```python
seen=set();print(next(i for i in (x * (2020 - x) if (2020 - x) in seen else seen.add(x) for x in map(int, open("day01.txt"))) if i is not None))
```

with a cheeky semi-colon to make two lines look like 1.

The tricky bit here is that we need to initialise a set, and then update it in the loop. Eventually, I came up with a way of doing this as a legit one-liner

```python
print((lambda seen: next(i for i in (x * (2020 - x) if (2020 - x) in seen else seen.add(x) for x in map(int, open("day01.txt"))) if i is not None))(set()))
```

basically we move the main logic into a (lambda) function, and immediately call it with a newly initialised set

```python
(lambda seen: ...)(set())
```

Part 2 is a triple-nested loop in the naive solution, and the `set` trick doesn't work in that case. It should be possible to do the triple-nested loop as a list comprehension, but you would need to read the input 3 times; or do the lambda trick, reading the file once, and passing it as a param to the lambda-wrapped comprehension.

# Day 2

This is another technically two-liner, but I think we can make allowances for imports.

```python
import re; print(sum(int(l) <= s.count(c) <= int(h) for (l, h, c, s) in (re.match(r"(\d+)\-(\d+) (\w): (\w+)", line).groups() for line in open("day02.txt"))))
```

Here we have a nested iterator - the inner reads the file and performs the regex parsing, the outer takes the regex output so we can use it to solve the actual problem.

In this case, parts 1 and 2 are pretty similar, and we can solve both in almost the same way.

```python
import re; print(sum((s[int(l)-1] == c) ^ (s[int(h)-1] == c) for (l, h, c, s) in (re.match(r"(\d+)\-(\d+) (\w): (\w+)", line).groups() for line in open("day02.txt"))))
```

(-1 because the numbers are 1-indexed)

A couple of things of note:

- in part 1, we use a chained range check `a <= x <= b`
- in part 2 we use the `^` (XOR) operator for the "one or other but not both" check

# Day 3

This is by far the most horrible... but I'm also pretty pleased with myself for coming up with it.

So we have a square map with some 'trees'. We want to move from the top to the bottom of the map, moving 1 space down and 3 spaces right with each step, and count how many trees we encounter. And we're told that the map repeats horizontally, so if we go off the edge of the map we need to wrap around (modulo)

So we have something like

```python
for y in range(height):
    x = 3 * y % width
    if map[x][y] == '#':
        total += 1
```

In the above, we're assuming that we've parsed the map into a nested array. (In rust I used a `HashSet` of tree positions, but the logic is more or less the same).

The problem is, we can't parse our map and then iterator over it in a one-liner. (Or maybe we can with the lambda trick)/

So suppose we don't parse the map, and just iterate of the string representation instead. At each step, the offset in the string moves to `y * (width+1) + (3 * y % 3)` - we've done `y * (width+1)` to account for the newline characters at the end of each row.

Or, turning it the other way, if we iterate over the input string, we know if we've hit one of our steps if the offset equals the above

```python
for i, c in enumerate(input):
    if i == y * (width+1) + (3 * y % 3) and c == '#':
        total += 1
```

But what's `y`? And how do we know the width of the map without iterating over it (and storing it as a variable)?

This reminded me of an [article](https://chrispenner.ca/posts/wc) I read about implementing a faster `wc` in haskell - `wc` being the unix 'word count' tool. The long and short of it is scanning over characters, incrementing the line count when we hit a newline character (`\n`).

In other words

```python
y = 0
width = None
for i, c in enumerate(input):
    if c == '\n':
        y += 1

        if width is None:
            width = i
```

We increment the current line (`y`) when we encounter a newline character. And when we encounter our **first** newline character, we set the `width` (otherwise the width would increase at every linebreak)

This does leave us with an unknown width until we hit the first newline, but for this problem, we don't need to know the width while we're on the first line since the only position we hit on the first line is `(0,0)`/`i == 0`

```python
if i == 0 # first line
    or (width is not None and i == y * (width+1) + (3 * y % 3)) ...
```

The final piece is how we update all three of our variables (`y`, `width`, and `total`) in a single loop. For this we use `reduce` - starting with `(0,0,0)` and updating on each iteration as appropriate. And at the end, we pick out our total from the triple `[2]`

```python
print(reduce(lambda (y, w, t), (i, c): (y+1 if c == '\n' else y, i if c == '\n' and not w else w, t+1 if c == '#' and (i == 0 or w != 0 and i == y*(w+1)+(3*y % w)) else t), enumerate(open("day03.txt").read()), (0, 0, 0))[2])
```

Note: this version only works with python 2 - python 3 doesn't allow tuple unpacking in function parameters. Instead, we have to do `lambda x, y: (x[0]+1 ...`, which is a little more verbose and harder to read (and this is already pretty hard to read). Also in python 3, we have to do `from functools import reduce`. You can see the python 3 version on my github

Part 2 you can do similar logic for each different 'path', then probably a `reduce` to get the product of all the paths.

# Day 4

This was the first one for which I thought of a one-liner. As you can see, it is by far the most straight-forward of these solutions.

```python
print(sum(all(f in s for f in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")) for s in open("day04.txt").read().split("\n\n")))
```

The problem is to find all entries (passports) which have all the required fields. But because the field name strings don't appear in any of the value strings, we can get away with doing a string membership test - no parsing required!

Another thing of note here is `sum(all(...) ...)`

Here we're taking advantage of the fact that is python, booleans are a subclass of integers - specifically `True == 1` and `False == 0`. This means we can do arithmetic like `True + True == 2`, or in our case, sum to count the number of `True` values.

A more explicit way of doing it might be `1 if True else 0` or by filtering - `sum(1 for s in ... if all(...))` - but both those are more characters ;)

Part 2 involves too many steps to do in a one-liner, I think.

# Day 5

The trick to day 5 is noticing that the boarding pass representation is just a roundabout way of doing binary numbers - just with `B` and `R` in place of 1s and `F` and `L` in place of 0s

If we have a binary string where the the digits are left-to-right smallest-to-largest, then we can convert to decimal as

```python
value = 0
for i, c in enumerate(string):
    if c == '1':
        value += 1 << i
```

where `1 << i` is a bit-shift, equivalent to `2 ** i` (2 to the power of `i`)

Since out puzzle input is largest-to-smallest order, we have to reverse it first.

```python
print(max(sum((1 << i) if c in 'BR' else 0 for i, c in enumerate(reversed(l.strip()))) for l in open("day05.txt")))
```

Not included here, but I think you could do part 2 in a similar way to day 1, looking for `x-1` where `x-1` is missing but `x` and `x-2` are present.

# Day 6

This was another one where both parts were more or less the same.

In part one, we use a `set` to find the number of unique characters. BUT, because the members in each group are newline separated, we need to make sure to exclude those, or our counts will be off-by-one.

```python
print(sum(len(set(group.replace('\n', ''))) for group in open('day06.txt').read().split('\n\n')))
```

The logic in part two is a little more laboured, but essentially, count how many of the first member's characters are in all the other members' characters.

```python
ref = group[0]
in_all = 0
for c in ref:
    if all(c in g for g in groups):
    in_all += 1
```

We also use the sum-over-bool from day 4, and the inner loop from day 2 to pre-split the groups into members

```python
print(sum(sum(all(c in m for m in members) for c in members[0]) for members in (group.split() for group in open('day06.txt').read().split('\n\n'))))
```

# To Be Continued..?

I may or my not do more of these one-liners/blogs, depend how hard they get. You can alway check my github for any new ones.


Chris.


[...with apologies to Guido Van Rossum]
