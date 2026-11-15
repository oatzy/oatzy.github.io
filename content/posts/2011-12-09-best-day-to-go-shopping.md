---
layout: post
title: Best Day to Go Shopping
date: '2011-12-10T01:08:00Z'
author: Oatzy
tags:
- foursquare
- statistics
- christmas
- graph
- programming
- python
- sociology
- data analysis
- maths
modified_time: '2011-12-10T16:58:05.968-08:00'
thumbnail: /images/best-day-to-go-shopping/shoppers-norm-av.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-6173983660618777230
blogger_orig_url: https://oatzy.blogspot.com/2011/12/best-day-to-go-shopping.html
---

**The Question**

As the title suggests - which is the best (least busy) day to go shopping on?

Or more generally, how do crowds at shopping centres vary over time? Which days are busiest, or least busy? Are the shops getting busier as we get closer to Christmas? Less busy?!

It an interesting question, and one that's probably been looked into before. But still, I had an idea and I'm running with it.

[*Feel free to skip straight to the results if you're not interested in statistics and the likes..*]

**Data Collecting**

Data collection on this is tricky. Especially if you don't have legions of people to go out and actually count people. What I want to do is extract numbers with the minimum of effort.

So here's the game - [Foursquare](https://foursquare.com/).

If you're unfamiliar, Foursquare is a 'social game', for which you 'check-in' to locations and earn points and badges accordingly. It's also good if you're an [obsessive types](https://oatzy.github.io/2011/01/01/life-by-numbers-end-of-year-report.html) who likes to keep track of where they've been.

So the idea is this - some subset of shoppers will be Foursquare users, who will check-in when they visit any given shopping centre. If we can extract check-in counts over a given time period, hopefully that can be used as an indicator of a place's 'busyness'. Obviously, this is flawed - but more on that below.

Right. So on the Foursquare page for a given venue, there isn't a total historical record of check-ins over time. Instead, what we have is the total number of check-ins at that location up to the time when you loaded the webpage.

What we do, then, is record that number at some fixed time every day (say, midnight). Then the number of check-ins on a given day is the difference between the total at the end of the day and the total for the end of the previous day. Easy.

In fact, to make life a little easier, I wrote [this bit of code](https://github.com/oatzy/question-nobody-asked/blob/main/best-day-to-go-shopping/CheckinCounter.py) [python]. All I have to do is remember to run that every evening, and we have our data.

**Sampling**

There are two possible sources of [sampling errors](http://en.wikipedia.org/wiki/Sampling_%28statistics%29#Errors_in_sample_surveys):

1\) *Location*

If we only track one location, we have a very small [sample size](http://en.wikipedia.org/wiki/Sample_size). That means we're subject to perturbations - for example, a major event like the Christmas lights being switched on - or just general statistical noise. Also, shopping patterns may vary across the country, or depending on how close to a city centre the centre is located, and so on.

It's actually fairly easy to overcome this. First of all, we have this list of the [largest shopping centres in the UK](http://en.wikipedia.org/wiki/List_of_shopping_centres_in_the_United_Kingdom_by_size). From that list I picked 20 locations to sample. This data can then be normalised and averaged to look for any general patterns that are (relatively) store independent.

Oh, and I should probably mention, since this data is being collected from places in the UK only, patterns may vary for different countries.

2\) *Users*

Using Foursquare data, we're working on the assumption that as the number of shoppers increases (or decreases), the number of Foursquare check-ins will *increase in proportion*.

This is not necessarily the case.

First of all, we look up the Foursquare user demographics. There is no one source of definitive data on this (that I could find). But to get a general idea, there is [this](https://docs.google.com/viewer?a=v&q=cache:VVFYrrMekikJ:www.bart.gov/docs/BART_Foursquare_Survey_Report.pdf+&hl=en&pid=bl&srcid=ADGEESiK0XfFH2-xHiv8wsawT4DvsalcV3F_BPmhTEdUvfIHQKZnMdMzy7C4f3fv9KZ-2mrxiT-P37txiTuq0IzGJCjti7Oi_GsDYZt2VaIe0oXFUT-Ud5ot7C6YvzTa90sPLfyPlLkn&sig=AHIEtbTDg0_FvLzUNjpxu4aKgCexA0L_bw&pli=1), based on a survey of BART travelers.

Obviously, this demographic source is for users of an American transport service, but I'm assuming it's representative of Foursquare users in general.

From this we see that the typical user is most likely male, age 25-34. Or to put it another way, women, young people, and old people are under-represented. And from my experience, it seems like women and old people are the most common shoppers on weekdays.

So this may introduce a [disparity](http://en.wikipedia.org/wiki/Sample_bias) between the data and reality. But it's not one we can really do anything about (without seeking an alternative source of data). So, as long as there is a general size proportionality between shoppers and check-ins, we'll consider the data acceptable.

**Results**

By far, Saturday is the worst day to go shopping (in terms of crowds). But you already knew that.

So I have my data for the last 3 weeks, for 20 shopping centres across Britain. Here's the [raw data](https://github.com/oatzy/question-nobody-asked/blob/main/best-day-to-go-shopping/checkins.txt), for if you're into that sort of thing.

I worked out the check-ins for each place on each day, then normalised by shopping centre - so that the total number of check-ins for each shopping centre over the three week period now adds up to 100. I then averaged these 'norms' across all shopping centres.

Here's what those results look like.

[![](/images/best-day-to-go-shopping/shoppers-norm-av.png)](/images/best-day-to-go-shopping/shoppers-norm-av.png)

In fact, I went back and 'tidied up' the data, removing venues with less than 100 check-ins total during the recording period - since their sample sizes were maybe too small for any patterns to be statistically significant - and removed a couple of anomalies (one place ended up with negative check-ins).

This is what the tidy plot looks like

[![](/images/best-day-to-go-shopping/adjusted-update.png)](/images/best-day-to-go-shopping/adjusted-update.png)

*[Updated since original post]*

Pretty similar, but some of the bars are now closer together (removes the anomalies from Sunday and Wednesday).

So from the results above, the order of days, from least to most busy, seems to be:

1\) *<strong>Monday</strong>*\
2\) *<strong>Thursday</strong>*\
3\) *<strong>Tuesday</strong>*\
4\) *<strong>Wednesday</strong>*\
5\) *<strong>Sunday</strong>*\
6\) *<strong>Friday</strong>*\
7\) *<strong>Saturday</strong>*

But note, it's pretty close amongst the top 3 least busy days.

It shouldn't be too surprising that weekdays are less busy than weekends - what with people working.

As for Sunday being so low compared to Friday and Saturday - well, that might be the result of Sunday opening hours.

For example, [Meadowhall](http://www.meadowhall.co.uk/website/home.aspx) has typical opening hours of 9am-8pm, but on Sundays it's 11am-5pm -\> 11hrs vs 6hrs. So maybe it would make sense to re-adjust accordingly. But deciding how, exactly, to re-adjust is tricky. So we'll just leave it be.

NB/ Wednesday, week 2 maybe distorted due to [public sector strikes](http://www.bbc.co.uk/news/uk-15953806) - there certainly appeared to be more people on the train. But but a lot of that increase was from children (see sample bias above).

Of course, each shopping centre is unique, and there will be variation as to which days are best and worse for each. As an example, here's what the (non-normilised) plot looks like for [Westfield London](https://web.archive.org/web/20111210044556/http://uk.westfield.com:80/london) (the most checked-in to shopping centre by far)

[![](/images/best-day-to-go-shopping/shoppers-westfield.png)](/images/best-day-to-go-shopping/shoppers-westfield.png)

Again, pretty similar to the average. But in this case, Wednesday is less busy than the average, and Thursday more. And Friday has that weird dip in week 2, bringing its average down.

One last thing I'd like to point out - notice there is no particular week-on-week trend. That is, the number of check-ins isn't (on average) increasing as we get closer to Christmas. Or decreasing for that matter. Which is, perhaps, not what you'd expect.

But maybe that will change within the next couple of weeks. And certainly after Christmas, when the January sales kick off. Maybe.

This is an on-going project - bear in mind, this is only 3 weeks worth of data, so it may be too soon to draw any solid conclusions - but I will keep you posted. Maybe I'll do another post just after Christmas, or after New Year's. At any rate, I'll tweet it when I do.

Oatzy.

[There's always online shopping..]
