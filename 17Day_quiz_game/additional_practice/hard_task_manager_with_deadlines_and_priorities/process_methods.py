from datetime import datetime
from pathlib import Path

from task_manager import TaskManager
import get_methods
import data

path_for_all_tasks = Path("D:\\Personal\\Programming\\Course Hunter\\Python\\100days\\17Day_quiz_game\\additional_practice\\hard_task_manager_with_deadlines_and_priorities\\all.txt")
path_for_overdue_tasks = Path("D:\\Personal\\Programming\\Course Hunter\\Python\\100days\\17Day_quiz_game\\additional_practice\\hard_task_manager_with_deadlines_and_priorities\\overdue.txt")
path_for_last_sorted_tasks = Path("D:\\Personal\\Programming\\Course Hunter\\Python\\100days\\17Day_quiz_game\\additional_practice\\hard_task_manager_with_deadlines_and_priorities\\sorted.txt")

task_manager = TaskManager()

def add_new_task():
    print("Create new task:")
    title, desc, deadline, priority = get_methods.get_all_attributes()
    new_id = task_manager.add_task(title, desc, deadline, priority)
    print("New task successfully added:\n"
          f"{task_manager.find_task(new_id)}")


def find_the_task():
    task = task_manager.find_task(get_methods.get_id())
    if not task:
        print("Task not found")
        return
    print(task)


param_to_change = {
    "title": get_methods.get_title,
    "desc": get_methods.get_description,
    "deadline": get_methods.get_deadline,
    "priority": get_methods.get_priority,
    "status": get_methods.get_status,
}

prompt_to_change_task = ("What would you like to change?"
                         "(title, description, deadline, priority, status, exit(to cancel editing))\n"
                         "Enter your choice: ")


def change_existing_task():
    task_id = get_methods.get_id()
    print(f"Let's change task {task_id}: ")
    try:
        param = input(prompt_to_change_task)
    except ValueError:
        print("Invalid input.")
        return
    if param == 'exit':
        print("Editing canceled.")
        return
    if param not in param_to_change:
        print(f"You can't change {param}")
        change_existing_task(task_id)
    new_data = param_to_change[param]()
    edited_task = task_manager.change_task(task_id, param, new_data)
    if not edited_task:
        print(f"Error editing task {task_id}. Recheck your data and try again.")
        return
    print(edited_task)


def delete_task():
    task_id = get_methods.get_id()
    data.archive.append(task_manager.delete_task(task_id))
    print(f"Task {task_id} successfully deleted.")


def clear_list_of_tasks(list_of_tasks):
    return list_of_tasks.clear()


def receive_all_tasks():
    data.all_tasks = clear_list_of_tasks(data.all_tasks)
    data.all_tasks = task_manager.get_all_tasks()
    print(get_methods.get_all_tasks_from_list(data.all_tasks))


def receive_all_overdue_tasks():
    data.overdue_tasks.clear()
    data.overdue_tasks = task_manager.get_overdue_task()
    print(get_methods.get_all_tasks_from_list(data.overdue_tasks))


def receive_sorted_tasks():
    receive_all_tasks()
    receive_all_overdue_tasks()
    data.sorted_tasks.clear()
    data.sorted_tasks = sort_tasks()
    print(get_methods.get_all_tasks_from_list(data.sorted_tasks))


def sort_tasks():
    ans = input("You'd like to sort all task or overdue? Enter a - for all, o - for overdue, c - for cancel: ").lower()
    if ans == 'c':
        print("Sorting canceled...")
        return
    elif ans == 'a':
        if len(data.all_tasks) == 0:
            print("You can't sort empty list. Sorting canceled...")
            return sort_tasks()
        tasks = data.all_tasks
    elif ans == 'o':
        if len(data.overdue_tasks) == 0:
            print("You can't sort empty list. Sorting canceled...")
            return sort_tasks()
        tasks = data.overdue_tasks
    else:
        print("Unknown list of tasks. Sorting canceled...")
        return

    param = input("What parameter should I use to sort the list (deadline, status, priority): ")
    if param not in data.sort_parameters:
        print("Unknown sort parameter. Process canceled...")
        return
    order = bool(input("Enter the order. T - for descending, F - for ascending"))

    if param == 'deadline':
        result = task_manager.sort_by_deadlines(order, tasks)
    elif param == 'status':
        result = task_manager.sort_by_status(order, tasks)
    else:
        result = task_manager.sort_by_priority(order, tasks)
    return result


def receive_archive_tasks():
    if len(data.archive) == 0:
        print("There no archive tasks.")
    else:
        print(get_methods.get_all_tasks_from_list(data.archive))


def save_tasks():
    ans = input("Which tasks you'd like to save? Enter a - for all, o - for overdue, s - for last sorted.: ").lower()
    if ans == "a":
        data.all_tasks.clear()
        data.all_tasks = task_manager.get_all_tasks()
        task_manager.save_to_json(path_for_all_tasks, data.all_tasks)
    elif ans == "o":
        data.overdue_tasks.clear()
        data.overdue_tasks = task_manager.get_overdue_task()
        task_manager.save_to_json(path_for_overdue_tasks, data.overdue_tasks)
    elif ans == "s":
        task_manager.save_to_json(path_for_last_sorted_tasks, data.sorted_tasks)
    else:
        print("Unknown list. Saving canceled...")
        return

