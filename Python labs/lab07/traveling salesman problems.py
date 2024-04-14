from itertools import permutations

def tsp(graph):
    num_cities = len(graph)
    # Initialize DP table
    dp = [[float('inf')] * num_cities for _ in range(1 << num_cities)]
    dp[1][0] = 0  # Base case: Starting from city 0

    # Iterate over all possible subsets of cities
    for mask in range(1, 1 << num_cities):
        for u in range(num_cities):
            # If city u is in the subset and it's not the starting city
            if mask & (1 << u) and u != 0:
                for v in range(num_cities):
                    # If city v is in the subset, not equal to u, and there's a path between u and v
                    if mask & (1 << v) and u != v and graph[u][v] != float('inf'):
                        dp[mask][u] = min(dp[mask][u], dp[mask ^ (1 << u)][v] + graph[v][u])

    # Find the minimum cost to return back to the starting city
    return min(dp[-1][v] + graph[v][0] for v in range(1, num_cities))

# Example usage:
# Define the graph representing distances between cities
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print("Minimum cost of traveling:", tsp(graph))
