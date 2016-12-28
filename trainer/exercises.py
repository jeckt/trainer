# -*- coding: utf-8 -*-

"""
trainer.exercises
===============

This module handles the representation
and management of programming exercises
"""

import os
import csv

# TODO(steve): should this class inherit from
# list, set of dict class? Initial thoughts no.
# We want exercises to be SIMPLER than a list
# object but has some similar attributes.
# TODO(steve): should we switch from python
# pickle to json pickle for cross platform
# compatibility
# TODO(steve): Should a load method be implemented?
# This will make Exercises handle it's own data
# storage implementation. Or is this trainer's role?
# Current design decision is to have trainer
# handle the data storage implementation
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
        self._index = 0
        return self

    def next(self):
        """Iterator interface method"""
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration()

    def __eq__(self, other):
        """Comparison operator"""
        if type(self) == type(other):
            return self._items == other._items
        else:
            return False

    def __getitem__(self, index):
        """Index operator"""
        if not isinstance(index, int):
            msg = 'Indicies must be integers, not {}'.format(type(index))
            raise TypeError(msg)

        if index >= len(self._items) or abs(index) > len(self._items):
            error_msg = "Index out of range. Index {}".format(index)
            raise IndexError(error_msg)

        return self._items[index]

    def update(self, old_exercise, new_exercise):
        """Update existing exercise

        Examples
        --------
        >>> from trainer.trainer import Exercises, Exercise
        >>> tasks = Exercises()
        >>> ex = Exercise("Calcumalate powers of two numbers using argparse")
        >>> tasks.append(ex)
        >>> tasks[0]
        Calcumalate powers of two numbers using argparse
        >>> new_ex = Exercise("Calculate powers of two numbers using argparse")
        >>> tasks.update(ex, new_ex)

        Parameters
        ----------
        old_exercise : :obj:`Exercise`
            an existing exercise in the set to update
        new_exercise : :obj:`Exercise`
            new exercise to override the existing exercise
        """
        msg = "{} exercise must be of type Exercise, not {}"
        if not isinstance(old_exercise, Exercise):
            raise TypeError(msg.format("Old", type(old_exercise)))

        if not isinstance(new_exercise, Exercise):
            raise TypeError(msg.format("New", type(new_exercise)))

        if old_exercise not in self._items:
            error_msg = "{} not in exercises".format(old_exercise)
            raise ValueError(error_msg)

        idx = self._items.index(old_exercise)
        self._items[idx] = new_exercise

    def remove(self, exercise):
        """Remove exercise from set based on
        the exercise name

        Examples
        -------
        >>> from trainer.trainer import Exercises, Exercise
        >>> tasks = Exercises()
        >>> ex = Exercise("Calculate powers of two numbers using argparse")
        >>> tasks.append(ex)

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

    def add_exercises_from_csv(self, filename):
        """Add one or more exercuses using a csv file

        Examples
        --------
        >>> from trainer import Exercises
        >>> exercises = Exercises()
        >>> exercises.add_exercises_from_csv('my_exercises.csv')
        >>> exercises[0]
        'Command line tool to calculate powers of two numbers using argparse'

        Parameters
        ----------
        filename: str
            filename of the programming exercises to add. file should be
            a csv of the form

            programming exercise 1
            programming exercise 2
            programming exercise 3
        """
        if not os.path.isfile(filename):
            error_msg = "no such file or directory: '{}'".format('fake.csv')
            raise IOError(error_msg)

        try:
            tmp = []
            with open(filename, 'rb') as f:
                reader = csv.reader(f)
                for row in reader:
                    ex = Exercise(row[0])
                    tmp.append(ex)
        except:
            raise

        self._items += tmp

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

