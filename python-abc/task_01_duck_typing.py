#!/usr/bin/python3
"""Module that defines Shape abstract class and its subclasses"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape"""

    @abstractmethod
    def area(self):
        """Abstract method area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method perimeter"""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape"""

    def __init__(self, radius):
        """Instantiation with radius"""
        self.radius = radius

    def area(self):
        """Returns the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Returns the perimeter of the circle"""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
