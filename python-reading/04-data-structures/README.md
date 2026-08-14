# Project 04 — Data Structures & Comprehensions
**Difficulty: 4 / 10**

Reading idiomatic Python means fluently parsing list/dict/set comprehensions
and knowing when a tuple, set, or dict is the right tool. This project also
covers tuple unpacking, `zip`, and dict `get`/`setdefault`.

Read `data_structures.py`, predict each `print`, then run it.

## Concepts exercised
- List, dict, set, and tuple semantics (mutability, ordering, hashing)
- Comprehensions: list `[...]`, dict `{k: v ...}`, set `{...}`
- Tuple unpacking and the `*` rest syntax
- `zip` for parallel iteration
- `dict.get`, `dict.setdefault`, `collections.Counter`
- Nested data structures (list of dicts)

## Questions (answer before running)
1. Why does `squares[2]` equal `4`? What does the comprehension build?
2. `prices.get("pen", 0)` — what's returned and why use a default?
3. In `zip(names, scores)`, what happens if one list is longer?
4. After the set comprehension, is `4` in the set? Are duplicates kept?
5. In the nested dict `inventory[0]["name"]`, trace the two index operations.

## Interview angle
> "Rewrite this loop as a comprehension" / "Is this item in the set or the list?"
Know that `in` on a set/dict is O(1) but `in` on a list is O(n) — interviewers ask.

## Mutability rules to recall
- `tuple` is immutable but may *contain* mutable items
- `set` elements and `dict` keys must be **hashable** (so no lists, no sets)
- `frozenset` is the immutable, hashable set
