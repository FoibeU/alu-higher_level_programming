#!/usr/bin/python3

"""Defines a square."""


class Square:
    """Representation of Square class"""

    def __init__(self, size=0):
        """Initialize a square
        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Get/set size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Finds area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Defines the == comparison opeartor of two squares"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the != comparison opeartor of two squares"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Defines the > comparison opeartor of two squares"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the >= comparison opeartor of two squares"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Defines the < comparison opeartor of two squares"""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison opeartor of two squares"""
        return self.area() <= other.area()
