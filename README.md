# Barren Land Analysis

For this case study *myRetail RESTful service, Barren Land Analysis, Document Search*, I am using **Python v3.9** and sample examples in the shared document as my test cases for conducting the study.

[GitHub link](https://github.com/ManishaMatta/BarrenLandAnalysis/tree/main)

## Technical Assessment Case Studies
```
2.Barren Land Analysis

You have a farm of 400m by 600m where coordinates of the field are from (0, 0) to (399, 599). A portion of the farm is barren, and all the barren land is in the form of rectangles. Due to these rectangles of barren land, the remaining area of fertile land is in no particular shape. An area of fertile land is defined as the largest area of land that is not covered by any of the rectangles of barren land.
Read input from STDIN. Print output to STDOUT
Input : You are given a set of rectangles that contain the barren land. These rectangles are defined in a string, which consists of four integers separated by single spaces, with no additional spaces in the string. The first two integers are the coordinates of the bottom left corner in the given rectangle, and the last two integers are the coordinates of the top right corner.
Output : Output all the fertile land area in square meters, sorted from smallest area to greatest, separated by a space. 	
```
Sample Input | Sample Output 
--- | --- 
{“0 292 399 307”} | 116800  116800
{“48 192 351 207”, “48 392 351 407”, “120 52 135 547”, “260 52 275 547”} | 22816 192608 

## Solution
To understand the problem statement above, I first plotted the points on a graph to analyze the results. 
Through this analysis, I understood that the output area depends on the distinct areas separated by the barren land fields mentioned in the input. 
Further analysis revealed that we can represent the farmland as a 2D matrix, where we can map the barren lands.
The CodeBase is divided into 3 major sections/classes:
- **BLA.py** 
  - *main class* This is the entry point for executing the code. It consolidates the entire program flow from start to finish, handling and managing exceptions during execution etc.
- **IO.py**
  - *InputOutput class* This class primarily contains all functions related to input parameters and visualizing the farm with barren and fertile land.
- **Analysis.py**
  - *BLAnalysis class* This class implements the breadth-first search (BFS) algorithm to identify the area of fertile land.

#### Run Command
`python <FILE_PATH>/BLA.py <FARM_LENGTH> <FARM_WIDTH>`

## Results
The execution results for the 2 test cases are below
### Test Case 1
#### Execution Summary
![execution_1.png](resources%2Fexecution_1.png)
#### Visualization 
![farm_plot_1.png](resources%2Ffarm_plot_1.png)
### Test Case 2
#### Execution Summary
![execution_2.png](resources%2Fexecution_2.png)
#### Visualization
![farm_plot_2.png](resources%2Ffarm_plot_2.png)

> NOTE: The output result is highlighted in the red box.

## Code Coverage
The Codebase was unit tested with 99% coverage with `unitest` python package.
![Code_Coverage_1.png](resources%2FCode_Coverage_1.png)
![Code_Coverage_2.png](resources%2FCode_Coverage_2.png)
Please find the webpage displaying the code coverage distribution --> [index.html](resources%2Findex.html)

## Execution Video
[Execution.mp4](resources%2FExecution.mp4)

## Recommendations
Though this code resolved the problem there could still be few improvements in terms of scalability, memory usage and performance.
This problem could also be resolved by compressing the grid for better memory usage.
