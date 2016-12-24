# -*- coding: utf-8 -*-

"""A set of unit tests for the trainer module"""

import sys
import os
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))

import unittest
import shutil
from trainer.trainer import Trainer

TEST_DATA_FILE = os.path.join(os.path.dirname(__file__), 'test_dataset_1.txt')

class TrainerConnectionTestCases(unittest.TestCase):
    """A set of unit test for testing connection"""
    def test_test_data_loaded(self):
        trainer = Trainer(conn=TEST_DATA_FILE)
        self.assertTrue(trainer._is_data_loaded,
                "Trainer could not load test data")

    def test_data_does_not_exist(self):
        with self.assertRaises(IOError) as context:
            trainer = Trainer(conn='fail_data')

        self.assertTrue('Could not connect to data' in context.exception)

    def test_data_loaded(self):
        trainer = Trainer()
        self.assertTrue(trainer._is_data_loaded,
                "Trainer could not load test data")

# TODO(steve): should test cases be refactored?
# moving test cases into small test suites may be
# better identification or errors.
class TrainerTestCases1(unittest.TestCase):
    """A set of unit tests for the trainer class"""
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

    def test_get_all_exercises(self):
        tasks = self.trainer.get_all_exercises();
        self.assertEqual(len(tasks), 10)

    def test_get_new_list_of_exercises(self):
        tasks = self.trainer.get_new_list(5)
        self.assertEqual(len(tasks), 5)

    def test_not_enough_exercises_to_generate_new_list(self):
        with self.assertRaises(Exception) as context:
            tasks = self.trainer.get_new_list(15)

        error_msg = "15 exercises requested but only 10 available"
        self.assertTrue(error_msg in context.exception)

    def test_get_new_list_does_not_change_all_exercises(self):
        all_tasks = self.trainer.get_all_exercises()
        self.assertEqual(len(all_tasks), 10)

        tasks = self.trainer.get_new_list(7)

        new_all_tasks = self.trainer.get_all_exercises()
        self.assertEqual(len(new_all_tasks), 10)

        # it is safe to assume that we have a unique set of
        # programming exercises
        self.assertTrue(set(all_tasks) == set(new_all_tasks),
                "List of all tasks has been mutated!")

    def test_add_new_exercise(self):
        all_tasks = self.trainer.get_all_exercises()
        self.assertEqual(len(all_tasks), 10)

        exercise = "new random exercise"
        self.trainer.add_exercise(exercise)

        new_all_tasks = self.trainer.get_all_exercises()
        self.assertEqual(len(new_all_tasks), 11)

        self.assertIn(exercise, new_all_tasks)

    def test_add_duplicate_exercise(self):
        all_tasks = self.trainer.get_all_exercises()
        exercise = all_tasks[4]

        with self.assertRaises(Exception) as context:
            self.trainer.add_exercise(exercise)

        error_msg = "Exercise already exists. Exercise: {}".format(exercise)
        self.assertTrue(error_msg in context.exception)

    def test_add_new_exercise_persists_to_data_storage(self):
        exercise = "new random exercise"
        self.trainer.add_exercise(exercise)
        old_all_tasks = self.trainer.get_all_exercises()

        new_trainer = Trainer(conn=self.trainer._conn)
        new_all_tasks = new_trainer.get_all_exercises()

        # NOTE(steve): may be slow when data set size increases
        self.assertTrue(set(old_all_tasks) == set(new_all_tasks),
                "Changes aren't persisting to data storage")

    def test_get_all_exercises_returns_a_copy_only(self):
        all_tasks = self.trainer.get_all_exercises()
        self.assertEqual(len(all_tasks), 10)

        all_tasks.append('exercise should not be included')
        new_all_tasks = self.trainer.get_all_exercises()
        self.assertEqual(len(new_all_tasks), 10)

    def test_remove_existing_exercise(self):
        old_all_tasks = self.trainer.get_all_exercises()
        self.assertEqual(len(old_all_tasks), 10)

        exercise = old_all_tasks[2]
        self.trainer.remove_exercise(exercise)

        new_all_tasks = self.trainer.get_all_exercises()
        self.assertEqual(len(new_all_tasks), 9)

    def test_remove_exercise_not_in_trainer(self):
        exercise = "non existent exercise"
        with self.assertRaises(Exception) as context:
            self.trainer.remove_exercise(exercise)

        error_msg = "Exercise does not exist. "
        error_msg += "Cannot remove exercise. "
        error_msg += "Exercise: {}""".format(exercise)
        self.assertTrue(error_msg in context.exception)

    def test_remove_exercise_persists_to_data_storage(self):
        old_all_tasks = self.trainer.get_all_exercises()
        exercise = old_all_tasks[3]
        self.trainer.remove_exercise(exercise)
        updated_all_tasks = self.trainer.get_all_exercises()

        new_trainer = Trainer(conn=self.trainer._conn)
        new_all_tasks = new_trainer.get_all_exercises()

        # NOTE(steve): may be slow when data set size increases
        self.assertTrue(set(updated_all_tasks) == set(new_all_tasks),
                "Changes aren't persisting to data storage")

if __name__ == '__main__':
    unittest.main()
