#!/usr/bin/python3
"""Module that defines Fish, Bird, and FlyingFish classes"""


class Fish:
    """A Fish class"""

    def swim(self):
        """Prints swimming message"""
        print("The fish is swimming")

    def habitat(self):
        """Prints habitat message"""
        print("The fish lives in water")


class Bird:
    """A Bird class"""

    def fly(self):
        """Prints flying message"""
        print("The bird is flying")

    def habitat(self):
        """Prints habitat message"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A FlyingFish class that inherits from Fish and Bird"""

    def swim(self):
        """Prints swimming message"""
        print("The flying fish is swimming!")

    def fly(self):
        """Prints flying message"""
        print("The flying fish is soaring!")

    def habitat(self):
        """Prints habitat message"""
        print("The flying fish lives both in water and the sky!")
