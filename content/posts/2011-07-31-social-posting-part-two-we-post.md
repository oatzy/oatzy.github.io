---
layout: post
title: 'Social Posting - Part Two: We Post Together'
date: '2011-07-31T19:05:00Z'
author: Oatzy
tags:
- graph
- sociology
- infographic
- twitter
- tweets
- facebook
- maths
- modelling
- network
- tumblr
modified_time: '2011-07-31T12:07:51.373-07:00'
thumbnail: /images/social-posting-part-two-we-post/coherence-eqn-full-alt.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-8452815325099463455
blogger_orig_url: https://oatzy.blogspot.com/2011/07/social-posting-part-two-we-post.html
---

**Where were we..**

So the main limit to the stripped down model in the [previous post](https://oatzy.github.io/2011/07/30/social-posting-part-one-whos-online.html) is that it only puts people into one of two states - posting, or not posting.

A more realistic model would take into account how much people are posting. The nice thing is, the change to the model is only minor - T no longer has the condition that makes its value has to be either one or zero.

The values T_i now represents the post rate of each user - that is, the number of posts posted during some arbitrary time period, n.

Here is the full, modified equation for the model

$$ T(n) = \alpha \cdot W \cdot T(n - 1) + \beta $$

**Two More Things**

As you've probably noticed, we've introduced two new variables. They are:

**2**) *<strong>Beta</strong>*

Beta is a [column matrix](http://en.wikipedia.org/wiki/Column_matrix), with values represent each user's baseline post rate - that is, the rate at which a user would post if there was no-one else online - no audience, no-one to talk to.

**1**) *<strong>Alpha</strong>*

Alpha is a little more complicated. But loosely speaking, its values relate to the upper limit of each user's post rate (ignoring external effects).

It works like this: first, imagine everyone has some maximum post rate. Tbar (T with a line over the top) is the column matrix of these values. Now, suppose everyone is posting at their maximum rate. Alpha values are calculated by rearranging the model equation, thus

$$ \alpha_i = \frac{\bar{T}_i - \beta_i}{W_i \cdot \bar{T}} $$

Any negative values in W are set to 0, since (in theory) a user has their highest post rate when any of their antagonist are not online.

What this means, is that post rates are capped by their appropriate upper limits; when all members of the population reach their maximum post rates, we find that T(n) = T(n-1) for all n - i.e. the post rates all remain constant, unless externally affected.

For technical reasons alpha is a [diagonal matrix](http://en.wikipedia.org/wiki/Diagonal_matrix).

Alpha and Beta look like this

$$ \alpha = \begin{pmatrix} \alpha_1 & 0 & 0 & 0 \\ 0 & \alpha_2 & 0 & 0 \\ 0 & 0 & \alpha_3 & 0 \\ 0 & 0 & 0 & \alpha_4 \end{pmatrix} \qquad \beta = \begin{pmatrix} \beta_1 \\ \beta_2 \\ \beta_3 \\ \beta_4 \end{pmatrix} $$

They won't all ways be size 4, of course. Their size will depend on the size of each particular network. The values of alpha and beta could vary over time, but for all intents and purposes, it will suffice to hold them constant.

**Rainbow Graphs**

Going back to the graph from last time, we might get a system equation like this

[![](/images/social-posting-part-two-we-post/stationarypoint-example-proper.png)](/images/social-posting-part-two-we-post/stationarypoint-example-proper.png)

In this full model, it's not just a matter of online or offline. So instead of a series of network graphs, we represent the progression of a network as a set of line graphs.

What we find then is that the system described by this equation seems to tend towards some constant, stable point - regardless of initial conditions.

For example, with the equation described above, and starting at T(0) = [1,0,0,0] we get

[![](/images/social-posting-part-two-we-post/converge-below.png)](/images/social-posting-part-two-we-post/converge-below.png)

And even if we start from T(0) = [100, 100, 100, 100], we get

[![](/images/social-posting-part-two-we-post/converge-above.png)](/images/social-posting-part-two-we-post/converge-above.png)

In each case, the system converges to [15, 10, 5, 10] - Tbar - the maximum rates set when defining the variables for this system.

Interestingly, here's what happens when you set beta = 0 for all users - alpha values recalculated as [1.5, 1.11, 0.5, 1.11]

[![](/images/social-posting-part-two-we-post/converge-below-nobeta.png)](/images/social-posting-part-two-we-post/converge-below-nobeta.png)

You get this weird bouncing about. It does seem like they're converging towards some fixed points. And it's converging to points roughly in proportion to Tbar, though much lower.

In fact, in online/offline form, the system looks like this

[![](/images/social-posting-part-two-we-post/nobeta-bounce.png)](/images/social-posting-part-two-we-post/nobeta-bounce.png)

It's this early jumping on and off -line that causes the system to oscillate at first, before starting to settle down as time goes on.

We also see that, because the system starts much lower than its defined stationary point (Tbar), and because it doesn't have the boost of the base-rates, the actual stationary point the system is converging to is much lower.

If, however, T(0) were set to Tbar, then the system would have stayed constant at Tbar. Similarly, if T(0) were set to [0,0,0,0], then the system would stay there, since it wouldn't have the base-rates to get any of them off the ground.

**Antagonistic Altercations**

If we set up an antagonist system like that in the last post - with beta and Tbar as above, and conjugate alpha - we get a line graph that looks like this

[![](/images/social-posting-part-two-we-post/antagonist-lastpost.png)](/images/social-posting-part-two-we-post/antagonist-lastpost.png)

In this case, the base-rates act to temper A's dislike of B, so that B stays online; though the result is that the stable point is lower than the maximum for everyone. The stable point for A is lowered the most.

But if we remove the base-rates (and recalculate alpha accordingly), the system progresses much like it did last time

[![](/images/social-posting-part-two-we-post/antagonist-lastpost-nobeta.png)](/images/social-posting-part-two-we-post/antagonist-lastpost-nobeta.png)

That is, as soon as B shows up, A leaves - eventually followed by everyone else.

**Upping The Tension**

Now, what if we change the setup so that A and B both want to avoid each other.

One might question why two people who dislike each other would be 'friends' (in the social networking sense). I dunno. This is a hypothetical situation meant to demonstrate a point, god damn it!

Here's the system equation

[![](/images/social-posting-part-two-we-post/antagonist-ratemap.png)](/images/social-posting-part-two-we-post/antagonist-ratemap.png)

Matrix of maximums, Tbar, stays the same as above at [15,10,5,10].

So if we set T(0) = [0, 10, 5, 10], here's what happens

[![](/images/social-posting-part-two-we-post/antagonist-rate-graph.png)](/images/social-posting-part-two-we-post/antagonist-rate-graph.png)

A comes online because of their base-rate, and once they do, B disappears. Here's this system's initial and stable points

[![](/images/social-posting-part-two-we-post/antagonist-stablepoint.png)](/images/social-posting-part-two-we-post/antagonist-stablepoint.png)

In antagonistic systems such as this and the one before, Tbar isn't a stable point.

In this case, for example, the peak rate for A occurs when B is offline and C is at their peak rate. But C is at their peak rate when both A and B are online. So if B is offline, C can't be at their peak rate, and as a result neither can A. And vice versa. So Tbar can't be achieved, since the tension between A and B pushes down the rates of everyone, themselves included.

The system does still stabilise however. It just to stabilises with B offline, and everyone else at a slightly lower rate in this case.

Now, if we do as we did in the previous blog, and take A offline (indefinitely), here's how the system evolves

[![](/images/social-posting-part-two-we-post/antagonist-rate-graph-noA.png)](/images/social-posting-part-two-we-post/antagonist-rate-graph-noA.png)

In this case, the stable rates of C and D are lower than they were when B was 'forced' offline by A. And even though A isn't online, B isn't posting at their maximum rate.

**Exogenous Effects**

So as before, we also have to consider external effects.

People can suddenly, and unexpectedly disappear - maybe fall ill, get a job, or just not post for a while. Conversely they could find themselves in a situation where they're posting more - maybe because of a major news event, or because they're at work (procrastinating).

We can quite easily create these effects artificially, then observe how the model responds to that change. For example, we could gauge a person's importance (to a network) by removing them and seeing how dramatic an effect that has.

So in the antagonist examples above, we could say that A is more important to that network than B, since removing B had a greater (negative) effect on the C and D.

For this, we define some arbitrary function, E(n). We then multiply our model equation by this function

$$ T'_i(n) = E_i(n) \cdot T_i(n) $$

So for the example last time, where we removed two users C and D, then later reintroduced C, the function(s), E(n), might look like this

$$ \begin{aligned} E_1(n) &= \{\, 1 \;\; : \;\; n \ge 0 & \qquad E_2(n) &= \{\, 1 \;\; : \;\; n \ge 0 \\[1ex] E_3(n) &= \begin{cases} 0 & : \;\; 1 \le n \le 3 \\ 1 & : \;\; \textit{otherwise} \end{cases} & \qquad E_4(n) &= \begin{cases} 0 & : \;\; 1 \le n \le 5 \\ 1 & : \;\; \textit{otherwise} \end{cases} \end{aligned} $$

Or, if some major news story broke between n=2 and 5, then the function might look like this

$$ E_i(n) = \begin{cases} 3 & : \;\; 2 \le n \le 5 \\ 1 & : \;\; \textit{otherwise} \end{cases} \qquad \forall\, i $$

So, if we were to, say, remove A (indefinitely) from the top system above, then the result would look like this

[![](/images/social-posting-part-two-we-post/converge-below-noA-1.png)](/images/social-posting-part-two-we-post/converge-below-noA-1.png)

The important thing to note here is that even though B is the only person directly linked to A in the network, removing A from the graph lowers the rates of *everyone*.

Alternatively, we could double A

[![](/images/social-posting-part-two-we-post/converge-below-2A.png)](/images/social-posting-part-two-we-post/converge-below-2A.png)

In this case, multiplying A by two brings everyone else's stable points up. It's also worth noting that A' stable point isn't just doubled, but multiplied by 2.7. This is a good example of the feedback effect mentioned at the start of the previous blog - increasing A' rate increases everyone else's rates, increases A' rate.

Or if we half A

[![](/images/social-posting-part-two-we-post/converge-below-halfA.png)](/images/social-posting-part-two-we-post/converge-below-halfA.png)

In this case, everyone else' rates drop too, and A's rate stabilises at less than half it's maximum.

**Agitated Antagonist**

So what if we go back to our antagonist system, and start poking it..\.

First of all, if we half A

[![](/images/social-posting-part-two-we-post/antagonist-rate-graph-halfA.png)](/images/social-posting-part-two-we-post/antagonist-rate-graph-halfA.png)

Then B is able to stay online, but with a stable point much lower than their maximum.

But, here's where things get interesting - if instead we double B, here's what happens

[![](/images/social-posting-part-two-we-post/antagonist-rate-graph-2B.png)](/images/social-posting-part-two-we-post/antagonist-rate-graph-2B.png)

This time, they each scare each other off. *But*, once the other goes offline, they each come back in the next turn, only to scare each other off again. And so on. And all this jumping between extremes makes C and D jump about as well, but half a cycle out of sync.

At least, that's what happens for initial conditions [0, 10, 5, 10]. If we start with all at 0, the behaviour is nearer to that with no external effects.

**In General**

So it seems to be the case that externally changing one user affects (almost) everyone in the graph.

That being said, I would[](http://en.wiktionary.org/wiki/guess) expect that when the model is generalised to much larger networks, we would find that the greater the distance between two users, the less affect they will have on each other.

It probably stands to reason then that, for a given user, it's only worth considering a graph as wide as friends of friends. Maybe friends of friends of friends for (a collection of) dramatic changes at that distance.

More in general, when you apply the model to a system of more than four people (as we've looked at here), you would expect things to get more complicated.

But the overall results should be similar - that is, in most cases the system will tend towards some stable state. It may just take longer to reach that point, depending on the size of the graph.

**In Conclusion**

So the long and short of it is this - in most cases, a group's post rates will typically converge towards some stable point.

If there aren't any antagonists, and if the base-rates aren't zero for everyone in the network, then the stable state will typically be the common maximum, Tbar. Otherwise, the system may oscillate, or else become stable at a much lower set of rates.

If we set all base-rates to 0, we find that the systems behave much like they did in the simplified online/offline model discussed in the previous blog; with some quirks of their own.

In the absence of base-rates, or in the presence of antagonists, initial conditions become important, affecting if and where the system stabilises.

When we consider external effects, the same will tend to be true - but with the stable points altered, according to what that effect is.

Modifying one user affects everyone else in the graph (to some degree). Modifying different users will have different effects on the rest of the graph, depending on the 'importance' of that user.

Of course, in the real world, external effects are unpredictable, and will tend to keep the system off-balance (unstable). But we do what we can.

Oh, and if you were wondering how I got the numbers for the graphs, [here's](https://github.com/oatzy/question-nobody-asked/blob/main/social-posting-part-two-we-post/coherence.py) the code I used. But be forewarned, it's very sloppy.

Oatzy.

[..and the fundamental interconnectedness of all users[.](http://en.wikipedia.org/wiki/Dirk_Gently)]
