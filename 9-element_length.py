#!/usr/bin/env python3

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the given list.

    Args:
        lst: Iterable containing sequences whose lengths need to be calculated.

    Returns:
        List of tuples, where each tuple contains an element from the input list
        and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
