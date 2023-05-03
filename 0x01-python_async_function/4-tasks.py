#!/usr/bin/env python3

"""
Task wait n module
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n: number of times the wait_random method should be called
        max_delay: maximum number of seconds to delay the execution

    Returns:
        A list of delays sorted in ascending order
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    delayed_tasks = [await task for task in asyncio.as_completed(delays)]
    return delayed_tasks
