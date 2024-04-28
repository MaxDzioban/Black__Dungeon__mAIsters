"""Tests"""
import unittest
from line import Point, Line
class TestLine(unittest.TestCase):
    '''Test'''
    def setUp(self):
        self.line1 = Line(Point(0.0, 0.0), Point(1.0, 3.0))
        self.line2 = Line(Point(1.0, 3.0), Point(0.0, -3.0))

    def test_init_point(self):
        point3 = Point(0, 4)
        self.assertEqual(point3.x, 0)
        self.assertEqual(point3.y, 4)

    def test_init_line(self):
        self.assertEqual(self.line1.point1.x, 0.0)
        self.assertEqual(self.line1.point1.y, 0.0)
        self.assertEqual(self.line1.point2.x, 1.0)
        self.assertEqual(self.line1.point2.y, 3.0)
        self.assertEqual(self.line1.k, 3.0)
        self.assertEqual(self.line1.l, 0.0)

    def test_intersect_none(self):
        line4 = Line(Point(0.0, 1.0), Point(1.0, 4.0))
        self.assertFalse(self.line1.intersect(line4))

    def test_ok_intersect(self):
        line5 = Line(Point(0.0, 0.0), Point(1.0, 3.0))
        line6 = self.line1.intersect(line5)
        self.assertEqual(line6.point1.x, 0.0)
        self.assertEqual(line6.point1.y, 0.0)
        self.assertEqual(line6.point2.x, 1.0)
        self.assertEqual(line6.point2.y, 3.0)

    def test_point_intersect(self):
        point1 = self.line2.intersect(self.line1)
        self.assertEqual(point1.x, 1.0)
        self.assertEqual(point1.y, 3.0)

    def test_not_intersect(self):
        line5 = Line(Point(1.0, 3.0), Point(0.0, -3.0))
        line6 = self.line2.intersect(line5)
        self.assertEqual(line6.point1.x, 1.0)
        self.assertEqual(line6.point1.y, 3.0)
        self.assertEqual(line6.point2.x, 0.0)
        self.assertEqual(line6.point2.y, -3.0)

    def test_error_intersect(self):
        with self.assertRaises(Exception) as context:
            self.assertRaises(Line('fdfdfd', Point(1, 2)), context.exception)

    def test_corenr_intersect1(self):
        line1 = Line(Point(2,4), Point(2,5))
        line2 = Line(Point(0, 0), Point(1 ,1))
        point5 = line2.intersect(line1)
        self.assertEqual(point5.x, 2)
        self.assertEqual(point5.y, 2)

    def test_corenr_intersect2(self):
        line1 = Line(Point(2,4), Point(2,5))
        line2 = Line(Point(2, 1), Point(2 ,2))
        line5 = line2.intersect(line1)
        self.assertEqual(line5.point1.x, 2)
        self.assertEqual(line5.point1.y, 1)
        self.assertEqual(line5.point2.x, 2)
        self.assertEqual(line5.point2.y, 2)
