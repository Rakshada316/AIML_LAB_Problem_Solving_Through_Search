# Problem Solving Through Search

## AIML Practical Assignment 2

This project demonstrates different search techniques used in Artificial Intelligence to solve problems.

## Problem Statement

Evaluate the performance of various algorithms such as Uninformed Search, Informed Search, Local Search and Constraint Satisfaction for problem solving through Search.

## Objectives

- To understand different problem-solving search techniques.
- To implement Uninformed Search algorithms.
- To implement Informed Search algorithms using heuristic information.
- To implement Local Search using Hill Climbing.
- To solve Sudoku using Constraint Satisfaction.
- To compare the performance of different search algorithms.

## Algorithms Implemented

The following algorithms are implemented in Python:

1. Breadth-First Search (BFS)
2. Depth-First Search (DFS)
3. A* Search
4. Greedy Best-First Search
5. Hill Climbing
6. Sudoku using Constraint Satisfaction Problem (CSP)

## Types of Search

### 1. Uninformed Search

Uninformed search does not use heuristic information.

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

### 2. Informed Search

Informed search uses heuristic information to guide the search.

- A* Search
- Greedy Best-First Search

A* uses:

`f(n) = g(n) + h(n)`

Greedy Best-First Search uses:

`f(n) = h(n)`

### 3. Local Search

Hill Climbing is a local search technique. It starts from an initial state and moves towards a better neighbouring state.

### 4. Constraint Satisfaction Problem

Sudoku is solved as a Constraint Satisfaction Problem.

The constraints are:

- No repeated number in a row.
- No repeated number in a column.
- No repeated number in a 3×3 box.

## Technology Used

- Python
- Visual Studio Code (VS Code)
- `heapq` library
- Python lists
- Dictionaries
- Sets
- Queue and Stack

## Platform Used

The programs were written, executed and tested using:

**Visual Studio Code (VS Code)**

## Project Structure

```text
Problem_Solving_Through_Search/
│
├── bfs.py
├── dfs.py
├── astar.py
├── greedy_best_first.py
├── hill_climbing.py
├── sudoku_csp.py
└── README.md
```

> Note: Change the file names above if your actual Python file names are different.

## How to Run the Programs

### Step 1

Install Python on your computer.

### Step 2

Open this project folder in Visual Studio Code.

### Step 3

Open the VS Code terminal.

### Step 4

Run the required Python program.

For example:

```bash
python bfs.py
```

Other programs can be run in the same way:

```bash
python dfs.py
python astar.py
python greedy_best_first.py
python hill_climbing.py
python sudoku_csp.py
```

## Performance Evaluation

The algorithms are compared using:

- Number of nodes or states explored
- Path cost
- Execution time
- Memory usage
- Solution quality

Different algorithms perform differently depending on the problem and search space.

## Result

All the implemented search techniques were executed successfully. The practical helped in understanding how different search strategies can be used to solve Artificial Intelligence problems.

## Conclusion

This project demonstrates Uninformed Search, Informed Search, Local Search and Constraint Satisfaction techniques. It also shows that the selection of a search algorithm depends on the type of problem, search space, available information and required solution.
