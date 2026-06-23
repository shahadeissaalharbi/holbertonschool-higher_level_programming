#!/usr/bin/python3
"""Module that defines CountedIterator class"""


class CountedIterator:
    """An iterator that keeps track of the number of items iterated"""

    def __init__(self, iterable):
        """Instantiation with an iterable"""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the number of items iterated"""
        return self.count

    def __next__(self):
        """Returns the next item and increments the counter"""
        item = next(self.iterator)
        self.count += 1
        return item
