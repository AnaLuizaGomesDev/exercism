"""Module providing a function printing python version."""
import sys

def print_python_version():
    """Function printing python version."""
    print(sys.version)

def leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0
