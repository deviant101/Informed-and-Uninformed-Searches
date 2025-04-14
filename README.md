# The Quest for a Treasure: A Comparative Analysis of Search Algorithms

This project implements and compares various informed and uninformed search algorithms in a grid-based environment representing a magical forest. The goal is to find an optimal path from a start point to a goal point while navigating through different terrain types with varying traversal costs.

## Project Overview

In this magical forest, a brave explorer named Arin embarks on an adventure to find a treasure hidden inside an ancient temple. The forest is represented as a grid with different terrain types:

- **Normal Path**: Easy to traverse (cost: 1)
- **Walls**: Impassable obstacles
- **Quicksand**: Slows movement (cost: 3)
- **Portals**: Instant teleportation to another location (cost: 0)
- **Wild Beasts**: Dangerous areas (cost: 5)

The explorer starts at the Campfire Point (S) and must reach the Temple (G) using the most efficient path.

## Implemented Search Algorithms

The project implements five search algorithms:

1. **Breadth-First Search (BFS)**: An uninformed search algorithm that expands the shallowest unexpanded node.
2. **Depth-First Search (DFS)**: An uninformed search algorithm that expands the deepest unexpanded node.
3. **Uniform-Cost Search (UCS)**: An uninformed search algorithm that expands the node with the lowest path cost.
4. **Greedy Best-First Search (GBFS)**: An informed search algorithm that expands the node estimated to be closest to the goal.
5. **A* Search**: An informed search algorithm that combines UCS and GBFS to find optimal paths efficiently.

## Performance Metrics

Each algorithm is evaluated based on the following metrics:
- **Path Cost**: The total cost of the path found
- **Nodes Expanded**: The number of nodes processed during the search
- **Execution Time**: The time taken to find a path (measured in seconds)
- **Memory Usage**: The peak memory consumption (measured in MB)
- **Obstacles Encountered**: The number and types of obstacles faced along the path

## Project Structure

- `main.py`: Entry point of the program. Sets up the grid, runs the search algorithms, and displays results.
- `search_algorithms.py`: Contains the implementation of the five search algorithms.
- `visualizer.py`: Handles visualization of the grid, paths, and performance comparisons.

## Running the Project

To run the project:

```bash
python main.py
```

This will execute all five search algorithms on the grid, display the paths found, and show performance comparisons.

## Visualization

The project provides two types of visualizations:

1. **Path Visualization**: For each algorithm, the found path is plotted on the grid with different colors representing different terrain types.
2. **Performance Comparison**: Bar charts comparing the execution time, memory usage, and nodes expanded for each algorithm.

## Terrain Information

| Terrain Type | Marker | Description | Cost | Color |
|--------------|--------|-------------|------|-------|
| Normal Path | 0 | Walkable terrain | 1 | Light Gray |
| Wall (❌) | -1 | Impassable obstacle | ∞ | White |
| Quicksand (⏳) | 2 | Slows movement | 3 | Yellow |
| Portal (🔄) | 3 | Instantly moves to exit | 0 | Purple |
| Wild Beasts (⚠️) | 4 | Dangerous area | 5 | Red |
| Start (S) | 5 | Starting position | 0 | Green |
| Goal (G) | 6 | Target location | 0 | Blue |

## Requirements

- Python 3.x
- NumPy
- Matplotlib
