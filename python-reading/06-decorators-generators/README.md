# Project 06 — Decorators & Generators
**Difficulty: 6 / 10**

These two features are everywhere in modern Python (web frameworks, `dataclasses`,
`asyncio`, ORM models). Reading them well means understanding **what runs when**:
decorators run at definition time; generators pause at `yield` and resume on demand.

Read `decorators_generators.py`, predict each `print`, then run it.

## Concepts exercised
- A decorator is a function that takes a function and returns a function
- `@syntax` is just `func = decorator(func)` applied at definition time
- `functools.wraps` preserves the wrapped function's metadata
- Generators: `yield` suspends, `next()` resumes, raises `StopIteration` when done
- Lazy evaluation and infinite sequences
- `yield from` for delegating to a sub-generator

## Questions (answer before running)
1. The `@log_calls` line — when does the decorator body execute: at `def` or at call?
2. What does `next(gen)` return the first time, and what is `x` after it?
3. Why doesn't `evens()` hang forever? What stops each `next()` call?
4. What does `yield from` do in `chained()`?
5. In `sum(range_gen(4))`, how many times is `yield` executed?

## Interview angle
> "Implement a decorator that times a function" or "Explain what `yield` does."
The crisp answer: `yield` turns a function into a generator; calling it returns an
iterator without running the body; the body runs lazily, pausing at each `yield`.

## Mental model
- **Decorator** = "wrap this function, return a new one, run setup at import time"
- **Generator** = "a function that produces values one at a time, pausing state"
