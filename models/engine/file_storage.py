#!/usr/bin/python3
"""
class FileStorage to store objects in a file
"""
import json


class FileStorage:
    """
    class that that serializes instances to a
    JSON file and deserializes JSON file to
    instances:
    """
    __file_path = "file_storage.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj class name>.id
        """
        FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        new_dic = {}
        for key in FileStorage.__objects:
            new_dic[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(new_dic, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            from models.base_model import BaseModel
            with open(FileStorage.__file_path, "r") as file:
                for key, value in json.load(file).items():
                    class_name = eval(value['__class__'])(**value)
                    FileStorage.__objects[key] = class_name

        except Exception:
            pass
