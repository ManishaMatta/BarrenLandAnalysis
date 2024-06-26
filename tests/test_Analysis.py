import unittest
from Analysis import BLAnalysis


class TestAnalysis(unittest.TestCase):

    def test_FarmLand(self):
        """
        Function test case for unit testing the farmland global variable
        :return: the farmland variable post initialization
        """
        self.assertEqual(BLAnalysis.FarmLand, '')  # assert verify the default values of the variable

    def test_bla_setup(self):
        """
        Function test case for unit testing for setting up the distribution of farm land
        :return: 2D array which depicts the farm land distribution
        """
        self.assertEqual(BLAnalysis.bla_setup(4, 5, [[0, 2, 3, 4]]), None)  # assert verify the expected output

    def test_bla_analysis(self):
        """
        Function test case for unit testing for analysis the farm for fertile lands
        :return: list of fertile land areas
        """
        # mock input for the farm distribution
        BLAnalysis.FarmLand = [[0, 0, -1, -1, -1], [0, 0, -1, -1, -1], [0, 0, -1, -1, -1], [0, 0, -1, -1, -1]]
        self.assertEqual(BLAnalysis.bla_analysis(4, 5), [8])  # assert verify the expected output for mocked inputs

    def test_bfs(self):
        """
        Function test case for unit testing for bfs analysis based on a start point
        :return: the area for the fertile land
        """
        # mock input for the farm distribution
        BLAnalysis.FarmLand = [[0, 0, -1, -1, -1], [0, 0, -1, -1, -1], [0, 0, -1, -1, -1], [0, 0, -1, -1, -1]]
        self.assertEqual(BLAnalysis.bfs(0, 0, 4, 5), 8)  # assert verify the expected output for mocked inputs
