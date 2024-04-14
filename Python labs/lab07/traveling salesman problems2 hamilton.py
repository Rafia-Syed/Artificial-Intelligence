import itertools

def tsp(graph, start=0):
    n = len(graph)
    vertices = list(range(n))
    min_cost = float('inf')
    min_path = None
    
    for path in itertools.permutations(vertices[1:], n-1):
        path = (start,) + path
        cost = 0
        for i in range(n-1):
            cost += graph[path[i]][path[i+1]]
        cost += graph[path[-1]][start]
        
        if cost < min_cost:
            min_cost = cost
            min_path = path
    
    return min_cost, min_path

# Example graph
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_city = 0  # Starting city
min_cost, min_path = tsp(graph, start=start_city)
print("Minimum weight Hamiltonian Cycle:")
print(" -> ".join([str(city) for city in min_path]) + f" -> {start_city}: {min_cost}")
