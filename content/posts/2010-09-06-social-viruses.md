---
layout: post
title: Social Viruses
date: '2010-09-06T22:24:00Z'
author: Oatzy
tags:
- graph
- celebrities
- sociology
- twitter
- tweets
- modelling
- network
modified_time: '2010-09-07T03:53:28.700-07:00'
thumbnail: /images/social-viruses/25things.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-8862965883406397712
blogger_orig_url: https://oatzy.blogspot.com/2010/09/social-viruses.html
---

In online social networks, ideas can spread between users like viruses. Literally. And this means that [mathematical models](http://en.wikipedia.org/wiki/Modelling_in_Epidemiology) of epidemics can be applied directly to the spread of memes, tweets/RTs, links, news, viral marketing, etc.

**25 Random Things**

The first example is the "*25 things*" meme that was going around Facebook a short while back. How it worked was, a user would write \`25 random things\` about themself then 'tag' 25 friends.

In the wake of this phenomenon, [Slate.com](http://www.slate.com/id/2211068) took a survey of a number of users, asking them when they first encountered the meme and if and when they participated.

This information was then sent to a biology professor, who used it to model the spread of the meme through Facebook, using the ([previously mentioned](http://oatzy.blogspot.com/2010/09/modelling-zombie-apocalypse.html)) SIR model.

[![](/images/social-viruses/25things.png)](/images/social-viruses/25things.png)

Now what's particularly special and nice about the "*25 things*" is that, because of the tagging, the contact rate is 25 - i.e. each 'infected' individual tried to pass the 'infection' on to 25 other people.

And what the modelling found was that on average 1.27 of those 25 people would become 'infected' themselves. Which is a nice example and a nice demonstration of how the spread of memes resembles the spread of viruses.

**Brighten Up Your Day..**

*..by moving at least one of Tony Blair's books to the crime section in your local bookshop*

In particular here, I'm looking at the way tweets and memes spread through Twitter - such as the "*Crime-Section Blair*" and the "*Status Copy*".

One of the main differences between these two is that one was spread (primarily) by RTing, while the other was spread by direct copy/pasting. But for all intents and purposes, that difference doesn't have a significant effect on spreading.

The key difference between Twitter and Facebook is to do with contact rate and clustering.

In the "*25 things*" meme, the contact rate was a constant 25. But even in general Facebook users are, on average, in contact with about [150 people](http://www.physorg.com/news183791343.html) (friends). And generally, there's not that much variation from this average.

With Twitter, on the other hand, the people you might come into contact with varies *WIDELY*.

I tried looking up figures for average number of followers per user, but couldn't find one definitive answer. For demonstrative purposes, I'm going with the one from the [Guardian](http://www.guardian.co.uk/technology/blog/2009/jun/29/twitter-users-average-api-traffic) - 126.

Now I currently have about 100 followers, which is close to the 'average'. Stephen Fry, on the other hand, has 1,756,00 followers - 5 orders of magnitude larger, and a significant attenuation from the 'average'. And this degree of variation among users has a massive effect when trying to model spread on Twitter.

**An Analogy**

So take, for example, some air-borne virus - say, flu.

If '*patient zero*' stays relatively contained - equivalent of staying at home - the only people likely to catch the virus are those immediately around them.

If on the other hand '*patient zero*' goes to a mass-populated area - say a shopping centre, or a hospital - the virus will find more victims. And those victims will spread out and pass it on to more people, and the virus will spread more throughout the general population - an epidemic.

In this analogy then, the 'house' is equivalent to a relatively small and contained network of friends - for example, me and my small group of followers. A tweet is unlikely to spread much outside of my network.

Celebrities, on the other hand are the man in the shopping centre, or a 'care-giver' at a hospital - they expose the 'virus' to a large number of people. And anyone who's then 'infected' will carry that on to their own network. And then it may even spread out more from there.

So for a '*tweet epidemic*', a tweet/RT has to come into contact with one of these mass connectors (as [previously](http://oatzy.blogspot.com/2010/09/forced-trending-topics.html) [discussed](http://oatzy.blogspot.com/2010/09/six-degrees-and-how-we-met.html)).

**Sometimes I Just Want To Copy Someone Else's Status,..**

*..Word for Word, and See If They Notice.*

The major different between the "*Blair*" meme and the "*Copy*" meme, is that in the former, '*patient zero*' was a 'connector' - highly influential with lots of followers. So it's not that surprising that it spread.

[And it was also funny, which made it more ['contagious'](http://www.channel4.com/news/articles/politics/tony+blairaposs+book+takes+unexpected+journey/3759707).]

The problem with the "*Copy*" meme is that, by it's nature, it's harder to trace back to it's original source. [Know Your Meme](http://knowyourmeme.com/memes/sometimes-i-just-want-to-copy-someone-else%E2%80%99s-status) cites the first appearance<em>\*</em> as being on *August 26th* by @*Tim_Waters* - a Leeds man with 507 followers. Which isn't a significant number.

But not long after his initial tweet, it reached @*elspethjane* (3,100 followers) and a bit later *Dolly Parton* (722,000 followers) - so by this point it had reached epidemic, and was spreading like wildfire.

If you're a frequent Twitter (or even Facebook) user, no doubt you saw it at least once.

Anyway, all this complicates things - trying to model if and how a tweet will reach a connector. One could assume that in the case of the "*Copy*" meme, this came down to it's high 'contagiousness' - that it survived long enough to spread to one or more connectors.

**Visual Demonstration**

These are based on a [previous](http://oatzy.blogspot.com/2010/07/follow-up-twitter-network.html) graph of my Twitter follows. For this, we pretend that this small network is completely isolated.

In this first one, the red circle in the middle posts a tweet. The purple circles are the people who see that tweet:

[![](/images/social-viruses/graph-stripped-RT1.png)](/images/social-viruses/graph-stripped-RT1.png)

So the tweet is already reaching 7 people. Now if the node labelled 2 ReTweets, then only one more person will see it (total audience 8).

If node 1 RTs, then the tweet reaches an extra 3 people (10 people total). So in this case, 1 is more of a connector than 2.

For a better example of the importance of connectors, we have the below:

[![](/images/social-viruses/graph-stripped-RT2.png)](/images/social-viruses/graph-stripped-RT2.png)

Again, red tweets, purple are audience. So in this case, there's only an audience of 2. And if the node at the bottom RTs, it won't matter.

If the circled node RTs, though, the tweet will reach 2 more people - one of whom is a mass-connector, who could spread it to an additional 5 people, which could lead to it spreading even further.

So ultimately, the number of people following you is only as important as *who* those people are. The red circle may only have 2 'followers', but via the circled node, they could still reach all or most of the entire population, with little difficulty.

**Modelling Spread**

So it comes down to this - on Facebook, information or memes will spread fairly uniformly, following the SIR model.

And at it's most basic level, the spread of tweets can be sufficiently modeled by the SIR approach as well. Especially if the tweet doesn't encounter a mass-connector, and instead spreads through a population whose followers count is sufficiently close to that ~150 average.

For example, if I post something worth RTing, at best it's going to go maybe 2 generations out. And this *could* be described by the SIR equations. Though given degree of spread, it'd hardly be worth it.

The limitation of the SIR equations though, is that it assumes homogenous mixing of susceptible and infected - i.e. that everyone in the population has equal odds of being infected. But as with the analogy, on Twitter you get more clustering, so that's not necessarily the case.

Instead, you have to use [this](http://www.utexas.edu/features/archive/2003/meyers.html) approach, where you plot out a situation-specific network graph of the system - like the above diagrams - and work from that. And given that Twitter has in excess of 4 million users, that's a little beyond my resources and inclination<em>\*\*</em>.

But basically, if a tweet hits a connector, it will spread like swine-flu hysteria.

Oatzy.

\* [TechCrunch](http://techcrunch.com/2010/08/26/twitter-human-virus/) found an earlier example on the *19th of August* - a Bieber fan with 809 followers. It's hard to say if Tim wrote the (almost identical) tweet independent of her, or if she was the true 'patient zero'.

\*\* This guy crawled Twitter and got connections for most of the users (at the time of crawling). You can find this data, and his analysis, [here](http://an.kaist.ac.kr/traces/WWW2010.html).
