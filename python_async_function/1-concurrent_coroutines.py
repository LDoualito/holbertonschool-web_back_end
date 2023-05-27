#!/usr/bin/env python3
""" Import wait_random and write a new function wait_n """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Create a sorted list with delay """
    tasks = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    list = [await task for task in asyncio.as_completed(tasks)]
    return list