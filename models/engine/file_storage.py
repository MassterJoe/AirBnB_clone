#!/usr/bin/python3
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
    def save(self):
        with open(self.__file_path, 'w') as f:
            dict_obj = {}
            for key, value in self.__objects.items():
                dict_obj[key] = value.to_dict()
            json.dump(dict_obj, f)
    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                dict_obj = json.load(f)
                for key,value in dict_obj.items():
                    class_name = value["__class__"]
                    if class_name == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif class_name == 'User':
                        FileStorage.__objects[key] = User(**value)
                    elif class_name == 'Place':
                        FileStorage.__objects[key] = Place(**value)
                    elif class_name == 'State':
                        FileStorage.__objects[key] = State(**value)
                    elif class_name == 'Amenity':
                        FileStorage.__objects[key] = Amenity(**value)
                    elif class_name == 'Review':
                        FileStorage.__objects[key] = Review(**value)
                    del value["__class__"]
                    self.__objects(eval(class_name)(**value))
        except FileNotFoundError:
            pass
