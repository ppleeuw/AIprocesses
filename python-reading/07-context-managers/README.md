# Project 07 — Context Managers & Protocols
**Difficulty: 7 / 10**

"Protocol" is Python's word for an informal interface: if an object has the
right dunder methods, it just *works* with a language feature — no inheritance
needed ("duck typing"). This project covers the **context manager protocol**
(`__enter__`/`__exit__`), `contextlib`, the **iterator protocol**, and
**`__getattr__`/`__setattr__`** for dynamic attribute behavior.

Read `context_managers.py`, predict each `print`, then run it.

## Concepts exercised
- The `with` statement and the context manager protocol
- `__enter__` returns the bound name; `__exit__` always runs (even on error)
- `contextlib.contextmanager` — writing a CM as a generator
- The iterator protocol: `__iter__` + `__next__`
- `__getattr__` (fallback attribute lookup) vs `__getattribute__` (every access)

## Questions (answer before running)
1. Does `"acquired"` print even though the `with` block raises? Why?
2. What does `__exit__`'s return value of `False` mean? What if it returned `True`?
3. In `Timer`, what does the `yield` accomplish inside `contextmanager`?
4. `list(CountDown(3))` — trace `__iter__` and `__next__`. What's the result?
5. `Config().debug` — `debug` isn't defined on the instance. Why does it return `False`?

## Interview angle
> "How would you ensure a file/lock is always released, even if an exception fires?"
Answer: the `with` statement guarantees `__exit__` runs. Returning `True` from
`__exit__` *suppresses* the exception; `False` (or `None`) lets it propagate.

## The protocol mental model
A protocol is **not** a class you inherit from. It's a *contract*: implement the
dunder methods, and Python's syntax (`with`, `for`, `len()`, `in`) will use them.
