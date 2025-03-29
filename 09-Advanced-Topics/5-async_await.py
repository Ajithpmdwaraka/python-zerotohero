# Using asyncio for asynchronous programming

import asyncio

async def async_task(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)
    print(f"Task {name} completed")

async def main():
    await asyncio.gather(async_task(1), async_task(2), async_task(3))

asyncio.run(main())
