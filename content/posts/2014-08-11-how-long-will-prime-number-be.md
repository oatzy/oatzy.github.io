---
layout: post
title: How Long Will a Prime Number Be?
date: '2014-08-11T22:37:00Z'
author: Oatzy
tags:
- probability
- mathematical methods
- problem solving
- puzzles
- maths
modified_time: '2014-08-11T15:37:38.754-07:00'
thumbnail: /images/how-long-will-prime-number-be/exN.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-5294002417505298865
blogger_orig_url: https://oatzy.blogspot.com/2014/08/how-long-will-prime-number-be.html
---

File this under things I think about when I'm trying to get to sleep.

**The Question**

The idea is this - pick a random integer between 0 and 9. If it's prime, stop. If it's not prime, pick another random integer and stick it on the end of the first number. If this new number is prime, stop. If it isn't prime, pick another random integer, and so on.

So, for example:

1 -\> not prime\
2 -\> 12 -\> not prime\
7 -\> 127 -\> prime -\> stop.

The question is this - on average, how long would we expect the number to be when we get a prime?

**Sometime Programming Just Won't Cut It**

Normally, this is where I'd bust out Python and write a little program to run through the procedure a few times and see what happens. The problem is, [testing whether a number is prime](http://en.wikipedia.org/wiki/Primality_test) tends to be really slooooow.

The 'easiest' algorithm, [trial division](http://en.wikipedia.org/wiki/Trial_division) - literally checking if the number is divisible by any of the integers less than it - has (worst case) speed O(sqrt(n)). What this means is, each time we add a digit to our number, it will take ~sqrt(10) = 3.16 times longer to check if it's prime. And that time soon adds up. There are quicker algorithms, for example [AKS](http://en.wikipedia.org/wiki/AKS_primality_test), but they're too complicated to bother with.

Instead, we can figure out the answer with some good old-fashioned maths.

**Some Good Old-Fashioned Maths**

Lets re-state the problem - what we want to know is the expected length of the prime number. Here we use the standard definition for the [expectation value](http://en.wikipedia.org/wiki/Expected_value)

$$ <N> = \sum_{N=1}^{\infty} N \cdot p(N) $$

So now the problem is find p(N), which in this case is the probability that a number of length N is prime. Now, as any romantic mathematician will tell you, prime numbers are mysterious things, which are scattered about the number line seemingly at random. However, what we do have is the '[Prime Number Theorem](http://en.wikipedia.org/wiki/Prime_number_theorem)', which estimates the number of prime numbers smaller than n, as

$$ \pi(n) = \frac{n}{ln(n)} $$

where ln(n) is the [natural logarithm](http://en.wikipedia.org/wiki/Natural_logarithm). Here's a [Numberphile video](https://www.youtube.com/watch?v=l8ezziaEeNE) explaining the theorem.

So, for one digit numbers (numbers less than 10) there are ~10/log(10) = 4.2 prime numbers (well, technically 4, but this is an estimate). So the probability that a one digit number is prime is estimated as 0.42. The estimate gets better as the number of digits gets bigger.

Now, for numbers of two or more digits, the number of primes that are N digits long is (approximately) the number of primes less than 10^N minus the number of primes less than 10^(N-1). So then, the probability of an N-digit number being prime is the number of N-digit primes divided by the total number of N-digit numbers. It can be shown (homework) that this probability is given by

$$ p(N) = \frac{0.9N - 1}{0.9N(N-1)\,ln(10)} $$

Plotting this function, we see that the probability goes to zero as N goes to infinity

[![](/images/how-long-will-prime-number-be/pN.png)](/images/how-long-will-prime-number-be/pN.png)

In other words, the longer the number gets the less likely it is to be prime. In this case, you can probably guess what the expected length of our prime will be.

So we have

$$ <N> = \sum_{N=1}^{\infty} N \cdot p(N) = \sum_{N=1}^{\infty} \frac{0.9N - 1}{0.9(N-1)\,ln(10)} $$

And as N-\>infinity, N p(N) -\> 1/ln(10). What this means is the sum doesn't converge - it goes to infinity. So on average we expect our prime to be infinitely long.

**So Basically**

To cut a long story short, the procedure is most likely to stop when the number is only one digit long. Or else, the longer the number gets, the less likely the procedure is to stop. This is another reason why the programming solution was a non-starter.

Oatzy.

[Now stop doing maths and go to sleep.]
