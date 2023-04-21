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
            edit_tasks()

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


def edit_tasks():
    """
    Function to manage tasks in the todo_list global variable
    """
    global todo_list

    while True:
        # Print the current list
        print("BIG BOX TEXT")
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
            print("BIG BOX TEXT")
            print(f"Task {index+1} updated.")
        elif action == 'd':
            # Delete the task
            del todo_list[index]
            clear()
            print("BIG BOX TEXT")
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
