#!/usr/bin/env python3

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the string and the square of the int/float.

    Args:
        k: The string key.
        v: The int or float value.

    Returns:
        A tuple containing the string key and the square of the int/float value.
    """
    return (k, v ** 2)
