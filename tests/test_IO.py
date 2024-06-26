import unittest
from IO import InputOutput
from unittest.mock import patch


class TestIO(unittest.TestCase):

    @patch('builtins.input', side_effect=['0 2 3 4', ''])
    def test_stdin_1(self, mock_input):
        """
        Function test case for unit testing the stdin function with correct input parameters
        :param mock_input: mock input from stdin
        :return list of barren land coordinates
        """
        self.assertEqual(InputOutput.stdin(4, 5), [[0, 2, 3, 4]])  # assert verify the expected output for mocked inputs

    @patch('builtins.input', side_effect=['0 2 3 4 5', ''])
    def test_stdin_2(self, mock_input):
        """
        Function test case for unit testing the stdin function with incorrect input parameters
        different number of input variables
        :param mock_input: mock input from stdin
        :return list of barren land coordinates
        """
        self.assertEqual(InputOutput.stdin(4, 5), [])  # assert verify the expected output for mocked inputs

    @patch('builtins.input', side_effect=['0 2 3 6', ''])
    def test_stdin_3(self, mock_input):
        """
        Function test case for unit testing the stdin function with incorrect input parameters
        coordinate size entered by used exceeds the dimensions
        :param mock_input: mock input from stdin
        :return list of barren land coordinates
        """
        self.assertEqual(InputOutput.stdin(4, 5), [])  # assert verify the expected output for mocked inputs

    def test_visualize_land_1(self):
        """
        Function unit test case for visualization function in all scenarios
        :return: image with the plotted graph with coordinates of the barren land plotted on the farm land
        """
        # assert verify the expected output for mocked inputs, by image analysis
        self.assertEqual(InputOutput.visualize_land(4, 5, [[0, 2, 3, 4]]), None)


