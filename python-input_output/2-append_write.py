#!/usr/bin/python3

"""Appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    Args:
        filename (str): name of the file to write
        text (str): text to append to the file
    Returns:
        number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        characterAdded = file.write(text)
        return characterAdded
