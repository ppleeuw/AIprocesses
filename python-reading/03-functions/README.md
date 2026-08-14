# Project 03 — Functions, Scope & Default Arguments
**Difficulty: 3 / 10**

Functions are where interviewers start testing whether you understand **when**
code runs and **what** a name refers to. The classic traps: mutable default
arguments, late-binding closures, and `global`/`nonlocal`.

Read `functions.py`, predict each `print`, then run it.

## Concepts exercised
- Definition vs. call time
- Positional, keyword, and default arguments
- Mutable default argument pitfall (the most famous Python interview question)
- LEGB name resolution: Local → Enclosing → Global → Built-in
- `global` / `nonlocal` declarations
- `*args` / `**kwargs`

## Questions (answer before running)
1. `append_to(1)` returns `[1]`. Then `append_to(2)` returns `[1, 2]`. Why?!
2. What does `funcs[0]()` print, and why is it 2 and not 0? (late binding)
3. In `outer`, can `inner` read `x`? Can it rebind it without `nonlocal`?
4. After `counter()` is called twice, what is `count`? How does `nonlocal` make this work?
5. In `greet("Sam", title="Dr")`, which argument is positional and which is keyword?

## Interview angle
> "Explain why this function behaves differently on the second call."
The mutable default answer: defaults are evaluated **once** at definition time,
and the same list object is reused across calls. Say it out loud.

## The one-line rule to memorize
> **Never use a mutable object as a default argument.** Use `None` and create
> the object inside the function body instead.
