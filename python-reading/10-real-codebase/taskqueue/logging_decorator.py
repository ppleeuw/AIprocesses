"""A decorator that logs calls. Applied to TaskQueue methods."""
import functools


def logged(func):
    """A decorator: wraps a function to print before/after it runs.

    'func = logged(func)' happens at definition time; 'wrapper' runs on each call.
    functools.wraps copies metadata so the wrapped function keeps its name/doc.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[log] calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[log] {func.__name__} done")
        return result
    return wrapper
