from datetime import datetime

from task_manager import TaskManager
import data

task_manager = TaskManager()
all_tasks = []
overdue_tasks = []


def get_title(prompt='Enter title: '):
    try:
        return input(prompt)
    except ValueError:
        print("Invalid input.\n ")
        get_title()


def get_description(prompt='Enter description: '):
    try:
        return input(prompt)
    except ValueError:
        print("Invalid input.\n ")
        get_description()


def get_deadline(prompt='Enter deadline in yy-mm-dd: '):
    try:
        date = input(prompt)
        deadline = datetime.strptime(date, "%Y-%m-%d").date()
        return deadline
    except ValueError:
        print("Invalid input.\n ")
        get_deadline()


def get_priority(prompt='Enter priority (Low, Medium, High, Critical): '):
    priority = input(prompt).upper()
    try:
        return data.Priority[priority].name
    except KeyError:
        print("Invalid priority type.\n")
        get_priority()


def get_status(prompt='Enter status (Open, In_progress, Blocked, Done, Rejected): ')
    status = input(prompt).upper()
    try:
        return data.Status[status].name
    except KeyError:
        print("Invalid priority type.\n")
        get_status()


def start():
    pass

start()
