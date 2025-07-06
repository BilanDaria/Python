from datetime import datetime
from pathlib import Path

from task_manager import TaskManager
import data

task_manager = TaskManager()
all_tasks = []
overdue_tasks = []
sorted_tasks = []

path_for_all_tasks = Path("D:\\Personal\\Programming\\Course Hunter\\Python\\100days\\17Day_quiz_game\\additional_practice\\hard_task_manager_with_deadlines_and_priorities\\all.txt")
path_for_overdue_tasks = Path("D:\\Personal\\Programming\\Course Hunter\\Python\\100days\\17Day_quiz_game\\additional_practice\\hard_task_manager_with_deadlines_and_priorities\\overdue.txt")
path_for_last_sorted_tasks = Path("D:\\Personal\\Programming\\Course Hunter\\Python\\100days\\17Day_quiz_game\\additional_practice\\hard_task_manager_with_deadlines_and_priorities\\sorted.txt")


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


def add_new_task():
    print("Create new task:")
    # title = get_title()
    # desc = get_description()
    # deadline = get_deadline()
    # priority = get_priority()
    title, desc, deadline, priority = get_all_attributes()
    new_id = task_manager.add_task(title, desc, deadline, priority)
    print("New task successfully added:\n"
          f"{task_manager.find_task(new_id)}")


def find_the_task():
    task = task_manager.find_task(get_id())
    if not task:
        print("Task not found")
        return
    print(task)


param_to_change = {
    "title": get_title,
    "desc": get_description,
    "deadline": get_deadline,
    "priority": get_priority,
    "status": get_status,
}

prompt_to_change_task = ("What would you like to change?"
                         "(title, description, deadline, priority, status, exit(to cancel editing))\n"
                         "Enter your choice: ")


def change_existing_task(task_id):
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


def sort_tasks():
    if len(all_tasks) == 0 and len(overdue_tasks) == 0:
        print("You don't have any tasks. Try to get all tasks before sort them.")
        return
    if len(all_tasks) == 0:
        tasks = overdue_tasks
    elif len(overdue_tasks) == 0:
        tasks = all_tasks
    else:
        ans = input("You'd like to sort all task or overdue? Enter a - for all, o - for overdue: ").lower()
        if ans == 'a':
            tasks = all_tasks
        elif ans == 'o':
            tasks = overdue_tasks
        else:
            print("Unknown list of tasks.")
            return
    order = input("Enter the order. T - for descending, F - for ascending")
    result = task_manager.sort_by_deadlines(order, tasks)
    return result


def save_tasks():
    global all_tasks
    global overdue_tasks
    global sorted_tasks

    ans = input("Which tasks you'd like to save? Enter a - for all, o - for overdue, s - for last sorted.: ").lower()
    if ans == "a":
        all_tasks.clear()
        all_tasks = task_manager.get_all_tasks()
        task_manager.save_to_json(path_for_all_tasks, all_tasks)
    elif ans == "o":
        overdue_tasks.clear()
        overdue_tasks = task_manager.get_overdue_task()
        task_manager.save_to_json(path_for_overdue_tasks, overdue_tasks)
    elif ans == "s":
        task_manager.save_to_json(path_for_last_sorted_tasks, sorted_tasks)


def first_task():
    print("Let's start with the first task in our workspace!")
    ans = input("Would you like to create your first task? y/n: ").lower()
    if ans == 'n':
        print('What a pitiful situation... What else you can do in Task Manager program without tasks 🤔.')
        return
    add_new_task()


def main_block(point):
    global all_tasks
    global overdue_tasks
    global sorted_tasks

    if point == 1:
        add_new_task()
    elif point == 2:
        find_the_task()
    # elif point == 3:
    #     task_id = get_id()
    #     change_existing_task(task_id)
    elif point == 4:
        task_id = get_id()
        task_manager.delete_task(task_id)
        print(f"Task {task_id} successfully deleted.")
    elif point == 5:
        all_tasks.clear()
        all_task = task_manager.get_all_tasks()
        print(task_manager)
    # elif point == 6:
    #     overdue_tasks.clear()
    #     overdue_tasks = task_manager.get_overdue_task()
    #     print(overdue_tasks)
    # elif point == 7:
    #     sorted_tasks.clear()
    #     sorted_tasks = sort_tasks()
    #     print(sorted_tasks)
    # else:
    #     save_tasks()


menu_items = ("What you may to do (enter the number of chose option):\n"
              "0 - escape? 😈\n"
              "1 - create new task\n"
              "2 - find exact task\n"
              "3 - change existing task\n"
              "4 - delete task (are you sure?)\n"
              "5 - get all tasks\n"
              "6 - sort tasks by deadlines\n"
              "7 - get all overdue tasks\n"
              "8 - save tasks to file\n"
              "Your choice: ")


def start():
    global all_tasks
    all_tasks = task_manager.get_all_tasks()
    if len(all_tasks) == 0:
        first_task()

    while True:
        try:
            point = int(input(menu_items))
        except TypeError:
            print("Enter a number of prefer option)")
            continue
        if point == 0:
            print("Bye, sunshine) See u later 😘")
            break
        if 0 < point >= 8:
            print("...\nTry again, sweety)")
            return
        main_block(point)


start()
# all_tasks = task_manager.get_all_tasks()
# print(type(all_tasks))
