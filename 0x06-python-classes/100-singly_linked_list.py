#!/usr/bin/python3
""" class Node that defines a node of a singly linked list """


class Node:
    """ class node """
    def __init__(self, data, next_node=None):
        """Initializes the data.
        Args:
        data :  must be an integer, otherwise raise.
        next_node :  can be None or must be a Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.data = value

    @property
    def next_node(self):
        return self.next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) or value is not None:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """class SinglyLinkedList that defines a singly linked list"""

    def __init__(self):
        """Initializes the data."""
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                if current.value < value:
                    current = current.next
            current.next = new_node

    def __print__(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
