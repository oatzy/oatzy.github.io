---
layout: post
title: With Enough Tries..?
date: '2011-07-13T02:20:00Z'
author: Oatzy
tags:
- money
- statistics
- nerd
- lottery
- everyday maths
- problem solving
- hypothetical question
- random
- hand-waving
- maths
modified_time: '2011-07-13T07:12:45.904-07:00'
blogger_id: tag:blogger.com,1999:blog-14769935.post-1608238224456289229
blogger_orig_url: https://oatzy.blogspot.com/2011/07/with-enough-tries.html
---

Probability is tricky. It isn't always intuitive. Coincidences aren't necessarily as rare or as unusual as they might seem.

I can't remember how I got to it, but the other day I came across the wiki article on the [Law of Truly Large Numbers](http://en.wikipedia.org/wiki/Law_of_Truly_Large_Numbers). An interesting idea to say the least.

Then a couple of days later I was looking through one of my [books](http://www.amazon.co.uk/Why-Buses-Come-Threes-Mathematics/dp/1861058624/ref=sr_1_1?ie=UTF8&qid=1310516988&sr=8-1) for blog ideas, and came across an essay with an example strikingly similar to that in the wiki article (in never gave it a name).

[Coincidence](http://of%20course%20not%20don%27t%20be%20silly/)?

**So what is the Law of Truly Large Numbers?**

The Wiki page gives this description:

> *[The law] states that with a sample size large enough, any outrageous thing is likely to happen.*

The example given on the page is a little inelegant, so I'll go with the (abridged) similar example from the book,

> Suppose that a really memorable, once in a lifetime coincidence is one which has a one in a million chance of happening today, and that during any particular day there are 100 opportunities..\. [T]he chance that one of these coincidences will happen to you tomorrow is 1 in 10,000. Still very unlikely..\.

> [But] the chance that every one of the next twenty years will have *no* one-in-a-million coincidences for you is.. 0.48, or a 48 per cent chance.

> According to this extremely rough and ready calculation, there is actually more than a fifty-fifty chance that in the next twenty years you will experience a memorable one-in-a-million coincidence. This also means that for every twenty people you know, there is a greater than 50% [chance] that one of them will have an amazing story to tell during the course of a year.

Now this is an interesting thought.

And it raises an interesting question - *If you play the lottery enough times, does winning eventually become significantly more likely? Inevitable?*

It's an often quoted 'fact' that you're more likely to be stuck by lightening on your way to buy your ticket, than you are to win. But what does 'the law' have to say on the subject?

**Preamble**

For this we're assuming a [good old fashion](http://en.wikipedia.org/wiki/Lottery_mathematics), six balls from a pool of 49 lottery.

Probability of winning the jackpot (matching all six balls) with one ticket is *1/13983816* or about *7 in 100million*

If you play two lotteries, then your odds of winning are (Odd of winning the first) + (odds of winning the second) + (odds of winning both).

OR, and this is easier to work out,

Let 'Odds of not winning', *q = 1-p(winning)*

'Odds of winning at least once in two games' = 1 - (odds of winning neither) = *1 - (q\*q)*

This can be generalised to 'Odds of winning jackpot playing *n* games', *p =* *1 - (q^n)*

**Round One: Will I hit the Jackpot in My Lifetime?**

First of all, odds of winning the jackpot by playing every week for a year

*p = 1 - [1-p(winning)]^52* = *3.7 in 1million*

So not great. How about if you play ever week, starting on your 16th birthday and giving up (dying) on your 86th. Or basically, playing for 70 years. Probability of hitting that jackpot?

About *1 in 4,000* chance. So still not great.

Of course, if you buy 40 tickets a week, then that gives you a *1 in 100* chance of winning the jackpot at some point in your life. But by that point you're spending *£2,080* a year on lottery tickets. The average jackpot would have to be more than *£14.6 million* for the [expected return](http://en.wikipedia.org/wiki/Expected_return) (prize\*chance of winning) to make it worth playing.

**Round Two: What About Immortality?**

So we've got the equation *p = 1 - (q^n)*

The question is, can we find *n* - i.e. the number of games you'd have to play - such that the probability of winning (*p*) is 50:50

The trick is [logarithms](http://en.wikipedia.org/wiki/Logarithm), and the formula is

*n = log(1-p)/log(q)*

So for p = 0.5, n = *9,692,842* games, or about *186,400* years.

For a 1 in 4 chance of winning? *77,363* years

1 in 100 hundred chance?! *2,703* years

Alternatively, to have a 50:50 chance of winning in your lifetime (70 years) you'd need to buy *2,663* tickets a week. Yeah.

Basically, even by the *Law of Truly Large Numbers,* and immortality, you'd be waiting a ridiculously long time and you'd still be lucky to win.

**Round Three: I'll Take Anything!**

Now wait a minute, I hear you say, I could still win something by matching 5 numbers, or even 3. Okay, that's a fair point.

So you need to match 3 or more numbers to win *something*. Probability of winning anything in any given game? *~6 in 100,000*

So once again, chance of winning something if you play every week for 70 years? *195 in 1,000*

Now that's interesting. That's just short of a *1 in 5* chance. But to be worth playing, the average prize value would have to be *~£18,666*. Worth it? I'll let you decide<em>\*</em>.

And finally, how long would you have to play to have a 50:50 chance of winning something? ~*223* years. Or *45* years if you buy *5* tickets a week.

Which is going to be a real kick in the balls if that something turns out to be £5.

**Or To Put it Another Way**

*\** Imagine a game you only get to play once. You pay me *£3,640* to play, then you pick a number between *1 and 5*. I then generate a random number between 1 and 5.

If the number that's generated is the number you chose then you will win some randomly chosen prize between *£5* and *£5million*; you're more likely to win a smaller prize than a larger one, and you can't know in advance what the prize will be.

Want to play?

If you play the lottery, but answered no to the above, you should probably reconsider.

*<strong>tl;dr</strong>* As has been said many times before, your odds of winning the lottery jackpot are catastrophically minute. Even if you were to play every week of your life.

Oatzy.
