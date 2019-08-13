class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = BinaryTreeNode(None)

    def _preorderHelper(self,node):
        print(node.data)
        if node.left is not None:
            self._preorderHelper(node.right)
        if node.right is not None:
            self._preorderHelper(node.left)

    def preorderTraversal(self):
        self._preorderHelper(self.root)