---
layout: post
title: Sharing a Burger Between Three
date: '2012-07-02T21:16:00Z'
author: Oatzy
tags:
- nerd
- mathematical methods
- geometry
- over-thinking
- random
- approximation
- graph
- trigonometry
- optimisation
- proofs
- algorithm
- everyday maths
- problem solving
- hypothetical question
- maths
modified_time: '2012-07-02T15:33:19.867-07:00'
thumbnail: /images/sharing-burger-between-three/diagram-1.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-4657040004420301186
blogger_orig_url: https://oatzy.blogspot.com/2012/07/sharing-burger-between-three.html
---

There are several ways to divide a burger evenly between three people.

Probably the best is to cut it radially (like a pizza). It can be tricky working out exactly where to make the cuts, but if you can pull it off, then all the pieces will be roughly identical (topping distribution notwithstanding).

But for the sake of arguing, lets say you want to divide the burger by making two parallel cuts: Where, then, do you make the cuts so that all three people get the same amount of burger?

NB/ This gets quite maths-heavy, so if you're not interested in that sort of thing, feel free to skip right to the end for the solution.

**Geometry**

For simplicity, we're going to consider the burger as a circle, and make the cuts so that each chunk has the same area. The two cuts are going to be the same distance from, and parallel to, the central axis of the burger, so we only need to consider the position of one of the cuts.

Here's the set-up

[![](/images/sharing-burger-between-three/diagram-1.png)](/images/sharing-burger-between-three/diagram-1.png)

We work out the area of the cut-off as the area of the circular segment, minus the area of the triangle.

*<strong>-</strong> <strong>Aside</strong><strong>: Radians</strong>*

[Radians](http://en.wikipedia.org/wiki/Radians) are basically an alternative way of measuring angles. For maths and physics they're generally more useful than degrees.

They're relatively easy - there are 2pi radians in a full circle, so 2pi radians = 360 degrees

1 radian = 180/pi = 57.3 degrees\
1 degree = pi/180 = 0.017 radians, etc.

\*    \*    \*

Back to the circle; with angle x in radians, the area of the circular segment is

$$ A_{seg} = \frac{x}{2}r^2 $$

The area of a triangle is half base times height..

*<strong>- Aside: Area of the Triangle</strong>*

We start by splitting the triangle down the middle, so that we have two identical right angle triangles

[![](/images/sharing-burger-between-three/diagram-triangle.png)](/images/sharing-burger-between-three/diagram-triangle.png)

The height, l = r\*cos(x/2)

The base, b = 2\*(r\*sin(x/2))

So the area of the triangle is (l\*b)/2 = r^2 sin(x/2)cos(x/2)

Finally, use the [identity](http://en.wikipedia.org/wiki/Double_angle#Double-.2C_triple-.2C_and_half-angle_formulae) *sin(2x) = 2sin(x)cos(x)*\
to get

$$ A_{tri} = \frac{1}{2}r^2\sin(x) $$

\*    \*    \*

So the area of the cut-off is

$$ A_{cut} = \frac{x}{2}r^2 - \frac{1}{2}r^2\sin(x) $$

and it needs to equal a third the area of the circle = 1/3 pi r^2.

So first, we need to find x satisfying

$$ \frac{x}{2}r^2 - \frac{r^2}{2}\sin(x) = \frac{\pi}{3}r^2 $$

or

$$ \sin(x) = x - \frac{2\pi}{3} $$

Once we have a value for x, we find where to make the cut from

$$ \frac{l}{r} = \cos\left(\frac{x}{2}\right) $$

**Intermission**

The thing about this equation is it doesn't have an exact, analytical solution - to find the solution you have to use [numerical methods](http://en.wikipedia.org/wiki/Root-finding_algorithm). Well, I say you have to use numerical methods; these days you can just type the equation into [WolframAlpha](http://www.wolframalpha.com/), and you'll get a solution like \*snaps fingers\*

Which is nice. I even have the WolframAlpha app on my phone. But when I thought up this question I was on holiday in Sherwood forest, where there was literally no mobile singal.

So that was out of the question. And since I'm not in the habit of carrying a scientific calculator around with me, I was stuck with the basic calculator on my phone. It looks like this:

[![](/images/sharing-burger-between-three/2012-07-02-01.57.07.png)](/images/sharing-burger-between-three/2012-07-02-01.57.07.png)

No trig functions, no square roots, no pi button. It doesn't even do brackets, or have a memory function. Luckily, I am in the habit of carrying around a notepad and pen.

Anyway, there are two ways of working this out with only a basic calculator. The first is 'easier', but only if you know some stuff, and the numbers happen to be nice (in this case, they kind of are). The second is harder, in that it requires more number crunching, but it'll work with any numbers, and can be more precise.

Again, feel free to skip to the solution if you're not interested in the gritty details.

**Method One**

First of all, here's a graph of the two sides of the equation

|  |
|:--:|
| [![](/images/sharing-burger-between-three/graph-edit.png)](/images/sharing-burger-between-three/graph-edit.png) |
| hand-drawn with [Skitch](http://evernote.com/skitch/) |

We want to find the point at which the two graphs cross. We can see that that happens somewhere between 2pi/3 and pi (120 and 180 degrees). So, lets make a guess that it's exactly halfway between these two values: 5pi/6 (150 degrees).

For the right hand side of the equation: 5pi/6 - 2pi/3 = 0.52

NB/ I'm using pi=3.1416 (rounded to 4 decimal places). If you prefer, you could use the approximation 22/7. The result should be roughly the same.

For the left hand side of the equation, we need to work out sin(5pi/6)

At A-level, we were expected to memorise sin() and cos() of angles 0, 30, 45, 60, 90, and 180 (degrees). We were also expected to know the [formulas](http://en.wikipedia.org/wiki/List_of_trigonometric_identities#Angle_sum_and_difference_identities) for sin() and cos() of sums of angles. For sin(), it works like

$$ \sin(a + b) = \sin(a)\cos(b) + \sin(b)\cos(a) $$

Why is this important? Well 150 degrees = 180 - 30 (5pi/6 rads = pi - pi/6)

So

$$ \begin{aligned} \sin(150) = \sin(180 - 30) &= \sin(180)\cos(-30) + \sin(-30)\cos(180) \\ &= (0)\left(\frac{\sqrt{3}}{2}\right) \;+\; (-0.5)(-1) \;=\; 0.5 \end{aligned} $$

And since 0.5 is pretty close to 0.52 - less than 5% error - we can accept the convenience of that answer and say it's close enough.

So our approximate value of x is 5pi/6 <u>*= 2.618*</u>

[Incidentally, the identity for sin(2x) is just a special case of the above, with a=b=x; i.e. sin(2x) = sin(x+x) = 2sin(x)cos(x)]

Now we just need to work out l/r = cos(x/2) = cos(5pi/12)

For this one, 5pi/12 rads = 75 degrees = 45 + 30, so we can use

$$ \cos(a + b) = \cos(a)\cos(b) - \sin(a)\sin(b) $$

So

$$ \begin{aligned} \cos(75) = \cos(45 + 30) &= \cos(45)\cos(30) - \sin(45)\sin(30) \\ &= \left(\frac{1}{\sqrt{2}}\right)\left(\frac{\sqrt{3}}{2}\right) \;-\; \left(\frac{1}{\sqrt{2}}\right)\left(\frac{1}{2}\right) \;=\; \frac{\sqrt{3} - 1}{2\sqrt{2}} \end{aligned} $$

And we just have to evaluate that. But we don't have a square root button. Now, I just happen to know that sqrt(3) ~ 1.73 and sqrt(2) ~ 1.41.

But I'm just weird like that. Let's say you don't. How do you work it out?

*<strong>- Aside: Square Roots</strong>*

There are [several ways](http://en.wikipedia.org/wiki/Methods_of_computing_square_roots) of working out square roots with just basic operators. For two easy examples:

The first is '[Trial and Improvement](http://en.wikipedia.org/wiki/Trial_and_improvement)' - pick a number, square it, does that give the right answer? If not, pick another number based on whether the last guess was too big or too small.

For example: sqrt(3)

> 1.5 -\> 2.25 -\> too small\
> 1.7 -\> 2.89 -\> too small\
> 1.8 -\> 3.24 -\> too big\
> 1.75 -\> 3.0625 -\> too big\
> 1.73 -\> 2.9929 -\> too small\
> 1.74 -\> 3.0276 -\> too big\
> 1.735 -\> 3.010225 -\> too big\
> 1.7325 -\> 3.00155625 -\> too big\
> 1.732 -\> 2.999824 -\> too small\
> etc.

The second method is the "[Babylonian Method](http://en.wikipedia.org/wiki/Babylonian_method#Babylonian_method)". It's more systematic, and can converge to the correct answer quicker than guessing. But it can be irritating if your calculator doesn't have a memory function.

It uses the recurrence relation

$$ x_{n+1} = \frac{1}{2}\left(x_n + \frac{S}{x_n}\right) $$

Basically, you make a guess xn. Divide the number you want to square root (S) by xn. If xn is lower than the actual square root, then S/xn will be greater than it. That means the actual root will be between xn and S/xn, so we make the next guess xn+1 the average of these two values. Repeat until x is sufficiently accurate.

For example: sqrt(2)

> x0 = 1.5 -\> 2/1.5 = 1.33\
> x1 = (1.5 + 1.33)/2 = 1.4166.. -\> 2/1.4167 = 1.41176..\
> x2 = (1.4167 + 1.41176..)/2 = 1.41421.. -\> 2/1.41421 = 1.41421..

\*    \*    \*

Whatever way you do it, you repeat the process until you get the degree of accuracy you're happy with.

You should get the answer around *<u>l/r = 0.259</u>*

**Method Two**

We go back to the equation sin(x) = x - 2pi/3

We still have to find the solution numerically, we still don't have a calculator with a sin() function, and this time the numbers don't work out nicely.

So, the question is, how do we calculate sin(x)?

*<strong>- Aside: Taylor Expansion</strong>*

The [Taylor Expansion](http://en.wikipedia.org/wiki/Taylor_expansion) of a function is a way of fitting a polynomial (sums of powers) to a more complicated function. It works like this

$$ \begin{aligned} f(x) &= \sum_{n=0} \frac{f^{(n)}(a)}{n!}(x - a)^n \\ &= f(a) + \frac{f'(a)}{1!}(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \frac{f^{(3)}(a)}{3!}(x - a)^3 + \cdots \end{aligned} $$

Basically, it gives a way of converting a function we can't calculate into an infinite sum of powers of x, which we *can* calculate.

It's usually expanded around the origin (x0=0), since the equations work out neater. But you can do it around any point, x0=a. This is useful if the value you are trying to calculate is far from x=0. The closer x is to x0=a, the quicker the sum converges.

Even though the expansion is an infinite sum, it's usually sufficient to just take the first few terms, since each additional term makes a smaller and smaller contribution to the sum.

So the trick is working out how many terms you need to include to get some desired level of accuracy.

\*    \*    \*

In this case, I'm going to use the Taylor Expansion of sin(x) around x0=pi, since the approximate value (2.6) is nearer to pi than 0.

Here's what the expansion looks like

$$ \begin{aligned} \sin(x) &= \sum_{n=0} \frac{f^{(n)}(\pi)}{n!}(x - \pi)^n \\ &= sin(\pi) + \frac{cos(\pi)}{1!}(x - \pi) + \frac{-sin(\pi)}{2!}(x - \pi)^2 + \frac{-cos(\pi)}{3!}(x - \pi)^3 + \cdots \\[1ex] &= (\pi - x) - \frac{(\pi - x)^3}{3!} + \frac{(\pi - x)^5}{5!} - \frac{(\pi - x)^7}{7!} + \cdots \end{aligned} $$

So, how many terms do we need to include?

Here's what the graph looks like for different numbers of terms

|  |
|:--:|
| [![](/images/sharing-burger-between-three/taylor-graphs-alt.png)](/images/sharing-burger-between-three/taylor-graphs-alt.png) |
| plotted with [WolframAlpha](http://www.wolframalpha.com/) |

For a value around 2.6, it can be shown that including the first two terms is correct to ~3 decimal places; the first three terms is correct to ~5 decimal places; the first four terms to ~7 decimal places, etc.

So I would probably go to the third term (for 5dp), but only take the result to 3dp.

NB/ We shouldn't get too hung up on getting an extremely accurate value for x, since we're already getting rounding errors from the factors of pi in the expansion. Also, since we're calculating x to 5dp, we should use pi=3.14159

That means we want to solve

$$ \begin{aligned} (\pi - x) - \frac{(\pi - x)^3}{3!} + \frac{(\pi - x)^5}{5!} &= x - \frac{2\pi}{3} \\ \frac{5\pi}{3} - 2x - \frac{(\pi - x)^3}{3!} + \frac{(\pi - x)^5}{5!} &= 0 \end{aligned} $$

which can't be solved exactly.

So, for finding the correct value (without [WolframAlpha](http://www.wolframalpha.com/input/?i=5pi%2F3+-+2x+-+%28pi-x%29%5E3%2F3%21+%2B+%28pi-x%29%5E5%2F5%21)), we can use any [root-finding method](http://en.wikipedia.org/wiki/Root-finding_algorithm). For what it's worth, I used Trial and Improvement; the other methods are easier with a computer.

But, note that the function is decreasing

[![](/images/sharing-burger-between-three/graph-2.png)](/images/sharing-burger-between-three/graph-2.png)

So if the guess gives a value greater than zero, you need to *increase* the value of x (and vice versa).

If you run through all that (I won't go into detail), it gives a value around <u>*x=2.605*</u>

Alternatively, you could expand around x0=5pi/6 (if you know/can work-out sin and cos of 150 deg without a calculator).

In this case you'd only need up to the term in x^2 (correct to ~4dp). Using this expansion would mean [solving](http://www.wolframalpha.com/input/?i=0.5+-+sqrt%283%29%2F2+%28x+-+5pi%2F6%29+-+1%2F4+%28x+-+5pi%2F6%29%5E2+%3D+x+-+2pi%2F3) a quadratic equation, which is [easy](http://en.wikipedia.org/wiki/Quadratic_equation#Quadratic_formula). But using this expansion can introduce more rounding errors from the factors of sqrt(3). It's a matter of preference, I guess. The answer should be about the same.

Finally, we need to calculate cos(x/2)

Again, we use the Taylor Expansion to calculate cos(). In this case, we're doing the expansion around x0=0; the expansion is

$$ \cos x = \sum_{n=0} \frac{(-1)^n}{(2n)!}x^{2n} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots $$

In this case, you just keep adding terms until the result remains approximately constant to some desired degree of accuracy (3pd).

This gives a value around <u>*l/r = 0.265*</u>

**So What is the Real Answer?**

Once I got to somewhere where I could get at WolframAlpha, I checked the real numbers; here are the [results](http://www.wolframalpha.com/input/?i=sin%28x%29+%3D+x-+2pi%2F3):

[![](/images/sharing-burger-between-three/soln-1.png)](/images/sharing-burger-between-three/soln-1.png)

The approximation of x from *Method One* (2.618) is an over estimate by ~0.5%, which is relatively [acceptable](http://en.wikipedia.org/wiki/Margin_of_error). The approximation from *Method Two* (2.605) is correct to 3 decimal places, which is definitely acceptable.

And for the [value](http://www.wolframalpha.com/input/?i=cos%282.6053256746%2F2%29) of l/r

[![](/images/sharing-burger-between-three/soln-2.png)](/images/sharing-burger-between-three/soln-2.png)

From *Method One* (0.259), the approximation is an under estimate by 2%, and correct to 2 decimal places, so is probably acceptable. The approximation from *Method Two* (0.265) is, again, correct to 3 decimal places. So that is also acceptable.

So, if the numbers happen to be convenient and you know some trigonometry, you're probably as well using *Method One*. If not, or if you just want more accuracy, then go for *Method Two*.

**Applying the Results**

The results are actually quite nice, in terms of practical application (dividing up a burger). The ratio of the radius (0.265) being close to one quarter, you find the cuts like this

[![](/images/sharing-burger-between-three/diagram-cuts.png)](/images/sharing-burger-between-three/diagram-cuts.png)

That is, find the central axis, then find the (imaginary) line halfway between the centre and the edge - make the cut halfway between the centre and this imaginary line (maybe cut an extra hair's breadth towards the edge). Repeat on the other side.

Easy.

So, now you know. Obviously, all this applies to dividing any circular thing evenly between three people. You could probably even adapt the methods for sharing between even more people.

And in theory, You could do all this with *just* pen and paper (no calculator). Though you probably wouldn't want to. I know I wouldn't..

Oatzy.

[<em>Wow, I really managed to stretch that one out</em><strong>[.](http://en.wikipedia.org/wiki/That%27s_what_he_said)</strong>]
