#!/usr/bin/python3
"""Module that defines VerboseList class"""


class VerboseList(list):
    """A list class that prints notifications on modifications"""

    def append(self, item):
        """Adds item and prints notification"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extends list and prints notification"""
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Removes item and prints notification"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops item and prints notification"""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
