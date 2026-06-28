#!/usr/bin/python3
"""Module for converting class to JSON."""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
