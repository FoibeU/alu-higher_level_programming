#!/usr/bin/python3
"""
    Define a Rectangle class with width and height
"""


class Rectangle:
    """Representation of a Rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with optional width and heigth.
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width property getter: retrieve the wdith of the class.
        Returns:
            width (int): the width instance attribute
        width.setter: set the width of the class.
        it also checks for TypeError and ValueError.
        Args:
            value (int): value to set the width to
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height property getter: retrieve the height of the class.
        Returns:
            height (int): the height instance attribute
        height.setter: set the height of the class.
        it also checks for TypeError and ValueError.
        Args:
            value (int): value to set the height to
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area of a rectangle.
        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.
        Returns:
            int: perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """printable representation of the rectangle class.
        Returns:
            str: print the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for x in range(self.__height):
            for y in range(self.__width):
                rect.append("#")
            # append new line until the last value of height
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Produce string representation of the class Rectangle.
        Returns:
            str: representation of the class
        """
        return f"Rectangle({str(self.__width), {str(self.__height)}})"

    def __del__(self):
        """Prints a message when a rectangle is deleted and decrement number of instances by 1"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
