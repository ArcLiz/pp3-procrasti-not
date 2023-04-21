"""
Module containing general utilities
in addition to large formatted text segments
"""
import os


def clear():
    """
    Clearing the terminal to reduce
    information amount
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# encouragement_choices = []

MAIN_MENU = """
 ___________________________________________________________________
|                                                                   |
|            Welcome to Sir Procrasti-Not's Main Menu               |
|                                                                   |
|   From here you have access to all you'll need for your day.      |
|   You can add new tasks to your task list by simply writing the   |
|   task and press enter, or you can chose one of the options in    |
|   the list below.                                                 |
|                                                                   |
|   Remember! Wherever you are within the program, you can press    |
|   0 and enter to get back to this menu.     Happy Tasking!        |
|___________________________________________________________________|
"""


# MANAGER_HEADER = """Boxed text"""

# MANAGER_EMPTY = """Boxed text"""

EDIT_HEADER = """
 ___________________________________________________________________
|                                                                   |
|                        Bippety Boppety Boop                       |
|                                                                   |
|   This is the menu for viewing, editing and deleting your tasks.  |
|                                                                   |
|   Your current To Do list and all it's functions are shown below. |
|___________________________________________________________________|
"""
