---
layout: post
title: Hidden messages and an optimal ternary scarf
date: '2024-01-20T18:22:00.000+00:00'
author: Chris Oates
tags:
- crochet
- maths
- optimisation
- coding
modified_time: '2024-01-20T23:43:00.000+00:00'
---

A while ago, I found a [pattern for a tunisian crochet scarf](https://raffamusadesigns.com/tunisian-crochet-ribbed-scarf-pattern/) that I kinda liked. The design was straightforward - just three solid blocks; I picked 1 blue, 1 grey, 1 cream.

I got maybe 20 rows into it, then got bored. I ended up [frogging](https://rowhouseyarn.com/blogs/news/frogging-to-frog-or-not-to-frog) it.

But now I have these three balls of super-soft aran yarn, and what to do with them?

I wondered if I could make the pattern more interesting by cycling - blue, grey, cream, blue, grey, ... - but that's not much more exciting.

I had the thought that I could completely randomise the colours - for each row, pick one of the three colours at random (roll a dice, even).

I like the idea of encoding information in arts and crafts. In my [temperature blanket](https://oatzy.github.io/2023/07/30/temperature-blanket.html) I encoded temperatures as different colours, and months as white and coloured rings representing binary numbers.

And here I have 3 colours - a [base 3 encoding](https://en.wikipedia.org/wiki/Ternary_numeral_system) - and, conveniently, three base-3 bits (trits?) can represent 27 values - enough for all 26 letters, plus a whitespace character.

# A simple plan

So suppose we want to make a scarf.

We have three colours, which we might map as

```jsx
0 -> cream
1 -> blue
2 -> grey
```

The most simple mapping of characters to numbers is to make `A=1, B=2, C=3`, etc. saving `0` for the whitespace character.

As mentioned, we're representing 27 characters so we need 3 rows per character.

If we take my name, `CHRIS OATES`, and translate it to ternary as above, we get

```jsx
010 022 200 100 201 000 120 001 202 012 201
```

Or in colours

![Basic mapping in tunisian crochet](/assets/ternary/basic.jpg)

Not too bad. But doesn't it feel a little... unbalanced?

Ignoring the space character (`000`) we have 14 cream, 7 blue, and 9 grey.

Cream (zeroes) are way over-represented.

Every possible 3 bit value is represented in the simple encoding, so in a random sequence of letters, we would expect all 3 colours to appear with roughly equal frequency... except, English isn't a random sequence of letters.

# Popularity contest

Some letters appear in the English language a lot [more than others](https://en.wikipedia.org/wiki/Letter_frequency).

So maybe we want to account for this in our encoding to get a more even balance of colours.

For example, if we assigned `E` as `222` then `2` would end up very much over represented. It would be better to assign `E` a value with all three bits like `012`

The 3 bit ternary numbers can be split into 4 broad groups

- 6 are one of each digit, e.g. `012`
- 3 are all the same digit (of which `000` is our space)
- 6 are two the same, split up, e.g. `010`
- 12 are two the same together; 6 left e.g. `001`, and 6 rights e.g. `100`

So the obvious thing is to assign the 6 one-of-each codes to the six most common letters (E, T, A, S, ...), and likewise the 2 all-the-same codes to the two least common letters (Q, Z)

The six two-split codes can be assigned to the 7th-12th most common letters, on the basis that colours clumped together are less pleasing.

How the actual codes within those groups are assigned is largely arbitrary (more on that later).

Here's one possible encoding [^1]

```bash
e -> 012   t -> 120   i -> 201
a -> 021   n -> 102   m -> 210

s -> 010   u -> 121   r -> 202
w -> 020   d -> 101   k -> 212

g -> 011   o -> 122   h -> 200
v -> 022   f -> 100   l -> 211

p -> 001   j -> 110   b -> 221
x -> 002   c -> 112   y -> 220

z -> 111   q -> 222
```

And here's my name again, using this encoding

```bash
112 200 202 201 010 000 122 021 120 012 010
```

and in colour

![Frequency mapping in stockinette](/assets/ternary/frequency.jpg)

Hmm... this looks even less balanced than before.

However, this time we have 11 cream, 9 blue, and 10 grey, not counting the space block. Almost perfectly balanced.

So what's the issue? The problem this time is that colours aren't well distributed. We have lots of repeated digits (10, including the white space block), and the blues are biased towards the right.

# Going wider

I said in the previous section that how the codes are assigned to letters within each group is arbitrary.

We can do better than that.

Suppose we look at [pairs of letters](https://en.wikipedia.org/wiki/Bigram) - can we assign codes so as to maintain 'evenness' across pairs? And will that make the encoding more even across whole texts? [^2]

For example, in the above we assigned `Q=222`. Now Q is (almost) always followed by a U, so it would be foolish to assign e.g. `U=220` as we would then get a run of five 2s in a row `222 220`

It would be better to give U a code with no 2s, say `101` -> `222 101`

We should also take into account the white space character. I want to keep white space pinned as `000`, so letters which tend to appear at the end of words should not end with 0s, and letters which tend to appear at the start of words should not start with 0s.

For example, if we assigned `Y=100` and `D=001`, we might suddenl**y d**iscover a run of 7 zeros - `100 000 001`

# A more perfect encoding

To figure out the 'best' encoding, we need a way to quantify or 'score' each possible encoding.

We did this implicitly, above, for the 3 bit codes - i.e. the all-different codes are higher scoring than the all-same codes because they have a higher variety of digits/colours.

Likewise, the two-same-split codes are higher value than 2-same-together codes because the colours are more spread out.

We just need to extend that logic to pairs of 3 bit codes (or equivalently, 6 bit codes) and come up with an empirical 'score' function, alike

```jsx
score(123, 213) = 1
score(111, 111) = 0
```

For scoring the 'spread' of digits, we can

1. look at each pair of bits
2. add 1 if different, else add 0 if same
3. divide by the total number of pairs (5)

e.g.

```jsx
220 021 -> 22, 20, 00, 02, 21 -> 0 + 1 + 0 + 1 + 1 = 3 -> 0.6
```

For 'balance' we can use [entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) with a base of 3

```jsx
- n0/6 * log3(n0/6) - n1/6 * log3(n1/6) - n2/6 * log3(n2/6)
```

where `n0` is the number of `0` digits, etc. [^3]

For example, in worst case scenario, all digits the same, we get

```jsx
6/6 * log3(6/6) + 0 + 0 = log3(1) = 0
```

and in the best case, two of each digit, we get

```jsx
3 * ( -2/6 * log3(2/6) ) = (3 * -1/3) * log3(1/3) = -1 * -1 = 1
```

So now we can smash (multiple) the balance score together with the spread score to get a combined score for a given pair of codes, e.g.

```jsx
s(121, 102) = (4/5) * (log3(6)/6 + log3(2)/2 + log3(3)/3)
            = 0.8 * 0.921
            = 0.736
```

Now we have to take into account how those codes are assigned to actual letter pairs. That is, it's better to assign high scoring codes to common pairs (EA) than to uncommon pairs (ZW)

Similar to how we can calculate the frequency of individual letters in the English language - by counting occurences in a text - we can also calculate the frequency of letter pairs in English.

We can use these frequencies as a weighting, by multipling the letter pair frequency by the score of the assigned codes.

So if we come up with a possible mapping, calculate the score for each possible letter pair and take the sum, we can calculate the total score for that mapping

```jsx
total score = sum [ f(c_i, c_j) * s(c_i, c_j) ]
```

For example, in the `A=1` encoding, we would calculate

```jsx
total score = f(a, a) * s(001, 001) + f(a, b) * s(001, 002) + ... + f(z, z) * s(222, 222)
```

# The best enough

What now?

Here's the tricky part - we have a method of scoring any given encoding, but how do we find the 'best' one?

The problem is, there are `26!` (factorial) possible ways of assigning codes to characters - `4 x 10^26` - that's more than something something in the universe! 🤯

Suffice to say, finding an optimal solution [^4] is not viable.

Instead, we can look at a [heuristic solution](https://en.wikipedia.org/wiki/Heuristic_(computer_science)).

The approach that worked the best for me was

1. generate a random starting mapping
2. for each character in the mapping, find the swap which produces the best score
3. repeat 2 until the score doesn't increase anymore
4. repeat 1+2 multiple times and pick the best scoring result

You can find my code [here](https://github.com/oatzy/ternary). I won't go into detail about the code in this post, as it is already quite long. I have provided code comments.

For my experiments, I grabbed a copy of [Frankenstein off Project Gutenberg](https://www.gutenberg.org/ebooks/84) to generate the bigram frequencies. This gives us `426_160` letter pairs

As the baseline, the scores for the mappings we already discussed are

- `A=1` -> `0.51581`
- letter frequency-based -> `0.58679` [^5]

I tried multiple runs and the best score I got was `0.66869`

Here's what that mapping looks like

```bash
a -> 210   b -> 122   c -> 022
d -> 121   e -> 021   f -> 221
g -> 011   h -> 012   i -> 101
j -> 100   k -> 001   l -> 020
m -> 220   n -> 202   o -> 120
p -> 110   q -> 222   r -> 201
s -> 212   t -> 102   u -> 010
v -> 002   w -> 211   x -> 200
y -> 112   z -> 111
```

I tried running it a few times, and it consistently turned up this mapping as the best, which suggests it's the most optimal. Or perhaps it's the most optimal solution that this method can generate; maybe a different optimisation method could generate an even better solution. [^6]

Here's what my name looks like with the optimised mapping

```bash
022 012 201 101 212 000 120 210 102 021 212
```

and here it is in colours

![Optimal mapping in half-treble crochet](/assets/ternary/optimal.jpg)

Doesn't that look so much more balanced?

Here we have 11 cream, 10 blue, and 12 grey, this time including the space block since it was part of the optimisation. It's almost perfectly balanced, and this time it also has a much better spread of colours; we have only 5 repeated digits (of which 2 are in the space block)

# Spinning out

This idea can be extended to different bases. For example, with 4 colours and 2 rows per colour you get 64 possibilities - enough for upper and lower case, 10 digits, 1 space, and 1 left over for a period (or exclamation mark!)

The principle remains the same, you just have more character combinations to deal with.

Similarly, I've been talking about a scarf, but this would work just as well for a blanket. For, what is a blanket if not a really wide scarf?

Alternatively, we could construct a blanket of squares - similar to my temperature blanket - with one block per character comprised of 3 bands of colour representing the 3 bits.

This can make for a much more striking design

![Example basic mapping in squares design](/assets/ternary/squares.jpg)

Tho in the squares case, the criteria for what is optimal is slightly different.

For example, in the above the second and third to last squares are `202 012` which has no repeated digits

But with squares

```bash
22222 22222
20002 21112
20202 21012
20002 21112
22222 22222
```

the last digits [^7] - the outer rings of 2s - **are** adjacent.

And that's only thinking one-dimensionally. For a blanket, we're going to have a grid, with the text split across multiple rows. How do we account for that?

And notice that in a square the outer ring would use a lot more yarn than the inner ring. So maybe we'd like to ensure that each digit is represented in each position roughly equally - that we use roughly equal amounts of each colour.

Maybe I'll come back to this idea in a future blog...

# Unravelled

At this point, you're expecting to see a completed scarf?

The truth is, I already used some of the yarn I mentioned to [make a sock](https://www.ravelry.com/projects/oatzy/crochet-slipper-socks). Yes, just the one sock. And maybe someday I'll get around to making it a matching pair.

And maybe someday I'll even make a ternary scarf.

But first I need to figure out what message is worth wearing around one's neck...

Chris.

[was this all just a waste of time? you must be new here]

---

# Epilogue: Structure and interpretation of scarf

Suppose you're presented with a scarf. It's made up of stripes of three different colours, but the patterns seem... odd. Random? But why would anyone make a random patterned scarf?

Given that there are three colours, you think maybe it's a base 3 encoding, and you intuit that 3 rows gives you 27 sequences - enough for 26 letters and a space.

You might assume a basic encoding - `A=1`, `B=2`, etc. But you don't know how the colours map to bits `0`, `1`, `2`

But then, there are only 6 possible arrangements, so you can just try them all, and see what yields a meaningful message. Perhaps you notice a particular colour regularly appears in blocks of 3, and you think "maybe that's a space character". You call that colour `0` and now you only need to figure out which colour is `1` and which is `2` - two possibilities.

It's not trivial, but it's possible. This feels ideal to me.

By comparison, you couldn't infer the frequency-based or optimal encoding in the same way - in the first one, some of the assignments are arbitrary, and in the second the assignment is heuristic so even following the same procedure you might not reproduce the same mapping.

If the message (scarf) is long enough, you can ignore the base 3 aspect, treat each 3-row sequence as an arbitrary symbol and perform [frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis) to figure out the letter mapping.

But we're talking a [Tom Baker length of scarf](https://en.wikipedia.org/wiki/Fourth_Doctor#/media/File:The_Fourth_Doctor_(6097263309).jpg), at least.

# Appendix: the example stitches

Each of the examples uses a different stitch/technique. Some may call this an unfair comparison, but it made things more interesting for me ;)

The first example, for the `A=1` encoding, was done in [tunisian crochet](https://en.wikipedia.org/wiki/Tunisian_crochet), using repeated tunisian simple stitch (TSS)

The second example, for the frequency encoding, was knitted in a basic [stockinette](https://en.wikipedia.org/wiki/Basic_knitted_fabrics#Stockinette/stocking_stitch_and_reverse_stockinette_stitch) - 1 row knit stitch + 1 row purl stitch.

In this case there are actually two rows per bit (1 knit + 1 purl). This was mostly so the colour change would always happened along the same edge, for my convenience.

The last example, for the optimal encoding, was done in regular crochet, using repeated half-treble (Htr) crochet stitches in UK notation, or half-double (Hdc) in US notation.

I didn't do an example for the squares because that would have required cutting the yarn (and also I'm lazy).

# Footnotes

[^1]: For the common-ness of letters I [copied Morse code](https://en.wikipedia.org/wiki/Morse_code#Alternative_display_of_common_characters_in_International_Morse_code), which isn't strictly accurate to the English language. Tho it should be said that any frequency mapping is not going to be universally correct. It depends on the text it's calculated from. Tho they do tend to align at the extremes.

[^2]: Naturally we can extend this to groups of 3 letters, groups of N letters, or whole words. But let's not get carried away ;)

[^3]: Fun fact, even tho there are `27 * 27 = 729` possible pairs of 3 digit codes, if we ignore permutations, there are only 7 unique partitions of 6 digits into 3 types, and therefore only 7 entropies to calculate

    ```jsx
    600 -> 0
    510 -> 0.410
    420 -> 0.579
    411 -> 0.790
    330 -> 0.631
    321 -> 0.921
    222 -> 1
    ```

[^4]: there are at least two optimal solutions; for any given solution, we can swap the 1s with the 2s and get another mapping with the exact same score. We can't do the same with 0s since we pinned the white space character as `000`, otherwise there would be 6 equivalents for each solution.

[^5]: as mentioned in footnote 1, the frequency encoding in this blog is based on Morse code. An encoding based on measured letter frequencies scores `0.62144`; better than Morse, but still less than 'optimal'

[^6]: This mapping was a close second

    ```bash
    a -> 120   b -> 211   c -> 011
    d -> 212   e -> 012   f -> 112
    g -> 022   h -> 021   i -> 202
    j -> 200   k -> 002   l -> 010
    m -> 110   n -> 101   o -> 210
    p -> 220   q -> 111   r -> 102
    s -> 121   t -> 201   u -> 020
    v -> 001   w -> 122   x -> 100
    y -> 221   z -> 222
    ```

    Its score is `4 x 10^-16` less than the 'optimal'. But notice, if you swap all the 1s for 2s and vice versa in the optimal mapping you get this mapping! This is actually expected, per footnote 4. The difference in scores is probably a floating point rounding quirk.

[^7]: I think you would call that.. little-endian? I could never remember which is which