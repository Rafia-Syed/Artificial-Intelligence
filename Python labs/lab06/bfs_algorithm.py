def bfs(initial_state, is_goal, get_neighbors):
    queue = [(initial_state, [])]  # Queue of states to explore, each state paired with its path
    visited = set()  # Set to keep track of visited states

    while queue:
        state, path = queue.pop(0)  # Get the next state and its path from the queue
        if state in visited:
            continue  # Skip this state if it has already been visited

        visited.add(state)  # Mark the state as visited

        if is_goal(state):
            return path + [state]  # Return the path to the goal state

        neighbors = get_neighbors(state)  # Get neighboring states
        if not neighbors:
            continue  # Skip if there are no valid moves from this state

        # Add neighbors to the queue with their paths
        for neighbor in neighbors:
            queue.append((neighbor, path + [state]))

    return None  # If no goal state is found


def is_goal(state):
    return state == (0, 0, 0, 3, 3)  # All missionaries and cannibals are on the other side


def get_neighbors(state):
    moves = []
    m1, c1, b, m2, c2 = state

    if b == 1:  # Boat on initial side
        for i in range(3):
            for j in range(3):
                if (m1 - i >= c1 - j >= 0 or m1 - i == 0) and (m2 + i >= c2 + j >= 0 or m2 + i == 0):
                    moves.append((m1 - i, c1 - j, 0, m2 + i, c2 + j))
    else:  # Boat on other side
        for i in range(3):
            for j in range(3):
                if (m1 + i >= c1 + j >= 0 or m1 + i == 0) and (m2 - i >= c2 - j >= 0 or m2 - i == 0):
                    moves.append((m1 + i, c1 + j, 1, m2 - i, c2 - j))
    return moves


# Define the initial state
initial_state = (3, 3, 1, 0, 0)

# Call the bfs function
path_to_goal = bfs(initial_state, is_goal, get_neighbors)

# Print the path to the goal state
print("Path to the goal state:")
for state in path_to_goal:
    print(state)
