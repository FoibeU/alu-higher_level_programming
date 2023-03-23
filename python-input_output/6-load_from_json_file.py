#!/usr/bin/python3

"""Create object from a JSON file"""

import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”
    Args:
        filename (str): name of the file to
    """
    with open(filename, encoding="utf-8") as file:
        json_text = file.read()
        return json.loads(json_text)
