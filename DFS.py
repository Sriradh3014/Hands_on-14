class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

    def dfs(self, start):
        def dfs_util(node, visited):
            visited.add(node)
            print(node, end=' ')
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    dfs_util(neighbor, visited)

        visited = set()
        dfs_util(start, visited)

# Create the graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Perform depth-first traversal
print("Depth First Traversal:")
g.dfs(2)

#output:-
#Depth First Traversal:
#2 0 1 3 