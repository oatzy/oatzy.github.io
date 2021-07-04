---
layout: post
title: Valid User Names, and Making Problems for Co-workers
date: '2021-07-04T14:30:00.000-00:00'
author: Chris Oates
tags:
- coding
- biographical
- unix
modified_time: '2021-07-04T14:53:00.000-00:00'
---

# A wild PR appeared!

The problem went like this - you've given a string specifying a (unix) user. It can have one of three formats

```bash
username/uid
username
uid
```

The string needs to be parsed into a (valid) user id (uid) so that it can be applied (`chown`) to a file.

The implementation in the PR was along these lines (simplified for clarity)

- if '/' in line, split and check that the second part is a valid uid
- else, check if the whole string is a valid uid
- else, check if the whole string is a valid username

Which is a perfectly sensible implementation!

But in my experience, users are anything but sensible.

# What even is a valid user name?

My first thought looking at this PR was - haven't I seen Active Directory (AD) user names containing `/` ? (or was that `\` ?)

My second thoughts was, what if it's a purely numerical username (e.g. `12345`)?

At this point I went to check google/stack overflow. The [answer](https://serverfault.com/questions/73084/what-characters-should-i-use-or-not-use-in-usernames-on-linux) I got was that either user names must match `NAME_REGEX="^[a-z][-a-z0-9]*\$"`, or maybe anything goes?

Let's try it out

```bash
$ useradd 12345

$ useradd evil/12345
```

Oh dear...

Or if I wanted to be truly evil,

```bash
$ useradd evil
$ id evil
uid=1001(evil) gid=1001(evil) groups=1001(evil)

# shadow another user's uid
$ useradd 1001
$ id 1001
uid=1002(1001) gid=1002(1001) groups=1002(1001)

# username which matches the expected string format for a valid user
$ useradd evil/1001
$ id evil/1001
uid=1003(evil/1001) gid=1003(evil/1001) groups=1003(evil/1001)
```

I feel like our QA engineer would be proud of that one.

The user id string we're trying to parse was actually coming from another of our software, so at this point the problem goes up the chain, and now I've ruined two co-worker's days 😬

# Tilting at edge-cases

So is any of this reasonable? Would a user ever even want to create a numerical username?

Well what I've learned in this job is - if something's possible, some user will try to do it.

In our company wiki, we have a "customer path hall of shame" for all the weird and wonderful file paths which have broken our code in one way or another - emoji, non-unicode bytes (latin1?), quotation marks, trailing whitespace(!) They make for excellent test cases.

Having said that, I imagine there's a lot of other software which doesn't support numerical user names (or would misinterpret them as uids).

I actually tried to repeat my test, but unintentionally did `adduser` instead of `useradd`, and got this error

```bash
$ adduser 12345
adduser: Please enter a username matching the regular expression configured
via the NAME_REGEX configuration variable.  Use the `--force-badname'
option to relax this check or reconfigure NAME_REGEX.
```

My view is, supporting edge case is good, up to a point. It's a trade-off between how hard it is to support, versus how much not supporting it would upset users (and how many).

User names containing a slash are a bit niche. But what about user names with non-ASCII characters? They don't match the `NAME_REGEX`, but what if your **actual** name contains, e.g. an umlaut (like one of my co-worker's does)?

Chris

[See also, [falsehoods programmers believe about names](https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/)]