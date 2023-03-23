#!/usr/bin/python3

"""Defines a class-to-JSON function"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure
    Args:
        obj (object): a simple data structure
    Returns:
        Dictionary representation of obj
    """
    return obj.__dict__
