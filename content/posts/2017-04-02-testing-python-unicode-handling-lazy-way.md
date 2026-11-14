---
layout: post
title: Testing Python Unicode Handling the Lazy Way
date: '2017-04-02T18:22:00Z'
author: Oatzy
tags:
- unittest
- testing
- programming
- python
- problem solving
- coding
modified_time: '2017-04-02T11:25:45.782-07:00'
blogger_id: tag:blogger.com,1999:blog-14769935.post-4864588153713212359
blogger_orig_url: https://oatzy.blogspot.com/2017/04/testing-python-unicode-handling-lazy-way.html
---

**Background**

At work, we've been working on a [Python API](http://arcapix.com/gpfsapi/) for IBM's [Spectrum Scale](http://www-03.ibm.com/systems/uk/storage/spectrum/scale/) (GPFS) filesystem.

The API is well tested, with good coverage. But one thing that's caught us out a couple of times is unicode.

For those not familiar, Python 2.7 has both byte strings and unicode strings. In most cases, the two are interchangeable. But there are some quirks, which can lead to bugs if not handled correctly.

Now it's usually safe to assume that users will work with byte strings - mostly because when you create a string, that is the default format. And internally, we always use byte strings.

But this being an API, it gets used by other people. And what I've come to learn is users do all sorts of weird things. The amount of bugs we've had from frankly bizarre filenames..\. (why would anyone put a newline character it a file name?!)

And users aside, unicode can also come from interfacing with other code - for example, the <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">json.loads</span> method.

All of which is to say, realistically, it's best not to ignore unicode.

**Unittesting**

Listen, I understand the value and importance of [unittesting](https://en.wikipedia.org/wiki/Unit_testing). I just find it so dull compared to writing 'proper' code. And frustrating! In my experience, most of the errors and fails raised by unittests come from the tests themselves, rather than the code they're supported to be testing. (Maybe that's on me).

So yeah. The thought of having to write a whole bunch of new unittests - most of which were going to be more or less exact copies of the tests that already existed - didn't appeal to me.

Instead, I wondered if maybe there was a lazier way of doing it.

The easiest way to do that was to take advantage of the tests that we'd already written. All we needed was a way to run those tests with some mechanism for convert any strings passed to API function calls to unicode.

**Set Trace**

One thing I particularly like about Python is the ability to monkey patch things - playing with existing code on the fly, without having to change the actual source code.

That's why the <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">sys.settrace</span> function is one of my favourites.

I came across set trace when I was looking at ways to do logging in the API. We wanted to be able to log function calls, functions returns, etc. The problem was, we didn't really want to add individual logging statements to each and every function. Aside from the effort, it'd really clutter the code.

After considering a couple other options (decorators, metaclasses), I came across settrace.

[settrace](https://docs.python.org/2/library/sys.html#sys.settrace) isn't well explained in the official docs. You can find a better explanation [here](https://pymotw.com/2/sys/tracing.html#sys-tracing).

settrace allows you to set a trace function - a function which will be called for every line of code run, for every function call and return, for every exception - perfect!

A trace function receives 3 arguments - <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">event</span>, <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">frame</span>, and <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">args</span>.

<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">event</span> is a string indicating what the code is doing (line, call, return).

<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">args</span> is some arguments, which vary depending on the event - for example, if <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">event</span> is <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">'return'</span>, then <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">args</span> will hold the function return value.

And <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">frame</span> is a [frame](https://docs.python.org/2/library/inspect.html) object. This is where we get most of our information for reporting.

The frame object holds some interesting stuff - the <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">f_locals</span> attribute holds the frame locals<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">,</span> and in the case of a call event, these locals are any variables that have been passed into the function.

There's also <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">f_code</span> - the code object for the function being called. And from that we can get things like <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">f_code.co_name</span> - the name of the function being called/returned from.

So as a simple example we might have

``` python
import sys

def trace(frame, event, args):
    if event == "call":
        print frame.f_code.co_name, "called with", frame.f_locals
    elif event == "return":
        print frame.f_code.co_name, "returned", args
    return trace

sys.settrace(trace)
```

I ended up using <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">settrace</span> to write an '[strace](https://en.wikipedia.org/wiki/Strace)' style script, which can be used to trace API function calls for a given script or piece of code. Which is pretty cool.

**The Solution**

So how does this apply to the unicode problem?

As mentioned above, we can get the parameters passed to the function from <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">frame.f_locals</span>. And because <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">f_locals</span> is a dict, it's mutable. That means that we can change it's values, and those changes will persist when the function being traced continues executing.

This is how this solution works - we convert any strings in <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">f_locals</span> to unicode. The code being 'traced' then behaves as if its functions had been passed unicode to begin with.

While we're at it, we have to make sure we also convert any strings in lists, tuples, dicts - in particular because <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">\*args</span> and <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">\*\*kwargs</span> are ultimately just a tuple and a dict.

<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">H</span>ere's the complete solution

``` python
"""Unittest wrapper, which converts strings to unicode.

Check that your code can handle unicode input
without having to write new unittests.

Usage is identical to unittest:

$ python -m unicodetest tests.unit.test_whatever
"""
import atexit
import sys

# mimic the behaviour of unittest/__main__.py
from unittest.main import main, TestProgram, USAGE_AS_MAIN
TestProgram.USAGE = USAGE_AS_MAIN


def unicodify(value):
    """Convert strings to unicode.

    If value is a collection, its members
    will be recursively unicodified.
    """
    if isinstance(value, str):
        return unicode(value)
    if type(value) is dict:
        return {k: unicodify(v) for k, v in value.iteritems()}
    if type(value) in (list, tuple, set):
        return type(value)(unicodify(v) for v in value)
    return value


def unicoder(frame, event, args):
    """For all function calls, convert any string args to unicode."""
    if event == "call":
        for k, v in frame.f_locals.iteritems():
            frame.f_locals[k] = unicodify(v)
    return unicoder


if __name__ == '__main__':
    # make sure unicoder is disabled at exit
    atexit.register(lambda: sys.settrace(None))

    # activate unicoder
    sys.settrace(unicoder)

    # run unittests
    # cli args are passed thru to unittest
    # so the usage is identical
    sys.argv[0] = "python -m unicodetest"
    main(module=None)
```

I decided mimic the <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">unicode/\_\_main\_\_.py</span> script, so that it works as a drop-in replacement for the Python [unittest](https://docs.python.org/2/library/unittest.html) module - e.g.

<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">\$ python -m unicodetest discover -v tests/</span>

This sets the trace to the unicoder function, then calls the usual unittest method to run whatever tests we have pre-written.

**Dummy Test**

``` python
$ cat test_dummy.py

from unittest import TestCase

def dummy(value):
    return value

class Test_Type(TestCase):

    def test_string_type(self):
        self.assertIsInstance(dummy('foo'), unicode)

$ python -m unittest test_dummy

test_string_type (testtype.Test_Type) ... FAIL

======================================================================
FAIL: test_string_type (testtype.Test_Type)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "testtype.py", line 13, in test_string_type
    self.assertIsInstance(dummy('foo'), unicode)
AssertionError: 'foo' is not an instance of <type 'unicode'>

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)

$ python -m unicodetest test_dummy

test_string_type (testtype.Test_Type) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
```

**Comments and Caveats**

In <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">unicodify</span> I've used <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace"> </span>

<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">if type(value) is dict</span>

PEP8 [recommends](https://www.python.org/dev/peps/pep-0008/#programming-recommendations) instead using

<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">if isinstance(value, dict)</span>

But this caused issues for us. In the API, we use <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">OrderedDict</span> as one of the base classes for collection objects. But their init functions doesn't have the same function signature as a dict (ordered or otherwise).

So using <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">isinstance</span> causes things to break. But that's fine - in the case of our collection objects, the members don't need unicodifying anyway. This will, however, miss actual <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">OrderedDict</span>s, so you may wish to change the code accordingly. 

When I first tried the code, I kept getting the following error message

<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">Exception TypeError: "'NoneType' object is not callable" in \<function \_remove at 0x7f4a9aae36e0\> ignored</span>

It wasn't fatal - the code worked in spite of it - but it was a little off-putting. With a little Googling, I found someone with [the same problem](https://github.com/ionelmc/python-hunter/issues/7), and a [corresponding solution](https://github.com/ionelmc/python-hunter/commit/207e8c63ee75cbe4c83c97f32c17c6a67b62a55e#diff-c10b24d69ebd64b6c4e526e9372b0ddaR125).

Basically, the issue was with the trace function not being disabled properly on exit. That's what the [<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">atexit</span>](https://docs.python.org/2/library/atexit.html) line is for.

If the code you're testing is fairly simple, then you can use the code above as is. If it's a bit more complex, you'll probably find that converting strings to unicode in ALL functions causes problems in code outside of your control - in builtin modules, 3rd party modules.

This was the case for our API - the conversion seemed to upset regex (or something).

In this case, we need to make a slight tweak to make it only affect calls to functions from a particular module (the one we're trying to test).

In this case, we use the [<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">insp<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">e</span>ct.getmodule</span>](https://docs.python.org/2/library/inspect.html#inspect.getmodule) method with the frame's <span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">f_code</span> member. That lets us identify what module the function being called came from, and apply unicoding conversion (or not) accordingly.

``` python
module = inspect.getmodule(frame.f_code)
if module and module.__name__.startswith('mymodule'):
    # etc.
```

Now, I'm not a fan of hard-coding a module name into the script. Ideally, I'd probably add a command line flag to specify the module of interest. But parsing that would make the code more complicated, and would break the 'drop-in replacement' nature of the script. So this is left as an exercise for the reader.

**Conclusion**

So<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace">,</span> rather than writing a whole bunch of new tests, I got away with writing only ~50 lines of code. And I didn't even have to change any of the existing code.

Hurray for laziness.

Oatzy.

[inb4 use [Python 3](https://docs.python.org/3/howto/unicode.html#python-s-unicode-support)]
