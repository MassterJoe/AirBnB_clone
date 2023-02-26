#!/usr/bin/python3
import unittest
import time
import models
from  models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()
    def test_attribute(self):
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        
if __name__ == "__main__":
    unittest.main()
