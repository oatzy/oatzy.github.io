---
layout: post
title: The Cost of Loyalty
date: '2011-10-06T17:37:00Z'
author: Oatzy
tags:
- money
- coffee
- nerd
- over-thinking
- everyday maths
- problem solving
- maths
modified_time: '2011-10-06T10:37:32.533-07:00'
thumbnail: /images/cost-of-loyalty/loyalty-formulas.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-7552648771279649011
blogger_orig_url: https://oatzy.blogspot.com/2011/10/cost-of-loyalty.html
---

So if you have a loyalty card for, say, Costa you will get 5 points for every pound you spend. One point is worth 1 pence, so you're effectively saving 5p from each £1 you spend - a saving of 5%, right?

Yeah, it's not that simple.

For one thing, if you think of it as paying full price then getting 5p back per £1, then there's the restriction that these 5 pences you're 'saving' can only be spent in Costa. Also, you only get points for the whole pounds you spend (not the pence).

So what *are* you saving?

Think of it this way - let's say every time you go to Costa you buy the same thing, spending the same amount of money each time.

The question then is, *<strong>how many visits does it take to earn enough points to get your usual order for free?</strong>*

Okay, so we have our usual order, with price P. The amount of money you 'save' (in the form of points) per visits is 0.05\*floor(P). The [floor function](http://en.wikipedia.org/wiki/Floor_function) - f() from now on - rounds the price down to the nearest pound, since you don't get points for pennies.

So we want to find the number, N, of purchases we need for the total points value to be greater than or equal to our order price P. In other words:

*0.05\*f(P)\*N = P*

or  *N = P/(0.05\*f(P))*

Now, lets start by looking at the simplest case, where P is an exact number of pounds - i.e. P = f(P)

In this case, P and f(P) cancel each other out, so *N = 20*. Notice, regardless of whether your order is £1 or £20, it will always take 20 visits to get one 'free'.

More generally, the equation becomes *N = ceil(20\*P/f(P))*

Where [ceil](http://en.wikipedia.org/wiki/Floor_function) is a function which rounds the value up to the nearest whole number. Because there's no such thing as a fractional visit, unless you count a visit in which you spend less than usual. Anyway.

Okay, so lets look at an example - a pot of tea costs about £1.60. So we work out N = ceil(20\*1.6/f(1.6)) = ceil(32/1) = 32 visits. And just to check, for a pot of tea you get 5 points per visit (5p), and 32\*0.05 = 1.60 = the price of a pot of tea. Perfect.

**Now. What about savings?**

In the tea example, you're buying 32 pots of tea and getting one for free. Which isn't a great saving, but it is a saving nonetheless.

So, the total amount you spend is *P\*N*, and you're getting *N+1* pots. That means the effective price per cup works out at *P\*N/(N+1)*.

For tea, that means you're effectively paying ~£1.55 per pot - a saving (S) of 5p per pot. What's that saving as a percent? Without going into too much detail, it turns out it's *%S = 1/(N+1)*.

Which works out at 3% for tea. Which is less than the 5% saving you might have expected.

**Incidentally..**

The example for when the price is an exact number of pounds turns out to offer an effective saving of ~4.76%. Which, again, is less than 5%, but a little better. This, by the way, is also the *maximum* % saving you can achieve with a Costa card.

In general, the % saving is much worse when the pence amount of P is high and the pound amount is low - the worst case being when the price is £1.99. This would require 40 visits to 'get one free' and offers a saving of only 2.4%.

So based on best and worst case scenarios, we can say that your % saving will always be between 2.4% and 4.8%. Similarly, visits required to get one free, N, will always be between 20 and 40.

[In fact, the absolute worst case is when P is less than 1, in which case you never get any points.]

**But to clarify..**

This 'saving' is the saving over what you would have paid if you bought N+1 pots of tea and didn't have a loyalty card - i.e. not getting the N+1th one for free.

But what if you could spend the money you saved on something else?

Think of it this way - you've bought N pots of tea, and thanks to the loyalty card, you've saved the equivalent of the cost of one more pot of tea (£1.60). In this case, the saving per pot bought would be P/N. For the pot of tea, that's 1.60/32 = 5p.

To get the percent saving (per order), we divide this number by total price, P. For tea that works out at 3.1%. In fact, this is equivalent to the point-value saved per purchase, divided by the full order price - i.e. *0.05\*f(P)/P == 1/N*

So for the whole-pound values, this does, in fact, work out at a 5% saving. And the worst saving is still for £1.99 purchases, now working out at a 2.5% saving.

**One more thing**

All of this also goes for Tesco, and Waterstones, and wherever else does money-for-points loyalty cards too. You just replace 0.05 with however many points you get per pound, divided by 100 (e.g. Tesco = 0.01).

If we call this value [rho](http://en.wikipedia.org/wiki/Rho) (which looks a bit like a lower-case p), then the general formulas are:

$$ N = \mathit{ceil}\left(\frac{P}{\rho \cdot \mathit{fl}(P)}\right) \qquad \%S = \frac{1}{N+1} $$

But again, we're assuming you spend approximately the same amount (P) every time you visit a given place. If not, things get tricky. For a rough estimate, one thing we can try is using an average per visit spend (Pbar).

One other thing we can do is replace the P on the top of the fraction with a target points/saving; replacing f(P) with f(Pbar) if necessary.

So, for example, if the average order (Pbar) is £3.55 and you want enough points to get a free slice lemon cake (£2.50), then it will take N = 17 visits.

Oatzy.
