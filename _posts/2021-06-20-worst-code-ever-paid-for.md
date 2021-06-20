---
layout: post
title: The Worse Code I Ever Got Paid For
date: '2021-06-20T16:26:00.000-00:00'
author: Chris Oates
tags:
- coding
- python
- biographical
modified_time: '2021-06-20T19:07:00.000-00:00'
---

*Or, the not-so-fast Fourier transform, and what we take for granted in Python.*

# The Project

This started with my university 3rd year project. It involved signal processing - taking data from a mass spectrometer and finding the peaks. The peaks correspond to different compounds in whatever is being analysed.

Finding peaks is pretty easy, just look for the points where the gradient of the data goes from positive to negative. Except if there's noise, we might get a bunch of false peaks. So we've got to get rid of the noise.

I tried out various techniques for removing noise, and one that turned out to be quite effective was the [low-pass filter](https://en.wikipedia.org/wiki/Low-pass_filter). A low-pass filter removes high frequencies, but allows low frequencies to 'pass'. This turned out to be quite effective, since the signal peaks were much bigger and wider than the noise peaks.

![Screenshot of my project applying a low-pass filter](/assets/fourier/lowpass-ui.png)

One way to implement this is to convert the data to the 'frequency domain' using a Fourier transform, zero out the data above a certain frequency, then convert back to the 'time domain' using an inverse Fourier transform.

Which was easy enough, when I was developing in python

```python
from scipy import fftpack

temp = fftpack.rfft(data)
temp[cutoff:] = 0  # this is a numpy array
data = fftpack.irfft(temp)
```

At the end of the year, my project supervisor asked if I'd be interested in a summer job, integrating some of my code into a local company's commercial software.

# The Job

Problem was, their software was written in Delphi - a language I did not (and still don't) know. The boss told me it was like Pascal, another language I don't know. From my own perspective, it felt quite like C, with maybe some C++ or Java bits thrown in.

But I was young and arrogant enough to think I could pick it up easily enough. And to my credit, I did get the job done. And what's a few memory leaks between friends, anyway?

But the real problem was that Fourier transform for the low-pass filter. Working with Python, you can really take these things for granted. In Delphi, the only library I could find from a google search was one you have to pay for.

But how hard could it be to implement one myself?

As it turned out... not actually that hard! But we'll come back to that.

Basically, I read [the wikipedia article](https://en.wikipedia.org/wiki/Fast_Fourier_transform), and came up with a working implementation in an evening.

I don't have the code, it's propably on an old laptop somehwere, but here are some notes I did at the time

![Photo of FFT notes](/assets/fourier/fft-notes.jpg)

(please ignore the fact I kept writing 'DTF' instead of [DFT](https://en.wikipedia.org/wiki/Discrete_Fourier_transform))

I was pretty pleased with myself at the time; writing a working fast Fourier transform in a language I barely knew.

The only problem was, when it was given a really big bit of data, it would take *ages* to calculate. Like, the software literally froze for several seconds. And also, the memory leaks I alluded to earlier...

I didn't understand it at the time. I guess I just assumed it was normal when the data gets large(?)

# The Mistake

The punchline came a couple years later, when I was reading a book on data structures and algorithms in Python [^1]. See, another thing you take for granted in Python is dynamic arrays - arrays where you can just `append` new values.

But what do you do in a language like Delphi (or C), where you only have fixed length arrays?

Here's (roughly) what I did [^2]

```c
int new[length+1];

for (i=0; i<length; i++) {
	new[i] = old[i];
}

new[length] = value
```

That is, create a new array, one element bigger than the old, copy all the value from old to new, then set the last value in 'new' to the value you want to append.

If you don't know any better, like I didn't, this probably seems reasonable. Or at least, 'intuitive'.

The problem is, this is an `O(N)` operation - that is, it takes an amount of time proportional to the size of the array. So a bigger array means appending a value takes longer.

What I learned from that data structures book was how Python [dynamic arrays](https://en.wikipedia.org/wiki/Dynamic_array) (lists) really work.

Effectively, you allocate more 'capacity' than you need right now - say, twice as much

```c
int array[2*length];
```

As long as you've got some capacity left, you can append an item like

```c
array[length] = value;
length += 1;
```

And once the array fills up, rather than assigning a new array of `length+1`, you double its length.

This makes appending an '[amortised](https://en.wikipedia.org/wiki/Amortized_analysis)' (average) `O(1)` operation - that is, the time it takes to append an item is always (roughly) the same, regardless of the array size.

# The End

At the end of the summer, I was paid for my time, and was grateful for it and for the experience.

But in retrospect, I'm not sure I should have been paid for that particular code.

I just hope they've since fixed it, or at the very least, gotten rid of it.


Chris.

[^1]: For context, I studied theoretical physics, so I was never taught these things

[^2]: I don't remember any Dephi, so this snippet is more like C