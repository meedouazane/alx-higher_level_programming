#!/usr/bin/python3
'''  the “base” of all other classes in this project '''
import json
import csv
import os


class Base:
    '''  the “base” of all other classes in this project '''

    ''' private class attribute __nb_objects (id) '''
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the data.
        Args:
        id: assign the public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns the JSON string representation of list_dictionaries '''
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''  writes the JSON string representation of list_objs to a file '''
        filename = cls. __name__ + ".json"
        string = ""
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                to_dict = [i.to_dictionary() for i in list_objs]
                string = cls.to_json_string(to_dict)
                f.write(string)

    @staticmethod
    def from_json_string(json_string):
        ''' returns the list of the JSON string representation json_string '''
        if json_string is None or json_string == "[]":
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' returns an instance with all attributes already set '''
        if dictionary is not None:
            if cls.__name__ == 'Rectangle':
                inst = cls(1, 1)
            if cls.__name__ == 'Square':
                inst = cls(1)
            inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        ''' returns a list of instances '''
        filename = cls. __name__ + ".json"
        with open(filename, 'r') as f:
            if not os.path.exists(filename):
                return []
            else:
                string = f.read()
                lst = cls.from_json_string(string)
                return [cls.create(**i) for i in lst]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''  writes the CSV string representation of list_objs '''
        filename = cls. __name__ + ".csv"
        fields = ["id", "width", "height", "x", "y"]
        with open(filename, mode='w', newline="") as f:
            if list_objs is None or list_objs == "[]":
                f.write("[]")
            if cls.__name__ == 'Rectangle':
                string = csv.DictWriter(f, fieldnames=fields)
            else:
                string = csv.DictWriter(f, fieldnames=["id", "size", "x", "y"])
            for row in list_objs:
                string.writerow(row.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        ''' returns a list of instances from csv '''
        filename = cls. __name__ + ".csv"
        string = []
        fields = ["id", "width", "height", "x", "y"]
        with open(filename, mode='r') as f:
            if not os.path.exists(filename):
                return []
            if cls.__name__ == 'Rectangle':
                string = csv.DictReader(f, fieldnames=fields)
            else:
                string = csv.DictReader(f, fieldnames=["id", "size", "x", "y"])
            lst = [dict([k, int(v)] for k, v in d.items()) for d in string]
            return [cls.create(**i) for i in lst]
