---
layout: post
title: Writing Python like Rust
date: '2020-05-10T00:00:00.000-00:00'
author: Chris Oates
tags:
- python
- rust
- go
- golang
modified_time: '2019-05-10T00:00:00.000-00:00'
---
_Or, how I learned to stop worrying and love the type annotations._

Listen, I didn't plan on making a whole _'writing X like Y'_ series. But here we are.


I've recently been working on a new project at work - my first project in pure Python 3. Meaning, I get to play with all the new toys!

And as I was writing this code, it struck me that was borrowing a lot of tricks from Rust (and a little Go).


# Types

One thing I've really gotten into in Python 3 is [type annotations](https://www.python.org/dev/peps/pep-0484/).

The format is quite like Rust

```python
def repeat(text: str, number: int) -> str: ...
```

```rust
fn repeat(text: &str, number: usize) -> &str {...}
```
_(casually ignoring lifetimes)_

Unlike in a strongly typed language, the python type annotations aren't enforced. You run a static checker like [mypy](http://mypy-lang.org/), which is kind of like a compile-time check. But there's no guarantee when the code is run, that the type annotations will be respected (by external code).

Still, I've found that type checking has caught some potentially dumb bugs. In particular, it's good at catching `Optional`s, where I haven't checked/dealt with the case where the value might be `None`. That's one thing I could get sloppy about in python 2 (_"it probably won't be None in practice"_)

# Structs

Rust and Go (and C) don't have objects, in the traditional sense. Instead, they have structs.

Structs are basically containers for a collection of values.

The biggest roadblock to doing something like structs in python was all the boilerplate. Bu this has been greatly simplified by introduction of [dataclasses](https://docs.python.org/3/library/dataclasses.html)

Dataclasses were officially added in python 3.7, but is available in earlier version via a [backport](https://pypi.org/project/dataclasses/). There's also [attrs](https://pypi.org/project/attrs/), which does basically the same thing.

Much like structs in Rust and Go, you declare your dataclass with its fields and the types of those fields

```python
@dataclass
class Event:
    id: str
    type: EventType
    timestamp: datetime
    user: str
```

All the other stuff like the `__init__` method, getters, setters, string formatter, etc. are generated for you.

Of course, one advantage Python has over Rust in this case is being able to give fields default values.

# Traits/Interfaces

Traits and interfaces define behaviours. The python equivalent is [Protocols](https://www.python.org/dev/peps/pep-0544/).

These were officially introduced in python 3.8, so for earlier versions you'll need the [typing_extensions](https://pypi.org/project/typing-extensions/) backport.

```python
class Reader(Protocol):

    def read(self, size: int = -1) -> str: ...


def print_contents(r: Reader):
    print(r.read())


with open('example.txt', 'r') as f:
    print_contents(f)
```

In the above, the open file instance doesn't explicitly sub-class the `Reader` class, but because it implements a `read` method which matches the protocol, it passes type checking.

In this sense, Protocols are more like Go than Rust. In Rust, you have to explicitly `impl Trait for Struct`, where as in python and Go it's implicit.


# Errors and Results

What I like about the Rust (and to a lesser extent, Go) approach to error handling is, you know up front if and what errors a function might return. And additionally, the compiler forces you to at least consider how you're going to deal with it.

By comparison, the python approach to dealing with exceptions is quite chunky

```python
try:
    function()
except SomeException:
    # etc
```
I think this, in fact, encourages just letting exceptions bubble up, rather than fussing about with handling them.

(Of course, if you're the sort of person who deals with errors in rust by just slapping `?` on anything that might fail, then you're more or less just doing exceptions)

There is a 3rd party library - [returns](https://github.com/dry-python/returns) - that lets you do Rust-style `Result` types. But that approach is quite 'unpythonic'.

In spite of the topic of this blog, I think you should always aim to write code which is idiomatic to the language you're using. If only so it's accessible to whoever has to maintain your code after you're gone.

# Odds and Ends

- Python 3.4 introduces [enums](https://docs.python.org/3/library/enum.html) into the standard library. But these only support primitive types (ints, strings) - sort of like C or Java.

One thing I miss from Rust is its 'richer' [enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html), and pattern matching - what the functional programmers would call [sum types](https://en.wikipedia.org/wiki/Tagged_union)

I did find a 3rd party library for [sumtypes](https://pypi.org/project/sumtypes/). I'm on the fence about whether this is pythonic. Also, I'd like to see a version using `dataclasses`, rather than `attrs`

- [pathlib](https://docs.python.org/3/library/pathlib.html) is a revelation. Way more pleasant than working with strings and `os.path`. And functionally, it's quite similar to rust [Path](https://doc.rust-lang.org/std/path/struct.Path.html)

- Rust does [iterators](https://doc.rust-lang.org/std/iter/trait.Iterator.html) as chains, e.g.

```rust
numbers.iter().filter(|x| x % 2 == 0).map(|x| x + 1).sum()
```

And there are 3rd party libraries, like [iterchain](https://iterchain.readthedocs.io/en/latest/) that will let you do the same sort of thing in python. But again, this isn't really 'pythonic'; the 'most' idiomatic way would be with list comprehension

```python
sum(x + 1 for x in numbers if x % 2 == 0)
```

# Conclusion

At this point, you're maybe wondering why we didn't just write the project in Rust?

Maybe if the python version goes down well, we'll get an opportunity to, as the kids say, 'rewrite it in rust'.

Chris

_[By the transitive property, can we write bash scripts like rust..?]_