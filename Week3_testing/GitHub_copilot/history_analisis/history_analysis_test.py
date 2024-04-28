import unittest
from history_analysis import sites_on_date, most_frequent_sites, get_url_info

class TestHistoryAnalysis(unittest.TestCase):

    def setUp(self):
        self.visits = [
            ('https://www.youtube.com/', 'YouTube', '2023-10-23', '11:55:31.705320', 0),
            ('https://www.youtube.com/', 'YouTube', '2023-10-22', '11:55:31.705320', 1083473),
            ('https://www.instagram.com/', 'Instagram', '2023-10-23', '11:55:39.190008', 467439),
            ('https://www.cms.ucu.edu.ua/my/index.php', 'Dashboard', '2023-10-23', '11:56:03.912323', 0),
            ('https://www.instagram.com/', 'Instagram', '2023-10-23', '11:55:39.655687', 414254256),
            ('https://www.youtube.com/', 'YouTube', '2023-10-22', '11:55:34.348591', 1006174780)
        ]

    def test_sites_on_date(self):
        self.assertEqual(sites_on_date(self.visits, '2023-10-22'), {'https://www.youtube.com/'})
        self.assertEqual(sites_on_date(self.visits, '2023-10-23'), {'https://www.youtube.com/', 'https://www.instagram.com/', 'https://www.cms.ucu.edu.ua/my/index.php'})

    def test_most_frequent_sites(self):
        self.assertEqual(most_frequent_sites(self.visits, 10), {'https://www.instagram.com/', 'https://www.youtube.com/', 'https://www.cms.ucu.edu.ua/my/index.php'})
        self.assertEqual(most_frequent_sites(self.visits, 2), {'https://www.instagram.com/', 'https://www.youtube.com/'})

    def test_get_url_info(self):
        self.assertEqual(get_url_info(self.visits, 'https://www.youtube.com/'), ('YouTube', '2023-10-23', '11:55:31.705320', 2, 542369736.5))
        self.assertEqual(get_url_info(self.visits, 'https://www.instagram.com/'), ('Instagram', '2023-10-23', '11:55:39.655687', 2, 207827347.5))
        self.assertEqual(get_url_info(self.visits, 'https://www.cms.ucu.edu.ua/my/index.php'), ('Dashboard', '2023-10-23', '11:56:03.912323', 1, 0))

if __name__ == '__main__':
    unittest.main()
