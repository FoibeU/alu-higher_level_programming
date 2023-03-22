#!/usr/bin/python3
"""
Check if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """Same class or inherit from
    Args:
        obj (Object): object of a class
        a_class (class): a specific class
    Returns:
        True: Same class or inherit from
        False: Not the same
    """
    if isinstance(obj, a_class):
        return True
    return False
