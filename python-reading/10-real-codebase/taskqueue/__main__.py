"""CLI entry point: run with 'python -m taskqueue ...'.

Demonstrates the standard CLI idiom: argparse for parsing, a dispatch dict
mapping subcommands to handler functions, and asyncio.run to drive async code.
"""
import argparse
import asyncio

from .queue import open_queue
from .task import Task


def cmd_add(args) -> int:
    """Build a Task (triggers __post_init__ validation) and enqueue it.

    Note: open_queue() is an async context manager; we enter it with 'async with'.
    Inside, q.add is decorated with @logged, so you'll see [log] lines.
    """
    async def _run():
        async with open_queue() as q:
            t = Task(args.title, priority=args.priority)
            q.add(t)
            print(f"added: {t.title} ({t.priority})")
            # Print all tasks: iterates the queue via __iter__.
            for task in q:
                print(f"  - {task.title}: {task.status.value}")
    asyncio.run(_run())
    return 0


def cmd_run(args) -> int:
    """Drain a couple of hardcoded tasks concurrently to show gather in action."""
    async def _run():
        async with open_queue() as q:
            q.add(Task("Write tests", priority="high"))
            q.add(Task("Refactor queue", priority="low"))
            # drain() runs all _process coroutines concurrently via gather.
            await q.drain()
    asyncio.run(_run())
    return 0


def build_parser() -> argparse.ArgumentParser:
    """argparse: the standard library CLI parser. Subparsers dispatch by command."""
    parser = argparse.ArgumentParser(prog="taskqueue")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="add a task")
    p_add.add_argument("title")
    p_add.add_argument("--priority", default="normal")
    p_add.set_defaults(func=cmd_add)

    p_run = sub.add_parser("run", help="run the demo queue")
    p_run.set_defaults(func=cmd_run)

    return parser


def main(argv=None) -> int:
    """The entry point. Parses args and dispatches to the matching handler."""
    parser = build_parser()
    args = parser.parse_args(argv)
    # Each subparser stores its handler in 'func' via set_defaults.
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
