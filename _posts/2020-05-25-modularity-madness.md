---
layout: post
title: Modularity Madness
date: '2020-05-25T00:00:00.000-00:00'
author: Chris Oates
tags:
- python
- pragmatic programmer
- modularity
modified_time: '2019-05-25T00:00:00.000-00:00'
---


As mentioned in an earlier blog, I’ve recently been working on a new project at work. It’s not often one gets to write something wholly from scratch.

In this case, I had just read the revised edition of [The Pragmatic Programmer](https://pragprog.com/book/tpp20/the-pragmatic-programmer-20th-anniversary-edition), so I had all sorts of ideas in my head about design and best practices.

So let’s talk about modularity.

# Interfaces

The task at hand is downloading a file.

I defined the download interface as

```python
def downloadfn(source: ByteReadable, target: Path):
    ...
```

We can define a type alias for this (which will come in handy later)

```python
DownloadFn = Callable[[ByteReadable, Path], None]
```

`ByteReadable` is a protocol (interface) I’m using for ‘something’ that can be open to return a `ByteReader`, which is also a protocol for something which can be read, returning bytes.

In other words

```python
class ByteReadable(Protocol):

    def open(self) -> ByteReader:
        ...

class ByteReader(Protocol):

    def read(self, size: int = -1) -> bytes:
        ...
```

As discussed in a previous blog, a [protocol](https://www.python.org/dev/peps/pep-0544/) is an ‘implicit’ interface - anything which implements the protocol methods is considered to implement the protocol (so will pass type checking).

Files support the protocols ‘out of the box’, and [BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO) objects support the `ByteReader` protocol. This is good for unit testing.

But what we’re really interesting in is a class which wraps a [requests streaming response](https://requests.readthedocs.io/en/master/user/advanced/#streaming-requests) for the remote file.

Something like (but not exactly)

```python
class RemoteFile:

    def open(self) -> DownloadStream:
        resp = requests.get(url, stream=True)
        return DownloadStream(resp)


class DownloadStream:

    def read(self, size: int = -1) -> bytes:
        return self.stream.read(size)
```

# Basic Download

So, with our interface defined, the most basic implementation is just this

```python
def simple_download(source: ByteReadable, target: Path):
    with source.open() as f:
        target.write_bytes(f.read())
```

# Chunked Download

The above is all well and good, but if it’s a large file we’re downloading, that’s going to hold a lot of data in RAM.

So instead, we can download in chunks

```python
def chunked_download(source: ByteReadable, target: Path):
    chunk_size = 4 << 20  # 4MiB
    with source.open() as fin:
        with target.open('wb') as fout:
            for chunk in iter(lambda: fin.read(chunk_size), b''):
                fout.write(chunk)
```

But suppose we want to make the ‘chunk size’ configurable - suppose we let users pass a chunk size via a cli flag or whatever.

We can do

```python
def chunked_download(source: ByteReadable, target: Path, *, chunk_size: int = 4<<20):
    with source.open() as fin:
        with target.open('wb') as fout:
            for chunk in iter(lambda: fin.read(chunk_size), b''):
                fout.write(chunk)
```

But now the function signature no longer matches the interface.

Actually, there’s an easy fix for this

```python
from functools import partial

download: DownloadFn = partial(chunked_download, chunk_size=args.chunk_size)
```

We’ve explicitly declares the type as `DownloadFn` because mypy can’t infer it for [partial](https://docs.python.org/3/library/functools.html#partial-objects)

Another option would be to use a wrapper function, but the end result is basically the same

# Rollback on Error

Suppose the download fails - maybe the internet connection drops. In that case, we want to remove the partially downloaded file before raising the error.

For this, we can create a wrapper function

```python
def rollback(downloadfn: DownloadFn) -> DownloadFn:
    def wrapped(source: ByteReadable, target: Path):
        try:
            downloadfn(source, target)
        except Exception:
            if target.exists():
                target.unlink()
            raise
    return wrapped
```

(for simplicity, I’m ignoring the case where target already exists)

The point here, is that the wrapper could be applied to `simple_download` or `chunked_download` or any other function which implements the interface.

We could even use the wrapper as a decorator

```python
@rollback
def download(...): ...
```

But that way, we can’t apply the rollback dynamically (we'll come back to that later).

# Checksum Verification

At this point we,re going to slightly ‘break’ the interface.

See, in my use case, the object I’m passing to the download functions isn’t ‘only’ `ByteReadable`. It contains metadata about the source file, like size. And in particular, we have a sha1 checksum for the file.

So first of all, we’ll create a couple of new protocols

```python
class Checksumable(Protocol):
    checksum: str


class ReadCheckable(ByteReadable, Checksumable):
    ...
```

Now we can write a new wrapper

```python
def verify(downloadfn: DownloadFn) -> DownloadFn:
    def wrapped(source: ReadCheckable, target: Path):
        downloadfn(source, target)
        assert source.checksum == sha1(target.read_bytes()).hexdigest()
    return wrapped
```

(strictly speaking, the return type isn't `DownloadFn`. Also, don't use `assert` in practice, as it might get optimised away)

This is where the common interface really shines - if we put `verify` inside `rollback` then a failed checksum will cause the 'corrupted' download to be removed.

```python
download = rollback(verify(chunked_download))
```

(If we don’t want a checksum fail to trigger a rollback, we can do that by simply swapping the order of wrappers)

## Streaming Checksum

Actually, the above checksum check is quite inefficient; we download the file, then read the whole thing again to calculate the checksum. Wouldn’t it be nice if we could calculate the checksum as we’re downloading.

The common interface actually cuts both ways.

Just as we can do an alternate implementation of `DownloadFn`, we can also do an alternate implementation of the `ByteReadable` that we pass in.

So we can create a wrapper *class* like this

```python
class HashReadable:

    def __init__(self, readable: ByteReadable):
        self.hasher = sha1()
        self.readable = readable
        self.reader: Optional[ByteReader] = None

    def open(self) -> ByteReader:
        self.reader = self.readable.open()
        return self

    def read(self, size: int = -1) -> bytes:
        assert self.reader is not None
        data = self.reader.read(size)
        self.hasher.update(data)
        return data

    def checksum(self):
        return self.hasher.hexdigest()
```
(incidentally, this implements both `ByteReadable`and `ByteReader`)

And for convenience, we can write another wrapper function

```python
def stream_verify(downloadfn: DownloadFn) -> DownloadFn:
    def wrapped(source: ReadCheckable, target: Path):
        verified_source = StreamHasher(source)
        downloadfn(verified_source, target)
        assert verified_source.checksum() == source.checksum
    return wrapped
```

# So what’s the point to all this modularity?

Well for one, it gives us separation of concerns. The function which does the downloading doesn’t need to worry about what happens if there’s an error - that’s handled by a separate function. We can have download verify checksums if available, but we don’t have to modify the download function itself if not.

This makes it easier to construct the download function dynamically, based on user configurations - suppose we want to allow users to disable checksum verification to reduce download overhead

```python
downloadfn = simple_download
if args.verify:
    downloadfn = verify(downloadfn)
downloadfn = rollback(downloadfn)
```

Otherwise, we would have a single function with all the logic mixed together and a bunch of feature flags.

```python
def download(source, target, *, rollback=True, verify=True):
    try:
        with source.open() as f:
            target.write_bytes(f.read())
        if verify:
            assert source.checksum == sha1(target.read_bytes()).hexdigest()
    except Exception:
        if rollback and target.exists():
            target.unlink()
        raise
```

And if we want to add another feature, we have to update this function and add a new flag, until the whole thing turns into a ball of mud.

Modularity is also good for testability. We can test each ‘feature’ independent of the others.

Or suppose we come up with another download method - maybe a multi-part download. As long as it implements the `DownloadFn` interface, we can use the existing `verify` and `rollback` wrappers.

And we could write even more wrappers:
 - preallocate target
 - backup target if it exists
 - progress bar (as another readable wrapper)

(These are left as an exercise for the reader)

So hopefully I’ve convinced you of the power of interfaces, modularity, and composition.

{% include callout.html type="info" content="Follow up: [Modularity vs Inheritance](https://oatzy.github.io/2021/06/27/modularity-vs-inheritance.html)"  %}

Chris

*[it’s interfaces all the way down]*