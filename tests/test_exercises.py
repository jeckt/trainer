# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))

import unittest

from trainer.exercises import Exercises, Exercise

TEST_DATA_FILE = os.path.join(os.path.dirname(__file__), 'test_dataset_1.txt')

class ExercisesOutputTestCases(unittest.TestCase):
    """A test suite for pickle and csv output methods"""
    pass

class ExercisesTestCases(unittest.TestCase):
    def setUp(self):
        self.exercises = Exercises()

    def test_exercises_valid_comparison(self):
        ex = Exercise("new exercise")
        self.exercises.append(ex)

        new_exercises = Exercises()
        new_exercises.append(ex)
        self.assertEqual(new_exercises, self.exercises)

    def test_exercises_invalid_comparions_type_difference(self):
        ex = Exercise("new exercise")
        self.exercises.append(ex)

        fake_exercises = 5
        self.assertNotEqual(self.exercises, fake_exercises)

    def test_exercises_invalid_comparions_different_exercises(self):
        ex = Exercise("new exercise")
        self.exercises.append(ex)

        new_exercises = Exercises()
        self.assertNotEqual(self.exercises, new_exercises)

    def test_create_exercises_object(self):
        self.assertIsInstance(self.exercises, Exercises)

    def test_exercises_starts_with_zero_length(self):
        self.assertEqual(len(self.exercises), 0)

    def test_add_valid_exercise(self):
        ex = Exercise("New exercise")
        self.exercises.append(ex)

        self.assertEqual(len(self.exercises), 1)
        self.assertTrue(ex in self.exercises)

    def test_add_invalid_exercise(self):
        ex = 5
        with self.assertRaises(TypeError) as context:
            self.exercises.append(ex)

        msg = "Invalid type. Must be of type Exercise"
        self.assertTrue(msg in context.exception)

    def test_add_duplicate_exercise(self):
        ex = Exercise("New exercise")
        self.exercises.append(ex)

        with self.assertRaises(Exception) as context:
            self.exercises.append(ex)

        error_msg = "Cannot add duplicate exercise. Exercise {}".format(ex)
        self.assertTrue(error_msg in context.exception)

    def test_remove_valid_exercise(self):
        ex = Exercise("New exercise")
        self.exercises.append(ex)

        self.exercises.remove(ex)
        self.assertEqual(len(self.exercises), 0)
        self.assertNotIn(ex, self.exercises)

    def test_remove_exercise_invalid_type(self):
        with self.assertRaises(TypeError) as context:
            self.exercises.remove(1)

        error_msg = "Invalid type. Must be of type Exercise"
        self.assertTrue(error_msg in context.exception)

    def test_remove_exercise_not_exist(self):
        ex = Exercise("Non existant exercise")
        with self.assertRaises(ValueError) as context:
            self.exercises.remove(ex)

        error_msg = "Exercise not in set. Exercice: {}".format(ex)
        self.assertTrue(error_msg in context.exception)

    def test_get_exercise_by_index(self):
        ex = Exercise("New exercise")
        self.exercises.append(ex)

        self.assertEqual(self.exercises[0], ex)

    def test_get_exercise_using_invalid_index_type(self):
        with self.assertRaises(TypeError) as context:
            invalid_item = self.exercises['x']

        error_msg = 'Indicies must be integers, not {}'.format(type('x'))
        self.assertTrue(error_msg in context.exception)

    def test_get_exercise_by_index_out_of_bounds(self):
        with self.assertRaises(IndexError) as context:
            invalid_item = self.exercises[0]

        error_msg = "Index out of range. Index {}".format(0)
        self.assertTrue(error_msg in context.exception)

    def test_get_exercise_using_negative_out_of_bounds_index(self):
        with self.assertRaises(IndexError) as context:
            index = -1
            invalid_item = self.exercises[index]

        error_msg = "Index out of range. Index {}".format(index)
        self.assertTrue(error_msg in context.exception)

    def test_get_exercise_using_valid_negative_index(self):
        ex = Exercise("New exercise")
        self.exercises.append(ex)

        self.assertEqual(self.exercises[-1], ex)

    def test_copy_valid_exercises_object(self):
        ex = Exercise("New exercise")
        self.exercises.append(ex)

        new_exercises = Exercises(self.exercises)
        self.assertIsInstance(new_exercises, Exercises)

    def test_copy_invalid_exercises_object(self):
        with self.assertRaises(TypeError) as context:
            invalid_exercises = Exercises('x')

        msg = "{} object is not of type Exercises".format(type('x'))
        self.assertTrue(msg in context.exception)

class ExerciseTestCases(unittest.TestCase):
    def test_create_exercise(self):
        desc = "New Exercise"
        ex = Exercise(desc)

        self.assertIsInstance(ex, Exercise)

    def test_exercise_valid_comparison(self):
        desc = "New Exercise"
        ex = Exercise(desc)
        ex1 = Exercise(desc)

        self.assertEqual(ex, ex1)

    def test_exercise_invalid_comparison_different_type(self):
        desc = "New Exercise"
        ex = Exercise(desc)

        self.assertNotEqual(ex, desc)

    def test_exercise_invalid_comparison_difference_exercise(self):
        ex1 = Exercise("First Exercise")
        ex2 = Exercise("Second Exercise")

        self.assertNotEqual(ex1, ex2)


if __name__ == '__main__':
    unittest.main()
