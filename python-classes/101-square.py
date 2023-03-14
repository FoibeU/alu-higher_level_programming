#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square
        Args:
            size (int): size of the square
            position (tuple): position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """property getter: retrive the value of size.
        Returns:
            int: the set instance attribute.
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

    @property
    def position(self):
        """property getter: retrive the value of position.
        Returns:
            int: the set instance attribute.
        position.setter: set the value of self.__position.
        It also checks for TypeError.
        Args:
            value (tuple): value to initialize self.__position with.
        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates the area of the current square.
        Returns:
            int: the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Printsro stdout the square with the character #"""

        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        for x in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")
            for z in range(self.__size):
                print("#", end="")
            print("")

    def __str__(self):
        """Defines the Printing of a square"""

        if self.__size != 0:
            for i in range(self.__position[1]):
                print("")

        for x in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")
            for z in range(self.__size):
                print("#", end="")
            if x != self.__size - 1:
                print("")
        return ""
