import unittest
from expression_calculator import calculate_expression

class TestExpressionCalculator(unittest.TestCase):
    def test_addition(self):
        result = calculate_expression("Скільки буде 5 додати 5?")
        self.assertEqual(result, 10)

    def test_multiplication_and_addition(self):
        result = calculate_expression("Скільки буде 2 помножити на 10 додати 7?")
        self.assertEqual(result, 27)

    def test_division_and_subtraction(self):
        result = calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
        self.assertEqual(result, 9)

    def test_invalid_expression(self):
        result = calculate_expression("Скільки буде 3 в кубі?")
        self.assertEqual(result, "Неправильний вираз!")

if __name__ == '__main__':
    unittest.main()