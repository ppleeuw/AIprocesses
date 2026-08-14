"""
Project 03 — Functions, Scope & Default Arguments
Difficulty 3/10

Watch for the mutable-default pitfall and late-binding closures.
"""


# --- The mutable default argument pitfall ---------------------------------
# Default values are evaluated ONCE when 'def' runs, not on each call.
# So 'items=[]' is the SAME list object shared by every call that uses the default.
def append_to(value, items=[]):
    items.append(value)
    return items


print(append_to(1))           # predict: [1]
print(append_to(2))           # predict: [1, 2]  -- the shared list persists!

# Correct pattern: use None as a sentinel and create the list inside.
def append_to_safe(value, items=None):
    if items is None:          # 'is None' is the idiomatic sentinel check
        items = []
    items.append(value)
    return items


print(append_to_safe(1))      # predict: [1]
print(append_to_safe(2))      # predict: [2]  -- fresh list each call


# --- LEGB resolution: Local, Enclosing, Global, Built-in -----------------
x = "global"


def outer():
    x = "enclosing"            # local to outer, enclosing to inner

    def inner():
        # Reading x looks up: local (none) -> enclosing ("enclosing") -> hit!
        print(x)              # predict: "enclosing"

    inner()


outer()


# --- global / nonlocal ----------------------------------------------------
count = 0


def counter():
    # 'nonlocal count' would let us rebind the enclosing 'count'.
    # Here 'count' is module-global, so we need 'global'.
    global count
    count += 1
    return count


print(counter())               # predict: 1
print(counter())               # predict: 2


# --- Late-binding closures in a loop --------------------------------------
# Closures capture the NAME, not the VALUE. All these lambdas look up 'i'
# at call time, when the loop is done and i == 2.
funcs = [lambda: i for i in range(3)]
print(funcs[0]())             # predict: 2  (not 0!)
print(funcs[1]())             # predict: 2
print(funcs[2]())             # predict: 2

# Fix: bind the current value as a default argument.
funcs_fixed = [lambda i=i: i for i in range(3)]
print(funcs_fixed[0]())       # predict: 0


# --- *args and **kwargs ---------------------------------------------------
def greet(name, *args, **kwargs):
    # args is a tuple of extra positional args
    # kwargs is a dict of extra keyword args
    title = kwargs.get("title", "")  # safe lookup with default
    extras = ", ".join(args) or "none"
    return f"{title} {name} (extras: {extras})"


print(greet("Sam", "vip", "guest", title="Dr"))  # predict: ?
