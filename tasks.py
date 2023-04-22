"""
All functions that controls task management,
e.g. vieweing, adding, removing, updating and doing tasks
"""
import time
import random
import sys

from colorama import Fore

from utilities import MANAGER_HEADER, MANAGER_EMPTY, encouragement_choices
from utilities import clear, MAIN_MENU, EDIT_HEADER, COMPLETED_HEADER
from utilities import MANAGER_ENCOURAGE

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
{Fore.GREEN}1. View, Edit or Delete tasks in my list
2. Start working through my tasks\n"""

    while True:
        if first_time:
            print(f"""{menu_text}
Or add a new task to your list by writing it below.
e.g. 'Do the dishes'{Fore.RESET}""")
            first_time = False

        action = input('> ')

        if action == '0':
            clear()
            print(f"""{menu_text} {Fore.MAGENTA}
Pff, trying to test me with the 0-escape so soon?! Welp, nothing happened. :)
Add a new task below or chose from the alternatives above to proceed.\
    {Fore.RESET}""")

        elif action == '1':
            clear()
            edit_tasks()

        elif action == '2':
            clear()
            task_manager()

        else:
            todo_list.append(action)
            clear()
            print(f"""\
{menu_text}
{Fore.CYAN}{action} {Fore.GREEN}was added to your list.
Add a new task below or choose from the alternatives above to proceed.\
{Fore.RESET}""")
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
        try:
            index = int(input(f"""{Fore.GREEN}
Enter the index of the task you want to edit or
delete {Fore.CYAN}(0 to exit){Fore.RESET}\n> """)) - 1
        except ValueError:
            print(f"""{Fore.RED}
Invalid input, please enter a valid index.{Fore.RESET}""")
            time.sleep(2)
            clear()
            continue

        # Exit if the user enters 0
        if index == -1:
            clear()
            setup_menu()
            break

        # Ensure the index is valid
        if index < 0 or index >= len(todo_list):
            print(f"""{Fore.RED}
Invalid index, please try again.{Fore.RESET}""")
            time.sleep(2)
            clear()
            continue

        # Ask the user whether to edit or delete the task
        xyz = "Do you want to (e)dit or (d)elete the task?"
        prompt = f"""{Fore.GREEN}\
{xyz[:15]}{Fore.CYAN}(e){Fore.GREEN}dit or {Fore.CYAN}(d)\
{Fore.GREEN}{xyz[28:]}{Fore.RESET}"""

        action = input(f"""{prompt}\n> """)

        if action == 'e':
            # Edit the task
            new_task = input(f"""{Fore.GREEN}Enter the new task:
{Fore.RESET}> """)
            todo_list[index] = new_task
            clear()
            print(EDIT_HEADER)
            print(f"{Fore.CYAN}Task {index+1} updated.{Fore.RESET}")
        elif action == 'd':
            # Delete the task
            del todo_list[index]
            clear()
            print(EDIT_HEADER)
            print(f"{Fore.CYAN}Task {index+1} deleted.{Fore.RESET}")
        elif action == '0':
            clear()
            setup_menu()
        else:
            print(f"{Fore.RED}Invalid input, please try again.{Fore.RESET}")
            continue

        # Print the updated list
        print("\nUpdated To Do List:")
        for i, task in enumerate(todo_list):
            print(f"{i+1}. {task}")

        # Ask the user whether to continue editing or exit
        action = input(f"""
{Fore.GREEN}Do you want to continue editing tasks?{Fore.CYAN} (y/n)
{Fore.RESET}> """)
        if action == 'y':
            clear()
            edit_tasks()
        elif action == '0':
            clear()
            setup_menu()    
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

    while True:
        print(f"""{MANAGER_HEADER}

The task chosen is....""")
        # Chosing a random task
        if todo_list:
            next_task = random.choice(todo_list)

            print(f"""\n{Fore.CYAN}{next_task}
{Fore.RESET}
Once done, you have {len(todo_list)-1} task(s) left to complete.""")
        else:
            clear()
            print(MANAGER_EMPTY)
            input(f"""In order to start working through your To do list,
you'll need to go back to my main menu and start adding tasks.
{Fore.GREEN}
Press enter to go back and setup your To Do list.{Fore.RESET}""")
            clear()
            setup_menu()
            break

        # Mark a task as completed and add to completed_list
        completed = input(f"""{Fore.GREEN}
Have you completed this task?{Fore.CYAN} (y/n)
{Fore.RESET}> """).lower()

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
                time.sleep(3)
            else:
                clear()
                tasks_complete()
                break
        if completed == "n":
            while True:
                clear()
                print(MANAGER_ENCOURAGE)
                print(f"""
Oof, come on my friend!
You can do it, I'm completely sure of it.

All I can offer at this point are these alternatives
{Fore.GREEN}
1. Temporarily skip this task (shuffle new)
2. Permanently skip this task (delete)
3. Quit ProcrastiNot

{Fore.RESET}Which one suits you best?""")

                choice = input("> ")
                if choice == "1":
                    random.shuffle(todo_list)
                    next_task = todo_list[0]
                    print("""That's completely fine.

Let's skip this task for now and try the next one.""")
                    time.sleep(3)
                    clear()
                    break
                elif choice == "2":
                    todo_list.remove(next_task)
                    print(f"""
{Fore.CYAN}{next_task} {Fore.GREEN}was removed from your list.

{Fore.RESET}Loading a new task..""")
                    time.sleep(3)
                    clear()
                    break
                elif choice == "3":
                    agree = input(f"""{Fore.RED}\
Are you sure? This can not be reversed. {Fore.CYAN}(y/n)
{Fore.RESET}> """).lower() == "y"
                    if agree:
                        print(f"{Fore.MAGENTA}Goodbye!{Fore.RESET}")
                        time.sleep(3)
                        clear()
                        sys.exit(0)
                elif choice == "0":
                    clear()
                    setup_menu()
                else:
                    print(f"{Fore.RED}Invalid input!{Fore.RESET}")
                    time.sleep(2)
                    continue
        elif completed == "0":
            clear()
            setup_menu()
        else:
            clear()


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
        up_next = input(f"""{Fore.GREEN}
Now, would you like to set up a new To Do list? {Fore.CYAN}(y/n)
{Fore.RESET}> """).lower()

        if up_next == "y":
            completed_tasks = []
            clear()
            setup_menu()
            break
        elif up_next == "0":
            clear()
            setup_menu()
        else:
            print(f"{Fore.MAGENTA}Goodbye!{Fore.RESET}")
            time.sleep(3)
            clear()
            sys.exit(0)
