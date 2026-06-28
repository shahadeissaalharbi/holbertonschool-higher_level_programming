#!/usr/bin/python3
"""Module for pickling custom classes."""
import pickle


class CustomObject:
    """A custom Python class that supports serialization with pickle."""

    def __init__(self, name, age, is_student):
        """Initializes a CustomObject instance.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the current instance and saves it to a file.

        Args:
            filename (str): The filename to save the serialized object.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and returns an instance of CustomObject from a file.

        Args:
            filename (str): The filename to load the serialized object from.

        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
