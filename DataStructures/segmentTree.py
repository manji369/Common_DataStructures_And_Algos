class MinSegmentTree:
    def __init__(self):
        self.tree = []
        self.array = []

    def nextPowerOf2(self, num):
        if num == 0:
            return 1
        if num < 0:
            raise Exception("number less than 0")
        if num&(num-1) == 0:
            return num
        while num&(num-1) > 0:
            num = num&(num-1)
        return num << 1

    def parent(self, idx):
        return (idx-1)//2

    def left(self, idx):
        return 2*idx + 1

    def right(self, idx):
        return 2*idx + 2

    def createSegmentTree(self, arr):
        m, n = len(arr), 2*self.nextPowerOf2(len(arr))-1
        self.array = arr
        self.tree = [float('inf')]*n
        self.constructMinSegmentTree(arr, 0, m - 1, 0)
        return self.tree

    def constructMinSegmentTree(self, arr, low, high, pos):
        if low == high:
            self.tree[pos] = arr[low]
            return
        mid = (low+high)//2
        self.constructMinSegmentTree(arr, low, mid, self.left(pos))
        self.constructMinSegmentTree(arr, mid + 1, high, self.right(pos))
        self.tree[pos] = min(self.tree[self.left(pos)], self.tree[self.right(pos)])

    def querySegmentTree(self, qlow, qhigh):
        return self.rangeMinimumQuery(0, len(self.array)-1, qlow, qhigh, 0)

    def rangeMinimumQuery(self, low, high, qlow, qhigh, pos):
        if qlow <= low and qhigh >= high:
            return self.tree[pos]
        if qlow > high or qhigh < low:
            return float('inf')
        mid = (low+high)//2
        return min(self.rangeMinimumQuery(low, mid, qlow, qhigh, self.left(pos)),
                   self.rangeMinimumQuery(mid+1, high, qlow, qhigh, self.right(pos)))

    def updateSegmentTree(self, idx, val):
        delta = val-self.array[idx]
        self.array[idx] += delta
        self.updateSegmentTreeUtil(idx, delta, 0, len(self.array)-1, 0)

    def updateSegmentTreeUtil(self, idx, delta, low, high, pos):
        if idx < low or idx > high:
            return
        if low == high:
            self.tree[pos] += delta
            return
        mid = (low+high)//2
        self.updateSegmentTreeUtil(idx, delta, low, mid, self.left(pos))
        self.updateSegmentTreeUtil(idx, delta, mid + 1, high, self.right(pos))
        self.tree[pos] = min(self.tree[self.left(pos)], self.tree[self.right(pos)])


class SumSegmentTree:
    def __init__(self):
        self.tree = []
        self.array = []

    def parent(self, idx):
        return (idx-1)//2

    def left(self, idx):
        return 2*idx + 1

    def right(self, idx):
        return 2*idx + 2

    def nextPowerOf2(self, num):
        if num == 0:
            return 1
        if num < 0:
            raise Exception("number less than 0")
        if num&(num-1) == 0:
            return num
        while num&(num-1) > 0:
            num = num&(num-1)
        return num << 1

    def createSegmentTree(self, arr):
        m, n = len(arr), 2 * self.nextPowerOf2(len(arr)) - 1
        self.array = arr
        self.tree = [float('inf')] * n
        self.constructSumSegmentTree(arr, 0, m - 1, 0)
        return self.tree

    def constructSumSegmentTree(self, arr, low, high, pos):
        if low == high:
            self.tree[pos] = arr[low]
            return
        mid = (low+high)//2
        self.constructSumSegmentTree(arr, low, mid, self.left(pos))
        self.constructSumSegmentTree(arr, mid + 1, high, self.right(pos))
        self.tree[pos] = self.tree[self.left(pos)] + self.tree[self.right(pos)]

    def querySegmentTree(self, qlow, qhigh):
        return self.rangeSumQuery(0, len(self.array)-1, qlow, qhigh, 0)

    def rangeSumQuery(self, low, high, qlow, qhigh, pos):
        if qlow <= low and qhigh >= high:
            return self.tree[pos]
        if qlow > high or qhigh < low:
            return 0
        mid = (low+high)//2
        return self.rangeSumQuery(low, mid, qlow, qhigh, self.left(pos)) +\
                   self.rangeSumQuery(mid+1, high, qlow, qhigh, self.right(pos))

    def updateSegmentTree(self, idx, val):
        delta = val-self.array[idx]
        self.array[idx] += delta
        self.updateSegmentTreeUtil(idx, delta, 0, len(self.array)-1, 0)

    def updateSegmentTreeUtil(self, idx, delta, low, high, pos):
        if idx < low or idx > high:
            return
        if low == high:
            self.tree[pos] += delta
            return
        mid = (low+high)//2
        self.updateSegmentTreeUtil(idx, delta, low, mid, self.left(pos))
        self.updateSegmentTreeUtil(idx, delta, mid + 1, high, self.right(pos))
        self.tree[pos] = self.tree[self.left(pos)] + self.tree[self.right(pos)]

mst = MinSegmentTree()
# print(mst.nextPowerOf2(4))
print(mst.createSegmentTree([-1, 2, 4, 0]))
print(mst.array)
print(mst.querySegmentTree(2, 3))
mst.updateSegmentTree(2, -2)
print(mst.array)
print(mst.querySegmentTree(2, 3))
sst = SumSegmentTree()
print(sst.createSegmentTree([-1, 2, 4, 0]))
print(sst.array)
print(sst.querySegmentTree(2, 3))
sst.updateSegmentTree(2, -2)
print(sst.array)
print(sst.querySegmentTree(2, 3))