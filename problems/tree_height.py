class TreeNode(object):
    def __init__(self):
        self.data = None
        self.children = []

class Tree(object):
    def __init__(self):
        self.root = TreeNode()

    def _getHeightFromNode(self, node):
        
        # base case is a leaf
        if len(node.children) < 1:
            return 0

        h = 0
        for child in node.children:
            h = max(h, self._getHeightFromNode(child))

        #this level + child height
        return 1 + h

    def getHeight(self):
        return self._getHeightFromNode(self.root)