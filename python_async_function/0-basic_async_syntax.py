#!/usr/bin/env python3
""" Write an asynchronous coroutine """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Return random delay between 0 and max_delay """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay