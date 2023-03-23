#!/usr/bin/python3
"""Define an empty BaseGeometry class"""


class BaseGeometry:
    """An empty class"""

    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer value
        Args:
            name (str): name of the value
            value (int): the value passed
         Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
