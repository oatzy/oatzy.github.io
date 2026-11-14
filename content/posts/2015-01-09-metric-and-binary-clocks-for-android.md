---
layout: post
title: Metric and Binary Clocks (for Android)
date: '2015-01-09T17:01:00Z'
author: Oatzy
tags:
- time
- metric clock
- binary
- metric
- clock
- nerd
- android
- hand-waving
modified_time: '2015-01-11T16:57:50.352-08:00'
thumbnail: /images/metric-and-binary-clocks-for-android/Screenshot_2013-10-12-17-13-30.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-8863241527627371068
blogger_orig_url: https://oatzy.blogspot.com/2015/01/metric-and-binary-clocks-for-android.html
---

A long while back I wrote a couple of blogs about clocks. In [the first](http://oatzy.blogspot.co.uk/2010/08/decimalising-time.html) I talked about decimalising time. Half a year later, I wrote [another](http://oatzy.blogspot.co.uk/2011/01/needlessly-incomprehensible-clock.html) where I designed a couple of circular binary clocks. I thought I'd try to recreate those clocks for my phone.

I had a widget making app - [Zooper](https://play.google.com/store/apps/details?id=org.zooper.zwfree&hl=en_GB) - installed on my phone, that I'd played with before. I build myself an autumnal homescreen, that looked like this.

[![](/images/metric-and-binary-clocks-for-android/Screenshot_2013-10-12-17-13-30.png)](/images/metric-and-binary-clocks-for-android/Screenshot_2013-10-12-17-13-30.png)

I don't use that theme anymore. These days I prefer a more minimalist homescreen - no widgets, as few icons as possible. But if you like it, you can [[download]](https://www.dropbox.com/sh/h0xeohfu4lxoyuh/AAAbtXxZelo8YQSTbEAKa2gza?dl=0) the widgets/wallpaper for the above theme. You'll need the [Media Utilities](https://play.google.com/store/apps/details?id=com.batescorp.notificationmediacontrols.alpha&hl=en_GB) app for the music bar.

Note - if you want to use any of the widgets I've linked in this blog, you'll need the [paid version](https://play.google.com/store/apps/details?id=org.zooper.zwpro&hl=en_GB) of Zooper. Alternatively, you can try to recreate them yourself - I'll include important details in this blog. There are other widget making apps, but I don't know much of using them.

**How to Make a Basic Clock Widget**

I'm going to quickly go over making a normal clock first so you can get a sense of how stuff works.

Making a circular clock, such as below, is pretty straightforward. Create a progress bar object for the minutes (the inner ring) and set its 'curve' value to 360. Then set the min and max values to 0 and 60 respectively and set the current value to \#Dm# (the current minutes). You may need to rotate and reposition it.

Create the hours circle in much the same way - using \#Dh# for 12h format, or \#DH# for 24h format. There are then loads of style settings you can play with. In the end you'll have something like this.

[![](/images/metric-and-binary-clocks-for-android/Screenshot_2015-01-07-19-36-25.png)](/images/metric-and-binary-clocks-for-android/Screenshot_2015-01-07-19-36-25.png)

Above is actually one of the built-in widgets that I de-cluttered a little. So if you don't want to go to the trouble of creating a widget from scratch, you can just tweak the ones that are already installed.

Note - all the clock images in this blog are shown on a grey background for clarity. Their actual backgrounds (if you download them) are transparent.

<strong>Backwards Clock </strong> [[download]](https://www.dropbox.com/s/uf5rakmombc5u1c/backwards-clock.zw?dl=0)

[![](/images/metric-and-binary-clocks-for-android/Screenshot_2015-01-07-17-54-47.png)](/images/metric-and-binary-clocks-for-android/Screenshot_2015-01-07-17-54-47.png)

This is actually the last one I made. I have an analogue backwards clock on my bedroom wall, that my sister got me from the [Science Museum in London](http://www.sciencemuseum.org.uk/). I figured, while I was at making clocks, why not make one of those as well. I put it second in this blogs because it's trivially different from the normal, forwards clock.

As before, you make your hour and minute rings from progress bars, but in this case you set the curve to negative 360. Like I said, trivial.

<strong>Decimalised/Metric Clock </strong> [[download]](https://www.dropbox.com/s/9ze3ompo7awmuc5/decimal-clock.zw?dl=0)

[![](/images/metric-and-binary-clocks-for-android/Screenshot_2015-01-07-17-55-56.png)](/images/metric-and-binary-clocks-for-android/Screenshot_2015-01-07-17-55-56.png)

That's 17:55 in real money.

The idea behind 'metric' or decimalised time is that the day is redefined as being 10 hours long, with 100 minutes per hour and 100 seconds per minute. The construction of the clock itself is the same as for the normal clock, we just have to convert the current time to metric.

For that, we first convert the current time to minutes, and divide that by the total number of minutes in a standard day (24\*60) - this gives us the fraction of the day that's elapsed. Multiplying that by the number of hours in a metric day (10) gives us the current decimalised hour.

For example, if we decimalise the time 12:51, we get the hour as 5.3542. In fact, because of the way metric time works, 5, is the hour and the first two digits after the decimal point, 35, is the minutes.

So for the hours ring, we set the current value to

```
$(0.00649*(60*#DH# + #Dm#))$
```

The progress bar object will automatically round this down to the nearest whole number.

To extract the minutes, we can use the '[modulo](http://en.wikipedia.org/wiki/Modular_arithmetic)' operator (written as a percentage symbol '%' in coding). The modulo operator gives us the remainder from division. So if we multiply the (metric) hours by 100, and take mod 100 we get something like \((100\cdot 5.3542) \bmod 100 = (535.42 \bmod 100) = 35.42\). Again, the progress bar will round this down.

So we can set the current value for the minutes ring to

```
$(0.649*(60*#DH# + #Dm#) % 100)$
```

I also included a text output the decimalised time. As mentioned above, we can just calculate the metric hour, which will give us something like 5.35. But I wanted it to have it to have the 5:35 format like a normal clock.

We already have our expressions above for the metric hours and minutes. We just need to slip in a couple of 'floor' functions to round them down to whole numbers. The other thing is that when the minutes is less than 10, they display as a one digit number, e.g. 5:3 instead of 5:03. To fix this we just throw in an if-statement.

The code for the text output of the metric time looks like this

```
$(floor(0.00694*(60*#DH#+#Dm#)))$:$(0.694*(60*#DH#+#Dm#)%100)<10?(0)$$(floor(0.694*(60*#DH#+#Dm#)%100))$
```

Yeah, it's a little unwieldy.

<strong>Binary Clock </strong> [[download]](https://www.dropbox.com/s/b0q1du0n4ml66hg/binary-clock.zw?dl=0)

[![](/images/metric-and-binary-clocks-for-android/Screenshot_2015-01-07-19-29-25.png)](/images/metric-and-binary-clocks-for-android/Screenshot_2015-01-07-19-29-25.png)

[10011:011101](https://en.wikipedia.org/wiki/Binary_number) = 19:29

In this design, each segment on each ring represents a power of two/binary digit. When the segment is grey it's a zero, when it's blue it's a one. So in the above, the hour (outer ring) is 10011 in binary, or \(1\cdot 16 + 0\cdot 8 +0\cdot 4 + 1\cdot 2 + 1\cdot 1 = 19\), in base 10.

In this case, we can't use progress bars. Instead, we have to make each ring segment an individual rectangle object, that will change its colour depending on whether it's representing a one or a zero. This makes constructing the clock a little less straightforward.

For the minutes ring, create 6 rectangles each with a curve of 60, and rotated so that they form a circle. Similarly, for the hours ring create 5 rectangles with curve 72, and so on.

I originally tried aligning everything 'free-hand'. That didn't work so well, so I created a temporary full circle as a guide. Of course, you don't have to make a binary clock circular - you could have it as a line of dot/bars. I just like the circle design.

Now, we need a way of converting the time to binary, and a way of telling each block whether the binary digit it represents is a one or a zero. At this point, I'm going to make a claim -

> *The n-th digit of a number, x, in binary is a zero if \(x \bmod 2^{n+1} \lt 2^{n}\), or a one otherwise.*

I'll prove this in a supplemental blog, that will be posted shortly after this one. In the meantime, you might like to try proving it for yourself.\*

*[edit]* - You can read that supplemental blog [here](http://oatzy.blogspot.co.uk/2015/01/follow-up-binary-proof-and-trinary-clock.html).

So we can use this condition to set/change the colours of each rectangle. For example, for the 2nd rectangle on the minutes ring (n=1), go to "Advanced Parameters", and enter something like

```
$(#Dm# % 4)<2?([c]#19ffffff[/c]):([c]#ff1084cb[/c])$
```

Or for the 5th rectangle on the hours ring (n=4), enter

```
$(#DH# % 32)<16?([c]#19ffffff[/c]):([c]#ff1084cb[/c])$
```

And so on.

I also made an annotated version of the design [[download]](https://www.dropbox.com/s/8kshu9xeeavxl2k/binary-num-clock.zw?dl=0) to make telling the time slightly easier; albeit at the cost of looking a little cluttered

[![](/images/metric-and-binary-clocks-for-android/Screenshot_2015-01-05-20-45-07.png)](/images/metric-and-binary-clocks-for-android/Screenshot_2015-01-05-20-45-07.png)

(16+4):(32+8+4+1) = 20:45

I tried adding a seconds circle, like in the version from the old blog, but the widgets don't seem to refresh often enough for it to work. Which is a shame, 'cause it's fun to [watch the seconds move](https://dl.dropboxusercontent.com/u/4635169/time/time2/index-alt.htm).

<strong>Proportional Binary Clock </strong> [[download]](https://www.dropbox.com/s/3v3v4tutm1xucbs/alt-binary-clock.zw?dl=0)

[![](/images/metric-and-binary-clocks-for-android/Screenshot_2015-01-07-13-52-11.png)](/images/metric-and-binary-clocks-for-android/Screenshot_2015-01-07-13-52-11.png)

13:52

This is pretty much the same as the one above, except, each segment is sized in proportion to the power of two it represents - the 8-segment is four times as big as the 2-segment, etc. I did this to give a better perspective on how much time has passed - because, really, one minute shouldn't take up as much of the clock face as 16 minutes. And also, I just think it looks neat.

The mechanics work the same as above. The tricky part is getting the rectangle sizes, curves and rotations right, and getting everything lined up just right, without loosing you mind over how that one bit is half a pixel out of place and there's nothing you can do about it so just let it go, okay!

Okay..\.

Oatzy.

[Making a backwards, binary, metric clock is left as an exercise for the reader.]

\* Hint: Try re-writing x as a sum of powers of 2.\
Bonus: Generalise for other bases.
