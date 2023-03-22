#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
    Args:
        obj (Object): object of a class
        a_class (class): a specific class
    Returns:
        True if it's a subclass of a class
        False if otherwise
    """
    if issubclass(type(obj), a_class) and (type(obj) is not a_class):
        return True
    return False
