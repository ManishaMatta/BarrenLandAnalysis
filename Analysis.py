import numpy as np


class BLAnalysis:

    FarmLand = ''

    @staticmethod
    def bla_setup(farm_length, farm_width, barren_coordinates):
        BLAnalysis.FarmLand = np.zeros(shape=(farm_length, farm_width), dtype="int")
        for x1, y1, x2, y2 in barren_coordinates:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    BLAnalysis.FarmLand[x][y] = -1

    @staticmethod
    def bla_analysis(farm_length, farm_width):
        fertile_land = []
        for y in range(0, farm_width):
            for x in range(0, farm_length):
                if BLAnalysis.FarmLand[x][y] == 0:
                    area = BLAnalysis.bfs(x, y, farm_length, farm_width)
                    fertile_land.append(area)
        return sorted(fertile_land)

    @staticmethod
    def bfs(x, y, farm_length, farm_width):
        queue = [(x, y)]
        plot_size = 0
        while not queue == []:
            x, y = queue.pop(0)
            if BLAnalysis.FarmLand[x][y] == 0:
                plot_size += 1
                BLAnalysis.FarmLand[x][y] = 1
                if x > 0:
                    queue.append((x-1, y))
                if x < farm_length - 1:
                    queue.append((x+1, y))
                if y > 0:
                    queue.append((x, y-1))
                if y < farm_width - 1:
                    queue.append((x, y+1))
        return plot_size
