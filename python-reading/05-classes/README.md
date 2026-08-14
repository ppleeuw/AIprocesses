# Project 05 — Classes, Inheritance & Dunder Methods
**Difficulty: 5 / 10**

OOP is where "can you read code" becomes "can you read *design*". This project
covers `__init__`, `self`, inheritance, `super()`, method resolution order
(MRO), and the data-model dunder methods (`__repr__`, `__eq__`, `__lt__`)
that make objects behave like built-ins.

Read `classes.py`, predict each `print`, then run it.

## Concepts exercised
- `__init__` vs class vs instance attributes
- `self` is just the first parameter (a convention, not a keyword)
- Single & multiple inheritance, `super()`
- Method Resolution Order (MRO) and the C3 linearization
- Dunder methods: `__repr__`, `__str__`, `__eq__`, `__lt__`, `__len__`
- `@property` for computed attributes

## Questions (answer before running)
1. `Account("Ada").owner` — where does `owner` come from, `__init__` or class?
2. Both `Dog` and `Cat` define `speak`. What does `Cat().speak()` print, and why?
3. In `SavingsAccount.deposit`, what does `super().deposit(amount)` resolve to?
4. Why define `__eq__` and `__lt__` together? What does `sorted(accounts)` use?
5. `circle.area` is accessed like an attribute but is a method — how does `@property` do that?

## Interview angle
> "Show me the MRO of class C." / "Why did they override `__repr__`?"
A precise answer: `__repr__` is for developers (used by the REPL and debugging);
`__str__` is for end users. If only `__repr__` is defined, `str()` falls back to it.

## Key reading skill
When you see `class X(Y):`, immediately ask: what does `Y` provide, and what
does `X` override? Trace method calls up the MRO, not just "the parent".
