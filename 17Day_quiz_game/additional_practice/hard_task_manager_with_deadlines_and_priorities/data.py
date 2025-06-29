from enum import Enum, auto
from task import Task

class Status(Enum):
    OPEN = auto()
    IN_PROGRESS = auto()
    DONE = auto()


class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class IDCounter:
    _counter = 0

    def get_next_id(self):
        self._counter += 1
        return self._counter


changeable_points = {
    "title", "description", "deadline", "status", "priority"}
