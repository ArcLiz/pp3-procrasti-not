"""
Main module including an initial welcome function,
the user handbook and the main().
"""
from utilities import clear
# from tasks import setup_menu


# def welcome():
# """
# Welcoming the user to the app, offering further
# information or a way to begin list setup.
# """


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
    print("I work, for now")


# def main():
# """
# The main function controlling how the app runs.
# """
