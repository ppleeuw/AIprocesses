# Project 02 — Control Flow & Conditionals
**Difficulty: 2 / 10**

Now you can read statements. The next skill is tracing **which branch** executes
and **how many times** a loop runs. Interviewers test this with off-by-one loops,
`elif` chains, and short-circuit `and`/`or`.

Read `control_flow.py`, predict every `print` and the final `result`, then run it.

## Concepts exercised
- `if` / `elif` / `else` (only one branch ever runs)
- Truthiness: empty containers and `0` are falsy
- Short-circuit evaluation of `and` / `or`
- `for` over iterables, `range` semantics (exclusive end)
- `while`, `break`, `continue`, and the `else` clause on loops

## Questions (answer before running)
1. In `classify(15)`, which branch runs and why is only one printed?
2. What does `result = status or default` evaluate to if `status = ""`?
3. How many times does the `for i in range(1, 6)` loop body run?
4. The loop `else` runs only when the loop finishes **without** `break`.
   Will the `for...else` here print "completed"? Trace `break` carefully.
5. In the `while n > 0` loop, what is the final value of `n` and why does the loop stop?

## Interview angle
> "I'll show you a function. Tell me what `classify(x)` returns for x = 15, 5, -3."
Practice tracing input through branches aloud, naming each condition.

## Gotcha to memorize
`range(1, 6)` produces `1, 2, 3, 4, 5` — the second argument is **exclusive**.
Off-by-one errors here are the #1 reading mistake in interviews.
