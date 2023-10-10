#!/usr/bin/python3
''' function that creates an Object from a “JSON file" '''
import json


def load_from_json_file(filename):
    ''' creates an Object from a “JSON file" '''
    with open(filename, 'r') as json_file:
        data = json_file.read()
        my_obj = json.loads(data)
        return my_obj
