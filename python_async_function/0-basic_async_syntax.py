#!/usr/bin/env python3

import asyncio
from typing import Union
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay (inclusive).
    Returns the random delay as a float.

    Args:
        max_delay: The maximum delay in seconds (default = 10).

    Returns:
        The random delay as a float.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

# Test the coroutine
print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
