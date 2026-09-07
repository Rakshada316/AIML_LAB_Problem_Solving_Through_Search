def objective_function(x):
    return -x**2 + 12*x + 5


def hill_climbing(start, minimum, maximum):
    current = start
    states_explored = 1

    while True:
        best = current
        current_value = objective_function(current)

        neighbors = []

        if current > minimum:
            neighbors.append(current - 1)

        if current < maximum:
            neighbors.append(current + 1)

        for neighbor in neighbors:
            states_explored += 1
            neighbor_value = objective_function(neighbor)

            if neighbor_value > current_value:
                best = neighbor
                current_value = neighbor_value

        if best == current:
            break

        current = best

    return current, objective_function(current), states_explored


start = int(input("Enter starting point: "))
minimum = int(input("Enter minimum limit: "))
maximum = int(input("Enter maximum limit: "))

best_state, best_value, states_explored = hill_climbing(
    start, minimum, maximum
)

print("\n=== Hill Climbing Result ===")
print("Best Position:", best_state)
print("Highest Value:", best_value)
print("States Checked:", states_explored)