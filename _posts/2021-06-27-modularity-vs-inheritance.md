---
layout: post
title: Modularity vs Inheritance
date: '2021-06-27T16:32:00.000-00:00'
author: Chris Oates
tags:
- coding
- python
- design
modified_time: '2021-06-27T18:02:00.000-00:00'
---

{% include callout.html type="primary" content="This is a direct follow on to the [Modularity Madness](https://oatzy.github.io/2020/05/25/modularity-madness.html) blog. I actually drafted it shortly after writing that post, but for whatever reason never got around to finishing it at the time."  %}

Further to my previous post, I wanted to talk a bit more about how the `DownloadFn` is used, and why it's defined as a stand-alone function.

The basic idea is we have something generating file 'events', and these events are passed to a 'thing' which does something with those events. This thing, I called `Worker` because, for the life of me, I can't think of a better name.

The worker interface looks like this

```python
class Worker(Protocol):

    def enact(event: Event): ...
```

This is pretty vague. Essentially, an event is passed to the `Worker` and depending on the type of event it will do a different thing.

`Worker` is a class, because it collects together methods for handling different events in a particular way. For example, we might have a POSIX worker, which enacts the events for a POSIX-based target filesystem. Or we might have a 'logging' worker, which simply writes the incoming events to a log file.

Now, I could have defined the interface as something more specific, like

```python
class Workers:

    def enact_create(self, create_event): ...
    def enact_delete(self, delete_event): ...

    def enact(self, event):
        if event.type == EventType.CREATE:
            self.enact_create(event):
        # etc
```

But I didn't want to over-specify the interface.

As a particular example, we can have `MOVE` events and `RENAME` events, but in the context of a POSIX worker, those correspond to the same operation - `mv`

Where the download function comes into play is in the `create` method

Suppose we went with this approach

```python
class Worker:

    def download(self, source, target):
        with source.open() as f:
            target.write_bytest(f.read())
```

Now, as in the previous post, we want to extend the download functionality to do rollback on error. In a 'traditional' object-oriented approach, we might try something with inheritance, like

```python
class RollbackWorker(Worker):

    def download(source, target):
        try:
            super().download(source, target)
        except Exception:
            if target.exists():
                target.unlink()
            raise
```

Not so bad. But then if we want to add download verification...

Things quickly balloon. And the worst part is, we're creating all these subclasses, but we're only change one, auxiliary method - that is, the method we're changing isn't even part of the `Worker` interface.

So instead, what I did was this

```python
class Worker:

    def __init__(self, downloadfn):
        self.downloadfn = downloadfn

    def create(self, event):
        #...
        self.downloadfn(source, target)
```

Now, we can drop in any of the bespoke download functions from the previous post, no subclasses required.

We can even drop in a mock one for testing

```python
download = Mock()
worker = Worker(download)

worker.enact(create_event)

download.assert_called_with(...)
```

Not that there's anything wrong with sub-classing, per se. But in this specific case, it made more sense to separate out the bit that can change (the download function) from the central class (Worker).


Chris.