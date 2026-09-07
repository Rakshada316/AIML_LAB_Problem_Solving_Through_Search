import heapq

number_of_nodes = int(input("Enter number of nodes: "))

print("Enter node names:")
node_names = input().split()

graph = {}

# Initialize graph
for node in node_names:
    graph[node] = []

# Input edges and their costs
number_of_edges = int(input("\nEnter number of edges: "))

print("Enter the edges with cost (example: A B 5):")

for _ in range(number_of_edges):
    first_node, second_node, edge_cost = input().split()
    edge_cost = int(edge_cost)

    graph[first_node].append((second_node, edge_cost))
    graph[second_node].append((first_node, edge_cost))


# Input heuristic values
heuristic = {}

print("\nEnter heuristic value for each node:")

for node in node_names:
    heuristic[node] = int(input(f"h({node}) = "))


def a_star(start_node, goal_node):

    # Priority queue stores:
    # (f_cost, g_cost, current_node, path)
    priority_queue = [
        (heuristic[start_node], 0, start_node, [start_node])
    ]

    # Stores the best known g-cost for each node
    best_g_cost = {
        start_node: 0
    }

    nodes_explored = 0

    while priority_queue:

        # Remove the node with the lowest f-cost
        f_cost, current_g_cost, current_node, current_path = heapq.heappop(
            priority_queue
        )

        nodes_explored += 1

        # Check if goal is reached
        if current_node == goal_node:
            return current_path, current_g_cost, nodes_explored

        # Explore all neighbors of the current node
        for neighbor_node, edge_cost in graph[current_node]:

            # Calculate the new g-cost for the neighbor
            new_g_cost = current_g_cost + edge_cost

            # Check whether this is a better path to the neighbor
            if (
                neighbor_node not in best_g_cost
                or new_g_cost < best_g_cost[neighbor_node]
            ):

                # Store the better g-cost
                best_g_cost[neighbor_node] = new_g_cost

                # Calculate f(n) = g(n) + h(n)
                new_f_cost = (
                    new_g_cost + heuristic[neighbor_node]
                )

                # Add the neighbor to the priority queue
                heapq.heappush(
                    priority_queue,
                    (
                        new_f_cost,
                        new_g_cost,
                        neighbor_node,
                        current_path + [neighbor_node]
                    )
                )

    return None, None, nodes_explored


# Input start and goal nodes
start_node = input("\nEnter start node: ")
goal_node = input("Enter goal node: ")

# Run A*
path, path_cost, nodes_explored = a_star(
    start_node,
    goal_node
)

# Display result
print("\n--- A* Search Result ---")

if path:
    print("Path:", " -> ".join(path))
    print("Path Cost:", path_cost)
else:
    print("Goal not found")

print("Nodes Explored:", nodes_explored)