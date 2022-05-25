from binaryTree import Tree, TreeNode
from typing import Optional

def treeSearchRecursive(x: Optional[TreeNode], k: int):
    if x is None or x.key == k:
        return x
    if x.key < k:
        return treeSearchRecursive(x.right, k)
    return treeSearchRecursive(x.left, k)

def treeSearchIterative(x: Optional[TreeNode], k: int):
    while x is not None and x.key != k:
        if x.key < k:
            x = x.right
        else:
            x = x.left
    return x

def treeMaximumRecursive(x: TreeNode):
    if x.right is None: return x
    return treeMaximumRecursive(x.right)

def treeMaximumIterative(x: TreeNode):
    while x.right is not None:
        x = x.right
    return x

def treeMinimumRecursive(x: TreeNode):
    if x.left is None: return x
    return treeMinimumRecursive(x.left)

def treeMinimumIterative(x: TreeNode):
    while x.left is not None:
        x = x.left
    return x

def treeSuccessor(x: TreeNode):
    if x.right is not None: return treeMinimumIterative(x.right)
    y = x.p
    while y is not None and y.right == x:
        x = y
        y = y.p
    return y

def treePredecessor(x: TreeNode):
    if x.left is not None: return treeMaximumIterative(x.left)
    y = x.p
    while y is not None and y.left == x:
        x = y
        y = y.p
    return y

def treeInsertIterative(T: Tree, z: TreeNode):
    if T.root is None:
        T.root = z
        return
    y = None
    x = T.root
    while x is not None:
        y = x
        x = x.left if z.key < x.key else x.right
    z.p = y
    if z.key < y.key:
        y.left = z
    else:
        y.right = z

def treeInsertRecursive(x: TreeNode, z: TreeNode):
    if z.key < x.key:
        if x.left is None:
            x.left = z
        else:
            treeInsertRecursive(x.left, z)
    else:
        if x.right is None:
            x.right = z
        else:
            treeInsertRecursive(x.right, z)

def treeDelete(T: Tree, z: TreeNode):
    if z.left is None:
        transplant(T, z, z.right)
    elif z.right is None:
        transplant(T, z, z.left)
    else:
        y = treeSuccessor(z)
        if y.p != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y

def transplant(T: Tree, u: TreeNode, v: TreeNode):
    if T.root == u:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v is not None:
        v.p = u.p
