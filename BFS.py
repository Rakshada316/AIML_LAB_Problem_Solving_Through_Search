from collections import deque


n = int(input("Enter number of nodes: "))

graph = {}

print("\nEnter nodes :")
nodes = input().split()


for node in nodes:
    graph[node] = []

# Input edges
m = int(input("\nEnter number of edges: "))
print("Enter edges (example: A B):")

for _ in range(m):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)


# Breadth-First Search
def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    nodes_explored = 0

    while queue:
        current, path = queue.popleft()
        nodes_explored += 1

        # Check if goal is reached
        if current == goal:
            return path, nodes_explored

        # Explore unvisited neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, nodes_explored



start = input("\nEnter start node: ")
goal = input("Enter goal node: ")


path, nodes_explored = bfs(start, goal)


print("\nBFS Result : \n")

if path:
    print("Path:", " -> ".join(path))
else:
    print("Goal not found")

print("Nodes Explored:", nodes_explored)