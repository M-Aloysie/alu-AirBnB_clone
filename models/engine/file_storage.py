#!/usr/bin/python3

import re
import importlib
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
"""
    we imported json, re, and importlib
"""


class FileStorage():
    """
        this class will help us to store all instances that
        will be created
    """
    __file_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', 'file.json'))
    __objects = {}

    def all(self):
        """
            this method will return the dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """
            this method will set obj into __objects with key which is
            the catenated obj's id and its class name and the value
            which is this object its self.
        """
        id = obj.id
        key = f"{type(obj).__name__}.{id}"
        self.__objects[key] = obj

    def save(self):
        """
            this method will save __objects after being serialized into
            __file_path
        """
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    # def add_underscore(self, string):
    #     """
    #         this method will help us to convert the class_names
    #         to the names of the file in which they are defined in
    #         remember the convention we are using is that if we have
    #         a class named BaseMode, this class is defined in file called
    #         base_model.py. We will apply this is reload() function bellow
    #     """
    #     result = re.sub(r'(?<!^)([A-Z])', r'_\1', string)
    #     return result.lower()

    def reload(self):
        """
            this method will take the contents of the file which are in
            json string and convert them back to dictionary
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, class_id = key.split('.')
                    cls = class_name
                    # cls_file_name = self.add_underscore(class_name)
                    # module_name = "models." + cls_file_name
                    # module = importlib.import_module(module_name)
                    # cls = getattr(module, class_name)
                    # obj = cls(**value)
                    # self.__objects[key] = obj
                    if cls == "BaseModel":
                        obj = BaseModel(**value)
                        self.__objects[key] = obj
                    elif cls == "User":
                        obj = User(**value)
                        self.__objects[key] = obj
                    elif cls == "Amenity":
                        obj = Amenity(**value)
                    elif cls == "Review":
                        obj = Review(**value)
                    elif cls == "City":
                        obj = City(**value)
                    elif cls == "State":
                        obj = State(**value)
                    elif cls == "Place":
                        obj = Place(**value)
        except FileNotFoundError:
            pass
