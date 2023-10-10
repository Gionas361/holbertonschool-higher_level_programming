#!/usr/bin/python3
"""Define a class named SQUARE"""


class Square:
    """S Q U A R E."""

    def __init__(self, size=0):
        """Start new square"""
        self.__size = size

    @property
    def size(self):
        """Determined sizw?"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Squared size?"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A R E A"""
        return (self.__size * self.__size)
