#!/usr/bin/python3
''' unittest for square  all methodes'''
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

    def test_string(self):
        ''' test getter with string '''
        with self.assertRaises(TypeError):
            s1 = Square("b")

    def test_str0(self):
        ''' test without all '''
        r1 = Square(5)
        expect = f"[Square] ({r1.id}) 0/0 - 5"
        self.assertEqual(expect, r1.__str__())

    def test_str1(self):
        ''' test without all '''
        r1 = Square(1, 2, 3, 4)
        expect = f"[Square] ({r1.id}) 2/3 - 1"
        self.assertEqual(expect, r1.__str__())

    def test_negative_number(self):
        ''' test negative number'''
        with self.assertRaises(ValueError):
            r1 = Square(5, -4, 2, -1)
            r1.__str__()

    def test_string(self):
        ''' test with string'''
        with self.assertRaises(TypeError):
            r1 = Square(5, "b", 2)
            r1.__str__()

    def test_empty(self):
        ''' test empty'''
        with self.assertRaises(TypeError):
            r1 = Square()
            r1.__str__()

    if __name__ == "__main__":
        unittest.main()
