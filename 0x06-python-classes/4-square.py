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
        if isinstance(value, int):
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError("size must be an integer")



    def area(self):
        return self.__size ** 2