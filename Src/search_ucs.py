# search_ucs.py
import heapq
from typing import Tuple, List, Optional
from .environment import Environment

def ucs(env: Environment, start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    
    rows, cols = env.rows, env.cols
    visited = set()
    pq = [(0, start, [start])]  # (cost_so_far, current_pos, path_so_far)

    while pq:
        cost, (x, y), path = heapq.heappop(pq)

        if (x, y) == goal:
            return path  # found goal

        if (x, y) in visited:
            continue
        visited.add((x, y))

        # 4 directions (up, down, left, right)
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if env.is_valid(nx, ny) and (nx, ny) not in visited:
                new_cost = cost + env.get_cost(nx, ny)
                heapq.heappush(pq, (new_cost, (nx, ny), path + [(nx, ny)]))

    return None  # no path found
