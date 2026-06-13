#!/usr/bin/python3
"""
This module contains a function that adds 2 integers.
It handles integers and floats, and raises TypeError for other types.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (cast to int).
    Raises TypeError if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
