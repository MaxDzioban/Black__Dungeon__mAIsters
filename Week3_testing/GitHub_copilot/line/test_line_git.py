import unittest
from line import Line, Point

class TestLine(unittest.TestCase):
    def setUp(self):
        # Create two lines for testing
        self.line1 = Line(Point(0.0, 0.0), Point(1.0, 3.0))
        self.line2 = Line(Point(2.0, 2.0), Point(4.0, 6.0))

    def tearDown(self):
        # Clean up any resources used for testing
        pass

    def test_no_intersection(self):
        # Test case for lines that do not intersect
        self.assertIsNone(self.line1.intersect(self.line2))

    def test_intersection(self):
        # Test case for lines that intersect
        expected_point = Point(0.5, 0.75)
        self.assertEqual(self.line1.intersect(self.line1), expected_point)

    def test_coincident_lines(self):
        # Test case for coincident lines
        self.assertEqual(self.line1.intersect(self.line1), self.line1.start)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
