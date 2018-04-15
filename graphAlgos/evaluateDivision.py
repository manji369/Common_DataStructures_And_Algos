from collections import defaultdict
import heapq

class Solution:
    def calcEquation(self, equations, values, queries):
        g = defaultdict(list)
        for (a, b), v in zip(equations, values):
            g[a].append((b, v))
            g[b].append((a, 1/v))

        res = []
        for query in queries:
            a, b = query
            if a not in g or b not in g:
                res.append(-1.0)
                continue
            q, seen = [(a, 1)], set()
            while q:
                v1, cost = heapq.heappop(q)
                if v1 not in seen:
                    seen.add(v1)
                    if v1 == b:
                        res.append(cost)
                        break
                    for v2, c in g.get(v1, ()):
                        if v2 not in seen:
                            heapq.heappush(q, (v2, cost*c))
            else:
                res.append(-1.0)
        return res

sol = Solution()
print(sol.calcEquation([ ["a","b"],["b","c"] ], [2.0,3.0], [ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]))