import unittest
from datetime import datetime
from chrome_history import most_frequent_sites, get_url_info

class TestMyFunctions(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.visits = [
            ('https://youtube.com/', 'YouTube', '2023-10-23', '11:55:31.705320', 0),
            ('https://youtube.com/', 'YouTube', '2023-10-22', '11:55:31.705320', 1083473),
            ('https://www.instagram.com/', 'Instagram', '2023-10-23', '11:55:39.190008', 467439),
            ('https://cms.ucu.edu.ua/my/index.php', 'Dashboard', '2023-10-23', '11:56:03.912323', 0),
            ('https://www.instagram.com/', 'Instagram', '2023-10-23', '11:55:39.655687', 414254256),
            ('https://youtube.com/', 'YouTube', '2023-10-22', '11:55:34.348591', 1006174780)
        ]

    def test_most_frequent_sites(self):
        # Test case with 3 most frequent sites
        result = most_frequent_sites(self.visits, 3)
        expected = {'https://www.instagram.com/', 'https://youtube.com/', 'https://cms.ucu.edu.ua/my/index.php'}
        self.assertEqual(result, expected)

        # Test case with 2 most frequent sites
        result = most_frequent_sites(self.visits, 2)
        expected = {'https://www.instagram.com/', 'https://youtube.com/'}
        self.assertEqual(result, expected)

        # Test case with 10 most frequent sites (all available)
        result = most_frequent_sites(self.visits, 10)
        expected = {'https://www.instagram.com/', 'https://youtube.com/', 'https://cms.ucu.edu.ua/my/index.php'}
        self.assertEqual(result, expected)

        # Test case with empty visits list
        result = most_frequent_sites([], 5)
        expected = set()
        self.assertEqual(result, expected)

    def test_get_url_info(self):
        # Test case with existing URL
        result = get_url_info(self.visits, 'https://youtube.com/')
        expected = ('YouTube', '2023-10-23', '11:55:31.705320', 1083473, 0)
        self.assertEqual(result, expected)

        # Test case with non-existing URL
        result = get_url_info(self.visits, 'https://example.com/')
        expected = ('', '', '', 0, 0)
        self.assertEqual(result, expected)

        # Test case with empty visits list
        result = get_url_info([], 'https://youtube.com/')
        expected = ('', '', '', 0, 0)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
