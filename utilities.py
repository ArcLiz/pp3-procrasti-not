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

# MAIN_MENU = """Boxed text"""

# MANAGER_HEADER = """Boxed text"""

# MANAGER_EMPTY = """Boxed text"""

# EDIT_HEADER = """Boxed text"""
