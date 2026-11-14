---
layout: post
title: The Twitter Virus
date: '2010-09-21T14:47:00Z'
author: Oatzy
tags:
- programming
- javascript
- worm
- exploit
- twitter
- tweets
- viruses
modified_time: '2010-09-21T16:01:44.882-07:00'
thumbnail: /images/twitter-virus/Moar-Twit-Virus.png
blogger_id: tag:blogger.com,1999:blog-14769935.post-1512711795451847852
blogger_orig_url: https://oatzy.blogspot.com/2010/09/twitter-virus.html
---

**Background**

So here's what's happened - Twitter has been '[hacked](http://mashable.com/2010/09/21/twitter-mouseover-bug/)'. Now personally, I don't like such ambiguous use of the word hacked, since it tends to imply that some sort of infiltration or breaking in has taken place. But that's just me.

No. What actually happened is that someone discovered that URLs can be posted that include JavaScript (and in particular the "*onMouseOver*" function), which was executed when you hovered over said link. Then the *Script Kiddies* got their hands on it, and all hell broke loose

This is an example of '*code injection*' or '[*cross-site scripting*](http://en.wikipedia.org/wiki/Cross_site_scripting)'- that is, code can be posted to a website - be it by a comment, a status update or whatever - and the site will execute it as if it were part of the site's own code.

For most sites, it's not possible, because comments, etc. are 'sanitised' so that code like this is removed or just displayed as plain-text, so it can't be executed. For example, on [*Den of Geek*](http://www.denofgeek.com/) they strip away all HTML tags from comments, which has the drawback of disallowing formatting, but gets the job done. But these things can slip through the net from time to time.

One other recent example was [on YouTube](http://arstechnica.com/tech-policy/news/2010/07/pranksters-have-a-field-day-with-youtube-injection-flaw.ars). YouTube would normally validate it's code by stripping away the "\<script\>" tag which *should* have prevented the problem. Except, someone realised that if you start the comment with "\<script\>\<script\>", only the first tag is stripped away, so the code is still executed.

And this was used to cause all sorts of havoc - redirecting people to porn sites, or adding banners and pop-ups to videos (mostly on Justin Bieber videos), and so on.

In YouTube's case it took about an hour to spot the problem and two more to fix it (apparently). And apparently Twitter has been fixed now (approx. 2hours later). So kudos to them.

**The Code**

What's interesting about this is how involuntary activating it can be. All you have to do is hover over the link to execute it. Which, to be fair, is both simple and elegant (regardless of how inelegant the code itself looks).

The general form looks like this:

> *[some URL]/@"onmouseover="[some javascript]*

In it's simplest form, the code might be something like this (via [Sophos.com](http://www.sophos.com/blogs/gc/g/2010/09/21/twitter-onmouseover-security-flaw-widely-exploited/)):

[![](http://www.sophos.com/images/blogs/gc/2010/09/onmouseover-popup.jpg)](http://www.sophos.com/images/blogs/gc/2010/09/onmouseover-popup.jpg)

Which only uses the 'alert' function to create an annoying pop-up with some random message.

As for code that will redirect you to some other site, I can't find an example, but one way of doing it might take the general form but add something like:

> *window.location.href = [redirect URL]*

Which is all very straight forward, very annoying and fairly boring. There's probably other havoc you can reek that will temporarily redesign a person's homepage, graffiti it, or whatever.

**The Virus**

Now these are personal favourites - the self-retweeting tweets. Literally a self-replicating Twitter status virus.

Here's some example code:

[![](/images/twitter-virus/Moar-Twit-Virus.png)](/images/twitter-virus/Moar-Twit-Virus.png)

They both basically do the same thing, though the latter does it more elegantly.

The first one finds the 'first text area' - i.e. the status input box - fills it with it's own URL - *this.innerHTML* - hits the update button for you - *('.status-update-form').submit()* - and then darkens the screen with *modal-overlay* which means that the page itself is unreachable (without reloading) and clicking anywhere reactivate the exploit.

[![](/images/twitter-virus/overlay.jpg)](/images/twitter-virus/overlay.jpg)

 [Yeah, I wanted to see what it did :p]

For the second one, it gets the element with the tag Id="status". Here's a section of Twitter source code:

[![](/images/twitter-virus/Source-Code.png)](/images/twitter-virus/Source-Code.png)

So that would be the status input box as with the first example. It's just a nicer way of going about it, in my opinion. But anyway.

And in this case, rather than just straight copying itself, it actually RTs the named user's last tweet (usually the code itself), which again is a nicer way of doing it. And it gives the original poster the credit they deserve (albeit with the potential risk of having their account suspended).

Video of the exploit in action [here](http://gizmodo.com/5643732/the-twitter-website-is-under-attack).

Another variant blacks out the actual status, like so:

[![](/images/twitter-virus/Twit-Blackout.png)](/images/twitter-virus/Twit-Blackout.png)

And what that means is (a) you don't know what's going on under there, and (b) your curiosity is more likely to get the better of you.

The code is the same as the first of the above, except instead of the the *modal-overlay* you have *"style="color:#000;background:#000;* - basically, 'make the status black text on black background'.

**One Last Thing**

Obviously, the exploit wasn't limited to "onMouseOver". Any JavaScript could've been used (so long as it was 140 characters or less). But nonetheless, the code would need a trigger, and mouseover was one of the best ways of doing it. Others apparently managed to make it activate by moving the cursor anywhere on screen. So yeah.

Personally I'd be interested to see how far this spread. And indeed, given the 'contagiousness' of it, it'd be quite useful for modelling how this - and indeed everything else - spread through Twitter (as I've [previously](http://oatzy.blogspot.com/2010/09/social-viruses.html) [talked about](http://oatzy.blogspot.com/2010/09/spread-through-network.html)).

Again, a great part of this was the celebs and the connectors; including an early victim, Sarah Brown (Gordon's wife), who has over 1mil followers. And as I said, passing it on isn't as voluntary as RTing.

Why should we have been worried? Imagine the blackout version of the above, but with an added redirect to some malicious site. Yeah. Not that that should be a problem anymore.

I was going to say, if you want to have a play, learn a little JavaScript and have a go. But I guess you can't now. Shame.

Wonder if anyone's tried XSS on Facebook yet..\.

*<strong>[Update]</strong>*

The exploit has definitely been [nullified](http://twitter.com/delbius/status/25120366027). Twitter explain what happened [here](http://blog.twitter.com/2010/09/all-about-onmouseover-incident.html).

One of the [discoverers](http://twitter.com/zzap/status/25105107613) of the exploit seems to be @[Zzap](http://twitter.com/zzap) [[source](http://news.netcraft.com/archives/2010/09/21/twitter-users-fall-victim-to-new-xss-worm.html)], who had no malicious intent for it. More curiosity. And he, himself, was inspired by the now suspended "RainbowTwtr" - screenshot of how they used it [here](http://news.netcraft.com/wp-content/uploads/2010/09/web-rainbow.png).

[This guy](http://www.securelist.com/en/blog/2297/Live_Twitter_XSS) from Kaspersky gives a brief analysis, including a graph of the exploit's growth over time (reaching 93 tweets per second at it's peak). [ThreatPost](http://threatpost.com/en_us/blogs/twitter-closes-web-hole-after-attack-hits-500000-092110) also has some analysis.

The exploitative tweets themselves don't seem to have been deleted by Twitter, but mouseover now does nothing (other than what a link is mean to do).

Anyway. As you were..

Oatzy.

[I'll be honest, I'm not an expert of any sort on JavaScript. But I know enough to get by.]
