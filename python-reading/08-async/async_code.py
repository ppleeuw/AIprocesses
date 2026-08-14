"""
Project 08 — Async / Await & Concurrency
Difficulty 8/10

async def returns a coroutine; await is the handoff to the event loop.
"""
import asyncio


# --- async def defines a COROUTINE FUNCTION ------------------------------
# Calling fetch() does NOT run the body — it returns a coroutine object.
# The body only runs when the coroutine is awaited (or scheduled).
async def fetch(item_id):
    await asyncio.sleep(0.1)   # non-blocking: hands control back to the loop
    return item_id


# --- Running the event loop ----------------------------------------------
async def main():
    # await actually drives the coroutine to completion and gives the result.
    result = await fetch(1)
    print(result)              # predict: 1

    # gather() schedules multiple coroutines and runs them CONCURRENTLY.
    # Total wall time ~= max(0.1, 0.1) = 0.1s, NOT 0.1 + 0.1 = 0.2s.
    results = await asyncio.gather(fetch(10), fetch(20))
    print(results)             # predict: [10, 20]


asyncio.run(main())            # entry point: creates the loop and runs main()


# --- async with: the async context manager protocol ----------------------
class AsyncTimer:
    async def __aenter__(self):
        print("async enter")   # like __enter__, but awaitable
        return self

    async def __aexit__(self, *exc):
        print("async exit")


async def use_timer():
    async with AsyncTimer():
        print("inside async with")


asyncio.run(use_timer())
# predict: async enter / inside async with / async exit


# --- async for: the async iterator protocol -------------------------------
class AsyncRange:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __aiter__(self):
        return self            # async iterators also return themselves

    async def __anext__(self):
        if self.i >= self.n:
            raise StopAsyncIteration   # the async stop signal
        await asyncio.sleep(0)  # yield control to the event loop
        self.i += 1
        return self.i - 1


async def consume():
    out = []
    async for x in AsyncRange(3):   # awaits __anext__ each iteration
        out.append(x)
    print(out)                 # predict: [0, 1, 2]


asyncio.run(consume())
