---
layout: post
title: Persistent dict with SQLite
date: '2021-07-11T16:48:00.000-00:00'
author: Chris Oates
tags:
- coding
- python
- sqlite
modified_time: '2021-07-11T18:54:00.000-00:00'
---

# SQLite

This is a pattern I've used a couple of times now.

Basically I needed to store some key-value type data — like a dict in python — but it needed to be persistent, so that if the program is stopped and restarted, the data is retrievable.

In particular, I wanted something light-weight and with no extra dependencies. I'm not dealing with a lot of data, so redis would be overkill.

SQLite is ideal for this sort of thing. Even better, Python has a builtin [sqlite3](https://docs.python.org/3/library/sqlite3.html) module.

(I could use [SQLAlchemy](https://www.sqlalchemy.org/), and have on other projects, but again, it would be overkill here).

To take a specific use-case, we have a piece of software which generates reports for multiple 'projects'. Individual project reports can be generated weekly or monthly. We want to keep track of when a report was last generated for each project so that we don't generate more than one in a given report period.

The basic implementation looks something like this

```python
class LastRunSQL:

    def __init__(self, connection: sql.Connection):
        self.connection = connection
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS 'lastrun' "
            "(name TEXT PRIMARY KEY, timestamp TIMESTAMP)"
        )

    def __getitem__(self, name: str) -> datetime:
        item = self.connection.execute(
            "SELECT timestamp FROM 'lastrun' WHERE name=?", (name,)
        ).fetchone()

        if item is None:
            raise KeyError(name)

        return item[0]

    def __setitem__(self, name: str, timestamp: datetime):
        self.connection.execute(
            "REPLACE INTO 'lastrun' VALUES(?,?)", (name, timestamp)
        )
        self.connection.commit()
```

Note - when no matches are found, `sqlite3` will return `None`. So for consistency with python dict behaviour, we have to check the return value and raise a `KeyError` if nothing is found.

Having the table names as a literal, scattered throughout the code, feels a little messy. If it weren't SQL, I'd probably use a variable and string formatting. Perhaps I'm being overly cautious.

# Types and Testing

Once we have an instance of this class, the access pattern looks like

```python
db['foo'] = datetime.now()
print(db['foo'])
```

That is, it works like a regular dict.

This is intentional. The idea is that, for testing, we can just switch out for an actual dict [^1].

Now, we could make this a subclass of `MutableMapping`. But if we look at the definition of [MutableMapping](https://docs.python.org/3/library/collections.abc.html#module-collections.abc), we see that we would need to also implement `__delitem__`, `__iter__`, and `__len__` methods. And while that would be easy enough to do [^2], we simply don't need it here.

So what can we do instead, to satisfy type-checking? [^3]

```python
class LastRun(Protocol):

    def __getitem__(self, name: str) -> datetime: ...
    def __setitem__(self, name: str, timestamp: datetime): ...
```

Using a [Protocol](https://docs.python.org/3/library/typing.html?highlight=protocol#typing.Protocol) [^4] means anything with the `__getitem__` and `__setitem__` methods will satisfy the `LastRun` 'type' - including our `LastRunSQL`, as well as `Dict[str,datetime]`

# Extending the Interface

In another case, I needed to be able to insert a lot of entries at once.

With the implementation above, we can happily do

```python
for key, value in items:
    db[key] = value
```

However, this would be quite inefficient - especially since that implementation does a commit after every insert.

To work around it, I defined another protocol [^5]

```python
@runtime_checkable
class BulkInsertable(Protocol):

    def bulk_insert(self, items: Iterable[Tuple[str, datetime]]): ...
```

And on the SQL class, added an implementation like

```python
def bulk_insert(self, items: Iterable[Tuple[str, datetime]]):
    """Insert many items into the mapping.

    Unlike ``__setitem__`` it uses INSERT instead of REPLACE.
    Therefore, the mapping should be empty or the items should not
    already exist, or else a 'unique constraint' error may be raised
    """
    self.connection.executemany(
        "INSERT INTO 'lastrun' VALUES(?,?)", items
    )
    self.connection.commit()
```

Then in the code which did the mass insert, I have

```python
if isinstance(db, BulkInsertable):
    db.bulk_insert(items)
else:
    for key, value in items:
        db[key] = value
```

Alternatively, this could be done as a baseclass or [mixin](https://en.wikipedia.org/wiki/Mixin), where the iterative method is the default implementation. The reason I did it as a protocol was, again, so I could drop in a regular dict without having to change anything.

# Connections

Firstly, I should note that, for the datetime to [work properly](https://docs.python.org/3/library/sqlite3.html#default-adapters-and-converters), we need to open the connection with `detect_types=sql.PARSE_DECLTYPES`

For one project, I just kept things as above - passing the database connection into the class init - because I was using the same database for multiple things (multiple tables).

But in this case, we were only using the database in one place, so I added a little helper [^6]

```python
class LastRunSQL:

    # ...

    @classmethod
    @contextmanager
    def open(cls, path) -> Iterator["LastRunSQL"]:
        with sqlite3.connect(
            path, detect_types=sql.PARSE_DECLTYPES
        ) as conn:
            yield cls(conn)


with LastRunSQL.open('example.db') as db:
    # do a thing
```

# Alternatives

Finally, I should mention that, along similar lines there is the builtin [shelve](https://docs.python.org/3/library/shelve.html) module. Similar to what we've been discussing, it's a persistent dict-like object, but in this case backed by pickling the data. Because of this, shelves support more datatypes than sqlite. It also has the benefit (or limitation, depending on your perspective) that it doesn't have a fixed schema.

On the other hand, the resulting database can't be used outside of python (if that's something you care about). And SQLite3 supports concurrent access.

In any case, the nice thing about the protocol we defined is, we can switch SQLite out for anything else that satisfies the interface - including `shelve`. Or if we needed to scale up, we could use redis after all.

Chris.

---

[^1]: granted, we could also use a `:memory:` sqlite database
[^2]: full implementation of a [SQLite-backed MutableMapping](https://gist.github.com/oatzy/dc605e8280f8c383d39d1d7cdab90948)
[^3]: the ellipsis is valid python. We could also use `pass`
[^4]: for python < 3.8, you'll need to install `typing_extensions`
[^5]: the `@runtime_checkable` decorator is required to make `isinstance` check work
[^6]: the order of the decorators is important
