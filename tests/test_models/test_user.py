#!/usr/bin/python3
""" Unit tests for user.py file"""


import unittest
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User


class TestUser(unittest.TestCase):
    """ Unit tests for user.py file"""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def test_user(self):
        """Test if the inheritance works"""

        self.assertTrue(issubclass(User, BaseModel))


    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of User class."""

        b = User()
        self.assertEqual(str(type(b)), "<class 'models.user.User'>")
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))



if __name__ == "__main__":
    unittest.main()
