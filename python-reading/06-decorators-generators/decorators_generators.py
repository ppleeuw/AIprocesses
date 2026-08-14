"""
Project 06 — Decorators & Generators
Difficulty 6/10

Decorators wrap functions at definition time. Generators yield lazily.
"""
import functools


# --- A decorator is a higher-order function -------------------------------
# 'log_calls' takes a function 'func' and returns a NEW function 'wrapper'.
def log_calls(func):
    @functools.wraps(func)      # preserve func's __name__ and __doc__
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}({args})")
        result = func(*args, **kwargs)   # actually call the original
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


# This line runs AT DEFINITION TIME: add = log_calls(add)
@log_calls
def add(a, b):
    return a + b


print(add(2, 3))
# predict order:
#   calling add((2, 3))
#   add returned 5
#   5


# --- Generators: yield suspends, next() resumes --------------------------
def count_up_to(limit):
    n = 1
    while n <= limit:
        yield n            # suspend here, emit n
        n += 1             # resume here on next call


gen = count_up_to(3)
print(next(gen))           # predict: 1  (runs to first yield)
print(next(gen))           # predict: 2  (resumes after yield, runs to next)
print(next(gen))           # predict: 3


# --- Infinite generator: lazy, so it never hangs until you consume it ----
def evens():
    n = 0
    while True:            # infinite loop, but yield pauses each step
        yield n
        n += 2


e = evens()
print(next(e), next(e), next(e))   # predict: 0 2 4


# --- yield from: delegate to a sub-generator ------------------------------
def chained():
    yield from [1, 2]     # emits 1 then 2
    yield from (3, 4)      # emits 3 then 4


print(list(chained()))    # predict: [1, 2, 3, 4]


# --- Generator expression (like a list comp but lazy) --------------------
# Saves memory: produces values on demand instead of building a list.
def range_gen(n):
    for i in range(n):
        yield i * i


# sum() consumes the generator; only ONE value exists in memory at a time.
print(sum(range_gen(4)))  # predict: 0+1+4+9 = 14


# --- A practical decorator: retry on failure -----------------------------
def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times - 1:
                        raise
        return wrapper
    return decorator


@retry(3)
def flaky():
    return "ok"


print(flaky())            # predict: ok
