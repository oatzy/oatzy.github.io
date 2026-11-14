---
layout: post
title: The Exact Change Problem
date: '2010-09-08T18:52:00Z'
author: Oatzy
tags:
- money
- buses
- nerd
- everyday maths
- problem solving
- reblog
- public transport
- maths
modified_time: '2010-09-08T12:03:59.489-07:00'
blogger_id: tag:blogger.com,1999:blog-14769935.post-1292374110590965044
blogger_orig_url: https://oatzy.blogspot.com/2010/09/exact-change-problem.html
---

[*Reblog: Originally titled '[Pimp My Change](http://blogs.myspace.com/index.cfm?fuseaction=blog.viewcustom&friendId=130305886&blogId=437352124&swapped=true)'*]

There's an old problem in discrete mathematics, known as the [Subset Sum Problem](http://en.wikipedia.org/wiki/Subset_sum_problem) which goes as follows:

> Given a set of integers, does the sum of some non-empty subset equal exactly zero? For example, given the set { −7, −3, −2, 5, 8}, the answer is YES because the subset { −3, −2, 5} sums to zero. [[wiki](http://en.wikipedia.org/wiki/Subset_sum_problem)]

Or in another context, imagine you're at a restaurant and for some [unknown](http://xkcd.com/287/) and perverse reason, you want the total cost of your meal to add up to, say, £10. The problem is to pick items from the menu so as to satisfy this condition.

In terms of computer science, this problem is [NP-Complete](http://en.wikipedia.org/wiki/NP-Complete); that is as the problem gets bigger the time taken to find a solution increases non-polynomially (e.g. exponentially).

In other words, if you wanna solve it (even with a computer) you've gotta be willing to wait several thousand years for an answer.

So lets now make the problem slightly different:

> Given a certain monetary note [£5/10/20], find a subset of items in a shop such that the change given contains, in exact change, £1.30.

But, there does hide in this seemingly equivalent problem a few interesting caveats:

1\) The change given needn't be exactly £1.30

2\) If the change isn't exactly £1.30, you have to account for the fact change will usually be given in the smallest number of coins - e.g. £2 is more likely to be given as a £2 coin rather than two £1 coins (or any other arrangement).

3\) By taking into account change you already have, the problem is slightly altered. But the solution is found in essentially the same way.

So why is any of this important?

While I'm waiting for my awesome new all access special pass to be delivered I have to pay for the bus, meaning £1.30 both ways on a bus that accepts exact change only.

Of course by making certain assumptions, as those above, it's fairly easy to work out, given a starting amount (*a*), how much you need to spend (*s*) to get £1.30 exactly. The hard part is finding items such that (*a - s) = £1.30*.

This is the essence of the Subset Sum Problem.

But in this instance, there is that loophole that the change needn't be exactly £1.30 - it just has to contain that amount.

So, for example, lets say we start with a £5 note. And lets say, since change will likely be given in the smallest number of coins, our change needs to contain at least one of each of 10p, 20p and £1 coins.

To get 10p & 20p - we need to buy something with a pence value in 11-20p or 61-70p

To get £1 - given the 30p will be taken from one of the five pounds, we have £4 to play with. So we need to buy something with a pound value of £1/3

For other values of *c* and *a*, the solutions to the above are relatively similar.

So from the above - if we start with £5 - we have a range of 40 *(=(10+10) x 2)* possible sums to add up to, cutting the problem down to a more manageable size.

So we don't have an exact solution, but a simplification to the problem instead. And in most cases that's good enough.

But one other thing I should perhaps mention, is that the change needn't all be collected in one transaction - i.e. it can be collected in smaller parts, such as 5p s or 50p s, etc.

Of course, I could just give the smallest amount I have exceeding £1.30. But that would mean giving away money unnecessarily. Or, you know, I could ask a cashier kindly to change the money for me..\. I dunno.

[*[Follow Up](http://blogs.myspace.com/index.cfm?fuseaction=blog.viewcustom&friendId=130305886&blogId=437507122&swapped=true)*]

Firstly, if you're on campus, a quick and dirty solution to the change problem is to go to *CostCutter* and buy a *Ginsters* Tortilla Wrap [your choice of filling] at a cost of £3.19. A total rip-off, I know.

But the change will be £1.81, most likely given as £1, 50p, 20p, 10p and 1p. And this price lays within the range outlined in the previous blog. Simple.

Another thing to note, whilst playing this 'game', is that you're restricted in what you buy by what you like, what you're willing to spend to get the change and what it would be insane to buy just for the change - i.e. vast numbers of really small items like 1p sweets (if such things still exist).

And conversely, what you choose to buy may also affect what else you buy, if anything. So for example, if you bought the tortilla wrap, you may be weary about getting anything else, in case it ruined the change.

And one final thing to note is that if you plan to use the bus two or more times in one day, it may in fact be easier to get a day-rider, at £2.60, given that £2 is easier to get than single £1s and 60p is generally easier to get than two lots of 30p.

So yeah, just a little something to ponder. Hope it was easy enough to follow.

Till next time,

Oatzy.
