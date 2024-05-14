#!/usr/bin/python3

"""define a class square"""


class Square:
    """ini square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value > 0:
            self.__size = value
        else:
            print("size must be an integer")

    def area(self):
        return self.__size ** 2
