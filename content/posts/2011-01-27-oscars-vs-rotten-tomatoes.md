---
layout: post
title: The Oscars Vs. Rotten Tomatoes
date: '2011-01-28T02:39:00Z'
author: Oatzy
tags:
- king's speech
- statistics
- films
- graph
- oscars
- infographic
- rotten tomatoes
- inception
- maths
modified_time: '2011-01-28T08:40:01.293-08:00'
thumbnail: /images/oscars-vs-rotten-tomatoes/crit-dist.jpg
blogger_id: tag:blogger.com,1999:blog-14769935.post-8029603125523369716
blogger_orig_url: https://oatzy.blogspot.com/2011/01/oscars-vs-rotten-tomatoes.html
---

**What Do Critics Know**

This is something I looked at briefly last year. I wondered if there was any correlation between [Rotten Tomatoes](http://www.rottentomatoes.com/) score - a score based on an aggregate of critic' reviews - and winning an Academy Award for Best Picture. That is, is the highest rated of the nominees for a given year most likely to win?

The short answer is no.

**Data Mining**

For those interested, the data was collected like this.

First, the list of nominees and winners is copied from [Wikipedia](http://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture). The data is then imported into [Google Refine](http://code.google.com/p/google-refine/) to be tidied up and sorted. Then, still in Refine, the list is reconciled - that is, each film on the list is linked to the appropriate page on [FreeBase](http://www.freebase.com/).

Having been reconciled, extra data can then be pulled from FreeBase; and with a bit of extra coding, the Rotten Tomatoes scores can also be mined.

NB/ some scores had to be input by hand, some scores are unavailable, and there may (but not necessarily) be errors.

You can look at the data [here](https://spreadsheets.google.com/ccc?key=0AgfLII2ZglYqdEJyRFVOUk8ycXROZDFmRVUweEs2bmc&hl=en&authkey=CLj785cD).

**Analysis**

First of all, I looked at the distribution of scores for winners vs. Nominees

[![](/images/oscars-vs-rotten-tomatoes/crit-dist.jpg)](/images/oscars-vs-rotten-tomatoes/crit-dist.jpg)

If there were some correlation, you'd expect the winners to be, generally, further to the left than the other noms. But looking at the graph, there's hardly any significant difference. In fact, the proportion of nominees with a score of 100 is greater than that of the winners.

NB/ the numbers were scaled to matching sizes.

I also looked at the number of winners that were the highest rated in their year - this works out at *22%*. Which isn't amazing (a little over one fifth). And on top of that, the number of winners that were the lowest rated in their year works out at *18.3%* (a little under one fifth).

So as I said in the short answer, there's not much of a correlation.

I also tried working with only the films since 1970, since most of the unavailable scores were for films prior to then. But the results were effectively the same.

**Audience Knows Best**

I created a few year-wise graphs, such as below (2009-2002)

[![](/images/oscars-vs-rotten-tomatoes/crit-2009-2002.jpg)](/images/oscars-vs-rotten-tomatoes/crit-2009-2002.jpg)

and looking at them only confirmed the weak correlation between score and winning.

But one in particular stood out - 2005. In 2005, [Crash](http://en.wikipedia.org/wiki/Crash_%282004_film%29) won the award despite being the lowest rated of the nominees. But I'll come back to that.

The other one that got me thinking was 2008 - both [Slumdog Millionaire](http://en.wikipedia.org/wiki/Slumdog_millionaire) and [Milk](http://en.wikipedia.org/wiki/Milk_%28film%29) got a rating of *94*.

But it occurred to me that, maybe the reason Slumdog won was because it was more appealing to a wider audience. Think about it; Slumdog is a love story, whose protagonist overcoming adversity and against all odds, gets a [happy ending](http://en.wikipedia.org/wiki/Happy_ending). Milk is a biopic about a politician and gay rights activist who is assassinated. Both are top quality films, but Slumdog has wider appeal. And maybe that's important.

Granted, I'm exaggerating, a little, the weight of the effect of wider appeal for the sake of making my point. But you get the idea.

You have to bear in mind that the Academy Award for Best Picture isn't voted for by a handful of people with a potentially homogeneous taste - it's voted for by a comity of [over 5,000](http://en.wikipedia.org/wiki/Oscars#Voters) people. So having that wider apeal is going to help.

This would also explain why genre films tend to struggle.

Luckily, Rotten Tomatoes also has an "Audience" rating - a score out of 100, based on audience interest. And sure enough, [Slumdog](http://www.rottentomatoes.com/m/slumdog_millionaire/) gets a score of *90*, versus [Milk](http://www.rottentomatoes.com/m/milk/) with *88*. Granted, it's a small difference, but it gives some credence to the theory.

So going back to 2005, I checked the Audience scores,

[![](/images/oscars-vs-rotten-tomatoes/audience-2005.jpg)](/images/oscars-vs-rotten-tomatoes/audience-2005.jpg)

and indeed [Crash](http://www.rottentomatoes.com/m/1144992-crash/) was the highest audience rated.

**Caveats**

Firstly, Audience scores fall into two variations - "want to see/not interested", or "liked/disliked". Generally, the older films are in the former category, while the newer are in the latter.

And each of these have their own potential problems.

For the first, the problem is causality - did a film get the Oscar because a because of the wider interest, or are people interested in seeing it because it won an Oscar?

There are also psychological consideration. People are weird; when a film gets a generally strong (or poor) response from critics, this can influence people's opinions - some people like to hate things because everyone loves them. Some people are just [influenced](http://en.wikipedia.org/wiki/Herd_mentality) by their peers' opinions.

But these aren't really things we can test or adjust for.

The Audience score is also going to be loosely related to the critic score, in as much as they both relate, to some extent, to the films 'quality'.

**Statistically Wiser**

So as before, we have the score distribution

[![](/images/oscars-vs-rotten-tomatoes/audience-dist.jpg)](/images/oscars-vs-rotten-tomatoes/audience-dist.jpg)

And, this is more what you'd want to see - the winners having a stronger tendency towards higher scores than the nominees.

Similarly, you can work out how many of the winners were highest rated in their year - in this case *36.6%*; double the number for critic score. Similarly, the number ranked lowest in their year drops to *7.3%*

And together, this supports the idea that there's a stronger skew towards higher scores, and thus that audience opinion is a better indicator of Oscar winners than critical opinion.

Of course, the better predictive power from the audience score could just be an example of [wisdom of the crowd](http://en.wikipedia.org/wiki/Wisdom_of_the_crowd).

Obviously, this still isn't 100% predictive power, or even 50%. So it's far from perfect. I also tried various ways of combining both scores, but wasn't able to significantly improve on the results for audience scores alone.

**Prediction 2011**

Based on all this, I'd say the smart money for this year would be [The King's Speech](http://en.wikipedia.org/wiki/The_King%27s_Speech).

[![](/images/oscars-vs-rotten-tomatoes/rating-2010.jpg)](/images/oscars-vs-rotten-tomatoes/rating-2010.jpg)

While it's only joint-third highest rated of the year according to the critics, it has the highest audience score of the nominees.

But then, everyone's expecting it to win anyway.

We shall have to wait and see..\.

Oatzy.
