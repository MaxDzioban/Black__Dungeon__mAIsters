import unittest
from flatten import flatten

class TestFlatten(unittest.TestCase):
    def test_flatten_nested_lists(self):
        lst1 = [1, [2]]
        self.assertEqual(flatten(lst1), [1, 2])

        lst2 = [1, 2, [3, [4, 5], 6], 7]
        self.assertEqual(flatten(lst2), [1, 2, 3, 4, 5, 6, 7])

    def test_flatten_empty_list(self):
        lst3 = []
        self.assertEqual(flatten(lst3), [])

    def test_flatten_empty_nested_list(self):
        lst4 = [[]]
        self.assertEqual(flatten(lst4), [])

    def test_flatten_non_list_argument(self):
        arg = 123
        self.assertEqual(flatten(arg), arg)
