---
layout: post
title: The Tilting Coffee Cup
date: '2010-08-07T18:55:00Z'
author: Oatzy
tags:
- coffee
- nerd
- everyday maths
- problem solving
- maths
modified_time: '2010-08-08T03:49:33.300-07:00'
thumbnail: /images/tilting-coffee-cup/cup.jpg
blogger_id: tag:blogger.com,1999:blog-14769935.post-1805280083548489669
blogger_orig_url: https://oatzy.blogspot.com/2010/08/tilting-coffee-cup.html
---

So here's the story - Me and my dad were at Costa, and dad noted that the table was slanting to one side, pointing to his coffee. It looked something like this:

[![](/images/tilting-coffee-cup/cup.jpg)](/images/tilting-coffee-cup/cup.jpg)

Which is fair enough, but I had tea, which comes with a teapot and an empty cup. What that meant was I wouldn't be able to completely fill the cup - the slant meant there was a certain volume of the cup I wouldn't be able to fill.

So I did what any person who is me would do - work out what the volume is.

Feel free to have a go yourself. Solution follows..\.

First of all, it's important that we assume the cup is approximately cylindrical near the top (for simplicity). And that seems like a fair enough assumption.

 [![](/images/tilting-coffee-cup/cylin-cut.png)](/images/tilting-coffee-cup/cylin-cut.png)

So the shape of the empty volume is approximately a cylinder cut diagonally, edge to edge. And what that means is it can be found by calculating the volume of the cylinder and halving it:

$$ V = \tfrac{1}{2}(\pi r^2 h) $$

But what if you don't know *h*, and can't or don't want to measure it (in public). Here's a transverse cross-section of the cup:

[![](/images/tilting-coffee-cup/cup-xsect.png)](/images/tilting-coffee-cup/cup-xsect.png)

So side on, the volume forms a right angle triangle. And if we can find the angle of the tilt and the radius of the cup then you can work out *h*:

$$ \tan(\theta) = \tfrac{h}{2r} \;\; \Rightarrow \;\; h = 2r \cdot \tan(\theta) $$

And substituting that into the equation for volume and simplifying:

$$ \begin{gathered} V = \tfrac{1}{2}\pi r^2 \cdot 2r\,\tan(\theta) \\ V = \pi r^3\tan(\theta) \end{gathered} $$

Simple!

We estimated the radius at *5cm*, and using a spirit-level app on my phone found the tilt to be *3 degrees*. So what you get is:

$$ \begin{gathered} \textit{with} \;\; \theta = 3^\circ, \;\; r = 5\,\text{cm} \\ h = 10 \cdot \tan(3) \approx 0.5\,\text{cm} \\ V = 5^3\pi \cdot \tan(3) = 6.55\,\text{ml} \end{gathered} $$

And, to be fair, *6.55ml* isn't that much wasted space - about one and a third teaspoons. But the point is, I had my answer.

And, of course, the other thing you can do with that equation is work backwards to find the incline (if you know *h* or *V*):

$$ \theta = \tan^{-1}\left(\tfrac{V}{\pi r^3}\right) \qquad \theta = \tan^{-1}\left(\tfrac{h}{2r}\right) $$

Or if you know *h* for when the cup is on a flat surface (*h_0*), you can work out the maximum you can tilt the cup before spilling:

$$ \theta_{max} = \tan^{-1}\left(\tfrac{h_0}{r}\right) \;\; \textit{where} \;\; h_0 = \tfrac{1}{2}h $$

So there you have it.\
And I promise I'll stop doing math-y posts. Honest.

Oatzy.

[Answering the questions no-one asked.]
