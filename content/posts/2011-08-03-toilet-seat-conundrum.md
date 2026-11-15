---
layout: post
title: The Toilet Seat Conundrum
date: '2011-08-04T02:07:00Z'
author: Oatzy
tags:
- statistics
- game theory
- gender
- python
- sociology
- over-thinking
- everyday maths
- hypothetical question
- maths
- modelling
modified_time: '2011-08-04T08:23:11.211-07:00'
thumbnail: /images/toilet-seat-conundrum/Game1Matrix.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-5151246961732753848
blogger_orig_url: https://oatzy.blogspot.com/2011/08/toilet-seat-conundrum.html
---

Gentlemen, do you leave to toilet seat up, or courteously put it down after use?

I read a (somewhat tongue-in-cheek) article a while back, I can't remember where, that explained the toilet seat conundrum in terms of game theory.  As best I can remember, it was quite clever. I was recently reminded of it when reading a [Cracked article](http://www.cracked.com/blog/7-female-behaviors-that-baffle-men-explained21_p2/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+CrackedRSS+%28Cracked%3A+All+Posts%29&utm_content=Google+Reader), and thought I'd try to recreate it, and - as is my wont - take it a step further.

[Game theory](http://en.wikipedia.org/wiki/Game_theory), for those unfamiliar, is an area of maths/economics that studies 'competitive' interactions, "*in which an individual's success in making choices depends on the choices of others*".

**Preamble**

The (average) probability of the gentleman needing to 'sit down' when visiting the bathroom, we call *p\**. The probability of not is *(1-p)*.

If the toilet seat is in the 'wrong position' for a given visit, we call the cost of this *c1*, and we assume that this cost is the same for both genders. This may not be strictly true.

The simplest cost would be in having to move the seat, typically in the form of mild inconvenience, and the potentially unpleasant experience of having to touch the underside of the seat. I'm also told that there are certain perils in visiting the toilet at the night, if the seat is in the upright position and is required to be otherwise. I can't say this is a cost I've ever experienced.

One might argue that the 'costs' are inconsequential; but for the sake of arguing, they aren't.

For the sheer hell of it, we'll call the woman *Alice* and the man *Bob*. Alice and Bob have been in a relationship/living together just long enough to quarrel over such matters. I suspect, for most people, this is a non-issue; but that's not the point of the post.

There is a third possible game, not discussed below, in which Bob can just leave the seat down at all times. In this case, we have *c3*, the cost of clean up if Bob's aim isn't quite up to scratch.

Oh, and there is a fourth game, where the default position of the the seat is upright. This is the worst possible game for Alice, and is only the best possible game for Bob if *p\<0.28*. I can only imagine this game working in an all male household, and even then (a re-adjusted) Game One works out better.

**Game One - Leave It As Is**

Probability of the seat being down is the probability of Alice being the last to visit the lav plus the probability Bob was the last and left the seat down. Probability the seat is up is 1 minus the above.

Here's the cost matrix for this game

[![](/images/toilet-seat-conundrum/Game1Matrix.png)](/images/toilet-seat-conundrum/Game1Matrix.png)

Where cost is *c1* multiplied by the probability that the seat is in the wrong position

To get the total costs to Alice and Bob for this game, we work out

(Probability the seat is down x the cost if seat is down) + 

(probability seat is up x cost if seat is up)

[![](/images/toilet-seat-conundrum/costs-game1.png)](/images/toilet-seat-conundrum/costs-game1.png)

And we can work out the ratio of costs

*B:A  =\>  2p+1 : 1*

In the extreme case, where *p=0* (Bob never poops), their costs are equal. But in all other cases, Bob's cost is greater than Alice's.

**Game Two - Return to Default**

Default meaning the seat is always returned to the downright position after use. The probability of the seat being up is always 0.

Here's what the matrix looks like

[![](/images/toilet-seat-conundrum/Game2Matrix.png)](/images/toilet-seat-conundrum/Game2Matrix.png)

In this case, Alice incurs no cost. Bob, on the other hand, incurs double cost - when he needs to urinate, he has to move the toilet seat twice: up before use, and down afterwards.

It's obvious that Alice, once again, fairs better than Bob.

Game Three, mentioned in the preamble, works the same as this, but with *2c1* replaced with *c3*. Alice still comes out better though. Unless she doesn't like the thought of sitting on a toilet seat that's (potentially) been peed on - even if it is cleaned - in which case, there's some abstract cost to her.

If she doesn't mind, then which of games Two and Three Bob would prefer depends on which is smaller: *2c1* or *c3*.

**Lowest Costs**

First of all, we note that in both games Alice comes out better than Bob - incurring a lower cost in both cases. That said, Alice does better in the latter game, incurring no cost at all in that one. So Game Two is preferable to Alice.

But what about Bob?

If we take the cost ratio of game one to game two for Bob, this is what we get

*B1:B2  =\>  2p+1 : 4*

In the extreme case of *p=1* (Bob never urinates), Game Two incurs a greater cost for Bob (*3:4*) - and by extension, Game Two always incurs a greater cost to Bob.

*THIS* is where and why the conflict arises.

Alice prefers Game Two, Bob prefers Game One.

**Tipping the Scales**

So Alice would prefer to play Game Two, but she has to encourage Bob towards it. So Alice introduces a new penalty - *c2* - for Bob leaving the toilet seat up.

The cost will typically be something along the lines of a [bollocking](http://www.urbandictionary.com/define.php?term=bollocking), silent treatment, arguments, or whatever.

So what we do is this - the odds of Bob leaving the toilet seat up, and Alice being the next to use the bathroom -\> (1-p)/2

Multiplied by the cost, *c2*, and added to the pre-existing total cost for game one

[![](/images/toilet-seat-conundrum/costs-game1-2Bc2.png)](/images/toilet-seat-conundrum/costs-game1-2Bc2.png)

Now, we - or rather, Alice - wants the cost to be such that Game Two is preferable, i.e. *B'1 \> B2*

Rearranging and simplifying, we get

*c2 \> 4c1(2p+1)*

However, if Alice were feeling kind, she could introduce a 'reward' for putting the toilet seat down, instead. It works effectively the same - barring psychological, [carrot/stick](http://en.wikipedia.org/wiki/Carrot_and_stick) considerations.

For this, Alice would have to offer a reward, *R*, with

[![](/images/toilet-seat-conundrum/game1-reward.png)](/images/toilet-seat-conundrum/game1-reward.png)

Arguably, Bob could introduce a new cost - or enticement - himself, to 'persuade' Alice towards Game One. But TV leads me to believe that this is seldom thought of, or executed.

This might be because Alice has more to gain/lose - in as much as, Alice can avoid any cost by 'playing' Game Two. Bob, on the other hand, incurs some cost in both games.

You can draw your own conclusions on that one.

In terms of a co-operative solution, if we add together Alice and Bob' costs in each game and compare, we find that Game One has a lower total cost than Game Two.

So one could argue that Game One is better overall. The challenge, though, is convincing Alice that that is the best solution for *both* of them, given that, from Alice' point of view, she does worse in Game One.

**Casino Bathrooms**

So this is all well and good, but it's kind of a specialised case - the situation of a house with one male, one female, and one toilet. In our house, for example, we have two males, two females and three toilets. What then?

There are a few other problems with the probability-based approach, as well. For one thing, it uses an average poop-probability for the gentleman. It also assumes both Alice and Bob use the bathroom about the same number of time during a given time period - whereas some people have more robust insides than others.

So for this, we create a [Monte Carlo simulation](http://en.wikipedia.org/wiki/Monte_Carlo_method).

[This is what we call excessive commitment to an idea.]

In the simulation, we create a 'person' object, and assign to them a gender, an average number of bathroom visits, and, for males, an average bladder to bowel movement ratio. To capture the day to day variability in number of visits to the bathroom, we use [Poisson distributions](http://en.wikipedia.org/wiki/Poisson_distribution).

We also create a 'toilets' set, representing however many toilets there are, and their current states -\> 1 = toilet seat up, 0 = toilet seat down. Each toilet has an equal chance of being chosen for use by any given person at any given time.

Each person has a counter, which is incremented when the person in question has to move the seat. At the end, these counters are grouped by gender for comparison.

**In the Middle of Our Street**

So I created a 'house' of two males, two females, and three toilets (variables chosen arbitrarily). Then ran the simulation for *10,000* hypothetical days.

The Game One simulation gives a result of ~ *3.28* seat moves per male per day, and *2.27* seat moves per female per day. That's a *male:female* seat move ratio of *1.44*.

The Game Two simulation gives a result of *9.11* seat moves per male per day - bearing in mind, men have to move the seat twice per standing visit, in this version - and women never have to move the seat.

Code [here](https://github.com/oatzy/question-nobody-asked/blob/main/toilet-seat-conundrum/toilet-seat.py).

Fun fact: Without additional costs and rewards, Game One is always preferable to men, Game Two to women. Regardless of the balance of men and women in a house.

So now you know!

Of course, in some cultures the conflict never really arises, since it is 'the norm' for men to sit for all visits to the lavatory.

Oatzy.

\*[inb4 *shouldn't* p *be the probability of needing to urinate lol*]
