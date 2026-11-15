---
layout: post
title: TrainRank
date: '2010-12-08T23:29:00Z'
author: Oatzy
tags:
- trains
- public transport
- maths
- modelling
- network
- pagerank
modified_time: '2010-12-08T15:29:14.074-08:00'
thumbnail: /images/trainrank/map.jpg
blogger_id: tag:blogger.com,1999:blog-14769935.post-6313992094728997104
blogger_orig_url: https://oatzy.blogspot.com/2010/12/trainrank.html
---

Or StationRank. Either way, it's a misnomer, since [PageRank](http://en.wikipedia.org/wiki/Pagerank) is named after it's creator, Larry Page. But I digress.

Anyway, the idea is basically this - going back to the [previously mentioned](https://oatzy.github.io/2010/08/26/train-problem.html) train problem, in a moment of inspiration it seemed worth trying working out PageRanks for UK train network; this hopefully correlating somehow to where passengers on a given train are likely to be going.

**Stations**

First of all, there is a total of about 2,518 train stations in the UK, and damned if I'm going to (or even could) work out a PageRank for the entire network. Even if you only use the [Virgin CrossCountry routes](http://www.crosscountrytrains.co.uk/Tickets_and_timetables/Routes.aspx), you're still working with short of 100 stations. So for this I used the major stations on the CC line. There's about 30. Major stations, by the way, are the ones with a big circle on the map below

[![](/images/trainrank/map.jpg)](/images/trainrank/map.jpg)

Obviously the simplification has an effect on the results. I compared to [station use](http://www.guardian.co.uk/news/datablog/2009/jul/02/rail-transport-travelleisure) numbers for those stations included and got a [correlation coefficient](http://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient) so close to 0 as to make no odds. But you have to bare in mind the use numbers include all train lines going in and out of each station (not just the Virgin CrossCountry lines).

Anyway, for demonstrative purposes it's good enough.

**Ranks**

So the TrainRanks are as follows

[![](/images/trainrank/TrainRanks.png)](/images/trainrank/TrainRanks.png)

And at the very least, it seems to fit alright with my experience - my experience being limited to traveling between Sheffield and Coventry.

**Random Trains**

So what does it mean? For websites, it's based on this idea of a 'random surfer' clicking random links, resulting in probabilities of the surfer ending up on any given page.

So by analogue, we assume a train that moves randomly around the network; and that includes randomly changing direction and taking routes that wouldn't, in the real world, be valid. We then imagine a passenger on this slightly erratic train - a station's TrainRank is the probability the passenger will get off at that station.

Or alternatively, if there are 100 people on this train then, for example, about 7 of those people will get off at Birmingham New Street.

Now obviously, there are some problems with that definition, the most obvious being that that's just not how trains work. Similarly, I don't know if or how this would fit into my previous model. But it's interesting to consider, nonetheless.

**Simplifying Routes**

It does seem to make sense to limit the ranks to given networks, since passengers have to get off the train of one network to leave the station or get on a train for another network. But at the same time, what other networks call at a given station may have an effect on the probability a passenger will get off the train at that station. Maybe.

But on the other hand, it doesn't make sense to simplify to route level, since routes being straight lines, their TrainRanks would probably end up forming something close to a [normal distribution](https://oatzy.github.io/2010/12/08/normal-icicles.html) - the middle station having the highest probability, and decreasing towards the ends.

Just some thoughts, anyway.

Oatzy.
