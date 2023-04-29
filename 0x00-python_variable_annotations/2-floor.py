#!/usr/bin/env python3
"""
returns float of float
"""


def floor(n: float) -> int:
    """
    calculates the floor for a n
    """
    if n >= 0:
        return int(n - (n % 1))
    else:
        return int(n - (1 - (n % 1)))
