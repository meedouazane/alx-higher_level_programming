#!/usr/bin/python3
''' tests for Rectangle '''
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    ''' tests for Rectangle '''

    def test_positive4(self):
        ''' positive numbers for hieght, width, x, y and id '''
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)

    def test_withString(self):
        ''' passing a string  '''
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "S")

    def test_negative1(self):
        ''' passing a negative number for height'''
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -12)

    def test_negative2(self):
        ''' passing a negative number for width'''
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 12)

    def test_negative3(self):
        ''' passing a negative number for x and 0 for y'''
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 5, -1, 0)

    def test_negative4(self):
        ''' passing a negative number for y'''
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, 3, -11)

    def test_withString2(self):
        ''' passing a string for x '''
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 5, "X", 2)

    def test_withString3(self):
        ''' passing a string for witth  '''
        with self.assertRaises(TypeError):
            r1 = Rectangle("W", 12, 2, 3)

    def test_withString4(self):
        ''' passing a string for y '''
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 1, 3, "f")

    def test_area(self):
        ''' passing valid numbers  '''
        r1 = Rectangle(5, 6)
        self.assertEqual(r1.area(), 30)

    def test_AreaWithString1(self):
        ''' passing a string for height '''
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "S")
            r1.area()

    def test_AreaWithString2(self):
        ''' passing a string for height '''
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)
            r1.area()

    def test_AreaWithNegative1(self):
        ''' passing negative number for height '''
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -10)
            r1.area()

    def test_AreaWithNegative2(self):
        ''' passing negative number for width '''
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 10)
            r1.area()

    def test_AreaWith0(self):
        ''' passing 0 for height '''
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 0)
            r1.area()

    def test_AreaWith0(self):
        ''' passing 0 for width '''
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 50)
            r1.area()

    def test_Area(self):
        ''' passing x and y also '''
        r1 = Rectangle(10, 5, 6, 2)
        self.assertEqual(r1.area(), 50)

    def test_Areaempty(self):
        ''' empty '''
        with self.assertRaises(TypeError):
            r1 = Rectangle()
            r1.area()
                                        
    if __name__ == "__main__":
        unittest.main()
