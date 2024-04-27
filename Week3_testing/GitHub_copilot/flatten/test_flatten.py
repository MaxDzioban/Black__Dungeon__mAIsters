import unittest
from flatten import *
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
        arg = 10
        self.assertEqual(flatten(arg), 10)

    def test_flatten_mixed_types(self):
        lst5 = [1, [2, 3], 'hello', [4, [5, 6]], None]
        self.assertEqual(flatten(lst5), [1, 2, 3, 'hello', 4, 5, 6, None])

if __name__ == '__main__':
    unittest.main()
