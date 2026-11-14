---
layout: post
title: The Train Problem
date: '2010-08-26T23:35:00Z'
author: Oatzy
tags:
- trains
- nerd
- everyday maths
- problem solving
- public transport
- maths
modified_time: '2010-08-26T16:42:47.817-07:00'
thumbnail: /images/train-problem/difference-eqn.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-4093151854698036158
blogger_orig_url: https://oatzy.blogspot.com/2010/08/train-problem.html
---

It started with a simple question - will I get a seat on the train?

While it may seem like a straight-forward question, since I thought of it, finding a solution has been the smoldering bane of my existence. I tried several approaches in the past, each with varying degrees of success. But the one I'm going to outline is the best I've managed - it makes no assumptions and is based on simple logic. But more on that shortly.

**Approach**

Whether you'll get a seat depends on two things:

1\) the total number of seats on the train\
2\) the number of passengers on the train

For *(1)*, the number of seats is countable (prior to boarding the train). So what you need to try and calculate/estimate is *(2)* how many people are on the train, and therefore, how many seats (if any) will be available.

**Modelling**

The number of people on a train when it leaves a station can be described as follows

> Passengers = (passengers on-board when the train arrived) - (passengers who get off) + (passengers who get on)

Or as a difference equation; at station i:

[![](/images/train-problem/difference-eqn.png)](/images/train-problem/difference-eqn.png)

where *N_i* is passengers on-board, *D_i* is passengers 'disembarking' and *B_i* is passengers boarding.

But that's only useful if we know *N\_{i-1}*, *D_i* and *B_i* - and to be fair, we can count the people on the platform for an estimate of B_i. But, how do we know, or work-out, the other two variables?

Consider a simplified version\* - a train that visits 4 stations (total):

[![](/images/train-problem/train-diagram.jpg)](/images/train-problem/train-diagram.jpg)

So what the diagram shows is, we can think of the problem in terms of passengers traveling between any two given stations. Define a function *T(i, j)* as the number of passengers traveling from station *i* to station *j* (we'll look at *T* in more detail later).

So for the example above,

N_0 = passengers getting on at *0*; passengers traveling from *0* to *1*, *2* and *3* = T(0, 1) + T(0, 2) + T(0, 3)\
N_1 = passengers already on minus getting off plus getting on = T(0, 2) + T(0, 3) + T(1, 2) + T(1, 3)\
N_2 = T(0, 3) + T(1,3) + T(2, 3)\
N_3 = 0  [since everyone gets off at *3*]

And from all that, we get that *B_i* and *D_i* can be written mathematically as

[![](/images/train-problem/B-D-Summations.png)](/images/train-problem/B-D-Summations.png)

And all of this can be combined into one 'train equation'

[![](/images/train-problem/Train-Eqn.png)](/images/train-problem/Train-Eqn.png)

**Usage**

So once you've solved that equation, your probability is simply

[![](/images/train-problem/prob.png)](/images/train-problem/prob.png)

(Where S in total number of seats available.)

And that's all well and good, and theoretically it works. But it's also useless if we can't define *T(i, j)*.

So how do you define *T(i, j)*?

First of all, logic says that it should be dependent on the popularity of the stations in question. For example, you'd expect more people to be going *Sheffield* to *Birmingham New Street* than *Derby* to *Birmingham International*.\
[if you don't know what I'm on about, you'll just have to trust me.]

And for this, we can work from something like [this](http://www.guardian.co.uk/news/datablog/2009/jul/02/rail-transport-travelleisure) [a spreadsheet giving details on the use of every station in the UK]. The only downside is, I haven't figured out the best way to use this data yet.

The other major thing to consider is temporal effects - you would expect, for example, higher use at rush-hours etc. Similarly, over the course of the year, you might expect higher usage, say, around Christmas. And if you've been on a train around Christmas, or at rush-hour, you'll be familiar with this horror.

So the T-function might involve something to distort it into this sort of shape

[![](/images/train-problem/rush-hour.png)](/images/train-problem/rush-hour.png)

But with, maybe, a less dramatic dip in the middle. That equation, in case you're interested is a variation on *Sin(x)[2Sin(x) +1]*

*Pro tip*: I have found that the best time to travel in the afternoon is around 3 o'clock.

But realistically, these are the sort of things you'd have to measure 'experimentally'. And being a theoretical man, that's really not for me to bother with.

**Practical Advice**

Of course, all this assumes that you don't have a seat reserved. If you do, all this is null and void. But otherwise..

The major caveat to this is that, due to the complexity of the system, this approach can't tell you exactly how many seats there will be. At best, it's a general estimate.

In fact, in general, this approach is really impractical, and as a result nigh on useless. Instead, you're best bet is to take steps to actively improve your odds. Most of this is fairly obvious, but still..

So for example:

1\) Stand at the far end of the platform (away from the crowds) to reduce your per carriage competition.\
2\) If you know which way the train is coming in, try to stand towards the back (for Virgin Trains). Carriage C/D is usually the completely unreserved one.\
3\) In the subtlest and calmest way possible, get to the front of any queue at your door of choice.\
*Pro tip*: Stand side on to the train so you're facing into the carriage. There's a good reason for why that gets you on quicker, but I can't, for the life of me, remember where I read it. But I do know from experience that it works.\
4\) Once you're on, quickly assess how many free seats there are. If they seem limited, grab the first (unreserved) one you see. If there aren't any unreserved, just grab the first free seat you come to and pray no-one tries to claim it.\
5\) If all else fails, just remember - the cool kids sit on the floor (Y)

**Conclusion**

Another thing to note is that this could ultimately be applied to an form of public transport. But there's a certain added complexity in buses (and some trams) since they won't necessarily visit all stops on a route. But this can be approximated by making the T-function for these stops zero.

As will all my maths-y posts so far, this is really more of an intellectual exercise, that can't really be applied practically. But there you go.

'Til next time,

Oatzy

[\*funny story, the inspiration for this approach actually came from Quantum Physics (quantised energy levels, etc).  Yeah, I know. I'm a nerd.]
