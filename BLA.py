import sys
from IO import InputOutput
from Analysis import BLAnalysis
from datetime import datetime


def main(args):
    """
    Main Function, initiated at the start of execution
    :param args: input parameters : farm_length,farm_width
    :return: the exit code based on the execution
    """
    analysis_start_time = datetime.now()  # capture the start time for the program
    try:  # Executing the main function calls inside a try block to avoid unplanned code exceptions
        if len(args) == 2:  # verify the number of input parameters passed
            farm_length = int(args[0])  # assigning the 1st run time variable to farm length
            farm_width = int(args[1])  # assigning the 2st run time variable to farm width
        else:  # if the number of parameters are not as expected
            print("Farm Dimensions not valid, existing the analysis")  # error message in Stdout
            exit(1)  # exit the code execution with code 1

        # Calling function to read barren land dimensions from stdin
        barren_coordinates = InputOutput.stdin(farm_length, farm_width)
        # visualizing the used inputs in a matplotlip graph for better understanding of the test case
        InputOutput.visualize_land(farm_length, farm_width, barren_coordinates)
        # Sample test Codes while code development
        # barren_coordinates=[[0,292,399,307]]
        # barren_coordinates=[[48,192,351,207],[48,392,351,407],[120,52,135,547],[260,52,275,547]]
        analysis_start_time = datetime.now()  # Capturing the start time prior to analysis
        # setting up a 2D array with numpy based on input parameters
        BLAnalysis.bla_setup(farm_length, farm_width, barren_coordinates)
        # function to calculate the fertile area in the farm land
        area = BLAnalysis.bla_analysis(farm_length, farm_width)
        print("Fertile Land Area in square meters - sorted from smallest area to greatest => ",
              ' '.join([str(i) for i in area]))  # stdout for the area calculated from analysis
    except Exception as e:  # capturing any runtime exceptions while code execution
        print("Received an Exception while executing code, Please verify and rerun : ", e)  # error message
    finally:  # Code conclusion after processing
        analysis_end_time = datetime.now()  # Capturing the end date for the analysis
        print("Execution Start Time :", analysis_start_time)  # Displaying the start date
        print("Execution End Time :", analysis_end_time)  # Displaying the end date
        print("Time Taken for Analysis :", analysis_end_time-analysis_start_time)  # Displaying the execution time


if __name__ == "__main__":
    main(sys.argv[1:])  # Code Initiation
