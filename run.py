"""
Main module including an initial welcome function,
the user handbook and the main().
"""
from colorama import Fore

from utilities import clear
from tasks import setup_menu


def welcome():
    """
    Function to welcome the user where they can
    begin using the app or get further instructions
    """
    clear()
    print("""\
 ___________________________________________________________________
|                                                                   |
|          Hello there, stranger! Do you come in peace?             |
|                                                                   |
|                          ¯\_(^^)_/¯                               |
|___________________________________________________________________|""")
    name = input("\nBefore we begin, " + Fore.GREEN + """

What would you like me to call you?""" + Fore.RESET + "\n> ")

    clear()

    print(f"""\
 ___________________________________________________________________
|                                                                   |
|   Greetings, {name}! It is a pleasure to meet you.          
|                                                                   |
|   I am your friendly neighborhood Procrasti - Not, a tool made    |
|   to help you manage your daily tasks. I personally feel that     |
|   "tool" has a negative ring to it, I'd much rather you call me   |
|                                                                   |
|                           ..a friend!                             |
|___________________________________________________________________|""")

    while True:
        handbook = input(Fore.GREEN + """
Do you want to know more about the services I can offer you
before we start setting up your To Do list?""" + Fore.CYAN + """ (y/n)
""" + Fore.RESET + "> ").lower()
        if handbook == 'y':
            display_handbook()
            break
        elif handbook == 'n':
            print('Great! Let us get started on building your "To Do - list".')
            clear()
            break
        else:
            print(Fore.RED + "Invalid input, please enter 'y' or 'n" + """
> """ + Fore.RESET)

    setup_menu()


def display_handbook():
    """
    A detailed explanation on how the app works.
    """
    clear()

    print(Fore.RESET + """\
 ___________________________________________________________________
|                                                                   |
|            A Beginners Guide to Sir Procrasti - Not               |
|                                                                   |
|   Have you ever had one of those days where you have so many      |
|   things on your to do list, that you end up not doing a single   |
|   one? I know that I have. Sir Procrasti - Not is here to help.   |
|                                                                   |
|   It's all super simple. Just;                                    |
|   1. Add your planned tasks to your To Do list                    |
|   2. Start ticking of items on your list!                         |
|                                                                   |
|   Sir Procrasti - Not will randomly chose a task from your list   |
|   that you are to complete, before moving on. When you're         |
|   finished with the decided on task, Sir Procrasti - Not will be  |
|   the one cheering you on to keep going!                          |
|                                                                   |
|   And who knows, maybe he has a few wise words to share, to       |
|   keep your spirits up throughout the day.                        |
|                                                                   |
|                           Good Luck!                              |
|___________________________________________________________________|
""")
    input(Fore.GREEN + "Press enter to begin.." + Fore.RESET)
    clear()
    setup_menu()


def main():
    """
    The main function controlling how the app runs.
    """
    welcome()


main()
