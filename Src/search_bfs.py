# search_bfs.py
from collections import deque
from typing import Tuple, List, Optional
from .environment import Environment

def bfs(env: Environment, start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    
    rows, cols = env.rows, env.cols
    visited = set()
    queue = deque([(start, [start])])  # (current_position, path_so_far)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path  # found goal

        if (x, y) in visited:
            continue
        visited.add((x, y))

        # 4 directions (up, down, left, right)
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if env.is_valid(nx, ny) and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None  # no path found






