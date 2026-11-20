---
layout: post
title: Fibonacci's Rainstorm
date: '2011-06-25T00:50:00Z'
author: Oatzy
tags:
- collatz
- music
- fibonacci
- markov chain
- nerd
- maths
modified_time: '2011-06-24T17:50:27.438-07:00'
thumbnail: /images/fibonaccis-rainstorm/notes.jpg
blogger_id: tag:blogger.com,1999:blog-14769935.post-6175780257131559206
blogger_orig_url: https://oatzy.blogspot.com/2011/06/fibonaccis-rainstorm.html
---

A couple years back I got it in my head that I was going to try and write a musical about time travel.

Yeah, I don't know either.

But perhaps the maddest thing about that idea is that I have next to no musical training. Not that I'm the sort to let that stop me. So instead, the plan was to try and create music using maths. Which is a little weird.

But not actually as mad as it sounds. After all, [Pythagoras](http://en.wikipedia.org/wiki/Pythagoras#Musical_theories_and_investigations) (yes, that Pythagoras) was the first - or so the legend goes - to study the [maths of harmonics](http://en.wikipedia.org/wiki/Pythagorean_tuning), and why certain sounds are more pleasing to the ear than others.

It's all to do with fractions. But I won't go into all that because it's not relevant to my thing - there's a good, brief explanation in this video, [How to Solve a Song with Math](http://igniteshow.com/videos/how-solve-song-math-ep-85).

**Musical Integers**

The basic idea was as simple as this - you assign an musical note to each integer - say, starting with *1 = Middle C*, *2 = C#*, etc. though there are other methods of assignment - then generate integer sequences and seeing what they sound like.

For a good example of this sort of thing, here's mathemusician Vi Hart on the [music of pi](http://youtu.be/XJtLSLCJKHE).

After playing around with various functions, what I settled on where that *Hailstone numbers*; which I misremembered as being called rainstorm numbers.

**Collatz Conjecture**

The [Collatz Conjecture](http://en.wikipedia.org/wiki/Collatz_conjecture) (also known as the hailstone numbers) works something like this

[![](/images/fibonaccis-rainstorm/collatz_conjecture.png)](http://xkcd.com/710/)

Well, all except the last sentence fragment. The actual idea is that, regardless of what starting number you pick, the sequence will always end on the number 1 (full details on the [wiki page](http://en.wikipedia.org/wiki/Collatz_conjecture)).

The *Collatz Conjecture* is currently unproven, though recently someone published a [proposed proof](http://science.slashdot.org/story/11/06/05/1446209/Collatz-Proof-Proposed-Hailstone-Sequences-End-In-1) - currently [under scrutiny](http://www.reddit.com/r/math/comments/hqqph/collatz_3n_1_conjecture_solved/c1xp6iu). But that's a whole other story.

So you pick some number, generate the sequence and see what it sounds like. Here's the sequence for 12 - [Collatz-12](http://soundcloud.com/oatzy/collatz-12)

That is - *12, 6, 3, 10, 5, 16, 8, 4, 2, 1*

The problem with using hailstone numbers is that it has the potential for massive jumps - for example *7, 22, 11, 34, 17, 52*, etc - and such a sequence would not sound pleasing (this goes back to Pythagoras).

**Lateralis**

So my second idea was to combine it with the [Fibonacci Sequence](http://en.wikipedia.org/wiki/Fibonacci_sequence) - that is *1, 1, 2, 3, 5, 8, 13*, etc - where each number in the sequence is the sum of the two preceding numbers.

This was actually inspired, slightly, by the *Tool* song *[Lateralis](http://youtu.be/EDlC7oG_2W4)*, where the syllables of the lyrics form a rising and falling Fibonacci Sequence:

> *Black / then / white are / all I see / in my infancy / red and yellow then came to be / reaching out to me / lets me see.*

So the idea was to perform the *Collatz algorithm* on the numbers of the *Fibonacci sequence* - which sounds something like this - [FibCollatz](https://soundcloud.com/oatzy/fib-collatz) 

*1 / 1 / 2, 1 / 3, 10, 5, 16, 8, 4, 2, 1 / 5, 16, 8, 4, 2, 1 / 8, 4, 2, 1*

**Finishing Touches**

Now the next part's a bit fuzzy. While I still have the notebook in which I worked out the tune, my notes aren't exactly clear.

[![](/images/fibonaccis-rainstorm/notes.jpg)](/images/fibonaccis-rainstorm/notes.jpg)

But, basically, what happened was that the resulting tune (see above) was far too erratic in places. So I made a lot of modifications to it, but still based vaguely on patterns in the generated tune.

And the final touch I added to make the tune sound richer was chords. Again, I didn't know anything about chords. But a quick look on [wikipedia](http://en.wikipedia.org/wiki/Chord_%28music%29#Triads) told me how to make major and minor chords, so I decided to add the minor chords of the first notes of each bar.

Here's what the final tune sounds like this - [Fibonacci's RainStorm](https://soundcloud.com/oatzy/fibonaccis-rainstorm)

Yes, it's a bit short and basic. But all things considered, I'd say I did pretty well.

**More Math Music**

I've already [mentioned above](http://youtu.be/XJtLSLCJKHE) the music based on the digits of pi.

There was also a guy who worked out a way to convert games of [chess into music](http://jonathanwstokes.com/2011/02/14/chess-music/).

And, as mention briefly in a [previous post](https://oatzy.github.io/2011/04/21/markovs-next-tweet.html), you can go (almost) completely random and generate music using Markov chains - [for example](http://thepasqualian.com/?p=1831).

Oatzy.

[Oh, and I never did write that musical. Not that that should surprise you.]
