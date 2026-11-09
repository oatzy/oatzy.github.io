---
layout: post
title: The AI That Came To Dinner
date: '2026-11-09T00:00:00.000+00:00'
author: Chris Oates
tags:
- coding
- cooking
- hobby
- AI
modified_time: '2026-11-09T00:00:00.000+00:00'
---

My job has indoctrinated me into the cult of AI.

All staff at our company are 'expected' to embrace AI, and use it as much as possible. Truthfully, this doesn't bother me - I'm lazy by nature, so if the computer wants to write code for me, I'm not going to fight it.

The effect is that I spend most of my work day in a Claude Code terminal, or else reviewing other people's code (mostly written by Claude). But actually, prior to the adoption of AI, most of my work days were writing specs/tickets for juniors and reviewing the PRs they came back with. So not that different, really.

Anyway, after about 4 months, I've relented and spent my own money on a Claude subscription. 

For what purpose?


# A Cure For Laziness

I rarely write code outside of work.

And when I do, it's rarely for coding's own sake ([Advent](https://oatzy.github.io/2020/12/06/advent-of-code-2020-python-oneliners.html) [of](https://oatzy.github.io/2021/12/02/advent-of-code-awk-oneliner.html) [Code](https://oatzy.github.io/2024/01/02/advent-of-code-jq.html) notwithstanding). Rather, I'll have some idea, a 'Question Nobody Asked' if you will, and code is just a means to an end.

When I thought about what I might do with a personal AI account, I thought back to past blogs - all the times I left something open-ended because I was too lazy to finish it off. I thought about the [gravity game](https://oatzy.github.io/2015/02/23/designing-general-relativity-based.html) that I designed but never built, in particular.

I also thought about the very last post here, and when I tried to have a local AI parse a recipe into json. And failed miserably.


# fix it

Here's how it went: I opened up Claude Code (Opus 5.5) in the `recipe_optimiser` [repo](https://github.com/oatzy/recipe-optimiser) and pointed it at the markdown version of that [last blog post](https://oatzy.github.io/2026/01/04/cooking-for-software-engineers.html), which explained the purpose of the repo.

Claude has a read and comes back with the following:

```
What would you like to do? Some ideas the post itself suggests:
- Better scheduling: improve how clashing hands-on steps get resolved ("it could be better").
- Brute force: recipes don't have many steps, so it could try every ordering and pick the best one.
- Parser: try the JSON conversion with a bigger model.
- Tidy-up: add a README, tests or a proper command-line interface.
```

**> create a claude skill to replace the parser**

The first thing to do was replace the recipe parser. Originally it was intended to use a local model, but due to my low spec laptop it was entirely useless. So I got Claude to generate its own ['skill'](https://github.com/oatzy/recipe-optimiser/blob/main/.claude/skills/parse-recipe/SKILL.md) (set of instructions), which works embarrassingly well with Opus 5.5

```
Steps I added (the recipe implies them but doesn't list them):
- 3a, bringing the water to the boil: 10 min

Times I guessed:
- 1, chop the onion: 5 min
- 2, mince the garlic: 2 min
- 3b, cook the spaghetti: 10 min (the recipe says "according to package instructions")
- 4a, heat the oil: 2 min
- 6a, add the tomatoes and oregano and season: 1 min
- 7, drain and combine: 1 min
- 8, add the basil and serve: 1 min

Times from the recipe: softening the onion (5), the garlic (1) and the simmer (10). I treated softening the onion as hands-on.
```

Then my professional developer brain kicked in, and said that I (Claude) should do the tidy-up it suggested (Tests! Docs! In this economy?) 

Actually, that made a good basis for the next step - trying the brute-force idea I floated in the post. The unit tests encode the 'rules' of the optimiser, so that the brute-force approach can be tested for correctness and consistency.

**> let's try the brute force approach and see how it compares**

As it turns out, at least for the sample recipes I had, brute force is only marginally better than the heuristic-based algorithm I hand-rolled, and at the cost of the script taking longer to run.

```
┌───────────┬─────────────┬────────────┬──────────┬──────────────────┬──────────┐
│  Recipe   │  Approach   │ Total time │ Waiting* │ Hands-on clashes │ Run time │
├───────────┼─────────────┼────────────┼──────────┼──────────────────┼──────────┤
│ Meatballs │ current     │ 46 min     │ 7 min    │ 0                │ 6 ms     │
├───────────┼─────────────┼────────────┼──────────┼──────────────────┼──────────┤
│ Meatballs │ brute force │ 46 min     │ 6 min    │ 0                │ 8.6 s    │
├───────────┼─────────────┼────────────┼──────────┼──────────────────┼──────────┤
│ Spaghetti │ current     │ 28 min     │ 0 min    │ 0                │ 1 ms     │
├───────────┼─────────────┼────────────┼──────────┼──────────────────┼──────────┤
│ Spaghetti │ brute force │ 28 min     │ 0 min    │ 0                │ 1 ms     │
└───────────┴─────────────┴────────────┴──────────┴──────────────────┴──────────┘

*Waiting is the minutes a not-prepable step (like hot oil) sits before the next step uses it. Some waiting can't be avoided. For example, the oven finishes preheating before the meatballs go in, and both plans have that.
```

Not that I'm smug about it ;)

Then Claude had a suggestion of its own:

**> try the OR-Tools solver and compare**

This is an approach I wouldn't have tried without AI, because I'm too lazy to learn how to use a [SAT-solver](https://developers.google.com/optimization/introduction/python).

The key thing about a [SAT-solver](https://en.wikipedia.org/wiki/SAT_solver) is it can find a 'provably' most optimal solution (if one exists), and it does it a lot faster than brute-force.

As it turns out, when using the SAT-solver, the *total* cooking time for the sample recipes still comes out at about the same as my heuristic method; but the SAT is able to arrange steps so that there's less waiting around.

In the repo, the SAT-solver replaced the brute-force code, but the brute-force is still viewable at this [commit](https://github.com/oatzy/recipe-optimiser/commit/82217816e70236429a38070ae8c13b4895b69faa)

So far, my algorithm is performing a lot better than I expected. But maybe that's a quirk of the sample recipes?

**> search the web for some fair use recipes for a bigger test set**

Most online recipes are copyrighted to the author, so Claude ended up pulling recipes from [Wikibooks Cookbook](https://en.wikibooks.org/wiki/Cookbook:Table_of_Contents) (creative commons licensed).

```
What this shows:
- Current method: it always matched the shortest total time of the waiting-first solver, but it left 1–4 minutes more waiting on three recipes (meatballs, fish and chips, shepherd's pie).
- Pad Thai shows the trade-off most clearly: the waiting-first plans take 44 minutes to avoid a single minute of waiting, where total and both finish in 39.
- Fish and Chips has a lot of waiting that can't be avoided. There's only one fryer, so the chips are kept warm while the fish fries.
- Speed: the solver takes under 0.2 s on all the new recipes. The meatballs are the slowest at 1.6 s with the waiting goal.
```

And this is the problem with AI - it's very easy to fall down a rabbit hole.

The [same repo](https://github.com/oatzy/recipe-optimiser) has all of the updated code if you're curious.


# Cooking For Lazy Engineers

I stopped doing the hand-optimisation shortly after writing the last post. And I never used the script in practice.

It just took too much time and effort. And I found that I started to care less about being so precise. Cooking, it turns out, is very forgiving. If something is ready too soon, you can turn the heat down low, or just pop a lid on it. It always works out in the end.

It started out a couple of times when I forgot to set my timer going and had to guess at when things were 'ready'. Eventually, I didn't bother with the timer at all. After a while, after enough practice, you learn to trust your eyes (and a thermometer) more than a clock.


# A-Why?

First and foremost, I want to reassure you that I will never let an AI anywhere near my (prose) writing. That much should be apparent from this post - despite the occasional emdash, I think my style is too erratic to ever be mistaken for AI.

In fact, one of the first things I put in my personal CLAUDE.md was *"I do not want [Claude] to write blog posts for me"*. I've been writing this blog for [over 15 years](https://oatzy.github.io/2025/07/28/questions-nobody-asked.html), and the writing is 'the point'.

But as alluded to, you may see more posts like this one, where I re-visit past posts to finish off the bits I was too lazy to do with my own ten fingers. 

Future posts may also use AI to some degree. And as is my way, I will go into specific detail about _how_ I used it. I see too many posts and demos of people saying "look what I did with AI" without them really talking about how they did it. Personally, I think that's the most interesting part.

I lied earlier. Yes, using Claude at work showed me what it was capable of. But I held out for the longest time because I didn't want to pay out of pocket for something I didn't have a *good* use for. Revisiting old blogs is a fine idea, but it's not worth the cost of a subscription.

What actually got me to pay up was a future project I have in mind - something involving crochet.

Watch this space...


Chris.


[Maybe I could get Claude to fix the blog's MathJax rendering.]

