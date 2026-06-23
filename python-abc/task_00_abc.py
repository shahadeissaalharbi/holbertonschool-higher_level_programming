#!/usr/bin/python3
"""Module that defines Animal abstract class and its subclasses"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method sound"""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal"""

    def sound(self):
        """Returns Bark"""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal"""

    def sound(self):
        """Returns Meow"""
        return "Meow"
