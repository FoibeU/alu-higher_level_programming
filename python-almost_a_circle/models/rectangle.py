#!/usr/bin/python3
"""Representation of Rectangle class inherits from Base class"""

from models.base import Base


class Rectangle(Base):
    """Defines Rectangle class with its attributes
    Args:
        Base (Class): Class inherits from
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle with optional width and height
        Args:
            width  (int): width of the rectangle
            height (int): height of the rectangle
            x (int): horizontal coordinate of the rectangle
            y (int): vertical coordinates of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width property getter: retrieve the width of the class.
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
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height property getter: retrieve the height of the class.
        Returns:
            height (int): the height instance attribute
        height.setter: set the height of the class
        it also checks for TypeError and valueError
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
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x property getter: retrieve the x of the class
        Returns:
            x (int): the x instance of the class
        x.setter: set the x of the class
        it also checks for TypeError and ValueError
        Args:
            value (int): value to set the x to
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y property getter: retrieve the y of the class
        Returns:
            y (int): the y instance of the class
        y.setter: set the y of the class
        it also checks for TypeError and ValueError
        Args:
            value (int): value to set the y to
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes area of the rectangle.
        Returns:
            Area value of the rectangle instances
        """
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle with the character #."""
        for x in range(self.__y):
            print()

        for y in range(self.__height):
            for z in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def __str__(self):
        """Represents rectangle string to the stdout"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update rectangle class instance attributes
        Args:
            *args (tuple): list of arguements
            *kwargs (dict): key and values of attributes
        *args is the list of arguments:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """

        attrs = ["id", "width", "height", "x", "y"]
        index = 0

        if args is not None and len(args) > 0:
            for arg in args:
                if index < 5:
                    setattr(self, attrs[index], arg)
                    index += 1
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Convert Rectangle instance to dictionary representation"""
        return ({
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        })
    # def to_dictionary(self):
    #     dict_list = ['x', 'y', 'id', 'height', 'width']
    #     dictionary = {}
    #     for i in dict_list:
    #         dictionary[i] = getattr(self, i)
    #     return dictionary
