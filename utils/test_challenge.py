""" In this module, I will create my answer to the challenge.

    The must-haves:
        - one test for each function
        - use of the Mock object
        - use pytest at least once

    Done:
        - created the skeleton (classes, functions, imports)
        - added a unit test for add function
        - works from command line: run `python -m unittest` in /utils folder
        - formatted & commented

    Todo:
        - a unit test for connect_to_db
        - a unit test for get_users_list_from_db
        - use pytest
        - use a Mock object
"""

from typing import List, Dict
# from unittest.mock import MagicMock  ## not used yet
import unittest

# import pytest  ## not used yet

from challenge import ConnectionDatabaseError, TestDbError
from challenge import add, connect_to_db , get_users_list_from_db


class TestAddition(unittest.TestCase):
    """A class to contain test methods for the add function."""

    def test_add(self):
        """ Test whether the add function correctly returns values
            for all integers between 1 and 200.

        Used methodology:
            - fill a list of tuples with the input values to test
            - assert that the function returns a correct result for each input
            - to compare the result of our function, we can use `sum(tuple)`

        Open question:
            For `test_range = 200`, 8 million tuples are created in the list.
            How well does this code scale upwards? On this machine, the code
            executes in 3 seconds, but the delay is noticeable. Is there a
            better way to perform this test?
        """

        triplets = []
        test_range = range(1, 201)

        for i in test_range:
            for j in test_range:
                for k in test_range:
                    triplets.append((i, j, k))

        for triplet in triplets:
            assert add(triplet[0], triplet[1], triplet[2]) == sum(triplet)

class TestConnect(unittest.TestCase):
    """ A class to contain test methods for the connect_to_db function."""

    def test_connection_string_is_test(self):
        """ Verify that this function raises a ConnectionDatabaseError
            when a different connection string than 'test' is provided.
        """

        self.assertRaises(ConnectionDatabaseError, connect_to_db, "godmode")

# Work in progress
class TestGetUsers(unittest.TestCase):
    """ A class to contain test methods for the get_users_list_from_db
        function.
    """

    def test_something3(self):
        """ TODO """

        pass


if __name__ == "__main__":
    unittest.main()
