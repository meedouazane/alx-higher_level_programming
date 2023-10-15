#!/usr/bin/python3
''' unittest for square '''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_square(unittest.TestCase):
    ''' unittest for square '''

    def test_getter(self):
        ''' test getter for square '''
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_getter2(self):
        ''' test getter for square '''
        s1 = Square(20)
        self.assertEqual(s1.size, 20)

    def test_neg(self):
        ''' test getter with negative number '''
        with self.assertRaises(ValueError):
            s1 = Square(-1)

    def test_zero(self):
        ''' test getter with zero '''
        with self.assertRaises(ValueError):
            s1 = Square(0)
