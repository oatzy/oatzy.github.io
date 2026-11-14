---
layout: post
title: 'Tumbling, Part One: Some Background'
date: '2011-06-25T21:49:00Z'
author: Oatzy
tags:
- doctor who
- graph
- sociology
- infographic
- maths
- network
- tumblr
- viruses
modified_time: '2011-06-28T18:07:41.189-07:00'
thumbnail: /images/tumbling-part-one-some-background/milkthing-graph.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-7772781446703186398
blogger_orig_url: https://oatzy.blogspot.com/2011/06/tumbling-part-one-some-background.html
---

I've talked about *Tumblr* [before](http://oatzy.blogspot.com/2010/12/quick-look-tumblr-reblogs.html), and I've [talked about](http://oatzy.blogspot.com/2010/09/social-viruses.html) using epidemiology models as an analogue for the spread of 'information' on social networks.

And having spent a fair amount of time on *Tumblr* recently, I have more insights, and more to say on the subject.

**Resummarising**

First of all, *Tumblr* is like *Twitter* in that a post can be spread from person to person by *reblogging* (similar to retweeting on *Twitter*). But more importantly, for a normal person like me, you will find that you'll get far more reblogs than you can ever get retweets. And this is important because it gives you more data to work from.

The key here is that you're typically sharing pictures. And in particular, often pictures that fall into certain fandoms - Tumblr is very good at fandoms. So if you post a picture relating to *Doctor Who*, then it will attract the attention of *Doctor Who* fans, who may like it and want to reblog it.

**An analogy**

Imagine there is some air born contagious disease, BUT it only affects men. Women can't even act as carriers.

Now imagine some guy has the disease. In a normal population, you have an approximately even mix of men and woman, so if the disease spreads, it will spread relatively slowly.

But this guy was just on holiday from his all boys boarding school. So when he goes back after the summer - can you see where this is going?

The fact that it's all boys, who are generally in close proximity, means that the disease is likely to spread through the boarding school like wildfire, infecting (almost) every boy.

(There could still be boys that are resistant to the disease, after all.)

Oh, and for completeness, if this infective guy were instead amongst a group of all women, then the disease wouldn't spread at all. But that should go without saying.

**Birds of a Feather**

If you are a massive *Doctor Who* fan, and if a huge chunk of what you post on Tumblr is *Doctor Who* related, then you are going to attract followers that are *Doctor Who* fans. You're likely to follow other *Doctor Who* fans yourself.

So it is, that subscribers to a given fandom with tend to cluster together, forming (relatively) tightly knit communities. If you then post a particularly popular ('contagious') image, then it will spread through the fandom like wildfire, as per the analogy.

Obviously, varying degrees of contagiousness still apply; fandom or not, a crappy picture isn't going to get much attention.

And on the other side of the coin, if you were then to post an image relating to a different fandom, which doesn't strongly overlap with *Doctor Who*, then the post will spread slowly, if at all.

**Big Milk Thing**

So I posted [this](http://oatzy.tumblr.com/post/6251885968) image shortly after *[A Good Man Goes to War](http://en.wikipedia.org/wiki/A_Good_Man_Goes_to_War)* aired. When I last checked, it had achieved a respectable *1,431* notes -\> *591* likes, and *840* reblogs.

One of the problems with *Tumblr* is that it doesn't time stamp reblogs. So, unless you're willing to put in the effort to keep track by hand, you can't get good *'spread over time'* data.

So what I did instead was work with '*spread over eccentricity*'. Here's a network graph to help illustrate

[![](/images/tumbling-part-one-some-background/milkthing-graph.png)](/images/tumbling-part-one-some-background/milkthing-graph.png)

The nodes are coloured by their distance (eccentricity) from me, going from red (closest), to blue (furthest away) - I'm the reddest dot, in the middle of the circular cluster near the top.

So what we can do is count how many pople are at each distance from me - equivalent to assuming that eccentricity is time linked. Which it isn't, but it's the best we have.

So here's the graph of that spread

[![](/images/tumbling-part-one-some-background/milkthing-soe.png)](/images/tumbling-part-one-some-background/milkthing-soe.png)

And reassuringly, it bears some similarity to epidemiology graphs - it hits at tipping point at the third generation causing a massive burst of reblogs, then slowly dies out; albeit with a secondary hump after generation 5.

You can actually see why the tipping points happen by the clusters in the network graph - the biggest super-node, *[matt-smith-](http://matt-smith-.tumblr.com/)*, exposed the image to a massive audience of *Doctor Who* fans.

Similarly in generation 5 with *[fuckyeahdrwho](http://fuckyeahdrwho.tumblr.com/)* - the second largest circular cluster - though the effect was smaller, arguably because a large number of people had already seen it at that point.

**Bar Graph of My Favorite Pies**

For contrast, here's what the network graph looks like for a *How I Met Your Mother* [image](http://oatzy.tumblr.com/post/6776420700) I posted

[![](/images/tumbling-part-one-some-background/himym-graph.png)](/images/tumbling-part-one-some-background/himym-graph.png)

In this case most of the spread is directly from me - as the original poster I act as a de facto super-node, as is the case with most posts. The post also doesn't spread very far this time, and in fact starts to die out straight away - as seen in the graph below.

[![](/images/tumbling-part-one-some-background/himym-soe.png)](/images/tumbling-part-one-some-background/himym-soe.png)

One could argue that, if the image were found by a *HIMYM* fan blog, it would have seen a resurgence similar to that for the *Dr Who* image. But on the other hand, I've had *Scrubs* [images](http://oatzy.tumblr.com/post/6790387858) reblogged by fan blogs, and still not seen them spread as much as the *Dr Who*,

[![](/images/tumbling-part-one-some-background/scrubs-graph.png)](/images/tumbling-part-one-some-background/scrubs-graph.png)

In this case, the image was reblogged by *[fyscrubs](http://fyeahscrubs.tumblr.com/)* - the bottom 'super-node' - and it still didn't spread very far.

So I think it's fair to say that *HIMYM* and *Scrubs* fans are (in general) less 'intense', and less numerous than *Doctor Who* fans. Or at least so on *Tumblr*.

*<strong>[edit]</strong>* - Shortly after I posted this blog, [an image](http://oatzy.tumblr.com/post/6689947433/the-hand-of-fear-sarah-jane-dont-forget-me) I posted last week - that had garnered very little attention until now - hit a super-node. And as with the *Dr Who* example, it exploded with likes and reblogs. So that's arguably points against a '*spread over time*' approach. If only because it's too unpredictable.

So that's that. In [Part 2](http://oatzy.blogspot.com/2011/06/tumbling-part-two-over-threshold.html) and [Part 3](http://oatzy.blogspot.com/2011/06/tumbling-part-three-stochastic-spread.html) of this series, I'll be looking at creating a mathematical model of the information spread discussed here.

Oatzy

[For the record, captioned screencaps aren't the *only* things I post on *Tumblr*.]
