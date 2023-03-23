#!/usr/bin/python3

"""A representation of a Student class"""


class Student:
    """Class that defines Student"""

    def __init__(self, first_name, last_name, age):
        """Insantiate Student object
        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student objects"""
        return self.__dict__
