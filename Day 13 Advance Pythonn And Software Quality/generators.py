
from typing import Iterator
from models import Task


def process_tasks(tasks: list[Task]) -> Iterator[Task]:

    for task in tasks:
        yield task
