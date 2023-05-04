# 0x02. Python - Async Comprehension

## Introduction
This project is about learning how to use Python's async comprehension syntax to work with asynchronous data streams. In this project, we will use the async for loop to asynchronously iterate over a stream of data, and use the async with statement to manage resources in an asynchronous context.

## Requirements
- Ubuntu 18.04 LTS
- Python 3.7 or later
- All the files must have #!/usr/bin/env python3 as the shebang
- All the files should be executable
- All the modules should have a documentation python3 -c 'print(__import__("my_module").__doc__)'

## Installation
To use the code in this repository, you need to have Python 3 installed on your computer. If you don't already have it installed, you can download and install it from the official Python website: https://www.python.org/downloads/

## Usage
All files in this repository are meant to be run as standalone scripts. To run a file, simply execute it using Python:

```
$ ./my_file.py
```
## Files

### 0-async_generator.py
A coroutine called `async_generator` that loops 10 times, each time asynchronously waits 1 second, then yields a random number between `0` and `10` using the random module.

### 1-async_comprehension.py
An asynchronous coroutine called `async_comprehension` that uses an async comprehension to return a list of `10` random numbers between `0` and `100` using the `asyncio` and random modules.

### 2-measure_runtime.py
A function called measure_runtime that measures the total execution time for the `async_comprehension` coroutine 4 times and returns the average time using the time and `asyncio` modules.

### 3-tasks.py
An asynchronous coroutine called `task_wait_random(max_delay: int = 10)` that waits for a random delay between 0 and max_delay seconds and returns that value. This file also contains a function called `wait_n(n: int, max_delay: int = 10)` that takes in `2` arguments: `n` and max_delay. The function should return a list of n delayed tasks using the `task_wait_random` coroutine.

### 4-tasks.py
An asynchronous coroutine called `task_wait_n(n: int, max_delay: int = 10)` that calls the wait_n function from` 3-tasks.py `and measures the execution time using the time module.

## Author
Tasos Avgoustidis (https://github.com/queensk)
