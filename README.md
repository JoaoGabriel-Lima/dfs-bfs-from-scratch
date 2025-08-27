# DFS and BFS from scratch — Maze Solver

This repository contains from-scratch implementations of Depth-First Search (DFS) and Breadth-First Search (BFS) applied to solving text-based mazes. The goal is to practice graph fundamentals, data structures, and path reconstruction. I’m practicing as part of Harvard’s CS50 AI course: [CS50’s Introduction to AI with Python](https://www.edx.org/learn/artificial-intelligence/harvard-university-cs50-s-introduction-to-artificial-intelligence-with-python).

## Overview

- Read a maze from a plain-text file (using characters A, B, #, and space) and build a grid graph.
- Self-contained DFS and BFS implementations using Python lists as stack/queue frontiers.
- Track visited nodes and reconstruct the path from goal back to start.
- Generate a textual visualization of the maze with visited nodes and the final path, saved under `maze/maze-examples/reconstructed/`.

## Project structure

- `main.py`: entry point. Loads the maze, runs DFS and BFS, prints results, and saves reconstructions.
- `bfs/bfs.py`: BFS implementation.
- `dfs/dfs.py`: DFS implementation.
- `maze/maze.py`: maze model; creates nodes and connects neighbors (up/down/left/right) while skipping walls.
- `maze/node.py`: `MazeNode` class (coordinates, visit flags, predecessor reference, and neighbor pointers).
- `maze/reader.py`: reads maze files and reconstructs/saves the textual visualization.
- `maze/maze-examples/`: example mazes and reconstructed outputs.

## Maze input format

Each `.txt` file represents a grid maze, for example:

- `A`: start
- `B`: goal
- `#`: wall
- ` ` (space): free cell

The file is read by `MazeReader`, and `Maze` creates a 2D matrix of `MazeNode` objects, connecting non-wall neighbors.

## Algorithms implemented

Both DFS and BFS share the same core ideas:

- `visited`: prevents reprocessing nodes.
- `visited_from`: stores the predecessor to reconstruct the path.
- `get_path(start, end)`: rebuilds the route from goal to start and returns the path from start to goal.

Differences:

- DFS (`dfs/dfs.py`)
	- Uses a stack (list with `pop()` from the end) to explore depth-first.
	- Finds a path to the goal but does not guarantee the fewest steps.

- BFS (`bfs/bfs.py`)
	- Uses a queue (list with `pop(0)`) to explore breadth-first.
	- In unweighted mazes, guarantees the shortest path in number of steps.

## Console and file output

After a search completes, `MazeReader.reconstruct_text(...)` prints the reconstructed maze directly to the console (line by line) and also writes it to a file in `maze/maze-examples/reconstructed/`. The symbols used are:

- `A`: start
- `B`: goal
- `#`: wall
- `O`: final reconstructed path
- `X`: visited cells
- ` ` (space): free, unvisited cells
- `?`: fallback for missing/invalid nodes

Example (illustrative):

```text
###                 #########
#   ###################   # #
# ####                # # # #
# ################### # # # #
#                     # # # #
##################### # # # #
#XXX##OOOOOOOOXX      # # # #
#X#X##O###X##O######### # # #
#X#OOOO#XXX##B#         # # #
#X#O##X################ # # #
###O##XXXXXXXXX    #### # # #
###O############## ## # # # #
###OOOOXXXXXXXXX##    # # # #
######O########X#######X# # #
######O####XXXXXXXXXXXXX#   #
AOOOOOO######################
```

Output files follow the pattern `<maze-name>.<METHOD>.reconstructed.txt`, e.g., `2.maze.example.BFS.reconstructed.txt`.

## How to run

Requirements: Python 3.10+ (no external dependencies).

1) Choose a maze file from `maze/maze-examples/` (by default, `main.py` uses `2.maze.example.txt`).
2) Run the program:

```bash
python3 main.py
```

The script runs DFS and then BFS, prints whether a solution was found, how many nodes were visited, and the step-by-step path. The textual reconstruction is printed in the console and saved to a file.

To switch the maze, change the argument passed to `Maze(...)` in `main.py`, for example:

```python
maze = Maze("3.maze.example.txt")
```

## Implementation notes

- `Maze.connect_nodes()` connects neighbors (left/right/up/down) only when they are not walls.
- The maze is reloaded between runs to reset `visited` state before executing the second algorithm.
- `get_path(...)` uses `visited_from` to rebuild the route from goal back to start.

## About this study

This project is part of my practice while following Harvard’s CS50 Introduction to AI with Python: [CS50’s Introduction to AI with Python](https://www.edx.org/learn/artificial-intelligence/harvard-university-cs50-s-introduction-to-artificial-intelligence-with-python).

