## Banker's-Algorithm

The Banker's Algorithm is a resource allocation and deadlock avoidance algorithm used in operating systems. This repository provides an implementation of the Banker's Algorithm in [programming language], allowing you to understand and simulate how the algorithm works.

## Overview

The Banker's Algorithm is designed to prevent deadlock in systems that allocate resources to multiple processes. It ensures that resources are allocated in a safe and deadlock-free manner by analyzing the current state of the system and the resource requests made by processes.

## Requirements

- Python 3.9
- PyQt5 library

## Installation

Follow these steps:

1. Ensure that you have Python 3.9 or a compatible version installed on your system. You can download Python from the official Python website: [https://www.python.org](https://www.python.org)

2. Clone this repository to your local machine or download and extract the ZIP file.

3. To install the required library, run the following command in the terminal:

    ```shell
    pip install pyqt5
    ```

## Usage

1. Open a terminal or command prompt and navigate to the project directory.

2. - Run the following code in the terminal:

      ```shell
      python source_code.py
      ```
      
   - The following window will appear:
   
   ![Main GUI](/images/image1.png "Main GUI")
   
 3. - Fill in the data for the Number of Processes and Number of Resources:

    ![Main GUI](/images/image2.png "Main GUI")
    
 4. - Click the Generate Input Fields to fill the tables with input fields. If you want to load an example, press the Load Example button to fill in the tables with data:

    ![Main GUI](/images/image3.png "Main GUI")

 5. - After filling in the Total Resources, Current Allocation, and Maximum Need tables press the Calculate Avaialbe button to calulate and fill in the Avaiable Resources: 
    
    ![Main GUI](/images/image4.png "Main GUI")

 6. - Press the Calculate Need button to calculate the Remaining Need matrix:
    
    ![Main GUI](/images/image5.png "Main GUI")

 7. - Choose the Process that you want to request the Resources for, then input the amount of resources you want to request in the table. After that press the Request Resources button:

    ![Main GUI](/images/image6.png "Main GUI")
    
 8. - A new window will appear with the newly updated tables. Press the Check Request button to check if the sequence is safe:

    ![Results GUI](/images/image7.png "Main GUI")

 9. - If the Sequence is safe, then a message will appear with the safe sequence:

    ![Results GUI](/images/image8.png "Main GUI")


## Contribution

Contributions to this repository are welcome. If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue. Please follow the repository's code of conduct and guidelines for contributing.
