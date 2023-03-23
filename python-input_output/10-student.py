#!/usr/bin/python3

"""A representation of a Student class"""


class Student:
    """Class that defines Student"""

    def __init__(self, first_name, last_name, age):
        """Insantiate a Student object
        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student objects
        If attrs is a list of strings, only attribute names
        contained in this list are retrieved.
        Args:
            attrs (list): attributes to retrieve
        """
        if type(attrs) is list:
            if all(type(item) is str for item in attrs):
                return {key: getattr(self, key)
                        for key in attrs if hasattr(self, key)}
        return self.__dict__
