---
layout: post
title: The Pirate Game
date: '2015-06-29T02:39:00Z'
author: Oatzy
tags:
- simulation
- game theory
- probability
- programming
- games
- over-thinking
- problem solving
- android
- coding
- java
- maths
modified_time: '2015-07-07T05:11:38.153-07:00'
thumbnail: /images/the-pirate-game/grid.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-8923283408104333702
blogger_orig_url: https://oatzy.blogspot.com/2015/06/the-pirate-game.html
---

A few months ago, my friend was telling me about this mobile game he wanted to make. He, and some of our other friends, are teachers, and this is a game they play with their students. The students apparently love it. And if there were an app version, they'd be willing to pay 59p for it. Or so they say.

Now, as he was explaining the game to me, I thought maybe he was building towards asking for my help. I felt almost betrayed that he didn't. Several years ago, [I'd built a website](http://oatzy.blogspot.co.uk/2011/02/designing-for-free.html) for this friend that he'd had nothing but praise and gratitude for.

A month or so later, I got a text message - "How are you at programming?" For whatever reason, the guy they had originally 'hired' wasn't doing it anymore.

"I'm capable", I replied. I'd done a course in Java at university. Admittedly, that was 'Java for Mathematicians'. And it was also almost 8 years ago. But how hard could it be to pick up again? Just like coding a bicycle. Or something like that..\.

**The Game**

As the title of the blog suggests, its called 'The Pirate Game'. In the classroom it's [played on paper](https://www.tes.co.uk/teaching-resource/the-pirate-game-end-of-term-activity-6258063).

Basically, you have a 7x7 grid filled with items - mostly coins, but also some items that let you do other things. There are attacks that let you, for example, rob or kill other players. There's a shield and a mirror that let you defend against attacks. There's a bank item that let's you save whatever points you have from being stolen, etc. There's a bomb that blows you up (sets your points to zero). And so on.

[![](/images/the-pirate-game/grid.png)](/images/the-pirate-game/grid.png)

This is the prototyping design. The final product will look less utilitarian.

At the start of the game, the players arrange the items in their grids to their liking. The teacher (game) then calls out random squares, and the players get whatever is in that square on their own grid. In the classroom, if a player gets an attack item, they have to raise their hand and tell the teacher who they want to use it on. The winner is whoever has the most points when all the squares have been called.

**Making Games 1: The Right Tools**

In a [previous blog](http://oatzy.blogspot.co.uk/2015/02/designing-general-relativity-based.html), I asserted that making mobile games was difficult. In fact, it turns out to not be so bad with the right framework. In this case I used the popular [LibGdx](http://libgdx.badlogicgames.com/). What's particularly nice about it is that there are a lot of how-to guides, and there's plenty of help for when things go wrong.

As they say, programming is 1% inspiration, 99% Googling.

For anyone interested in making their own Android game, I found these guides particularly helpful,

[LibGdx Zombie Bird Tutorial](http://www.kilobolt.com/zombie-bird-tutorial-flappy-bird-remake.html)\
[LibGdx Game Development Essentials](https://www.geekbooks.me/book/view/libgdx-game-development-essentials)\
[Set up Google Services with LibGdx](http://fortheloss.org/tutorial-set-up-google-services-with-libgdx/)

**HAL9000**

I got a first working version of the game done in the space of about a month - this was just the basic game mechanics, a bare-bones interface, and a single computer opponent that I could play against to check that the mechanics were doing what they were supposed to.

In those first few tests of the game, I found that the computer player kept beating me - at one point, 7 to 1. This seemed strange - neither I nor the computer could choose who we attacked, or which defences we used. So really, there wasn't anything either of us could do to influence the outcome of the game. The winner should have been totally random.

So loosing 7 times out of 8 seemed significant to me. As far as I could tell, the mechanics were working correctly. The only theory I could come up with was that maybe there was some advantage in the order in which we took our turns.

To try and figure out what was going on, I created a simulation. Basically, I re-wrote a very stripped down version of the player and game mechanics in [Python](https://www.dropbox.com/s/dpcenzal4tn7i13/pirate-sim.py?dl=0). I then had two computer players play against each other in 10,000 matches. The results from this were - Player 1: 5005, Player 2: 4995.\
In other words, the winner *was* just random chance. And turn order didn't matter.

If nothing else, this was a lesson in not drawing conclusions from such a small data set - it's not really statistically significant if there are only 8 data points (that's a standard error of ~3). After playing more games, the wins did end up averaging out.

**Making Games 2: Coordinating Players**

Development progressed. I got the full game mechanics working, and added more computer players (Clu and Ultron). I was now able to choose who I wanted to attack and what defences I wanted to use.

But the ultimate goal for the game is to let users play against their (human) friends. This meant I had to do a massive re-write to generalise the interaction mechanics.

Okay, lets look at an example of an interaction. Say I want to swap points with another player. First, my device needs to pop-up a player select dialog. Once I pick a target, the game needs to inform that player that I'm trying to swap points with them. If that player has a shield, their device needs to pop-up a dialog asking if they want to use it. The game then needs to inform me of my target's response - and if the target doesn't defend them self, we need to tell each other what our respective points are so that we can complete the swap.

That's a lot of back and forth to handle. Here are the rough diagrams I drew when I was trying to get the mechanics straight in my head.

[![](/images/the-pirate-game/diagrams.jpg)](/images/the-pirate-game/diagrams.jpg)

I doubt this helps clarifies things for anyone else.

So the way the interaction works in the code is, the attacker sends their target a data object telling them who the attacker is, what attack they're trying to use, and what points they have (though the points aren't visible to the target). Once the target has chosen their defence, they complete their side of the attack processing - so in the swap example, if the target doesn't defend, they set their points to those of the attacker.

The target then sends the attacker's original data, along with the defence they chose (if any) and their (pre-attack) points to all the other players. If the recipient is the original attacker, they complete their side of the attack. Then, all players are shown a notification telling them what happened.

[![](/images/the-pirate-game/dialog-ex.png)](/images/the-pirate-game/dialog-ex.png)

I figured I should give the computer players more piratical names.

All this coordination is done by a turn handler class. And what's nice is the computer players can also interact with each other, and with the local human player, via the turn handler.

All I need to do now is set up the stuff that actually sends the data between network players.

**Game Theory**

Through testing (looking for bugs and the like), I've played this game A LOT. And I've gotten a pretty good feel for how it works. It's actually quite fascinating when you really get into it. (Or maybe that's just Stockholm Syndrome talking).

Information is important to the game. Without it, players would be forced to make their moves at random. And when that happens, winning becomes mostly random chance. This is why players are shown notifications when other players interact - it allows them to strategise.

The most basic strategies are things like - rob people who have lots of points, don't try to rob people who have just been killed (they don't have any points to take), defend yourself when you have a lot of points (if you can). Really, this is just being sensible.

Then there are more subtle strategies. For example, sometimes it's better to lose a lot of points to the bomb or to being killed (removing those points from the game) rather than letting another player take them. Because, you don't need a lot of points to win, you just need more than everyone else.

Given the inherent randomness of the game, a lot of how you play will come down to how risk-averse you are. For example, a particularly risky strategy might be to let an opponent rob you (saving your defences), in the hopes that you can steal back your points, and more, later on.

When you play against humans (rather than AI), a whole bunch of social factors can come into play too. From what I hear, in the classroom, students tend to disproportionately target any members of staff that are playing. Though I can't imagine why.

One other interesting feature of the game is that it sometimes forces players to make disadvantageous moves. There's the bomb item that will take away your points when it inevitably comes up. And if you're in first place, the swap item forces you to give your points, and the lead, to another player.

So yeah, the game's not as simple as it might seem on the face of it.

**Artificial Intelligence**

In the first fully featured version of the game, the computer players made their decisions completely randomly. And that was fine - the game is perfectly playable with random opponents, it's not too easy, and the randoms can and will beat you on occasion. Sometimes by an embarrassing margin.

But random players also do things that don't make sense. So I wanted to create some computer players that used basic strategies to play more intelligently.

For interactions, these intelligent computer players (AI) use literal hit lists and avoid lists. As mentioned above, when two players interact, that information is sent to all other players. For humans, this information is displayed as a notification. For the AI, the information is processed to build/modify the hit and avoid lists.

For example, if Player 1 steals a lot of points from Player 2, then Player 1 is added to the hit list and Player 2 is added to the avoid list. If another player then kills Player 1, Player 1 is removed from the hit list and added to the avoid list. And so on.

If the AI then gets an attack square, they'll first check their hit list for a target. If the hit list is empty, they'll chose a random opponent who isn't on the avoid list. And so on.

There are also various basic heuristics for choosing which defences to use (and when), and for choosing a square when they get 'Choose Next'.

As they are, the AI are quite formidable, and at times frustratingly so. In general, I think it's better to have a mix of random and intelligent computer players. The AI offer a challenge, while the chaotic influence of the random players keeps things interesting.

**Measuring Difficulty**

In the game's current form, you can play against 2-7 computer players, and these players can be either random or 'intelligent' (as above).  That means 33 unique opponent set-ups. Which raises the question - how can we rate the difficulty of any given set-up. 

Obviously it's harder to win when there are more opponents. Specifically, the probability of a random player winning in a game of N random players is 1/N. Think of it like this - if all the players behave in the same way, they are indistinguishable. And if they're indistinguishable, they must all have the same probability of winning (turn order doesn't matter).

The same logic applies to intelligent computer players (AI) - since they all follow the same set of rules, they must also be indistinguishable from each other. Therefore, the odds of an AI winning in a game of N AI players must also be 1/N .

But what happens when there's a mix? How much harder are AI to beat than randoms?

To answer that, we can run some more simulations. This time, instead of re-writing code in Python, I created a modified version of the turn handler (see above) within the game project itself. Essentially I just removed all code that related to human players, and added a few bits to track statistics.

I set up the 33 different player configurations, ran 10,000 matches for each, and worked out the probability of winning for an AI player - for simplicity, we're assuming that a human player (playing strategically) is roughly equivalent to an AI.

From those simulations I made this lovely surface plot (using [matplotlib](http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html#toolkit-mplot3d-tutorial)).

[![](/images/the-pirate-game/sim-surface-edit.png)](/images/the-pirate-game/sim-surface-edit.png)

Configurations with more than 7 opponents have been set to zero.

And what we find is AI are roughly twice as hard to beat as randoms - notice the surface is higher on the right hand side (when there are fewer AI).

In other words, your odds of winning in a match against two AI is roughly equal to your odds of winning in a match against four randoms. For simplicity, we're going to assume that the relationship is exactly two to one.

We can now calculate an approximation of the odds of winning as

\[ p(R, I) = \frac{2}{R + 2(I+1)} \]

And if we compare these probabilities to those from the simulations, we find that they are within standard error (order 0.01 for 10,000 trials).

[![](/images/the-pirate-game/prob-surface-edit.png)](/images/the-pirate-game/prob-surface-edit.png)

To get a difficulty rating, we can just turn the probability on it's head, and normalise by the probability for the easiest set-up (2 random opponents). That is,

\[ D = \frac{p_0}{p} = \frac{R + 2(I+1)}{4} \]

This gives us a difficulty rating between 1 and 4, which lets us easily divide the difficulty into three levels - easy, medium, and hard. Though, if your odds of winning in the easiest possible game is only 50:50, can it really be considered 'easy'?

Another nice property of this difficulty rating system is that the difficulty ratios match the probability ratios - that is, your odds of winning a 2 are half your odds of winning a 1, and so on. Specifically, your odds of winning are roughly \( \frac{1}{2D} \)

Incidentally, if we assume our human player instead makes their moves completely at random, then their odds of winning are lower overall - \( p = \frac{1}{R+1+2I} \) - but the difficulty stratification works out the same.

**Conclusion**

Ordinarily, I'd include my code for this sort of thing. But in this case, doing so might undermine my (and my friends') income. And they very kindly told me that I'd get the majority of the profits. Whatever those may ultimately be.

So far we've made a whopping 7p (!) just from having adMob set up in the test builds.

But before we can make any (real) money, we have to actually finish the game. The single player version is mostly done, and should be released in the near future. The last big thing to do is the UI (which is someone else's ~~problem~~ job).

Then the hard part is going to be setting up multi-player with Google Play Services. In particular, because there aren't any good guides (that I can find) for setting up Google multi-player with LibGdx.

When it is done, I'll post links and such here for anyone that might be interested.

*<strong>[edit]</strong>* - If you want to try the current beta, you can get it [here](https://play.google.com/store/apps/details?id=com.cavillum.pirategame.android).

Also, given that making an Android game has turned out to be much easier than I expected, I may in fact make the previously discussed relativity game myself (once the Pirate Game is finished). In that case, I might also provide my code.

Oatzy.

[I'd love to make an AI that uses machine learning to counter human players' personal strategies.]
