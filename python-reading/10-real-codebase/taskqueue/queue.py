"""The TaskQueue: an iterable + async context manager that drains concurrently."""
import asyncio
import contextlib

from .task import Task, TaskStatus
from .logging_decorator import logged


class TaskQueue:
    """A queue that is BOTH:
      - iterable: __iter__ yields tasks, so 'for t in q' and list(q) work
      - an async context manager: __aenter__/__aexit__ via @contextmanager

    Note this combines several protocols from earlier projects into one class.
    """

    def __init__(self):
        self._tasks: list[Task] = []

    # --- Iterable protocol ------------------------------------------------
    def __iter__(self):
        # Iterating the queue yields its tasks. Enables 'for t in q'.
        return iter(self._tasks)

    def __len__(self):
        # Lets len(q) work; also makes the object truthy/falsy sensibly.
        return len(self._tasks)

    # --- Decorated methods ------------------------------------------------
    @logged
    def add(self, task: Task) -> None:
        self._tasks.append(task)

    @logged
    async def drain(self) -> None:
        """Process all tasks concurrently.

        asyncio.gather schedules every coroutine together; total time is the
        max task time, not the sum. Each _process call awaits sleep (non-blocking).
        """
        # Build a coroutine per task, then run them all concurrently.
        coros = [self._process(t) for t in self._tasks]
        await asyncio.gather(*coros)

    async def _process(self, task: Task) -> None:
        task.status = TaskStatus.RUNNING
        await asyncio.sleep(0.05)   # simulate work, non-blocking
        task.mark_done()
        print(f"  done: {task.title}")


# --- async context manager written as a generator ------------------------
# Everything before yield is __aenter__; the yielded value is the 'as' target;
# the finally block is __aexit__ and runs even if the body raised.
@contextlib.asynccontextmanager
async def open_queue():
    q = TaskQueue()
    print("queue opened")
    try:
        yield q
    finally:
        print(f"queue closed ({len(q)} tasks)")


# Re-export so callers can do: from taskqueue.queue import open_queue
__all__ = ["TaskQueue", "open_queue"]
