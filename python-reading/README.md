# Python Code-Reading Practice — Difficulty 1 → 10

A graded series of **reading-only** projects to prepare for Python job interviews.
You do **not** write code here. You read heavily-commented snippets, predict each
`print` output on paper, then run the file to check. Each project ends with the
interview-style question you'll actually be asked.

## Why reading, not writing

Most interview "read this code" questions test whether you can **trace execution**
and **name the idiom** — not whether you can type. These projects build that muscle
in increasing difficulty, each one layering on the previous.

## The 10 projects

| # | Difficulty | Project | Core concepts |
|---|-----------|---------|---------------|
| 01 | 1/10 | [Basics](01-basics/) | Variables, types, operators, f-strings |
| 02 | 2/10 | [Control Flow](02-control-flow/) | if/elif, truthiness, loops, break/continue, loop-else |
| 03 | 3/10 | [Functions](03-functions/) | Scope (LEGB), mutable defaults, closures, *args/**kwargs |
| 04 | 4/10 | [Data Structures](04-data-structures/) | Comprehensions, zip, sets, dict.get, Counter |
| 05 | 5/10 | [Classes](05-classes/) | self, inheritance, super(), MRO, dunder methods, @property |
| 06 | 6/10 | [Decorators & Generators](06-decorators-generators/) | @syntax, functools.wraps, yield, next, yield from |
| 07 | 7/10 | [Context Managers & Protocols](07-context-managers/) | with, __enter__/__exit__, contextlib, iterator protocol, __getattr__ |
| 08 | 8/10 | [Async / Await](08-async/) | coroutines, await, gather, async with, async for |
| 09 | 9/10 | [Metaclasses & Descriptors](09-metaclasses-descriptors/) | __get__/__set__, data descriptors, __init_subclass__, type.__new__ |
| 10 | 10/10 | [Real Codebase](10-real-codebase/) | A multi-file `taskqueue` package tying 01–09 together |

## How to use this series

1. **Read** the project's `README.md` for the concepts and interview angle.
2. **Open** the `.py` file and read top to bottom.
3. For every `# predict: ?` marker, **write down** what you think it outputs.
4. **Run** the file (`python <file>.py`) and compare. Re-read the comments on any mismatch.
5. Answer the **Questions** section in the README — these mirror real interview prompts.

For project 10, read the package as a reviewer would: start at the entry point
(`taskqueue/__main__.py`), follow the call graph, and name every Python feature
you encounter.

## Requirements

- Python 3.10+ (uses `match`-free syntax; type hints like `list[Task]` need 3.9+).
- No third-party dependencies — standard library only.

## Progression

Each difficulty assumes you've internalized the previous one. If a project feels
opaque, go back one level — the comments there explain the building blocks the
next level takes for granted.
