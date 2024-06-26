import unittest
import BLA
from unittest.mock import patch


class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['0 2 3 4', ''])
    def test_main_1(self, mock_input):
        """
        Function test case for unit testing the main function with correct input parameters
        :param mock_input: mock input from stdin
        :return: the execution status for the function
        """
        self.assertEqual(BLA.main([4, 5]), None)  # assert verify the expected output for mocked inputs


    @patch('builtins.input', side_effect=['0 2 3 4', ''])
    @patch('builtins.exit')
    def test_main_2(self, mock_input, mock_exit):
        """
        Function test case for unit testing the main function with incorrect input arguments
        :param mock_input: mock input for stdin
        :param mock_exit: mock exit commands for testing exception handling
        :return: the execution status of the function
        """
        self.assertEqual(BLA.main([4]), None)  # assert verify the expected output for mocked inputs

    # @patch('sys.argv', ['4'])
    # def test_main_with_args(self):
    #     output = BLA.main(sys.argv)
    #     self.assertEqual(output, None)


if __name__ == "__main__":
    unittest.main()  # initiating the unittest main class
