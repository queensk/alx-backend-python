#!/usr/bin/env python3
"""
3. Tasks
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes an integer max_delay and returns a asyncio.Task that
    waits for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it.

    Args:
        max_delay (int): Maximum number of seconds to wait for.

    Returns:
        asyncio.Task: A Task that will wait for a random delay and return it.
    """
    return asyncio.create_task(wait_random(max_delay))
