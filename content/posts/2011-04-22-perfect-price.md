---
layout: post
title: The Perfect Price
date: '2011-04-23T01:10:00Z'
author: Oatzy
tags:
- money
- sociology
- over-thinking
- statistics
- graph
- everyday maths
- problem solving
- hypothetical question
- hand-waving
- maths
- modelling
- ted talks
modified_time: '2011-04-22T19:29:50.007-07:00'
thumbnail: /images/perfect-price/Norm.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-3324918830780153164
blogger_orig_url: https://oatzy.blogspot.com/2011/04/perfect-price.html
---

Say you made a thing. You put a lot of time and effort into your thing, and you're so proud of it, you want to share it with the world. But how much should you charge for it?

If you price it too high no-one will buy it. If you price it too low, you won't make a profit. And you spent far too much time and money on your thing to not turn a profit.

So you go to a good friend - who just so happens to work in marketing - and ask him to do a little market research for you. This friend is a pretty cool guy, so he goes out on to the streets and shows people your product, and asks them how much they'd be willing to pay for one. But being an expert, he does it in such a way as to get honest and unbiased answers.

After an afternoon of efficient (and pro bono) work, he comes back to you with good sample of 750 responses. After discarding 250 who weren't interested in your product, he analyses the remaining 500 responses.

And by some pleasing miracle, he finds that the prices these people are willing to pay approximates a [normal distribution](http://en.wikipedia.org/wiki/Normal_distribution), with average £10 and standard deviation £2.50

[![](/images/perfect-price/Norm.png)](/images/perfect-price/Norm.png)

So what do you charge? £10?

The people who said they would only pay a price less than £10 won't buy it, because they're cheap-skates, and who needs their business anyway. But on the plus side, half the people surveyed - 250 people - said they'd pay £10 or more. So you would expect to make about *£2,500* from the sample group.

Which isn't too bad. But can you do better?

You decide, because you're a bit of a smart-arse, to work out a function for your expected return for if you were to charge £x.

So what you do first is [integrate](http://en.wikipedia.org/wiki/Integral) your normal distribution function from x to infinity. This gives you the shaded-area under the curve - the proportion of your sample willing to pay £x,

[![](/images/perfect-price/Norm-int.jpg)](/images/perfect-price/Norm-int.jpg)

You then multiply that by the sample size (500) to get the *number* of people willing to play that amount, and by £x to get how much money you'd make all together. Easy.

Still with me?

Your resulting function looks like this,

[![](/images/perfect-price/erfc.gif)](/images/perfect-price/erfc.gif)

*(before being multiplied by the sample size)*

*erfc* is the [complementary error function](http://en.wikipedia.org/wiki/Complementary_error_function), but you needn't worry about what that is exactly, because that's what [Wolfram Alpha is for](http://www.wolframalpha.com/input/?i=x%2F2+erfc%28%28x-10%29%2F%282.5sqrt%282%29%29%29). So, proud of yourself for worked that out (somehow), you plot a graph of this function giving you a graph that looks like this

[![](/images/perfect-price/erfc-plot.jpg)](/images/perfect-price/erfc-plot.jpg)

And right away you spot that there is definitely a peak on that graph, and know that that would be the optimal amount to charge.

[![](/images/perfect-price/max-plot.jpg)](/images/perfect-price/max-plot.jpg)

So with [Wolfram Alpha' help](http://www.wolframalpha.com/input/?i=x%2F2+erfc%28%28x-10%29%2F%282.5*sqrt%282%29%29%29+maximum+between+5+and+10) again, it's a piece of cake for you find that that peak is at x=*£7.73*.

This is your best price. Which is a couple of quid less than the average your sample was willing to pay. But if you were to charge this amount, 409 people from your sample would be willing to buy your thing - and that would make you a respectable ~<em>£3,162 </em>

Good times!

And now you sit back in your chair and laugh, because a little maths just made you an extra *660-odd* quid. Which isn't bad going.

**As it turns out**, if you ask people what they'd be willing to pay (and if their responses approximate a normal distribution) then the price that maximises profits - the one that balances per-unit profit, and expected sales numbers - is ALWAYS less than the average of what people are willing to pay.

And cinemas - whose escalating prices are discouraging movie-goers and leading to declining profits - could perhaps learn something from this. But probably won't.

**Spherical Cow in a Vacuum**

The world, as you may have noticed, is not an [ideal place](http://en.wikipedia.org/wiki/Spherical_cow). Life is never so simple.

The [central limit theorem](http://en.wikipedia.org/wiki/Normal_distribution#Central_limit_theorem) says a normal distribution will often suffice (for a large enough sample population), but it's not necessarily going to be the best fit. Or it might be that the results from your sample [don't scale](http://en.wikipedia.org/wiki/Sample_bias) to the general public.

But much worse than that is people. People aren't rational, people don't necessarily know what they want, people don't know what things are worth, and people are surprisingly easy to manipulate - to an extent, you can effectively tell people what they want to pay; as anyone in marketing will proudly tell you, while grinning maniacally and eying up your wallet.

So in that vein, I leave you with these two TED talk - 

[Dan Gilbert on our mistaken expectations](http://www.ted.com/talks/lang/eng/dan_gilbert_researches_happiness.html)\
[Rory Sutherland: Life lessons from an ad man](http://www.ted.com/talks/lang/eng/rory_sutherland_life_lessons_from_an_ad_man.html)

Watch them.

Oatzy.

[There are lots of other [TED Talks](http://www.ted.com/) on a huge range of subjects. Most worth watching. Some of them are particularly fantastic. Go explore!]
