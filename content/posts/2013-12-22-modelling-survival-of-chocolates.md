---
layout: post
title: Modelling the Survival of Chocolates
date: '2013-12-22T20:16:00Z'
author: Oatzy
tags:
- simulation
- programming
- chocolate
- sociology
- analytical
- everyday maths
- problem solving
- maths
- modelling
modified_time: '2013-12-22T13:36:41.267-08:00'
thumbnail: /images/modelling-survival-of-chocolates/paper-choc-plot.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-478441352192107511
blogger_orig_url: https://oatzy.blogspot.com/2013/12/modelling-survival-of-chocolates.html
---

So it's been about a year since I last blogged. I've been kinda busy with university stuff, and growing my facial hair into something approaching a beard. I might write a blog about it at some point.

Anyway, I've got a little free time now - at least until after Christmas - so here we are. Let's waste some time..\.

**"This is a real paper, published in a proper journal"**

So the other day, my dad hands me this print out of an academic paper, "this seems like your sort of thing". The paper is called\
*"The survival time of chocolates on hospital wards: covert observational study"* [1]

The basic set-up is this: staff at various hospitals put out boxes of Roses and Quality Street chocolates on wards, and (covertly) recorded every time one was taken. From this, they analysed the 'survival' of the chocolates, according to [Kaplan-Meier](http://en.wikipedia.org/wiki/Kaplan-Meier_estimator) survival analysis.

[![](/images/modelling-survival-of-chocolates/paper-choc-plot.png)](/images/modelling-survival-of-chocolates/paper-choc-plot.png)

They found that the rate of chocolate consumption fit an exponential decay, with the median survival time for a chocolate being 51 minutes, and the survival half life ("time taken for 50% of the chocolates to be eaten") being 99 minutes. They also found that Roses chocolates were preferred over Quality Street.

**"Damn it, man, I'm a physicist, not a doctor!"**\
 \
So I'm reading this paper, and I'm thinking "I reckon I could model this". So I had a crack at it.

Basically, what we've got here is an [agent-based modelling](http://en.wikipedia.org/wiki/Agent_based_model) problem. Individuals encounter a box of chocolates at random intervals. Each box has a variety of different types of chocolates. So each individual will look through the box for any chocolate(s) they like the look of, and help themselves.

We can make a few simplifications to this. First of all, we work in fixed, discrete time intervals. In each time interval, some number of people will encounter the box of chocolates - one person per interval in the simplest model, and some random number of people in a more complex model.

Now, different people have different preferences. We could generate for each person a random set of preferences, but for simplicity we'll assume some 'average preference probability'. In other words, imagine there are equal numbers of each type of chocolates - what is the probability that any given person will pick type 1, type 2, etc. ? 

So, in the model, each person will pick a random chocolate based on this preference probability distribution. This accounts for the fact that some types of chocolate (strawberry) are naturally more popular than others (toffee penny).

**Here's Where it Gets Maths-y**

We have a box of N chocolates total. There are m different types of chocolate, with each type i=1,..,m having a count of ni such that 

[![](/images/modelling-survival-of-chocolates/eqn1.png)](/images/modelling-survival-of-chocolates/eqn1.png)

Each type also has a 'preference probability' pi with 0 \<= pi \<= 1 and

[![](/images/modelling-survival-of-chocolates/eqn2.png)](/images/modelling-survival-of-chocolates/eqn2.png)

In each time step dt an individual randomly chooses a type of chocolate, i in {1,..\.,m}, based on the preference distribution, and one chocolate of that type is removed from the box according to 

[![](/images/modelling-survival-of-chocolates/eqn3.png)](/images/modelling-survival-of-chocolates/eqn3.png)

This process is repeated until N(t) = 0

In the more complex model, some random number of individuals (following a Poisson distribution) each choose chocolates in each given time step. This is also functionally equivalent to a single individual choosing multiple chocolates in a single given time step.

**What Differential Does It Make?**

In the simplest model, one person chooses a single chocolate in each time step. This is nice, because it means we can express the model as a set of differential equations, which can be solved exactly.

For each type of chocolate we have the rate of consumption given by

[![](/images/modelling-survival-of-chocolates/eqn4.png)](/images/modelling-survival-of-chocolates/eqn4.png)

which has standard (exponential decay) solution 

[![](/images/modelling-survival-of-chocolates/eqn5.png)](/images/modelling-survival-of-chocolates/eqn5.png)

And since the total count N is just the sum of the individual counts ni we get the full solution

[![](/images/modelling-survival-of-chocolates/eqn6.png)](/images/modelling-survival-of-chocolates/eqn6.png)

In other words, it's just the sum of several exponential decays (with different decay rates) - making it, roughly, an exponential decay itself. 

[![](/images/modelling-survival-of-chocolates/chocolate-diff.png)](/images/modelling-survival-of-chocolates/chocolate-diff.png)

In particular, in the special case where all the chocolates are equally preferred such that pi = p for all i=1,..,m we get the solution

[![](/images/modelling-survival-of-chocolates/eqn7.png)](/images/modelling-survival-of-chocolates/eqn7.png)

And all that is loosely what was observed on the hospital wards. 

But these 'exact' solutions don't capture some of the subtleties of the real life set-up. For example, the toffee pennies might be completely ignored until they are the only option left; whereas, the exact solution assumes that (fractions of) all of the types of chocolate are being taken all the time, just at different rates.\
\
\
**"We did not seek ethical approval for this study..\."**

As an improvement on the analytical solution, we can create a computer simulated model, that captures more of the randomness of real life (code below). For the smplest model, the results look something like this

[![](/images/modelling-survival-of-chocolates/chocolate-sim.png)](/images/modelling-survival-of-chocolates/chocolate-sim.png)

Notice that in this version of the model, the number of chocolates decays more slowly, and has some of the granularity seen in the observed data plot. 

Plus, the randomness means the specific behaviour varies from run to run - for example, the orange line decays relatively quickly, while the blue has a long stretch when nothing is being taken.

Interestingly, this model seems to have a linear decrease for the first ~20-30 time steps in every sample run. This is probably because, for those first few steps, everyone can get what they want. But eventually, certain types run out, and the rate of consumption decays away.

**Why Do Chocoholics Come in Threes?**

I wrote about the [Poisson distribution](http://en.wikipedia.org/wiki/Poisson_distribution) before, back when I was [modelling cafes](http://oatzy.blogspot.co.uk/2011/01/model-cafe.html). Basically, while we might see an average of one person per time interval, we don't expect to see them so evenly spaced out. Rather, people will arrive in 'bursts' of varying size. This behaviour is described by the Poisson distribution.

So I wrote my simulation in Python, using the [numpy](http://www.numpy.org/) library for the Poisson distributed random numbers. The results look something like this

[![](/images/modelling-survival-of-chocolates/chocolate-pois.png)](/images/modelling-survival-of-chocolates/chocolate-pois.png)

In this case, the initial decrease is less linear than in the simple model, but the overall decay times are roughly the same (except for the blue line above). This is what we'd expect since, in the above, I chose the average number of people per interval to be 1.

So yeah. [Try the code](https://dl.dropboxusercontent.com/u/4635169/chocolates.py), have a play with the parameters, see what happens. The output is the total number of chocolates remaining after each time step.\
One thing to look at would be how changing the probabilities affects the rate of decay - for example, does the number of chocolates decay faster when all the chocolates are equally popular, or when some are much more popular than others. I suspect the former is the case.

It might also be worth adding an option where a person can pick again if their prefered chocolate isn't avaiable.\
**And the IgNobel Prize for Medicine goes to..\.**

So that's that. And I can definitely see the original paper being nominated for an [IgNobel](http://www.improbable.com/ig/), at the very least.

As for me, I have some [gift wrapping](http://oatzy.blogspot.co.uk/2011/12/gift-wrapping.html) I really need to get to..\.

Merry Christmas!

*<strong>Citation</strong>*

[1] P R Gajendragadkar, et al. *"The survival time of chocolates on hospital wards: covert observational study"* [BMJ 2013;347:f7198](http://www.bmj.com/content/347/bmj.f7198) (Published 14 December 2013)

Oatzy.

[Next job, modelling Her Majesty's [nuts](http://www.bbc.co.uk/news/uk-25344656)..\.]
