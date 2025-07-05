import data
class Task:
    def __init__(self, id, title, description, deadline, status, priority):
        self.id = id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = data.Status.OPEN
        self.priority = priority

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
