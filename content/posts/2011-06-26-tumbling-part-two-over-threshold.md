---
layout: post
title: 'Tumbling, Part Two: Over the Threshold'
date: '2011-06-26T19:57:00Z'
author: Oatzy
tags:
- graph
- programming
- nerd
- python
- voting
- twitter
- tweets
- maths
- modelling
- tumblr
modified_time: '2011-06-28T18:10:23.703-07:00'
thumbnail: /images/tumbling-part-two-over-threshold/vote-splits.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-4034203143492651273
blogger_orig_url: https://oatzy.blogspot.com/2011/06/tumbling-part-two-over-threshold.html
---

**I Didn't Vote For This**

A short while back, while people still cared about [AV versus FPTP](http://www.bbc.co.uk/news/uk-politics-11243595) voting, I wanted to come up with a voter simulation, so as to get data to compare the merits of the two (and a few other) systems, since real-world data is limited. Sadly, it came to no avail, since I had trouble coming up with a plausible way to simulate the behaviour of British voters.

The basis of how it worked was this - each voter has ten '*vote points*'. These points are divided amongst the parties according to how much the voter likes each party.

So if a voter was a strong *Conservative* supporter, they might give all their points to *Conservative*. A voter who's more liberal might give 6 points to the *Lib Dems* and 4 to *Labour*. Or whatever.

[![](/images/tumbling-part-two-over-threshold/vote-splits.png)](/images/tumbling-part-two-over-threshold/vote-splits.png)

In the case of the simulation, these points were going to be assigned randomly, but according to some [Markov Chain](http://en.wikipedia.org/wiki/Markov_chain) type model - based on the typical [voting habits of Brits](http://news.bbc.co.uk/1/hi/uk_politics/election_2010/default.stm). This, by the way, is where I was having trouble - for large numbers of voters, the result were always the same.

The other part of the model was to (randomly) assign to each voter an '*approval threshold*' - that is, if a voter assigns to a party a number of points higher than their personal *approval threshold*, then they 'approve' of that party, and will place a vote accordingly.

[![](/images/tumbling-part-two-over-threshold/votes-approval.png)](/images/tumbling-part-two-over-threshold/votes-approval.png)

So if, in the liberal example described above (*voter B* in the diagram), the voter has a threshold of 5, they would place a vote for only the *Lib Dems*; if, on the other hand, they had a threshold of 3, then (under an AV voting system) they would place a vote for both - order of preference: 1. *Lib Dem*, 2. *Labour*.

(In the diagram, all three 'voters' are given the same approval threshold for simplicity. The thresholds are by no means constant and universal.)

**I Like It, But Not that Much**

So what does this have to do with Tumblr? Well. On Tumblr, you can either ignore a post, like it, or reblog it.

Now, there are some people who will reblog almost anything that catches their fancy. Then there are people, like me, who are very picky and only reblog things they really like.

This is basically analogous to the *approval threshold* in the voting sim.

Obviously, the quality of a post is subjective (to some extent). But imagine first that for every post you see, you assign to it some rating from 0 to 10. The rating you assign to a given post will be (relatively) unique to you.

Here is how we get around the problem of subjectivity,

We assume that the ratings a large sample of people will assign to a given post will have some regular distribution - most likely a [normal distribution](http://en.wikipedia.org/wiki/Normal_distribution) - where the average and spread of ratings reflects (to some extent) the quality of that post. Or, at least according to that particular sample of people.

Each user then has two threshold values - a '*like threshold*' and a '*reblog threshold*'. And as before, if the rating a person assigns to a given post exceeds one of these thresholds, that person will either *like* or *reblog* the post (possibly both) accordingly.

**Some Asides**

It's worth noting that similar modelling can be applied to any piece of information that can be spread - whether it be on Twitter, by email, whatever - where you have some '*sharing threshold*' by which you judge whether or not you think a thing is worth sharing.

This may vary wildly from situation to situation. But in most cases outside of Tumblr, you will tend to find that people typically have a higher *share threshold* - higher standards, are more pick, are more wary of what they share, etc.

Another thing to consider, with Twitter in particular, the originator of a post can have a massive effect on how much said post is retweeted.

For example, some people (fangirls) will retweet someone like Justin Bieber simply by virtue of the fact that it's Justin Bieber. Conversely, some people may not retweet someone like Piers Morgan because they don't like him - even if they would otherwise like something he posted enough to have retweeted it.

Finally, people don't always share things simply because they like them - they may want to make some comment on the post, they may want to mock the post, whatever.

But for simplicity, we're ignoring that all these eccentricities, on the assumption that including them would have no appreciable effect on the model.

**Model Affinity**

I wrote a quick model of this behaviour (Python, can be viewed/downloaded [here](http://dl.dropbox.com/u/4635169/user.affinity-alt.py)).

For this model, the user's thresholds are generated uniformly - that is, all numbers in the ranges have the same probability of being chosen,

For the '*like threshold'* you pick a random number between 1 and 11.\
For the *'reblog threshold'* you pick a random number between the '*like threshold'* and 11<em>.</em>

The user's assessment of a post is randomly generated based on a normal distribution - in this case with *mean=5*, *sd=3*, constrained to the interval *[0,10]*. These values were chosen arbitrarily.

For a simulation of *100,000* users, this model returns approximately *25,575 likes* and *14,487 reblogs*. This gives a '*reblog to like' ratio* of *0.56*.

This is quite different from the *'R:L ratio'* of the Dr Who image, discussed in the [previous post](http://oatzy.blogspot.com/2011/06/tumbling-part-one-some-background.html) - which turns out to be *1.42*

But if we (effectively) increase the quality of the post - *mean=10*, *sd=2*, same interval - we now get approximately *32,393 likes* and *41,872 reblogs*, giving a *R:L ratio* of *1.29*

Which reflects reality quite well - that is, the better a post is, the more reblogs it will get (and the higher its *R:L ratio*). You could also get a similar effect by lowering the approval thresholds of the users - effectively lowering the users' standards.

*Note/* You could probably get a better replication of real world data by fine tuning the random variables. The ones used here were chosen fairly arbitrarily.

**Personal or Probable**

For large numbers of people, there are two ways you could work this into a model of post spreading:

1\) *On a per person basis*

That is, for each user work out whether they will ignore, like, or reblog, as you go. This would lead to richer behaviour on a per-simulation basis, and is better if you want a more detailed, more 'precise' model.

2\) *Based on the averaged probability*

That is, run a simulation for a large number of people (as above), work out the average number of likes/reblogs, and use this as the 'probability of liking/reblogging', constant for all users. So from the first simulation above, the probabilities would be:

*p(reblog) ~ 0.14*\
*p(like) ~ 0.26*

This would make the behaviour more uniform across multiple simulations, but would be less computationally taxing.

It can be argued that, when you average over a large number of simulations, you will get (almost) identical results for both approaches. So it's ultimately a matter of preference.

In [Part 3](http://oatzy.blogspot.com/2011/06/tumbling-part-three-stochastic-spread.html) of the series, I'll be looking at constructing a model of how posts spread through Tumblr, building on the model described here.

Oatzy.

**<em>[addendum]</em>** -  Due to a mild error, the section labeled '*Model Affinity*' had to be rewritten. If you read this post before this addendum was added, it's probably worth re-reading that section.
