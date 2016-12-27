# -*- coding: utf-8 -*-

"""
trainer.trainer
===============

Entry point for the trainer app

:copyright: (c) 2016 by Steven Nguyen.
:license: GNU GPLv3, see LICENSE for more details
"""

import os
import random
import pickle

from exercises import Exercises, Exercise

# TODO(steve): The orchestration layer should handle errors
# and display it to the users as oppose to raising errors
class Trainer(object):
    """Orchestrator between users and the app. Allows users
    to add, delete, edit programming exercises or generate
    a list of random programing exercises that have been added
    """
    _PROD_CONNECTION = os.path.join(os.path.dirname(__file__), 'data.pkl')

    def __init__(self, conn=None):
        """create the trainer class

        Examples
        --------
        >>> from trainer.trainer import Trainer
        >>> trainer = Trainer()

        Parameters
        ----------
        conn : :obj:`str`, optional
            connection to the data storage where the
            programming exercises are stored
        """
        if conn:
            self._conn = conn
        else:
            self._conn = Trainer._PROD_CONNECTION

        if not os.path.isfile(self._conn):
            self._is_data_loaded = False
            raise IOError("Could not connect to data")

        try:
            with open(self._conn, 'rb') as f:
                self._exercises = pickle.load(f)
        except:
            self._is_data_loaded = False
            raise

        self._is_data_loaded = True

    def get_all_exercises(self):
        """Get all programming exercises in Trainer"""
        return Exercises(self._exercises)

    def get_new_list(self, n):
        """Get number of random programming exercises"""
        total = len(self._exercises)
        if n > total:
            error_msg = "{} exercises requested but only {} available".format(n, total)
            raise Exception(error_msg)

        # TODO(steve): generate a set of test to ensure
        # no duplicates are being returned!
        all_exercises = list(self._exercises)
        new_list = []
        for i in xrange(n):
            index = random.randint(0, len(all_exercises) - 1)
            exercise = all_exercises[index]

            new_list.append(exercise)
            all_exercises.remove(exercise)

        return new_list

    def add_exercise(self, exercise):
        """Add exercise to Trainer"""
        if exercise in self._exercises:
            error_msg = "Exercise already exists. Exercise: {}".format(exercise)
            raise Exception(error_msg)

        self._exercises.append(exercise)
        self._save_exercises()

    def remove_exercise(self, exercise):
        """Remove exercise to Trainer"""
        if exercise not in self._exercises:
            error_msg = "Exercise does not exist. "
            error_msg += "Cannot remove exercise. "
            error_msg += "Exercise: {}""".format(exercise)
            raise Exception(error_msg)

        self._exercises.remove(exercise)
        self._save_exercises()

    # TODO(steve): method needs to be updated when 
    # multiple lists support is enabled
    def update_exercise(self, old_exercise, new_exercise):
        """Update existing exercise in Trainer"""
        self._exercises.update(old_exercise, new_exercise)
        self._save_exercises()

    def _save_exercises(self):
        try:
            with open(self._conn, 'wb') as f:
                pickle.dump(self.get_all_exercises(), f)
        except:
            raise

if __name__ == '__main__':
    import argparse

    desc = """
    Hello this is Trainer, your personal programming
    trainer. Trainer will help you improve your
    programming abilities by providing a random
    list of programming exercises for you to complete.

    You will first have to define a set of programming
    exercises for trainer to choose from.

    If no arguments are provided. Trainer returns all
    the exercises that have been added.
    """
    parser = argparse.ArgumentParser(description=desc)

    actions = parser.add_mutually_exclusive_group()
    actions.add_argument('-a', '--add',
            help='Add a programming exercise to Trainer')
    actions.add_argument('-r', '--remove',
            help='Remove a programming exercise to Trainer')
    actions.add_argument('-n', '--newlist', type=int,
            help='Generate a list of programming exercises')

    args = parser.parse_args()

    t = Trainer()
    if args.newlist:
        try:
            for i, ex in enumerate(t.get_new_list(args.newlist)):
                print "{}: {}".format(i, ex)
        except Exception as e:
            print e
    elif args.add:
        try:
            ex = Exercise(args.add)
            t.add_exercise(ex)
        except Exception as e:
            print e
    elif args.remove:
        try:
            ex = Exercise(args.remove)
            t.remove_exercise(ex)
        except Exception as e:
            print e
    else:
        for i, ex in enumerate(t.get_all_exercises()):
            print "{}: {}".format(i, ex)
