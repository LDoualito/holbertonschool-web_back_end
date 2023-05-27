#!/usr/bin/env python3

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.

    Args:
        multiplier: The float multiplier.

    Returns:
        A function that takes a float and returns the multiplied result.
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
