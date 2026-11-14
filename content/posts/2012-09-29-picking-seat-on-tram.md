---
layout: post
title: Picking a Seat on the Tram
date: '2012-09-29T23:53:00Z'
author: Oatzy
tags:
- game theory
- trains
- nerd
- over-thinking
- everyday maths
- public transport
- hand-waving
- maths
- modelling
modified_time: '2012-09-29T16:53:58.736-07:00'
thumbnail: /images/picking-seat-on-tram/IMG_20120929_155415.jpg
blogger_id: tag:blogger.com,1999:blog-14769935.post-7231300286912411191
blogger_orig_url: https://oatzy.blogspot.com/2012/09/picking-seat-on-tram.html
---

When I'm at university, I have to get the tram twice a day. Now I quite like the trams in Sheffield (at least, more than the trains and buses). But if there's anything I can do to get a little more leg room or personal space, then I'm going to try it.

On the way in to university, I get on the tram at the start of the line - i.e. the tram is more or less empty when I get on, so I have pretty much free choice of where I sit. In the main, middle section of the tram, seats are grouped into fours - two forwards, two backwards, face to face - and there are there are 5 rows and 2 columns of these groups.

(The are more seats in the front and rear carriages, but with difference layouts. And I almost never sit in those sections, so I'm ignoring them.)

When the tram's busy, you have to accept that you're probably going to be squashed, and bumping knees with the person across from you, and desperately trying to avoid awkward eye-contact. But when it's less busy, there's the chance for a bit of personal space.

The question is, where's the best place to sit (assuming you have free choice) so you're more likely to get some of that personal space?

Truth be told, I don't actually know. I figured, probably the best place is the forward-facing window seat in either of the 3rd (middle) row groups.

The logic was that a person would either have to sit next to you, or so they're facing backwards - generally less preferable options. And since people are more likely to grab seats nearest doors, the 3rd row is 'best' because it's equidistant from both doors.

Of course, if the front and rear doors aren't used equally, then the choice of row would have to be tweaked.

From that, I started thinking about how people chose which seat to take in a given four-group. And since I have nothing better to do than stare out the window for the 20-odd minute journeys, I figured I'd try to model it.

From empty to full there are 16 possible seat use configurations ('states'). People chose seats based on personal preferences, as well as which seats are already taken. So, for the model, we look at the different states, and consider how they might change with the addition or removal of various numbers of people.

Here's an example, that I sketched, of possible transitions resulting from the addition of one person at a time

[![](/images/picking-seat-on-tram/IMG_20120929_155415.jpg)](/images/picking-seat-on-tram/IMG_20120929_155415.jpg)

The red lines are possible changes of state where the number of people stays the same (usually after the removal of others). More on that later.

Now, the key thing here is that different states, and different transitions are more likely to occur than others.

For eample, a person with free choice is more likely to chose a forward-facing seat (some people tend to feel unwell traveling backwards), and a window-side seat so they've got something to stare at; unless they're planning on making a hasty exit.

So that would theoretically make the backward-facing aisle seat the least popular.

HOWEVER, if someone's already sat in FFWS, then BFAS becomes the more preferable, since it avoids having to sit next to, or directly in front of, some random stranger whose just staring blankly out the window in an unsettling sort of way. Also, personal space.

[![](/images/picking-seat-on-tram/IMG_20120929_160205.jpg)](/images/picking-seat-on-tram/IMG_20120929_160205.jpg)

And from there, if you introduce another person, they're most likely to sit FFAS, since BFWS is a bit awkward to get to and leaves you feeling kind of boxed-in. Plus you have the extra arm room on the aisle-side, and, if necessary, you can turn slightly to give yourself a little more leg room.

And if you add a four person, they have a hell of a time getting to the free seat, but it's their only option. Unless BFAS moves across to the window.

Now, back to those red lines in the diagram. From the 3-config described above, say BFAS leaves. You now have two people sat next to each other. The person in FFAS may then chose to move to BFAS for the sake of more personal space. This is kind of like how physical systems tend towards their lowest energy (least socially awkward) state.

The model itself is actually pretty straight-forward. What you do is construct a [stochastic matrix](http://en.wikipedia.org/wiki/Stochastic_matrix) (sometimes called a transition matrix) - basically, a 16x16 'table' that tells you the probability of the seating changing from one state to another. For example

[![](/images/picking-seat-on-tram/IMG_20120929_155559.jpg)](/images/picking-seat-on-tram/IMG_20120929_155559.jpg)

And this works for all possible transitions between all possible states.

The tricky part if determining the probabilities. You could just make random guesses at it. Or, if you were really determined, you could spend a load of time on trams, recording what transitions happen at each stop and how many times they happen. I don't plan on doing either.

But say you have your data and you've constructed your matrix, M. You could do a Monte Carlo type simulation using those probabilities. But with a stochastic matrix you can be more precise.

See, if you calculate M\*M, then the entries are the probabilities of moving from state i to j after two 'stops'. And if you calculate M^n, they you get the transition probabilities for after N stops.

And if you add up the entries down each column, j, then you have the probability of being in state j after N stops - that is, you can find the most likely seating configuration after some arbitrary number of stops. You could also use this method to work out the popularity of each seat over all possible states.

Which I think is pretty cool.

And that's all well and good for the groups. But what if you want to model the whole tram? That's where things get tricky, since you have to model how people chose seat groups, which itself depends on what seats are already taken in groups.

Ultimately, it can be modeled the same way, with a transition matrix. Only now, you're working with a 40x40 matrix.

Not difficult, per se, but certainly requires a lot of data and number crunching..\.

Come to think of it, if you were going to go to the trouble of observing and counting state transitions, you could just count how many times each seat is sat in over some arbitrarily long period to figure out each seat's popularity. Then you just need to try to get the seat *next to* the least popular.

But counting isn't as fun as modeling.

Oatzy.

[*I wonder what normal people think about on public transport..*]
