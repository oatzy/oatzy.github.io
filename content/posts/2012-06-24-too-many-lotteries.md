---
layout: post
title: Too Many Lotteries
date: '2012-06-25T00:07:00Z'
author: Oatzy
tags:
- probability
- nerd
- lottery
- games
- proofs
- over-thinking
- everyday maths
- problem solving
- maths
modified_time: '2012-06-24T17:51:01.275-07:00'
thumbnail: /images/too-many-lotteries/102525_0.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-313622568677561345
blogger_orig_url: https://oatzy.blogspot.com/2012/06/too-many-lotteries.html
---

So recently I'd gotten really into this TV show - it's called '[Life](http://en.wikipedia.org/wiki/Life_%28NBC_TV_series%29)', and it's a 'murder of the week' crime drama starring Damian Lewis. Lewis plays Detective Crews, who was previously in prison for a muder he didn't commit, and he's into zen and such. It's a bit silly. But in an endearing sort of way.

Unfortunately, the only way I could watch it (short of buying the DVDs) is to stay up til 4am. Which isn't really a problem; I don't have anything to get up for. Though it is tricky getting to sleep as the sun's coming up.

Anyway, the point is, by 4am, there are only, like, four adverts on rotation (on FX, at least). These are: upcoming shows on FX, whatever product JML is flogging, that tacky accident helpline ad with Esther Rantzen, and this '*Win Trillions*' thing.

*Win Trillions* is a lottery sindicate thing - from what I understand, it works like this: a bunch of people from around the world get together, each buying tickets for their respective countries' lotteries. If one of the sindicate members wins, they split the winnings with their fellow sindicate members (and presumedly, *Win Trillions* takes a cut).

Really, though, the details aren't that important. What is important is their slogan - "play more lotteries, get more chances".

Which isn't a false claim. It's just kind of misleading; playinng more lotteries *does* mean more chances of winning, but only in a similar way as buying more tickets for a single lottery means more chances of winning - your odds of winning are so small to begin with ([*~1 in 13,983,816*](http://en.wikipedia.org/wiki/Lottery#Probability_of_winning)) that you'd have to play thousands of lotteries (or buy thousands of tickets) to significantly improve your chances. And there are only so many lotteries in the world.

**Strategies**

You'll notice I used the word 'similar' back there; the fact is, buying more tickets, and playing more lotteries don't 'improve' odds in the same way.

So the question is, which is the better strategy - buying many tickets for a single lottery, or buying one ticket for each of several lotteries?

First, imagine I have a dice; I'm going to roll the dice, and you have to bet on the outcome. Your choice is this - would you rather place three bets on one dice roll, or one bet on each of three dice rolls?

For the first case, say you place your bets on it being 1, or 2, or 3. Your odds of guessing the correct number (and winning) is 3 in 6 (=0.5).

For the second case, say you bet that each of the rolls will be 6. Then your odds of winning 'something' is odds of winning just one of the dice rolls, plus the odds of winning just two of the dice rolls, plus the odds of winning all three.

Which is trickier to work out. For example, the odds of winning the first roll only, is odds of getting the first roll right (1 in 6), *and not* getting the second roll right (5 in 6) *and not* getting the third roll right (5 in 6) - which makes the probability of getting just the first roll right = 1/6 \* 5/6 \* 5/6 = 25 in 216

And you have to work out the probabilities for all possible winning outcomes (in this case, there are seven winning outcomes, one losing.).

Alternatively, we can use the trick that the odds of winning *something* is one  minus the odds of winning *nothing*. The odds of winning nothing is the odds of getting all the bets wrong: 5/6 \* 5/6 \* 5/6 = 125 in 216 (0.58)

So the odds of winning something is 91 in 216 (=0.42)

So for this dice game, it's better to place your three bets on a single dice roll.

But what about in general?

We say each game has a probability *p* of winning, and that we're going to place *n* bets (with n\>1).

For the single game bet, the probability of winning is *n\*p*

For the multi-game bet, the probability of winning is

$$ 1 - (1 - p)^n $$

**Which is bigger?**

Well for n = 1, the games are idential. For n = 2, the single game is *2p*, the multi-game is *2p - p^2*; the single game has higher odds. For n \>= 1/p, the single game gives a probability greater than or equal to 1 - i.e. guaranteed win - where the multi-game always gives a values less than one; again, the single game gives better odds.

So it's looking like the single game is always better. But how do we prove it?

For this, we look at the [binomial expansion](http://en.wikipedia.org/wiki/Binomial_expansion) of (1-p)^n

A Binomial Expansion works like this

$$ \begin{aligned} (x + y)^n &= \sum_{k=0}^{n} \frac{n\ldots(n - k + 1)}{k!}x^k y^{n-k} \\ &= x^n + nyx^{n-1} + \frac{n(n - 1)}{2!}y^2x^{n-2} + \ldots \end{aligned} $$

where *k!* is the [factorial](http://en.wikipedia.org/wiki/Factorial) of k. For example: 2! = 2\*1; 3! = 3\*2\*1; 4! = 4\*3\*2\*1; etc.

In this case, x = 1 and y = -p, so the expansion becomes

$$ (1 - p)^n = 1 - np + \frac{n(n - 1)}{2!}p^2 - \frac{n(n - 1)(n - 2)}{3!}p^3 + \ldots $$

Which makes the probability of winning the multi-game

$$ 1 - (1 - p)^n = np - \frac{n(n - 1)}{2!}p^2 + \frac{n(n - 1)(n - 2)}{3!}p^3 - \ldots $$

So whether or not the mutli-game has higher odds than the single game depends on the sum of the terms after np.

First, we compare the k-th and (k+1)-th (adjacent) terms in the expansion

$$ \frac{n\ldots(n - k + 1)}{k!}p^k \stackrel{?}{=} \frac{n\ldots(n - k - 1)(n - k)}{(k + 1)!}p^{k+1} $$

Which simplifies to

$$ 1 \stackrel{?}{=} \frac{n - k}{k + 1}p $$

The righthand side has it's maximum value when n is maximum. We previously defined the maximum value of n as *1/p*, so

$$ \frac{\frac{1}{p} - k}{k + 1}p = \frac{1 - pk}{k + 1} \;<\; 1 $$

since p and k are always greater than 0.

Which means

$$ \frac{n\ldots(n - k + 1)}{k!}p^k > \frac{n\ldots(n - k - 1)(n - k)}{(k + 1)!}p^{k+1} $$

In other words, each term in the expansion is smaller than the ones before it.

This means that, if we pair up terms,

$$ \begin{aligned} \left(-\frac{n(n - 1)}{2!}p^2 + \frac{n(n - 1)(n - 2)}{3!}p^3\right) &< 0 \\ \left(-\frac{n\ldots(n - 3)}{4!}p^4 + \frac{n\ldots(n - 4)}{5!}p^5\right) &< 0 \\ \left(-\frac{n\ldots(n - k + 1)}{k!}p^k + \frac{n\ldots(n - k)}{(k + 1)!}p^{k+1}\right) &< 0 \end{aligned} $$

i.e. the sum of each pair will be negative. Therefore, the sum of all the pairs (all the terms in the expansion after np) is negative. So necessarily

$$ 1 - (1 - p)^n = np + \left(-\frac{n(n - 1)}{2!}p^2 + \frac{n(n - 1)(n - 2)}{3!}p^3 - \frac{n\ldots(n - 3)}{4!}p^4 + \ldots\right) < np $$

Which means the **<em>odds of winning the single game is ALWAYS better than the odds of winning the multi-game</em>**.

**Pay-Outs**

You might have noticed that the single game has a single possible payout, where playing the multi-game means you could win double, triple, or even more of the prize. So the odds of winning the multi-game are lower, but you stand to win more.

Does that mean it's worth the extra risk?

For this, we look at the expected winnings for each game. The expected winnings is calculated as the *probability of winning* multiplied by the *prize amount*.

So if you were guessing the outcome of a dice roll, and the prize was £1, then the expected winnings from playing that game would be ~17p.

Or think of it like this - if you had to guess the outcome of a dice roll six times, you would expect to be right once out of six. So your expected prize for 6 rolls is £1, or 17p per roll.

For this single game, the payout is easy: *w\*n\*p* (where w is the prize for winning one game)

For the multi-game it's more complicate. We can't use the same trick as last time; instead, we have to work out odds of winning one game times prize from one game + odds of winning two games times prize from two game + etc.

The general form is the series sum

$$ \begin{aligned} &n(w)p(1 - p)^{n-1} + \frac{n(n - 1)}{2!}(2w)p^2(1 - p)^{n-2} + \ldots \\ &= \sum_{k=1}^{n} \frac{n\ldots(n - k + 1)}{k!}(kw)p^k(1 - p)^{n-k} \end{aligned} $$

Which can be manipulated and simplified to give

$$ \begin{aligned} &= w\sum_{k=1}^{n} \frac{n\ldots(n - k + 1)}{(k - 1)!}p^k(1 - p)^{n-k} \\ &= w\sum_{k=0}^{n-1} \frac{n\ldots(n - k)}{k!}p^{k+1}(1 - p)^{n-k-1} \end{aligned} $$

Now, if we expand it out again

$$ = w\left(np(1 - p)^{n-1} + n(n - 1)p^2(1 - p)^{n-2} + \ldots\right) $$

Then there's a factor of np in each term, so we can take that outside the bracket

$$ = wnp\left((1 - p)^{n-1} + (n - 1)p(1 - p)^{n-2} + \ldots\right) $$

And since n is some arbitrary interger, we can substitute m = n - 1 and put it back in summation form

$$ \begin{aligned} &= wnp\left((1 - p)^m + mp(1 - p)^{m-1} + \ldots\right) \\ &= wnp\sum_{k=0}^{m} \frac{m\ldots(m - k + 1)}{k!}p^k(1 - p)^{m-k} \end{aligned} $$

Now, you might notice the summation part is actually a binomial expansion; in this case we have x = (1 - p) and y = p, so

$$ \sum_{k=0}^{m} \frac{m\ldots(m - k + 1)}{k!}p^k(1 - p)^{m-k} = ((1 - p) + p)^m = (1)^m = 1 $$

For all values of p and m = n - 1.

Therefore, the expected payout of the multi-game is always *w\*n\*p*

You'll notice that this is the exact same expected payout as for the single game. As in, **<em>regardless of which strategy you use, your expected payout is the same</em>**.

So the question is, would you rather a low risk low prize game, or a high risk (potentially) high prize game?

**Complexities**

You'll notice for this I assumed all lotteries have the same odds of winning and the same prize amount. This is not necessarily true.

Even so, from this, the best strategy would be to find the lottery with the best single game single bet expected payout (prize \* probability of winning), and buy several tickets for that game, rather than spread your money around.

The other thing in lotteries is you can usually win smaller prizes for matching fewer numbers. But I don't imagine that changes which strategy is best.

So now you know. For what it's worth. The odds of winning playing, say, 70 tickets on one lottery is only about two 10,000ths of a percent better than playing one ticket on 70 lotteries.

Incidentally, those derivations up there count as [mathematical proofs](http://en.wikipedia.org/wiki/Mathematical_proof). So these conclusions I've drawn are irrefutable<em>\*</em>. And the results apply to any game where you're placing bets on a single probability random outcome - not just lotteries.

Oatzy.

[*\*-* Assuming I haven't cocked it up..\.]
