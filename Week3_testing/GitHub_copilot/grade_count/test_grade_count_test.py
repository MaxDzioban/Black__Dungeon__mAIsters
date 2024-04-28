import unittest
from grade_count import calculate_grade

class TestGradeCount(unittest.TestCase):
    def test_average_grade_A(self):
        result = calculate_grade(85, 90, 67, 70, 87)
        self.assertEqual(result, "Average grade = 79.8 -> C")

    def test_average_grade_B(self):
        result = calculate_grade(97, 93, 84, 78, 80)
        self.assertEqual(result, "Average grade = 86.4 -> B")

    def test_invalid_grade(self):
        result = calculate_grade(85, 90, 67, 70, 105)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()