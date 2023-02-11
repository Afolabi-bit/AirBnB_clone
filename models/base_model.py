#!/usr/bin/python3
"""This module defines the base model for our project"""
import uuid
import datetime
from models import *


class BaseModel():
    """
        This class defines all common attributes/methods
        for other classes
    """
    def __init__(self, *args, **kwargs):
        """insantiates the class"""
        if not (kwargs):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                else:
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)


    def __str__(self):
        """String reprresentation of class"""
        return f'[BaseModel] ({self.id}) {self.__dict__}'

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
            returns a dict containing all
            key/values of __dict__ instance
        """
        map_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.isoformat()
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class__.__name__
        return map_objects
