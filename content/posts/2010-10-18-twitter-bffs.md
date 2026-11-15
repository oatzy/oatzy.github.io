---
layout: post
title: Twitter BFFs
date: '2010-10-19T00:32:00Z'
author: Oatzy
tags:
- graph
- nerd
- sociology
- infographic
- twitter
- tweets
- maths
- modelling
- network
modified_time: '2010-10-18T18:22:25.784-07:00'
thumbnail: /images/twitter-bffs/geo-mean.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-9072327518134110595
blogger_orig_url: https://oatzy.blogspot.com/2010/10/twitter-bffs.html
---

**Mentions**

So if you wanted to make a very basic [BFF](http://en.wiktionary.org/wiki/BFF) app, you would probably take the means of the numbers of mentions between a user and each of their followers, then pick out, say, the 5 highest.

So maybe define *R(a,b)* for [two users](http://en.wikipedia.org/wiki/Alice_and_bob) as the number of times *'Alice'* mentions '*Bob*', and R(b,a) vice versa (assuming that both counts are taken over the same period of time).

In this instance, I would probably go with the [geometric mean](http://en.wikipedia.org/wiki/Geometric_mean),

[![](/images/twitter-bffs/geo-mean.png)](/images/twitter-bffs/geo-mean.png)

since this would weed out any one-sided relationships by making the result zero.

You'd probably also want to factor in whether they're following each other, so define

[![](/images/twitter-bffs/fab.png)](/images/twitter-bffs/fab.png)

and multiply the mean by it. Or, in other words, make it zero if they don't both follow each other.

And that would suffice.

The only major downside to this is - imagine a pair of people who talk a massive amount, but all of what they say to each other is abusive. BFF wouldn't be the best way to describe them.

Unfortunately, unless you add "[sentiment analysis](http://en.wikipedia.org/wiki/Sentiment_analysis)" to the app - which is a little hit and miss at present - you're just going to have to assume everyone talks nice to each other.

**My BFFs**

Now, this is another situation where the best numbers aren't readily available - those ideally being:\
1\) date started following\
2\) total number of @replies since then

This obviously raises the same problems I talked about in the [previous](https://oatzy.github.io/2010/10/01/more-twitter-insights.html) post. But for demonstrative purposes, I'll use the number I can get.

So for this, I'm using [Twoolr](http://twoolr.com/), over the period Sept 1 - Oct 18 (48 days).

[![](/images/twitter-bffs/friend-table1.jpg)](/images/twitter-bffs/friend-table1.jpg)

Now a problem arises here. Twoolr seems to be missing a significant number of people for the second column, who I know for a fact have @replied me during that period. I don't know what's going on there, and unfortunately there's not much I can do to help it.

So the last column isn't really much use. But it could suffice to take, say, the top 5 and call them my Twitter BFFs over that 48 day period, if only so we have something vaguely resembling an answer.

Or alternatively I can just go [here](http://twitteranalyzer.com/ms.aspx?userId=oatz#), click on 'closest friends', and get this:

[![](/images/twitter-bffs/closest.jpg)](/images/twitter-bffs/closest.jpg)

Covering about 2 week. But then, that particular site's numbers haven't been entirely reliable in the past..

**Accounting for Rates**

Given that people tweet at [different rates](https://oatzy.github.io/2010/10/02/follow-up-women-really-do-tweet-more.html) - and may talk a lot with almost all their follows - it would probably make sense to take this into account.

For this I would probably say take

[![](/images/twitter-bffs/reply-fract.png)](/images/twitter-bffs/reply-fract.png)

i.e. the proportion of *Alice*'s total @replies that are directed at *Bob*. So for my numbers above the total is 525, and you'd divide everything through by that.

So then you can work that out for R(a,b) and R(b,a), take the geometric mean as before, multiply by 100 and your result should be a value between 0 and 100 vaguely indicating how 'close' *Alice* and *Bob* are.

Which sounds ridiculously straight forward. But that only works if you can get all the numbers. But that would require authorisation from both users in question, which in practice isn't easy.

Incidentally, this is why people are so desperate and willing to buy, sell and steal your personal data. It's valuable! Especially to marketing people.

**Improving the Results**

So there are other things you might want to include in the calculation to improve the 'quality' of the results. That is, there are other things we can measure that are also good indications of friendship and closeness.

Again, the absolute ideal way of working out how good friends people are would be to go through everything they send to each other (and not just on Twitter) to look at *what* exactly they're saying. But that's time consuming, and people tend not to like it when you invade their privacy and analyse what they say, to that great a degree.

1\) *Network*

Basically, how many friends *Alice* and *Bob* have in common. You could even go so far as to work out the biggest '[clique](http://en.wikipedia.org/wiki/Clique_%28graph_theory%29)' the two are part of - that is, the largest group *Alice* and *Bob* are in, such that everyone in that group are friends with each other.

[![](/images/twitter-bffs/net-map-with.png)](/images/twitter-bffs/net-map-with.png)So in general, you'd expect *Alice* to be closer friends with *Bob* than *Carol* if *Alice* and *Bob* have more friends in common - or are part of a large clique - than *Alice* and *Carol*.

I updated the network map (old version [here](https://oatzy.github.io/2010/07/31/follow-up-twitter-network.html)) to clarify this point, and also just because I can.

[![](/images/twitter-bffs/net-map-wo.png)](/images/twitter-bffs/net-map-wo.png)

[click to embiggen. Interactive version with me [here](http://manyeyes.alphaworks.ibm.com/manyeyes/visualizations/friend-network-1). Version without me [here](http://manyeyes.alphaworks.ibm.com/manyeyes/visualizations/friend-network-2).]

2\) *Retweets*

This tends to be better at showing how interesting a user finds another's tweets. So if you did decide to include it, you probably wouldn't give it much weight.

But at the same time, one would like to believe that - if for example someone you liked and someone you were indifferent to tweeted the same thing - you'd be more likely to retweet the person you liked. So it's mildly worth considering.

3\) *Follow Friday*

Like retweets, this *can* indicate how interesting a user is as much as it can indicate friendship. Ideally, you'd want to consider the reason (if any) accompanying the \#FF tweet.

4\) *Lists*

This is another one that's only useful if you can interpret how the lists are defined. Being on a list called "arseholes" for example, doesn't exactly suggest friendship.

But as I say, if you don't want things to get over-complicated, you can just ignore all the above.

**The Friendliest Tweeter**

If you want to be really clever, you could work out the numbers for all of a user's followers, then combine them (in some way) to get a '*friendliness score*' for that user.

Which is nice, because it would give people a way to compete over who's the friendliest (with their follows/followers).

Possibly more on that in a later post.

And yes, the title was a bit of a cheat since I can't actually tell you who my Twitter BFFs are. Sorry.

Oatzy.
