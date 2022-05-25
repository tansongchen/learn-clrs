from binaryTree import Tree, TreeNode

def preorderTraverse(root: TreeNode):
    if root is not None:
        print(root.key)
        preorderTraverse(root.left)
        preorderTraverse(root.right)

def inorderTraverse(root: TreeNode):
    if root is not None:
        preorderTraverse(root.left)
        print(root.key)
        preorderTraverse(root.right)

def postorderTraverse(root: TreeNode):
    if root is not None:
        preorderTraverse(root.left)
        preorderTraverse(root.right)
        print(root.key)
