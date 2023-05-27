#!/usr/bin/env python3
""" Write a coroutine called async_comprehension """
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Collect 10 random number using async_generator and return them """
    result = [i async for i in async_generator()]
    return result
