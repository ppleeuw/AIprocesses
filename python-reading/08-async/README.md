# Project 08 — Async / Await & Concurrency
**Difficulty: 8 / 10**

`asyncio` is the part of modern Python most people can *write* a toy example of
but struggle to **read** in real code. The keys: calling an `async def` does NOT
run it (it returns a coroutine); `await` is the actual handoff to the event loop;
and `async with`/`async for` are the async versions of the `with`/`for` protocols.

Read `async_code.py`, predict each `print`, then run it.

## Concepts exercised
- `async def` defines a **coroutine function**; calling it returns a coroutine
- `await` yields control to the event loop until the awaited task is done
- `asyncio.gather` runs coroutines **concurrently** (not in parallel)
- `async with` (async context manager) and `async for` (async iterator)
- The difference between concurrency (interleaving) and parallelism

## Questions (answer before running)
1. What does `fetch(1)` return if you call it WITHOUT `await`? Why is it not `1`?
2. With `gather`, do the two fetches run sequentially or concurrently? What's the total wall time?
3. In `AsyncTimer`, what do `__aenter__` and `__aexit__` correspond to in the sync world?
4. `AsyncRange` defines `__aiter__` and `__anext__`. What makes them "async"?
5. Why does `await asyncio.sleep(0)` matter — what does it let the loop do?

## Interview angle
> "What's the difference between threading and asyncio?"
Crisp answer: asyncio is **concurrent** on a single thread (cooperative, one task
at a time but many in flight via `await`); threading is **preemptive** parallelism
with the GIL. `await` is the only place control returns to the loop.

## The one-line rule
> Calling `foo()` where `foo` is `async def` does **nothing** until you `await` it
> (or schedule it). It returns a coroutine object, not the result.
