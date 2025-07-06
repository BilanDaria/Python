from enum import Enum, auto
from task import Task

change_point = {
    "title": Task.change_title,
    "desc": Task.change_description,
    "priority": Task.change_priority,
    "deadline": Task.change_deadline,
}


class Status(Enum):
    OPEN = auto()
    IN_PROGRESS = auto()
    BLOCKED = auto()
    DONE = auto()
    REJECTED = auto()


class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


class IDCounter:
    counter = 0

    def get_next_id(self):
        self.counter += 1
        return int(self.counter)


#### TEST DATA FOR TASK MANAGER ####

data = [
    {
        "id": 1,
        "title": "Complete Project Proposal",
        "description": "Draft and finalize the project proposal for the new client.",
        "deadline": "2023-11-15",
        "status": "In Progress",
        "priority": "High"
    },
    {
        "id": 2,
        "title": "Fix Website Bug",
        "description": "Resolve the checkout page error causing payment failures.",
        "deadline": "2023-11-10",
        "status": "Block",
        "priority": "Critical"
    },
    {
        "id": 3,
        "title": "Schedule Team Meeting",
        "description": "Organize a meeting to discuss Q4 goals and deliverables.",
        "deadline": "2023-11-08",
        "status": "Completed",
        "priority": "Medium"
    },
    {
        "id": 4,
        "title": "Update Documentation",
        "description": "Review and update API documentation for developers.",
        "deadline": "2023-11-20",
        "status": "Open",
        "priority": "Low"
    },
    {
        "id": 5,
        "title": "Review Code Merge",
        "description": "Test and approve the latest feature branch before deployment.",
        "deadline": "2023-11-12",
        "status": "In Progress",
        "priority": "High"
    },
]

# menu = {
#     1: task_manager.add_task,
#     2: task_manager.find_task,
#     3: task_manager.change_task,
#     4: task_manager.delete_task,
#     5: task_manager.get_all_tasks,
#     6: task_manager.get_overdue_task,
#     7: task_manager.sort_by_deadlines,
#     8: task_manager.save_to_json,
# }
