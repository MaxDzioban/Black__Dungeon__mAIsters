import unittest
from grade_to_letters import *

class TestGrades(unittest.TestCase):
    def test_calculate_grade(self):
        self.assertEqual(calculate_grade(90, 85, 95, 88, 92), "Average grade = 90.0 -> A")
        self.assertEqual(calculate_grade(80, 85, 75, 88, 82), "Average grade = 82.0 -> B")
        self.assertEqual(calculate_grade(70, 65, 75, 68, 72), "Average grade = 70.0 -> C")
        self.assertEqual(calculate_grade(60, 65, 55, 68, 62), "Average grade = 62.0 -> D")
        self.assertEqual(calculate_grade(50, 45, 55, 48, 52), "Average grade = 50.0 -> F")
        self.assertEqual(calculate_grade(110, 85, 95, 88, 92), None)
        self.assertEqual(calculate_grade(-10, 85, 95, 88, 92), None)
        self.assertEqual(calculate_grade(0, 0, 0, 0, 0), "Average grade = 0.0 -> F")
        self.assertEqual(calculate_grade(100, 100, 100, 100, 100), "Average grade = 100.0 -> A")
        self.assertEqual(calculate_grade(100, 0, 100, 0, 100), "Average grade = 60.0 -> D")
        self.assertEqual(calculate_grade(0, 100, 0, 100, 0), "Average grade = 40.0 -> F")
        self.assertEqual(calculate_grade(50, 50, 50, 50, 50), "Average grade = 50.0 -> F")
        self.assertEqual(calculate_grade(101, 85, 95, 88, 92), None)
        self.assertEqual(calculate_grade(-1, 85, 95, 88, 92), None)

# if __name__ == '__main__':
#     unittest.main()