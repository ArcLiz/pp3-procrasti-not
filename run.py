"""
Main module including an initial welcome function,
the user handbook and the main().
"""
from utilities import clear
# from tasks import setup_menu


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

    # should go to setup_menu()
    print("Testing functionality")


def display_handbook():
    """
    A detailed explanation on how the app works.
    """
    clear()

    print("""
Long block text of How the app works
""")
    input("Press enter to begin..")
    clear()
    # Should go to setup_menu() in time
    print("Test Test")


def main():
    """
    The main function controlling how the app runs.
    """
    welcome()


main()
