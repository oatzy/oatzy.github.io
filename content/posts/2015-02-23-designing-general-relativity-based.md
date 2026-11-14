---
layout: post
title: Designing a General Relativity Based Casual Game
date: '2015-02-23T21:51:00Z'
author: Oatzy
tags:
- simulation
- gravity
- mathematical methods
- python
- games
- geometry
- general relativity
- programming
- trigonometry
- physics
- maths
- modelling
modified_time: '2015-02-23T13:51:30.869-08:00'
thumbnail: /images/designing-general-relativity-based/game-mockup-alt1.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-2504472335556556518
blogger_orig_url: https://oatzy.blogspot.com/2015/02/designing-general-relativity-based.html
---

Let's suppose, for the sake of arguing, that I'm unemployed. It'd pretty great if there were a way I could make a quick buck (or a quick quid, in my case). Obviously, the solution is to make a super addictive mobile game. Then I can just sit back and watch the cash come pouring in.

Okay, so that's a pretty terrible plan - making a mobile app of any kind is no trivial thing, and there's no guarantee of making any significant amount of money (or any money at all). Still, I thought about it, and wondered - if I were to make a game, what would I do. This is one of the ideas I came up with.

**Game Concept**

A common type of casual game is the [physics-based game](https://en.wikipedia.org/wiki/Game_physics) - that is, a game where objects obey a form of classical Newtonian mechanics: your Angry Birds, your Flappy Birds, your games that don't involve birds. So, for example, when you catapult an angry bird, [it follows a parabolic path](http://www.wired.com/2010/10/physics-of-angry-birds/) like a real bird would (drag not-withstanding).

And that's all fine, but I wondered if you could make a game based on non-classical physics - quantum mechanics, relativity, that sort of thing.

Now, I don't want to call this '[Interstellar](http://www.imdb.com/title/tt0816692/): The Game' (not least because of copyright). That is, however, a good short hand for the idea behind the game.

The idea is this: you've been off exploring space, and now it's time to go home. So the main objective is to get back to Earth as quickly as possible, whilst dodging obstacles like planets, stars, black holes. But these massive objects have a gravitational pull, which can make maneuvering a little trickier, especially if you get too close to a black hole.

On the other hand, you can use massive objects to get a speed boost, by doing for example a [powered flyby](https://en.wikipedia.org/wiki/Oberth_effect). But being close to massive objects for too long (black holes in particular) will cause time dilation, which might make you late home.

**Game Construction**

The way I imagine the game is as a '[side-scroller](https://en.wikipedia.org/wiki/Side-scrolling_video_game)', where you move right to left (assuming the phone/tablet is held in landscape). I figure it would be a [top-down](https://en.wikipedia.org/wiki/Video_game_graphics#Top-down_perspective) view, moving in the x-direction with the spaceship - i.e. the sprite would be fixed in the x-direction, with freedom of movement up and down. All the obstacles would then move towards the sprite in the negative x-direction.

Here's what a (non-relativistic) binary orbit looks like from a frame of reference moving in the x-direction with the particle (blue).

<iframe allowfullscreen frameborder="0" height="375" mozallowfullscreen src="//player.vimeo.com/video/119661162" webkitallowfullscreen width="500">

</iframe>

In the code, this is done by calculating the particle velocity as normal, but instead of adding the velocity in the x-direction to the particle, you subtract it from all the obstacles.

For the sprite's up-down movement, you could either constrain the player to within the screen, or else if they drift off the edge of the screen, it would be a 'lost in space' game over.

Level construction can either be done by hand, or levels can be generated randomly / [procedurally](https://en.wikipedia.org/wiki/Procedural_generation) by adding massive objects of varying type/size/mass etc. at various points along the game map. I'd say go for random/procedural, since that makes creating levels easier, and would mean there are effectively unlimited levels. Though it might be worth storing generated levels for replayability.

For the representation of black holes, you could show an [accretion disc](https://en.wikipedia.org/wiki/Accretion_disc) ([like they did in Interstellar](http://www.wired.com/2014/10/astrophysics-interstellar-black-hole/)), have a background star field that's [gravitationally lensed](https://en.wikipedia.org/wiki/Gravitational_lens), or show a dotted line for where the event horizon is. Alternatively, you could do nightmare mode - give no visual indication of a black hole, and let the player infer its presence from its gravitational pull.

I tend to think that controls should be kept simple, and should be appropriate to the medium - in other words, no on-screen d-pads on touchscreens (if you can help it). Instead, I'd say use four directional swipes for a speed boost in whichever direction. In terms of code, this would be done by adding some constant to the velocity in the direction of the swipe.

One thing to remember is that in space there is no drag - nothing to slow you down (gravity notwithstanding). Steering like this can be surprisingly tricky. If you accelerate left, you will keep moving leftwards until you accelerate right to counter balance.

On the other hand, no drag means the player could keep accelerating forward until they're going arbitrarily fast. To stop this, you could put a limit on how many times the player can accelerate - for example, say that there's a limited amount of fuel. This also means the player would have to use their fuel wisely - baring in mind that breaking counts as accelerating. This makes tricks like gravitational assists even more important.

[![](/images/designing-general-relativity-based/game-mockup-alt1.png)](/images/designing-general-relativity-based/game-mockup-alt1.png)

Anyway, having an idea is all well and good, but really an idea isn't worth much if you can't prove that it's viable. So..\.

**Game Mechanics**

*<strong>Preamble</strong>*

I studied theoretical physics at university, and that included a module on General Relativity. But that module only covered the basics. As the lecturer pointed out, General relativity is a graduate level topic.

I read a bunch of articles for this blog, and have tried to get as scientifically accurate as possible - or at least I've tried to avoid making massive errors. But even so, there are numerous assumptions, approximations, and inaccuracies in this formulation. So just bear that in mind - I don't necessarily know what I'm talking about. Do feel free to offer corrections.

*<strong>Prototyping</strong>* - For coding the prototype/simulations I used Python with [PyGame](http://pygame.org/).

In PyGame, coordinates are defined with the origin (0,0) in the top right corner. This isn't a problem mathematically, it just means the graphical layout is 'upside-down'.

To make the videos in this post, I added the line

``` python
pygame.image.save(screen, 'output/frame%05d.png' % framenum)
```

to the code's main loop to save individual frames as a series of images (you'll need to iterate '*framenum*'). I then used '[ImageJ](http://www.andrewnoske.com/wiki/ImageJ)' to convert those images to (avi) video.

**<em>Terminology</em>** - I'm going to refer to moving objects as 'particles', 'planets', or as a 'spaceship' in the context of the game. I'll refer to static, gravitating objects as 'obstacles', '(massive) bodies', or 'stars'. In images and videos, planets are blue, and stars are yellow.

*<strong>Units</strong>* - I chose to use 'pixels' as the unit of length, and 'frames' as the unit of time. In this case, velocity is measured in 'pixels per frame' (px/fr).

This is useful, because it means the velocity of our particle is updated as \(v(t) = v(t-1)+a(t)\) and the position is updated as \(x(t) = x(t-1)+v(t)\). For my simulation, I used a frame rate of 50fps.

*<strong>Physical Constants</strong>* - We could use [geometrised units](https://en.wikipedia.org/wiki/Geometrized_unit_system), where the [Gravitational Constant](https://en.wikipedia.org/wiki/Gravitational_constant) (G) and the [Speed of Light](https://en.wikipedia.org/wiki/Speed_of_light) (c) are both set equal to one. In that case we wouldn't need to include them in the maths/code. However, my inner-mathematician likes generality, so I'm going to keep them around.

The constant 'G' only ever appears alongside obstacle masses (as GM), so we can set it to one and say that it's value is absorbed into the (otherwise arbitrary) mass values. It's worth keeping G around though, so we can easily tweak the strength of gravity, if need be.

The speed of light controls the strength of relativistic effects - larger c, weaker relativity. In my code I set the speed of light to c = 12 px/fr. This seems to make things behave in a way that looks 'right'.

**<em>Object Properties</em>** - We could try to go for a certain level of realism - try, for example, to work out a conversion between real world distances and pixels, try to get everything to scale. But that's too much faffing. Besides, if everything were to scale, a 1px Earth would orbit at a distance of 23000px around a 100px sun.

For obstacle masses, I set M = 500 (arbitrary units). The particle mass isn't really important since it can be cancelled out in all the equations. From a theoretical perspective, all that matters is that it's much smaller than the obstacle masses. I set both the obstacles and particle radii to 12.5 pixels (25x25px sprites). Object radii aren't important outside of collision handling.

**Newtonian Gravity**

For particle acceleration, we start with [Classical Newtonian gravity](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation).

\[ a = \frac{G M}{r^{2}} \]

where G is the gravitational constant, M is the mass of the gravitating body (the obstacle) and r is the distance between the centres of our particle and the obstacle. We're assuming that the particle is moving in a 2D plane, so we have \(r = \sqrt{dx^{2} + dy^{2}}\), where \(dx = x_p - x_{ob}\) and \(dy = y_p - y_{ob}\) are the x and y distances between the particle and obstacle.

[![](/images/designing-general-relativity-based/radial-distance-diagram.png)](/images/designing-general-relativity-based/radial-distance-diagram.png)

This gives us the magnitude of the acceleration, pointing from the centre of the particle to the centre of the obstacle. For our purposes, we need to resolve this acceleration into x and y components.

[![](/images/designing-general-relativity-based/angle-resolve-diagram-alt1.png)](/images/designing-general-relativity-based/angle-resolve-diagram-alt1.png)

The components are given by

\[ \ddot{x} = -\frac{G M}{r^{2}} \cos(\theta) \equiv -\frac{G M}{r^{3}} dx\\ \\
\ddot{y} = -\frac{G M}{r^2} \sin(\theta) \equiv -\frac{G M}{r^{3}} dy\]

Where \(\theta = \arctan\left(\frac{dy}{dx}\right) \) is the angle between the x-axis and the position/acceleration vector. The [double dots](https://en.wikipedia.org/wiki/Notation_for_differentiation#Newton.27s_notation) mean 'second derivative with respect to time', i.e. acceleration.

If there are multiple gravitating objects, we have to calculate the contributions from each, and [add them](https://en.wikipedia.org/wiki/Euclidean_vector#Addition_and_subtraction) all together to get the total acceleration.

\[ \ddot{x} = -\sum_i \frac{G M_{i}}{r_{i}^{3}} dx_{i} \\ \\
\ddot{y} = -\sum_i \frac{G M_{i}}{r_{i}^{3}} dy_{i} \]

As mentioned above, once we have the acceleration we add that to the velocity, then add the velocity to the position to work out where the particle moves to. Below is an example of a Newtonian orbit using the above.

<iframe allowfullscreen frameborder="0" height="375" mozallowfullscreen src="//player.vimeo.com/video/119661161" webkitallowfullscreen width="500">

</iframe>

**General Relativity**

Since we want the game to include [General Relativistic](https://en.wikipedia.org/wiki/General_relativity) effects like time dilation, we also have to take into account the other effects of relativity - in particular, how it modifies particle motion/acceleration.

For simplicity, we're going to assume our obstacles (planets, stars, black holes) are uncharged, and non-rotating. In that case, we use the [Schwarzchild metric](https://en.wikipedia.org/wiki/Schwarzschild_metric), which describes the gravitational field in the vicinity of an (uncharged, non-rotating) massive object.

\[ c^2 d\tau^2 = \left(1 - \frac{r_s}{r}\right) c^2 dt^2 - \frac{dr^2}{\left(1- \frac{r_s}{r}\right)} - r^2 d\theta^2 \]

We're assuming the particle is moving in the 2D plane around the equator of the massive object. \(r_s\) is the object's [Schwarzchild radius](https://en.wikipedia.org/wiki/Schwarzschild_radius) (also known as the 'event horizon' in the context of black holes), defined as

\[ r_s = \frac{2GM}{c^2} \]

Without going into too much detail, [we can derive](http://arxiv.org/pdf/gr-qc/9505010v1.pdf) from the Schwarzchild metric the particle's acceleration in Cartesian-like coordinates as

\[ \ddot{x} = - \frac{G M}{r^3} dx - \frac{3 G M L^2}{c^2 r^5} dx \\ \\
\ddot{y} = - \frac{G M}{r^3} dy - \frac{3 G M L^2}{c^2 r^5} dy \]

Where the first term is the classical Newtonian gravitation, as seen above.

The second term is purely relativistic, and will usually only have a significant effect when a particle is sufficiently close to a massive body's Schwarzchild radius.

The main effect of this term is to increase gravitational acceleration in the vicinity of the massive object, and to cause close orbits to precess, as can be seen below

<iframe allowfullscreen frameborder="0" height="375" mozallowfullscreen src="//player.vimeo.com/video/119661160" webkitallowfullscreen width="500">

</iframe>

Notice that the point at which the particle is closest to the 'star' (the [perihelion](https://en.wikipedia.org/wiki/Perihelion_and_aphelion)) moves over time. This doesn't happen in the classical limit of Newtonian gravity. In fact, explaining the [anomalous precession of Mercury](https://en.wikipedia.org/wiki/Tests_of_general_relativity#Perihelion_precession_of_Mercury) was one of the first pieces of evidence supporting the theory of General relativity.

In the acceleration equation, L is the [angular momentum](https://en.wikipedia.org/wiki/Angular_momentum) (per unit mass) of our particle, and c is the speed of light. Angular momentum (per unit mass) is calculated as

\[ L = \left|r\right| \left|v\right| \sin(\phi) \equiv (dx\ v_y - dy\ v_x) \]

where \(\phi\) is the angle between the radial vector (r) and the velocity vector (v)

[![](/images/designing-general-relativity-based/L-angle-diagram-alt.png)](/images/designing-general-relativity-based/L-angle-diagram-alt.png)

The angle can be calculated as

\[ \phi = \alpha - \theta = \arctan\left(\frac{v_y}{v_x}\right) - \arctan\left(\frac{dy}{dx}\right) \]

where \(\alpha\) is the angle between the velocity vector and the x-axis, and \(\theta\) is the angle between the position vector and the x-axis.

In the two body case, angular momentum is a [constant of motion](https://www.youtube.com/watch?v=iWSu6U0Ujs8), so only needs to be calculated once - say, once the particle's initial position and velocity has been set.

*<strong>Caveat</strong>* - Strictly speaking, the radial length 'r' in the Schwarzchild metric is not the same as the [Euclidian distance](https://en.wikipedia.org/wiki/Euclidean_distance) \(\sqrt{dx^2 + dy^2}\). At least, not when relativistic effects are significant. Rather, r is defined as the circumference of a sphere surrounding the massive body, divided by \(2\pi\). Defining r this way means the length of an interval dr isn't affected by the curving of spacetime near the massive body.

By comparison, an observer falling towards a black hole would see lengths stretching longer and longer the closer they got to the black hole event horizon - an observer at a distance r would measure the interval dr to have a length of \( \left( 1  - \frac{r_s}{r} \right)^{-\frac{1}{2}} dr \).

All this to say, the particle distances displayed in the game (and the simulation videos) are distances in [Schwarzchild coordinates](https://en.wikipedia.org/wiki/Schwarzschild_coordinates), projected onto a Euclidean plane, not distances as viewed by an observer such as our particle/spaceship.

**Relativity for Multiple Bodies**

This is where things get dicey. In the General relativistic limit, combining the fields of multiple massive objects is [not so straightforward](http://cds.cern.ch/record/427018/files/9912113.pdf).

The lazy way of doing this is to just vector sum the relativistic accelerations, like we did for the Newtonian case. This is problematic, though, because it assumes the particle's angular momentum around each massive body is constant. This is not true.

Instead, we can make a simplification - we can sum the Newtonian terms as before, but we'll only consider the relativistic term when we're sufficiently close to any given body. This cut-off is going to be fairly arbitrary. Ideally, we want the 'radius of influence' to be as big as possible, but small enough that the particle can never be within the relativistic limits of more than one body at a time. The main problem here is that the way the game is set up means all the massive bodies are unrealistically close together, so it's hard to make the radius of influence big enough to be ideal. In my code, I chose the cut-off to be \(10 r_s \simeq 70px\).

Now, the angular momentum around this close body is still not constant (although, arguably, it may be sufficient to assume it is). The forces from other local bodies can cause [torque](https://en.wikipedia.org/wiki/Torque), which will change the particle's angular momentum.

[![](/images/designing-general-relativity-based/torque-diagram.png)](/images/designing-general-relativity-based/torque-diagram.png)

Torque is calculated as

\[ \Gamma = \left|r\right| \left|F\right| \sin(\gamma)\ \equiv r_x\ F_y - r_y\ F_x\]

where \(\gamma = \theta_1 - \theta_0 = \arctan(\frac{dy_1}{dx_1}) - \arctan(\frac{dy_0}{dx_0}) \) is the angle between the position vector (r) and the force vector (F), and \(\theta_0\) and \(\theta_1\) are the angles between r and the x-axis, and F and the x-axis, respectively.

For the force from a gravitating body, the torque can be written out as

\[\Gamma = \frac{G M_1 }{r_1^3} \left(dy_0\ dx_1 - dx_0\ dy_1\right) \]

We only need to take into account Newtonain gravitation in calculating torque, since we're already assuming the particle is outside the relativistic limit of these other bodies.

So once the particle enters a massive body's radius of influence, we calculate it's initial angular momentum, as above. Then, in each time step (for as long as the particle is in the radius of influence), we calculate the total torque from all local bodies, and add that torque to the particle's angular momentum (before calculating the new acceleration).

This is a big simplification. But it's good enough, and correct in the limiting case of a single/well isolated body. Especially if the radius of influence can be made sufficiently big.

While we're on torque - if our spaceship accelerates (fires its thrusters) while it is close to a massive body, we will need to take into account any torque from that as well

\[ \Gamma = dx_0\ a_y - dy_0\ a_x \]

Where \(a_x\) and \(a_y\) are the x and y accelerations caused by the thrusters. This is ignoring the details of how a spaceship [actually maneuvers](https://en.wikipedia.org/wiki/Astronautics). If you're interested, you'll have to look into that for yourself.

So putting it all together we have

\[ \ddot{x} = -\sum_i \frac{G M_i}{r_i^3} dx_i \ - \frac{3 G M_0 L_0^{2}}{c^2 r_0^{5}} dx_0\\ \\
\ddot{y} = -\sum_i \frac{G M_i}{r_i^3} dy_i \ - \frac{3 G M_0 L_0^{2}}{c^2 r_0^{5}} dy_0 \]

where \(M_0\) is the body whose radius of influence the particle is within (if any), and

\[L_0 = L_{0}(t-1) +\sum_{i\ne 0} \frac{G M_i}{r_i^3}(dx_i\ dy_0 - dx_0\ dy_i) + (dx_0\ a_y - dy_0\ a_x)\]

**Time Dilation**

For a single massive object, the [time dilation](https://en.wikipedia.org/wiki/Time_dilation) can be derived from the Schwarzchild metric (see above). Dividing through by \(c^2 d\tau \) and rearranging we get

\[&nbsp; \left(1- \frac{r_s}{r}\right)^2 \left(\frac{dt}{d\tau}\right)^2 = \left(1- \frac{r_s}{r}\right)\left(1 + \frac{r^2 \dot{\theta}^2}{c^2}\right) + \frac{\dot{r}^2}{c^2} \]

where the dots mean 'derivative with respect to \(\tau\)'. And since \( \dot{r}^2 + r^2 \dot{\theta}^2 \equiv v_x^2 + v_y^2 = v^2 \), we can re-write and rearrange further to get

\[ dt = \frac{d\tau}{\left(1- \frac{r_s}{r}\right)}\sqrt{1- \frac{r_s}{r}\left(1 + \frac{r^2 \dot{\theta}^2}{c^2}\right) + \frac{v^2}{c^2}} \]

where dt is the '[coordinate time](https://en.wikipedia.org/wiki/Coordinate_time)' - time as measured by an observer at rest, far away from any gravitational fields. For the sake of the game we can say that this represents time as measured on Earth. In reality, the Earths gravitational field does cause it's own time dilation effect. \(d\tau\) is the '[proper time](https://en.wikipedia.org/wiki/Proper_time)' - time as measured by a clock on our spaceship.

Notice, in the limit of a stationary particle, that is \(\dot{r}=r\dot{\theta}=0\), we get the purely gravitational time dilation

\[ dt = \frac{d\tau}{\sqrt{1 - \frac{r_s}{r}}} \]

Similarly, in the limit of \( r \gt\gt r_s\) (i.e. when our particle is far from any gravitating bodies), the time dilation equation reduces to the [Special Relativistic](https://en.wikipedia.org/wiki/Special_relativity) case

\[ dt = d\tau \sqrt{1 + \frac{v^2}{c^2}} \]

Note - in this, the velocity v is the '[proper velocity](https://en.wikipedia.org/wiki/Proper_velocity)' - velocity with respect to proper time. This is different from coordinate velocity - velocity with respect to coordinate time.

While a particle can't have a coordinate velocity greater than the speed of light 'c', because of time dilation it can have a proper velocity greater than 'c'. This doesn't, however, mean that a particle can travel faster than light, since light has a proper velocity of infinity. Coordinate velocity and proper velocity are related by

\[ v_c = v \left(\frac{d\tau}{dt}\right) \equiv \frac{v}{ \sqrt{1+\frac{v^2}{c^2}}}\]

where the equivalence is true in the Special relativistic limit. Notice that when proper velocity equals the speed of light (c), the coordinate velocity equals \(\frac{c}{\sqrt{2}}\) - less than the speed of light.

**Time Dilation for Multiple Bodies**

Here, we once again have the problem of combining the effects of multiple gravitating masses. Some would argue, at this point, that trying to be scientifically accurate is more trouble than it's worth. Still, I'm going to at least try.

To start, we [can](http://www.ipgp.fr/~tarantola/Files/Professional/GPS/Neil_Ashby_Relativity_GPS.pdf) [replace](https://en.wikipedia.org/wiki/Time_dilation#Time_dilation_due_to_gravitation_and_motion_together) the Schwarzchild radius terms with the local (Newtonian) gravitational potentials as

\[ \frac{r_s}{r} = \frac{2GM}{c^2 r} \rightarrow&nbsp; \sum_i \frac{2 G M_i}{c^2 r_i} =&nbsp; \sum_i \frac{2U_i}{c^2} = \frac{2U}{c^2}\]

Where \(U_i\) are the individual [gravitational potentials](https://en.wikipedia.org/wiki/Gravitational_potential) of the various local gravitating bodies.

For the term in \(r^2 \dot{\theta}^2\), we note that \(r^2 \dot{\theta}^2\ = \frac{L^2}{r^2} \), where L is angular momentum (per unit mass). So we can use the same trick we did for combining accelerations - that is, only take this term into account when the particle is within a body's radius of influence.

So putting it all together, we have

\[ dt = \frac{d\tau}{\left(1 - \frac{2U}{c^2}\right)}\sqrt{1 - \frac{2U}{c^2} - \frac{2U_0}{c^2}\frac{L_0^2}{r_0^2 c^2} + \frac{v^2}{c^2}} \]

With \(L_0\) defined as above. Alternatively, we could just omit the angular momentum term since it's of order \(c^{-4}\). In my simulation, it amounted to a ~0.17% decrease in the dilation ratio.

The typical dilation ratio in my simulation was \(\frac{dt}{d\tau} \approx 1.07\), which admittedly isn't significant.

[In the movie](http://iopscience.iop.org/0264-9381/32/6/065001/article) Interstellar, a lot of the time dilation came from the fact that their black hole (Gargantua) was spinning very fast. If you want to do that, you'll have to work it out for yourself - for that you would use the [Kerr metric](https://en.wikipedia.org/wiki/Kerr_metric). With rotating black holes, you'd also need to take into account other effects like [frame dragging](https://en.wikipedia.org/wiki/Frame-dragging).

Of course, we've chosen arbitrary masses, an arbitrary speed of light, distances not to any sort of realistic scale. We can always tweak the specific time dilation to our liking. In particular, if the realistic dilation isn't dramatic enough, we could artificially inflate it. So long as we keep key behaviours, like dilation going to infinity when the particle reaches a black hole event horizon, etc.

**Collision Handling**

[Collision handling](https://en.wikipedia.org/wiki/Collision_detection) is important for figuring out when the game is over - for figuring out if the player crashed into a planet, or fell into a black hole. Now, PyGame has [in-build collision handling](http://www.pygame.org/docs/ref/sprite.html). But where's the fun in that.

The easiest way to check if two circular objects have collided is to check if the distance between their centres is less than the sum of their radii

[![](/images/designing-general-relativity-based/overlap-diagram-alt.png)](/images/designing-general-relativity-based/overlap-diagram-alt.png)

In other words, we have the condition - a collision occurred if \( dx^2 + dy^2 \le (r_p + r_{ob})^2 \).

Easy. There is a special case though - because the particle moves in discrete steps from frame to frame, if the particle is moving fast enough, it could move from one side of an obstacle to the other without ever overlapping.

[![](/images/designing-general-relativity-based/pass-collision-diagram.png)](/images/designing-general-relativity-based/pass-collision-diagram.png)

The basic collision handling would miss this. So this is a little trickier to catch. In the above diagram, I've traced the path going from the particle's position in the previous step to its current position.

We can say that the particle collided with the obstacle if there's a point on that path that's closer to the centre of the obstacle than \( R = r_p + r_{ob} \). In other words, if the particle had moved continuously along the path from \(x_0\) to \(x_1\), would there have been any point(s) where the particle and the obstacle overlapped.

To figure this out, first we find the equation for the line passing through the particles' two positions as

\[ y = m x + c = \left(\frac{v_y}{v_x}\right) x + \left(y_0 - \frac{v_y}{v_x} x_0 \right) \]

(in this case, m and c are gradient and constant, respectively, not mass and speed of light).

Second, we're going to define a function for the distance between a point on the particle's path and the obstacle's centre

\[ f(x) = (x_{ob} - x)^2 + (y_{ob} - y)^2 = (x_{ob} - x)^2 + (y_{ob} - m x - c)^2 \]

Now we're going to look for the point along the path of closest approach to the obstacle. To do that we look for x such that the separation f(x) is minimised. In other words \( \frac{d}{dx} f(x) = 0\)

If you work through the maths, you get

\[ x_{min} = \frac{x_{ob} + m y_{ob} - m c}{1 + m^2} \]

Which gives us the condition - a collision occurred if \(f(x_{min}) \le R^2\) and \(x_0 \le x_{min} \le x_1\) (assuming \(x_0 \le x_1\)).

[![](/images/designing-general-relativity-based/pass-collision-diagram-2.png)](/images/designing-general-relativity-based/pass-collision-diagram-2.png)

Both these collision handlers can also be used to check if the particle crosses a black hole's event horizon - just replace \(r_{ob}\) with \(r_s\), the Schwarzchild radius.

Of course, in the game, the spaceship sprite wouldn't be circular. But, you know. You could create an 'imaginary' circle around the sprite, or give the sprite a radius of zero (so it collides when its centre overlaps the obstacle). Or you could just use a third party library. Either way.

**Bonus: Elastic Recoil**

For my own amusement, I had the particle [elastically recoil](https://en.wikipedia.org/wiki/Elastic_collision) off of the obstacles, as well as the sides of the screen, so that I could just watch it drifting and bouncing about endlessly. It's weirdly hypnotic.

For screen boundaries, you have, for example

[![](/images/designing-general-relativity-based/boundry-recoil-diagram.png)](/images/designing-general-relativity-based/boundry-recoil-diagram.png)

In this case, we flip the particle velocity in the x-direction as \( v_{x}' = -v_{x} \), and move the particle's x position to \( x_{p}' = W - (x_{p} - W) = 2 W - x_p \), where W is the pixel width of the game window. You do the same sort of thing for the other 3 boundaries.

For recoil off obstacles, things are not so straight forward. The procedure works like this: First, check for a collision. Then, find the point along the particle's path where it first makes contact with the obstacle - that is where \(f(x) = R^2\).

[![](/images/designing-general-relativity-based/contact-diagram-alt1.png)](/images/designing-general-relativity-based/contact-diagram-alt1.png)

Finding this point is just a matter of solving a quadratic equation to get

\[ \begin{align*}
x' &amp;= \frac{x_{ob} + m y_{ob}-mc}{1 + m^2} \pm \frac{\sqrt{(x_{ob} + m y_{ob}-mc)^2&nbsp; - (1+m^2)(x^2_{ob} + y^2_{ob}+c^2 - 2 c y_{ob} - R^2)}}{1 + m^2} \\ \\ &amp;\equiv a \pm b
\end{align*} \]

If \(v_x \gt 0\) then x' = a - b, if \(v_x \lt 0\) then x' = a + b

So move the particle back to the point of first contact. Then we want to flip the particle velocity so that the angle of incidence \(\phi\) between the velocity vector (v) and the position vector (r) equals the angle of reflection

[![](/images/designing-general-relativity-based/elastic-recoil-diagram-alt.png)](/images/designing-general-relativity-based/elastic-recoil-diagram-alt.png)

The new velocity is given by

\[v'_x = -\left|v\right| \cos(\beta)&nbsp; \\ \\ v'_y = -\left|v\right| \sin(\beta)\]

with \(|v| = \sqrt{v_{x}^{2} + v_{y}^{2}} \), and

\[ \beta = \alpha - 2 \phi = 2\arctan\left(\frac{-dy}{-dx}\right) - \arctan\left(\frac{v_y}{v_x}\right) \]

where \( \alpha \) is the angle between the x-axis and the old velocity vector (v), and \(\beta\) if the angle between the x-axis and the new velocity vector (v').

Note - in the code I used ['arctan2(y,x)](http://docs.scipy.org/doc/numpy/reference/generated/numpy.arctan2.html#numpy.arctan2)' from the Numpy library, for which the signs of 'x' and 'y' are important. dy and dx are negative in the above because I have the position vector pointing from the particle to the obstacle (opposite to how it's defined).

Finally, we want to move the particle to where it should be from recoiling.

[![](/images/designing-general-relativity-based/recoil-position-diagram.png)](/images/designing-general-relativity-based/recoil-position-diagram.png)

In other words, we want to move the particle to the point along it's new velocity vector, such that it's the same distance from the contact point as it would be if the particle hadn't collided. To do this, we can just resolve the distance \( r' = \sqrt{(x_1 - x')^2 + (y_1 - y')^2} \) in the direction of the new velocity vector, as

\[ x_1 ' = x' - r' \cos(\beta) \\ \\ y_1 ' = y' - r' \sin(\beta) \]

Admittedly, this doesn't work perfectly - sometimes it behaves a little screwy. Especially when the particle spirals in on an obstacle. Of course, none of this recoil stuff is necessary for the game, since you want collisions to end the game. Like I said, this was more for my own amusement.

<iframe allowfullscreen frameborder="0" height="375" mozallowfullscreen src="//player.vimeo.com/video/120176087" webkitallowfullscreen width="500">

</iframe>

**Conclusion**

If you were feeling really ambitious, you could do the game from the first-person perspective of someone on the spaceship - see for example '[Falling into a Black Hole](http://jila.colorado.edu/~ajsh/insidebh/index.html)', or the [Interstellar papers](http://arxiv.org/find/gr-qc/1/au:+James_O/0/1/0/all/0/1).

There are almost certainly things wrong with this 'formulation' of General Relativity. But then, this is meant to be for a game, so it [doesn't need to](https://en.wikipedia.org/wiki/Rationalization_%28making_excuses%29) be 100% scientifically accurate. I did feel like I should make an effort, though. And I'm willing to call this good enough. If you're someone who knows what they're talking about, feel free to offer your thoughts/corrections.

Anyway, I've done my job as a theoretician - now it's up to someone else to actually make the game. If you do, please send me link to the completed game. And maybe give me a name-check? A little kickback would be nice too..\. ;)

You can have a look at my prototype/simulation code [here](https://www.dropbox.com/sh/l4ai8vacc921x9t/AAAp630npPaluD8QhYNhXbf4a?dl=0).

Oatzy.

[Gravity, don't mean too much to me[.](http://www.youtube.com/watch?v=seFu9fQ_-FI)]
