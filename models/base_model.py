#!/usr/bin/python3

import uuid
import datetime
import models
"""
    imported uuid, and datetime modules
"""


class BaseModel:
    """
        this is the class that all other classes in this project
        will inherit from
    """

    def __init__(self, *args, **kwargs):
        """
            this is an init method, this method will be called directly
            as we create a new instance of this BaseModel class
        """
        key = None
        if kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = kwargs.get('id')
        #         elif key == 'created_at' or key == 'updated_at':
        #             self.key = datetime.datetime.strptime(
        #                 kwargs.get(key), '%Y-%m-%dT%H:%M:%S.%f')
        # elif key == 'created_at' or key == 'updated_at':
        # setattr(self, key, datetime.datetime.strptime(
        #         kwargs.get(key), '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.datetime.strptime(
                        kwargs.get(key), '%Y-%m-%dT%H:%M:%S.%f'))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            models.storage.new(self)

    def __str__(self):
        """
            this method will print class name, id of an instance
            and a dictionary representation of an instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            this method will return the time we have updated our instance
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            this method will return the dictionary representation of
            this instance
        """
        y = self.__dict__.copy()
        y['__class__'] = self.__class__.__name__
        y['created_at'] = self.created_at.isoformat()
        y['updated_at'] = self.updated_at.isoformat()
        return (y)
