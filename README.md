# Puzzle

## Description

This project implements a program to solve a problem of building the longest sequence of numbers, where each number ends with the last two digits of the next number. The program allows users to upload a file with numbers, find the longest path in the form of a graph, and display the result in both detailed and compact formats.

## Functionality

1. **Reading data from a file:** The user can select a text file containing numbers for further processing.
2. **Building the graph:** Each number is compared with others to build a graph where edges connect numbers that share the same last two digits.
3. **Finding the longest path:** The program finds the longest path through the numbers in the graph, where each number ends with the last two digits of the next one.
4. **Displaying results:** The results are presented in two formats:
   - **Detailed result:** Shows the path with the numbers and their corresponding digits.
   - **Compact result:** Displays the simplified form of the path.

## Requirements

- Python 3.x
- Libraries:
  - `tkinter` (for creating the graphical interface)
  - `collections`

## Instructions

1. Make sure you have Python 3.x installed. To check, enter:
   ```bash
   python --version
   ```

2. Run the program:
   ```bash
   python BAD_test.py
   ```

3. Select a text file with numbers using the "Choose File" button.

4. The program will process the data and display two types of results:
   - **Detailed result** (will show numerical values with their corresponding digits).
   - **Compact result** (a simplified format without extra symbols).

## Sample Input

The file may contain a list of numbers, each on a new line. For example:

```
123456
567890
901234
345678
```

## Sample Output

After processing, the program will display something like this:

- **Detailed result:** `1234(56)78(90)12(34)56`
- **Compact result:** `1234567890123456`
