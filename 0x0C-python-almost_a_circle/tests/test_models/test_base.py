#!/usr/bin/python3
''' Unittest for base '''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def testassignid(self):
        ''' test assign id '''
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def testwithoutid1(self):
        ''' test without assign id '''
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def testwithoutid2(self):
        ''' test without assign id '''
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def testwithoutid3(self):
        ''' test without assign id '''
        b1 = Base()
        self.assertEqual(b1.id, 3)

    def testid0(self):
        ''' test assign id '''
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def testNegativeid(self):
        ''' test assign negative id '''
        b1 = Base(-10)
        self.assertEqual(b1.id, -10)
