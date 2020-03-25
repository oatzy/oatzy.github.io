---
layout: post
title: Writing Bash Scripts like Python
date: '2020-03-25T00:00:00.000-00:00'
author: Chris Oates
tags:
- python
- bash
modified_time: '2019-03-25T00:00:00.000-00:00'
---

In the [previous post](https://oatzy.github.io/2020/01/08/python-style-logging-in-bash.html), I talked about implementing python-like logging in bash.

In that post, I said that it's generally a bad idea to write code in one language as if it were another. But for bash, I'm willing to make an exception.

As I mentioned before, I'm no bash expert. I generally try to avoid it. But there are times when bash really is "the right tool for the job". So in this post, I'm going to talk about how I approach writing bash scripts, and what I bring over from python.


# Functions

Firstly, while it's not necessary to declare functions with the `function` keyword, I like to do it anyway for clarity. It's especially helpful with syntax highlighting

```bash
hello() {
    # do stuff
}

function hello() {
    # do stuff
}
```

Per the usual advice, I aim for small functions that do one thing.

In generally, I would say that any pipeline or non-trivial usage of an external tool should be wrapped as a function with a description name.

For example, suppose I have a csv file with file names and sizes (and possibly some other metadata) and I want to get a list of paths sorted from largest to smallest, I might do

```bash
function paths_by_size() {
    sort "$1" -rn -d, -k2 | cut -d, -f1
}

function main() {
    for path in $(paths_by_size "metadata.csv"); do
        # stuff
    done
}
```

You could even go a step further and split `paths_by_size` into a 'sort by second field' function and a 'get first field' function

# Parameters

It can help to give function parameters names, especially when the function receives more than one

Variables declared in functions should be marked as `local` to avoid 'leakage'

```bash
function add() {
    local x=$1
    local y=$2
    echo $(($x + $y))
}
```

## Default Parameters

Bash has a syntax for setting default values for un-set parameters

```bash
function hello() {
    local name=${1:-world}
    echo "hello $name!"
}
```

## Variadic Arguments

That is, a function parameter that can capture multiple values. In python, we'd use `*args`

In bash, you can capture all function arguments with `$@` or `$*` (depending on whether you care about [splitting on whitespace](https://unix.stackexchange.com/a/129077))

If you want some positional arguments as well, then you can use `shift`

```bash
function log() {
    local level=$1
    shift
    local message="$@"
    # etc
}

log $INFO hello world
# INFO:hello world
```

# Modules

In python, we have this construct `if __name__ == '__main__'`. For those unfamiliar, the check is saying "is this file being run as a script". If False, then the file is being imported as a module.

This is important, because when we're importing the file as module, we don't want it to 'execute' anything, we just want access to its function, classes, etc.

I did some googling, and it turn out there is an equivalent construct in bash

```bash
function main() {
    # do stuff
}

if ! (return 0 2>/dev/null); then
    main $@
fi
```

If we try `return 0` in the shell we get an explanation of why it works

```console
$ return 0
bash: return: can only `return' from a function or sourced script
```

In other words, if `return 0` fails, then we're **not** in a sourced (imported) script.

As with the python version, this allows us to `source` (import) the script into other scripts for re-use or testing or whatever

```bash
source logging.sh

log $ERROR oops
```

As an additional point, if you use script options like `set -eo pipefail`, it's a good idea to put them inside the if. Another script sourcing it might not expect (or want) those options being set.

# Returns and Errors

Bash has the `return` keyword for returning an integer return code

```bash
function doit() {
    return 1
}
```

This can be used to indicate if the function encountered an error - a return value of zero means success, a non-zero value means an error. The specific non-zero value can be used to indicate a specific error.

We can check whether a function returned non-zero with a simple if

```bash
if doit; then
    # success
fi

if ! doit; then
    # failure
fi
```

If we want to check the specific return code, we can use `$?` - e.g. `if [ $? -eq 2 ]; then ...`

Additionally, a function can 'return' some value via stdout - for example

```bash
function hello() {
    echo "hello $1!"
}

function main() {
    msg=$(hello "world")
    echo "$msg
}
```

And we can combine the two types of return for a sort of error handling

```bash
function divide() {
    if [ $2 -eq 0 ]; then
        echo "ERROR: zero division"
        return 1
    else
        echo $(($1/$2))
    fi
}

function main() {
    if ! res=$(divide $x $y); then
        echo "$res" >&2
        exit 1
    else
        echo "$res"
    fi
}
```

In fact, this is more similar to how Go does error handling

```go
if value, err := divide(x, y); err != nil {
    panic(err);
} else {
    fmt.Println(value);
}
```

If I were to compare it to python, I would say it's most like doing the function call in a try-except

```python
try:
    value = divide(x, y)
except Exception as e:
    sys.exit(str(e))
else:
    print(value)
```


# Odds and Ends

The following are just some general ideas

- per python convention (amongst others), global variables should be uppercase, and local variables should be lowercase
- in general, avoid global variables unless they are constants; definitely don't mutate global variables
- don't use `exit` outside of `main`. If another script tries to import (source) and use a function that calls `exit` then that script is going to exit unexpectedly
- since bash function signatures don't declare arguments, it's a good idea to put them in a comment/docstring
- run your bash scripts through something like [shellcheck](https://www.shellcheck.net/) to pickup potential issues
- check dependencies - if you want to use a particular shell command, make sure it exists/is installed with something like

```bash
function require() {
    hash "$1" || exit 127
}

require jq
```

# Putting it Together

To round it all out, I'm going to show an example of a complete python script and its (nearest) equivalent in bash.

The scripts use the github API to get the real name for a given username

```python
#!/usr/bin/env python

import logging
import sys

import requests

GITHUB_URL = "https://api.github.com/users/"


def get_name(username):
    url = GITHUB_URL + username
    logging.info("fetching %s", url)

    resp = requests.get(url)

    if resp.ok:
        return resp.json()['name']

    raise Exception(resp.text)


def main(username):
    try:
        name = get_name(username)
    except Exception:
        logging.critical("couldn't fetch name for %s", username)
        sys.exit(1)
    else:
        print(name)


if __name__ == '__main__':
    main(sys.argv[1])
```

```bash
#!/usr/bin/env bash

source "logging.sh"
source "require.sh"

require jq

GITHUB_URL="https://api.github.com/users/"


function get_name() {
    local url="$GITHUB_URL$1"
    log $INFO "fetching $url"

    curl -s "$url" | jq -er .name
}


function main() {
    local username="$1"
    if ! name=$(get_name "$username"); then
        log $CRITICAL "couldn't get name for $username"
        exit 1
    else
        echo "$name"
    fi
}


if ! (return 0 2>/dev/null); then
    main "$1"
fi
```

Like I said, I'm no bash expert, so I'm not going to claim these are 'best practices'. They might not even be good practices.

But this blog doesn't have a comments section, so you can't tell me otherwise ;)


Chris.


_[Sometimes I write bash just to wind up my bash-phobic colleague]_