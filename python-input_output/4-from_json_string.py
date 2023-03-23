#!/usr/bin/python3

"""Python (Object) representation of a JSON"""


import json


def from_json_string(my_str):
    """Converts json string to python object
    Args:
        my_str (object): json to deserialize
    Returns:
        object (Python data structure)
    """
    return json.loads(my_str)
