#!/usr/bin/python3
"""
    Representation of the class MyList that inherits from list
"""


class MyList(list):
    """Class that inherits fron list object"""

    def print_sorted(self):
        """Sorted list in ascending order
        Returns:
                list: list in sorted order
        """
        print(sorted(self))
