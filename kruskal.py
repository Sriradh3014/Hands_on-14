class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def kruskal(self):
        self.edges.sort(key=lambda x: x[2])
        uf = UnionFind(self.num_vertices)
        mst = []

        for edge in self.edges:
            u, v, weight = edge
            if uf.find(u) != uf.find(v):
                mst.append((u, v, weight))
                uf.union(u, v)

        return mst


# Example usage:
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

minimum_spanning_tree = g.kruskal()
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)

#Output:-
#Minimum Spanning Tree:
#(2, 3, 4)
#(0, 3, 5)
#(0, 1, 10)