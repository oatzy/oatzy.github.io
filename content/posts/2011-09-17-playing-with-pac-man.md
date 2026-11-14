---
layout: post
title: Playing with Pac-Man
date: '2011-09-18T02:02:00Z'
author: Oatzy
tags:
- nerd
- games
- infographic
- over-thinking
- dreams
- pac-man
- graph
- graph theory
- problem solving
- hypothetical question
- maths
- network
modified_time: '2011-09-17T19:02:12.424-07:00'
thumbnail: /images/playing-with-pac-man/pacman--graph.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-3022113809302593808
blogger_orig_url: https://oatzy.blogspot.com/2011/09/playing-with-pac-man.html
---

**What the Puck?**

For those unfamiliar, [Pac-Man](http://en.wikipedia.org/wiki/Pacman) is an old arcade game, where you play as a cheese pizza trying to collect pellets while being chased round a maze by four whimsically named ghosts. Although really, if you are unfamiliar with Pac-Man, there's something wrong with you. Anyway, you can have a play online [here](http://www.thepcmanwebsite.com/media/pacman_flash/).

The four ghost are *Blinky*, *Pinky*, *Inky*, and *Clyde*. For a good explanation of the ghosts' behaviours, [here](http://gameinternals.com/post/2072558330/understanding-pac-man-ghost-behavior)'s a post from the tragically short-lived '[Game Internals](http://gameinternals.com/)' blog.

*tl;dr* Blinky chases, Pinky ambushes, Inky teams up with Blinky, and Clyde does pretty much whatever the fuck he wants. But really, you should read the article.

And as for the origin of the name, I'll let [Scott Pilgrim](http://youtu.be/y6x4P6Afje4) explain. Or if you prefer to read, [wikipedia](http://en.wikipedia.org/wiki/Pacman#Development).

**Wakking Round in Circles**

[Graph Theory](http://en.wikipedia.org/wiki/Graph_theory) is a fantastic area of maths. Graph Theory can find you the [shortest route](http://en.wikipedia.org/wiki/Shortest_path_problem), help you get out of a [maze](http://en.wikipedia.org/wiki/Maze_solving_algorithm), tells you how to [colour a map](http://en.wikipedia.org/wiki/Four-color_theorem) so no adjoining regions are of the same colour, to [reconstruct](http://www.pnas.org/content/98/17/9748.long) DNA fragments, and help you find the [best route](http://en.wikipedia.org/wiki/Traveling_salesman_problem) for sight-seeing. Among many [other things](http://en.wikipedia.org/wiki/Graph_theory#Applications).

But sadly graph theory tends to be covered more in Computer Science courses than Maths courses. So for myself, i have to be content with [books](http://www.amazon.co.uk/Nets-Puzzles-Postmen-exploration-mathematical/dp/0199218439/ref=sr_1_1?ie=UTF8&qid=1316307859&sr=8-1) and the internet. Not that I let such thing hold me back.

So the question is this - *Find the optimal route around the Pac-Man maze*

What we want to do is find a route around the maze while collects every pellet. Or in graph theory terms, a route which travels along every edge at least once.

First of all, we need to turn the maze into a network graph. For this, we place a node at each junction, and join pairs of nodes according to whether or not there is a direct route between the pair.

So here's what the maze looks like, beside what the graph of that maze looks like.

[![](/images/playing-with-pac-man/pacman--graph.png)](/images/playing-with-pac-man/pacman--graph.png)

The blue edges are the ones with pellets. The red edges are the ones without pellets, which you don't necessarily have to visit.

And we can assign to each edge a 'weight' - i.e. the distance (in grid squares) between the pairs of nodes

[![](/images/playing-with-pac-man/pacman-weight-graph.png)](/images/playing-with-pac-man/pacman-weight-graph.png)

Now, first of all, we note that there are a lot of node where an odd number of edges meet (with odd degree). What this means is that the graph is not [Eulerian](http://en.wikipedia.org/wiki/Eulerian_path) - what that means is, there doesn't exist a route around the graph which visits each edge *exactly* once.

Which means that we will definitely have to travel along some paths more than once.

So the optimal path is going to be the one which minimises the total distance traveled. This is an example of the [Chinese Postman Problem](http://en.wikipedia.org/wiki/Chinese_postman), and fortunately, there is an algorithm for finding the shortest route.

Without going into too much detail, what you do is pair up odd nodes, and find the shortest paths between them (using [Dijkstra's Algorithm](http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)). This makes the graph Eulerian, i.e. so that a route that visits each edge at least once exists.

So if we take the bottom corner as an example, there are four node of odd degree (green).

[![](/images/playing-with-pac-man/example-chinese-comb.png)](/images/playing-with-pac-man/example-chinese-comb.png)

By finding the shortest paths between pairs of odd nodes (red), we can make this mini-graph Eulerian - i.e. so all nodes have even degree. This means we can find the optimal tour around the graph (right). In this case we have to travel an additional 12 units.

Of course, it gets more complicated when you're working with the full Pac-Man graph.

When there are more than two nodes of odd degree, you also have to find the combination of pairings which minimises the total tour size. For an idea of scale, there are 20 odd nodes in the Pac-Man graph. That means there are 654,729,075 pair combinations to check and compare. And you have to [run](http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Running_time) Dijkstra's algorithm 10 times for each of those permutations. It adds up.

So instead, I took the essence of the algorithm and constructed a route by hand. This is not necessarily the optimal route. For this route, you have to travel an extra 60 units - including 9 units along a path segment that doesn't contain any pellets.

[![](/images/playing-with-pac-man/pacman-path.png)](/images/playing-with-pac-man/pacman-path.png)

There are other paths around the maze which cover (and recover) the same same ground as the above solution, and others that double back over different ground, but that add up to the same distance.

One constraint, in the case of Pac-Man, is that the path has to start at the point near the bottom of the maze, where Pac-Man starts in the game.

But also, it doesn't matter where the tour finishes (where as, the Chinese Postman starts and finishes at the same point). This means modifications to the 'optimal' solution may be possible/required.

In the bottom-corner example, we can eliminate some of the extra paths (up to 9 units worth) if we don't care where we end up.

If I ever get around to programming and running the proper algorithm, I'll let you know what the 'proper' solution is. And if you can find a better solution, let me know.

Of course what I haven't taken into account is the fact that, as you're making your way around the maze, you're also trying to avoid ghosts. I'll be honest, this path finding was more of an intellectual exercise than anything practical. You can find some strategic tips [here](http://strategywiki.org/wiki/Pac-Man/Tips).

**This Maze Ain't Big Enough For the Both of Us.**

If you follow me on Twitter, you may have already read about this - in a dream I formulated a multiplayer version of Pac-Man. But weird, subconscious machinations aside..

I looked it up on wikipedia, and there was already a multiplayer Pac-Man - [Pac-Man Vs.](http://en.wikipedia.org/wiki/Pac-Man_Vs.) But in that game you have one player playing as Pac-Man, and any additional players as ghosts. The aim is for the Pac-Man player to collect pellets and for ghost players to stop them. My idea is better.

First of all, you'd probably need to make the maze bigger. Each player plays as a Pac-Man, and like the normal game, their aim is to collect the most points, while trying to avoid ghosts. The game introduces a new special pellet which lets you cannibalise an opponent Pac-Man (much like the pellet that lets you eat ghosts).

Each player starts with two lives. If they lose both their lives they become a ghost. As a ghost, other ghosts can't hurt you, but you can't collect any pellets. If you catch an opponent Pac-Man, you steal one of their lives (becoming a 'living' Pac-Man again, with one life). If an opponent Pac-Man gets one of the special ghost pellets, they can eat a ghost opponent, killing them for good.

The game ends when all the pellets are collected or when all players are ghosts/dead. The winner is the player with the most points.

Or something like that.

If only I have the know how to make a real, playable version. But, hey, if there happens to be anyone out there reading this who could make it, please do..

Oatzy.
