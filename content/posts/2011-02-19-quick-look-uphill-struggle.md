---
layout: post
title: 'Quick Look: Uphill Struggle'
date: '2011-02-20T00:07:00Z'
author: Oatzy
tags:
- statistics
- graph
- programming
- nerd
- python
- maths
- modelling
modified_time: '2011-02-19T17:51:15.641-08:00'
thumbnail: /images/quick-look-uphill-struggle/pickup-hist.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-368088204837233953
blogger_orig_url: https://oatzy.blogspot.com/2011/02/quick-look-uphill-struggle.html
---

When the parent's work schedules both coincide with a school day, it's often my displeasure to have to retrieve the small one from school. And because I don't drive, that's a *~30min* round trip, which involves a fairly [steep hill](http://runkeeper.com/user/oatzy/activity/24429951).

I don't much care for it.

I didn't [track](https://oatzy.github.io/2011/01/01/life-by-numbers-end-of-year-report.html) how many times that happened last year. But out of shear curiosity, and because I can, I tried modelling the set up to get an estimate.

You could probably work it out with probability alone. But that's too much like hard work.

**Assuming..\.**

Firstly, we assume I can randomise the parent's shifts - that is, there's no particular pattern to them. We also assume that their shifts are independent of each other and of school days and school holidays. That's not strictly true. But since there isn't a strong, underlying pattern linking them, we just ignore it.

Same goes for holidays, which in this model are also arranged at random. We can also ignore date, month, etc. because of the above assumptions and because it's just easier that way.

And finally, we ignore sick days, study days and over-time, since they aren't really predictable, and should hopefully average out over repeated trials.

I've also included a 10% chance that, for whatever reason, I *won't* have to pick the sister up. That number's just a random guess.

**Hand-waving explanation**

First you create three sets representing a year's worth of shifts for each of my parent and a year's worth of school. You then randomly delete a year's worth of holidays, bank holidays, and training days from the sets.

Finally, you count on how many days, shifts and school days coincide.

You can look at the code [here](https://github.com/oatzy/question-nobody-asked/blob/main/quick-look-uphill-struggle/pickup.py).

Since this is [another](https://oatzy.github.io/2011/01/29/snakes-and-ladders.html) random use of the [Monte Carlo method](http://en.wikipedia.org/wiki/Monte_carlo_method) - you run the model 10,000 times and then draw a histogram of the resulting counts.

**Hey Look!**

It's a [normal distribution](https://oatzy.github.io/2010/12/08/normal-icicles.html)

[![](/images/quick-look-uphill-struggle/pickup-hist.png)](/images/quick-look-uphill-struggle/pickup-hist.png)

Which isn't that [surprising](http://en.wikipedia.org/wiki/Central_limit_theorem).

The average is around *32 times a year*, with about *78%* chance that I'll have to pick up the young 'en between *27* and *37* times in any given year.

Oh, and obviously if you increase the *10%* probability mentioned above, the average will get smaller (and vice versa)

[![](/images/quick-look-uphill-struggle/pick-percents.png)](/images/quick-look-uphill-struggle/pick-percents.png)

And that's pretty much it. Any questions?

Oatzy.
