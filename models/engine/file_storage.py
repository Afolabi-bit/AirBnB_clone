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
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(objdict, f)

    def reload(self):        
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
