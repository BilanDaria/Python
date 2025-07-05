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
    _counter = 0

    def get_next_id(self):
        self._counter += 1
        return self._counter


#### TEST DATA FOR TASK MANAGER ####

data = [
    {
        "title": "Complete Project Proposal",
        "description": "Draft and finalize the project proposal for the new client.",
        "deadline": "2023-11-15",
        "status": "In Progress",
        "priority": "High"
    },
    {
        "title": "Fix Website Bug",
        "description": "Resolve the checkout page error causing payment failures.",
        "deadline": "2023-11-10",
        "status": "Block",
        "priority": "Critical"
    },
    {
        "title": "Schedule Team Meeting",
        "description": "Organize a meeting to discuss Q4 goals and deliverables.",
        "deadline": "2023-11-08",
        "status": "Completed",
        "priority": "Medium"
    },
    {
        "title": "Update Documentation",
        "description": "Review and update API documentation for developers.",
        "deadline": "2023-11-20",
        "status": "Open",
        "priority": "Low"
    },
    {
        "title": "Review Code Merge",
        "description": "Test and approve the latest feature branch before deployment.",
        "deadline": "2023-11-12",
        "status": "In Progress",
        "priority": "High"
    },
    {
        "title": "Prepare Monthly Report",
        "description": "Compile performance metrics and present findings to management.",
        "deadline": "2023-11-30",
        "status": "Open",
        "priority": "Medium"
    },
    {
        "title": "Backup Database",
        "description": "Perform a full backup of the production database.",
        "deadline": "2023-11-09",
        "status": "Block",
        "priority": "Critical"
    },
    {
        "title": "Organize Team Event",
        "description": "Plan a team-building activity for next month.",
        "deadline": "2023-12-01",
        "status": "Open",
        "priority": "Low"
    },
    {
        "title": "Respond to Client Emails",
        "description": "Address pending client inquiries and follow-ups.",
        "deadline": "2023-11-07",
        "status": "In Progress",
        "priority": "Medium"
    },
    {
        "title": "Upgrade Server Hardware",
        "description": "Schedule and execute server upgrades for better performance.",
        "deadline": "2023-11-25",
        "status": "Block",
        "priority": "High"
    }
]
