n = int(input("Enter number of nodes: "))

graph = {}

print("\nEnter nodes (ex : A B C):")
nodes = input().split()

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


# Depth-First Search
def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes_explored = 0

    while stack:
        current, path = stack.pop()


        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        # Check if goal is reached
        if current == goal:
            return path, nodes_explored

        # Add unvisited neighbors to the stack
        for neighbor in reversed(graph[current]):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None, nodes_explored


# Input start and goal nodes
start = input("\nEnter the start node: ")
goal = input("Enter the goal node: ")

# Perform DFS
path, nodes_explored = dfs(start, goal)

# Display result
print("\nDFS Result: \n")

if path:
    print("Path:", " -> ".join(path))
else:
    print("Goal not found")

print("Nodes Explored:", nodes_explored)