---
layout: post
title: Twitter Friend Network
date: '2010-07-31T00:53:00Z'
author: Oatzy
tags:
- graph
- infographic
- twitter
- network
modified_time: '2010-07-30T18:24:17.655-07:00'
thumbnail: /images/twitter-friend-network/follow-network.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-62057509465484766
blogger_orig_url: https://oatzy.blogspot.com/2010/07/twitter-friend-network.html
---

I'll get to the technical stuff shortly. All you need to know right now is that this is a network map showing who follows each other.

[![](/images/twitter-friend-network/follow-network.png)](/images/twitter-friend-network/follow-network.png)

Size of the bubbles is proportional to the number of links to it.

That big blob in the middle that everyone's connected to is me, obviously. It should be labelled, but, apparently it hates me.

Oh, and that's just a screen shot up there. The real, interactive version is [here](http://manyeyes.alphaworks.ibm.com/manyeyes/visualizations/friend-follows-2).

Okay, so what happened was I was playing with the [Twitter API for Python](http://code.google.com/p/python-twitter/). I already had this idea - for the people I follow, who follows who (within that group)? Now when I first thought of the idea, I thought I'd have to go through everyone by hand. So thank God for the API.

What the code does [you can find it [here](https://github.com/oatzy/question-nobody-asked/blob/main/twitter-friend-network/twitterFollows.py) if you're interested] is retrieve a list of the people I follow, then for each user checks which of the other users in the list they follow. Then outputs the result.

I know, that's basically what I said up there. But it really is that straight forward.

Well, it actually wasn't that straight forward. For some reason it missed out some connection that I know were there. In particular, Charlie Brooker was causing a few problems (and I'll be damned if I know why).

But I tried my best to make do, and the first graph was a complete and utter mess - the celebrities were causing too much 'noise'. It was obscuring the graph.

So once I'd removed the celebrities, Charlie's delinquency wasn't a problem anymore. That being said, I did have to go through the list afterwards making a few corrections. And there may still be errors in the data. If you spot any, please let me know.

And that's pretty much it.

But while I'm on the subject, the website I used to build the graph was [ManyEyes](https://web.archive.org/web/20100731103237/http://manyeyes.alphaworks.ibm.com/manyeyes/) [brought to you by IBM]. It does a crap load of different graphs and infographical goodness, and it's definitely worth checking out and having a play with.

So yeah. Enjoy. And if you make any fancy graphs of your own, please do share.

Oatzy.

[edit] - I created a more stripped down [version](http://manyeyes.alphaworks.ibm.com/manyeyes/visualizations/friend-follows-3) by removing the people who never tweet. It looks a lot more clear.
