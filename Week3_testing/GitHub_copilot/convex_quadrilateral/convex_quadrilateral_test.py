import unittest
from convex_quadrilateral import *
import unittest

class TestFourLinesArea(unittest.TestCase):

    def test_area_with_parallel_lines(self):
        # Test case with parallel lines
        k1, c1 = 1, 2
        k2, c2 = 1, 4
        k3, c3 = 3, 6
        k4, c4 = 3, 8
        expected_area = 0
        self.assertAlmostEqual(four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4), expected_area)

    def test_area_with_invalid_lines(self):
        # Test case with invalid lines
        k1, c1 = 1, 2
        k2, c2 = 3, 4
        k3, c3 = 5, 6
        k4, c4 = 7, 8
        expected_area = None
        self.assertIsNone(four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4))

    def test_area_with_zero_length_sides(self):
        # Test case with zero length sides
        k1, c1 = 1, 2
        k2, c2 = 1, 2
        k3, c3 = 1, 2
        k4, c4 = 1, 2
        self.assertEqual(four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4), 0)

    def test_area_with_horizontal_lines(self):
        # Test case with horizontal lines
        k1, c1 = 0, 2
        k2, c2 = 0, 4
        k3, c3 = 0, 6
        k4, c4 = 0, 8
        expected_area = 0
        self.assertAlmostEqual(four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4), expected_area)
    # END: Additional Test Cases
    def test_area_with_complex_numbers(self):
        # Test case with complex numbers
        k1, c1 = 1j, 2j
        k2, c2 = 2j, 3j
        k3, c3 = 3j, 4j
        k4, c4 = 4j, 5j
        expected_area = 0
        self.assertAlmostEqual(four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4), expected_area)

if __name__ == '__main__':
    unittest.main()
