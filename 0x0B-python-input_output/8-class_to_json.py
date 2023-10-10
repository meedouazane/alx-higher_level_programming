#!/usr/bin/python3
import json
''' function that returns the dictionary description
    with simple data structure  '''


def class_to_json(obj):
    ''' returns the dictionary description
    with simple data structure '''
    return json.dumps(obj.__dict__)
