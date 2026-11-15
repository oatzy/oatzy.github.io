---
layout: post
title: Where are the Carriages?
date: '2012-03-04T00:12:00Z'
author: Oatzy
tags:
- rant
- rush hour
- trains
- voting
- optimisation
- algorithm
- public transport
- hand-waving
- maths
modified_time: '2012-03-03T16:12:33.357-08:00'
blogger_id: tag:blogger.com,1999:blog-14769935.post-7422877434607215907
blogger_orig_url: https://oatzy.blogspot.com/2012/03/where-are-carriages.html
---

**\<rant\>**

So it's around 9am, and you're waiting for a train. The trains in your area are a bit scummy, but whatever, you can't drive, and you've got to get to work/uni somehow. It's pretty busy, what with it being 9am, and when the train finally pulls up.. it's a single carriage.

Now a single car has [around 50 seats](http://en.wikipedia.org/wiki/British_Rail_Class_142), and this train is packed tight, with people standing in the aisles and the doorways, being forced to get intimate. And with everyone on board the conductor can barely get through the door. There are clearly enough people on this train to fill two cars, with people still having to stand.

So what gives? You're pretty pissed about having to stand for half an hour, and you've been inadvertently touched by strangers in ways you're not comfortable with. So you get your complaining hat on, and you turn to the internet to unleash the fury.

The train company's website directs you to their [Twitter feed](https://twitter.com/#%21/northernrailorg), where a poor public relations person is taking a barrage of vitriol from other angry commuters, while doing their best to remain polite and professional.

Several other people have already made your complaint, but all they're getting in return is "[Apologies we try to avoid this where possible](https://twitter.com/#%21/northernrailorg/status/175648061274591232)", or that the short trains were "[due to operational reasons](https://twitter.com/#%21/northernrailorg/status/174544893220360193)". And that's not really a satisfying response. You're not even sure it means anything.

\</rant\>

**So Where Are The Carriages?**

*Disclaimer*: I have no idea how the train company actually operates. I just like to write blogs about applied maths.

Here's the setup - you're in charge of logistics for the train company. You have a fixed number of trains/cars, and, for each day, a list of services and expected numbers of passengers.

How do you apportion the carriages between the services?

Obviously, every service needs at least one car, and services with more passengers need more cars.

So if you had, for example, three services with 50, 100, and 150 passengers respectively, and 6 cars, then it's easy to divvy them up - one for the first, two for the second, and three for the third.

But in general, it won't be possible to divide up the cars exactly like that; so what do you do about remainders?

This is actually similar to the problem of apportioning parliamentary seats between states in the US.

Currently there are 435 seats in the [House of Representatives](http://en.wikipedia.org/wiki/United_States_House_of_Representatives#Apportionment), which need to be shared out between the 50 states according to each state's population - the idea being that each seat should represent roughly the same number of voters.

There are [various methods](https://web.archive.org/web/20111228030702/http://www.ctl.ua.edu:80/math103/apportionment/quick.htm) for doing this, but I'm only going to go over two of them.

**The Hamilton method**

*[Hamilton's Method](http://en.wikipedia.org/wiki/Hamilton_method)* is the easiest and most intuitive.

Say you've got only two services - service A has 85 passengers, service B has 115 passengers (200 passengers total). And you happen to have 4 carriages - a total 200 seats. So seats for everyone! Except service A needs 1.7 cars, and service B needs 2.3 cars. And you can't divide a car into two chunks.

But for starters, you can give one car to service A (50 seats), and two to service B (100 seats). So what about the fourth? Regardless of which service you give it to, some people are going to end up having to stand. So what you want to do is minimise that number.

For service A, 35 people need a seat. For service B, 15 people need a seat. So it makes sense to give the last car to service A. 15 people still have to stand, but - short of building more cars - there's really nothing you can do about that.

This is also known as the [*largest remainder method*](http://en.wikipedia.org/wiki/Largest_remainder_method).

What if the passenger numbers were 75 and 125? Well in that case, I guess it would have to be a judgement call.

Anyway, that's the basic idea of the Hamilton method - divide up the cars as far as you can, then give the remaining car(s) to the service(s) which 'need them most'.

Things get trickier when you're dealing with larger numbers of passengers and cars, but ultimately it's pretty straight-forward.

**The Huntington-Hill Method**

Where trains differ from apportioning of parliamentary seats, is that a carriage has a fixed capacity, whereas the number of people a seat can represent is free to change.

And this means that you won't encounter some of the '[quirks](http://en.wikipedia.org/wiki/Alabama_paradox)' that arise from the Hamilton method - such as the *Alabama Paradox* (where increasing the total number of seats can mean a state losing seats), or the *Population Paradox* (where increasing a state's population can result in that state losing seats).

[You won't encounter them, but they're worth mentioning 'cause they're pretty cool.]

[*Huntington-Hill's Method*](http://en.wikipedia.org/wiki/Huntington%E2%80%93Hill_method) - the one currently used by the House of Representatives - is, generally, a more powerful method than Hamilton's, and [isn't susceptible](http://www.cut-the-knot.org/ctk/Democracy.shtml) to the various paradoxes. Another benefit is that it can be set up to guarantee that each state will get at least one seat.

It works by assigning seats, one by one, based on each state's '[priority quotient](http://en.wikipedia.org/wiki/Highest_averages_method)' - itself based on the state's population, and a 'modified divisor' based on the number of seats already allocated to that state.

But one advantage Hamilton's Method has over HHM, is that it will always give each service its ideal number of cars, either rounded up of down to the nearest whole number. So if a service's ideal number is 3.67, then Hamilton's method will assign either 3 or 4 cars to that service.

HHM, on the other hand, can 'violate quota' - that is, it can result in a given service being assigned more or fewer cars than it's ideal number (e.g. the 3.67 service might end up with only 2 cars). But this problem only occurs when the number of cars is fixed prior to apportioning. And sadly, it usually is.

As an aside, it turns out it's [impossible](http://en.wikipedia.org/wiki/Alabama_paradox#Impossibility_result) to find a 'perfect' method of apportioning - one with neither paradoxes nor quota violating. Incidentally, the [mathematical theory](http://en.wikipedia.org/wiki/Category:Voting_theory) surrounding voting is [quite fascinating](https://web.archive.org/web/20111207175029/http://www.newscientist.com/article/mg20627581.400-electoral-dysfunction-why-democracy-is-always-unfair.html). You know, if you're into that sort of thing.

**Unfortunately..**

Either method would work perfectly well. The problem is, while rounding up or down to the nearest car may seem trivial, the 50 seats that that one car represents can be a significant gain/loss for a service.

The lack of precise information can cause problems as well. You can only estimate how many passengers a given service will have in advance, and if you under-estimate, people are gonna be pretty pissed.

And on top of that, the numbers have to be recalculated from time to time as passenger numbers change..

Basically, getting the number of cars right can be tricky.

Of course, this all assumes that Northern Rail (or whatever company) has enough carriages to adequately satisfy its needs in the first place. Some how I doubt that's the case.

So ideally, NR needs to work out how many cars it actually needs, and build them. But I can't see that happening. And even if it did happen, it'd probably mean higher fares. And fares are pretty bad as they are.

Really, though, NR could do with a complete makeover just in general, given [how](http://en.wikipedia.org/wiki/Northern_Rail#Criticism) [shitty](https://twitter.com/#%21/northernfail) it is. Seriously, you should see the difference between them and the London Midland service. Ridiculous.

Incidentally, I also have strong feelings about the buses; don't even get me started. Trams are alright though - one every 10mins, seldom short of seats, sufficient leg-room.. bliss.

*<strong>tl;dr</strong>* - Where are the carriages, then? As it turns out, it's probably just that they [don't have enough](https://twitter.com/#%21/northernrailorg/status/175558593863622656) to go around.

This is what we get for [privatising](http://en.wikipedia.org/wiki/Privatization_of_British_Rail) the trains..\.

Oatzy.

[My complaining hat is a trilby. I like to look bad-ass while I'm complaining.]
