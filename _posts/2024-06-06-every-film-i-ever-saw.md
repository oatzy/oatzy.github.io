---
layout: post
title: Every film I ever saw - data mining myself
date: '2024-06-06T19:56:00.000+00:00'
author: Chris Oates
tags:
- biography
- data
- movies
modified_time: '2024-06-07T00:06:00.000+00:00'
---

I signed up for [Letterboxd](https://letterboxd.com/oatzy/).

# trakt

One of the first options, on creating a letterboxd account, is importing data from other services - one of them being [trakt](https://trakt.tv/).

I don't use trakt directly. For many years, I've been using [SeriesGuide](https://www.seriesgui.de/) to keep track of TV shows. I used this in combination with trakt because I could then use the trakt api to get a list of new episodes 'today' for [completely legal reasons](https://oatzy.github.io/2020/05/17/encounter-with-rust-safety.html).

SeriesGuide also lets you track films.

So I [exported my data](https://github.com/anoopsankar/Trakt2Letterboxd) and imported it into Letterboxd - roughly 950 films

And what's interesting about this is trakt had recorded *when* I'd watched each film, and Letterboxd displays this in a ['diary'](https://letterboxd.com/oatzy/films/diary/).

This is quite pleasing.

The only problem is, the earliest film I had recorded in trakt was [Interstellar](https://letterboxd.com/film/interstellar/) in November 2014.

I could do better. I could go farther.

Too far? Who's to say...

# eTickets

There were a couple films - [Spider-man: No Way Home](https://letterboxd.com/film/spider-man-no-way-home/) and [Venom: Let There be carnage](https://letterboxd.com/film/venom-let-there-be-carnage/) - which I hadn't logged. Luckily, I have etickets, so just had to search my emails to get the exact date.

But I only started buying tickets online in 2021, when movies started to come back after covid

[the first film I saw, post-covid, was [Black Widow](https://letterboxd.com/film/black-widow-2021/)]

# Ticket stubs

My next thought was

> *you know... I'm the sort of person who would keep old ticket stubs; and I bet I know where they are...*
>

And reader, I am, and I did

![A bundle of ticket stubs](/assets/ticket_stubs.jpg)

I was surprised by how far back they go - the oldest is for [The World is Not Enough](https://letterboxd.com/film/the-world-is-not-enough/) in 1999.

I was also surprised by some of the films, for example I have no memory of seeing [Lilo & Stitch](https://letterboxd.com/film/lilo-stitch/) at the cinema, but I have a ticket stub that says otherwise.

On the other hand, I was disappointed by how much was missing. I saw [Pokemon: The Movie 2000](https://letterboxd.com/film/pokemon-the-movie-2000/) at the cinema - I have the promo cards to prove it - but sadly no ticket stub to say when.

# Notion

While looking over my watch history from trakt, I noticed a weird empty spot from November-December 2022. This didn't look right, because I'm in the habit of watching movies every weekend.

Maybe I was lazy those two months, or maybe trakt was having some issues? I dunno.

I started using [notion](https://www.notion.so/) for note keeping in 2020, and I had a movie watching list in there. And when I watched a movie, I would check a box to hide it.

Now, I didn't record when exactly I watched the films, but notion does auto-track the last edit time on each item - such as when a checkbox is checked.

I was a little lax about when I checked the box on notion - sometimes it would be days later - but it was enough to tell me which films I was missing from that period.

[I also did star ratings in notion, which I could manually copy across]

# Netflix

Netflix keeps a [watch history](https://help.netflix.com/en/node/101917), and even better lets you download it as a [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) file

But not a CSV that can be imported to letterboxd.

It only tells you title and watch date, and annoyingly combines tv shows and movies.

The quick and dirty work around was to [grep](https://en.wikipedia.org/wiki/Grep) out words like "Episode", "Season", "Series"

Starting from the bottom, the earliest entry was [Cloudy With a Chance of Meatballs](https://letterboxd.com/film/cloudy-with-a-chance-of-meatballs/) in September 2014

I only had to add a few entries from 2014 before I hit the movies I'd recorded in trakt.

# Prime Video

Amazon also keeps a watch history, but you have to make a [formal request](https://www.amazon.co.uk/hz/privacy-central/data-requests/preview.html) and wait a couple of days for the download.

It's CSV again, and with a similar issue as netflix of mixing tv and movies. And to make matters worse, it seems to record trailers, including the ones that auto-play in the app

I only got Amazon Prime when I entered full time employment (end of 2015), and 2015 onwards I had in trakt. So most of it was already covered.

There were a couple of early films I hadn't logged. The first film I watched on Prime was [It Follows](https://letterboxd.com/film/it-follows/) on Boxing Day 2015.


I've watched films on other streaming services, but none before 2015. I did have to look up one on [Crunchyroll](https://www.crunchyroll.com/), which sadly does not provide a downloadable history.

# LoveFilm

...was a DVD rental service, like the UK equivalent of the original incarnation of netflix.

I signed up for an account in 2010. [LoveFilm](https://en.wikipedia.org/wiki/LoveFilm) was later bought out by Amazon, who ultimately discontinued the service in 2017

Unfortunately, I don't have any record of what films I rented or when. I searched my email and found two "Your next rental is on the way..." messages ([Twelve Monkeys](https://letterboxd.com/film/twelve-monkeys/) and [Creation](https://letterboxd.com/film/creation/))

Apparently, I deleted all the subsequent emails.

IIRC, my subscription was 3 DVDs a month, and I had the account ~7 years - totalling about 250 films, which is a pretty major loss of data.

When I was requesting my Amazon data, I also enquired about my LoveFilm rental history. But they just sent me another copy of my prime video data (which doesn't include Lovefilm). So one has to assume that data no longer exists.

# Foursquare

Clutching at straws, I was starting to wonder if I could use my phone's location data (google maps) to figure out when I visited (or was near) a cinema. Then I remembered I had something even better.

There was a period, 2010-2014, when I used [foursquare](https://foursquare.com/city-guide) to record everywhere I went - including cinema visits, and including what film I saw

(2014 conveniently being when I started tracking films in SeriesGuide, more or less)

And the data still exists on the foursquare website (tho it was hard to find the right login page from google). Once I reset my password, it was a simple matter of filtering on *"Category: Movie Theatre"*.

But it turned out I didn't log the specific film for my first 3 recorded cinema visits.

For the first one, I added the comment *"Mind suitably braced for being blown..."* and safely assumed this was [Inception](https://letterboxd.com/film/inception/) (it aligned with the release date)

Similarly, I remembered seeing [Source Code](https://letterboxd.com/film/source-code/) around this time, and it wasn't mentioned in any of my other check-ins. And again the release date lines up.

For the last one I wasn't sure what it could be. I had a scroll through old blog posts from around that time for clues, and lo and behold - "[Tron Legacy](https://letterboxd.com/film/tron-legacy/): [A Review](https://oatzy.github.io/2011/01/15/tron-legacy-review.html)"

Incidentally, there are a couple other old posts on this blog [for](https://oatzy.github.io/2010/08/08/inception-review.html) [film](https://oatzy.github.io/2010/08/15/handful-of-film-reviews.html) [reviews](https://oatzy.github.io/2010/08/27/good-departed-pilgrim-flew-over.html)

# Twitter

Between 2009 and 2015, I was a prolific tweeter, so it seemed likely I would have mentioned watching a bunch of films.

To check, I downloaded my twitter data. I can find quite a few relevant tweets by grepping: 'watch' (watched, watching), 'cinema', 'film', 'movie', 'see' (seen), 'saw' ...

```
Watched 'Non Stop'. Was better than I expected. As if any movie where Liam Neeson plays an action hero could be bad.
-- Sat Aug 16 21:55:48 +0000 2014
```

[I guess a lot can [change](https://letterboxd.com/film/retribution-2023/) in 10 years :p]

But this isn't foolproof, it's hard to pick out all mentions or allusions to films

```
Who is this old joker? #BucketList
-- Sat Sep 11 21:06:15 +0000 2010
```

Maybe one could use machine learning to pick out movie titles.

Then there's this spicy take

```
I've got nothing against subtitled film, but they're a pain in the arse if you like to watch films while you eat. #RemakeAllTheForeignFilms
-- Sun Feb 26 13:59:20 +0000 2012
```

I remembered I was referring to [The Extraordinary Adventures of Adele Blac-Sec](https://letterboxd.com/film/the-extraordinary-adventures-of-adele-blanc-sec/) - or as I typed it into google, since I couldn't remember the title, *"french comic movie adel"*.

Side note: one set of tweets shows me starting to watch [Michael Bay's Transformers](https://letterboxd.com/film/transformers/), and giving up after ~1 hour. Should that count?

# MySpace

Before twitter, I had a MySpace blog, and from 2007-2008 I updated it almost daily.

In a way, the blog was like a proto-twitter, in that it was a collection of disconnected thoughts, autobiography, and random quotes and song lyrics.

I kept a backup of all my posts when MySpace went out of fashion; the live blog no longer exists.

So I fetched the backup and, as with the tweets, grepped for pertinent words

```
2 Aug 2007
    [Another chapter of my pathetic life]

    I'm disinclined to acquiesce to your request.

    Means no.

    Due to the lack of decent TV before the setting of the sun, I've rediscovered my DVD collection.
    [I've got perhaps more Johnny Depp DVDs than is normal for a boy of my age]
    Today I watched 'Pirates of the Caribbean: Curse of the Balck Pearl' [longest name ever], and tomorrow I intend to watch 'Deadman's Chest'.

    Other movies I've watched over the past week [most on TV]:
    'Edward Scissorhand', 'Charlie's Angels', 'Secretary', the back end of Napolean 'Dynamite', 'Charlie and the Chocolate Factory', 'Constantine', 'Dodge Ball'...
    can't think of any others off the top of my head.
```

Frustratingly, a few time I mention going to the cinema, without saying which film I saw

```
I went to the movies. But I don't need to tell you about that, 'cause most of my 'core' readers were there.
```

[Reading back over those blogs, I was surprised by how often I wrote about getting drunk. Ah, to be 18 again.]

# Memory?

It's frustrating, knowing you saw a film at the cinema, but not being able to pin down an actual date.

I mean, it's going to be within, say, 2 weeks of release. But I'm not sure I can allow myself that big a margin of error.

# Compromise

Of course, I'm never going to be able to figure out *when* I saw every film I ever saw.

Beyond a certain point I just have to settle for logging that I saw a film 'at some point'.

Even this is harder than it seems.

Given a specific film, it's fairly easy to say whether or not I've seen it. So one approach was to browse through popular films, directors, actors. But there are going to be things you miss from this approach - the unpopular, the obscure.

The harder approach is trying to randomly remember films I've seen.

[*"Ooh, what was that [vampire film](https://letterboxd.com/film/byzantium/) with Saoirse Ronan?"*]

This mostly works by association - I've seen this film, oh that reminds me of this other film.

I've reached the point where I think I've covered maybe 99% - I struggle to think of new ones.

Then occasionally I'll be like *"wait, how did I forget [Who Framed Roger Rabbit?](https://letterboxd.com/film/who-framed-roger-rabbit/)"*

# Fool's Errand

One thing I've learned from the films I had concretely recorded - there are films I've seen that I have no memory of seeing. Which means there are probably films I don't remember, which I don't have any record of.

And if you don't remember seeing a film, does it really count?

To date, I've managed to log ~1,800 films, of which ~1,200 have a definitive watch date. So I managed to pin down ~250 films in addition to those from trakt.

Which is not too shabby. Not an entirely fruitless endeavour.

Chris.

[It really is a shame I couldn't get that LoveFilm data]