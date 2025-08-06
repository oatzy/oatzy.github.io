---
layout: post
title: Pokemon TCG Pocket, Part 2 - How long it takes
date: '2025-08-06T19:00:00.000+00:00'
author: Chris Oates
tags:
- maths
- probability
- pokemon
- pokemon tcg pocket
modified_time: '2025-08-06T19:00:00.000+00:00'
---

# Champion

In a [previous post](https://oatzy.github.io/2025/04/08/how-log-to-pull-pokemon.html), I used a simulation to predict how long it would take to complete the _Champion of the Sinnoh Region_ secret mission. It said that I should expect to open around 250 booster packs.

I have now completed that mission! And I finally have the Garchomp emblem I was after

![Garchomp emblem](/assets/pokemon-tcg-champion.jpg)

So how long did it *actually* take?

On my **253rd booster** (1265 pack points), I finally pulled the one-star _Gastrodon_ - the last one-star card I needed. I also had enough pack points to buy the missing two-star _Cynthia_ (1250 pp), completing the mission.

I wish I could say I felt more excited when that happened, but mostly I was just relieved that it was done with.

## Statistics

So, having opened 253 _Space-Time Smackdown_ booster packs - of which about 200 were the _Palkia_ variants - what did I end up with?

- **152/155** one- to four- diamond cards; 99/99 from _Palkia_
- **20/24** one star cards; 12/12 from _Palkia_
- **4/24** two-star cards (not counting _Cynthia_); 3 from _Palkia_
- **0** three-star (immersive) cards
- **1** crown (gold) card

Counting duplicates, I pulled 43 one-star cards, 5 two-star cards, and 1,265 cards all together.

Oh, and I also pulled a rare booster. Which was quite a shock! But it didn’t have any of the cards I needed, which made me feel very ungrateful.

# How long would it take to complete the set?

Given the above, a natural next question is how long would it take to complete the set?

I’m currently missing **27** of the 207 cards from _Space-Time Smackdown_.

That doesn’t sound like a lot, but they’re mostly two-star and higher.

The simulation I wrote for the previous post is not suited to answering this question. So I wrote a _brand new_ simulation - [source code here](https://github.com/oatzy/pokemon-tcg-pocket-sim)

According to that simulation, I should expect to open about **1400** more booster packs to complete the set, which is more than 5 times the number I’ve already opened!

I think you’ll all agree with me when I say: “nah...”

For just the one- to four- diamond cards, I should expect to open about **200** more packs.

# Sanity check

But wait a second, I’m only missing _3_ of the one- to four- diamond cards. Would it really take that many more packs?

This feels a little off. But how can we check?

An easy set to validate the simulation against in Mythic Island, since it doesn’t have any booster variants.

The new simulation gives us a breakdown of expected packs opened by rarity:

- **Crown**: _309.2062_
- **Three Star**: _89.547_
- **Two Star**: _656.0182_
- **One Star**: _113.0376_
- **Four Diamond**: _136.5308_
- **Three Diamond**: _87.1258_
- **Two Diamond**: _57.6122_
- **One Diamond**: _43.8046_


## Immersive

Any easy rarity to validate is the three star ‘immersive’, since there’s only one of them.

In the [previous post](https://oatzy.github.io/2025/04/08/how-log-to-pull-pokemon.html), I showed how to calculate the probability of pulling a specific card from each booster. For the three star, this comes out to `1.12%`

And since pulling the card is a [Bernoulli trial](https://en.wikipedia.org/wiki/Bernoulli_trial), the expected number of boosters is `1/p = 89`, which is roughly equal to the simulated number.

## Diamond

There’s a 100% chance of pulling 3 one-diamond cards per booster. But for now, it’s easier pretend we pull one at a time.

If we pick one card from a set of 35 with equal probability, how long do we expect until we collect them all?

It seemed likely this was a well know problem with an exact solution, but I wasn’t sure how to identify it. This is the sort of thing AI is actually useful for

> “Ah, a classic problem with a rather elegant solution! You're asking about the **Coupon Collector's Problem”**

When it comes to AI, it's best to check their work. Wikipedia confirms this is indeed [the problem I was looking for](https://en.wikipedia.org/wiki/Coupon_collector's_problem)

The solution is `E[t] = n * Hn` where `Hn` is the [harmonic number](https://en.wikipedia.org/wiki/Harmonic_number) `Hn = 1/1 + 1/2 + 1/3 + ... + 1/n`

So, for the 35 common cards that comes to `145`

And since we pull 3 per booster, that’s `48` boosters.

Again. this agrees quite well with the simulation results.

## Star

The probability of pulling any one star is `12.595%`, so we expect to pull one on average **every 8 packs**.

The expected number of pulls to get all **6** one-star cards is `14.7`, so the expected number of packs is `8 * 14.7 = 117`. Another close match.

## And so

You can follow similar logic for the other rarities.

At this point you might be wondering, did I waste my time writing a simulation, when there’s an exact solution?

Maybe.

To be fair, things get more complicated when you take into account variants and the ability to buy cards.

Anyway, the simulation results seem sound. I guess I was just lucky with my pulls. I did also get some of the cards from wonder picks, which probably throws off the numbers too.

# Free to play

Now we have the ability to simulate opening boosters, we can start to ask other questions.

For example, **if I’m a free-to-play user** opening 2 booster packs a day for a month (until the new expansion is released), **what cards do I expect to pull?** How many rare cards? How close do I get to completion?

Let’s take a more recent expansion: _Eevee Grove_

If I open 2 * 30 = 60 boosters, I would expect

- **64** of the 69 diamond cards
- **10** one-star or rarer cards (not counting duplicates).
- **1/2** chance of pulling the three-star immersive card
- **1/8** chance of pulling the gold crown card

By comparison, if I go premium and open 3 packs a day, 90 per month, I would expect

- **67**  out of 69 diamond cards
- **13** one-star or rarer cards
- **2/3** chance of pulling the immersive card
- **1/6** chance of pulling the crown

As for myself, I did manager to collect all the _Eevee Grove_ diamond cards after **75 packs**, which is much less than the expected **185 packs**.

But then, a couple of the rare and ex cards I got off wonder picks. Actually, after about 50 packs I was down to 3 cards missing, and just opening pack after pack with nothing new. I wouldn’t be surprised if it had taken another 100+ packs to get those last 3 if I hadn’t wonder picked them.

# Feature creep

With a solid base simulation, it’s very easy to keep adding features.

For one, I re-implemented the original mission simulation. Reassuringly, the results agree with the old one.

In fact, I wrote it so that you can define any mission you like in json format. You can also give it an ‘initial state’, what cards you’ve already pulled, to see how much longer it'll take.

I may have gotten carried away.

I won’t go into the details here, you can have a look for yourself in [the repo](https://github.com/oatzy/pokemon-tcg-pocket-sim).

# Impossible dream

I’ve been drafting this blog for a while. I was planning to post it in line with the release of the latest set _“Wisdom of Sea and Sky”_, only to discover that the set introduces a new type of booster: _“regular plus one card”_.

Naturally, I couldn’t post the blog until I’d updated the simulation to account for these new boosters. It turned out to be a little fiddly.

But now, finally, to wrap up - below are the number of packs you should expect to open to complete each of the expansions that have been released at time of writing:

| Expansion | Diamonds | Everything |
| --- | --- | --- |
| Genetic Apex | 790 | 2052 |
| Mythical Island | 149 | 659 |
| Space-Time Smackdown | 460 | 1660 |
| Triumphant Light | 190 | 832 |
| Shining Revelry | 307 | 1137 |
| Celestial Guardians | 485 | 2048 |
| Extradimensional Crisis | 148 | 859 |
| Eevee Grove | 182 | 906 |
| Wisdom of Sea and Sky | 521 | 1820 |

Considering the (current) release cadence of a new expansion every month, it is practically impossible to complete every set. It’d take a good while to complete just one set! (Unless you’re willing to spend A LOT of money).

# Conclusion

In the previous post, I suggested that always opening the same booster would suck the joy out of the game. I definitely felt that, and wouldn’t recommend it.

But then, there’s a two-star full art _Garchomp_ in the _Triumphant Light_ expansion. Two two-star _Garchomps_ in fact!

And because I don’t learn my lessons, I’m at it again. Based on the simulation, I won’t have them any time soon...

Chris.

[I wonder if I can simulate wonder picks]