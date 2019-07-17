class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Binary Tree
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)
        
    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root,"")[:-1]
        
    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start:
            hasVal = False
            if start.value == find_val:
                hasVal = True
            return hasVal or self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False
        
    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

# Binary Search Tree
class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)
    
    def search_helper(self, start, find_val):
        if start.value == find_val:
            return True
        elif find_val < start.value:
            if start.left:
                return self.search_helper(start.left, find_val)
        elif find_val > start.value:
            if start.right:
                return self.search_helper(start.right, find_val)
        return False
    
    def insert_helper(self, start, new_val):
        if start.value == new_val:
            return
        if new_val > start.value:
            if start.right:
                self.insert_helper(start.right, new_val)
            else:
                start.right = Node(new_val)
        if new_val < start.value:
            if start.left:
                self.insert_helper(start.left, new_val)
            else:
                start.left = Node(new_val)
        return
                
    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root,"")[:-1]

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
        