# Project 10 — Reading a Real-World Idiomatic Codebase
**Difficulty: 10 / 10**

This is the capstone. Projects 01–09 taught isolated features; here they all
appear together in the style of real production code: type hints, dataclasses,
an iterator/iterable, a context manager, a decorator, async, descriptors-ish
validation via dataclass `__post_init__`, an `__init_subclass__` registry,
and a `__main__` entry point with `argparse`.

You will NOT be asked to write any of this. Your job is to **read** it: trace
the call graph, explain each idiom, and predict behavior.

## The codebase
```
taskqueue/
├── __init__.py        # public API re-exports
├── task.py            # the Task dataclass + validation + registry
├── queue.py           # the TaskQueue: iterator, context manager, async drain
├── logging_decorator.py   # a @log decorator applied to queue methods
└── __main__.py        # CLI entry point (python -m taskqueue)
```

## How to read it (the interview skill)
1. **Start at the entry point** (`__main__.py`), not the leaves. Find `main()`.
2. Follow the first call: what type is the argument, where does it come from?
3. For each idiom, name it aloud: "this is a dataclass with `__post_init__`
   validation", "this is a context manager using `contextlib.contextmanager`".
4. When you hit `async def`, note where `await` hands off and what runs concurrently.
5. Predict the output of `python -m taskqueue add "Write tests" --priority high`
   before running it.

## Questions (answer before running)
1. `Task("x", priority="extreme")` — what happens and which method enforces it?
2. `TaskQueue.__iter__` yields tasks; `list(q)` — how does that work under the hood?
3. The `@logged` decorator wraps `add` and `drain`. When does the wrapper body run?
4. `async with TaskQueue() as q:` — name both protocols this single line uses.
5. `drain()` uses `asyncio.gather`. Why concurrent and not a plain `for` loop?
6. `Task` is registered via `__init_subclass__`? Check `task.py` — is it, or not? Explain.

## Interview angle
> "Here's a small package. Walk me through what `python -m taskqueue` does,
>  end to end, naming every Python feature you recognize."

The expected narration covers: `argparse` parsing → `Task` dataclass construction
with `__post_init__` validation → `TaskQueue` (a context manager) → `@logged`
decorator wrapping `add` → `__iter__` enabling `for t in q` → `asyncio.run(drain)`
using `gather` for concurrency. Saying these *names* out loud is the skill.

## Run it
```bash
python -m taskqueue add "Write tests" --priority high
python -m taskqueue add "Refactor queue" --priority low
python -m taskqueue run
```
