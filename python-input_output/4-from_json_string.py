#!/usr/bin/python3
"""Module for converting JSON string to object."""
import json


def from_json_string(my_str):
    """Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
