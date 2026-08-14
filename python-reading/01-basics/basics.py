"""
Project 01 — Basic Syntax, Variables & Types
Difficulty 1/10

Read this file top to bottom. Predict each print() output before running.
"""

# --- Variables are name bindings, not boxes --------------------------------
# 'name' is bound to a str object. The object is immutable; rebinding
# 'name' just points the name at a new object.
name = "Jamie"
print(name)            # predict: ?

# --- Numeric types --------------------------------------------------------
age = 30               # int (arbitrary precision in Python 3)
price = 9.99           # float (IEEE 754 double)

# Integer division // drops the fractional part; % gives the remainder.
share = 7 // 2         # -> 3   (floor division, not truncation toward zero)
leftover = 7 % 2       # -> 1
print(share, leftover) # predict: ?

# Precedence: * and / bind tighter than + and -. Use parens for clarity.
total = 3 + 4 * 2      # -> 11, not 14
print(total)           # predict: ?

# --- Booleans and None ---------------------------------------------------
# bool is a subclass of int: True == 1, False == 0.
is_admin = True
print(is_admin + 1)    # predict: ?  (hint: True behaves like 1)
nothing = None         # the singleton "no value"
print(nothing is None) # predict: ?  ('is' tests identity, not equality)

# --- Strings --------------------------------------------------------------
# Indexing returns a one-character str, not a 'char' type (Python has none).
first = name[0]        # -> "J"
print(type(first))     # predict: ?

# f-strings: expressions inside {} are evaluated, then formatted.
# :.2f means "float with 2 decimal places".
print(f"Total: {total:.2f}")   # predict: ?
print(f"{name} is {age}")     # predict: ?

# --- Multiple assignment & swap -------------------------------------------
# Right-hand side is a tuple, evaluated fully before any assignment.
a, b = 1, 2
a, b = b, a             # swap: a becomes 2, b becomes 1
print(a, b)            # predict: ?

# --- Augmented assignment -------------------------------------------------
counter = 5
counter += 3           # equivalent to counter = counter + 3
print(counter)         # predict: ?
