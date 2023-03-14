#!/usr/bin/python3
"""
    Define a Rectangle class with width and height
"""


class Rectangle:
    """Representation of a Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with optional width and heigth.
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

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
