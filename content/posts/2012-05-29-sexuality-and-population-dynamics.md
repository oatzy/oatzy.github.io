---
layout: post
title: Sexuality and Population Dynamics
date: '2012-05-30T01:23:00Z'
author: Oatzy
tags:
- lesbians
- programming
- sociology
- infographic
- analytical
- over-thinking
- population dynamics
- hypothetical question
- maths
- modelling
modified_time: '2012-05-30T11:29:02.953-07:00'
thumbnail: /images/sexuality-and-population-dynamics/model-flow.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-3996765015493626779
blogger_orig_url: https://oatzy.blogspot.com/2012/05/sexuality-and-population-dynamics.html
---

So I was reading [this](http://misformaddie.tumblr.com/post/21092347758) response to a [Daily Mail opinion piece](https://web.archive.org/web/20120615000936/http://www.dailymail.co.uk:80/debate/article-2129340/Gay-cure-bus-advert-Homosexuality-IS-departure-norm.html) about those 'gay cure' bus adverts, and I see this quote (from the Mail article)

> “*Since only about one percent of us are [gay], homosexuality is obviously a departure from the norm..\. Reversing that proportion would spell the end of the human race, which is clearly undesirable.*”

There are several things wrong with this statement - some of which the response, linked above, points out.

First of all, that 1% values. The actual number is a tricky figure to pin down. The UK Office of National Statistics puts the figure at 1.5% gay or bisexual; the linked response lists 3 studies which put the value around 7% (for the UK), and various other [studies](http://en.wikipedia.org/wiki/Demographics_of_sexual_orientation) suggest number in the modern West is somewhere between 2-13%.

Secondly, just because something is (statistically) "a departure from the norm", doesn't mean it's bad - for example, ~10% of people are [left-handed](http://en.wikipedia.org/wiki/Left-handedness), ~2% of people have [red hair](http://en.wikipedia.org/wiki/Ginger_hair), etc. ([Historical](http://en.wikipedia.org/wiki/Bias_against_left-handed_people) [beliefs](http://en.wikipedia.org/wiki/Ginger_hair#Prejudice_and_discrimination_against_redheads) notwithstanding.)

But all that's tangential. What I'm interested in is the second part - would a majority gay population spell the end of humanity?

[NB/ for the remainder of the blog, I shall be using 'gay' colloquially, as shorthand for all of LGBTQUA, etc.]

**The Simple Model**

It's an interesting [population dynamics](http://en.wikipedia.org/wiki/Population_dynamics) question, and it's easy to model if we make some assumptions and simplifications:

1\) We assume that homosexuals don't reproduce at all (either directly or indirectly). This isn't true - but it seems to be a common belief.

2\) We assume that the rest of the population reproduces with some fixed [rate](http://en.wikipedia.org/wiki/Population_growth) (*b=0.02059*), which doesn't change from year to year. Similarly, we assumes a fixed death rate (*d=0.00812*), which affects all members of the population equally.

3\) We assume that sexuality is binary, definite and static, with a fixed incidence of homosexuality, *g = 0.07* - that is, of all children born 7% will be gay.

So the model we're using is preposterously simplified - effectively,

*new population = old population + births - deaths*

[![](/images/sexuality-and-population-dynamics/model-flow.png)](/images/sexuality-and-population-dynamics/model-flow.png)

And we can easily program this model and run simulations.

Now, there are two ways to interpret the article's statement in the context of our model -

1\) "if 99% of the (initial) population were gay" assuming the 7% incidence

The outcome looks like this

[![](/images/sexuality-and-population-dynamics/plot-g07.png)](/images/sexuality-and-population-dynamics/plot-g07.png)

In this case, the population drops at first, but then starts to grow again, exponentially - certainly not the end of the human race. Also notable is that the proportion of the population that is gay stabilises at 7% (as expected).

2\) "if 99% of people were born gay"

Now, the outcome looks like this

[![](/images/sexuality-and-population-dynamics/plot-g99.png)](/images/sexuality-and-population-dynamics/plot-g99.png)

Exponential decay - so, in this case, humanity would die out. But if 99% of the population isn't reproducing, what do you expect?

Here are the [phase portraits](http://en.wikipedia.org/wiki/Phase_portrait) of the above two cases, for a slightly different view of what's happening (gay population along x, straight population along y)

[![](/images/sexuality-and-population-dynamics/phase-portraits-alt.png)](/images/sexuality-and-population-dynamics/phase-portraits-alt.png)

Again, for *g=0.07* the population tends to infinity; for *g=0.99* the population tends to zero. Note that this behaviour is (ultimately) the same for all initial population ratios.

**What I Learned in MAS271**

We don't actually need numerical simulations to study the behaviour of this (or similar) systems - the model can be solved analytically.

First of all, we generalise the system. We start with a pair of coupled, first-order differential equations describing the behaviour of the two populations

$$ \begin{aligned} \dot{x} &= a_{11}x + a_{12}y \\ \dot{y} &= a_{21}x + a_{22}y \end{aligned} $$

Now, these two populations are mutually exclusive subgroups of the total population - that is, total population z = x + y. So with a little [mathematical trickery](http://mathbin.net/98300), we can combine these two into a single equation, describing the behaviour of the total population

$$ \ddot{z} = (a_{11} + a_{22})\dot{z} - (a_{11}a_{22} - a_{12}a_{21})z $$

This is a second-order, linear differential equation, so has the general solution of the form

$$ z(t) = A_{z_1}e^{\lambda_1 t} + A_{z_2}e^{\lambda_2 t} $$

Where lambda values are given by

$$ \lambda_{1,2} = \frac{(a_{11} + a_{22}) \pm \sqrt{(a_{11} + a_{22})^2 - 4(a_{11}a_{22} - a_{12}a_{21})}}{2} $$

And A-coefficients are constants, which are determined by the system's initial conditions. If the initial total population is z0, and the inital size of the x population is x0, then we get

$$ \begin{aligned} A_{z_1} &= \frac{x_0(a_{11} - a_{12} + a_{21} - a_{22}) - z_0(\lambda_2 - a_{12} - a_{22})}{\lambda_1 - \lambda_2} \\ A_{z_2} &= \frac{x_0(a_{11} - a_{12} + a_{21} - a_{22}) - z_0(\lambda_1 - a_{12} - a_{22})}{\lambda_2 - \lambda_1} \end{aligned} $$

In other words, we now have an (analytical) equation which completely describes how the population will behave for any given set of variable.

Incidentally, the equations for x and y have the same form as z. The only difference is the A-coefficients.

**Boom or Bust**

What we want to do is be able to determine the long term behaviour of the population based on the given set of variables - that is, will the population grow, or die out?

For the coupled system above, there is only one stationary point, at (x,y) = (0,0) - i.e. when the total population is zero. What this means is, if the population is zero, it will stay zero. If it has any other value, then the population size will change over time.

In terms of the stability of the system, if (0,0) is *stable*, the population will tend towards zero - i.e. will die out. If (0,0) is *unstable*, the population will tend to infinity - i.e. grow indefinitely.

As it turns out, the lambda values above are the [eigenvalues](http://en.wikipedia.org/wiki/Eigenvalues) of the coupled system, meaning their values determine the [stability](http://en.wikipedia.org/wiki/Stability_theory) of the system:

i\) if both lambdas are *negative*, the system is stable and the population will *die out*;

ii\) if one or both of the lambdas are *positive*, the system is unstable and the population will *grow to infinity*.

Now, if we take the limit of z(t) for t tends to infinity, we can simplify the population equation

$$ \lim_{t \to \infty} z(t) = A_{z_1}e^{\lambda_1 t} $$

What this tells us is, if lambda1 is less than one the population will die out. If lambda1 is greater than one, the population will grow.

And we can use this to determine the conditions for instability - the conditions under which the population will grow. In this case the condition is *lambda1 \> 0*. But this can be simplified down to

$$ a_{11}a_{22} - a_{12}a_{21} < 0 $$

There's one last trick we can do - determine what proportion of the total population will be in the sub-population x (e.g. what what fraction of the population will be gay) as t tends to infinity.

For this, we determine the equation for population x (in a similar fashion to z), and take advantage of the limits to get the equation

$$ \lim_{t \to \infty} \frac{x(t)}{z(t)} = \frac{z_0a_{12} - x_0(\lambda_2 + a_{12} - a_{11})}{x_0(a_{11} - a_{12} + a_{21} - a_{22}) - z_0(\lambda_2 - a_{12} - a_{22})} $$

Note that this equation is time-independant, i.e. the proportion will tend to some constant value.

**Back to Basics**

Just as a sort of check, we'll go back to the basic model. For this, we have

$$ \begin{aligned} \dot{x} &= [-d]x + [bg]y \\ \dot{y} &= [b(1 - g) - d]y \end{aligned} $$

Which gives lambda and A values

$$ \begin{aligned} \lambda_1 &= b(1 - g) - d & \qquad \lambda_2 &= -d \\[1ex] A_{z_1} &= \frac{z_0 - x_0}{1 - g} & \qquad A_{z_2} &= \frac{x_0 - gz_0}{1 - g} \end{aligned} $$

Which gives the population equation

$$ z(t) = \frac{z_0 - x_0}{1 - g}e^{[b(1-g)-d]t} + \frac{x_0 - gz_0}{1 - g}e^{-dt} $$

Which behaves like the graphs at the top. And this tends to

$$ \lim_{t \to \infty} z(t) = \frac{z_0 - x_0}{1 - g}e^{[b(1-g)-d]t} $$

And gives

$$ \lim_{t \to \infty} \frac{x}{z} = g $$

That is, the proportion of the population that will be gay stabilises at the pre-defined 'birth' ratio - which is what we saw from the numerical model. Note also that this value is independent of initial conditions and doesn't vary over time.

**Simple Instability**

Finally, for the simple model, the condition for instability (growth) is given by

$$ g < 1 - \frac{d}{b} $$

For the numerical values chosen above, this gives the condition *g \< 0.606* - that is, if less than 61% of the population is 'born' gay, then the population won't die out. And 61% is a pretty high upper limit - a majority, in fact.

Similarly, we can use this inequality to find under what conditions g=0.99 is viable. In this case, it requires a birth rate 100 times the death rate.

So, if the death rate is 0.008 (i.e. 8 death for every 1,000 people), then it requires a birth rate of 0.8 (800 birth per 1,000 people). Now, for each 1,000 people, 99% is gay, meaning 10 straight people per 1,000. Of those, about half is female (5). In other words, each woman would have to give birth to *160* *babies per year*!

Clearly this isn't feasible. But for comparisons sake, consider bees or ants - these species are [eusocial](http://en.wikipedia.org/wiki/Eusocial), meaning populations made of one fertile queen, and hundreds of (mostly) sterile drones. In this case, the high birth-to-death ratio is more reasonable, and the predominantly non-reproducing population is still viable.

**A More Complex Model**

In the simple model we assumed that only the straight population reproduces, and that both populations die at the same rate. So we make the following modifications:

1\) First of all, lets tweak the model so that the gay population has children as well, with some separate birth rate, *b1*.

2\) Of those born to gay couples, some proportion *g1* will be gay (NB/ [studies](http://en.wikipedia.org/wiki/Homosexuality#Etiology) show that the majority of children raised by same-sex parents grow up to be heterosexual).

3\) And for completeness, lets say that the gay population has a different death rate as well, *d1*.

Here's what the model looks like

[![](/images/sexuality-and-population-dynamics/model-flow2.png)](/images/sexuality-and-population-dynamics/model-flow2.png)

And here are the coupled equations

$$ \begin{aligned} \dot{x} &= [b_1g_1 - d_1]x + [bg]y \\ \dot{y} &= [b_1(1 - g_1)]x + [b(1 - g) - d]y \end{aligned} $$

Now, all the previously derived general equations and such from earlier still apply. But in this case, the variables can't really be simplified, and writing them out in full would just be a mess.

So if we take, for example, b and d as before, and *b1 = 0.00103*, *d1 = 0.01218*, and *g1 = 0.03*, here are the new phase diagrams for g = 0.07 and 0.99

[![](/images/sexuality-and-population-dynamics/complex-phase-portraits.png)](/images/sexuality-and-population-dynamics/complex-phase-portraits.png)

For this model, the phase portraits are basically the same as for the simple model - i.e. the effect of using the modified model over the simple model is negligible.

**Complex Conditions**

So, for this model, the condition for growth looks like this

$$ 1 < \frac{b}{d}(1 - g) + \frac{b_1}{d_1}g_1 $$

The important thing to note here is, if the condition for the simple model (*g\<1-d/b*) is satified, then the condition for the complex model is necessarilty satisfied.

In fact, if we set g to its maximum possible value 1 (i.e. all babies born to straight couple are gay), then the human race will still persist so long as *g1 \> d1/b1*.

And what this means is, so long as the birth rate (b1) is greater than the death rate (d1), then every baby born could be gay, the human race still wouldn't die out.

However, given the low birth rate for gay couples (compared to death rate), this might not actually be satisfied IRL. In which case, an entirely gay population is still not sustainable.

For the b and d values already chosen, we can use the condition to plot how the upper limit of g varies with g1

[![](/images/sexuality-and-population-dynamics/g-g1-graph.png)](/images/sexuality-and-population-dynamics/g-g1-graph.png)

So for these values, the upper limit of g can increase by no more than 3.4%. So, again, the extra complexity doesn't give a significantly different result compared to the simple model.

In fact, the additional variables only become significant when *(b1/d1)g1 \> 0.15* (for the values above); or in general, when

$$ \frac{b_1}{d_1}g_1 > 0.05\left(\frac{b}{d}\right) $$

So, if we keep b and d as before, *g=0.07*, and re-set b1=b, d1=d, and *g1=0.06*, then *(b1/d1)g1=0.152*, and the phase portrait looks like this

[![](/images/sexuality-and-population-dynamics/b1d1g1-0152.png)](/images/sexuality-and-population-dynamics/b1d1g1-0152.png)

Here, the upper limit on g has risen to *0.67*. (cf: 0.61 for the simple model). And, if we set the initial condition *x0=0.07\*z0*, then the limit of *x/z = 0.0697*; just less than g.

*<strong>tl;dr -</strong>* So, would homosexuality ever mean the end of the human race? - Under some circumstances, yes. But in most (real world) cases, no. And even if a majority of the population were LGBT, the human race still wouldn't necessarily die out.

*BUT*, as a final note - remember that these are very simplified models of population dynamics. So take the results with a grain of salt. The science of [sexuality](http://en.wikipedia.org/wiki/Human_sexuality) is much more complex and much less abstract than this.

Oatzy.

[Putting my degree to good use.]
