---
layout: post
title: Lights Out (Game)
date: '2015-01-02T02:54:00Z'
author: Oatzy
tags:
- christmas
- programming
- nerd
- python
- games
- coding
- puzzles
- random
modified_time: '2015-01-01T18:54:46.834-08:00'
thumbnail: /images/lights-out-game/lightsout-ex.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-30923740457024521
blogger_orig_url: https://oatzy.blogspot.com/2015/01/lights-out-game.html
---

I was watching this year's [RI Christmas Lectures](http://www.rigb.org/christmas-lectures), and it reminded me of this game I had when I was much younger. It was, I think, a Christmas present from my grandparents, back in '96. It was called *Lights Out*, and it looked something like [this](https://www.google.co.uk/search?q=lights+out+game&source=lnms&tbm=isch&sa=X&ei=cd6lVO_0CovB7AaMjIHYDg&ved=0CAgQ_AUoAQ&biw=1366&bih=696).

Basically, the console had a 5x5 grid of these rubbery, transluscent buttons with little red lights underneath them. When you press a button, that button and the four adjacent buttons switch state - light on to light off, or off to on. So, in the example below (where blue square are lights), if you press the centre square, the centre square turns off and the four adjacent squares turn on.

[![](/images/lights-out-game/lightsout-ex.png)](/images/lights-out-game/lightsout-ex.png)

In the game, you're given a pattern of lights, such as the one above, and the task is to press buttons until all the lights are out.

Interestingly, in the pattern above (on the left), you can clear the board by just pressing the squares that are on at the start (in any order).

Anyway, I was reminded of that. Meanwhile, I'd been learning some [Pygame](http://www.pygame.org/) for this other thing (that I'll talk about in a later blog). Now, Pygame is a [Python](https://www.python.org/) library for making games (amongst other things). So you can probably see where this is going..\.

Coding a 'Lights Out' clone was straightforward enough - the code is short and not too complicated. The above images are actually screenshots. You can look at my code/download it [here](https://www.dropbox.com/s/pcjmz11a0jncuqf/lightsout.py?dl=0). You'll need Python and Pygame to run it.

This is a very threadbare version of the game. You can load a level as a text file of five lines of ones and zeros, like [here](https://www.dropbox.com/s/927jmw3yw43nzc0/level.txt?dl=0). Or else you can just play from a blank board - make patterns then try to get rid of them again (not necessarily as easy as it sounds).

If you want something more fancy, or if you don't want to install Python and all that, there are probably loads of playable clones online.

Now, at this point you're probably thinking "Yeah, that's great. But what about the maths of Lights Out?". And you'd be damn right to ask. If you're interested, there's a good summary, as well as links to articles/papers, on the [wikipedia page](https://en.wikipedia.org/wiki/Lights_Out_%28game%29). I don't want to just repeat what's written there. Basically, it all comes down to [linear algebra](https://en.wikipedia.org/wiki/Linear_algebra).

Anyway, have fun with that.

Oatzy.

[Call this a late Christmas present.]
