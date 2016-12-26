# -*- coding: utf-8 -*-

"""
trainer.exercises
===============

This module handles the representation
and management of programming exercises
"""

# TODO(steve): should this class inherit from
# list, set of dict class? Initial thoughts no.
# We want exercises to be SIMPLER than a list
# object but has some similar attributes.
class Exercises(object):
    """Container for programming exercises"""
    def __init__(self, exercises=None):
        self._index = 0
        self._items = []
        if type(exercises) == type(self):
            self._items = list(exercises._items)
        elif exercises:
            msg = "{} object is not of type Exercises".format(type(exercises))
            raise TypeError(msg)

    def __iter__(self):
        """Return class as the iterator"""
        return self

    def __eq__(self, other):
        """Comparison operator"""
        if type(self) == type(other):
            return self._items == other._items
        else:
            return False

    def next(self):
        """Iterator interface method"""
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration()

    def __getitem__(self, index):
        """Index operator"""
        if not isinstance(index, int):
            msg = 'Indicies must be integers, not {}'.format(type(index))
            raise TypeError(msg)

        if index >= len(self._items) or abs(index) > len(self._items):
            error_msg = "Index out of range. Index {}".format(index)
            raise IndexError(error_msg)

        return self._items[index]

    def remove(self, exercise):
        """Remove exercise from set based on
        the exercise name

        Examples
        -------
        >>> from trainer.trainer import Exercises
        >>> tasks = Exercises()
        >>> tasks.append("Calculate powers of two numbers using argparse")

        Parameters
        ----------
        exercise : :obj:`Exercise`
            exercise to delete from set
        """
        if not isinstance(exercise, Exercise):
            msg = "Invalid type. Must be of type Exercise"
            raise TypeError(msg)

        if exercise not in self._items:
            error_msg = "Exercise not in set. Exercice: {}".format(exercise)
            raise ValueError(error_msg)

        return self._items.remove(exercise)

    def append(self, exercise):
        """Add exercise to the set of
        exercises

        Examples
        -------
        >>> from trainer.trainer import Exercises
        >>> tasks = Exercises()
        >>> tasks.append("Calculate powers of two numbers using argparse")

        Parameters
        ----------
        exercise : :obj:`Exercise`
            programming exercise to add to the set of exercises
        """
        if not isinstance(exercise, Exercise):
            msg = "Invalid type. Must be of type Exercise"
            raise TypeError(msg)

        if exercise in self._items:
            msg = "Cannot add duplicate exercise. Exercise {}".format(exercise)
            raise Exception(msg)

        self._items.append(exercise)

    def __len__(self):
        """Returns number of exercises"""
        return len(self._items)

class Exercise(object):
    """Represents a single exercise"""
    def __init__(self, description):
        self._description = description

    def __repr__(self):
        return self._description

    def __str__(self):
        return self._description

    def __eq__(self, other):
        if type(other) is type(self):
            return self._description == other._description
        else:
            return False


if __name__ == '__main__':
    pass

