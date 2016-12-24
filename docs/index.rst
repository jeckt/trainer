.. trainer documentation master file, created by
   sphinx-quickstart on Sat Dec 24 14:41:15 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==========================================
Trainer: Your Personal Programming Trainer
==========================================

Trainer is a simple application that generates a random list
of user defined programming exercises. Users can use this
to train/practise on their programming skills.

It is very simple to use::

    >>> from trainer.trainer import Trainer
    >>> trainer = Trainer()
    >>> trainer.get_all_exercises()
    0. Build a skeleton python project and create git repo.
    1. Calculate powers of two numbers using Python argparse.
    >>> exercise = "Python inheritance: person and employee classes
    >>> trainer.add_exercise(exercise)
    >>> trainer.get_all_exercies()
    0. Build a skeleton python project and create git repo.
    2. Python inheritance: person and employee classes
    >>> trainer.get_new_list(2)
    0. Calculate powers of two numbers using Python argparse.
    1. Build a skeleton python project and create git repo.

==============
The User Guide
==============

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
