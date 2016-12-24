# -*- coding: utf-8 -*-

"""A set of functional tests that reflect user stories"""

import sys
import os
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))

import unittest
import shutil
from trainer.trainer import Trainer

TEST_DATA_FILE = os.path.join(os.path.dirname(__file__), 'test_dataset_1.txt')

class FunctionalTestCase1(unittest.TestCase):
    """A set of functional test cases that highlight
    the interactions between users and the trainer"""
    def setUp(self):
        # NOTE(steve): the performance impact
        # of copying a data for each test will
        # be an issue with larger test data sets
        self._TMP_DATA_FILE = "_tmp_data.txt"
        i = 0
        while os.path.isfile(self._TMP_DATA_FILE):
            self._TMP_DATA_FILE = "_tmp_data_{}.txt".format(i)
            i += 1

        shutil.copyfile(TEST_DATA_FILE, self._TMP_DATA_FILE)
        self.trainer = Trainer(conn=self._TMP_DATA_FILE)

    def tearDown(self):
        if os.path.isfile(self._TMP_DATA_FILE):
            os.remove(self._TMP_DATA_FILE)

    def test_user_creates_new_list(self):
        """A daily user would typically log into trainer
        generate a list and start working on the exercises
        throughout the day. No further interaction"""

        # user starts up trainer and requests for
        # three programming exercises
        tasks = self.trainer.get_new_list(3)

        # check that three programming exercises
        # have in fact been returned
        self.assertEqual(len(tasks), 3)

    def test_user_adds_exercise_to_trainer(self):
        """A daily user wants to check all the exercises
        they have added to the trainer so far"""

        # user starts up trainer and grabs the
        # list of exercises currently in the trainer
        all_tasks = self.trainer.get_all_exercises()

        # user checks that there are 10 exercises
        # as he remembers it
        self.assertEqual(len(all_tasks), 10)

        # user proceeds to add another exercise
        # that he thinks might help him learn
        # the python argparse library
        exercise = "Use argparse to calculate the power of two numbers"
        self.trainer.add_exercise(exercise)

        # user grabs the list of all exercises again
        # and checks that the exercise has been added
        new_all_tasks = self.trainer.get_all_exercises()
        self.assertEqual(len(new_all_tasks), 11)
        self.assertIn(exercise, new_all_tasks)

    def test_user_removes_exercise_from_trainer(self):
        """A daily user finds that an exercise he has
        been doing over the last six months is no
        longer useful. She is a master at it! User
        proceeds to delete the exercise from trainer"""

        # user opens up the trainer and gets 
        # all the exercises currently in the system
        all_tasks = self.trainer.get_all_exercises()

        # user checks that there are 10 exercises
        # as he remembers it
        self.assertEqual(len(all_tasks), 10)

        # user deletes the first exercise in the
        # list as she no longer needs it
        removed_task = self.trainer.remove_exercise(all_tasks[0])

        # user grabs the new list of all exercises
        # and checks that there are only 9
        # exercists left and the correct one has 
        # been removed
        new_all_tasks = self.trainer.get_all_exercises()
        self.assertEqual(len(new_all_tasks), 9)
        self.assertNotIn(removed_task, new_all_tasks)

if __name__ == '__main__':
    unittest.main()
