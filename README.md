# Barren Land Analysis

For this case study *myRetail RESTful service, Barren Land Analysis, Document Search*, I am using **Python v3.9**. Along with the sample examples in the shared document I am using few additional test cases for robustness and code verification in all corner cases.

[Code GitHub link](https://github.com/ManishaMatta/BarrenLandAnalysis/tree/main)

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
Certainly! Here's a refactored and elaborated description of the components mentioned:

### BLA.py

**Main Class**
- **Purpose**:
  - This file serves as the main entry point for executing the entire program.
  - It consolidates the entire program flow from start to finish, ensuring smooth execution.
  - It handles and manages exceptions that may occur during execution, ensuring robustness.

**Responsibilities**:
- **Execution Flow**:
  - Initializes necessary components and resources required for the program.
  - Coordinates the interaction between different modules and classes.
  - Manages the sequence of operations required to process the farm data and compute fertile land areas.
- **Exception Handling**:
  - Implements mechanisms to capture and handle exceptions gracefully.
  - Ensures that errors or unexpected events during program execution are managed appropriately to prevent program failure.

### IO.py

**InputOutput Class**
- **Purpose**:
  - This class is responsible for managing input parameters and visualizing the farm with barren and fertile land.
  - It handles reading input data, processing it, and displaying results.

**Responsibilities**:
- **Input Handling**:
  - Provides methods to read input data, such as farm dimensions and barren land rectangles from user.
  - Validates and parses input data to ensure correctness and consistency.
- **Visualization**:
  - Implemented function to visualize the farm grid with marked barren and fertile land areas.
  - Generates graphical or textual representations of the farm to aid in understanding and analysis.

### Analysis.py

**BLAnalysis Class**
- **Purpose**:
  - This class encapsulates the logic for analyzing barren and fertile land areas using the Breadth-First Search (BFS) algorithm.

**Responsibilities**:
- **BFS Implementation**:
  - Implements the BFS algorithm to traverse the farm grid and identify contiguous areas of fertile land.
  - Manages the exploration of grid cells, ensuring that all fertile areas are accurately identified and measured.
- **Calculation**:
  - Computes and returns the areas of fertile land based on the results of BFS traversal.
  - Ensured that the algorithm efficiently handles large grids and complex configurations of barren land.

### Elaboration:

- **Integration**: BLA.py serves as the orchestrator, utilizing IO.py for input/output operations and coordinating with Analysis.py to perform the actual analysis using BFS.
- **Modularity**: Each module (BLA.py, IO.py, Analysis.py) focuses on specific responsibilities, promoting code organization and maintainability.
- **Exception Handling**: BLA.py ensures robustness by encapsulating exception handling logic, safeguarding the overall execution of the program.
- **Visualization**: IO.py enhances understanding by providing visual representations of the farm's barren and fertile areas, aiding in analysis and decision-making.

By structuring the codebase in this manner, the responsibilities are clearly delineated, promoting clarity, maintainability, and scalability of the barren land analysis application. Each component plays a crucial role in ensuring the program operates efficiently and effectively, handling various aspects from input processing to algorithmic analysis and output visualization.
#### Run Command
`python <FILE_PATH>/BLA.py <FARM_LENGTH> <FARM_WIDTH>`

## Results
The execution results for the 2 test cases are below
### Execution Video
[Execution.mp4](resources%2FExecution.mp4 "") 
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
#### Command to execute all the unit test cases
`python -m unittest discover -s tests`
#### Commands to install and map the code coverage for all classes
`pip install coverage` <-- Installing the coverage python package

`coverage run -m unittest discover -s tests` <-- executing the unit test cases to analyse the code coverage

`coverage html` <-- displaying the analysed coverage as an HTML file 

![Code_Coverage_1.png](resources%2FCode_Coverage_1.png)
![Code_Coverage_2.png](resources%2FCode_Coverage_2.png)
Please find the webpage displaying the code coverage distribution --> [index.html](resources%2Findex.html)

## Outcome

#### Time Complexity
The time complexity of using the grid method with BFS is **O(V + E)**. Here, V represents the number of nodes, which is proportional to the area of the grid (l * w), and E denotes the edges between nodes, corresponding to direct adjacency of coordinates.
#### Memory Usage
As the farm size increases, the memory storage requirements also increase. This includes both the size of the 2D array representing the farm and the queue used to store all unmarked nodes for analysis.
#### Optimization & Recommendations
Though this code resolved the problem there could still be few improvements in terms of scalability, memory usage and performance.
This problem could also be resolved by spacial compressing by reducing grid size for better memory usage.

**Spatial Compression Techniques** 
- **Sparse Matrix Representation**: Utilize sparse matrix representation for the grid to minimize memory usage, especially since most of the land might not be barren.
- **Run-Length Encoding (RLE)**: Apply RLE to compress rows of the grid, storing only the lengths of consecutive barren or fertile land segments.
- **Quadtree Decomposition**: Divide the grid into quadrants recursively until homogeneous regions are identified. This hierarchical structure simplifies the representation of land.

**BFS Algorithm Optimization**
- **Multi-threading/Multiprocessing**: Implement multi-threading or multiprocessing to parallelize BFS traversal, particularly beneficial for large grids.
- **Chunk Processing**: Divide the grid into smaller chunks and process them concurrently, merging results afterward.
- **Priority Queue**: Utilize a priority queue to prioritize cells based on specific heuristics, such as proximity to barren land.

