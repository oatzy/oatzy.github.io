---
layout: post
title: Advent of Code 2021, Day 1 in 52 Chars of AWK
date: '2021-12-02T23:40:00.000+01:00'
author: Chris Oates
tags:
- coding
- python
- awk
- advent of code
- code golf
modified_time: '2021-12-02T23:40:00.000+01:00'
---

Here is a solution to day 1 (both parts) in 52 characters of AWK

```python
{a+=($0>x);b+=($0>z);z=y;y=x;x=$0}END{print a-1,b-3}
```

Okay, this is going to take some unpacking...

# Background

This is my 4th year doing [Advent of Code](https://adventofcode.com/2021). For the last couple of years, I used rust, but this year... I dunno, maybe the novelty's worn off.

Last year, I did [a few](https://oatzy.github.io/2020/12/06/advent-of-code-2020-python-oneliners.html) of the [early puzzles](https://oatzy.github.io/2020/12/13/advent-of-code-2020-week2-oneliners.html) as Python one-liners. For this year, I wanted to see if I could do any as bash one-liners. But for day one, it ended up as just an awk one-liner, which I [code-golfed](https://en.wikipedia.org/wiki/Code_golf) down to 52 characters.

To explain this, I'm going to start by deriving a solution in python, then I'll explain how this translates into awk. I think it'll be clearer that way.

# Problem

You can see the full problem description [here](https://adventofcode.com/2021/day/1), but it boils down to counting the number of times values increase in a sequence of integers. Then in part two, it's mostly the same, except using a sliding, three-value window.

# Python

Let's start with a basic solution to part one in python

```python
count = 0
for i in range(1, len(items)):
    if items[i] > items[i-1]:
        count += 1
```

Simple enough.

In fact, we can take advantage of that fact that booleans are basically just `1` and `0`, alike so

```python
count = 0
for i in range(1, len(items)):
    count += (items[i] > items[i-1])
```

Or if we really wanted, we could compress this down to a one-liner

```python
sum((items[i] > items[i-1]) for i in range(1, len(items)))
```

But that's not what we're trying to do this year. This year we're doing awk!

Okay, now let's look at part 2 - one solution would be

```python
count = 0
for i in range(len(items)-3):
    if sum(items[i:i+3]) > sum(items[i+1:i+4]):
        count += 1
```

But actually, we can simplify this a little

Consider we have values `A B C D`

To compare the first window of 3 values to the next window, we compare: `(A + B + C) < (B + C + D)`

Notice we have `B + C` on both sides of the comparison. So we can cancel them out to give us just: `A < D`

Now, back to python

```python
count = 0
for i in range(3, len(items)):
    if items[i] > items[i-3]:
        count += 1
```

This looks a lot like our solution to part 1!

Indeed, we can combine them into a single loop

```python
part1 = part2 = 0
for i in range(len(items)):
    if i > 1:
        part1 += items[i] > items[i-1]
    if i > 3:
        part2 += items[i] > items[i-3]
```

The first `if` isn't strictly necessary, but I've included it for symmetry.

Alright, I think we're ready to switch to awk

# Awk

It turns out [awk](https://www.gnu.org/software/gawk/manual/gawk.html) is actually pretty good for Advent of Code (or the easy ones at least).

Awk is a stream processing language (like sed). You give it a file, and it loops over the lines of the file doing some processing. Considering a lot of the AoC inputs are texts files with one 'value' per line, this works quite nicely.

The drawback is, it only gives us access to the 'current' line; we don't know what the next line is until we receive it. And we only know the previous line if we store it.

Let's start small, with just part 1

```python
NR > 1 {count += ($0 > prev)}
{prev = $0}
END {print count}
```

Okay, there's a few things to explain here

1. `NR` is a builtin variable, it's effectively the current line number (starting from 1)
2. variables in awk are automatically initialised - so the first time we reference the variable `count`, it's created and set equal to `0`
3. awk splits lines into column, based on whitespace. The first column is assigned to variable `$1`, the second to `$2`, etc. and the variable `$0` represents the entire line
4. numerical columns (or indeed a whole numerical line) is automatically converted to integers
5. as with python, bools are equivalent to `1` and `0`
6. the `END` block runs only after all the input lines have been processed

In python, the above would be equivalent to

```python
# implicit variables
count = 0
prev = 0

# main loop
for NR, var0 in enumerate(items, 1):
    if NR > 1:
        count += (var0 > prev)
    prev = var0

# END
print(count)
```

Now, part 2 is similar, but a little messier, since we need to keep track of three prior lines

```python
NR > 3 {count += ($0 > prev3)}
NR > 2 {prev3 = prev2}
NR > 1 {prev2 = prev1}
{prev1 = $0}
END {print count}
```

At this point, you can perhaps see how we would combine the two solutions

```python
NR > 3 {part2 += ($0 > prev3)}
NR > 2 {prev3 = prev2}
NR > 1 {
    part1 += ($0 > prev1);
    prev2 = prev1
}
{prev1 = $0}
END {print part1, part2}
```

Easy-peasy

# Golfing

Now we can start getting rid of redundancies.

First, recall that variables are auto-initialised. So for this line

```python
NR > 2 {prev3 = prev2}
```

it doesn't matter that `prev2` isn't set for the first two iterations

```python
NR > 3 {part2 += ($0 > prev3)}
NR > 1 {part1 += ($0 > prev1)}
{
    prev3 = prev2;
    prev2 = prev1;
    prev1 = $0
}
END {print part1, part2}
```

But what if we dropped the conditionals completely?

```python
{
    part2 += ($0 > prev3);
    part1 += ($0 > prev1);
    prev3 = prev2;
    prev2 = prev1;
    prev1 = $0
}
END {print part1, part2}
```

Okay, suppose we have values `1 2 3`. For the first 4 iterations, at the point when we update `part1` and `part2`, the 'prev' variables are as follows

```python
(NR=1) prev3 = 0; prev2 = 0; prev1 = 0
(NR=2) prev3 = 0; prev2 = 0; prev1 = 1
(NR=3) prev3 = 0; prev2 = 1; prev1 = 2
(NR=4) prev3 = 1; prev2 = 2; prev1 = 3
```

Now we can be a bit cheeky, and observe that none of our puzzle input values are `0`.

So for the first iteration, `$0 > prev1` will always evaluate to `1` (true). Similarly, for the first 3 iterations, `$0 > prev3` will also always evaluate to `1` (true).

All this means is, we have to apply a 'correction' to the final results: `print part1 - 1, part2 - 3`

After that, it's just a matter of reducing all the variables to single characters, and dropping all the whitespace

```python
{a+=($0>x);b+=($0>z);z=y;y=x;x=$0}END{print a-1,b-3}
```

Voila! 52 characters.

# Bonus: Day 2

This one worked out quite nicely too - both parts in 57 characters

```python
/f/{x+=$2;y+=a*$2}/n/{a+=$2}/u/{a-=$2}END{print x*a,x*y}
```

The trick here is using a regex match - `/pattern/` - on a single character which is unique to each instruction - `f` for `forward`, `u` for `up`, and `n` for `down` (since `d o w` also appear in `forward`)

In terms of solving both parts, we note that the x distance is calculated the same in both parts, and the a(im) in part 2 is calculated the same as the y direction was in part one.

# Bonus: Day 3

I only managed the first part for this one, and it clocks in at a chunky 92 characters

```python
BEGIN{FS=""}{for(i=1;i<=NF;i++)a[NF-i]+=$i}END{for(k in a)2*a[k]>NR?g+=2^k:e+=2^k;print g*e}
```

Setting 'field separator' (`FS`) to empty allows us to treat individual characters as columns. `NF` is another of the builtin variables - in this case the number of columns (fields). We use an array to sum the bits down each column; as with variables, the array is initialised on demand.

Then, in the END block, we compare each column sum to the the number of lines - `1` is most common if it appears in more than half the lines. We use that to convert the sums array to a decimal number (gamma) and its compliment (epsilon).

Part 2 requires multiple passes over the puzzle input, so even if I came up with a solution, it would probably exceed 100 chars. I certainly couldn't combine it with the solution to part 1.

# Summary

I want to be clear that I'm no awk expert; I only dabble by way of using bash for work. Maybe someone else can golf these down even further.

If you want to actually run these awk commands, you can save them to a file, and run them like

```bash
awk -f day1.awk input.txt
```

Or directly from the cli like so

```bash
awk '{a+=($0>x);b+=($0>z);z=y;y=x;x=$0}END{print a-1,b-3}' input.txt
```

Anyway, if I come up with any good ones for later days, I'll update this post with them.

You can also find all my solutions (including python ones) in my [GitHub repo](https://github.com/oatzy/advent_of_code_2021).

Chris.

_[pretty AWK-some... am I right? guys? where are you going?]_