from graphAlgos.disjointSetUnion import DSU

class graph:
    def kruskal(self, edges):
        edges.sort(key=lambda tup: tup[2])
        dsu = DSU()
        for u, v, w in edges:
            dsu.makeSet(u)
            dsu.makeSet(v)
        res = []
        cnt = 0
        for u, v, w in edges:
            if dsu.find(u) != dsu.find(v):
                dsu.union(u, v)
                res.append((u, v, w))
                cnt += w
        return res, cnt

g = graph()
print(g.kruskal([('A', 'B', 3), ('A', 'D', 1), ('B', 'D', 3), ('B', 'C', 1), ('C', 'D', 1), ('D', 'E', 6), ('C', 'E', 5), ('C', 'F', 4), ('E', 'F', 2)]))