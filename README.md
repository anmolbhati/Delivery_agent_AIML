

````markdown
# 🚚 Autonomous Delivery Agent

Ever wondered how a delivery drone finds its way through a busy city?  
This project brings that concept to life! It's a simulation of a smart delivery agent that navigates a grid-based city, dodging obstacles and tricky terrain to find the best possible path to deliver its packages.

I built this to explore the core ideas of artificial intelligence — how algorithms can make rational decisions, plan efficiently, and adapt on the fly, just like a real autonomous vehicle would.

## What Can It Do?

- **Navigate Complex Cities:** The agent finds its way through maps filled with roads, costly terrains, and static buildings.
- **⏱ Choose the Best Strategy:** It doesn't just find *a* path; it finds the *best* path using different AI techniques:
  - **BFS (Breadth-First Search):** Finds the shortest route by number of steps. Great for simple maps.
  - **UCS (Uniform-Cost Search):** Finds the cheapest route, avoiding expensive terrain. The reliable, cost-conscious option.
  - **A\* Search:** The smart navigator! Uses a built-in "sense of direction" to find the optimal path much faster.
  - **Local Replanning:** The agile problem-solver. If a car suddenly blocks the road, it quickly finds a new detour without starting from scratch.
- **Provide Clear Results:** For every run, it tells you the total cost of the trip, the path followed, and how long it took.

## Getting Started

### 1. Grab the Code

First, clone the project to your computer:

```bash
git clone https://github.com/YOUR_USERNAME/autonomous-delivery-agent.git
cd autonomous-delivery-agent
````

### 2. Run a Delivery!

Use the command line to tell the agent which map to use and how to think. It's super easy.

**Example commands:**

```bash
# Have the smart A* algorithm deliver a package on a small map
python main.py --algo astar --map maps/map_small.txt --start 0 0 --goal 4 4

# Test the agent's ability to react to a moving obstacle on the dynamic map
python main.py --algo local --map maps/map_dynamic.txt --start 0 0 --goal 5 5
```

If you want a popup window with animation (instead of terminal view):

```bash
python main_gui.py --algo astar --map maps/map_small.txt --start 0 0 --goal 4 4
```

## Understanding the Map Files

The city layouts are simple text files. Here’s a quick guide:

* Each map is a grid of integers.
* **Cell meanings:**

  * `1` = Road (cost 1)
  * `2, 3...` = Higher terrain cost (mud, water, etc.)
  * `-1` = Building/obstacle (blocked)
* Example (`map_small.txt`):

```
1 1 1 1 1
1 -1 -1 1 1
1 1 1 1 1
1 -1 1 -1 1
1 1 1 1 1
```

## Learn More & See the Results

Curious about which algorithm performed best? Want to see the analysis and performance graphs?

Check out the full **`report.pdf`** included in this project!
It explains the environment model, algorithms, results, and when each approach works best.

---

## Contributors

* **Anmol Bhati**

```



