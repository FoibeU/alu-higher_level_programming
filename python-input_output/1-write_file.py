#!/usr/bin/python3

"""Writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)
    Args:
        filename (str): name of the file to write
        text (str): text to write to the file
    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        characterWritten = file.write(text)
        return characterWritten
