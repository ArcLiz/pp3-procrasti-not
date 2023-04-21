"""
All functions that controls task management,
e.g. vieweing, adding, removing, updating and doing tasks
"""
# from utilities import MANAGER_HEADER, MANAGER_EMPTY, MAIN_MENU, EDIT_HEADER
from utilities import clear

todo_list = []
# completed_tasks = []


def setup_menu():
    """
    The main menu from which the user sets up their list.
    From here they can also access the edit menu
    """
    global todo_list
    first_time = True
    menu_text = """Some big fancy text box

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
            # to edit_tasks()
            print("Testing edit tasks location")

        elif action == '2':
            clear()
            # to task_manager()
            print("Testing task manager location")

        else:
            todo_list.append(action)
            clear()
            print(f"""{menu_text}
{action} was added to your list.
Add a new task below or chose from the alternatives above to proceed.""")
            continue


# def edit_tasks():
# """
# The menu in which users can edit or delete tasks from their list.
# """


# def task_manager():
# """
# The main task managing function incl. randomizing tasks,
# completion counter and cheering on the user.
# """


# def tasks_complete():
# """
# The final "screen", congratulating the user on finishing their list.
# Giving options to quit app or restart to set up a new list.
# """
