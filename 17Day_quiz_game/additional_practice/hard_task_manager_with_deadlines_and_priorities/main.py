import data
import get_methods
import process_methods

menu_items = ("What you may to do (enter the number of chose option):\n"
              "0 - escape? 😈\n"
              "1 - create new task\n"
              "2 - find exact task\n"
              "3 - change existing task\n"
              "4 - delete task (are you sure?)\n"
              "5 - get all tasks\n"
              "6 - sort tasks by deadlines\n"
              "7 - get all overdue tasks\n"
              "8 - get archive tasks\n"
              "9 - save tasks to file\n"
              "Your choice: ")


def first_task():
    print("Let's start with the first task in our workspace!")
    ans = input("Would you like to create your first task? y/n: ").lower()
    if ans == 'y':
        process_methods.add_new_task()
        return
    print('What a pitiful situation... What else you can do in Task Manager program without tasks 🤔.')
    exit()



def main_block(point):
    if point == 1:
        process_methods.add_new_task()
    elif point == 2:
        process_methods.find_the_task()
    elif point == 3:
        process_methods.change_existing_task()
    elif point == 4:
        process_methods.delete_task()
    elif point == 5:
        process_methods.receive_all_tasks(True)
    elif point == 6:
        process_methods.receive_sorted_tasks()
    elif point == 7:
        process_methods.receive_all_overdue_tasks(True)
    elif point == 8:
        process_methods.receive_archive_tasks()
    else:
        process_methods.save_tasks()


def start():

    while True:
        try:
            point = int(input(menu_items))
        except TypeError:
            print("Enter a number of prefer option)")
            continue
        if point == 0:
            print("Bye, sunshine) See u later 😘")
            break
        if 0 < point >= 10:
            print("...\nTry again, sweety)")
            continue
        main_block(point)


first_task()
start()
