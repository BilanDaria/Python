from datetime import datetime

import data


class Task:
    def __init__(self, task_id, title, description, deadline, priority):
        self.id = task_id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = data.Status.OPEN.name
        self.priority = data.Priority[priority].name

    def change_title(self, new_title):
        self.title = new_title

    def change_description(self, new_desc):
        self.description = new_desc

    def change_deadline(self, new_deadline):
        self.deadline = new_deadline

    def change_status(self, new_status):
        self.status = new_status

    def change_priority(self, new_priority):
        self.priority = new_priority

    def update_fields(self, point, new_data):
        update_map = {
            "title": self.change_title,
            "description": self.change_description,
            "priority": self.change_priority,
            "deadline": self.change_deadline,
            "status": self.change_status,
        }
        if point not in update_map:
            print("Unchangeable point.")
            return
        update_map[point](new_data)

    class Task:
        ...

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline.isoformat(),  # convert date to str
            "status": self.status,
            "priority": self.priority,
        }

    @classmethod
    def from_dict(cls, data_dict):
        deadline = datetime.fromisoformat(data_dict["deadline"]).date()
        return cls(
            data_dict["id"],
            data_dict["title"],
            data_dict["description"],
            deadline,
            data_dict["priority"]
        )

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Deadline: {self.deadline}\n"
                f"Priority: {self.priority}\n"
                f"Status: {self.status}\n")

    def __repr__(self):
        return self.__str__()
