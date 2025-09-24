import argparse, time
import matplotlib.pyplot as plt
import numpy as np
from Src.environment import Environment
from Src.agent import Agent

def animate_agent(env: Environment, agent: Agent, goal):
    # Create figure
    fig, ax = plt.subplots()
    grid = env.grid.copy()

    # Draw static obstacles as -1 → black
    cmap = plt.cm.get_cmap("gray_r", 5)  # grayscale colormap
    img = ax.imshow(grid, cmap=cmap, vmin=-1, vmax=3)

    def draw():
        temp_grid = grid.copy()
        gx, gy = goal
        ax.clear()
        temp_grid[gx, gy] = 3  # mark goal
        ax.imshow(temp_grid, cmap=cmap, vmin=-1, vmax=3)
        ax.scatter(agent.current_position[1], agent.current_position[0],
                   c="red", marker="o", s=200, label="Agent")
        ax.scatter(goal[1], goal[0], c="green", marker="*", s=200, label="Goal")
        ax.legend(loc="upper right")
        plt.pause(0.4)

    # Animate steps
    while not agent.reached_goal():
        agent.move_step()
        draw()

    plt.show()

def run_agent(algo: str, map_file: str, start, goal, animate=True):
    env = Environment(map_file)
    agent = Agent(env, start, goal)

    # Choose algorithm
    if algo == "bfs":
        planned = agent.plan_with_bfs()
    elif algo == "ucs":
        planned = agent.plan_with_ucs()
    elif algo == "astar":
        planned = agent.plan_with_astar()
    elif algo == "local":
        planned = agent.plan_with_local()
    else:
        print("Unknown algorithm:", algo)
        return

    if not planned:
        print("❌ No path found.")
        return

    print(f"✅ Path found with {algo.upper()} | Cost: {agent.cost}")

    if animate:
        animate_agent(env, agent, goal)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Autonomous Delivery Agent with GUI")
    parser.add_argument("--algo", type=str, required=True,
                        choices=["bfs", "ucs", "astar", "local"])
    parser.add_argument("--map", type=str, required=True)
    parser.add_argument("--start", type=int, nargs=2, default=[0,0])
    parser.add_argument("--goal", type=int, nargs=2, default=[4,4])
    args = parser.parse_args()

    run_agent(args.algo, args.map, tuple(args.start), tuple(args.goal))

