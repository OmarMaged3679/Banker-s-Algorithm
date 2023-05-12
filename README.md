## Banker's-Algorithm GUI

The Banker's Algorithm is a resource allocation and deadlock avoidance algorithm used in operating systems. It ensures that resources are allocated in a safe and deadlock-free manner by analyzing the current state of the system and the resource requests made by processes. This project provides a graphical user interface (GUI) implementation of the Banker's Algorithm using Python. The GUI allows users to interact with the algorithm visually and provides an intuitive way to input data, run simulations, and observe the results. Please refer to the [Installation](#installation) section for instructions on how to set up the environment and install the necessary dependencies. Once the installation is complete, you can run the program and start using the Banker's Algorithm GUI.

## Requirements

- Python 3.9
- PyQt5 library

## Installation

Follow these steps:

1. Ensure that you have Python 3.9 or a compatible version installed on your system. You can download Python from the official Python website: [https://www.python.org](https://www.python.org)

2. To install the required library, run the following command in the terminal:

    ```shell
    pip install pyqt5
    ```
3. Clone this repository to your local machine or download and extract the ZIP file.

4. Open a terminal or command prompt and navigate to the project directory, then run the following code in the terminal:

      ```shell
      python source_code.py
      ```
      
   - The following window will appear:
   
   ![Main GUI](/images/image1.png "Main GUI")

## Usage
   
 1. -Begin by entering the values for the **Number of Processes** and **Number of Resources** fields:

    ![Main GUI](/images/image2.png "Main GUI")
    
 2. To set up the tables with input fields, follow these steps:
       - Click the **Generate Input Fields** button. This will create tables where you can enter your own data.

       Alternatively, you can load an example by:
       - Clicking the **Load Example** button. This will automatically fill the tables with pre-defined data, providing a ready-to-use example.

    ![Main GUI](/images/image3.png "Main GUI")

 3. - After filling in the **Total Resources**, **Current Allocation**, and **Maximum Need** tables, click the **Calculate Available** button to calculate and populate the 'Available Resources' table:
    
    ![Main GUI](/images/image4.png "Main GUI")

 4. - Click the **Calculate Need** button to calculate and display the **Remaining Need** table:
    
    ![Main GUI](/images/image5.png "Main GUI")

 5. - To request resources for a process, follow these steps:
        a. Select the process for which you want to request resources from the table.<br />
        b. Enter the amount of resources you wish to request for the selected process in the corresponding table cell.<br />
        c. Click the **Request Resources** button to initiate the resource request.<br />

    ![Main GUI](/images/image6.png "Main GUI")
    
 6. - After clicking the 'Request Resources' button, a new window will open, displaying the updated tables. To verify the safety of the resource allocation sequence, click the **Check Request** button:

    ![Results GUI](/images/image7.png "Main GUI")

 7. - If the sequence is determined to be safe, a message will appear displaying the safe sequence:

    ![Results GUI](/images/image8.png "Main GUI")


## Contribution

Contributions to this repository are welcome. If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue. Please follow the repository's code of conduct and guidelines for contributing.
