---
layout: post
title: My hat contains a hidden message
date: '2024-03-17T16:49:00.000+00:00'
author: Chris Oates
tags:
- crochet
- maths
- binary
- design
modified_time: '2024-03-17T17:29:00.000+00:00'
---

I shaved my head.

My hair's been getting thinner for a while now, so I thought I'd try going all in.

I’m still getting used to it.

But one thing I _did_ expect, was that my head would feel colder now. So I needed a hat.

I looked over my save crochet patterns and found this one - [Widcombe C2C crochet hat](https://www.hanjancrochet.com/free-c2c-crochet-hat-patten/)

It uses a crochet technique called ‘corner-to-corner’ (c2c) - effectively the fabric is made up of squares, worked in diagonal rows.

The design as written is okay, but a little generic. I wanted something more meaningful.

The c2c effectively gives us a grid, and in the original design the middle band is a repeating pattern of 6x10 square blocks.

So the question was, what could I do with this?

Well a row of 6 squares gives us 6 bits, allowing us to represent 64 values - more than enough to encode characters of the (latin) alphabet.

Meanwhile we have 10 rows, and it just so happens that my name contains 10 letters - CHRIS OATES

In fact, we only need 5 bits to represent the alphabet, so we have one spare. I considered leaving it blank, or using it to represent uppercase/lowercase. But none of those looked very good, so I just used repeating blocks of 5x10.

The complete design looks like this

![Hat design](/assets/binary_hat/hat-pattern.jpg)

And here’s the completed hat

![Completed hat](/assets/binary_hat/finished-hat.jpg)

Following the pattern diagonally was... fun.

But at least my head isn't cold anymore.

Chris.