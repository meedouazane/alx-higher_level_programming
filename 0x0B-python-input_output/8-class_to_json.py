#!/usr/bin/python3
''' function that returns the dictionary description
    with simple data structure  '''
import json


def class_to_json(obj):
    ''' returns the dictionary description
    with simple data structure '''
    return json.dumps(obj.__dict__)
