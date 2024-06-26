import numpy as np


class BLAnalysis:

    FarmLand = ''  #

    @staticmethod
    def bla_setup(farm_length, farm_width, barren_coordinates):
        """
        Function for creating the initial 2D numpy array t indicate the farm land
        :param farm_length: length of the farm land
        :param farm_width: width of the farm land
        :param barren_coordinates: barren land coordinates from user
        """
        # creating a 2D  0's numpy array in the dimensions of farm land of int type
        BLAnalysis.FarmLand = np.zeros(shape=(farm_length, farm_width), dtype="int")
        for x1, y1, x2, y2 in barren_coordinates:  # iterating each barren land coordinates entered
            for x in range(x1, x2 + 1):  # traversing the x-axis
                for y in range(y1, y2 + 1):  # traversing the y-axis
                    BLAnalysis.FarmLand[x][y] = -1  # updating the 2D array to -1 for barren land

    @staticmethod
    def bla_analysis(farm_length, farm_width):
        """
        Function for calculating the fertile land area
        :param farm_length: length of the farm land
        :param farm_width: width of the farm land
        :return: list of fertile land areas which are sorted in ascending order
        """
        fertile_land = []  # initializing a fertile land list
        for y in range(0, farm_width):  # traversing the width of the farm
            for x in range(0, farm_length):  # traversing the length of the farm
                if BLAnalysis.FarmLand[x][y] == 0:  # if the value at point is 0 [initial/default value]
                    area = BLAnalysis.bfs(x, y, farm_length, farm_width)  # calling the bfs algorithm for the point
                    fertile_land.append(area)  # include the returned area in the initial list
        return sorted(fertile_land)  # returning the sorted area list for fertile lands

    @staticmethod
    def bfs(x, y, farm_length, farm_width):
        """
        Function for traversing array through breadth first search algorithm
        :param x: x coordinate for the point of interest
        :param y: y coordinate for the point of interest
        :param farm_length: length of the farm land
        :param farm_width: width if the farm land
        :return: returns a int after calculating the area based on point of interest
        """
        queue = [(x, y)]  # initializing a queue with the point of interest
        plot_size = 0  # initializing the area attribute to 0
        while not queue == []:  # iterator to execute until the queue is not empty
            x, y = queue.pop(0)  #
            if BLAnalysis.FarmLand[x][y] == 0:  #
                plot_size += 1  #
                BLAnalysis.FarmLand[x][y] = 1  #
                if x > 0:  #
                    queue.append((x-1, y))  #
                if x < farm_length - 1:  #
                    queue.append((x+1, y))  #
                if y > 0:  #
                    queue.append((x, y-1))  #
                if y < farm_width - 1:  #
                    queue.append((x, y+1))  #
        return plot_size  #
