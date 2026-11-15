---
layout: post
title: 'Revisited: Tweets by Gender'
date: '2011-02-04T00:26:00Z'
author: Oatzy
tags:
- statistics
- graph
- gender
- infographic
- twitter
- tweets
modified_time: '2011-02-03T16:26:30.341-08:00'
thumbnail: /images/revisited-tweets-by-gender/rates-old.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-5396609866611142549
blogger_orig_url: https://oatzy.blogspot.com/2011/02/revisited-tweets-by-gender.html
---

So I first looked at this [here](https://oatzy.github.io/2010/10/01/more-twitter-insights.html), with a follow up [here](https://oatzy.github.io/2010/10/02/follow-up-women-really-do-tweet-more.html). The conclusion was that among the people I follow, the women do tweet more than the men.

So it's now about 4 months since that last post, so I thought I'd have a quick look at how things have changed.

As a quick recap for those too lazy to click the link above, here are the results from last time (now in graph form)

[![](/images/revisited-tweets-by-gender/rates-old.png)](/images/revisited-tweets-by-gender/rates-old.png)

If you want to know about the technical details, you *will* have to click the link.

And here are the new numbers

[![](/images/revisited-tweets-by-gender/rates-new.png)](/images/revisited-tweets-by-gender/rates-new.png)

It's pretty much the same deal, but it's there for those interested. And just to further clarify whatever point it is I'm trying to make, here's a [boxplot](http://en.wikipedia.org/wiki/Boxplot) comparison of the numbers (made in [R](https://web.archive.org/web/20090530041817/http://www2.warwick.ac.uk:80/fac/sci/moac/degrees/modules/ch923/r_introduction/boxplot))

[![](/images/revisited-tweets-by-gender/boxplot.jpg)](/images/revisited-tweets-by-gender/boxplot.jpg)

The three circles over the female's numbers are outliers. And once you factor out the outliers, you find the numbers are actually quite similar. But the middle quartiles (the box parts) are still slightly lower for the males.

The other thing I did, for the shear hell of it, was the rates for the last 4 months; the other graphs are 'lifetime' rates.

[![](/images/revisited-tweets-by-gender/rates-inter.png)](/images/revisited-tweets-by-gender/rates-inter.png)

You can get the dataset for all these numbers - as well as totals, days online, changes in rates, etc. - [here](https://spreadsheets.google.com/ccc?key=0AgfLII2ZglYqdGFueEFZOUZJZUZ4b0ZZcXhVd3BnLVE&hl=en&authkey=CNq6gIUP).

**What About Everyone Else?**

This isn't something I'm going to try and work out myself, because frankly it's not worth the amount of effort it would require.

So I googled it instead, and found [this](http://blog.hubspot.com/blog/tabid/6307/bid/5987/Data-Shows-On-Twitter-Women-Are-More-Social.aspx?source=BlogTwitter_%5BData%20Shows:%20On%20Twitt%5D)

[![](/images/revisited-tweets-by-gender/tweets.gif)](/images/revisited-tweets-by-gender/tweets.gif)

Apparently, on average women tweet *12%* more than men. That number is based on total number of tweets posted though, where mine are based on rate.

But [an article](http://blogs.hbr.org/cs/2009/06/new_twitter_research_men_follo.html) I linked in the first post suggested that men and women tweet at about the same rate.

So make of all this what you will.

Oatzy.

[If you see anything that looks like an error, leave me a comment and I'll look into it.]
