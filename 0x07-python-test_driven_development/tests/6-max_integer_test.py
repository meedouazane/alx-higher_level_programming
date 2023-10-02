#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_positive(self):
        '''
        test positive
        args:
            self: Arg
        '''
        inte = max_integer([1, 2, 3, 4])
        self.assertEqual(inte, 4)

    def test_negative(self):
        '''
        test negative numbers
        args:
            self: Arg
        '''
        inte = max_integer([-1, -2, -3, -4])
        self.assertEqual(inte, -1)

    def test_mixed(self):
        '''
        test mixed numbers
        args:
            self: Arg
        '''
        inte = max_integer([1, -2, 3, -4])
        self.assertEqual(inte, 3)

    def test_empty(self):
        '''
        test empty list
        args:
            self: Arg
        '''
        self.assertIsNone(max_integer([]))
    def test_one(self):
        '''
        test one elemnt
        args:
            self: Arg
        '''
        inte = max_integer([3])
        self.assertEqual(inte, 3)
    def test_same(self):
        '''
        test with the same number
        args:
            self: Arg
        '''
        inte = max_integer([3, 3, 3])
        self.assertEqual(inte, 3)

if __name__ == '__main__':
    unittest.main()
