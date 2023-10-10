#!/usr/bin/python3
'''  class Student that defines a student '''


class Student:
    '''  class Student that defines a student '''

    def __init__(self, first_name, last_name, age):
        ''' Public instance attributes:
        args:
            first_name:
            last_name:
            age:
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' retrieves a dictionary representation of a Student '''
        if isinstance(attrs, list):
            if all (isinstance(i, str) for i in attrs):
                return {elmnt: getattr(self, elmnt) for elmnt in attrs if hasattr(self, elmnt)}
        return self.__dict__
