import unittest
from cmudict_4 import *

class TestCmudict(unittest.TestCase):
    def test_dict_reader_tuple(self):
        file_dict = "NACHOS 1 N AA1 CH OW0 Z"
        expected_output = [("NACHOS", 1, ["N", "AA1", "CH", "OW0", "Z"])]
        self.assertEqual(dict_reader_tuple(file_dict), expected_output)

        file_dict = "HELLO 3 HH EH1 L OW0"
        expected_output = [("HELLO", 3, ["HH", "EH1", "L", "OW0"])]
        self.assertEqual(dict_reader_tuple(file_dict), expected_output)

    def test_dict_reader_dict(self):
        file_dict = "NACHOS 2 N AE1 CH OW0 Z"
        expected_output = {"NACHOS": {("N", "AE1", "CH", "OW0", "Z"), ("N", "AA1", "CH", "OW0", "Z")}}
        self.assertEqual(dict_reader_dict(file_dict), expected_output)

        file_dict = "HELLO 1 HH EH1 L OW0"
        expected_output = {"HELLO": {("HH", "EH1", "L", "OW0")}}
        self.assertEqual(dict_reader_dict(file_dict), expected_output)

    def test_dict_invert(self):
        input_dict = {"WATER": {("W", "A", "T", "E", "R")}}
        expected_output = {1: {("WATER", ("W", "A", "T", "E", "R"))}}
        self.assertEqual(dict_invert(input_dict), expected_output)

        input_dict = {
            "AABERG": {("AA1", "B", "ER0", "G")},
            "A.": {("EY1",)},
            "A": {("EY1",), ("AH0",)},
            "A42128": {("EY1", "F", "AO1", "R", "T", "UW1", "W", "AH1", "N", "T", "UW1", "EY1", "T")},
            "AAA": {("T", "R", "IH2", "P", "AH0", "L", "EY1")}
        }
        expected_output = {
            1: {
                ("A.", ("EY1",)),
                ("AABERG", ("AA1", "B", "ER0", "G")),
                ("AAA", ("T", "R", "IH2", "P", "AH0", "L", "EY1")),
                ("A42128", ("EY1", "F", "AO1", "R", "T", "UW1", "W", "AH1", "N", "T", "UW1", "EY1", "T"))
            },
            2: {
                ("A", ("EY1",)),
                ("A", ("AH0",))
            }
        }
        self.assertEqual(dict_invert(input_dict), expected_output)

        input_dict = {
            "HELLO": {("HH", "EH1", "L", "OW0")},
            "WORLD": {("W", "ER1", "L", "D")},
            "PYTHON": {("P", "AY1", "TH", "AH0", "N"), ("P", "AY1", "TH", "AH0", "N", "S")}
        }
        expected_output = {
            1: {
                ("HELLO", ("HH", "EH1", "L", "OW0")),
                ("WORLD", ("W", "ER1", "L", "D"))
            },
            2: {
                ("PYTHON", ("P", "AY1", "TH", "AH0", "N")),
                ("PYTHON", ("P", "AY1", "TH", "AH0", "N", "S"))
            }
        }
        self.assertEqual(dict_invert(input_dict), expected_output)

    def test_dict_reader_tuple_edge_cases(self):
        file_dict = ""
        expected_output = []
        self.assertEqual(dict_reader_tuple(file_dict), expected_output)

        file_dict = "WORD"
        expected_output = [("WORD", 0, [])]
        self.assertEqual(dict_reader_tuple(file_dict), expected_output)

    def test_dict_reader_dict_edge_cases(self):
        file_dict = ""
        expected_output = {}
        self.assertEqual(dict_reader_dict(file_dict), expected_output)

        file_dict = "WORD"
        expected_output = {"WORD": set()}
        self.assertEqual(dict_reader_dict(file_dict), expected_output)

    def test_dict_invert_edge_cases(self):
        input_dict = {}
        expected_output = {}
        self.assertEqual(dict_invert(input_dict), expected_output)

        input_dict = {"WORD": set()}
        expected_output = {0: {("WORD", ())}}
        self.assertEqual(dict_invert(input_dict), expected_output)

if __name__ == "__main__":
    unittest.main()
