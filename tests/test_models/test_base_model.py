#!/usr/bin/python3
""" BaseTest module """


from datetime import datetime, timedelta
from models.base_model import BaseModel
import time
from unittest import mock
import unittest


class BaseModelTest(unittest.TestCase):
    """ BaseTest class """

    def testClassDocumentation(self):
        """
            Class have documentation
        """
        self.assertGreater(len(BaseModel.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Constructor have documentation
        """
        self.assertGreater(len(BaseModel.__init__.__doc__), 0)

    def testStrDocumentation(self):
        """
            __str__ function have documentation
        """
        self.assertGreater(len(BaseModel.__str__.__doc__), 0)

    def testSaveDocumentation(self):
        """
            save function have documentation
        """
        self.assertGreater(len(BaseModel.save.__doc__), 0)

    def testToDictDocumentation(self):
        """
            to_dict function have documentation
        """
        self.assertGreater(len(BaseModel.to_dict.__doc__), 0)

    def testSave(self):
        """
            Test save function
        """
        b1 = BaseModel()
        b1.name = "Holberton"
        b1.my_number = 89
        b1.my_wrong_test = None
        b1.save()
        self.assertGreater(b1.updated_at, b1.created_at)
        self.assertDictEqual(
            b1.to_dict(),
            {
                '__class__': 'BaseModel',
                'created_at': b1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'id': b1.id,
                'my_number': 89,
                'name': "Holberton",
                'updated_at': b1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
                
            }
        )
    def testStr(self):
        b1 = BaseModel()
        string = "[BaseModel] ({}) {}".format(b1.id, b1.__dict__)
        self.assertEqual(string, str(b1))
