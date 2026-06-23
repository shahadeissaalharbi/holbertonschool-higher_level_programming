#!/usr/bin/python3
"""Module that checks if object is an instance of a class or inherits from it"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or inherits from it"""
    return isinstance(obj, a_class)
