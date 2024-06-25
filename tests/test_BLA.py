import unittest
import BLA
from unittest.mock import patch


class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['0 2 3 4', ''])
    def test_main_1(self, mock_input):
        self.assertEqual(BLA.main([4, 5]), None)

    @patch('builtins.input', side_effect=['0 2 3 4', ''])
    @patch('builtins.exit')
    def test_main_2(self, mock_input, mock_exit):
        self.assertEqual(BLA.main([4]), None)

    # @patch('sys.argv', ['4'])
    # def test_main_with_args(self):
    #     output = BLA.main(sys.argv)
    #     self.assertEqual(output, None)


if __name__ == "__main__":
    unittest.main()
