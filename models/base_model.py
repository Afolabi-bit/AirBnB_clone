#!/usr/bin/python3
"""This module defines the base model for our project"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
        This class defines all common attributes/methods
        for other classes
    """
    def __init__(self, *args, **kwargs):
        """instantiates the class"""
        if not (kwargs):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value


    def __str__(self):
        """String reprresentation of class"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            returns a dict containing all
            key/values of __dict__ instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
