import time
import random

import asyncio

async def wait(wait_time, callback):
    time.sleep(wait_time)
    callback()

def set_random_timeout(min_time, max_time, callback):
    wait_time = random.randint(min_time, max_time)
    asyncio.run(wait(wait_time, callback))