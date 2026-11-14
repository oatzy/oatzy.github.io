---
layout: post
title: Put the following in order
date: '2019-12-30T16:27:00Z'
author: Oatzy
tags:
- scoring
- sorting
- games
- algorithm
- over-thinking
- everyday maths
- problem solving
- puzzles
- random
- maths
modified_time: '2019-12-30T08:27:51.095-08:00'
blogger_id: tag:blogger.com,1999:blog-14769935.post-78262668589642859
blogger_orig_url: https://oatzy.blogspot.com/2019/12/put-following-in-order.html
---

YouTube channel, [College Humor](https://www.youtube.com/user/collegehumor), has a game show series called '[Um, Actually](https://www.youtube.com/watch?v=ZsZjFAfJJ3c&list=PLuKg-WhduhkkSIZioiqPV8X2WpEMWTUAu)' - a game of nerdy corrections, and general nerd trivia.

One of the 'shiny questions' involves putting things is order, for example, putting space ships or fictional creatures in order by size.

The way the scoring works (as far as I can tell) is you get one point for each item you put in the right 'position'. So if you guess (1,3,2,4), then you would get 2 points for getting 1 and 4 in the correct position.

The problem was, in the creatures game, there was this one creature which looked like a single-celled organism, but was actually the size of a galaxy (or something), making it the largest.

So suppose you get everything else in the right order, but you fell for the trap and put this surprisingly massive organism as smallest e.g. (2,3,4,1)

In that case, everything is in the wrong position, so no points. But I would argue since all but one are in the right *order* you should only lose one point.

The [FineBros](https://www.youtube.com/user/TheFineBros/) channel does a similar game - e.g. put the [top 10 most liked videos of 2019](https://www.youtube.com/watch?v=TQ-rvJosRr8) in order. Under their scoring system, you get 2 points if an entry is in the right position, and 1 point if it's off by one. So (1,3,2,4) would be worth 6 points and (2,3,4,1) would be worth 3 points

This is slightly better, but you still have a case where you can lose significant points for getting just one or two entries out of place. For example, if you had (3,4,5,6,7,1,2), then you would get 0 points, even tho 5 of 7 are in the right order.

So, can we come up with a better scoring system?

**Levenshtein Distance**

The first things that comes to mind is [Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance) or '[minimum edit](https://en.wikipedia.org/wiki/Edit_distance)' distance.

This measures the distance between two strings (words) based on the minimum number of edits to get from one to the other. In this context, an edit is a single character addition (cats -\> chats), deletion (cats -\> cat), or substitution (cats -\> bats)

Now, this doesn't seem quite relevant to our problem; we're not adding, deleting, or substituting, we're swapping. For Levenshtein, a swap would be considered a deletion + an addition (or 2 substitutions) e.g. cats -\> cas -\> cast

We could calculate the Levenshtein distance and just divide it by 2 - effectively treat delete+add (2 edits) as equivalent to a swap (1 edit). Or else, we can just take the general principle of finding the minimum number of swaps required to get from the guess solution to the correct order.

As for the actual score, we can take the number of entries in the list (N) minus the minimum number of swaps.

So for our original examples, (1,3,2,4) is worth 3, and (2,3,4,1) is also worth 3.

In the latter case, 1 wasn't 'swapped' with an actual element, but you could think of it as a swap with an implied 'null' element - (..,null,1,2,3,4,null,..) -\> (..,null,null,2,3,4,1,null,..\.)

**Dynamic Programming**

[Dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming) is an approach to solving a certain class of problem which would take a ridiculous amount of time to solve by brute force. With dynamic programming, these problems can be solved in a more reasonable amount of time by breaking them down and solving recursively.

One of the classic problem in dynamic programming is - f[ind the longest increasing sub-sequence](https://en.wikipedia.org/wiki/Longest_increasing_subsequence) in a list of numbers?

For example, in (2,3,1,7,4,9,5,8) the longest increasing sub-sequence would be (2,3,4,5,8). So in this case, we might say the score is 5/8

Going back to our other examples, (1,3,2,4) would have sub-sequence (1,2,4) or (1,3,4), worth 3 in either case. And (2,3,4,1) would be (2,3,4) which is also worth 3

**Weighted Error**

This is all well and good, but doesn't it feel like (2,3,4,1) is 'more wrong' than (1,3,2,4). Each has one element out of order, but in the former that one element if further from where it's 'supposed' to be.

One correction might be to calculate the error as sum[abs(x-x')] where x is the position of an element, and x' is where it's supposed to be. So (1,3,2,4) would be (abs(1-1) + abs(3-2) + abs(2-3) + abs(4-4)) = 2

However, this is flawed. For the (2,3,4,1) example, the error comes out at 6. Once again, we're being penalised for all the elements that are in the right order but off-by-one

So a slight modification would be to only calculate the error for those elements which are out of place - that is, find the longest sub-sequence, and then calculate the error for all elements which don't belong to that sub-sequence.

For (1,3,2,4) the error would be 1 and for (2,3,4,1) it would be 3

But how do we get from the error to the actual score?

We can start by calculating the maximum error, then subtracting the calculated error from it. So what's the maximum error?

The most wrong you can be would be to get everything in the wrong order - i.e. all elements reversed. So if we have N elements, the error would be

abs(1 - N) + abs(2 - N-1) + ..\. + abs(N -1) = (N - 1) + (N - 3) + ..\. + (N - 1) = 4 \* (N - 2)

Actually, there's a subtle flaw in this reasoning - even if all the elements are reversed, there is technically a longest sub-sequence of 1, so one of the entries shouldn't count towards the maximum error. The element we chose as the 1 correct one will affect the maximum error. If we chose the first element in the sequence, the max error is reduced by N-1, whereas if we chose one from the middle the max error is reduced by 1 or 0 (depending if there is an odd or even number of elements)

For simplicity, we'll just assume the middle entry and say max error adjustment is 0

So going back once more to our original examples, (1,3,2,4) has a score of 8 - 1 = 7, and (2,3,4,1) has a score of 8 - 3 = 5, making the latter 'more wrong' as desired.

**Conclusion**

I'm not sure if there was a point to all this. I don't think this is useful outside of scoring this particular kind of game.

It might be interesting to run an neural net or [genetic algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm) or similar using this as the [score function](https://en.wikipedia.org/wiki/Fitness_function). I'd be interested to see how a neural net performed at sorting, in terms of performance and correctness.

But anyway,

Chris.
