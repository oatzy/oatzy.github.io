---
layout: post
title: Python-style Logging in Bash
date: '2020-01-08T00:00:00.000-00:00'
author: Chris Oates
tags:
- python
- bash
- logging
modified_time: '2019-01-08T00:00:00.000-00:00'
---

One of the great sins in programming is trying to write code in one language like code from another language.

Having said that, I'm a shell scripting newbie. So when I had cause to write some bash, I found myself reaching for some python 'home comforts'.

Okay, so what I actually did wasn't so bad

```bash
function log() {
    echo "log: $@" >&2
}
```

I think this is a fairly common approach to 'logging' in bash.

But around the same time, I was reading about arrays in bash, and that gave me an idea for how you could implement python-style logging, with variable logging levels.


# Code

```bash
#!/usr/bin/env bash

_LEVELS=(DEBUG INFO WARNING ERROR CRITICAL)

export DEBUG=10
export INFO=20
export WARNING=30
export ERROR=40
export CRITICAL=50


function log() {
    # Write a message to logging at the given level
    #
    # Usage: log <level> <message>

    local effective=${LOGLEVEL:-$WARNING};

    local level=$1;
    local levelname=${_LEVELS[$((level/10-1))]};

    shift;

    if [[ $level -ge $effective ]]; then
        printf "%s:%s: %s\n" "$levelname" "$0" "$@" >&2;
    fi
}

function setLevel() {
    # Set the logging level
    #
    # Usage: setLevel <level>

    export LOGLEVEL=$1
}

# convenience functions
alias debug='log $DEBUG'
alias info='log $INFO'
alias warning='log $WARNING'
alias warn=warning
alias error='log $ERROR'
alias critical='log $CRITICAL'
```

# Example Usage

If you want to make use of this, just save the script somewhere locally and `source` it

```bash
$ source logging.sh

$ setLevel $INFO

$ log $INFO "hello world"
INFO:bash: hello world

$ log $DEBUG "can't see me"

$ setLevel $DEBUG

$ debug "now you see me"
DEBUG:bash: now you see me
```

Better yet, throw your bash script in the trash, and re-write it in python :p


Chris.