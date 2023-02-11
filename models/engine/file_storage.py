#!/usr/bin/python3
"""This module handles storage of Class instances as JSON"""
import json
import os


class FileStorage():
    """
        This file serializes instances to a
        JSON file and deserializes JSON to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_cls_name, obj.id)] = obj 

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):        
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                object_dict = json.loads(f.read())
            FileStorage.__objects = object_dict
