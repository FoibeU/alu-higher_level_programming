#!/usr/bin/python3

"""Defines a class Node that defines a node of a singly linked list"""


class Node:
    """A node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Create a new node
        Args:
            data (int): The data to be added to the node.
            next_node (Node): pointer to the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """property getter: retrive the value of data.
        Returns:
            int: the data instance attribute.
        size.setter: set the value of self.__data.
        It also checks for TypeError.
        Args:
            value (int): value to initialize self.__data with.
        Raises:
            TypeError: if value is not an integer.
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """property getter: retrive the value of next_node.
        Returns:
            node: the next_node instance attribute.
        size.setter: set the value of self.__next_node.
        It also checks for TypeError.
        Args:
            value (node): value to initialize self.__next_node with.
        Raises:
            TypeError: if value is not a node object.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defines a singly linked list"""


class SinglyLinkedList:
    """A singly linked list"""

    def __init__(self):
        """Constructor for SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node to the singly linked list
        The node is inserted at an ordered position in the list
        Args:
            value (Node): The node to insert
        """

        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head

            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node

            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Defines the printing of a singly linked list"""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node

        return '\n'.join(values)
