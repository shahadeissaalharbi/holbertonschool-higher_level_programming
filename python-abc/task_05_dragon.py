#!/usr/bin/python3
"""Module that defines SwimMixin, FlyMixin, and Dragon classes"""


class SwimMixin:
    """A mixin that provides swim functionality"""

    def swim(self):
        """Prints swimming message"""
        print("The creature swims!")


class FlyMixin:
    """A mixin that provides fly functionality"""

    def fly(self):
        """Prints flying message"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon class that inherits from SwimMixin and FlyMixin"""

    def roar(self):
        """Prints roaring message"""
        print("The dragon roars!")
