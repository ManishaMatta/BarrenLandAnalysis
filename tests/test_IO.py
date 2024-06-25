import unittest
from IO import InputOutput
from unittest.mock import patch


# python -m unittest discover -s tests
# pip install coverage
# coverage run -m unittest discover -s tests
# coverage html

class TestIO(unittest.TestCase):

    @patch('builtins.input', side_effect=['0 2 3 4', ''])
    def test_stdin_1(self, mock_input):
        self.assertEqual(InputOutput.stdin(4, 5), [[0, 2, 3, 4]])

    @patch('builtins.input', side_effect=['0 2 3 4 5', ''])
    def test_stdin_2(self, mock_input):
        self.assertEqual(InputOutput.stdin(4, 5), [])

    @patch('builtins.input', side_effect=['0 2 3 6', ''])
    def test_stdin_3(self, mock_input):
        self.assertEqual(InputOutput.stdin(4, 5), [])

    def test_visualize_land_1(self):
        self.assertEqual(InputOutput.visualize_land(4, 5, [[0, 2, 3, 4]]), None)
