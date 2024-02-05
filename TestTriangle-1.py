# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle1 import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(5,7,9),'Scalene','5,7,8 is a scalene triangle')

    def testIsocelesTriangle(self):
        self.assertEqual(classifyTriangle(6,8,6),'Isosceles','6,8,6 should be isoceles')

    def testNotValidTriangle(self):
        self.assertEqual(classifyTriangle(3,7,2),'NotATriangle','3,7,2 is not a valid triangle')

    def testNegativeInputTriangle(self):
        self.assertEqual(classifyTriangle(3,-7,2),'InvalidInput','3,-7,2 is not a valid triangle')

    def testSideEqualToZero(self):
        self.assertEqual(classifyTriangle(0,4,5),'InvalidInput','0,4,5 has one or more sides equal to zero')

    def testSideGreaterThan200(self):
        self.assertEqual(classifyTriangle(201,70,80),'InvalidInput','One or more sides were greater than 200')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

