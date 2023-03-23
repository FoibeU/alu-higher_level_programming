#!/usr/bin/python3
"""
Reads a text file
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.
    Args:
        filename (str): name of the file to read
    """

    with open(filename, encoding="utf-8") as file:
        read_file = file.read()
    print(read_file, end="")
