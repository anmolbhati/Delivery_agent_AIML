# search_local.py
import random
from typing import Tuple, List, Optional
from .environment import Environment

def manhattan(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def hill_climbing(env: Environment, start: Tuple[int, int], goal: Tuple[int, int], max_restarts: int = 10) -> Optional[List[Tuple[int, int]]]:
    
    best_path = None
    best_score = float("inf")

    for _ in range(max_restarts):
        current = start
        path = [current]
        visited = set()

        while current != goal:
            visited.add(current)
            neighbors = []
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = current[0] + dx, current[1] + dy
                if env.is_valid(nx, ny) and (nx, ny) not in visited:
                    neighbors.append((nx, ny))

            if not neighbors:
                break  # dead end

            # Choose the neighbor with best heuristic (greedy move)
            current = min(neighbors, key=lambda n: manhattan(n, goal))
            path.append(current)

            # Small random chance to jump to a random neighbor (to escape local minima)
            if random.random() < 0.1:
                current = random.choice(neighbors)
                path.append(current)

        # Track best attempt
        if current == goal and len(path) < best_score:
            best_score = len(path)
            best_path = path

    return best_path
