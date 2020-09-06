---
layout: post
title: The First Program I Ever Wrote
date: '2020-09-05T10:54:00.000-00:00'
author: Chris Oates
tags:
- biographical
- coding
- maths
- python
modified_time: '2020-09-06T00:03:00.000-00:00'
---
When people ask how I got into programming, I usually tell them "mostly for maths stuff". And they look at me, kind of confused. I think people forget (or don't know) that my degree was in Theoretical Physics. Originally, I was a maths nerd, and programming was just a tool for making doing maths easier.

# Pythagoras

Back in secondary school (high school), we'd just been taught about Pythagoras's theorem

$a^2 + b^2 = c^2$

And we were doing exercises, which was pretty dull - once you get the concept, the exercises are just putting numbers in to the equation.

But an interesting thing was that a lot of the exercises used 'pythagorean triplet' - sets of three integers which fit the equations. I guess the textbooks use them because the numbers work out nicely, no rounding and all that.

- $3^2 + 4^2 = 5^2$
- $5^2 + 7^2 = 12^2$

After doing a few of these exercises, I noticed a pattern in some of the triplets - that the two largest values were one different from each other - 4 and 5, 12 and 13

With a little algebra, you can work out

$$x^2 + y^2 = (y + 1)^2 \\
x^2 = y^2 + 2y + 1 - y^2 \\
y = \frac{(x^2 - 1)}{2}$$

So for example if x = 3, y = (3^2 - 1) / 2 = 4; y + 1 = 5

You'll notice that because of that divide-by-two, this only works if x is odd. But it works for all odd numbers

- 3, 4, 5
- 5, 12, 13
- 7, 24, 25
- 111, 6160, 6161

# The Calculator

To test my theory, I was working through all the odd numbers, putting numbers into my calculator, seeing if my equations worked. After a handful, I was thinking - there's got to be an easier way of generating these triplets.

And it just so happened that my calculator was a graphing calculation (Casio fx-9750 PLUS)

Now I've never been one for reading the whole instructions start to end. I'm pretty lazy, I just skim until I find the bits that are relevant to what I'm trying to do.

(And to be fair, the instruction book for that calculator was pretty chunky)

Which brings us to **the first program I ever wrote**

```
?->N:(N^2-1)/2
Ans+1
```

On the first line `?->N` asks for input and assigns it to variable `N`

It then calculates `(N^2 - 1) / 2` and outputs it to screen

Then when you press `EXE` (enter) again, it calculates `Ans+1` - the previous result + 1 - and outputs that to screen

In python this would be roughly

```python
while True:
	N = int(input("?"))
	Ans = (N**2 - 1)/2
	print(Ans)
	input()
	print(Ans+1)
```

So now I could generate all the triplets I wanted!

# Branching Out

I later decided I wanted a version of this program that would run on my Windows 98 PC. I didn't know anything about programming languages, so I initially went with one that happened to be on a CD ROM stuck to the front of a computer magazine. The language was a variation on BASIC.

Then I later did a google search for something like "best programming language", which lead me to python. I read the 'getting started' thing on the python website, and the rest is history...


Chris.

[I need to figure how to make Jekyll do LaTeX]