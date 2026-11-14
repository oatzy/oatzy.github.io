---
layout: post
title: Gift Wrapping
date: '2011-12-29T01:08:00Z'
author: Oatzy
tags:
- OCD
- christmas
- arts and crafts
- optimisation
- algorithm
- over-thinking
- everyday maths
- problem solving
- maths
modified_time: '2012-12-03T13:15:38.408-08:00'
thumbnail: /images/gift-wrapping/sort-wrap.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-8009654822357324024
blogger_orig_url: https://oatzy.blogspot.com/2011/12/gift-wrapping.html
---

In these times of austerity, one has to be economical with one's wrapping paper.

Yeah, I know, this would have been much more useful about a week ago. But I just never got around to it. And I use the word 'useful' loosely; any saving one might get from these 'techniques' will most likely be insignificant.

Nonetheless..\.

**Rectangles**

All gifts - no matter shape or size - can be wrapped with a rectangular piece of paper.

This is easily proved. However doing so may not be the neatest or most efficient approach. For example, it's easy to efficiently wrap a cuboid (book, DVD, box) with a rectangular piece of paper, it's less easy to wrap a bike (efficiently) with a single, and in this case, very large piece. However, in the case of a bike, one could use several, smaller pieces of paper for more efficient wrapping.

For a ball, one might be tempted to say that a more unusual shape - maybe a [truncated icosahedral](http://en.wikipedia.org/wiki/Truncated_icosahedron) shell - would be more efficient. However, cutting out such a shape would result in lots of little slivers of waste, and would take a lot of time and effort. Instead, it's usually easier, and not greatly inefficient to just use a rectangular piece, and some creative folding and scrunching.

So here's the point - for a given gift, we can define a rectangle (or set of rectangles) which most efficiently wraps that gift.

For a cuboid of sides L(ength), W(idth), H(eight), the minimum paper would be: *(H+L)* by *2(H+W)*, with a bit extra for overlap.

For a cylinder of dimensions H(eight) and R(adius), the paper would need to be: *2PI\*R* by *(H+2R)*, and a bit.

[*Proof that these cuts are optimal is left as an exercise for the reader.*]

For other shapes, this may be more tricky to determine, but for the sake of arguing, we will assume we know all the required rectangle's dimensions.

**Bin Packing**

So for a given collection of gifts to be wrapped, we have defined a set of rectangles. We now have to determine the most efficient way to cut these out from rolls of wrapping paper - i.e. a large rectangle, ~ 1m x 4m.

This is similar to solving a two-dimensional version of the [Bin Packing problem](http://en.wikipedia.org/wiki/Bin_packing_problem).

In the Bin Packing problem, we have several bins (cuboids) of fixed dimensions, and a collection of smaller cuboidal objects. The problem is to pack the objects into as few bins a possible - i.e. find an efficient way of fitting cuboids into boxes.

The problem is [NP-Hard](http://en.wikipedia.org/wiki/NP-hard), meaning that finding the optimal solution can take a very long time. However, there are algorithms which are fast and give [adequately optimal](http://en.wikipedia.org/wiki/Approximation_algorithm) solutions.

One, in particular, is called the First Fit algorithm, and it works something like this:

1\) Sort the rectangles into size order\
2\) Cut out the largest pieces still in the set\
2 i) If there is not enough paper left on the current roll, move on to the next/start a new roll\
3\) Repeat (in descending size order) until there are no more pieces left to cut.

There are also instructions for how to place the rectangles, for example first fit from bottom and right, to left and top.

[![](/images/gift-wrapping/sort-wrap.png)](/images/gift-wrapping/sort-wrap.png)

This [article](http://www.codeproject.com/KB/web-image/rectanglepacker.aspx) gives a more precise description of a similar algorithm, though that one is defined for a 'roll' of non-restricted dimensions.

**Realistically**

That's all well and good mathematically. But in the real world, it's likely more trouble to solve the problem than the saving in paper is worth.

However, the general principle of the algorithm can be loosely applied (if indeed it isn't the approach you already use) to improve on efficiency.

In general, you can easily sight-guess which gift in going to require the largest amount of paper. And from that you can apply the First Fit algorithm.

One change I make is, cut out and wrap the largest one left, first. Then wrap the gift(s) which best fits the off-cut.

[![](/images/gift-wrapping/offcut-diagram.png)](/images/gift-wrapping/offcut-diagram.png)

This is particularly good for rolls, where you want to unroll and use it a 'slice' at a time (rather than unrolling the whole thing).

Anyway, something to think about next time you happen to be wrapping a large number of gifts.

Even better if you can get some of that Tesco wrapping paper with the grid on the back.

Oatzy.

[No wasted paper from my wrapping this year. Just saying.]
