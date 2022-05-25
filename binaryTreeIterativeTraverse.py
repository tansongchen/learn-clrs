from binaryTree import Tree, TreeNode
from typing import List, Optional

def iterativePreorderTraverse(root: Optional[TreeNode]):
    stack: List[TreeNode] = [root]
    while stack:
        node = stack.pop()
        print(node.key)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)

def iterativeInorderTraverse(root: Optional[TreeNode]):
    stack: List[TreeNode] = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.key)
        root = root.right

def iterativePostorderTraverse(root: Optional[TreeNode]):
    stack: List[TreeNode] = []
    while stack or root:
        while root:
            stack.append(root)
            stack.append(root)
            root = root.left
        root = stack.pop()
        if len(stack) > 0 and stack[-1] == root:
            root = root.right
        else:
            print(root.key)
            root = None

if __name__ == '__main__':

    # Let us create trees shown
    # in above diagram
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    iterativePostorderTraverse(root)
