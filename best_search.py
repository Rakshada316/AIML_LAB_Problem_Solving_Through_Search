import heapq

# Input graph details
n = int(input("Enter number of nodes: "))

print("Enter node names:")
nodes = input().split()

graph = {}

# Initialize graph
for node in nodes:
    graph[node] = []

# Input edges
m = int(input("\nEnter number of edges: "))

print("Enter edges (example: A B):")

for _ in range(m):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)


# Input heuristic values
heuristic = {}

print("\nEnter heuristic value for each node:")

for node in nodes:
    heuristic[node] = int(input(f"h({node}) = "))


# Greedy Best-First Search
def greedy_best_first_search(start, goal):
    priority_queue = [(heuristic[start], start, [start])]
    visited = set()
    nodes_explored = 0

    while priority_queue:
        # Remove node with lowest heuristic value
        h, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        # Check if goal is reached
        if current == goal:
            return path, nodes_explored

        # Add unvisited neighbors to priority queue
        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor, path + [neighbor])
                )

    return None, nodes_explored


# Input start and goal nodes
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

# Perform Greedy Best-First Search
path, nodes_explored = greedy_best_first_search(start, goal)

# Display result
print("\n--- Greedy Best-First Search Result ---")

if path:
    print("Path:", " -> ".join(path))
else:
    print("Goal not found")

print("Nodes Explored:", nodes_explored)