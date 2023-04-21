"""
The function that welcomes the user
and presents the user with a quick app introduction
"""
import os


def clear():
    """
    Clearing the terminal to reduce
    information amount
    """
    os.system('cls' if os.name == 'nt' else 'clear')


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


MANAGER_HEADER = """
 ___________________________________________________________________
|                                                                   |
|                    Hocus Pocus, give us Focus!                    |
|                                                                   |
|   Welcome to the Task Managing, the job for which I was created.  |
|                                                                   |
|   We shall now begin with choosing one of your tasks, at random.  |
|   Once you've completed your task, I will choose another one.     |
|                                                                   |
|   When all the tasks are done, we'll be celebrating together.     |
|___________________________________________________________________|
"""


MANAGER_EMPTY = """
 ___________________________________________________________________
|                                                                   |
|                    Something went wrong!                          |
|                                                                   |
|   It seems you have yet to add items to your To Do list.          |
|___________________________________________________________________|
"""


MANAGER_ENCOURAGE = """
 ___________________________________________________________________
|                                                                   |
|                       We must remedy this!                        |
|                                                                   |
|     We shall not be beaten by negative thoughts or feelings.      |
|___________________________________________________________________|
"""


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


COMPLETED_HEADER = """
 ___________________________________________________________________
|                                                                   |
|            Congratulations on completing your tasks!              |
|                                                                   |
|   You've been a complete champion throughout these tasks,         |
|   Let me tell you!                                                |
|___________________________________________________________________|
"""

encouragement_choices = [
    "Great job!",
    "Wow, you're killing it!",
    "Yees, let's go!",
    "Give that maaan a cookie!"]
