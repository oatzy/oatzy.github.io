---
layout: post
title: 'Follow Up: A Binary Proof and a Trinary Clock'
date: '2015-01-12T00:55:00Z'
author: Oatzy
tags:
- time
- binary
- clock
- nerd
- proofs
- android
- maths
modified_time: '2015-03-14T15:38:48.874-07:00'
thumbnail: /images/follow-up-binary-proof-and-trinary-clock/Screenshot_2015-01-05-15-52-58.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-7939085758103022734
blogger_orig_url: https://oatzy.blogspot.com/2015/01/follow-up-binary-proof-and-trinary-clock.html
---

In the [last blog](http://oatzy.blogspot.co.uk/2015/01/metric-and-binary-clocks-for-android.html) I talked about making a binary clock widget (for Android) using [Zooper](https://play.google.com/store/apps/details?id=org.zooper.zwfree&hl=en_GB), and I made a claim about how individual binary digits can be extracted from a decimal number - what follows is an explanation/proof of why it works.

**The Claim**

The n-th digit of the binary representation of a number, x, is a zero if \(x \bmod 2^{n+1} \lt 2^{n}\), or a one otherwise.

**Proof**

To start, we express our number x as a sum of powers of 2. This makes sense, since this is basically how binary works. So we have

\[ x = \sum_{i=0} a_{i} 2^{i}\]\
where the \(a_i\) equal either 1 or 0 - these are equivalent to the i-th digits in the binary form of the number (reading right to left). For example, if x=5 then \(a_0=1, a_1=0, a_2=1\) and all other \(a_i=0\) (since 5 in binary is 101).

So lets split the sum up into three parts and expand

\[\begin{align*}
x &amp;=\ a_{n} 2^{n} \ +\ \sum_{i=0}^{n-1} a_{i}2^{i} \ +\ \sum_{i=n+1} a_{i} 2^{i} \\ \\
&amp;= a_{n} 2^{n} \\
&amp;+ (a_{0}2^{0} + a_{1}2^1 + \ldots + a_{n-1}2^{n-1}) \\
&amp;+ (a_{n+1}2^{n+1} + a_{n+2} 2^{n+2}+ a_{n+3} 2^{n+3}+\ldots)
\end{align*}\]\
Notice that in the second set of brackets, all the terms are divisible by \(2^{n+1}\) - so if we take mod \(2^{n+1}\), all of those terms disappear

\[ x \bmod 2^{n+1} = a_{n} 2^{n} + (a_{0}2^{0} + a_{1}2^1 + \ldots + a_{n-1}2^{n-1}) \]\
The terms in the remaining set of brackets [sum to](https://en.wikipedia.org/wiki/Geometric_series) some value between 0 and \(2^{n}-1\) (depending on the values of the \(a_i\)). We'll call this \(\sigma\) for convenience.

Therefore, if \(a_n = 1\) then

\[ x \bmod 2^{n+1} = 2^{n} + \sigma \ge 2^{n}\]\
And if \(a_n = 0\) then

\[ x \bmod 2^{n+1} = \sigma \le (2^{n} - 1) \lt 2^{n}\]\
QED

**Generalisation**

As with powers of 2, we can write numbers as the sum of powers of any number/base. For example, we can write 11 as \(2\cdot 3^0 + 0\cdot 3^1 + 1\cdot 3^2\) - or to put it another way, 11 in base 3 is 102.

So in general, we can write a number 'x' in terms some base 'b' as

\[ x = \sum_{i=0} a_{i} b^{i}\]\
where the \(a_i\) are whole numbers between 0 and (b-1) - equivalent to the i-th digits of x in base 'b'. So for example, for x=11 and b=3 we'd have \(a_0 = 2, a_1 = 0, a_2 = 1\) and \(a_i=0\) for all other i.

As before, we can split the summation and expand. But this time we're going to divide through by \(b^n\) as well

\[\begin{align*}
\frac{x}{b^n} &amp;=\ a_{n} \ +\ \frac{1}{b^n}\sum_{i=0}^{n-1} a_{i}b^{i} \ +\ \frac{1}{b^n}\sum_{i=n+1} a_{i} b^{i} \\ \\
&amp;= a_{n} \\
&amp;+ \frac{1}{b^n}(a_{0}b^{0} + a_{1}b^1 + \ldots + a_{n-1}b^{n-1}) \\
&amp;+ (a_{n+1}b^{1} + a_{n+2} b^{2} + a_{n+3} b^{3}+\ldots)
\end{align*}\]\
And now, all the terms in the last bracket are divisible by just 'b', so taking a modulo of 'b' will make those terms disappear. So we have

\[ \frac{x}{b^n} \bmod b = a_n + \varepsilon \]\
where \(\varepsilon \le \frac{b^{n}-1}{b^{n}} \lt 1 \).

And from this, we can define a general function for extracting \(a_n\) - the n-th digit of x in base 'b' - as

\[ D^{n}_{b}(x) = \left \lfloor{ \frac{x}{b^{n}} \bmod b }\right \rfloor\]\
where the brackets mean 'floor', or round down to the nearest whole number - basically, get rid of \(\varepsilon\).

So as an example, the zeroth and first digits of 35 in base 16 (hexadecimal) are

\[ D_{16}^{0}(35) = \left \lfloor{ \frac{35}{16^{0}} \bmod 16 }\right \rfloor = \left \lfloor{ 35 \bmod 16 }\right \rfloor&nbsp; = 3 \\ D_{16}^{1}(35) = \left \lfloor{ \frac{35}{16^{1}} \bmod 16 }\right \rfloor = \left \lfloor{ 2.1875 \bmod 16 }\right \rfloor&nbsp; = 2\]\
So 35 in hexadecimal is 23. Easy.

<strong>Trinary Clock </strong> [[download]](https://www.dropbox.com/s/xfxtzcqxtsxs164/trinary-clock.zw?dl=0)

[![](/images/follow-up-binary-proof-and-trinary-clock/Screenshot_2015-01-05-15-52-58.png)](/images/follow-up-binary-proof-and-trinary-clock/Screenshot_2015-01-05-15-52-58.png)

15:52

The thing is, binary clocks are great and all. But they're old hat. So now we have a way of finding the individual digits of a number in any base, we can make something a little more unique - a trinary clock.

[Before](http://oatzy.blogspot.co.uk/2015/01/metric-and-binary-clocks-for-android.html), when I constructed the binary clock, I used rectangles for each binary digit, which changed colour depending on whether the digit it represented was a one or a zero. For a trinary clock we'd need each rectangle to have 3 state - 0, 1, 2. The problem is, Zooper can only do 2-state logic - if-then-else - not else-ifs, and no nested if-statements. So we can't make a rectangle that switches between 3 colours.

Instead, I made each segment a progress bar with values 0-2. For the current value of each bar/digit, we can use the formula we found above - \(D^{n}_{3}(x) = \frac{x}{3^n} \bmod 3\).

For example, for the 3rd segment (n=2) of the hours ring, we'd set the current value to

```
$(#DH#/9) % 3$
```

The progress bar automatically rounds values down to the nearest whole number, so we don't have to worry about getting rid of any decimals. But you could add a 'floor' function if you wanted.

Like the binary clock, I made the sizes of each segment proportional to the values they represent - the three-segment is 3 times bigger than the one-segment, etc. And to make reading clearer, I've made the leading edge of each segment a darker blue - that way it's easier to tell where one segment ends and the next one begins.

<strong>Quinary (Base 5) Clock </strong> [[download]](https://www.dropbox.com/s/qf8rpja23i334c7/quintary-clock.zw?dl=0)

[![](/images/follow-up-binary-proof-and-trinary-clock/Screenshot_2015-01-05-22-44-54.png)](/images/follow-up-binary-proof-and-trinary-clock/Screenshot_2015-01-05-22-44-54.png)

22:44

Once you've figured out the trinary clock, adapting it to other bases is very straightforward.

<strong>Decary (Base 10) Clock </strong> [[download]](https://www.dropbox.com/s/q181cj6qh8vxvk9/decary-clock.zw?dl=0)

[![](/images/follow-up-binary-proof-and-trinary-clock/Screenshot_2015-01-06-22-16-19.png)](/images/follow-up-binary-proof-and-trinary-clock/Screenshot_2015-01-06-22-16-19.png)

22:16

You get the idea..\.

**Finally**

As far as telling the time goes, all the clocks in this and the previous blog are pretty..\. challenging. At least until you get the hang of it. But they look cool. And that, I think is worth the extra effort. If I ever get a smartwatch I'll probably try to port some of these designs over. And if/when I do, you can bet I'll post them here.

[edit] - Android Wear versions are [here](http://oatzy.blogspot.co.uk/2015/03/watch-face-concepts-for-android-wear.html).

Oatzy.

[Decary? Really..?]
