#!/usr/bin/python3
"""Module that checks if object is instance of a class that inherited from"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited from"""
    return isinstance(obj, a_class) and type(obj) is not a_class
