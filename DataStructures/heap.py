class MinHeap:
    def __init__(self):
        self.heapSize = 0

    def left(self, idx):
        return (idx << 1) + 1

    def right(self, idx):
        return (idx << 1) + 2

    def parent(self, idx):
        return (idx-1) >> 1

    def buildheap(self, arr):
        self.heapSize = len(arr)
        for i in range(self.heapSize//2-1, -1, -1):
            self.heapify(arr, i)

    def heapify(self, arr, idx):
        smallest = idx
        l, r = self.left(idx), self.right(idx)
        if l < self.heapSize and arr[l] < arr[smallest]: smallest = l
        if r < self.heapSize and arr[r] < arr[smallest]: smallest = r
        if smallest != idx:
            arr[idx], arr[smallest] = arr[smallest], arr[idx]
            self.heapify(arr, smallest)

    def extractMin(self, arr):
        if self.heapSize < 1:
            raise Exception("Heap underflow")
        res = arr[0]
        arr[self.heapSize-1], arr[0] = arr[0], arr[self.heapSize-1]
        self.heapSize -= 1
        self.heapify(arr, 0)
        return res

    def decreaseVal(self, arr, i, val):
        if val > arr[i]:
            raise Exception("New val is larger than current val")
        arr[i] = val
        while i > 1 and arr[self.parent(i)] > arr[i]:
            arr[i], arr[self.parent(i)] = arr[self.parent(i)], arr[i]
            i = self.parent(i)

    def insert(self, arr, val):
        self.heapSize += 1
        arr.append(float('inf'))
        self.decreaseVal(arr, self.heapSize-1, val)


h = MinHeap()
arr = [10, 7, 1, 9, 2, 8]
h.buildheap(arr)
print(arr)
# h.extractMin(arr)
# print(arr)
# h.extractMin(arr)
# print(arr)
h.decreaseVal(arr, len(arr)-1, 3)
print(arr)
h.insert(arr, 1)
print(arr)