from treeAlgos.node import Node
from collections import deque

def posOrderRec(root, res):
    if root is None:
        return res
    posOrderRec(root.left, res)
    posOrderRec(root.right, res)
    res.append(root.val)
    return res

def postOrderIter(root, res):
    if root is None:
        return res
    stack = [root]
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return res[::-1]

def postOrderIterOnePass(root, res):
    if root is None:
        return res
    cur = root
    stack = []
    while cur is not None or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            temp = stack[-1].right
            if temp is None:
                temp = stack.pop()
                res.append(temp.val)
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    res.append(temp.val)
            else:
                cur = temp
    return res


def preOrderRec(root, res):
    if root is None:
        return res
    res.append(root.val)
    preOrderRec(root.left, res)
    preOrderRec(root.right, res)
    return res

def preOrderIter(root, res):
    if root is None:
        return res
    stack = [root]
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res

def inOrderRec(root, res):
    if root is None:
        return res
    inOrderRec(root.left, res)
    res.append(root.val)
    inOrderRec(root.right, res)
    return res

def inOrderIter(root, res):
    if root is None:
        return res
    stack = []
    cur = root
    while True:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        if not stack:
            break
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res

def levelOrder(root, res):
    if root is None:
        return res
    q = deque([root, None])
    curRes = []
    while True:
        cur = q.popleft()
        if cur:
            curRes.append(cur.val)
        else:
            res.append(curRes)
            if not q:
                break
            curRes = []
            q.append(cur)
            continue
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    return res

def spiralOrder(root, res):
    if root is None:
        return res
    q = deque([root, None])
    curRes = []
    while len(q) > 1:
        cur = q[0]
        while cur is not None:
            cur = q.popleft()
            curRes.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            cur = q[0]
        res.append(curRes)
        curRes = []
        cur = q[-1]
        while cur is not None:
            cur = q.pop()
            curRes.append(cur.val)
            if cur.right:
                q.appendleft(cur.right)
            if cur.left:
                q.appendleft(cur.left)
            cur = q[-1]
        res.append(curRes)
        curRes = []
    return res

node = Node(1)
node.left = Node(-1)
node.right = Node(11)
node.left.left = Node(-2)
node.left.right = Node(-3)
node.left.right.right = Node(5)
node.right.left = Node(21)
node.right.right = Node(6)
print("Post order recursive")
print(posOrderRec(node, []))
print("Post order iterative")
print(postOrderIter(node, []))
print("Post order iterative one pass")
print(postOrderIterOnePass(node, []))
print("Pre order recursive")
print(preOrderRec(node, []))
print("Pre order iterative")
print(preOrderIter(node, []))
print("In order recursive")
print(inOrderRec(node, []))
print("In order iterative")
print(inOrderIter(node, []))
print("Level order iterative")
print(levelOrder(node, []))
print("Spiral order iterative")
print(spiralOrder(node, []))