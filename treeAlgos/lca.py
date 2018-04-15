from treeAlgos.node import Node

def lcaBst(root, n1, n2):
    if root is None:
        if n1 is None and n2 is None:
            return None
        else:
            raise Exception("Root is None")
    if n1 is None or n2 is None:
        raise Exception("given node None")
    while root:
        if root.val < n1.val and  root.val < n2.val:
            root = root.right
        elif root.val > n1.val and root.val > n2.val:
            root = root.left
        else:
            return root.val
    return None

def lca(root, n1, n2):
    if root is None:
        return root
    if root == n1 or root == n2:
        return root
    left = lca(root.left, n1, n2)
    if left is not None and left != n1 and left != n2:
        return left
    right = lca(root.right, n1, n2)
    if left is not None and right is not None:
        return root
    if left is None and right is None:
        return None
    return left if left is not None else right

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

print("LCA of 28, 78:")
print(lcaBst(node, node.right.left.right, node.right.right.right))
print("LCA of 6, 9:")
print(lcaBst(node, node.left.right.left, node.left.right.right))
print("LCA of 30, 78:")
print(lcaBst(node, node.right, node.right.right.right))
print("LCA of 28, 78:")
res = lca(node, node.right.left.right, node.right.right.right)
print(res.val if res else None)
print("LCA of 6, 9:")
res = lca(node, node.left.right.left, node.left.right.right)
print(res.val if res else None)
print("LCA of 30, 78:")
res = lca(node, node.right, node.right.right.right)
print(res.val if res else None)