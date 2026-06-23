#!/usr/bin/python3
"""Module that defines BaseGeometry class"""


class BaseGeometry:
    """A class BaseGeometry with area and integer_validator methods"""

    def area(self):
        """Raises an Exception with message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value is a positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
