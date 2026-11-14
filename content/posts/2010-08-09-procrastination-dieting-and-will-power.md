---
layout: post
title: Procrastination, Dieting and Will Power
date: '2010-08-10T00:53:00Z'
author: Oatzy
tags:
- dieting
- procrastination
- psychology
- will power
- nerd
- everyday maths
- problem solving
- maths
modified_time: '2010-08-09T17:58:29.299-07:00'
thumbnail: /images/procrastination-dieting-and-will-power/f-T-max.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-8945736300929382254
blogger_orig_url: https://oatzy.blogspot.com/2010/08/procrastination-dieting-and-will-power.html
---

As a follow up to the [previous](http://oatzy.blogspot.com/2010/08/beauty-of-procrastination.html) procrastination post, it's worth noting that, in fact, the '*Principle of Procrastination*' is a special case of a more general *will power* principle.

To demonstrate this, lets look at a more general example of temptation verses will power - Dieting.

Okay, so imagine your food options are *chocolate*, *curry*, *pasta* and *salad*. Your diet food is *pasta*, so call that *f_0*.

For the other three foods, put them in order of desirability - *curry*, *chocolate*, *salad*. Your preference may vary. Then label the foods accordingly - so *curry* would be *f_1*, *chocolate* *f_2*, and *salad* *f_3*.

So going back to the equation from last time:

[![](/images/procrastination-dieting-and-will-power/f-T-max.png)](/images/procrastination-dieting-and-will-power/f-T-max.png)

*D(f_0)* is then the desirability of the *pasta*, relative to the other three.

So say you want *curry* more than *pasta*, but *pasta* more than the other two. The above expression basically says, how many foods do you want more than the one you're supposed to have. In this case, there's only one, so the total number of temptations, *T* *= 1*.

And that's basically it. And further to that we can say that *T* is inversely proportional to the desirability of the *f_0* - i.e. the less you want what you're supposed to eat, the more things there are that you'd rather eat.

And this can be written mathematically as

[![](/images/procrastination-dieting-and-will-power/inv-prop-f.png)](/images/procrastination-dieting-and-will-power/inv-prop-f.png)

Where *k* is the constant of proportionality, which will usually depend on the total number of options, among other things.

So as you may have noticed, the equations are the same as last time, with slightly different symbols. And this is how we get our general case:

[![](/images/procrastination-dieting-and-will-power/T-max-t.png)](/images/procrastination-dieting-and-will-power/T-max-t.png)

[![](/images/procrastination-dieting-and-will-power/inv-t.png)](/images/procrastination-dieting-and-will-power/inv-t.png)

Where *t_i* are temptations, *T* is total temptations, *t_0* is the required thing and *D(t_i)*, as before, is the desirability of *t_i*.

So what were left with is this same question - *how do you quantify D(t_i)*?

In the case of dieting, it'd be dependent of things like: calorie content, how filling the food is, how much you like it (tastiness, etc). But I'll leave working out an exact formula for *D(f_i)* as an exercise for someone else.

So for procrastination, we just replace food with activities, and the same basic formula holds. But what made it a special case was that we could define another feature of the required task - its importance. We could then define desirability of that task in terms of its importance and got a slightly different looking, but equivalent equation:

[![](/images/procrastination-dieting-and-will-power/kI-t.png)](/images/procrastination-dieting-and-will-power/kI-t.png)

Obviously, though, the D-functions are different for any given 'problem'. So for procrastination, the D-function was time-dependent - the importance of a required task increased with time, meaning desirability decreased with time.

The desirability of food, on the other hand, may vary over time. But when it does, it usually fluctuates, more than it having a definite increase or decrease.

(NB/ I'm not talking about your wanting a given food decreasing over time due to, e.g. the food spoiling.)

So the other thing to consider, for general will power situations, is the '*Temptation Threshold*'. And again, this is just a generalisation of the one of the old statements

[![](/images/procrastination-dieting-and-will-power/q-t-w.png)](/images/procrastination-dieting-and-will-power/q-t-w.png)

Where *q* is some quality of *t_n*, whether it be how time consuming it is, how bad for you it is (calorie content), etc. - which is dependent on the specific required activity. *w* is a quantification of the lower limit of your will power (w.r.t. quality *q*). And finally, *t_n* (with *n* satisfying the above) is the '*Temptation Threshold*' item.

If we go back to the diet example, then - say you've eaten recently, so your desire for more *pasta* is decreased (as is your desire for *curry*). But you're still peckish. The *chocolate*, being a snack food, is now more desirable, and, in fact, the most desirable (*t_1*).

Now, say that the quality, *q* is calorie content - in this case *100 calories*. If your will power won't allow you *100 calories* then you won't eat the *chocolate*. BUT, if you will allow yourself those *100 calories*, the *chocolate* crosses the '*temptation threshold*', and you can feel guilty about it later.

And that same sort of logic applies to procrastination and indeed to any other test of will power. But what that also demonstrates is that D-functions and *w* can be very fluid, which makes them harder to given an absolute definition to.

For example, will power may depend on the importance of sticking to a diet; your will power might fall over time (as you get hungrier); it'll depend on what you've already eaten.., and so on.

And similarly, D-functions will depend on things like what you've already eaten; relative healthiness; feelings of guilt or of rewarding yourself.., and so on again.

And the important thing to keep in mind is that these things can be very person specific. They can also be hard to quantify. So in essence, these equations do nothing more than to put into mathematical terms, facts of life.

And that's an intellectual exercise more than anything useful - except for in instances when doing so can provide new insight. So that final question is this,

Have you gained any sort of insight from any of this?

Oatzy.
