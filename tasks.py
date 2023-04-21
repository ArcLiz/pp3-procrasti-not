"""
All functions that controls task management,
e.g. vieweing, adding, removing, updating and doing tasks
"""
import time
import random
import sys

from utilities import MANAGER_HEADER, MANAGER_EMPTY, encouragement_choices
from utilities import clear, MAIN_MENU, EDIT_HEADER, COMPLETED_HEADER

todo_list = []
completed_tasks = []


def setup_menu():
    """
    The main menu from which the user sets up their list.
    From here they can also access the edit menu
    """
    global todo_list
    first_time = True
    menu_text = f"""{MAIN_MENU}

Choose from the below alternatives:
1. View, Edit or Delete tasks in my list
2. Start working through my tasks\n"""

    while True:
        if first_time:
            print(f"""{menu_text}
Or add a new task to your list by writing it below.
e.g. 'Do the dishes'""")
            first_time = False

        action = input('> ')

        if action == '0':
            clear()
            print(f"""{menu_text}
Pff, trying to test me with the 0-escape so soon?! Welp, nothing happened. :)
Add a new task below or chose from the alternatives above to proceed.""")

        elif action == '1':
            clear()
            edit_tasks()

        elif action == '2':
            clear()
            task_manager()

        else:
            todo_list.append(action)
            clear()
            print(f"""{menu_text}
{action} was added to your list.
Add a new task below or chose from the alternatives above to proceed.""")
            continue


def edit_tasks():
    """
    The menu in which users can edit or delete tasks from their list.
    """
    global todo_list

    while True:
        # Print the current list
        print(EDIT_HEADER)
        for i, task in enumerate(todo_list):
            print(f"{i+1}. {task}")

        # Ask the user which index to edit or delete
        index = int(input("""
Enter the index of the task you want to edit or
delete (0 to exit):\n> """)) - 1

        # Exit if the user enters 0
        if index == -1:
            clear()
            setup_menu()
            break

        # Ensure the index is valid
        if index < 0 or index >= len(todo_list):
            print("Invalid index, please try again.")
            continue

        # Ask the user whether to edit or delete the task
        action = input("Do you want to (e)dit or (d)elete the task?\n> ")

        if action == 'e':
            # Edit the task
            new_task = input("Enter the new task:\n> ")
            todo_list[index] = new_task
            clear()
            print(EDIT_HEADER)
            print(f"Task {index+1} updated.")
        elif action == 'd':
            # Delete the task
            del todo_list[index]
            clear()
            print(EDIT_HEADER)
            print(f"Task {index+1} deleted.")
        else:
            print("Invalid input, please try again.")
            continue

        # Print the updated list
        print("\nUpdated To Do List:")
        for i, task in enumerate(todo_list):
            print(f"{i+1}. {task}")

        # Ask the user whether to continue editing or exit
        action = input("\nDo you want to continue editing tasks? (y/n)\n> ")
        if action == 'y':
            clear()
            edit_tasks()
        else:
            clear()
            setup_menu()
            break


def task_manager():
    """
    The main task managing function incl. randomizing tasks,
    completion counter and cheering on the user.
    """
    global todo_list
    global completed_tasks
    print(f"""{MANAGER_HEADER}

The task chosen is....""")
    while True:
        # Chosing a random task
        time.sleep(2)
        if todo_list:
            next_task = random.choice(todo_list)

            print(f"""\n{next_task}\n
Once done, you have {len(todo_list)-1} tasks left to complete.\n""")
        else:
            clear()
            print(MANAGER_EMPTY)
            input("""In order to start working through your To do list,
you'll need to go back to my main menu and start adding tasks.

Press enter to go back and setup your To Do list.""")
            clear()
            setup_menu()
            break

        # Mark a task as completed and add to completed_list
        completed = input("Have you completed this task? (y/n)\n> ").lower()

        if completed == "y":
            todo_list.remove(next_task)
            completed_tasks.append(next_task)
            clear()
            encouragement = random.choice(encouragement_choices)
            print(MANAGER_HEADER)

            if len(todo_list) != 0:
                print(f"""{encouragement}

You're doing really great.

Let's see what your next task is...""")
                time.sleep(2)
            else:
                clear()
                tasks_complete()
                break
        else:
            print("---STILL A WORK IN PROGRESS---")


def tasks_complete():
    """
    The final "screen", congratulating the user on finishing their list.
    Giving options to quit app or restart to set up a new list.
    """
    global completed_tasks

    print(COMPLETED_HEADER)
    print("You managed to complete all of these tasks:\n")
    for i, task in enumerate(completed_tasks):
        print(f"{i+1}. {task}")

    print("\nYou should be as proud of yourself as I am.")

    while True:
        up_next = input("""
Now, would you like to set up a new To Do list? (y/n)\n> """).lower() == "y"

        if up_next:
            completed_tasks = []
            clear()
            setup_menu()
            break
        else:
            print("Goodbye!")
            time.sleep(3)
            clear()
            sys.exit(0)
    return
