#!/usr/bin/python3
"""
Checks if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Exact same object
    Args:
        obj (Object): object of a class
        a_class (class): a specific class
    Returns:
        True: if the object is exactly an instance of the specified class
        False: Not the same
    """
    if type(obj) is a_class:
        return True
    return False
