---
layout: post
title: Modelling the Zombie Apocalypse
date: '2010-09-03T20:04:00Z'
author: Oatzy
tags:
- zombies
- nerd
- problem solving
- maths
- modelling
modified_time: '2010-09-03T13:04:14.356-07:00'
thumbnail: /images/modelling-zombie-apocalypse/Zombie-basic.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-1768911825968696377
blogger_orig_url: https://oatzy.blogspot.com/2010/09/modelling-zombie-apocalypse.html
---

..Or why, when the zombie apocalypse comes, we're all screwed.

**Maths of Epidemics**

The spread of an infection through a population can be modeled with variations on the [Kermack-McKendrick Model](http://en.wikipedia.org/wiki/Epidemic_model#The_SIR_Model). In this approach the population is divided into three groups:

1\) *Susceptible* - not yet infected, but able to catch the infection\
2\) *Infective* - infected individuals, capable of passing on the infection to susceptibles\
3\) *Removed* - after some period of time, infectives will recover (or die). These are usually considered immune to catching the infection again.

You then have a system of differential equations to describe how these groups vary over time, and hence how the infection spreads.

**How do you model a Zombie Apocalypse?**

In the paper "[WHEN ZOMBIES ATTACK!: MATHEMATICAL MODELLING OF AN OUTBREAK OF ZOMBIE INFECTION](https://web.archive.org/web/20100210071041/http://www.mathstat.uottawa.ca/%7Ersmith/Zombies.pdf)", mathematicians at Carleton University modified this model in various ways. In the simplest form, they replaced 'infective' with 'zombie' and allowed a certain proportion of the dead to be resurrected (as zombies).

[![](/images/modelling-zombie-apocalypse/Zombie-basic.png)](/images/modelling-zombie-apocalypse/Zombie-basic.png)

They found that the ultimate outcome of that model, for all conditions, is "Doomsday" - i.e. the entire population zombified or dead.

They then modify it for a scenario where the infected are quarantined. What they found is that unless there's sufficient quarantining in the early stages of infection, it's Doomsday again; albeit a slightly delayed one. And since that sort of quarantining would be unfeasible anyway, it's not even worth trying in most cases.

The next approach was to replace quarantining with 'cure' - assuming the cure didn't also provide immunity. The result of this model suggests that a state of stable co-existence between humans and zombies could be reached.

[![](/images/modelling-zombie-apocalypse/Z-Graph-Vacc.png)](/images/modelling-zombie-apocalypse/Z-Graph-Vacc.png)

But again, it's not ideal. You can only make so much of the cure. So the zombies would get you in the end.

The final alteration was replacing cure with strategic mass-eradication of zombies at frequent intervals. In this case, the zombie population *could* (eventually) be completely destroyed. But that is only if the resources for such attacks are available, and if the military (or whoever) act fast enough and often enough. Otherwise..\. you know..\. Doomsday..

To quote the article:

> "In summary, a zombie outbreak is likely to lead to the collapse of civilisation [..\.] As seen in the movies, it is imperative that zombies are dealt with quickly, or else we are all in a great deal of trouble."

So basically, unless we can wipe out the zombies quickly, trying to fight and survive is just delaying the inevitable.

You might as well just accept your fate and get to work munching on those delicious BBRRRAAAAAIIIIINNSS!!!

Oatzy.
