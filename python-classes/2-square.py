#!/usr/bin/python3
"""Define a class named SQUARE"""


class Square:
    """S Q U A R E."""

    def __init__(self, size=0):
        """Start new square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self, area):
        """A R E A"""
        self.__area = area * area
