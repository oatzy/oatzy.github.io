---
layout: post
title: Miscellaneous Crap
date: '2010-08-30T22:06:00Z'
author: Oatzy
tags:
- lesbians
- time
- statistics
- coffee
- nerd
- twitter
- everyday maths
- problem solving
- tweets
modified_time: '2010-08-30T16:10:05.216-07:00'
thumbnail: /images/miscellaneous-crap/xkcd-crop.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-2845845541998843778
blogger_orig_url: https://oatzy.blogspot.com/2010/08/miscellaneous-crap.html
---

**More Sex and Lesbians**

[Dimensional analysis](http://en.wikipedia.org/wiki/Dimensional_analysis) is a hell of a thing. You can come up with all sorts of [dubious](http://xkcd.com/687/) 'statistics'. Here's an example from [XKCD](http://xkcd.com/563/)

[![](/images/miscellaneous-crap/xkcd-crop.png)](/images/miscellaneous-crap/xkcd-crop.png)

I looked up the population density of my area - [South Yorkshire & Humberside](http://www.statistics.gov.uk/cci/nugget.asp?id=2231) = *340* people/km^2 - ran the numbers and got a radius of *452m*. So on a map, that looks something like this

[![](/images/miscellaneous-crap/map1.jpg)](/images/miscellaneous-crap/map1.jpg)

Now straight away, you see that on account of the relatively low population density around my house, this value probably isn't that accurate. There are several other assumptions and problems as well. But I'm not going to go into that.

As for the lesbians, it works out pretty much the same. The only difference is that you adjust the population size.

According to [Wikipedia](http://en.wikipedia.org/wiki/Lesbians#Population_estimates), an estimated *6.76%* of the female population of UK are lesbian - *~3.38%* of the total population. And that equates to a radius increase of about *x5.4*. This leads to a radius of *2.46km* (*~1.5 miles* in old money).

And that looks like this

[![](/images/miscellaneous-crap/lesmap.png)](/images/miscellaneous-crap/lesmap.png)

Again, this ignores things like the low population density of the area, the dubious lesbian population estimate, etc. and assumes that the average duration and frequency of lesbian sex about matches the general average, etc. And time dependency! But, again, I'm not going to go into all the details of that.

Why did I work out the numbers for lesbians? Why not? And that way I'm not just flat out copying XKCD. Plus I've got a quota to meet\*

**Will I Get a Girlfriend at University?**

So there are *18,480* undergraduate students at [Sheffield](http://en.wikipedia.org/wiki/Sheffield_University). If you adjust for gender, sexuality and relationship status (assuming 50% are in a relationship) that number becomes *4,359*.

But obviously that doesn't account for preferences like attractiveness, personality, intelligence, etc. and whether they'd be interested in me.

Now this guy, in the article "[Why I Will Never Have A Girlfriend](http://en.nothingisreal.com/wiki/Why_I_Will_Never_Have_a_Girlfriend)" goes a little further, using normal distributions and such to adjust for the above (a man after my own heart). So if I assume that I can apply the same ratios as he does, that number goes down to..\.

*\*drumroll\**

<u>*2.5*</u>

Yeah. It doesn't look good. But maths be damned! Besides, this estimating isn't an exact science.

**LD50**

The [LD50](http://en.wikipedia.org/wiki/LD50) of a given chemical is the dose that will killed ~50% of a population, or equivalently, that has a 50% chance of killing you. Usually based on dose per kilogram of body mass, and varies depending on animal, due to varying metabolic rates. So we can do some fun things with these values.

Let's assume a person weighing *14st*. To find for your own weight, divide by 14 and times by your weight in stones.

Note that the quantities would have to be consumed within the half-life of the chemical in question.

Caffeine - 192mg/kg = *41 cups of coffee*

Alcohol - 10.6g/kg = 118 units = *19.7 bottles of wine*

Theobromine - 488mg/kg ([estimated](http://en.wikipedia.org/wiki/Theobromine_poisoning)) = *3.1kg of dark chocolate*.

Now<em>,</em> [Hotel Chocolat](http://www.hotelchocolat.co.uk/chocolate-bars-Chcoslab/) sell 500g slabs of chocolate - so you'd only have to eat six of those to become seriously, and potentially fatally, ill. That being said, it'd take a strong man (or woman) to eat six of those in a day or less! And my hat goes off to anyone who tries.

For a 20kg dog (a small female Labrador, for example), it'd only take *240g* of dark chocolate. Which is why you shouldn't let dogs (or any small animals) have chocolate. But you already knew that.

I also remember reading somewhere (but can't remember where) that for a small bird it'd only take an M&M's worth of chocolate. So yeah, if you're looking for a new hobby..\. *\*\**

**Ireland and Alcohol**

The average [alcohol consumption](http://www.guardian.co.uk/news/datablog/2009/mar/03/drugs-and-alcohol-health) in Ireland (per person per year) is equivalent to *13.69* *litres* of pure alcohol (100% vol.). That's equivalent to *1,369* *units* per year, or *26.3 units* per week.

And just for fun - what that means is Irish people, on average, drink the equivalent of *11 pints of Guinness* a week.

[Yeah, I went there.]

Oh, and contrary to popular belief, Ireland doesn't consume the highest amount of alcohol in Europe (per person per year) - at *15* *litres*, Luxemburg does!

The UK only consumes a comparatively pitiful *12* *litres*, in case you were wondering.

**At What Times Do the Hands of a Clock Meet?**

I'm not going to go through the derivation, but basically you work out each hand's angular speed, equate and rearrange.

The equation looks like this

$$ T = H \;\, \mathit{hrs} + \frac{60}{11}H \;\, \mathit{mins} $$

Where, *H* is hours - 0 to 11 - and the minute fraction is rounded to the nearest whole number.

So, the times are - *0:00*, *1:05*, *2:11*, *3:16*, *4:22*, *5:27*, *6:33*, etc.

You could include the seconds hand as well, but that just complicates things. Well, not really. But..\. lazy :]

**When Will I catch Up to @PkmnTrainerJ?**

That is, when will I match his number of tweets? This is something I worked out [before](http://www.twitlonger.com/show/2d9sdt), reproduced here for the shear hell of it.

So first of all we have to assume that our rates of tweeting can be considered approximately constant when averaged over some period of time. So say my rate is *r_1* and his is *r_2*. If we assume that I post more tweets a day than him, then my relative speed of tweeting is

$$ r_1 - r_2 $$

(If his rate is greater than mine, then I'll 'never' catch up.)

You then take the difference between my tweets and his - i.e. how much I have to catch up by. Call that *d*.

So then *rate = tweets/time*, or, *time = tweets/rate*

$$ t = \frac{d}{r_1 - r_2} $$

If rate is in tweets per day, then time is in days.

I wrote a program for this, that you can look at [here](https://github.com/oatzy/question-nobody-asked/blob/main/miscellaneous-crap/twitterCatch.py), if you're so inclined. And according to that program, I should catch up in *437* *days*, or on *11th October 2011*.

*NB*, Due to difficulty in calculating the rates and the variability of rates over time, the results aren't particularly exact. Especially for long periods of time like above.

**Houses of Cards**

How many cards, *c*, does it take to build a house of cards *n* levels high?

$$ c = \frac{1}{2}n(3n + 1) $$

If you want to know how that's worked out, feel free to ask.

From that, we can rearrange to get the highest 'house' we can build with *c* cards

$$ n = \frac{1}{6}\left(\sqrt{(1 + 24c)} - 1\right) $$

So for a standard pack of 52 cards, the highest house you can build is *5 levels* high (with 12 cards left over). To Build a 6 level house you'd need 5 more cards.

Oatzy.

\* I don't actually have a quota. But I've definitely set a personal record for most uses of the word 'lesbian' in one post..\. I'll stop now.\
\*\* Please don't poison small birds.
