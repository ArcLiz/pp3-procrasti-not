"""
Main module including an initial welcome function,
the user handbook and the main().
"""
import time
from colorama import Fore

from utilities import clear, INIT_TXT
from tasks import setup_menu

WELCOME = " ________________________________\
___________________________________" + """
|                                                                   |
|   Greetings, {name}! It is a pleasure to meet you.
|                                                                   |
|   I am your friendly neighborhood Procrasti - Not, a tool made    |
|   to help you manage your daily tasks. I personally feel that     |
|   'tool' has a negative ring to it, I'd much rather you call me   |
|                                                                   |
|                           ..a friend!                             |
|___________________________________________________________________|"""


def welcome():
    """
    Function to welcome the user where they can
    begin using the app or get further instructions
    """
    clear()

    # Ask for user's name and validate the input
    while True:
        print(INIT_TXT)
        name = input(
            "\nBefore we begin,"
            f"{Fore.GREEN} \n\nWhat would you like me to call you?"
            f"{Fore.RESET}\n> ")
        if len(name.strip()) >= 1:
            break
        else:
            print(f"{Fore.RED} Invalid input!{Fore.RESET}")
            time.sleep(1)
            clear()

    clear()

    print(
        " ___________________________________________________________________"
        "\n"
        "|                                                                   |"
        "\n"
        f"|   Greetings, {name}! It is a pleasure to meet you.\n"
        "|                                                                   |"
        "\n"
        "|   I am your friendly neighborhood Procrasti - Not, a tool made    |"
        "\n"
        "|   to help you manage your daily tasks. I personally feel that     |"
        "\n"
        "|   'tool' has a negative ring to it, I'd much rather you call me   |"
        "\n"
        "|                                                                   |"
        "\n"
        "|                           ..a friend!                             |"
        "\n"
        "|___________________________________________________________________|"
        )

    print(
        f"\n{Fore.GREEN}Do you want to know more about the services"
        " I can offer you \nbefore we start setting up your To Do list?"
        f"{Fore.CYAN} (y/n){Fore.RESET}")

    while True:
        handbook = input("> ").lower()
        if handbook == 'y':
            display_handbook()
            break
        elif handbook == 'n':
            print('Great! Let us get started on building your "To Do - list".')
            time.sleep(2)
            clear()
            break
        else:
            print(f"{Fore.RED}Invalid input!{Fore.RESET}")
            time.sleep(2)
    clear()
    setup_menu()


def display_handbook():
    """
    A detailed explanation on how the app works.
    """
    clear()

    print(
        " ___________________________________________________________________"
        "\n"
        "|                                                                   |"
        "\n"
        "|            A Beginners Guide to Sir Procrasti - Not               |"
        "\n"
        "|                                                                   |"
        "\n"
        "|   Have you ever had one of those days where you have so many      |"
        "\n"
        "|   things on your to do list, that you end up not doing a single   |"
        "\n"
        "|   one? I know that I have. Sir Procrasti - Not is here to help.   |"
        "\n"
        "|                                                                   |"
        "\n"
        "|   It's all super simple. Just;                                    |"
        "\n"
        "|   1. Add your planned tasks to your To Do list                    |"
        "\n"
        "|   2. Start ticking of items on your list!                         |"
        "\n"
        "|                                                                   |"
        "\n"
        "|   Sir Procrasti - Not will randomly chose a task from your list   |"
        "\n"
        "|   that you are to complete, before moving on. When you're         |"
        "\n"
        "|   finished with the decided on task, Sir Procrasti - Not will be  |"
        "\n"
        "|   the one cheering you on to keep going!                          |"
        "\n"
        "|                                                                   |"
        "\n"
        "|   And who knows, maybe he has a few wise words to share, to       |"
        "\n"
        "|   keep your spirits up throughout the day.                        |"
        "\n"
        "|                                                                   |"
        "\n"
        "|                           Good Luck!                              |"
        "\n"
        "|___________________________________________________________________|"
        )
    input(f"{Fore.GREEN}\nPress enter to begin..{Fore.RESET}")
    clear()
    setup_menu()


def main():
    """
    The main function controlling how the app runs.
    """
    welcome()


main()
