"""
Project 04 — Data Structures & Comprehensions
Difficulty 4/10

Parse comprehensions and choose the right container.
"""

# --- List comprehension: builds a new list in one expression --------------
# [expression for item in iterable if condition]
squares = [n * n for n in range(5)]   # -> [0, 1, 4, 9, 16]
print(squares)                        # predict: ?
print(squares[2])                     # predict: 4  (indexing, 0-based)

# Conditional comprehension: keep only evens.
evens = [n for n in range(10) if n % 2 == 0]
print(evens)                          # predict: ?


# --- Dict & set comprehensions -------------------------------------------
prices = {"apple": 1.5, "banana": 0.5, "cherry": 3.0}
# Build a dict of item -> rounded price.
rounded = {k: round(v) for k, v in prices.items()}
print(rounded)                        # predict: ?

# get() with a default avoids KeyError for missing keys.
print(prices.get("pen", 0))           # predict: 0


# --- zip: iterate two sequences in parallel ------------------------------
names = ["Ada", "Linus", "Grace"]
scores = [90, 85, 95]
# zip stops at the SHORTEST iterable.
pairs = list(zip(names, scores))
print(pairs)                          # predict: [('Ada', 90), ...]


# --- Set comprehension: dedupe & membership ------------------------------
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = {n for n in numbers}          # -> {1, 2, 3, 4}
print(unique)                         # predict: ?
print(4 in unique)                    # predict: True  (O(1) lookup)


# --- Tuple unpacking & the *rest syntax ----------------------------------
first, *rest = [10, 20, 30, 40]
print(first, rest)                    # predict: 10 [20, 30, 40]

# Swap two values using tuple packing/unpacking.
a, b = 1, 2
a, b = b, a
print(a, b)                           # predict: 2 1


# --- collections.Counter & setdefault ------------------------------------
from collections import Counter

words = "the cat sat on the mat the cat".split()
counts = Counter(words)
print(counts.most_common(1))           # predict: [('the', 3)]

# setdefault: returns the key's value, inserting a default if absent.
freq = {}
for w in words:
    freq.setdefault(w, 0)              # insert 0 if 'w' missing
    freq[w] += 1
print(freq["the"])                    # predict: 3


# --- Nested data structures (list of dicts) ------------------------------
inventory = [
    {"name": "widget", "qty": 12},
    {"name": "gadget", "qty": 3},
]
# Chain two indexings: inventory[0] is a dict, then ["name"] on it.
print(inventory[0]["name"])           # predict: widget
total_qty = sum(item["qty"] for item in inventory)  # generator expr
print(total_qty)                       # predict: 15
