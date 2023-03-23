#!/usr/bin/python3

"""JSON representation of an object"""


import json


def to_json_string(my_obj):
    """Converts object to json string
    Args:
        my_obj (object): object to serialize
    Returns:
        JSON representation of an object
    """
    return json.dumps(my_obj)

