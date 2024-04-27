import unittest
from unittest.mock import patch
from target_en.terget_en import *

class TestTargetGame(unittest.TestCase):

    def test_generate_grid(self):
        grid = generate_grid()
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 3)
        for row in grid:
            self.assertIsInstance(row, list)
            self.assertEqual(len(row), 3)
            for letter in row:
                self.assertIsInstance(letter, str)

    @patch('builtins.input', side_effect=['word1', 'word2', 'word3'])
    def test_get_user_words(self, mock_input):
        user_words = get_user_words()
        self.assertIsInstance(user_words, list)
        self.assertEqual(len(user_words), 3)
        self.assertEqual(user_words, ['word1', 'word2', 'word3'])

    def test_get_words(self):
        letters = ['e', 't', 'o', 'o', 'p', 'n', 'p', 'u', 'r']
        words = get_words('en.txt', letters)
        self.assertIsInstance(words, list)
        for word in words:
            self.assertIsInstance(word, str)

    @unittest.parametrize('user_words, letters, words_from_dict, expected_result', [
        (['word1', 'word2', 'word3'], ['e', 't', 'o', 'o', 'p', 'n', 'p', 'u', 'r'], ['word1', 'word3'], ['word2']),
        (['word1', 'word2', 'word3'], ['e', 't', 'o', 'o', 'p', 'n', 'p', 'u', 'r'], ['apple', 'banana', 'cherry'], []),
        ([], ['e', 't', 'o', 'o', 'p', 'n', 'p', 'u', 'r'], ['word1', 'word2', 'word3'], [])
    ])
    def test_get_pure_user_words(self, user_words, letters, words_from_dict, expected_result):
        pure_user_words = get_pure_user_words(user_words, letters, words_from_dict)
        self.assertIsInstance(pure_user_words, list)
        self.assertEqual(len(pure_user_words), len(expected_result))
        self.assertEqual(pure_user_words, expected_result)

if __name__ == '__main__':
    unittest.main()
