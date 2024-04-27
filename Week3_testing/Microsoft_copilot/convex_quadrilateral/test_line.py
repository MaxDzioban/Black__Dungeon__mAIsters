import unittest
from unittest.mock import patch
from line import Point, Line

class TestPoint(unittest.TestCase):
    def test_point_creation(self):
        p = Point(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_point_str(self):
        p = Point(1, 2)
        self.assertEqual(str(p), "(1, 2)")

class TestLine(unittest.TestCase):
    def test_line_creation(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        l = Line(p1, p2)
        self.assertEqual(l.point1, p1)
        self.assertEqual(l.point2, p2)
        self.assertEqual(l.k, 1)
        self.assertEqual(l.l, 1)

    def test_line_creation_vertical(self):
        p1 = Point(1, 2)
        p2 = Point(1, 4)
        l = Line(p1, p2)
        self.assertEqual(l.point1, p1)
        self.assertEqual(l.point2, p2)
        self.assertEqual(l.k, "Foo")
        self.assertEqual(l.l, "Foo")

    def test_line_creation_horizontal(self):
        p1 = Point(1, 2)
        p2 = Point(3, 2)
        l = Line(p1, p2)
        self.assertEqual(l.point1, p1)
        self.assertEqual(l.point2, p2)
        self.assertEqual(l.k, 0)
        self.assertEqual(l.l, 2)

    def test_line_creation_same_points(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        with self.assertRaises(ValueError):
            Line(p1, p2)

    def test_line_creation_invalid_points(self):
        p1 = Point(1, 2)
        p2 = (3, 4)
        with self.assertRaises(ValueError):
            Line(p1, p2)

    def test_line_intersect_parallel(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        l1 = Line(p1, p2)
        p3 = Point(5, 6)
        p4 = Point(7, 8)
        l2 = Line(p3, p4)
        self.assertIsNone(l1.intersect(l2))

    def test_line_intersect_vertical(self):
        p1 = Point(1, 2)
        p2 = Point(1, 4)
        l1 = Line(p1, p2)
        p3 = Point(1, 6)
        p4 = Point(1, 8)
        l2 = Line(p3, p4)
        self.assertEqual(l1.intersect(l2), Point(1, 6))

    def test_line_intersect_horizontal(self):
        p1 = Point(1, 2)
        p2 = Point(3, 2)
        l1 = Line(p1, p2)
        p3 = Point(2, 4)
        p4 = Point(4, 4)
        l2 = Line(p3, p4)
        self.assertEqual(l1.intersect(l2), Point(3, 2))

    def test_line_intersect_general(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        l1 = Line(p1, p2)
        p3 = Point(2, 1)
        p4 = Point(4, 5)
        l2 = Line(p3, p4)
        self.assertEqual(l1.intersect(l2), Point(3, 4))

if __name__ == "__main__":
    unittest.main()
