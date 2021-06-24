#!/usr/bin/python3
"""
Module BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel attributes
    """
    
    
    def __init__(self, *args, **kwargs):
        """
        constructor methode
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """
        Return a string repr of BaseModel class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
    
    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__
        
        for key, value in self.__dict__.items():
            if not value:
                continue
            if key == "created_at" or key == "updated_at":
                new_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                new_dict[key] = value
        return (new_dict)
