from datetime import datetime

from data import IDCounter, changeable_points
from task import Task

n_id = IDCounter()
class TaskManager:

    def __init__(self):
        self.list_of_tasks = []

    def add_task(self, title, description, deadline: datetime, priority):
        new_task = Task(n_id, title, description, deadline, priority)
        self.list_of_tasks.append(new_task)

    def find_task(self, task_id):
        return next((i for i in self.list_of_tasks if task_id == i.id), None)

    def change_task(self, task_id, point):
        if point not in changeable_points:
            print(f"You can't change {point} in the task.")
        task = self.find_task(task_id)
        if not task:
            print("Task not found")
            return
        task


    def delete_task(self, task_id):
        pass

    def sort_by_deadlines(self, order):
        pass

    def get_overdue_task(self):
        pass

    def save_to_json(self):
        pass

    def __str__(self):
        pass


