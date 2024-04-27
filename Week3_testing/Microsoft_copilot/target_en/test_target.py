import unittest
from target import get_pure_user_words


class TestGetPureUserWords(unittest.TestCase):
    def test_valid_user_words(self):
        user_words = ['opto', 'open', 'uproot', 'xyz']
        letters = ['e', 'm', 'x', 'p', 'c', 'z', 'w', 'p', 'i']
        words_from_dict = {'open', 'uproot', 'propose', 'other'}
        expected_result = ['opto', 'xyz']
        self.assertEqual(get_pure_user_words(user_words, letters, words_from_dict), expected_result)

    def test_empty_user_words(self):
        user_words = []
        letters = ['e', 'm', 'x', 'p', 'c', 'z', 'w', 'p', 'i']
        words_from_dict = {'open', 'uproot', 'propose', 'other'}
        expected_result = []
        self.assertEqual(get_pure_user_words(user_words, letters, words_from_dict), expected_result)

    def test_no_central_letter(self):
        user_words = ['apple', 'banana', 'cherry']
        letters = ['e', 'm', 'x', 'p', 'c', 'z', 'w', 'p', 'i']
        words_from_dict = {'open', 'uproot', 'propose', 'other'}
        expected_result = []
        self.assertEqual(get_pure_user_words(user_words, letters, words_from_dict), expected_result)

    def test_word_in_dictionary(self):
        user_words = ['open', 'uproot', 'propose']
        letters = ['e', 'm', 'x', 'p', 'c', 'z', 'w', 'p', 'i']
        words_from_dict = {'open', 'uproot', 'propose', 'other'}
        expected_result = []
        self.assertEqual(get_pure_user_words(user_words, letters, words_from_dict), expected_result)

    def test_word_with_central_letter(self):
        user_words = ['opto', 'open', 'uproot', 'xyz']
        letters = ['e', 'm', 'x', 'p', 'c', 'z', 'w', 'p', 'i']
        words_from_dict = {'open', 'uproot', 'propose', 'other'}
        expected_result = ['opto', 'xyz']
        self.assertEqual(get_pure_user_words(user_words, letters, words_from_dict), expected_result)

if __name__ == '__main__':
    unittest.main()
