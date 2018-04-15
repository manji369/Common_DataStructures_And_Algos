from collections import defaultdict

class graph:
    def __init__(self, edges):
        self.edges = edges
        self.vertices = set()
        for u, v, w in edges:
            self.vertices.add(u)
            self.vertices.add(v)

    def bellmanFord(self, src):
        dist, parents = {}, {}
        for v in self.vertices:
            dist[v] = float('inf')
            parents[v] = None
        dist[src] = 0
        for i in range(len(self.vertices)-1):
            for u, v, w in self.edges:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    parents[v] = u
        for u, v, w in self.edges:
            if dist[v] > dist[u] + w:
                return "Has Negative cycle(s)"
        return dist, parents

graph1 = graph([(3, 4, 2), (4, 3, 1), (2, 4, 4), (0, 2, 5), (1, 2, -3), (0, 3, 8), (0, 1, 4)])
print(graph1.bellmanFord(0))
graph2 = graph([(0, 1, 1), (1, 2, 3), (2, 3, 2), (3, 1, -6)])
print(graph2.bellmanFord(0))