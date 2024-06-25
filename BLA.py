import sys
from IO import InputOutput
from Analysis import BLAnalysis
from datetime import datetime


def main(args):
    analysis_start_time = datetime.now()
    try:
        if len(args) == 2:
            farm_length = int(args[0])
            farm_width = int(args[1])
        else:
            print("Farm Dimensions not valid, existing the analysis")
            exit(1)

        barren_coordinates = InputOutput.stdin(farm_length, farm_width)
        InputOutput.visualize_land(farm_length, farm_width, barren_coordinates)
        # barren_coordinates=[[0,292,399,307]]
        # barren_coordinates=[[48,192,351,207],[48,392,351,407],[120,52,135,547],[260,52,275,547]]
        analysis_start_time = datetime.now()
        BLAnalysis.bla_setup(farm_length, farm_width, barren_coordinates)
        area = BLAnalysis.bla_analysis(farm_length, farm_width)
        print("Fertile Land Area in square meters - sorted from smallest area to greatest => ",
              ' '.join([str(i) for i in area]))
    except Exception as e:
        print("Received an Exception while executing code, Please verify and rerun : ", e)
    finally:
        analysis_end_time = datetime.now()
        print("Execution Start Time :", analysis_start_time)
        print("Execution End Time :", analysis_end_time)
        print("Time Taken for Analysis :", analysis_end_time-analysis_start_time)


if __name__ == "__main__":
    main(sys.argv[1:])
