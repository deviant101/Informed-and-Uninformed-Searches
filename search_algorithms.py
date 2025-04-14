from collections import deque
import heapq
import time
import tracemalloc
from typing import List, Tuple, Dict

class SearchAgent:
    def __init__(self, grid):
        self.grid = grid
        self.rows, self.cols = grid.shape
        self.start = (0, 0)
        self.goal = (9, 9)
        # Add portal pairs mapping
        self.portal_pairs = {(1, 8): (7, 0), (7, 0): (1, 8)}  # bidirectional portals

    def get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        x, y = pos
        neighbors = []
        
        # First check if current position is a portal
        if self.grid[pos] == 3:  # Portal
            portal_dest = self.portal_pairs.get(pos)
            if portal_dest:
                neighbors.append(portal_dest)
                
        # Add regular adjacent neighbors
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < self.rows and 
                0 <= new_y < self.cols and 
                self.grid[new_x, new_y] != -1):  # not a wall
                neighbors.append((new_x, new_y))
                
        return neighbors
    
    def get_cost(self, pos: Tuple[int, int]) -> int:
        cell_type = self.grid[pos]
        # Terrain costs as per specification
        costs = {
            0: 1,    # Normal Path
            -1: float('inf'),  # Wall
            2: 3,    # Quicksand
            3: 0,    # Portal
            4: 5,    # Wild Beasts
            5: 0,    # Start
            6: 0     # Goal
        }
        return costs.get(cell_type, float('inf'))
        
    def manhattan_distance(self, pos: Tuple[int, int]) -> int:
        return abs(pos[0] - self.goal[0]) + abs(pos[1] - self.goal[1])

    def bfs(self):
        tracemalloc.start()
        start_time = time.time()
        
        queue = deque([(self.start, [self.start])])  # Removed cost
        visited = {self.start}
        nodes_expanded = 0
        
        while queue:
            current, path = queue.popleft()  # Removed cost unpacking
            nodes_expanded += 1
            
            if current == self.goal:
                # Calculate cost only after finding path
                path_cost = sum(self.get_cost(pos) for pos in path[1:])  # Skip start position
                end_time = time.time()
                memory_current, memory_peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                return {
                    'path': path,
                    'cost': path_cost,
                    'nodes_expanded': nodes_expanded,
                    'time': end_time - start_time,
                    'memory': memory_peak / 10**6  # Convert to MB
                }
            
            for next_pos in self.get_neighbors(current):
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, path + [next_pos]))  # Removed cost tracking

    def dfs(self):
        tracemalloc.start()
        start_time = time.time()
        
        stack = [(self.start, [self.start])]  # Removed cost
        visited = {self.start}
        nodes_expanded = 0
        
        while stack:
            current, path = stack.pop()  # Removed cost unpacking
            nodes_expanded += 1
            
            if current == self.goal:
                # Calculate cost only after finding path
                path_cost = sum(self.get_cost(pos) for pos in path[1:])  # Skip start position
                end_time = time.time()
                memory_current, memory_peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                return {
                    'path': path,
                    'cost': path_cost,
                    'nodes_expanded': nodes_expanded,
                    'time': end_time - start_time,
                    'memory': memory_peak / 10**6
                }
            
            for next_pos in reversed(self.get_neighbors(current)):
                if next_pos not in visited:
                    visited.add(next_pos)
                    stack.append((next_pos, path + [next_pos]))  # Removed cost tracking

    def ucs(self):
        tracemalloc.start()
        start_time = time.time()
        
        pq = [(0, self.start, [self.start])]
        visited = set()
        nodes_expanded = 0
        
        while pq:
            cost, current, path = heapq.heappop(pq)
            
            if current in visited:
                continue
                
            visited.add(current)
            nodes_expanded += 1
            
            if current == self.goal:
                end_time = time.time()
                memory_current, memory_peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                return {
                    'path': path,
                    'cost': cost,
                    'nodes_expanded': nodes_expanded,
                    'time': end_time - start_time,
                    'memory': memory_peak / 10**6
                }
            
            for next_pos in self.get_neighbors(current):
                if next_pos not in visited:
                    new_cost = cost + self.get_cost(next_pos)
                    heapq.heappush(pq, (new_cost, next_pos, path + [next_pos]))
        
        tracemalloc.stop()
        return None

    def gbfs(self):
        tracemalloc.start()
        start_time = time.time()
        
        pq = [(self.manhattan_distance(self.start), self.start, [self.start], 0)]
        visited = set()
        nodes_expanded = 0
        
        while pq:
            _, current, path, cost = heapq.heappop(pq)
            
            if current in visited:
                continue
                
            visited.add(current)
            nodes_expanded += 1
            
            if current == self.goal:
                end_time = time.time()
                memory_current, memory_peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                return {
                    'path': path,
                    'cost': cost,
                    'nodes_expanded': nodes_expanded,
                    'time': end_time - start_time,
                    'memory': memory_peak / 10**6
                }
            
            for next_pos in self.get_neighbors(current):
                if next_pos not in visited:
                    new_cost = cost + self.get_cost(next_pos)
                    heapq.heappush(pq, (
                        self.manhattan_distance(next_pos),
                        next_pos,
                        path + [next_pos],
                        new_cost
                    ))
        
        tracemalloc.stop()
        return None

    def astar(self):
        tracemalloc.start()
        start_time = time.time()
        
        pq = [(0 + self.manhattan_distance(self.start), 0, self.start, [self.start])]
        visited = set()
        nodes_expanded = 0
        
        while pq:
            _, cost, current, path = heapq.heappop(pq)
            
            if current in visited:
                continue
                
            visited.add(current)
            nodes_expanded += 1
            
            if current == self.goal:
                end_time = time.time()
                memory_current, memory_peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                return {
                    'path': path,
                    'cost': cost,
                    'nodes_expanded': nodes_expanded,
                    'time': end_time - start_time,
                    'memory': memory_peak / 10**6
                }
            
            for next_pos in self.get_neighbors(current):
                if next_pos not in visited:
                    new_cost = cost + self.get_cost(next_pos)
                    f_cost = new_cost + self.manhattan_distance(next_pos)
                    heapq.heappush(pq, (f_cost, new_cost, next_pos, path + [next_pos]))
        
        tracemalloc.stop()
        return None
