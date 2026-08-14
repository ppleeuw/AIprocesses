# Project 09 — Metaclasses & Descriptors
**Difficulty: 9 / 10**

This is the deep end. These two mechanisms power `dataclasses`, ORMs (Django,
SQLAlchemy), `@property`, type validators, and Pydantic. You rarely *write*
them, but you will absolutely **read** code that uses them.

- A **descriptor** is any object with `__get__`/`__set__`/`__delete__` used as a
  *class attribute*; it intercepts attribute access. `property` is a built-in
  descriptor. This is how `self.name` can run validation automatically.
- A **metaclass** is a class whose *instances are classes*. `type` is the default
  metaclass. `__init_subclass__` is the modern, simpler alternative for most cases.

Read `metaclasses.py`, predict each `print`, then run it.

## Concepts exercised
- The descriptor protocol: `__get__`, `__set__`, `__set_name__`
- Data vs non-data descriptors (which wins against instance `__dict__`)
- `__init_subclass__` — hooks that run when a subclass is *defined*
- A minimal metaclass overriding `type.__new__`
- How `property` is "just" a data descriptor under the hood

## Questions (answer before running)
1. `p.age = -5` raises — which method enforces that, and when is it called?
2. `p.age` returns `30`, not a `Validated` object. Which method transforms it?
3. Why must `Validated` store values in `instance.__dict__[self.name]` and not in `self`?
4. `__init_subclass__` runs when `Dog` is *defined*. What does it print, and when?
5. The metaclass prints "creating class". At what point: class definition, or instantiation?

## Interview angle
> "How does `@property` actually work under the hood?"
Answer: `property` is a data descriptor. When you access `obj.x`, Python finds
`x` on the class (not the instance), sees `__get__`, and calls it. A *data*
descriptor (defines `__set__`) beats the instance `__dict__`; a *non-data*
descriptor (only `__get__`) loses to it.

## When to reach for each (reading guide)
- Need to intercept **attribute access** on instances → descriptor
- Need to customize **how a class itself is created** → metaclass or `__init_subclass__`
- Most real code uses `__init_subclass__` and `property`; raw metaclasses are rare.
