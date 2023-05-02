#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns list of all delayed async tasks
    """
    delays = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    delayed_tasks = [await delay for delay in asyncio.as_completed(delays)]
    return delayed_tasks
