from collections import defaultdict

class DSUNaive:
    def __init__(self):
        self.parents = {}

    def find(self, x):
        # No Path Compression
        while self.parents[x] != x:
            x = self.parents[x]
        return x

    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)

    def makeSet(self, x):
        self.parents[x] = x

class DSU:
    def __init__(self):
        self.parents = {}
        self.ranks = defaultdict(int)

    def find(self, x):
        # Path Compression
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        # Union by rank
        if x not in self.parents:
            self.makeSet(x)
        if y not in self.parents:
            self.makeSet(y)
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return False
        elif self.ranks[xp] < self.ranks[yp]:
            self.parents[xp] = yp
        elif self.ranks[xp] > self.ranks[yp]:
            self.parents[yp] = xp
        else:
            self.parents[xp] = yp
            self.ranks[yp] += 1
        return True

    def makeSet(self, x):
        self.parents[x] = x

if __name__ == "__main__":
    pass