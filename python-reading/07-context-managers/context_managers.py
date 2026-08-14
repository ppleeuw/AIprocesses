"""
Project 07 — Context Managers & Protocols
Difficulty 7/10

Protocols are informal interfaces: implement the dunders and the feature works.
"""
import contextlib


# --- The context manager protocol: __enter__ / __exit__ -------------------
class Resource:
    def __enter__(self):
        # Called when entering the 'with' block. Return value is bound
        # to the name after 'as'. Often 'return self'.
        print("acquired")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Called on block exit — ALWAYS, even if an exception occurred.
        # exc_* are None on normal exit, or the exception details on error.
        # Return True to SUPPRESS the exception; False/None to propagate it.
        print(f"released (exc={exc_type.__name__ if exc_type else None})")
        return False


# Even though the block raises, __exit__ still runs, then the error propagates.
try:
    with Resource() as r:
        print("using")
        raise ValueError("boom")
except ValueError:
    print("caught outside")
# predict order: acquired / using / released (exc=ValueError) / caught outside


# --- contextlib.contextmanager: a CM written as a generator ---------------
# Everything BEFORE 'yield' is __enter__; the value yielded is the 'as' value;
# everything AFTER 'yield' is __exit__ (runs even on error).
@contextlib.contextmanager
def Timer(label):
    print(f"[{label}] start")
    yield label              # this value is bound by 'as'
    print(f"[{label}] end")


with Timer("scan") as phase:
    print(f"inside, phase={phase}")
# predict: [scan] start / inside, phase=scan / [scan] end


# --- The iterator protocol: __iter__ + __next__ --------------------------
class CountDown:
    def __init__(self, start):
        self.n = start

    def __iter__(self):
        return self          # the object is its own iterator

    def __next__(self):
        if self.n <= 0:
            raise StopIteration   # signals "no more items" to the for loop
        self.n -= 1
        return self.n + 1    # return the value before decrement took effect


# 'for' calls __next__ repeatedly until StopIteration.
print(list(CountDown(3)))   # predict: [3, 2, 1]


# --- __getattr__: fallback for missing attributes ------------------------
class Config:
    defaults = {"debug": False, "timeout": 30}

    # __getattr__ is called ONLY when normal lookup FAILS.
    # (Contrast with __getattribute__, called on EVERY access.)
    def __getattr__(self, name):
        return self.defaults.get(name, None)


c = Config()
print(c.debug)              # predict: False  (not on instance -> __getattr__)
print(c.missing)            # predict: None   (not in defaults either)
