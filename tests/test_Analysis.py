import unittest
from Analysis import BLAnalysis


class TestAnalysis(unittest.TestCase):

    def test_FarmLand(self):
        self.assertEqual(BLAnalysis.FarmLand, '')

    def test_bla_setup(self):
        self.assertEqual(BLAnalysis.bla_setup(4, 5, [[0, 2, 3, 4]]), None)

    def test_bla_analysis(self):
        BLAnalysis.FarmLand = [[0, 0, -1, -1, -1], [0, 0, -1, -1, -1], [0, 0, -1, -1, -1], [0, 0, -1, -1, -1]]
        self.assertEqual(BLAnalysis.bla_analysis(4, 5), [8])

    def test_bfs(self):
        BLAnalysis.FarmLand = [[0, 0, -1, -1, -1], [0, 0, -1, -1, -1], [0, 0, -1, -1, -1], [0, 0, -1, -1, -1]]
        self.assertEqual(BLAnalysis.bfs(0, 0, 4, 5), 8)
