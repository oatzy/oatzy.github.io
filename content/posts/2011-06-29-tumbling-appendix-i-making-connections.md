---
layout: post
title: 'Tumbling, Appendix I: Making Connections'
date: '2011-06-29T20:19:00Z'
author: Oatzy
tags:
- graph
- programming
- nerd
- python
- infographic
- flowchart
- maths
- modelling
- network
- tumblr
modified_time: '2011-06-29T13:31:06.124-07:00'
thumbnail: /images/tumbling-appendix-i-making-connections/updated-model-flow1.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-8970070352313300423
blogger_orig_url: https://oatzy.blogspot.com/2011/06/tumbling-appendix-i-making-connections.html
---

**Where Things Get Interesting**

Recall in [Part 3](https://oatzy.github.io/2011/06/29/tumbling-part-three-stochastic-spread.html) (under '*Notes and Improvements*'), I mentioned the possibility of creating graphs of *how* a post spreads - ie who reblogged who.

As it turns out it was possible. And in fact, not that difficult.

You can find the modified code [here](https://github.com/oatzy/question-nobody-asked/blob/main/tumbling-appendix-i-making-connections/tumblr.model.2.py).

In addition to the outputs the previous iteration generated, this updated version also creates a '*graph.csv*' file, which contains all the links between reblogging users. This file can then be imported into, for example, [Gephi](http://gephi.org/), to create a visualisation of the graph.

**Modified Model**

The updated model works thing like this

[![](/images/tumbling-appendix-i-making-connections/updated-model-flow1.png)](/images/tumbling-appendix-i-making-connections/updated-model-flow1.png)

We have the set, *F*, of people who reblogged in the previous generation. For each of these users we iterate over their followers, with the reaction code as before.

But we now have the addition that, if the follower reblogs, a new property - *user.reblogged* - is set to the person they reblogged from. That (reblogging) user is then added to the temporary group *f_i* to be used in the next iteration.

The simulation ends when *f_i* is empty - ie, no-one reblogs.

**Pretty as a Picture**

So, keeping the initial conditions the same as for [Part 3](https://oatzy.github.io/2011/06/29/tumbling-part-three-stochastic-spread.html), here is an example output

[![](/images/tumbling-appendix-i-making-connections/sample-graph.png)](/images/tumbling-appendix-i-making-connections/sample-graph.png)

And here if the accompanying '*spread over eccentricity*' graph.

[![](/images/tumbling-appendix-i-making-connections/sample-flow.png)](/images/tumbling-appendix-i-making-connections/sample-flow.png)

Compare for those visualisations in [Part 1](https://oatzy.github.io/2011/06/25/tumbling-part-one-some-background.html)

I have to say, I am extremely pleased with this. I mean, just look at it! It's amazing.

Here's another example

[![](/images/tumbling-appendix-i-making-connections/sample-graph3.png)](/images/tumbling-appendix-i-making-connections/sample-graph3.png)

[![](/images/tumbling-appendix-i-making-connections/sample-flow3.png)](/images/tumbling-appendix-i-making-connections/sample-flow3.png)

And finally, here's a graph for a population size, *N* = *20,000 & f0 = 1,000*

[![](/images/tumbling-appendix-i-making-connections/sample-graph5-1.png)](/images/tumbling-appendix-i-making-connections/sample-graph5-1.png)

More reblogs overall, and lots more clustering in this case. Pretty awesome, right?

**Little Niggles**

The only things that really bother me now:

1\) The Like count seems a little high\
This is probably a result of the distribution/variables chosen in creating approval thresholds.

2\) There's only a small number of reblogs coming from OP.\
This relates to the '*reblogs from tags*' thing discussed in [Part 3](https://oatzy.github.io/2011/06/29/tumbling-part-three-stochastic-spread.html).

3\) Small population\
At some point, when I've got the time to run the simulation, I'd like to try it with larger populations/larger *f0*

But none of these things bother me too much, and I'm pleased with what I've got.

So that's basically that.

Oatzy.
