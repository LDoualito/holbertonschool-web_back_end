#!/usr/bin/env python3

import asyncio
from typing import Task
from random import randint
from time import sleep

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> Task[float]:
    """
    Function that takes an integer max_delay and returns an asyncio.Task.

    Args:
        max_delay: The maximum delay in seconds.

    Returns:
        An asyncio.Task object representing the execution of wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))

async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
