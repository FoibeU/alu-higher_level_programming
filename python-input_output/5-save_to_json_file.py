#!/usr/bin/python3
"""Save Object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation
    Args:
        my_obj (object): object to write to a file
        filename (str): name of the file to write to
    """
    with open(filename, "w", encoding="utf-8") as file:
        json_text = json.dumps(my_obj)
        file.write(json_text)
