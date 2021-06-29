#!/usr/bin/python3
"""
TestFileStorage class
"""
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import unittest
import os
import json

FileStorage = file_storage.FileStorage
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorage(unittest.TestCase):
    """FileStorage class Test"""

    def testAll(self):
        """Test all() returns the FileStorage objects"""
        storage = FileStorage()
        newDict = storage.all()
        self.assertEqual(type(newDict), dict)
        self.assertIs(newDict, storage._FileStorage__objects)

    def testNew(self):
        """Test new() add an object to the FileStorage objects"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                dict[instance_key] = instance
                self.assertEqual(dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def testSave(self):
        """Test save() saves objects to file.json"""
        os.remove("file_storage.json")
        storage = FileStorage()
        dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in dict.items():
            dict[key] = value.to_dict()
        string = json.dumps(dict)
        with open("file_storage.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))
