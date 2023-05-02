#!/usr/bin/env python3
"""
Measure the runtime
"""

import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n
import time


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measure the runtime
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
