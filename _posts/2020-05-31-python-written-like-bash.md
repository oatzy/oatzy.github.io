---
layout: post
title: Python Written like Bash
date: '2020-05-31T00:00:00.000-00:00'
author: Chris Oates
tags:
- python
- bash
modified_time: '2019-05-31T00:00:00.000-00:00'
---

The other day a coworker asked me to look at a python script he'd written - make sure there weren't any major issues (*"little ones are ok"* - his words).

One thing that immediately jumped out at me was how it was handling exit-on-error

```python
print >> sys.stderr, "Something went wrong. Exiting..."
sys.exit(1)
```

Aside from the very retro `print >>` syntax, compare with this typical bash snippet

```bash
echo "Something went wrong. Exiting..." >&2
exit 1
```

This is the sort of thing I was talking about to in the earlier [blog post](https://oatzy.github.io/2020/03/25/writing-bash-scripts-like-python.html), about writing code in the style of a language you're more comfortable with.

To be clear, I don't mention this to put my coworker down. The style is... unconventional, to be sure. But the script overall was functionally sound, with no bugs that I could see. So as far as I'm concerned, job's a good'en.

Oh, and in case you were wondering, the pythonic way of doing the exit-on-error would be

```python
sys.exit("Something went wrong. Exiting...")
```

When `sys.exit` is passed a string, it exits with code 1 and prints the message to stderr.


Chris