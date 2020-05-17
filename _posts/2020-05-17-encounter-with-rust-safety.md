---
layout: post
title: An Encounter with Rust Safety
date: '2020-05-17T00:00:00.000-00:00'
author: Chris Oates
tags:
- rust
modified_time: '2019-05-17T00:00:00.000-00:00'
---

A little while back, I decided to rewrite an old python tools of mine in rust.

This tool uses [torrent api](https://torrentapi.org/apidocs_v2.txt?&app_id=blog_example), an public api for searching torrents.

Now, the torrent api has an aggressive rate limit - it won't allow more than 1 request every 2 seconds. This means we have to actively limit our requests.

The basic workaround goes like this:
- track when the last request was made
- when a new request is made, check if the last one was more than 2 seconds ago
  - if not, sleep until we are able to make a request
- update the last request time

```rust
pub struct TorrentAPI {
    client: Client,  // reqwest client
    token: String,
    last_request: time::Instant,
    rate_limit: time::Duration,
}

impl TorrentAPI {
    fn search(&mut self, query: String) -> Vec<Torrent> {
        if self.last_request.elapsed() < self.rate_limit {
            thread::sleep(self.rate_limit - last);
        }
        *self.last_request = time::Instant::now();

        // ...
    }
}
```

But there's a problem.

See, as I was drafting the rust implementation, I fell for my worst instincts and started too generic, by writing a [trait](https://doc.rust-lang.org/book/ch17-02-trait-objects.html) (on the pretence that I _might_ write some alternative search implementations).

```rust
pub trait TorrentSearch {
    fn search(&self, query: String) -> Vec<Torrent>;
}
```

So we want to implement the `TorrentSearch` trait; that requires that `TorrentAPI` is immutable (`&self`). But since we're updating the last update time, `TorrentAPI` has to be mutable.

The 'simple' solution would have been to re-write the trait to simple accept `&mut self`, or dump the trait completely. After all, I invented the trait, I can do what I like with it.

And yet, doing that 'felt' wrong.

I read an article recently about how different languages '[shepherd](https://nibblestew.blogspot.com/2020/03/its-not-what-programming-languages-do.html)' us towards solving problems in certain ways - for example, perl shepherds you towards using regexes for everything. In this case, rust was forcing me to consider mutability, and shepherding me towards immutability.

At this point, I remembered something I read in the [Write an OS in Rust](https://os.phil-opp.com/) series - if you need a mutable object to implement an immutable trait, use '[interior mutability](https://doc.rust-lang.org/book/ch15-05-interior-mutability.html)'.

Loosely speaking, this means wrapping the mutable thing in a lock

```rust
pub struct TorrentAPI {
    client: Client,
    token: String,
    last_request: Mutex<time::Instant>,
    rate_limit: time::Duration,
}

impl TorrentAPI {
    fn search(&self, query: String) -> Vec<Torrent> {
        {
            let last = self.last_request.lock().unwrap().elapsed();
            if last < self.rate_limit {
                thread::sleep(self.rate_limit - last);
            }
            *self.last_request.lock().unwrap() = time::Instant::now();
        }

        // ...
    }
}
```

Incidentally, one thing I like about this solution is that the lock only wraps the specific bit that can mutate, not the whole struct. And you literally can't touch the wrapped value without locking it first. In python, you could add a lock to the structure, but still forget to use it.

I was reflecting on this solution - why am I using locks, when I'm not writing parallel code?

But I remembered one of the promises of rust is '[fearless concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html)'. And here, I'd been force to write code that _would be_ thread safe - enforced by the compiler. Even if I never need it to be*. By comparison, when I wrote the python version of this tool, I never even considered mutability or thread safety.

Anyway, I think this is what we mean when we say rust is 'safe'. It forces you to consider, and won't allow you to do, things which are potentially unsafe**.


Chris.

*obviously, with the rate limiting, there wouldn't be much merit in paralleling this code

**unless you put them in an `unsafe` block