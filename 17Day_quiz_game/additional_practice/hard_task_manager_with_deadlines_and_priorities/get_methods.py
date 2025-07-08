import data
from datetime import datetime


def get_id(prompt='Enter task id: '):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input.\n ")
        return get_id()


def get_title(prompt='Enter title: '):
    try:
        return input(prompt)
    except ValueError:
        print("Invalid input.\n ")
        return get_title()


def get_description(prompt='Enter description: '):
    try:
        return input(prompt)
    except ValueError:
        print("Invalid input.\n ")
        return get_description()


def get_deadline(prompt='Enter deadline in yy-mm-dd: '):
    try:
        date = input(prompt)
        deadline = datetime.strptime(date, "%Y-%m-%d").date()
        return deadline
    except ValueError:
        print("Invalid input.\n ")
        return get_deadline()


def get_priority(prompt='Enter priority (Low, Medium, High, Critical): '):
    priority = input(prompt).upper()
    try:
        return data.Priority[priority].name
    except KeyError:
        print("Invalid priority type.\n")
        return get_priority()


def get_status(prompt='Enter status (Open, In_progress, Blocked, Done, Rejected): '):
    status = input(prompt).upper()
    try:
        return data.Status[status].name
    except KeyError:
        print("Invalid priority type.\n")
        return get_status()


def get_all_attributes():
    title = get_title()
    desc = get_description()
    deadline = get_deadline()
    priority = get_priority()
    return title, desc, deadline, priority


def get_all_tasks_from_list(current_list):
    return '\n'.join(str(i) for i in current_list)


