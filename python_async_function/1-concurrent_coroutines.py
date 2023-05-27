#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio
from typing import List
from random import randint
from asyncio import sleep

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.
    Returns the delay as a float.

    Args:
        max_delay: The maximum delay in seconds. Default is 10.

    Returns:
        The delay as a float.
    """
    random_delay = randint(0, max_delay)
    await sleep(random_delay)
    return float(random_delay)

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.
    Returns the list of delays in ascending order without using sort().

    Args:
        n: The number of times to spawn wait_random.
        max_delay: The maximum delay in seconds.

    Returns:
        The list of delays in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        await task
        delays.append(task.result())

    delays.sort()
    return delays

# Test the coroutine
print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
