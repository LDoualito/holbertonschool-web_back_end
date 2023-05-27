#!/usr/bin/env python3
""" Write a new function task_wait_n """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Create a sorted list with delay """
    tasks = []
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    list = [await task for task in asyncio.as_completed(tasks)]
    return list