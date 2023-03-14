#!/usr/bin/python3

"""Defines a square."""


class Square:
    """Representation of Square class"""

    def __init__(self, size=0):
        """Initialize a square
        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """property getter: retrive the value of size.
        Returns:
            int: the size instance attribute.
        size.setter: set the value of self.__size.
        It also checks for TypeError and ValueError.
        Args:
            value (int): value to initialize self.__size with.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is lesser than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square.
        Returns:
            int: the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for x in range(self.__size):
            for y in range(self.__size):
                print("{}".format("#"), end="")
            print()
