#!/usr/bin/python3

"""Function that returns the list of
    available attributes and methods of an object:
"""


def lookup(obj):
    """List available attributes and methods of an object
    Args:
        obj (object): object to list its attributes and methods
    Returns:
        a list object
    """
    return (dir(obj))
