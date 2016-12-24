======
README
======

Trainer is a simple application that generates a random list
of user defined programming exercises. Users can use this
to train/practise on their programming skills.

=============
RELEASE NOTES
=============

0.0.1 (2016-12-24)
++++++++++++++++++

* Conception

====
TODO
====

#. (DONE) Build command line app that generates programming exercises randomly
   
   #. Create a user story of how to use trainer.
   #. Create a user story of how to add programming exercises to trainer
   #. Create a user story of how to delete programming exercises to trainer
   #. Add mock data that can used in the tests
   #. Implement functionality that enables the user stories

#. (DONE) Add documentation using Sphinx and upload to readthedocs.org
#. (DONE) Use git for source control and upload to github
#. Enable support for bulk add and delete of programming exercises

   #. Refactor the exercises out of the trainer class
   #. Investigate using Python pickling to store exercises instead of txt
   #. Provide out to text for visual inspection?
   #. Add ids to exercises to enable easier adding/removing

#. Enable support for generating lists with total estimate time it will take to complete
#. Enable a spec to be added each programming exercises that provides exercise details
#. Create setup.py and allow users to install trainer as a command line tool
#. Enable support for multiple lists for better management.
#. Enable support of python unittest to be use to validate programming exercises
#. Enable support to log time it took for each programming exercises
#. Enable reports on programming exercises completed and time taken. Journal. 
