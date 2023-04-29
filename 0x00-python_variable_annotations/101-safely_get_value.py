#!/usr/bin/env python3
"""
More involved type annotations
"""
from typing import Sequence, Any, Union, Mapping, TypeVar, Optional


T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, T], key: Any,
        default: Optional[T] = None) -> Union[T, None]:
    """
    More involved type annotations
    """
    if key in dct:
        return dct[key]
    else:
        return default
