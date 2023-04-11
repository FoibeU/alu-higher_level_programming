#!/usr/bin/python3
"""Representation of a Base class with its attributes"""

import json
import csv
import turtle


class Base:
    """Define a class Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """A class with private class attributes.
        def __init__: initialize class Base
        Args:
            id (int): id of an instance of class Base
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts dictionary to JSON string representation
        Args:
            list_dictionaries (dict): List of dictionaries
        Returns:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file.
        Args:
            cls (class): current class using the method
            list_objs (list): is a list of instances who inherits of Base
        """

        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [list.to_dictionary() for list in list_objs]
                file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Converts JSON string to dictionary representation
        Args:
            json_string (dict): JSON string representation
        Returns:
            JSON string representation of json_string
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Assign dictionary values to Instances
        Args:
            **dictionary (dict): list of dictionary
        Returns:
            an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_values = cls(1, 1)
            else:
                new_values = cls(1)
            new_values.update(**dictionary)
            return new_values

    @classmethod
    def load_from_file(cls):
        """Assign value from file to instances
        Args:
            cls (class): current class using the method
        Returns:
            an empty list, otherwise
            a list of instances
        """
        filename = str(cls.__name__) + ".json"

        try:
            with open(filename, encoding="utf-8") as file:
                json_dict = cls.from_json_string(file.read())
                return [cls.create(**jd) for jd in json_dict]
        except IOError:
            return "[]"

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write representation of list_objs to a file csv.
        Args:
            cls (class): current class using the method
            list_objs (list): a list of instances inherited from Base
        """
        filename = str(cls.__name__) + ".csv"

        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".csv"

        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return "[]"

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.forward(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

