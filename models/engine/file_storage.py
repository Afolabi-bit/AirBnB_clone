#!/usr/bin/python3
"""This module handles storage of Class instances as JSON"""
import json
import os
from models import base_model


class FileStorage():
    """
        This file serializes instances to a
        JSON file and deserializes JSON to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_cls_name = obj.__class__.__name__
        self.__objects["{}.{}".format(obj_cls_name, obj.id)] = obj

    def classes(self):
        from models import BaseModel

        classes = {"BaseModel": BaseModel}
        return classes

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                object_dict = json.load(f)
            for o in object_dict.values():
                cls_name = o["__class__"]
                del o["__class__"]
                self.new(eval(f"base_model.{cls_name}")(**o))
