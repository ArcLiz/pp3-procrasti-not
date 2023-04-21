"""
Main module including an initial welcome function,
the user handbook and the main().
"""
from utilities import clear
from tasks import setup_menu


def welcome():
    """
    Function to welcome the user where they can
    begin using the app or get further instructions
    """
    print("Hello there!\n")
    name = input("Before we begin, what would you like me to call you?\n> ")

    clear()

    print(f"Greetings, {name}. It is a pleasure to meet you.\n")
    print("""I am your friendly neighborhood Procrasti-Not,
a tool created to help you manage your daily tasks.""")

    while True:
        handbook = input("""
Do you want to know more about the services I can offer you
before we start setting up your To Do list? (y/n)\n> """).lower()
        if handbook == 'y':
            display_handbook()
            break
        elif handbook == 'n':
            print('Great! Let us get started on building your "To Do-list".')
            clear()
            break
        else:
            print("Invalid input, please enter 'y' or 'n\n> ")

    setup_menu()


def display_handbook():
    """
    A detailed explanation on how the app works.
    """
    clear()

    print("""
 ___________________________________________________________________
|                                                                   |
|            A Beginners Guide to Sir Procrasti-Not                 |
|                                                                   |
|   Have you ever had one of those days where you have so many      |
|   things on your to do list, that you end up not doing a single   |
|   one? I know that I have. Sir Procrasti-Not is here to help.     |
|                                                                   |
|   It's all super simple. Just;                                    |
|   1. Add your planned tasks to your To Do list                    |
|   2. Start ticking of items on your list!                         |
|                                                                   |
|   Sir Procrasti-Not will randomly chose a task from your list     |
|   that you are to complete, before moving on. When you're         |
|   finished with the decided on task, Sir Procrasti-Not will be    |
|   the one cheering you on to keep going!                          |
|                                                                   |
|   And who knows, maybe he has a few wise words to share, to       |
|   keep your spirits up throughout the day.                        |
|                                                                   |
|                           Good Luck!                              |
|___________________________________________________________________|
""")
    input("Press enter to begin..")
    clear()
    setup_menu()


def main():
    """
    The main function controlling how the app runs.
    """
    welcome()


main()
