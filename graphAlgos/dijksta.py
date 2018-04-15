from collections import defaultdict
import heapq

class graph:
    def __init__(self, edges):
        self.graph = defaultdict(list)
        self.vertices = set()
        for l, r, c in edges:
            self.graph[l].append((c, r))
            self.vertices.add(l)
            self.vertices.add(r)

    def dijkstraBetweenTwo(self, f, t):
        q, seen = [(0, f, ())], set()
        while q:
            cost, v1, path = heapq.heappop(q)
            if v1 not in seen:
                seen.add(v1)
                path = (v1, path)
                if v1 == t:
                    return (cost, path)
                for c, v2 in self.graph.get(v1, ()):
                    if v2 not in seen:
                        heapq.heappush(q, (cost+c, v2, path))
        return float('inf')

    def dijksta(self, src):
        q, dist, parent = [], {src: 0}, {src: None}
        for vertex in self.vertices:
            if vertex != src:
                dist[vertex] = float('inf')
                parent[vertex] = None
            heapq.heappush(q, (dist[vertex], vertex))
        while q:
            d, u = heapq.heappop(q)
            for duv, v in self.graph[u]:
                alt = d + duv
                if alt < dist[v]:
                    dist[v] = alt
                    parent[v] = u
                    for i in range(len(q)):
                        if q[i][1] == v:
                            q[i] = (alt, v)
                            break
                    heapq.heapify(q)
        return dist, parent

if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]
    graph = graph(edges)

    print("=== Dijkstra ===")
    print(edges)
    print("A -> E:")
    print(graph.dijkstraBetweenTwo("A", "E"))
    print("F -> G:")
    print(graph.dijkstraBetweenTwo("F", "G"))
    print(graph.dijksta("A"))