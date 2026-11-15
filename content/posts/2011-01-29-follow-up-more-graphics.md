---
layout: post
title: 'Follow Up: More Graphics'
date: '2011-01-29T21:49:00Z'
author: Oatzy
tags:
- statistics
- graph
- infographic
- snakes and ladders
- network
modified_time: '2011-01-29T13:49:59.779-08:00'
thumbnail: /images/follow-up-more-graphics/sl-board-graph.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-7253103867730393928
blogger_orig_url: https://oatzy.blogspot.com/2011/01/follow-up-more-graphics.html
---

I'm sticking these in a new post, rather than updating the [last post](https://oatzy.github.io/2011/01/29/snakes-and-ladders.html) (and potentially, nobody seeing them).

First of all, as I said yesterday, the 'entrance' squares of the snakes and ladders don't technically exist; in so much as, as soon as you land on them you move to the coresponding exit. So I updated the network graph to reflect this

[![](/images/follow-up-more-graphics/sl-board-graph.png)](/images/follow-up-more-graphics/sl-board-graph.png)

But this version isn't quite as aesthetically pleasing as the other one. Still, at least no-one can accuse me of not doing it right.

And as you'd probably expect, the number of curves directed into a given square's node in the above graph is loosely related to the probability of visiting that square

[![](/images/follow-up-more-graphics/indegree-sim-comp.png)](/images/follow-up-more-graphics/indegree-sim-comp.png)

And the other thing is, I wasn't happy with the board histogram - the bar chart of how often you land on each square. So I played with it a bit, to try and find the clearest, prettiest, and most easy to interpret representation of the data.

This is what I came up with

[![](/images/follow-up-more-graphics/Snakes-and-ladders2.png)](/images/follow-up-more-graphics/Snakes-and-ladders2.png)

The numbers for entrances and exits are stacked, so you can see how often a given exit square is visited in total, and what proportion of those visits are from moving along a snake or ladder.

For example, there's about a *47%* chance of getting to the end via the *80-100* ladder.

The arcs show which squares are linked.

Oatzy.
