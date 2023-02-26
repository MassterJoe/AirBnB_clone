#!/usr/bin/python3
import unittest
import time
import models
from models.base_model import BaseModel
class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()
    def test_attribute(self):
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_to_dict(self):
        d = self.model.to_dict()
        self.assertEqual(type(d), dict)
        self.assertTrue("__class__" in d)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertTrue("created_at" in d)
        self.assertTrue("updated_at" in d)
        self.assertTrue("id" in d)
        self.assertEqual(d["created_at"], self.model.created_at.isoformat())
        self.assertEqual(d["updated_at"], self.model.updated_at.isoformat())
    def test_save(self):
        prev_time = self.model.updated_at
        self.model.save()
        self.assertNotEqual(prev_time, self.model.updated_at)

if __name__=="__main__":
    unittest.main()
    

