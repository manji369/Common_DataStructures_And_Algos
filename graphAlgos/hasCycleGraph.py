from collections import defaultdict
from graphAlgos.disjointSetUnion import DSU

class hasCycleUnDir:
    def hasCycle(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge

class hasCycleDir:
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.v = V
        self.edges = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def buildGraph(self, edges):
        self.edges = edges
        for edge in edges:
            self.addEdge(*edge)

    def hasCycleUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.hasCycleUtil(neighbor, visited, recStack):
                    return True
            elif recStack[neighbor]:
                return True
        recStack[v] = False
        return False

    def hasCycle(self):
        visited = [False]*self.v
        recStack = [False]*self.v
        for node in range(self.v):
            if not visited[node]:
                if self.hasCycleUtil(node, visited, recStack):
                    return True
        return False

if  __name__ == "__main__":
    hasCycleUnDirObj = hasCycleUnDir()
    print(hasCycleUnDirObj.hasCycle([[1, 2], [1, 3], [2, 3]]))
    hasCycleDirObj = hasCycleDir(5)
    hasCycleDirObj.buildGraph([[1,2], [2,3], [3, 1]])
    print(hasCycleDirObj.hasCycle())