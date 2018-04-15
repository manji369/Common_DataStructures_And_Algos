from collections import defaultdict
from collections import deque

class graph:
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.v = V

    def buildGraph(self, edges):
        for u, v in edges:
            self.graph[u].append(v)

    def dfsUtil(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfsUtil(neighbor, visited)

    def dfs(self, v):
        visited = [False]*self.v
        self.dfsUtil(v, visited)

    def topologicalSortUtil(self, v, visited, q):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topologicalSortUtil(neighbor, visited, q)
        q.appendleft(v)

    def topologicalSort(self):
        visited = [False]*self.v
        q = deque([])
        for v in range(self.v):
            if not visited[v]:
                self.topologicalSortUtil(v, visited, q)
        return q

    def bfs(self, v):
        q = deque([v])
        visited = [False]*self.v
        visited[v] = True
        while q:
            cur = q.popleft()
            print(cur, end=' ')
            for neighbor in self.graph[cur]:
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True


if __name__ == "__main__":
    graph = graph(5)
    graph.buildGraph([[0, 1], [1, 2], [1, 3], [0, 4], [1, 4]])
    print(graph.dfs(0))
    print(graph.bfs(0))
    print(graph.topologicalSort())