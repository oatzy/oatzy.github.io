---
layout: post
title: Snakes and Ladders
date: '2011-01-29T02:12:00Z'
author: Oatzy
tags:
- markov chain
- nerd
- python
- infographic
- over-thinking
- snakes and ladders
- random
- statistics
- graph
- programming
- everyday maths
- problem solving
- hypothetical question
- maths
- modelling
- network
modified_time: '2011-01-29T05:50:40.907-08:00'
thumbnail: /images/snakes-and-ladders/snl-network-graph.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-6032554309152356465
blogger_orig_url: https://oatzy.blogspot.com/2011/01/snakes-and-ladders.html
---

Or *Chutes and Ladder*, if you're American. Yes, I am talking about the board game.\
The idea came from having read about people analysing Monopoly with simulations, [Markov chains](http://en.wikipedia.org/wiki/Markov_chains) and the likes. You can read about it in [Math Hysteria](http://www.amazon.co.uk/Math-Hysteria-Fun-games-mathematics/dp/0198613369/ref=sr_1_1?ie=UTF8&s=books&qid=1296265407&sr=8-1) by [Ian Stewart](http://en.wikipedia.org/wiki/Ian_Stewart_%28mathematician%29) or find a similar discussion [here](http://www.tkcs-collins.com/truman/monopoly/monopoly.shtml).

In the book, Professor Stewart also suggests that the reader might like to try the same for Snakes and Ladders. So I did\*.

If you're not familiar with Snakes and Ladders and how it works, you had a very deprived childhood. There's an example game board below

[![](http://upload.wikimedia.org/wikipedia/en/b/ba/Cnl03.jpg)](http://upload.wikimedia.org/wikipedia/en/b/ba/Cnl03.jpg)

[[wikipedia](http://en.wikipedia.org/wiki/Snakes_and_ladders)]

I don't know if or by how much game boards vary. But for simplicity, I'm assuming this is a representative layout. Variations aren't likely to dramatically affect the overall behaviour.

**Simulating the Game**

You start with a 'board' with a value for each square. All squares start with a value of 0. You can simulate the dice roll by randomly picking a number between one and six and move accordingly. Whatever square you land on, you add one to that square's value. If you land on a snake or a ladder, you move along it. Repeat until you get to square 100.

At the end, you have a record of how many times each square was visited.

Here's a network graph of all possible moves.

[![](/images/snakes-and-ladders/snl-network-graph.png)](/images/snakes-and-ladders/snl-network-graph.png)

Over-arcs are forward movements (dice rolls and ladders), under-arcs are backwards movements (snakes).

One run of the simulation is equivalent to one possible game. So what you do, is run the simulation, say, *10,000* times, and measure things like, how many times you land on each square, average or minimum number of turns it takes to get to the end, etc.

There is a way of solving this exactly, and mathematically, as discussed for Monopoly in Ian Stewart's book, and indeed as was done in [this paper](http://www.divbyzero.ca/oberman/w/images/c/cc/SnakesandLadders.pdf) [pdf]. But this way is much easier.

You can get the code [here](http://dl.dropbox.com/u/4635169/Snakes-and-Ladders.py).

**Results**

Here's a graph of number of times each square is landed on (out of 10,000 simulations). Snakes are green, ladders are red, arcs show which squares are connected.

[![](/images/snakes-and-ladders/Snakes-n-Ladders.png)](/images/snakes-and-ladders/Snakes-n-Ladders.png)

And you've got this slightly weird, overall, wave shape. And obviously, the snake and ladder landing squares are outliers - most visited ladders, *36-44* and *28-84*; most visited snakes, *47-26* and *49-11*.

NB/ technically I shouldn't include the 'entrances' of snakes and ladders in the graph, since when they're landed on, you move straight to the 'exits'. But for interests sake, they are included. They aren't included in the moves count as separate moves.

You can also graph the number of moves it takes to get to the end

[![](/images/snakes-and-ladders/Moves-dist.jpg)](/images/snakes-and-ladders/Moves-dist.jpg)

The minimum moves is *7*, and interestingly, you can also derive that answer from the network graph - that is the absolute [minimum](http://en.wikipedia.org/wiki/Snakes_and_ladders#Mathematics_of_the_game).

In this simulation, the [mode](http://en.wikipedia.org/wiki/Mode_%28statistics%29) is *21* and the average is *36.2*. The maximum, in this case, is effectively around *215*. But theoretically, if you were really unlucky you could keep landing on the same snake over and over; in which case, the maximum number of moves tends to infinity.

And, the last thing to look at is how much more likely you are to land on a snake than a ladder. First of all, there are (typically) 10 snakes and 9 ladders, so the simple answer would be 1.11 times more likely.

But when you go down a snake, as mentioned above, there's a chance you can go down the same snake again (or down other snakes or up other ladders). So it turns out, you're actually *1.23* times more likely to land on a snake than a ladder. Which isn't a dramatic difference; but the important thing is, you need no longer wonder.

On average, you'll land on about *4* snakes and *3.2* ladders per game.

**End Games**

Say you land on square 97 and roll a four; there are three possible ways to end the game:

*Past the End* - assume that moving past 100 means you've reached the end (this is what I did above).\
This is the easiest way to end the game.

*Roll Again* - stay in the same square and roll again until you roll a 3 (or less).\
This is effectively the same as the above, except (on average) it takes more rolls of the dice (but not necessarily more moves) to reach the end.

*Loop Back* - move three spaces forward (to 100) then one space back. Repeat until you land exactly one square 100.

This last one takes longer to get to the end, and has a greater risk of you landing on the snakes on squares 95 or 98, sending you back to 75 and 78 respectively.

And that's demonstrated in the graph below - both lines are effectively the same until about the last 25 squares, where the 'loop back' diverges towards more visits (as expected).

[![](/images/snakes-and-ladders/loopback-comp.jpg)](/images/snakes-and-ladders/loopback-comp.jpg)

You also have the moves distribution,

[![](/images/snakes-and-ladders/loop-move-dist.png)](/images/snakes-and-ladders/loop-move-dist.png)

which in this case is broader and pushed to right slightly; the average now *43.3.* Note also that *7* is still the minimum number of moves.

Also, in the 'loop back', the odds of landing on a snake goes up again - now *1.41* times more likely than a ladder. So on average, you'll land on about *5.2* snakes and *3.7* ladders per game.

**Triple Sixes**

Another [rule](http://en.wikipedia.org/wiki/Snakes_and_ladders#Playing) you could chose to include is - if you roll three 6s in a row, you go back to square 'zero'.

According to the simulation, you'll roll a triple six in about *13.4%* of games, on average.

But the triple six seems to have no significant effect on what squares you land on, the number of snake and ladders you'll land on, or oddly enough, the distribution of how many moves it takes to get to the end. This is probably because throwing triple sixes is so rare.

So there you go. Bet you didn't think snakes and ladders could be so complicated.

Oatzy.

\* truth be told, this is something other people have already done. But I like to try these things for myself.
