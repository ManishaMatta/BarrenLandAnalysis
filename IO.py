from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import os


class InputOutput:
    @staticmethod
    def stdin(farm_length, farm_width):
        """
        Function to read barren farm coordinates
        :param farm_length: total farm length
        :param farm_width: total farm width
        :return: consolidate list of all used input coordinates for barren land
        """
        barren_coordinates = []  # initializing a list for capturing coordinated for barren land
        print("Please enter the start[bottom-left] and end[top-right] coordinate for barren land in format"
              " => \"x1 y1 x2 y2\"")  # Displaying the syntax for entering barren land coordinates
        while True:  # creating a forever true loop for asking user input
            input_coordinates = input("Please enter coordinates else just press ENTER : ")  # requesting input from user
            if input_coordinates.strip() == "":  # checking if the input is empty
                break  # if empty breaking the loop, as end of user entry marked
            else:  # if the input has any other value
                string_input = input_coordinates.split(' ')  # split the user input based on space
                if len(string_input) == 4:  # checking if the user input has four values
                    coordinate = [int(c.strip()) for c in string_input]  # casting the values to int
                    if coordinate[0] < farm_length and coordinate[2] < farm_length and coordinate[1] < farm_width \
                            and coordinate[3] < farm_width:  # if the user coordinate is valid based on farm dimensions
                        barren_coordinates.append(coordinate)  # add the coordinates to the initial list
                    else:  # if values are not valid
                        # requesting the user to retry
                        print("The coordinates entered for barren land are out of bonds, Please try again")
                        continue  # continuing the loop for user retry
                else:  # if number of values entered arent 4
                    # requesting user to retry
                    print("Entered incorrect number of inputs:", input_coordinates, "Please try again")
                    continue  # continuing loop for user retry
        return barren_coordinates  # returning the barren land list after user entry

    @staticmethod
    def visualize_land(farm_length, farm_width, barren_coordinates):
        """
        Function to plot the barren land in graph for analysis and visualization
        :param farm_length: total farm length
        :param farm_width: total farm width
        :param barren_coordinates: List of barren land coordinates in farm
        Saves the plot under resource directory
        """
        fig = plt.figure()  # initialize a figure
        plt.xlim(0, farm_length)  # marking the x-axis limit
        plt.ylim(0, farm_width)  # marking the y-axis limit
        farm = plt.gca()  # requesting the current axis of the plot

        for x1, y1, x2, y2 in barren_coordinates:  # iterating through barren coordinates mentioned by user
            length = abs(x2 - x1)  # identifying the length of barren land
            width = abs(y2 - y1)  # identifying the width of barren land
            # include the barren coordinate details to the plot
            farm.add_patch(Rectangle((x1, y1), length, width, linewidth=1, edgecolor='r', facecolor="none"))
        plt.xlabel('X-axis: Farm Length')  # labeling the x-axis
        plt.ylabel('Y-axis: Farm Width')  # labeling the y-axis
        plt.title('Map with Barren Lands')  # adding a map title
        plt.grid(True)  # including grids in the map
        # creating a directory for storing the map
        os.mkdir("resources") if not os.path.exists("resources") else print("Directory exits")
        fig.savefig("resources/farm_plot.png")  # Saving the plot generated in the path mentioned
