---
layout: post
title: Simple Harmonic Sleep
date: '2012-01-28T22:07:00Z'
author: Oatzy
tags:
- data tracking
- sleep
- OCD
- procrastination
- found functions
- graph
- nerd
- over-thinking
- random
- maths
- modelling
modified_time: '2012-01-28T14:07:17.752-08:00'
thumbnail: /images/simple-harmonic-sleep/screenshot-crop.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-8698149030893768436
blogger_orig_url: https://oatzy.blogspot.com/2012/01/simple-harmonic-sleep.html
---

So I started using [SleepBot Tracker](https://market.android.com/details?id=com.lslk.sleepbot&hl=en) to track my sleep. This is what it's looking like so far

[![](/images/simple-harmonic-sleep/screenshot-crop.png)](/images/simple-harmonic-sleep/screenshot-crop.png)

Basically, I'm averaging about 8 hours, except on those two days near the start where I had to get up early for exams.

Now, being a physics student, the graph reminded me of that for damped simple harmonic motion (starting from 20/01, ignoring the first 3 points). And being a crazy person, I decided to try and model my sleep as such.

So what's [simple harmonic motion](http://en.wikipedia.org/wiki/Simple_harmonic_motion)?

*Simple harmonic motion is a type of periodic motion with a restoring force directly proportional to the* *the system's* *displacement* *from equilibrium*.

For example, a pendulum is a simple harmonic oscillator - it has periodic motion, its equilibrium is the lowest point of the swing, and the restoring force is gravity.

Now, one *could* argue that sleep is SHM-like - we have some typical sleep length (equilibrium), and if we get too little sleep, then we'll tend to sleep more in response, and vice versa (restoring force). But it's a dubious analogy at best.

A [damped](http://en.wikipedia.org/wiki/Damping) harmonic oscillator is one with damping, which *tends to reduce the amplitude of oscillations*. So, like air resistance in the case of the pendulum, which eventually causes it to stop swinging.

I'm not sure what the sleep-based analogy for damping would be.

There's a standard equation for defining a (weakly) damped harmonic oscillator. It looks like this:

[![](/images/simple-harmonic-sleep/78730_0.png)](/images/simple-harmonic-sleep/78730_0.png)

Where:- *A0* is the initial displacement, the *e* bit is the decaying term, *gamma* is the damping coefficient (which determines how quickly the oscillations decay), *cos()* is the oscillating term, *omega* is the (damped) frequency of oscillation, *t* is time (in days), *phi* is the phase shift, and *C* is the equilibrium amplitude.

So working out the variables from the data, the model equation for my sleep looks something like this

[![](/images/simple-harmonic-sleep/79122_0.png)](/images/simple-harmonic-sleep/79122_0.png)

And the graph looks like this

[![](/images/simple-harmonic-sleep/wolframalpha-graph1.png)](/images/simple-harmonic-sleep/wolframalpha-graph1.png)

And to prove I'm not entirely crazy, here are the real values and the model values plotted together

[![](/images/simple-harmonic-sleep/data-model1.png)](/images/simple-harmonic-sleep/data-model1.png)

Not a bad fit, right? [[error](http://en.wikipedia.org/wiki/Mean_square_error) 0.19]

In fact, you might notice the real data is still oscillating a little. But the equation outlined above tends to a constant amplitude of 8.3 (no more oscillations).

To account for this, we could add a baseline oscillation term

[![](/images/simple-harmonic-sleep/79124_0.png)](/images/simple-harmonic-sleep/79124_0.png)

And fitting the data again, here's what the graph looks like

[![](/images/simple-harmonic-sleep/data-model2.png)](/images/simple-harmonic-sleep/data-model2.png)

Arguably, a *slightly* better fit. [error 0.16]

So yeah. Basically, I'm procrastinating..

Oatzy.

[Just gotta be careful not to hit [resonant](http://en.wikipedia.org/wiki/Resonance) [sleepquency](http://en.wikipedia.org/wiki/Coma)]
