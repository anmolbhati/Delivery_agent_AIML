# agent.py
from typing import List, Tuple
from .environment import Environment
from .search_bfs import bfs
from .search_ucs import ucs
from .searchAstar import astar
from .search_local import hill_climbing


class Agent:
    def __init__(self, environment: Environment, start: Tuple[int, int], goal: Tuple[int, int]):
        self.env = environment
        self.start = start
        self.goal = goal
        self.current_position = start
        self.path: List[Tuple[int, int]] = []   # stores planned path
        self.cost: int = 0                      # total path cost

    def set_path(self, path: List[Tuple[int, int]], cost: int):
        """Store path and cost for the agent."""
        self.path = path
        self.cost = cost

    def move_step(self):
        """Move one step along the planned path."""
        if not self.path:
            return False
        self.current_position = self.path.pop(0)
        return True

    def reached_goal(self) -> bool:
        """Check if the agent has reached the goal."""
        return self.current_position == self.goal

    # -------------------- SEARCH PLANNERS --------------------

    def plan_with_bfs(self):
        """Plan a path from start to goal using BFS."""
        path = bfs(self.env, self.start, self.goal)
        if path:
            self.set_path(path, cost=len(path))
            return True
        return False

    def plan_with_ucs(self):
        """Plan a path from start to goal using Uniform-Cost Search."""
        path = ucs(self.env, self.start, self.goal)
        if path:
            # cost = sum of terrain costs
            total_cost = sum(self.env.get_cost(x, y) for x, y in path)
            self.set_path(path, cost=total_cost)
            return True
        return False

    def plan_with_astar(self):
        """Plan a path from start to goal using A* Search."""
        path = astar(self.env, self.start, self.goal)
        if path:
            total_cost = sum(self.env.get_cost(x, y) for x, y in path)
            self.set_path(path, cost=total_cost)
            return True
        return False

    def plan_with_local(self):
        """Plan a path from start to goal using Hill Climbing with random restarts."""
        path = hill_climbing(self.env, self.start, self.goal)
        if path:
            # heuristic-based search, so just count steps
            self.set_path(path, cost=len(path))
            return True
        return False










