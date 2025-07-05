from datetime import datetime
from pathlib import Path
import json

from data import IDCounter, change_point
from task import Task

n_id = IDCounter()
path = Path("D:\\Personal\\Programming\\Course Hunter\\Python\\100days\\17Day_quiz_game\\additional_practice\\medium_bank_account")


class TaskManager:

    def __init__(self):
        self.list_of_tasks = []

    def add_task(self, title, description, deadline: datetime, priority):
        new_task = Task(n_id, title, description, deadline, priority)
        self.list_of_tasks.append(new_task)

    def find_task(self, task_id):
        return next((i for i in self.list_of_tasks if task_id == i.id), None)

    def change_task(self, task_id, point, new_data):
        if point not in change_point:
            print(f"You can't change {point} in the task.")
            return
        task = self.find_task(task_id)
        if not task:
            print("Task not found")
            return
        change_point[point](new_data)
        return self.find_task(task_id)

    @staticmethod
    def __get_deadline(e):
        return e.deadline

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if not task:
            print('Task not found')
            return
        self.list_of_tasks.remove(task)
        return f"Task {task_id} was successfully deleted."

    @staticmethod
    def sort_by_deadlines(self, order, tasks):
        sorted_task = sorted(tasks, key=lambda x: x.deadline, reverse=(order if order else False))
        return sorted_task

    def get_all_tasks(self):
        return self.list_of_tasks

    def get_overdue_task(self):
        current_date = datetime.date()
        overdue_tasks = [i for i in self.list_of_tasks if current_date > i.deadline]
        return overdue_tasks

    def save_to_json(self):
        path.write_text(json.dumps(self.list_of_tasks, indent=4))

    def __str__(self):
        return '\n'.join(str(i) for i in self.list_of_tasks)


