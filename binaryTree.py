from typing import Optional

class TreeNode:
    def __init__(self, key=0, p=None, left=None, right=None):
        self.key = key
        self.p: Optional[TreeNode] = p
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

class Tree:
    def __init__(self, root=None):
        self.root: Optional[TreeNode] = root
