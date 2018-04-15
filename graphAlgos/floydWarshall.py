from collections import defaultdict

class graph:
    def __init__(self, V):
        self.graph = defaultdict(dict)
        self.v = V
        self.edges = []

    def buildGraph(self, edges):
        self.edges = edges
        for u, v, w in edges:
            self.graph[u][v] = w

    def floydWarshall(self):
        dist = [[float('inf')]*self.v for i in range(self.v)]
        path = [[None]*self.v for i in range(self.v)]
        for u, v, w in self.edges:
            dist[u][v] = w
            path[u][v] = u
            dist[u][u] = 0
            dist[v][v] = 0
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        path[i][j] = path[k][j]
        for i in range(self.v):
            if dist[i][i] < 0:
                return "Has Negative cycle(s)"
        return dist, path

graph1 = graph(4)
graph1.buildGraph([(0, 1, 3), (0, 2, 6), (0, 3, 15), (1, 2, -2), (2, 3, 2), (3, 0, 1)])
dist, path = graph1.floydWarshall()
print("Dist")
for d in dist:
    print(d)
print("\nPath")
for p in path:
    print(p)
graph1.buildGraph([(0, 1, 3), (2, 0, -2), (0, 3, 15), (1, 2, -2), (2, 3, 2), (3, 0, 1)])
print(graph1.floydWarshall())