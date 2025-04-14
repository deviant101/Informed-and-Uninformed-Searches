import numpy as np
from search_algorithms import SearchAgent
from visualizer import Visualizer

def main():
    # Initialize grid with normal paths
    N, M = 10, 10
    grid = np.zeros((N, M))
    
    # Define terrain features exactly as shown in the image
    walls = [(1, 3), (2, 3), (3, 3), (4, 3), (6, 6), (7, 6), (8, 6), (5, 8), (2, 7)]
    quicksand = [(3, 5), (6, 7)]
    portals = [(1, 8), (7, 0)]
    beasts = [(5, 4), (7, 2)]
    
    # Place terrain features on grid
    for w in walls:
        grid[w] = -1  # Walls (white)
    for qs in quicksand:
        grid[qs] = 2  # Quicksand (yellow)
    for p in portals:
        grid[p] = 3  # Portals (purple)
    for b in beasts:
        grid[b] = 4  # Wild Beasts (red)
    
    # Set start and goal
    grid[0, 0] = 5  # Start - green
    grid[9, 9] = 6  # Goal - blue
    
    # Initialize search agent and visualizer
    agent = SearchAgent(grid)
    viz = Visualizer(grid)
    
    # Track obstacles encountered for each algorithm
    def track_path_obstacles(path, grid):
        obstacles = {
            'Quicksand': 0,
            'Portals': 0,
            'Wild Beasts': 0
        }
        for x, y in path:
            cell = grid[x, y]
            if cell == 2:
                obstacles['Quicksand'] += 1
            elif cell == 3:
                obstacles['Portals'] += 1
            elif cell == 4:
                obstacles['Wild Beasts'] += 1
        return obstacles

    # Run all search algorithms
    algorithms = {
        'BFS': agent.bfs,
        'DFS': agent.dfs,
        'UCS': agent.ucs,
        'GBFS': agent.gbfs,
        'A*': agent.astar
    }
    
    results = {}
    
    for name, algorithm in algorithms.items():
        print(f"\n{'='*20} Running {name} {'='*20}")
        result = algorithm()
        if result:
            results[name] = result
            obstacles = track_path_obstacles(result['path'], grid)
            print(f"Path found with cost: {result['cost']}")
            print(f"Nodes expanded: {result['nodes_expanded']}")
            print(f"Time taken: {result['time']:.4f} seconds")
            print(f"Memory used: {result['memory']:.2f} MB")
            print("\nObstacles encountered:")
            for obstacle, count in obstacles.items():
                print(f"- {obstacle}: {count}")
            viz.plot_path(result['path'], name)
        else:
            print(f"No path found for {name}")
    
    # Plot performance comparison
    viz.plot_performance_comparison(results)

if __name__ == "__main__":
    main()
