---
layout: post
title: Needlessly Incomprehensible Clock Design
date: '2011-01-20T00:09:00Z'
author: Oatzy
tags:
- time
- binary
- clock
- javascript
- nerd
- random
modified_time: '2011-01-20T05:04:36.309-08:00'
thumbnail: /images/needlessly-incomprehensible-clock/clock.jpg
blogger_id: tag:blogger.com,1999:blog-14769935.post-6003741440737519709
blogger_orig_url: https://oatzy.blogspot.com/2011/01/needlessly-incomprehensible-clock.html
---

I'd be massively exaggerating if I said I had insomnia. I just have difficulty getting to sleep; I struggle to 'switch off' my brain.

So while I was trying to get to sleep last night, I somehow got on to designing this clock,

[![](/images/needlessly-incomprehensible-clock/clock.jpg)](/images/needlessly-incomprehensible-clock/clock.jpg)

The time, in case you couldn't work it out, is *23:46:52*

How does it work? It's part binary, but with an analogue-style layout. The central pie is seconds, the middle ring in minutes and the outer ring is hours.

Each ring is divided into chunks, sized in proportion to the powers of 2 that they represent. To get the time, you simply add up the 'illuminated' chunks.

So in the above example:\
hours = 1+2+4+16 = 23\
minutes = 2+4+8+32 = 46\
seconds = 4+16+32 = 52

It was even more incomprehensible when all the chunks were the same colour. There's also this slightly more comprehensible one, where all the chunks are the same size (within a given ring).

[![](/images/needlessly-incomprehensible-clock/Untitled-1-alt.jpg)](/images/needlessly-incomprehensible-clock/Untitled-1-alt.jpg)

The time on that one is *12:52:11*

There's a working version of the first [here](http://dl.dropbox.com/u/4635169/time/time2/index.htm), and of the second [here](http://dl.dropbox.com/u/4635169/time/time2/index-alt.htm). It's written in JavaScript with the help of the [jsDraw](http://jsdraw2d.jsfiction.com/) library.

Oatzy.
