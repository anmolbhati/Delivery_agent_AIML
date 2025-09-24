

import numpy as np

class Environment:
    def __init__(self, grid_file: str):
        
        self.grid = self._load_grid(grid_file)
        self.rows, self.cols = self.grid.shape
        self.dynamic_obstacles = []  # list of DynamicObstacle objects

    def _load_grid(self, grid_file: str) -> np.ndarray:
        
        with open(grid_file, "r") as f:
            lines = [line.strip().split() for line in f.readlines()]
        grid = np.array([[int(x) for x in row] for row in lines])
        return grid

    def is_valid(self, x: int, y: int) -> bool:
        
        if 0 <= x < self.rows and 0 <= y < self.cols:
            return self.grid[x, y] != -1
        return False

    def get_cost(self, x: int, y: int) -> int:
        
        return self.grid[x, y]

    def add_dynamic_obstacle(self, obstacle):
        """
        Add a dynamic obstacle to the environment.
        """
        self.dynamic_obstacles.append(obstacle)

    def update_dynamic_obstacles(self, timestep: int):
        """
        Update positions of all dynamic obstacles.
        """
        for obs in self.dynamic_obstacles:
            obs.update_position(timestep)


class DynamicObstacle:
    
    def __init__(self, path, deterministic=True):
        
        self.path = path
        self.deterministic = deterministic
        self.position = path[0] if isinstance(path, list) else path(0)

    def update_position(self, timestep: int):
        
        if self.deterministic and isinstance(self.path, list):
            idx = timestep % len(self.path)
            self.position = self.path[idx]
        elif callable(self.path):  # unpredictable function
            self.position = self.path(timestep)

    def get_position(self):
        return self.position
