---
layout: post
title: Su Doku Solver
date: '2011-08-21T02:41:00Z'
author: Oatzy
tags:
- programming
- su doku
- nerd
- python
- infographic
- problem solving
- hand-waving
modified_time: '2011-08-21T06:53:17.734-07:00'
thumbnail: /images/su-doku-solver/puzzle.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-2031990312790562501
blogger_orig_url: https://oatzy.blogspot.com/2011/08/su-doku-solver.html
---

**Cold Hard Logic**

Let's be frank, [Su Doku](http://en.wikipedia.org/wiki/Su_doku) solvers are dime a dozen. My favourite is the one in [Google Goggles](http://www.google.com/mobile/goggles/#text) - you point your camera at a puzzle and it uses OCR to interpret it, then solves it for you. None of that faffing with inputting the puzzle by hand. Anyway.

At the most basic level, computers run on maths and logic. So logic puzzles *should* be easy for computers to solve - it's just following a collection of logical rules. No creative thinking required.

The problem are,

1\) Inputting a problem in a form that the computer can parse (understand)\
2\) Translating the logical rules into a form the computer can apply\
3\) Applying said rules to a given input problem to find its solution.

Here's the main puzzle I'll be using as the example for this post [[source](http://www.conceptispuzzles.com/index.aspx)]. Feel free to try and solve it yourself before continuing (it should be easy).

[![](/images/su-doku-solver/puzzle.png)](/images/su-doku-solver/puzzle.png)

**The Rules**

So what are the rules? In the traditional version you're presented with a 9x9 grid, with some numbers already filled in. The idea is to enter into the grid the numbers 1-9, so that each number appears only once in each row, column, or box (3x3 square).

So that's fairly straight forward. But in that particular form, the rules are really only good for checking if your solution is right.

**Brute Force**

This *can* be use in a [brute-force](http://en.wikipedia.org/wiki/Brute-force_search) approach to solving, e.g.

1\) Stick numbers in empty squares at random\
2\) If any of the numbers break the rules, try again\
3\) Repeat until the right solution is found.

But that's incredibly inefficient and inelegant, and certainly not the way it's solved by people in the real world.

As an example, say our placement technique is this - take the numbers missing from each row, and just shuffle them around within their given row.

[There are probably better brute-force methods.]

If we use this approach on the puzzle above, there are *~4.95E26* possible number placements ([permutations](http://en.wikipedia.org/wiki/Permutations)), of which only one is correct. Say our computer can check *1 billion* *solutions per second*, it would take *16 billion years* to solve. Which is about *2 billion years* longer than the current [age of the universe](http://en.wikipedia.org/wiki/Age_of_the_universe).

As a ball park estimate, the general formula for the number of permutations for a grid of side *n* is given by -\> *((n-a)[!](http://en.wikipedia.org/wiki/Factorial))^n  -* Where *a* is the average number of numbers already placed in each row.

If, for example, we try to solve a 16-grid with *a=8* (half the numbers already placed), then the number of possible permutations is a mind-meltingly inconceivable *4.88x10^73*. At *1 billion checks per second*, that would take *1.5x10^57 years* to solve - *1 billionth* the lifespan of a black hole with the mass of the sun ([according to wikipedia](http://en.wikipedia.org/wiki/1_E19_s_and_more)).

This is an example of a *non-polynomial* time (NP) algorithm. More on that later.

**Rewriting the Rules**

The rules can be re-interpreted and applied in two fundamental ways

1\) *Which is the only square this number can appear in?*

That is, a particular number has to go in one particular square, because if you try to put it in any other square in that row (or column, or box) it will break the rules.

This is the most common approach in real world solving - that is, "three can't go in that row, or those columns because they already have threes in them, so it must go there" sort of thing.

[![](/images/su-doku-solver/sudoku-method1.png)](/images/su-doku-solver/sudoku-method1.png)

2\) *What is the only number that can go in this square?*

That is, if every other number already appears in the same row, column, or box as a given square, then that square can only be one particular number.

This is most obvious in the case where every other number in a given row is already filled in, but can also be used by considering all the rows, columns and boxes a square belongs to.

[![](/images/su-doku-solver/sudoku-method2.png)](/images/su-doku-solver/sudoku-method2.png)

This tends to be required more in the harder puzzles; you could probably solve the above puzzle by Rule One alone.

**Setting Up The Problem**

First of all, we create our grid. We can refer to each square in the grid by a sort of coordinate - *(i,j)* - with the square in the top left corner being [*(0,0)*](http://en.wikipedia.org/wiki/Zero-based_numbering) and the square in the bottom right being *(8,8)*

[![](/images/su-doku-solver/co-ordinates.png)](/images/su-doku-solver/co-ordinates.png)

We reference *Row i* as the set *{(i,j) : j in [0,8]}* and *Column j* as *{(j,i) : j in [0,8]}*

For boxes, we note that the index for the top-left square of each box are multiples of 3 - (0,0) (0,3) (0,6) (3,0) etc<em>. So, Box (m,n)</em> is given as *{(3m+i,3n+j) : i,j in [0,2]}* for *m,n in [0,2]*

So from this we can, for example, check the correctness of a puzzle (by rows) like this:

> <span style="color: orange">for</span> i <span style="color: orange">in</span> <span style="color: purple">range</span>(0,9):\
>     <span style="color: orange">for</span> j <span style="color: orange">in</span> <span style="color: purple">range</span>(0,8):\
>         <span style="color: orange">for</span> k <span style="color: orange">in</span> <span style="color: purple">range</span>(j+1,9):\
>             <span style="color: orange">if</span> Grid[i][j] == Grid[i][k]:\
>                 <span style="color: orange">return</span> <span style="color: #274e13">"incorrect puzzle"</span>

Checking columns and boxes works similarly.

If we have a fancy GUI, then inputting and parsing the grid is pretty straight forward. But we don't. So instead, we input the puzzle as one long string -\> <span style="font-family: &quot;Courier New&quot;,Courier,monospace">puzzle =</span><span style="color: #38761d; font-family: &quot;Courier New&quot;,Courier,monospace">"???36?9???2?.."</span>

<span style="color: #38761d"><span style="color: black">The first row is given by the characters (numbers) numbered [0,..,8], the second row is [9,..,17], and so on. In general, *row i* is the set of characters with index [9i,..,9i+j,..\.,9i+8]. </span></span>

<span style="color: #38761d"><span style="color: black">Parsing our puzzle into the Grid works like this then:</span></span>

> <span style="color: orange">for</span> i <span style="color: orange">in</span> <span style="color: purple">range</span>(0, 9):
>
>     <span style="color: orange">for</span> j <span style="color: orange">in</span> <span style="color: purple">range</span>(0, 9):
>
>         Grid[i][j] = puzzle[9i+j]

And so on..

**Applying the Rules**

Now, if you've done Su Dokus, you might be familiar with the technique of filling each square with the numbers one to nine and eliminating numbers as appropriate. That's basically the bulk of how this solver works:

1\) Assign to each empty square (<span style="color: #38761d">"?"</span>) the set *[1,..\.,9]*

[![](/images/su-doku-solver/number-sets-cropped.png)](/images/su-doku-solver/number-sets-cropped.png)

2\) For each number in a given square's set:\
    a) Check to see if that number is already fixed in another square in the same row, column, or box as the square in question. If so, eliminate the number from that square's set.

3\) Repeat for all squares in the grid

[![](/images/su-doku-solver/number-sets-elim-crop.png)](/images/su-doku-solver/number-sets-elim-crop.png)

From there, we can apply *Rule Two*:

4\) For each square:\
    a) if that square's set contains only one number, fix that square's value accordingly.

[![](/images/su-doku-solver/rule2-example.png)](/images/su-doku-solver/rule2-example.png)

5\) Go back to (2). Repeat until no more squares can be fixed.

[![](/images/su-doku-solver/elim-seq.png)](/images/su-doku-solver/elim-seq.png)

You can actually created a shortcut for this - create a collection of sets for each row (etc.), which contain the values already fixed in that row. That way, instead of checking every square along each row for fixed values, you just check in that row's set. (Trust me, it's easier.)

Applying *Rule One* is easy as looking along each row (or column, or box) to see if a given number appears in only one of the squares.

[![](/images/su-doku-solver/ruleone-example.png)](/images/su-doku-solver/ruleone-example.png)

Or more technically,

1\) For a given row (etc), for each number 1-9:\
    a) count how many times that number appears in square sets in that row\
    b) if a number's count equals 1, fix the value of the square it appears in accordingly.

2\) If you fix any new squares this way, go back to *(2)* to see if that will allow you to set any more squares.

You then just loop through rules *One* and *Two* until the puzzle is (hopefully) solved.

**One More 'Rule'**

In fact, this is just Rule Two, but with an added 'quirk'.

Here's what happens if you apply the method, so far, to a more difficult puzzle

[![](/images/su-doku-solver/hard-stuck.png)](/images/su-doku-solver/hard-stuck.png)

This is where the program gets stuck. What do you do from here? If we focus on the bottom-right corner box

[![](/images/su-doku-solver/hard-bottomcorner.png)](/images/su-doku-solver/hard-bottomcorner.png)

Notice there are no squares that can take only one value, and no values that only appear in one of the squares.

But look on that bottom row - the circled boxes can only take the values 3 or 5. What this means is that 3 and 5 can't go in any other of the squares in that box. So we eliminate 3s and 5s from the other squares in that box. Similarly for the 1/6 squares in the middle.

[![](/images/su-doku-solver/hard-bottomcorner-simp.png)](/images/su-doku-solver/hard-bottomcorner-simp.png)

We now have the square in the top-right of the box that can only be 8, and the middle-right that can only be 9. So we fix those values. And from there, it's pretty straight forward to solve the rest - going back to looping through *Rules* *Two* and *One*.

Not only is it tricky to spot in real world solving, it's also tricky to translate it into computer logic. It mostly involves looking for pairs of squares in a box (etc.) which have matching sets of size two (or triplets, size 3, or etc.). Fortunately, this sort of thing doesn't come up often.

**A Note on <em>P versus NP</em>**

So as mentioned above, it's easy enough to apply the standard rules (as states) to check if a solution is correct - you just check to make sure no number appears more than once in any given row, column, or box.

[![](/images/su-doku-solver/sudoku-solution-error-row.png)](/images/su-doku-solver/sudoku-solution-error-row.png)

It turns out, checking the correctness of a puzzle can be done in [polynomial time](http://en.wikipedia.org/wiki/Polynomial_time#Polynomial_time) (fast). For a grid of side *n*, the time required to check a solution\* is given by *-\> 3(n^3 - n)/2*

..Multiplied by the amount of time it takes a computer to work out if 2 numbers are equal or not (call this time t). So for a 9-grid, that time is *972t*.

For a grid of side *n=100*, the time is *~1.5million t*. Which on a modern computer is peanuts. For example, if our hypothetical computer can check *1 billion* 9-grids in one second, then it can check *650,000* 100-grids in a second.

By comparison, actually solving the puzzle - by the method outlined about, and by all other known methods - is done in [non-polynomial time](http://en.wikipedia.org/wiki/Time_complexity).

What this means, is that if you apply this algorithm to a larger grid - say, a *25x25*, or a *36x36* grid - then the amount of time it will take to solve the puzzle increases *rapidly* (exponentially), to the point where a puzzle couldn't be solve in the lifetime of the universe.

But, since checking the puzzle for correctness is polynomial, even if the puzzle took longer than the life of the universe to solve, you could still check to see if the solution is correct (that no number appears more than once in each row, etc) in a reasonable amount of time.

As mentioned above, the brute-force method outlined is non-polynomial (NP). Notice that it takes catastrophically longer - 70 orders of magnitude - to *solve* a 16-grid by brute-force, than it takes to *check* the solution to a, much larger, 100-grid.

Admittedly, I don't know what the time function is for the method outlined above. But suffice it to say, it's more efficient than the brute-force, but still non-polynomial.

What [P versus NP](http://en.wikipedia.org/wiki/P%3DNP) asks, then, is

*if the solution to a problem can be checked in polynomial time (quickly), then does there exist an algorithm that can* solve *the problem in polynomial time?*

At present, this is one of the great unsolved questions of mathematics and computer science, and a proof of whether or not P=NP will earn its discoverer [\$1million](http://en.wikipedia.org/wiki/Millennium_Prize_Problems)..\.

**Where's The Code?**

You'll probably have noticed, I've given a general, hand-wavy outline of how a program would work, and only given odd snippets of code.

I did write a solver in Python a few years back. I'd taken a Java programming course in my first year at university, and when the lecturer discussed a tic-tac-toe (naughts and crosses) playing program, it gave me the idea of how to represent a grid in a way a computer can parse. It also made me realise that there is actually a point to [object-oriented programming](http://en.wikipedia.org/wiki/Object-oriented_programming).

Anyway, long story short, I wrote the solver 3 years ago. It's kind of sloppy and inelegant. And it can't handle the 'tricky' puzzles - although, oddly enough, according to my notebook, I had worked out a way of implementing it, but apparently never did.

Or to put it another way, it works, but compared to the myriad others out there, it's nothing special.

If you're interested, as I mentioned at the beginning there are plenty of other solvers out there. They might not work according to the methods discussed in this post. But you should at least have an idea of how one might work, now.

And as a final note, these methods can also be used for hand-solving. It's generally not necessary to be so rigidly systematic, though. It's easier for humans to pick out number placements at a glace, without having to go through the whole *set-and-elimination* approach.

**In Case You Were Interested**

Here's the solution to the Su Doku at the top of the page

[![](/images/su-doku-solver/sudoku-solution.png)](/images/su-doku-solver/sudoku-solution.png)

You're on your own with finishing the other ('difficult') one..

Oatzy.

\* That is the time required for the code snippet at the top. There is a quicker approach - sum along each row, check if they equal 45 [=1+2+..+9].

> <div style="font-family: &quot;Courier New&quot;,Courier,monospace">
>
> <span style="color: orange">for</span> i <span style="color: orange">in</span> <span style="color: purple">range</span>(0,9):
>
> </div>
>
> <div style="font-family: &quot;Courier New&quot;,Courier,monospace">
>
>     sum = 0
>
> </div>
>
> <div style="font-family: &quot;Courier New&quot;,Courier,monospace">
>
>     <span style="color: orange">for</span> j <span style="color: orange">in</span> <span style="color: purple">range</span>(0,9):
>
> </div>
>
> <div style="font-family: &quot;Courier New&quot;,Courier,monospace">
>
>         sum = sum + Grid[i][j]
>
> </div>
>
> <div style="font-family: &quot;Courier New&quot;,Courier,monospace">
>
>     <span style="color: orange">if</span> sum != 45:
>
> </div>
>
> <span style="font-family: &quot;Courier New&quot;,Courier,monospace">       </span><span style="color: orange; font-family: &quot;Courier New&quot;,Courier,monospace">return</span><span style="font-family: &quot;Courier New&quot;,Courier,monospace"></span><span style="color: #274e13; font-family: &quot;Courier New&quot;,Courier,monospace">"incorrect puzzle"</span>

Do the similar for columns and boxes.

The time required for this is ~ *3n^2*. That gives a 9-grid time of *243t*, and a 100-grid time of *30,000t*.
