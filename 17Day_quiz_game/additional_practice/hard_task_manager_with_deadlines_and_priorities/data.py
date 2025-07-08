from enum import Enum, auto
from task import Task

change_point = {
    "title": Task.change_title,
    "desc": Task.change_description,
    "priority": Task.change_priority,
    "deadline": Task.change_deadline,
}

sort_parameters = ['deadline', 'status', 'priority']

archive = []
all_tasks = []
overdue_tasks = []
sorted_tasks = []


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

# 0. exit
# 1. create
# 2. find
# 3. change
# 4. delete (archive)
# 5. get all tasks
# 6. get overdue_tasks
# 7. sort
# 8. get archive tasks
# 9: save 10 json

# data = [
#     {
#         "id": 1,
#         "title": "Complete Project Proposal",
#         "description": "Draft and finalize the project proposal for the new client.",
#         "deadline": "2023-11-15",
#         "status": "In Progress",
#         "priority": "High"
#     },
#     {
#         "id": 2,
#         "title": "Fix Website Bug",
#         "description": "Resolve the checkout page error causing payment failures.",
#         "deadline": "2023-11-10",
#         "status": "Block",
#         "priority": "Critical"
#     },
#     {
#         "id": 3,
#         "title": "Schedule Team Meeting",
#         "description": "Organize a meeting to discuss Q4 goals and deliverables.",
#         "deadline": "2023-11-08",
#         "status": "Completed",
#         "priority": "Medium"
#     },
#     {
#         "id": 4,
#         "title": "Update Documentation",
#         "description": "Review and update API documentation for developers.",
#         "deadline": "2023-11-20",
#         "status": "Open",
#         "priority": "Low"
#     },
#     {
#         "id": 5,
#         "title": "Review Code Merge",
#         "description": "Test and approve the latest feature branch before deployment.",
#         "deadline": "2023-11-12",
#         "status": "In Progress",
#         "priority": "High"
#     },
# ]


