---
layout: post
title: How I Approach Software Design
date: '2021-08-29T18:29:00.000+01:00'
author: Chris Oates
tags:
- coding
- python
- design
modified_time: '2021-08-29T22:28:00.000+01:00'
---

What I wanted to talk about today is my approach to designing a piece of software, by looking at three projects I've worked on [^1]

But before we get to the example, lets lay out the approach

> find the 'core concept'

that is, when you strip it down to the most basic level, ignoring the implementation details, the edge cases, the error handling or whatever, what is the basic mechanism by which information flows from an input to a result. When you find this core concept, it's usually so basic that it feels self-evident, as you will see.

> figure out what changes or may change

for example if you needed to handle a different input, support a different (3rd party) service.

> figure out how those two pieces fit together

That is where the magic happens.

So, lets look at some examples

# Event Sync

This is a project I've alluded to in [previous](https://oatzy.github.io/2020/05/25/modularity-madness.html) [blog posts](https://oatzy.github.io/2021/06/27/modularity-vs-inheritance.html)

We have a cloud storage service. When you perform some action (create a file, delete a file) it generates an event, which we can poll using their API. So what we want to do is sync changes to a local file system by fetching events and performing the corresponding changes (download a file, delete a file).

In terms of core concept, this one perhaps the most obvious - it's [event driven](https://en.wikipedia.org/wiki/Event-driven_architecture). We have an event source and an event consumer.

As for what changes; whenever I'm working on a project which interacts with a 3rd party service, the question in the back of my mind is always - what if we want (or need) to switch out that service for another one? Suppose we want to support a different (or additional) storage service?

So we have the official SDK, which generates Event objects. But those objects are specific to that SDK. With an eye on being able to replace the service, we don't want to deal with those SDK events directly. Instead, we define our own, generic Event type.

```python
@dataclass
class Event:
    type: EventType
    path: Path
    timestamp: datetime
    # etc
```

What this means is, the event consumer doesn't care where the events come from, they look the same in any case [^2]

Similarly, we can switch out the event consumer so that instead of reflecting changes on a file system, it could reflect them on a different storage service (cloud-to-cloud sync). Again, the event source doesn't care what happens to the events it emits.

Another nice things is we can stick some filtering in the middle. As long as the filtering takes in generic Events and spits back out generic Events, neither the source nor the consumer even need to know it exists.

# ACL tool

[Access Control List](https://en.wikipedia.org/wiki/Access-control_list) (ACL) is basically the permissions on a file. If you've deal with linux you'll be familiar with user/group/other read/write/execute. In fact, you can assign permissions to specific users or groups using e.g. [setfacl](https://linux.die.net/man/1/setfacl).

So we wanted a tool like `setfacl` but for a different file system type (one which `setfacl` doesn't work on) - a tool for adding or removing permissions for a given user or group.

The basic concept here was

1. get the current ACL
2. perform some transformation on the ACL
3. put the updated ACL back on the file

Step (2) is an obvious thing that changes - this is where we add or remove entries from the ACL.

But we can also make changes to (1) and (3)

For example, instead of reading the ACL from the file, in (1) we can read it from the command line (or stdin), allowing us to copy the ACL off of another file.

Similarly, instead of writing the updated ACL to the file, in (3) we can print the updated ACL (to stdout). This gives us 'dry run'/test mode functionality.

```python

if args.test:
    putacl = print_acl
else:
    putacl = save_acl

def update_acl(path):
    acl = getacl(path)
    acl = updateacl(acl)
    putacl(path, acl)

for path in treewalk(root):
    update_acl(path)
```

# Workflow engine

In this case, I was refactoring some else's code. What is does is send files from one machine to another by uploading to cloud storage from one machine and downloading on the other [^3]. This is orchestrated using [Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html), with the two machines sharing a message queue.

What changes is the cloud storage service used as the intermediate - it may be Google cloud (gcs), Amazon (aws), etc.

The original looked something like this

```python
def send(provider_type, files):
    if provider_type == 'gcs':
        wf = chain(
            upload_to_gcs.s().set(queue='local'),
            download_from_gcs.s().set(queue='remote')
        )

    elif provider_type == 'aws':
        # basically the same thing but with aws tasks
    # etc

    res = wf.apply_async((files,))
    res.get()
```

A big switch-alike statement like this is definitely a code smell

One solution to this might be to define separate `send_via_gcs`, `send_via_aws`, etc. tasks. But another thing that changes is the workflow itself - that is, we want to support additional workflows, such as download-only for a file which is already in the cloud, or to delete files from a remote machine. Separate workflow functions for each provider [doesn't scale well](https://en.wikipedia.org/wiki/Combinatorial_explosion).

So the core concept here was building up a workflow (chain) of these tasks. The thing that changes is what cloud provider the tasks interact with. Traditionally, we might do something like this with classes and [polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)), but that doesn't really work for celery tasks... or does it?

Consider

```python
class GCSProvider:

    def upload(self):
        return upload_to_gcs.s()

    def download(self):
        return download_from_gcs.s()


def send(provider, files):
    wf = chain(
        provider.upload().set(queue='local'),
        provider.download().set(queue='remote')
    )

    res = wf.apply_async((files,))
    res.get()
```

For extensibility, a new provider just needs to implement the `Provider` interface, or we might adds new tasks (methods) to the interface. And as long as the interface is consistent across all providers we can (and did) define new workflows which will work with any of the providers.

# Conclusion

So that's all there is to it - what's the core concept, what's changeable?

Once you have that down, everything else is just building out - adding flesh to the bones.

This approach perhaps doesn't apply in all cases. In some cases, it may already be laid out for you (e.g. Django). But if you're starting on a brand new project with no existing framework, these are good questions to keep in mind.

Chris.

## Footnotes

[^1]: these are work projects, so I have to be vague on some of the details.
[^2]: this is also good for testing, since we can test the source and consumer independently
[^3]: it's a little more nuanced than that, but again, NDA