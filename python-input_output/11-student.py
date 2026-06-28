#!/usr/bin/python3
"""Module for Student class with serialization and deserialization."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to retrieve.

        Returns:
            dict: The dictionary representation of the student.
        """
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): The dictionary containing attribute names and values.
        """
        for k, v in json.items():
            setattr(self, k, v)
