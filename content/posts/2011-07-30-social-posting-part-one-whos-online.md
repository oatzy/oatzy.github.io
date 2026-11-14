---
layout: post
title: 'Social Posting - Part One: Who''s Online?'
date: '2011-07-30T20:14:00Z'
author: Oatzy
tags:
- graph
- nerd
- sociology
- infographic
- twitter
- tweets
- facebook
- maths
- modelling
- network
modified_time: '2011-07-30T13:14:53.294-07:00'
thumbnail: /images/social-posting-part-one-whos-online/M-def.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-1890510409807056422
blogger_orig_url: https://oatzy.blogspot.com/2011/07/social-posting-part-one-whos-online.html
---

**Coherence of Absence**

So imagine it's Sunday, there's nothing to do, nothing's open, nowhere to go, nothing on TV. So why aren't people spending all this free time online - tweeting, Facebooking, whatever?

Sunday is an online dead-zone.

A random hypothesis I thought up to explain this, posits that this may be the result of large numbers of people thinking "why post, if there's going to be no-one around to see it?". After all, no-one's around on Sunday. If they were, they'd be posting stuff.

I called it *Coherence of Absence*, because a fancy name can make a daft idea sound respectable. The alternative was *The Sunday Effect*.

Of course, it could be that people mostly social network when they're at work (procrastinating). Or maybe they're asleep/hungover on Sunday. Or have nothing to talk about, since Sundays are so boring. I dunno. I'm unemployed, so Sundays aren't much different to any other day of the week.

**In Other Words**

So this can be boiled down to two principles:

> **1.** People are likely to post more when there are more people online

> **2.** The number of people perceived to be online at any given time is based on who is posting

It's fairly intuitive that when there are more people online (posting), you'll post more - not just because there are more people to talk to - tweets to reply to, posts to comment on - but also because there's a bigger audience; more people to see what you have to say, regardless of how interesting or mundane that might be.

In essence, these two together create a feedback effect where your posting habits are based on your friends' posting habits, are based on (to some extent) your posting habits. And so on.

For point two, we can't generally say for sure whether or not someone is online, except for when they post something. Though there are exceptions. Of course, the irony of this model is that it assumes that everyone *is* online *all* the time - just waiting for someone else to indicate their presence with a post.

Don't get me wrong, I'm not saying this is definitely how the world works. This is more of a, let's suppose this is how it works - what then?

*NB/* the people a user follows are referred to as 'friends', since 'the people a user follows' is such a mouth full. These imaginary people may not, strictly speaking, consider each other friends.

**Technically**

Right, let's dive in: for some network of users, define a matrix M with entries

[![](/images/social-posting-part-one-whos-online/M-def.png)](/images/social-posting-part-one-whos-online/M-def.png)

For example

[![](/images/social-posting-part-one-whos-online/M-example.png)](/images/social-posting-part-one-whos-online/M-example.png)

NB/ connections between users needn't necessarily be two-way (except in the case of Facebook).

Next, we define a column matrix, T(n), with entries

[![](/images/social-posting-part-one-whos-online/T-def-1.png)](/images/social-posting-part-one-whos-online/T-def-1.png)

Now, we say that if at least one of a user's friends is posting, then the user will 'come online' and post in the next turn. Vice versa, if none of their friends are posting, then the user will 'go offline' and not post in the next turn.

To do this mathematically, we just [multiply the matrix](http://en.wikipedia.org/wiki/Matrix_multiplication) M by the matrix T. For example, if we start with only B online (blue),

[![](/images/social-posting-part-one-whos-online/graphs-example0.5.png)](/images/social-posting-part-one-whos-online/graphs-example0.5.png)

Then, as expected, all the people who follow B come online. B goes offline since none of the people they follow were online in the previous turn.

You'd then multiply M by T(1) to get T(2), M by T(2) to get T(3), and so on. Here's another example, starting with only A online,

[![](/images/social-posting-part-one-whos-online/graphs-example1.png)](/images/social-posting-part-one-whos-online/graphs-example1.png)

Easy.

**That's Not Normal**

The problem with the model so far is that there only needs to be one other person online for a user to join them. But one person online will be more significant to a person following 5 people, than to a person following 100.

So we might instead say, if at least half of a user' friends are online, then the user will join them in the next turn. First of all, we define a matrix, W, with entries,

[![](/images/social-posting-part-one-whos-online/W-def.png)](/images/social-posting-part-one-whos-online/W-def.png)

So for the example above, we get

[![](/images/social-posting-part-one-whos-online/W-example.png)](/images/social-posting-part-one-whos-online/W-example.png)

That is, the matrix M normalised so that the sum along each row equals 1. Our definition of T then becomes

[![](/images/social-posting-part-one-whos-online/Tni-defs.png)](/images/social-posting-part-one-whos-online/Tni-defs.png)

Which is just a fancy way of saying, if at least half of a user' friends are posting, then the user will post in the next term.

So, for example, if we start with A and D online,

[![](/images/social-posting-part-one-whos-online/graphs-example2-28weighted-29.png)](/images/social-posting-part-one-whos-online/graphs-example2-28weighted-29.png)

As before, everyone ends up online. But in this case, if we had started with only A online, then that means only a third of B' friends are online, so B wouldn't come online in the next turn. Nor would anyone else, for that matter - everyone ends up offline.

Of course, you could change it so that a user will come online if a third, or a fifth, or whatever of their friends are online. If you really wanted to.

**Weightlessness**

Of course, this supposes that a user cares about all their friends equally. In reality, we might care more about one person being around than another. There may even be people we don't care about at all (in terms of what we post), or people that we want to avoid.

The trick is this - instead of assigning everyone a 1 in the matrix M, let user i assign to each of their friends, j, some numerical weighting, based on how much i cares about j. If i prefers to avoid j, then this value may be negative.

Call this matrix W'. This matrix is, again, normalised to generate W, as before; making the sum along each row equal 1. The only difference is that with antagonists, some rows may add up to 0. So to avoid [division by zero](http://en.wikipedia.org/wiki/Division_by_zero) we have this

[![](/images/social-posting-part-one-whos-online/W-def-alt.png)](/images/social-posting-part-one-whos-online/W-def-alt.png)

At this point, I'll introduce the [equation](http://en.wikipedia.org/wiki/Recurrence_equation) for the model so far

[![](/images/social-posting-part-one-whos-online/coherence-eqn-simple.png)](/images/social-posting-part-one-whos-online/coherence-eqn-simple.png)

**Avoid the Antagonist**

So let's say this is our network now, with accompanying normalised-weighting matrix

[![](/images/social-posting-part-one-whos-online/antagonist-example.png)](/images/social-posting-part-one-whos-online/antagonist-example.png)

B has no qualms with A, but for whatever reason A harbors some secret dislike of B, and will typically want to avoid them. Why does A still follow B? Keeping up appearances, stalking? I dunno. Let's just pretend there's a good reason.

So, for example, if we start with A, C, and D online, here's what happens

[![](/images/social-posting-part-one-whos-online/graphs-example-antagonist.png)](/images/social-posting-part-one-whos-online/graphs-example-antagonist.png)

B comes online because both their 'friends are online. But B coming online effectively scares everyone else off, one by one. Admittedly, that's partly because I specifically chose weightings that would cause this to happen. But you get the idea.

Of course, once B goes offline, A might decide to come back online again, with D and then C following shortly after. At which point, we end up back at the start (1), where the cycle repeats.

**Can't Talk**

For this we go back to the first graph above, weightings all the same. Say one or more of the users go offline - maybe they're out on the town, or asleep, or something of that sort. What then?

If we take just one person offline, then nothing will happen to any of the other users - except if you remove B, in which case only A goes offline. So in the below example we take C and D offline (red)

[![](/images/social-posting-part-one-whos-online/graphs-example-removed.png)](/images/social-posting-part-one-whos-online/graphs-example-removed.png)

By (4) everyone is offline, so that when D comes back online at (5) there's no-one else online to keep them around. And D alone isn't sufficient to bring anyone else back online.

**Wait For It**

So this is a very simplified model. For one thing, it only considers people as either online or offline - or if you prefer, posting or not posting. It also assumes that, in the absence of an 'audience', a person won't post. And that leads to the implication that a social network can be destroyed by strategically removing users. It can't. I don't think.

Anyway, til next time..

Oatzy.
