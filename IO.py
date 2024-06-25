from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import os


class InputOutput:
    @staticmethod
    def stdin(farm_length, farm_width):
        barren_coordinates = []
        print("Please enter the start[bottom-left] and end[top-right] coordinate for barren land in format"
              " => \"x1 y1 x2 y2\"")
        while True:
            input_coordinates = input("Please enter coordinates else just press ENTER : ")
            if input_coordinates.strip() == "":
                break
            else:
                string_input = input_coordinates.split(' ')
                if len(string_input) == 4:
                    coordinate = [int(c.strip()) for c in string_input]
                    if coordinate[0] < farm_length and coordinate[2] < farm_length and coordinate[1] < farm_width \
                            and coordinate[3] < farm_width:
                        barren_coordinates.append(coordinate)

                    else:
                        print("The coordinates entered for barren land are out of bonds, Please try again")
                        continue
                else:
                    print("Entered incorrect number of inputs:", input_coordinates, "Please try again")
                    continue
        return barren_coordinates

    @staticmethod
    def visualize_land(farm_length, farm_width, barren_coordinates):
        fig = plt.figure()
        plt.xlim(0, farm_length)
        plt.ylim(0, farm_width)
        farm = plt.gca()

        for x1, y1, x2, y2 in barren_coordinates:
            length = abs(x2 - x1)
            width = abs(y2 - y1)
            farm.add_patch(Rectangle((x1, y1), length, width, linewidth=1, edgecolor='r', facecolor="none"))
        plt.xlabel('X-axis: Farm Length')
        plt.ylabel('Y-axis: Farm Width')
        plt.title('Map with Barren Lands')
        plt.grid(True)
        os.mkdir("resources") if not os.path.exists("resources") else print("Directory exits")
        fig.savefig("resources/farm_plot.png")
