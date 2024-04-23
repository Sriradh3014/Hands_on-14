class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

def topological_sort(graph):
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        topological_order.insert(0, node)

    topological_order = []
    visited = set()
    for node in range(len(graph)):  # Iterate over indices
        if node not in visited:
            dfs(node)
    return topological_order

# Create the graph
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

# Perform topological sorting
sorted_order = topological_sort(g.adj_list)
print(sorted_order)
#output:-[5, 4, 2, 3, 1, 0]