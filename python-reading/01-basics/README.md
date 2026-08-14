# Project 01 — Basic Syntax, Variables & Types
**Difficulty: 1 / 10**

The goal of this series is to teach you to **read** Python code, not to write it.
Interviewers love showing a short snippet and asking "what does this print?"
or "what is the type of `x` after this line?". Each project builds on the last.

This first project covers the absolute foundations. Read `basics.py` top to bottom,
trace the values in your head, then answer the questions below **before** running
the file. Running it is the answer key — use it to check, not to learn.

## Concepts exercised
- Variables as name bindings (not boxes)
- Built-in types: `int`, `float`, `str`, `bool`, `None`
- Arithmetic operators and their precedence
- String formatting (f-strings) and indexing
- `print`, `type`, and the REPL-style evaluation order

## How to use this project
1. Open `basics.py` and read every line in order.
2. For each `print(...)`, write down on paper what you think it outputs.
3. Only then run: `python basics.py`.
4. Compare. Re-read the comments explaining any mismatch.

## Questions (answer before running)
1. What is the type of `price` after line `price = 9.99`?
2. What does `name[0]` return, and why is it not `"J"` the character vs a single-char string?
3. Evaluate `7 // 2` and `7 % 2` — what do integer division and modulo give you here?
4. What does `f"Total: {total:.2f}"` mean, piece by piece?
5. After `a, b = b, a`, what are the values of `a` and `b`? Why does this swap work?

## Interview angle
> "Walk me through what happens, line by line, when Python executes this file."
Practice narrating aloud: name each type, each operator, and the order of evaluation.
