---
layout: post
title: Picking and Scoring Words for Hangman
date: '2011-09-11T23:26:00Z'
author: Oatzy
tags:
- statistics
- information theory
- programming
- nerd
- python
- games
- over-thinking
- problem solving
- entropy
- maths
modified_time: '2011-09-11T17:20:36.703-07:00'
blogger_id: tag:blogger.com,1999:blog-14769935.post-6116177399372295470
blogger_orig_url: https://oatzy.blogspot.com/2011/09/picking-and-scoring-words-for-hangman.html
---

[Hangman](http://en.wikipedia.org/wiki/Hangman_%28game%29), for those unfamiliar, is a popular way for primary school teachers to teach spelling in the guise of a fun guessing game, and a way for secondary school teachers to pass the time at the end of term when they can't be bothered with teaching.

**It Works Like This..**

In a dystopian future where the powers that be like to play deadly games with their political prisoners, Hangman sees one such prisoner, 27 year old Adrian Silk, standing on a platform in front of a cheering crowd; his crime - logical thought.

Adrian is presented with an unknown word - 9 letters, title of a 21st century movie - and his task is to determine that word by guessing letters.

With each correct guess he gets closer to discovering the mystery word and winning a stay of execution. With each incorrect guess, another piece of the gallows is built. If he can't reveal the word before the gallows are fully constructed, he'll be dancing a dead man's jig for the crowd.

He starts by guessing the vowels - A, E, I, O, U - two incorrect guesses, two pieces of the gallows built: I\_\_E\_\_IO\_

He guesses some common consonants - N, R, S, T - two more incorrect guesses, but still safe: IN_E_TION

Adrian stops to think - "are there any films called [INFECTION](http://en.wikipedia.org/wiki/Infection_%28film%29)? There are two, but they're pretty obscure.. Wait..!". And he hazards a guess - INCEPTION ..?

He's right! Adrian jumps for joy, and breathes a sigh of relief. And as the disappointed crowd jeers, Adrian is shot between the eyes by the Games Master - found guilty of the logical thought with which he'd been charged.

Still, if you think that's bad, you should see how they play KerPlunk!

**Lets Play a Guessing Game**

Okay, imagine you were guessing letters for an unknown word. But in this variation on the game, the hangman will only tell you when you've won, or else when you've run out of letters. That's all the information you get, nothing else.

The simplest approach to finding a word would be to just work your way through the alphabet - 26 letters, a *maximum* of 26 guesses to uncover *any* word.

But there will be a limit on how many incorrect guesses you can make - usually around 10. This means that, unless the word you're guessing contains 17+ unique letters this probably isn't the optimal approach.

So with no feedback and a guess limit, all you can do is guess letters 'at random'. But some letters appear more often in the English language than others. So you can make educated guesses, and go for the [more common letters](http://en.wikipedia.org/wiki/Letter_distribution) first: E, T, A, I, O, N, S, ..\.

If we assume that the probability, *p(ci)*, of a person guessing a given letter is roughly equal to that letter's [frequency in the English language](http://en.wikipedia.org/wiki/Letter_distribution#Relative_frequencies_of_letters_in_the_English_language), then the probability, big *P*, of that person guessing a correct letter in a word equals the sum of the probabilities of each unique letter in that word.

For example, in MISSISSIPPI, the unique letters would be {I,M,P,S}, so

P(MISSISSIPPI) = p(I)+p(M)+p(P)+p(S) = 4.025% + 2.406% + 1.929% + 6.327% = *14.687%*

What this immediately suggests for choosing words is:

1\) *Words with 'uncommon' letters are better*

Uncommon letters have lower probability *p(ci)*, so will make totals lower. E.g. C is less common than H, so (in the game described above) CAT is harder to guess than HAT

2\) *Words with fewer unique letters are better*

If there are fewer (and smaller) targets, it's harder to hit one of them by just firing at random.

**Parting Words**

So what about in a real game, where you get lots of feedback - which letters are right or wrong, where each letter appears and how many times.. This makes deduction a lot easier.

Have you ever tried to cheat at a crossword? There are loads of '[helpers](http://www.crosswordsolver.org/quicksolve.php)' online - put in the pattern and see what possible words match it. Well for hangman we take that a step further.\
Say our pattern is E_UA_I\_\_; there are 5 words it could be - EQUALITY, EQUALING, EQUALISE, EQUATION, EQUATING

First of all, EQUALISE is not a valid solution because it introduces an extra E. And if we'd guessed all the vowels to get that pattern, we can also rule out EQUATION since we've already determined that O doesn't appear in the solution word.

So to put it more concisely - we want to find words that match a given pattern, eliminating those which contain extra letters already guessed.

In the case above we're left with 3 words - EQUALITY, EQUALING, EQUATING - and which of the three the correct word is can be determined by guessing the letter T:

1\) E_UA_IT\_ which can only be EQUALITY\
2\) E_UATI\_\_ which can only be EQUATING\
3\) T doesn't appear in the word, in which case it can only be EQUALING

The fact that T is the most common consonant probably means each of those 3 words are poor choices for hangman. This is an example of a low entropy pattern.

Imagine, instead, that you're presented with a 3 letter word, and you've gone through the vowel and found you're left with the pattern \_A\_

What could that be? Maybe you guess T next and get \_AT - well that could be BAT, CAT, HAT, RAT, .. Or maybe T is wrong, then the word could be MAN, CAN, BAY, RAY, WAX, TAX, .. how many guesses have you got left?

In fact, there are 179 possible words which match this pattern. This would be a high entropy pattern.

So, more tips for picking good words:

1\) *Pick obscure words*

Even if there is only one word a pattern could fit, if the opponent doesn't know that word, then they are forced to keep guessing letter-wise. Which makes things a little more tricky.

2\) *Pick shorter words*

There are more 3 and 4 letter words in the English language than 8 and 9 letter words.

3\) *Avoid too many repeated letters*

For example, MISSISSIPPI only has 4 unique letters, but once you've guessed I and S, you've uncovered 73% of the word, and there's really nothing else \_ISSISSI\_\_I could be.

4\) *Pick words with high entropy patterns*

**A Question of Uncertainty**

In [Information Theory](http://en.wikipedia.org/wiki/Information_theory), [entropy](http://en.wikipedia.org/wiki/Entropy_%28information_theory%29) relates to the uncertainty in a piece of information. It's measured in bits, and, for a set of equally likely outcomes, is calculated as the base two [logarithm](http://en.wikipedia.org/wiki/Logarithm) of uncertainty.

So a coin toss has an uncertainty of 2, because there are two possible, equally likely outcome. That gives an entropy of 1 bit. For a given character in a word, if we assume all letters are equally likely, then there is an uncertainty of 26 - so that gives an entropy of log2(26) = 4.7 bits.

But as pointed out above, all letters are not equally likely in the English language. So the entropy is more complicated to work out: *H = -SUM[p(ci)\*log2(p(ci))]*. Anyway, it turns out the entropy of a given unknown letter is 4.18 bits.

In the case of word patterns, we work out entropy as log2 of number of valid words matching the pattern, since all matching words have the same probability of being correct.

For the low entropy example above, there are 3 possible words that match the pattern so that would give an entropy of log2(3) = 1.58 bits. The 3 letter, high entropy example, on the other hand - with it's 179 possible solutions - would have an entropy of 7.48 bits.

**So Where Does This Leave Us?**

The idea is this - to come up with a scheme for scoring the 'quality' of a word in terms of how hard it is to guess in a game of hangman.

First, we score our word by its letter, as described above, to get the probability of guessing a correct letter. We then take one minus this to find the probability that a letter guess is wrong - the lower the probability of guessing a correct letter, the higher that word's score.

Entropy has a well define method of measurement in Information Theory, as discussed above.

But if we measure the entropy of a word before any letters are guessed, we find that all words of the same length have the same entropy. So instead, it would be more useful to measure a word's entropy after, say, some common letters have been filled in. Since most people start by guessing the vowels, that is what I'm going to go with.

In some cases, there are so many possible pattern matches, that you'd do better to simply make educated guesses at letters until the solution is found. For this, we work out the letter-wise entropy. Again, before any letters are guessed, all words with the same number of unique letters have the same entropy.

So. Each unknown, unique letter in a word can be one of those not already guessed. So we can work out the entropy, *H(alpha)*, of the alphabet, sans the letters already guessed. Then, multiply that by the number of unique letters left to find, n.

So for example, if we guess the vowels and get the pattern \_A\_, then the entropy is  2\*H(consonants) = 5.62 bits

**From a Practical Stand Point**

To work out the word entropy we can [download a dictionary](http://www.morewords.com/enable2k.txt), then [write some code](http://dl.dropbox.com/u/4635169/word-count.py) which will find and count the words which match our required pattern, excluding those containing already guessed letters.

We then find the 'smallest maximum' entropy - which of the character entropy and the word entropy is smallest. In most cases it'll be the word entropy.

And finally we multiply that by the probability, one minus big P, to assign to each word a score:

*(1-P)\*min{H(W), H(C)}*

Or you can use [this code](http://dl.dropbox.com/u/4635169/HangmanScorer.py).

In and of themselves, the scores this gives don't have any specific meaning - the exact score for each word will depend on your choice of dictionary and initial guess letters. But so long as you use them consistently, the scores should stand as an indicator of each word's relative 'quality'.

For example, by this system, CAT gets a score of 5.3, and EQUALITY gets a score of 1.4. So CAT is a much better hangman word than EQUALITY.

**So What's the Best Word**

JAZZ, apparently. In fact, while researching this blog, I came across a few [other](http://www.jkwchui.com/2010/04/the-best-hangman-word/) [people](http://140.177.205.236/2010/08/13/25-best-hangman-words/)'s attempts to find the best words for hangman. Pleasingly, they went with different approaches to me.

In fact, JAZZ never occurred to me when I was thinking up random good words. The best I thought of was WAX. Also reassuring is the fact that JAZZ does score highly under my system - 6.07 - and scores only slightly better than WAX, with its score of 5.92

QUIZ is an interesting word. It contains the two least common consonants and the two least common vowels (P=9.89%). But there are only 12 words that match \_UI\_, so it has low entropy. Its final score is 4.13 - lower than that of CAT, with its more common letter set (P=20.0%).

Similarly GYM; it has P=6.34% and has no vowels, but there are only 29 words it could be, so has a score of 5.48. Or MY, with P=4.38% but only 5 possibilities, score 3.18. So it's a matter of balance between probability and entropy.

Ideally, I'd have run a whole dictionary through my system to look for a list of best words. But I didn't. *You* can if you really want. Otherwise, I'd recommend one of the blogs linked above for lists.

**In Summary**

So there you go. You can score some of your own words if you so wish. But for on the fly word assessment, just remember, pick:

1\) Words with 'uncommon' letters\
2\) Words with fewer unique letters\
3\) Obscure words\
4\) Shorter words\
5\) Words with fewer repeated letters\
6\) Words with high entropy patterns

And if you're trying to guess a 4 letter word with an A in the second position, odds are someone is trying to outfox you with JAZZ.

Oatzy.

[Full disclosure: If I got the information theory stuff wrong, it's because I only know as much as the one chapter of [this book](http://www.amazon.co.uk/Must-Beautiful-Equations-Modern-Science/dp/1862075557/ref=sr_1_1?ie=UTF8&qid=1315782692&sr=8-1), and odd bits on wikipedia.]
