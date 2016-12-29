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

   #. (DONE) Refactor the exercises out of the trainer class
   #. (DONE) Investigate using Python pickling to store exercises instead of txt
   #. (DONE) Provide support for loading exercises via csv. For ease of updating
   #. (DONE) Provide output to text for visual inspection?
   #. A more efficent way to run all test suites before check in?
   #. Helper methods to easily update persistent data storage for changes in
         Exercise and Exercises classes
   #. Add ids to exercises to enable easier adding/removing (auto generated id)

#. Enable support for generating lists with time to complete estimates

   #. Consider what the default behaviour should be if users don't supply a 
         time estimate. Should time estimates be optional?

#. Enable a spec to be added each programming exercises that provides exercise details
#. Create setup.py and allow users to install trainer as a command line tool
#. Enable support for multiple lists for better management.
#. Enable support of python unittest to be use to validate programming exercises
#. Enable support to log time it took for each programming exercises
#. Enable reports on programming exercises completed and time taken. Journal. 
