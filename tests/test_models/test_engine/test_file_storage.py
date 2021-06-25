#!/usr/bin/python3
"""
    FileStorage module
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class FileStorageTest(unittest.TestCase):
    """
        FileStorageTest Class
    """

    def testNew(self):
        """
            Test the new function
        """
        f1 = FileStorage()
        self.assertEqual(len(f1.all()), 0)
        b1 = BaseModel()
        f1.new(b1)
        self.assertEqual(len(f1.all()), 1)
        for key, value in f1.all().items():
            self.assertIsInstance(key, str)
            self.assertEqual("{}.{}".format(type(value).__name__, value.id), key)