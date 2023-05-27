#!/usr/bin/env python3

import asyncio
from time import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns total_time / n.

    Args:
        n: The number of times to spawn wait_random.
        max_delay: The maximum delay in seconds.

    Returns:
        The average execution time per wait_random call.
    """
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n

# Test the measure_time function
n = 5
max_delay = 9
print(measure_time(n, max_delay))
