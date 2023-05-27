#!/usr/bin/env python3

import asyncio
from typing import List
from random import randint
from time import sleep

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random n times with the specified max_delay.
    Returns the list of delays in ascending order without using sort().

    Args:
        n: The number of times to spawn task_wait_random.
        max_delay: The maximum delay in seconds.

    Returns:
        The list of delays in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(task_wait_random(max_delay))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    delays.sort()
    return delays

# Test the function
n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
