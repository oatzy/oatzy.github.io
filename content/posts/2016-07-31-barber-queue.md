---
layout: post
title: Barber Queue
date: '2016-07-31T17:09:00Z'
author: Oatzy
tags:
- simulation
- probability
- nerd
- mathematical methods
- python
- over-thinking
- programming
- algorithm
- everyday maths
- coding
- maths
- modelling
modified_time: '2016-07-31T11:44:07.301-07:00'
thumbnail: /images/barber-queue/p-leave-sunkcost.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-4131484574323347568
blogger_orig_url: https://oatzy.blogspot.com/2016/07/barber-queue.html
---

Time was when I needed a hair cut, I'd go at noon on a weekday, when the barber's is typically empty. One of the perks of being unemployed.

But these days I have to get my haircuts on Saturdays, before noon. Which is bad enough in itself - ideally I'd never see Saturday mornings at all. And to make matters worse, Saturday morning is also when the barbers is at its busiest.

Hence, I found myself sat in the waiter area of a barbershop for the best part of an hour. But this got me thinking about how queuing works at a barbers.

**First In Who's Next?**

At its core, the barber's queue is just a [first-in first-out](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)) (FIFO) queue. But it has two interesting features:

1\) *The queue 'structure' is unordered*

In general the queue 'structure' will be a waiting area with a bunch of seats. When someone new joins the queue, they're free to sit wherever. In fact, odds are, they'll pick a seat in a similar way to [how men choose urinals](https://blog.xkcd.com/2009/09/02/urinal-protocol-vulnerability/) - attempting to maximise personal space.

But the key point is, if someone were to just look at the queue, they wouldn't be able to tell who was next.

2\) *Each member of the queue knows whether or not they're next*

Each member of the queue probably doesn't know *who* exactly is next, but they do know (with reasonable certainty) whether or not it's them.

The way this works is relatively simple - when you join the queue, you're aware of who was there when you arrived (and of anyone who arrives after you). So when all the people who were there ahead of you have gone, you know that you're next.

**O(M G)**

Okay, lets break out some Python (2.7)

Just for fun, let's say that the capacity of the queue is fixed - i.e. the waiting area has a fixed number of seats (though in practice, people are free to stand, as I was forced to).

``` python
class BarberQueue(object):

    def __init__(self, capacity):
        self._capacity = capacity
        self._queue = [None]*capacity
        self._length = 0

    def __len__(self):
        return self._length

    def __str__(self):
        return ', '.join(str(i) if i is not None else '_'
                         for i in self._queue)

    def push(self, obj):
        pass

    def pop(self):
        pass
```

So each member of the queue has some awareness of who is ahead of them. But they don't need to know specifically who's who, they just need to keep track of how many are remaining. And in fact, that remaining count is exactly equivalent to the member's position in the queue.

``` python
class Member(object):

    def __init__(self, obj, position=0):
        self.value = obj
        self._position = position

    def __str__(self):
        return "%s (%s)" % (self.value, self._position)

    def is_next(self):
        return self._position == 0

    def move_up(self):
        self._position -= 1
```

So, going back to the push and pop methods

``` python
def push(self, obj):

    if self._length == self._capacity:
        raise Exception("Queue is full! Please come back later.")

    for i, m in enumerate(self._queue):
        if m is None:
            self._queue[i] = Member(obj, self._length)
            self._length += 1
            return
```

Here, we're picking a 'seat' by iterate over the queue looking for the first empty slot (with a value of None). We could implement any seat picking strategy we fancy, this is just the easiest.

Once we find an empty seat, we create a new 'Member' object for the item, with position set to the current length of the queue, then increment the queue length. Also, if the queue has no empty slots, we raise an exception.

``` python
def pop(self):
    if self._length == 0:
        raise Exception("The queue is empty")
    for i, m in enumerate(self._queue):
        if m is not None:
            if m.is_next():
                value = m.value
                self._queue[i] = None
                self._length -= 1
            else:
                m.move_up()
    return value
```

Here we iterate over the queue looking for the member who is 'next' (has position 0). While we're looking for the next person, we also de-increment the positions of the other members.

Of course, this isn't how things work in practice. The barber doesn't go to each person and say "*are you next?*", "*how about you?*". They simply say "*who's next?*", and the person who believes they are next steps forward. Though arguably, that's just equivalent to asking every member concurrently. But let's not complicate things.

``` python
>>> b = BarberQueue(3)
>>> for i in xrange(3):
 b.push(i)
 
>>> print b
0 (0), 1 (1), 2 (2)
>>> b.push(4)

Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
    b.push(4)
  File "<pyshell>", line 36, in push
    raise Exception("Queue is full! Please come back later")
Exception: Queue is full! Please come back later
>>> b.pop()
0
>>> print b
_, 1 (0), 2 (1)
>>> b.push(4)
>>> print b
4 (2), 1 (0), 2 (1)
>>> for _ in xrange(4):
 b.pop()
 
1
2
4

Traceback (most recent call last):
  File "<pyshell>", line 2, in <module>
    b.pop()
  File "<pyshell>", line 46, in pop
    raise Exception("Empty queue!")
Exception: Empty queue!
>>> print b
_, _, _
```

So there we have it. Of course, this type of queue isn't really useful from a programming perspective.

All of insertion, deletion, and lookup are worst-case \(O(N)\), where N is the queue's capacity (*not* the number of people in the queue). Which is pretty much worse than all other types of queue.

**Why do items keep disappearing from my queue?**

Okay, let's move away from computer-sciencey queues. There are certain behaviours in real-world queues that don't apply or wouldn't make sense to programmatic queues.

For one, as I alluded to earlier, the capacity of the queue is not enforced - there's room for overflow, even if it means people have to stand.

But on the other hand, when a place does get that full, people are less likely to stick around.

In particular, we have two situations:

1\) There's a non-zero *probability that a person will not stick around if the queue is full* or close to full. This probability will tend to be related to the length of the queue when that person arrives

\[p(not join) \sim f(capacity, length)\]

For example,

\[p(not join) = A\left(\frac{length}{capacity}\right) - C\]

where A and C are some constants relating to how likely the person is to stick around if the queue is 'full', and at what point they consider the place to be 'too full'.

2\) There's a non-zero *probability that a person already in the queue will leave* before they're served.  This probability will typically depend on how long the person has been waiting, and how many people are still ahead of them

\[p(leave) \sim g(wait, position)\]

It's interesting because as time passes, wait increases, but position decreases. So how the probability evolves depends on how those factors balance against one another.

In particular, the probability evolution will likely depend on how each particular person responds to the [sunk-cost fallacy](https://youarenotsosmart.com/2011/03/25/the-sunk-cost-fallacy/) - i.e. are they the sort to think "*well, I've waited this long, I might as well see it through to the end*", or do they think "*this is taking too long, I've got better things to do with my time*"?

For the sake of arguing, lets go with an [exponential function](https://en.wikipedia.org/wiki/Exponential_function) for the general form.

For a sunk-cost person we might have

\[p(leave) = B \cdot \exp\left(-d\cdot \frac{wait}{position}\right)\]

This is a function where p goes to zero as position goes to zero or wait goes to infinity (B and d are some arbitrary constants).

[![](/images/barber-queue/p-leave-sunkcost.png)](/images/barber-queue/p-leave-sunkcost.png)

Whereas for a non-sunk-cost person we might have

\[p(leave) = B \cdot \exp\left(-\frac{d}{wait \cdot position}\right)\]

This is a function where p goes to zero as position goes to zero, but goes to one as wait goes to infinity.

This gives us an interesting graph

[![](/images/barber-queue/p-leave-no-sunkcost.png)](/images/barber-queue/p-leave-no-sunkcost.png)

Because 'position' is discrete you get this nice step function, with intervals of the probability steadily rising, then suddenly dropping. We can also see that there's a point at which probability of leaving is maximum, around the time you're in the middle of the queue. Which seems plausible.

We also have situations where a person will leave and come back later. But since, when they come back, they have to join the back of the queue, they're mathematically indistinguishable from a someone arriving for the first time.

One other complicating situation is people in groups. For example, if there's a parent and child ahead of you in the queue, the child is getting their hair cut by one member of staff, the parent is waiting; another member of staff asks 'who's next?' - is it you or the parent?

Situations like these add uncertainty into a member's queue position, and by extension their knowledge of whether they're next.

In that situation, we might wait to see if anyone else steps up, and if not we can assume it's our turn.

So we have \(p(next)\), which is a [Bayesian probability](https://en.wikipedia.org/wiki/Bayes_theorem) that updates over time to reflect whether anyone else has stepped up yet. The longer we wait with no-one stepping up, the closer our probability gets to one.

[![](/images/barber-queue/p-next.png)](/images/barber-queue/p-next.png)

Of course, if you wait too long, someone behind you might assume you're not in the queue after all and try to go ahead of you. But that's a topic for another blog.

**Nothing's so simple that it can't be made complex**

I've written about queuing before, in the context of a mathematical [model of a cafe](https://oatzy.github.io/2011/01/09/model-cafe.html).

The long and short of it is this - people arrive at random (following a [Poisson distribution](https://en.wikipedia.org/wiki/Poisson_distribution)) and join the queue with some probability (see above). Each iteration, some people are served, some join the queue, some get tired of waiting and leave, etc.

I'm going to iterate in 5 min time-step and say that a haircut takes 10-25 minutes (i.e. 2-5 steps). The exact duration is randomly generated for each customer.

I'm going to say that on average one person shows up every 10 minutes (0.5 per step). Here's an [example](https://web.archive.org/web/20160729100145/http://docs.scipy.org:80/doc/numpy/reference/generated/numpy.random.poisson.html) of how that might look over 12 steps (one hour), using the Poisson distribution: *[2, 0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0]*

I set up the simulation so that you specify some number of steps for the barbers to be considered 'open'. After that, no more people are added to the queue, but the simulation keeps running until the queue is empty.

To begin with, I made it so that everyone who arrived stayed.

With 2 workers, capacity 10, and an arrival rate of 0.5, the queue length typically stayed below 3. The highest I saw it go was 7, which is still comfortably within capacity.

[![](/images/barber-queue/queue-size-no-leaving.png)](/images/barber-queue/queue-size-no-leaving.png)

Above is an example of how the queue size varied over time in a particular simulation.

Increasing the arrival rate to 0.7, the average maximum queue length goes up into the low teens. And when the rate goes up to 1, the maximum queue length goes all the way up into the 30s.

*Homework question* - how does maximum queue length vary as a function of number of workers and arrival rate?

As I mentioned, those simulations assumed that everyone stuck around. Once you turn on probabilistic leaving, things get a bit more interesting.

I tried both versions of the leaving probability. The result was largely the same, except that sunk-cost people tend to leave sooner - average wait before leaving 2.6 for sunk vs 7.4 for non-sunk. This is what we'd expect - people adhering to sunk cost will tend to leave before they get too invested.

[![](/images/barber-queue/queue-size-w-leaving.png)](/images/barber-queue/queue-size-w-leaving.png)

In the above example, orange is a time step when someone left the queue, and red is when a newcomer decided not to join the queue. I tuned the probability constants so that people don't start leaving until we're close to or at capacity, as we'd expect in real life.

**You and I have different ideas of what constitutes 'interesting'**

Going back to the original description of the barber's queue, here's an example of a full queue (bracketed numbers are queue positions)

> *542b5af6 (3), 33e323cf (5), 69e60241 (6), b3f12010 (0), fc89732e (7), 991f8709 (1), a0cb93cc (2), 17186c75 (4), 57269a3e (8), 8f1b61ca (9)*

Notice how, even with the basic seat picking strategy (take the first available), the members aren't in a predictable ordered.

When we look at the waiting times, we can see some interesting things. For example

> *..\.\
> 1c7081d1 waited 7.0\
> 34 1\
> 35 3\
> 50be68cf waited 9.0\
> 36 3\
> 37 4\
> 26ca11b7 waited 3.0\
> 38 3\
> 39 3\
> a571a7da waited 5.0*\
> *..\.*

Here we have a person who had to wait 9 steps (45mins) to be served, followed by someone who only had to wait 3 steps (15mins). Which just goes to show, how long you wait in a queue is very much a matter of timing and luck.

It's also interesting that you can run the simulation multiple times with the exact same settings, and one time the queue will never go higher than 4, while in the the next it'll go as high as 13. This is [complexity](https://en.wikipedia.org/wiki/Complexity) at work - various small random factors in the model interacting to produce wildly different outcomes.

So yeah. If you're interested, you can see the full [code here](https://github.com/oatzy/question-nobody-asked/blob/main/barber-queue/barber.py). I may have gotten carried away with the object-orienting.

Oatzy.

**[Post-Script**

My boss recently pointed out that it'd been over a year since my last blog post. That was another perk of being unemployed - more time to come up with dumb blog posts. Anyway, here's a quick update on some stuff.

**Pirate Game**

The last blog post was about the making of an Android game - The Pirate Game.

The game is now finished-ish and has been released in 'beta' on the [Play Store](https://play.google.com/store/apps/details?id=com.cavillum.pirategame.android).

In the [previous post](https://oatzy.github.io/2015/06/29/the-pirate-game.html), I mentioned that the game would eventually get a less utilitarian design. I ended up making that design myself (because I'm a control freak). I'm pretty pleased with how it turned out.

[![](/images/barber-queue/pg-board-mock.png)](/images/barber-queue/pg-board-mock.png)

Also, following a..\. less than positive review, I added some new game play modes.

I never did figure out multiplayer, though. If I ever get the time or inclination to go back to the game, that'll be on the todo list. But for the time being, I don't anticipate any updates to the game. Certainly not any time soon.

**New Job**

So yeah. I finally got a job. I'm now a Software Developer at a company called [Pixit Media](http://pixitmedia.com/).

The company sells large scale 'storage solutions' to companies primarily in the VFX industry, as well as universities and other such people that do high performance computing.

What I personally work on is primarily a Python API for the [IBM Spectrum Scale](http://www-03.ibm.com/systems/uk/storage/spectrum/scale/) (GPFS) filesystem. You can see the [API docs online](https://web.archive.org/web/20180202035444/http://www.arcapix.com:80/gpfsapi/). I wrote a decent amount of the documentation (and the code that's being documented).

In particular, the '[Getting Started With List Processing](https://web.archive.org/web/20180203222002/http://www.arcapix.com:80/gpfsapi/list_processing_guide.html)' guide. Admittedly the topic is a bit niche - I doubt many readers of this blog even know of GPFS, let along have a cluster with it installed. But you might still find it interesting; you can learn some stuff about [MapReduce](https://en.wikipedia.org/wiki/MapReduce) - a technique for taking advantage of parallelism when processing large data-sets.

There's also the '[example scripts](https://github.com/arcapix/gpfsapi-examples)' repository - scripts written to use the API, some of while I wrote. But, again, they're a bit niche.

]
