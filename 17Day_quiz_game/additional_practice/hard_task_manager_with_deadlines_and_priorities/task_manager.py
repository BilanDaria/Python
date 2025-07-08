from datetime import datetime
import json

from data import IDCounter, change_point, data
from task import Task

n_id = IDCounter()


class TaskManager:

    def __init__(self):
        self.list_of_tasks = []

    def add_task(self, title, description, deadline, priority):
        new_task = Task(n_id.get_next_id(), title, description, deadline, priority)
        self.list_of_tasks.append(new_task)
        return self.list_of_tasks[-1].id

    def find_task(self, task_id):
        # task = next((i for i in self.list_of_tasks if i.id == task_id), None)
        task = next((i for i in self.list_of_tasks if task_id == i.id), None)
        return task

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

    def get_task_index(self, task_id):
        return self.list_of_tasks.index(next((i for i in self.list_of_tasks if task_id == i.id), None))

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if not task:
            print('Task not found')
            return
        index = self.get_task_index(task_id)
        return self.list_of_tasks.pop(index)

    @staticmethod
    def sort_by_deadlines(order, tasks_list):
        sorted_task = sorted(tasks_list, key=lambda x: x.deadline, reverse=order)
        return sorted_task

    # Add sort_by_status
    @staticmethod
    def sort_by_status(order, tasks_list):
        sorted_task = sorted(tasks_list, key=lambda x: x.status.value, reverse=order)
        return sorted_task

    # Add sort_by_priority
    @staticmethod
    def sort_by_priority(order, tasks_list):
        sorted_task = sorted(tasks_list, key=lambda x: x.priority.value, reverse=order)
        return sorted_task

    def get_all_tasks(self):
        return self.list_of_tasks

    def get_overdue_task(self):
        current_date = datetime.date()
        overdue_tasks = [i for i in self.list_of_tasks if current_date > i.deadline]
        return overdue_tasks

    @staticmethod
    def save_to_json(path, tasks_list):
        path.write_text(json.dumps(tasks_list, indent=4))

    def __str__(self):
        return '\n'.join(str(i) for i in self.list_of_tasks)

    def __repr__(self):
        return self.__str__()