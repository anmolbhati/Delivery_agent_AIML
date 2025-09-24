# search_astar.py
import heapq
from typing import Tuple, List, Optional
from .environment import Environment

def manhattan(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(env: Environment, start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    
    open_set = []
    heapq.heappush(open_set, (0, 0, start, [start]))  # (f, g, node, path)
    visited = {}

    while open_set:
        f, g, (x, y), path = heapq.heappop(open_set)

        if (x, y) == goal:
            return path

        if (x, y) in visited and visited[(x, y)] <= g:
            continue
        visited[(x, y)] = g

        # Explore neighbors
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if env.is_valid(nx, ny):
                cost = g + env.get_cost(nx, ny)
                h = manhattan((nx, ny), goal)
                f_new = cost + h
                heapq.heappush(open_set, (f_new, cost, (nx, ny), path + [(nx, ny)]))

    return None
