---
layout: post
title: 'Quick Look: Don''t Blink..'
date: '2011-08-08T00:00:00Z'
author: Oatzy
tags:
- photos
- statistics
- doctor who
- pokémon
- everyday maths
- hypothetical question
- maths
modified_time: '2011-08-07T17:00:26.742-07:00'
blogger_id: tag:blogger.com,1999:blog-14769935.post-3239547500171801234
blogger_orig_url: https://oatzy.blogspot.com/2011/08/quick-look-dont-blink.html
---

"*..Don't even blink. Blink, and you're dead!*" threatened the frustrated photographer, following a fifth failed photo..

No, this isn't a [Doctor Who](http://en.wikipedia.org/wiki/Blink_%28Doctor_Who%29) thing (sorry). No, this is based on another lost article I read a while back:

**<em>How many photos do you have to take in order to get at least one where no one's blinking?</em>**

First things first, what's the probability of one person blinking when you take a photo of them?

Well for one thing, that's going to vary depending on environment, lighting, etc. And also on the shutter speed of the camera being used to take the picture.. But for simplicity, I'm ignoring all that.

The [average person](http://en.wikipedia.org/wiki/Blinking) blinks around *10 times per minute*, with an average blink lasting *300-400 milliseconds* (call it *350ms*). So in any given minute, the average person's eyes will be closed for a total of *3.5 seconds*.

We'll say the shutter is open for less than the duration of a blink. So the probability of a persons eyes being closed while the shutter is open -\> *p = 0.058*.

[I'll be honest, I'm not not entirely convinced that's right. But I'll go with it anyway.]

So the probability they don't blink -\> *(1-p) = 0.942*

If you're taking a picture of one person, that's only a *5.8%* chance of the subject ruining a photo by blinking. So your odds of a good shot are pretty good.

But if we have a much larger group of people - *n = 30* - the probability that none of those people blink while a photo is being taken:

*p1 = (1-p)^n = 0.165*

That's an *83.5%* chance that at least one person *will* blink. Those odds aren't so good.

So if we take *S* number of photos, what is the probability that at least one of those is 'perfect'?

This goes back to the methods use in the [Law Of Truly Large Numbers](http://oatzy.blogspot.com/2011/07/with-enough-tries.html) post - the probability of at least one perfect photo, big *P*, is one minus the probability that *none* of the *S* photos are perfect:

*P = 1 - (1-p1)^S*

So if we were to take, say, *S = 5 photos* -\> *P = 0.594*

Bearing in mind that you have to make these 30 people stand around while you take your however many photos, an almost 60% chance of the perfect shot from 5 tries it pretty reasonable.

But let's say you're the panicky sort, and you want to be *90%* certain that you have at least one perfect shot..?

Without going into the nitty-gritty, we can find *S* for *P = 0.9*, using some logarithms and algebra thus:

*S = ln(1-P)/ln(1-p1) = 12.8 shots*

And if you can get a group of *30 people* to stand still for *13 photos*, knowing that there's still a *10% chance* you won't get that perfect shot, then more power to you.

When people know they're having their picture taken, they generally try harder not to blink. Especially if you use a count down. So the probability of blinking, and by extension, the number of photos you'd have to take, drops dramatically. The numbers worked out above are probably more applicable for candid shots.

On the other hand, maybe the flashing going off (if you use one) will cause some people to automatically blink. And, admittedly, I've taken pictures of myself that have still managed to get capture me mid-blink. Though that might be down to a delay between click and shutter.

Of course, in this day and age, of digital cameras with instant preview, you can just keep shooting until you get the photo you want. Not like the dark old days of film cameras and photo roulette..\.

Oatzy.

[The word 'blink' and its variants appear *~17 times* in this post]

[As a random aside, working out the number of pokéball you need to throw to catch a given Pokémon is done in [much the same](http://bulbapedia.bulbagarden.net/wiki/Catch_rate#Probability_of_capture).]
