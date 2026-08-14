"""The Task model: a dataclass with validation and a subclass registry."""
from dataclasses import dataclass, field
from enum import Enum


class TaskStatus(Enum):
    """Enum: a set of named constants. Members compared by identity."""
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"


@dataclass
class Task:
    """A dataclass auto-generates __init__, __repr__, and __eq__.

    Validation lives in __post_init__, which dataclass calls after __init__
    finishes setting the fields. This is the idiomatic place to add checks.
    """
    title: str
    priority: str = "normal"
    status: TaskStatus = TaskStatus.PENDING

    def __post_init__(self):
        # Runs after the generated __init__ assigns fields.
        allowed = {"low", "normal", "high"}
        if self.priority not in allowed:
            raise ValueError(
                f"priority must be one of {allowed}, got {self.priority!r}"
            )

    def mark_done(self):
        self.status = TaskStatus.DONE
