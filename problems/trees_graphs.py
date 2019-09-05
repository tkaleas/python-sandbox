class BinaryNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def minimalTree(sortedArr):
    # Base Case
    if len(sortedArr) < 1:
        return None
        
    midpoint = int(len(sortedArr)/2)
    root = BinaryNode(sortedArr[midpoint])
    root.left = minimalTree(sortedArr[:midpoint-1])
    root.right = minimalTree(sortedArr[midpoint+1:])

    return root