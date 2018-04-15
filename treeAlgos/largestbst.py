from treeAlgos.node import Node

class Minimaxi:
    def __init__(self):
        self.isBst = True
        self.size = 0
        self.mini = float('inf')
        self.maxi = float('-inf')


def largestBST(root):
    if root is None:
        return Minimaxi()
    l = largestBST(root.left)
    r = largestBST(root.right)
    res = Minimaxi()
    if l.isBst == False or r.isBst == False or l.maxi > root.val or r.mini <= root.val:
        res.isBst = False
        res.size = max(l.size, r.size)
        return res
    res.isBst = True
    res.size = 1+l.size+r.size
    res.mini = l.mini if root.left is not None else root.val
    res.maxi = r.maxi if root.right is not None else root.val
    return res

node = Node(10)
node.left = Node(-10)
node.right = Node(30)
node.left.right = Node(8)
node.right.left = Node(25)
node.right.right = Node(60)
node.left.right.left = Node(6)
node.left.right.right = Node(9)
node.right.left.right = Node(28)
node.right.right.right = Node(78)
print(largestBST(node).size)