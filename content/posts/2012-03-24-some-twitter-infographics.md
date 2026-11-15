---
layout: post
title: Some Twitter Infographics
date: '2012-03-25T03:09:00Z'
author: Oatzy
tags:
- data tracking
- nerd
- python
- sociology
- infographic
- tweets
- sleep
- statistics
- OCD
- graph
- programming
- gender
- twitter
- data analysis
- tumblr
modified_time: '2012-03-24T20:46:54.915-07:00'
thumbnail: /images/some-twitter-infographics/edscription-cloud.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-7821856258678068359
blogger_orig_url: https://oatzy.blogspot.com/2012/03/some-twitter-infographics.html
---

I did [some](https://oatzy.github.io/2010/10/01/more-twitter-insights.html) [stuff](https://oatzy.github.io/2010/10/02/follow-up-women-really-do-tweet-more.html) [like](https://oatzy.github.io/2010/08/31/life-by-numbers.html) [this](https://oatzy.github.io/2011/01/01/life-by-numbers-end-of-year-report.html) before. And I figured, while I was updating my [network graphs](https://oatzy.github.io/2012/03/15/friend-network-evolution.html), why not update some of the other graphics?

And it helps that I worked out how to easily extract data from Twitter (see [previous blog](https://oatzy.github.io/2012/03/15/friend-network-evolution.html)). The code is [here](https://github.com/oatzy/question-nobody-asked/blob/main/some-twitter-infographics/TwitterStuff.py). Again, rate limits apply.

**Who Do I Follow?**

This is one of the ones I did [before](https://oatzy.github.io/2010/10/01/more-twitter-insights.html) - collect together the bios of the people I follow, then make a word cloud (using [Wordle](http://www.wordle.net/))

[![](/images/some-twitter-infographics/edscription-cloud.png)](/images/some-twitter-infographics/edscription-cloud.png)

Basically, I follow a bunch of *geeks* and *writers*. Who like '*things*'. So really, same as a year and a half ago.

I would point out though that 6 of the people I follow don't have bios, and about 7 just have lyrics.

Data [here](https://github.com/oatzy/question-nobody-asked/blob/main/some-twitter-infographics/descriptions.txt).

**Who Tweets the Most?**

These rates are worked out as *(total tweets posted)/(total days online)*. Obviously, the actually post rate will vary over different time scales..

[![](/images/some-twitter-infographics/bubble-rates.png)](/images/some-twitter-infographics/bubble-rates.png)

Bubble chart (made with [ManyEyes](http://www-958.ibm.com/software/data/cognos/manyeyes/)) - bubbles sized by tweet rate (the numbers on some of the bubbles).

The graph below gives a better idea of relative rates, and 'rankings' (click to embiggen)

[![](/images/some-twitter-infographics/rates-graph.png)](/images/some-twitter-infographics/rates-graph.png)

The blue line is actual values.

The orange is a logarithmic trend-line. It's a pretty good fit ([R2](http://en.wikipedia.org/wiki/R-squared)=0.95); and, loosely speaking, it means ~70% of the tweets in my timeline come from ~30% of the people I follow. [cf: [Pareto Principle](http://en.wikipedia.org/wiki/Pareto%27s_principle)]

You get similar log-shaped graphs when you split up the genders.

Full data [here](https://github.com/oatzy/question-nobody-asked/blob/main/some-twitter-infographics/twitterdata-2012317.txt).

**Chattiest Gender?**

You can read all the explanation, caveats, etc. in the previous posts ([here](https://oatzy.github.io/2010/10/01/more-twitter-insights.html) and [here](https://oatzy.github.io/2010/10/02/follow-up-women-really-do-tweet-more.html)). I'm just going to go straight into the data.

I follow 27 men and 21 women (excluding celebrities, etc.). The stats are as follow:

> Men:\
> Average = *6.21 tweets/day*\
> Standard Deviation = *6.47*
>
> Women:\
> Average = *13.79 tweets/day*\
> Standard Deviation = *14.27*

For clarity, here's a  [boxplot](http://en.wikipedia.org/wiki/Boxplot) (made in [R](http://www.r-project.org/))

[![](/images/some-twitter-infographics/gender-boxplot.png)](/images/some-twitter-infographics/gender-boxplot.png)

Basically, the women tweet more on average, and their rates are more spread out than for the men. In fact, roughly three quarters of the men tweet less than half of the women. Also, there's one outlier in the female group.

This is similar to what we found last time; although the women's average and spread aren't quite as high (average: 13.79 vs 19.21), and the men's average has increased slightly (6.21 vs 5.29).

If you take the ratio of the averages, the women tweet 2.15 times as much as the men. But maybe I just follow particularly chatty women..

Here's treemap ([ManyEyes](http://www-958.ibm.com/software/data/cognos/manyeyes/)), which should give you a better idea of the gender balance (boxes sized by tweet rate)

[![](/images/some-twitter-infographics/gender-treemap.png)](/images/some-twitter-infographics/gender-treemap.png)

Specifically, the graphic above is 62.5% purple (female).

Data [here](https://github.com/oatzy/question-nobody-asked/blob/main/some-twitter-infographics/twitterdata-2012317-gender.csv).

**Where in the World Are My Followers?**

The site I used [last time](https://oatzy.github.io/2010/10/01/more-twitter-insights.html) doesn't seem to exist anymore. So I'm using [MapMyFollowers](http://www.mapmyfollowers.com) instead. As the name suggests, these are my followers, rather than just the people I follow. Nonetheless..

[![](/images/some-twitter-infographics/followers-map.jpg)](/images/some-twitter-infographics/followers-map.jpg)

Mostly in the UK and the US. As you'd probably expect.

I will point out though, some of the locations are a little suspect. Some people haven't made their location available so aren't included, and others seem to be in countries they couldn't possibly be in. But it's the best we can do.

Here's a zoom in on the UK

[![](/images/some-twitter-infographics/followermap-uk.jpg)](/images/some-twitter-infographics/followermap-uk.jpg)

**What Do I Tweet?**

[![](/images/some-twitter-infographics/tweet-cloud.png)](/images/some-twitter-infographics/tweet-cloud.png)

Made with [Wordle](http://www.wordle.net/), with data from [TweetStats](http://tweetstats.com/).

Words are sized by how often I tweet them; and by extension, @usernames are sized by how often I tweet those people.

In fact, here are the people I 'mention' the most (TweetStats)

[![](/images/some-twitter-infographics/replies.png)](/images/some-twitter-infographics/replies.png)

Couldn't get a good source on who @replies me. That was one of the things Twoolr used to do..

**When Do I Tweet?**

[Twoolr](http://twoolr.com/) used to be awesome for Twitter statistics. But sadly, when they left beta, they started charging. And their free service went to shit. Luckily, I found [TweetStats](http://tweetstats.com/). Weirdly, it doesn't need you to log-in or anything, but somehow it can pull data on (nearly) all your tweets - beyond the 3,200 limit. Strange.

Here's some more graphs

[![](/images/some-twitter-infographics/tstat-agregates.png)](/images/some-twitter-infographics/tstat-agregates.png)

Basically, I tweet most on a Friday and Saturday, and at around 1-2pm.

And I've never tweeted at 5am. But that's probably because I'm always asleep at 5am

[![](/images/some-twitter-infographics/sleep-dist-03-25-02-35-35.png)](/images/some-twitter-infographics/sleep-dist-03-25-02-35-35.png)

Except that one time I got really drunk. ([SleepBot](https://web.archive.org/web/20121209225312/https://play.google.com/store/apps/details?id=com.lslk.sleepbot&hl=en))

**How Much Do I Tweet?**

This is another one I used to go to Twoolr for. And, to be fair, I still could. But that only goes as far back as April '10, and its graphics aren't as clear. Here's [TweetStats](http://tweetstats.com/) again

[![](/images/some-twitter-infographics/tweetstat-usage.png)](/images/some-twitter-infographics/tweetstat-usage.png)

Like I said [before](https://oatzy.github.io/2012/03/15/friend-network-evolution.html), I didn't tweet much in my first year. In fact, I only posted 36 tweets in all of 2009.

Now, the one problem with TweetStats is that 5 month gap in 2010. Why is this significant? Well, I was definitely tweeting during that time. In fact, by my estimates, over those 5 months I posted 5,724 tweets (~37tweets/day). So those 5 months account for 43% of all my tweets.

See, the thing is, in 2010, I was out of university, single, and unemployed. I posted a total 8,823 tweets - 24tweets/day. Since I've been back at university, that number's dropped to 11tweets/day.

That lull in Summer 2011 was when I was spending all my time on [Tumblr](https://oatzy.github.io/2011/06/25/tumbling-part-one-some-background.html) and watching classic [Doctor Who](http://oatzy.tumblr.com/tagged/doctor-who). Incidentally, I haven't posted on Tumblr since the start of September '11. It's terribly addictive, you see. I wouldn't recommend it; unless you're addicted to Doctor Who and Sherlock, and have lots of time on your hands..

So yeah.

Oatzy.

[Self-indulgent statistics, and pretty illustrations.]
