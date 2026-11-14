---
layout: post
title: Deal or No Deal
date: '2011-12-19T00:37:00Z'
author: Oatzy
tags: 
modified_time: '2011-12-18T16:37:28.569-08:00'
thumbnail: /images/deal-or-no-deal/DoND-samples.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-425802117433249417
blogger_orig_url: https://oatzy.blogspot.com/2011/12/deal-or-no-deal.html
---

One of the common criticisms of [Deal or No Deal](http://en.wikipedia.org/wiki/Deal_or_no_deal) (DoND) is that it's basically all just luck, and requires no skill.

Okay, so unlike most TV game-shows you don't have to know anything to play. In fact, based on knowledge/skill required to win and on average pay-out, DoND is probably the best TV show to play on - as said, you don't have to know anything to play, and once you're on the show you're guaranteed to walk away with *something*.

Okay, so how much you walk away with does indeed depend a lot on luck. But I would argue that it depends on luck in the same way that, for example, [Blackjack](http://en.wikipedia.org/wiki/Blackjack) (21) depends on luck. One might argue that there's no skill in Blackjack, and yet there's no denying that some people fair better at it than others. And one might say this disparity is the result of skill or strategy.

Certainly [card counting](http://en.wikipedia.org/wiki/Card_counting) (when you can get away with it) is a skill, and one which can increase your winnings.

**It's How you Play the Game**

Behind all the 'quirky' contestants, the blatant superstition and Noel Edmond's [interesting shirts](http://floralshirtsonline.co.uk/2011/03/top-ten-celebrity-floral-shirt-wearers/), lies a surprisingly complex game. Albeit a 'complex' game which can be played competently with little to no skill.

In fact skill only comes into it when you start trying to tip the probability scales in your favour, without relying on trinkets and 'special numbers'.

But before we start, I should probably outline the game for the sake of anyone unfamiliar:

There are 22 boxes, of which one is yours. Each box contains some unknown amount of money, ranging from 1p to £250,000.

The idea is to try and determine the value of your box by eliminating other boxes from the game. Also trying to determine the value of your box is 'The Banker', who will attempt to make offers to buy your box, and in doing so, try to make a profit for himself.

Your aim is to come out of the game with as much money as possible - ideally, either by selling your box for more than it's worth, or by keeping a box which is more valuable than any of The Banker's offers.

Still with me?

So there's actually a big [game theory element](http://en.wikibooks.org/wiki/Introduction_to_Game_Theory/Deal_Or_No_Deal) in this, when it comes to dealing with The Banker. There's also a risk assessment element, wherein, based on which values have been eliminated or are still in play, you have to decide whether you should play on.

In this blog, I'm going to be focusing on the offers part of the game, and deciding when to deal. I may come back to the other elements in later blog posts.

**Let's Play a Card Game**

Take a standard deck of 52 cards, shuffle them, and deal 10 cards face down.

The aim of the game is to get the best card possible.

You turn the cards over one at a time. If you want to keep the card you turn over, then that's your card forever. You can't swap it for another card later. If you turn over a card you don't want to keep then it's gone forever, and you can't go back to it later.

So, for example, say you turn over the first 4 cards, and you get - 2, 9, 8, 5 - Now you could have stuck on 9, since it's a pretty good card. But there are still 6 cards felt to turn over, so you decide play on.

You turn over 2 more cards - A, Q - Since Aces are low, it seems wise to stick on the Queen, since there's only the King that's better, and only 4 cards left to turn over.

So you turn the last 4 cards over  to see how well you fared, and you get - 7, 5, K, 10.

Okay, so there was a better card than the one you ended up with, but you still came out pretty well.

Anyway, hopefully you get an idea of how the game works.

So this is ultimately a game of chance and of how much risk you're willing to take to get a potentially better card. The question is, is there a strategy for maximising your chances of getting the best possible card?

Obviously, since the King is the absolute best possible card, you might be tempted to play until you find one. But since there's no guarantee that there will be a King on the table, you risk playing to the end, only to end up stuck with the last card, which could be really crappy.

**The Dating Game**

In the book "[How Long is a Piece of String](http://www.amazon.co.uk/How-Long-Piece-String-Eastaway/dp/1861056257/ref=sr_1_1?ie=UTF8&qid=1324252698&sr=8-1)", the author offers a variation on this game as a very simplified analogy for dating - the idea being to settle down with the best possible partner, bearing in mind that you usually won't be able to go back to dating anyone you passed on if you aren't able to find anyone better later, and that once you settle down into a relationship you stop dating, and potentially miss out on meeting someone better.

As far as the strategy goes, the author suggests turning over the first three cards as a sort of sample pool, then settling on the first card whose value exceed those of all three sample cards.

According to his probability measurements, this results in you getting the best card one time out of three. Which, apparently, is as good as you can hope to do.

So in the above example, your sample cards are 2, 9, 8. The first card after that which is greater than all those is, in fact, the Queen.

Like I said, it's not perfect. And a 1 in 3 success rate may not sound very good. But lets be clear - this is (theoretically) your absolute best strategy.

**Let's Make a Deal**

So ignoring the whole boxes stuff completely (I know, but stay with me here) we can reduce DoND to being a game where a contestant is presented with 7 (random) offers and is trying to decide which one (if any) to take.

And this is where the card game comes in - it's basically the same game, just with fewer offers/cards.

In fact, there are 7 offers, but if you decide to reject all those, you're stuck with the value in your box. So that's equivalent to the card game described above played with 8 cards.

So first of all, I should point out that the three card strategy from the book applies to a slightly different variation on the game I outlined. So we also have to tweak our strategy to match our tweaked game.

First of all, the book itself offers this detail - for a game with N card (choices), the sample size should be *N/e*, where [e](http://en.wikipedia.org/wiki/E_%28mathematical_constant%29)=2.71.. So for a game of 8 choices our sample should be 2.9 (~3).

But again, this is for a slightly different game than ours. So we'll want to check that this strategy really does apply to our game.

Thing is, there's a whole bunch of probability calculations involved in working that out. And probability calculations are a pain in the arse. So in lieu of all that, I did a [Monte Carlo simulation](http://en.wikipedia.org/wiki/Monte_Carlo_method) instead.

Here's [the code](http://dl.dropbox.com/u/4635169/DoND.py).

And what the code suggests, is that the best strategy is actually to pass on the first *two* offers - giving a success rate of about ~49%

For comparison, here's the success rates for different numbers of passes (rejected offers):

[![](/images/deal-or-no-deal/DoND-samples.png)](/images/deal-or-no-deal/DoND-samples.png)

And nearly 50:50 isn't bad odds. But we do have to keep in mind that this result is for a simulation of a card game which is a simplified analogy for one element of a game show.

Your results may vary.

But the implication is this - **<em>in a simplified game of DoND, the optimal strategy is to reject the first two offers, and take the first one after that which exceed them</em>**.

**Spank the Banker**

Obviously, DoND, when considered as a whole, is not as simple as accepting or rejecting a series of offers. For one thing, in the real game you have more information (i.e. what values are or aren't still in play) to help inform your decisions.

But this strategy *could* be considered at least some improvement on the 'by the gut' approach.

So yeah. Until possibly next time..

Oatzy.

[Get it? 'Cause 'deal' can also mean 'to distribute cards'.]
