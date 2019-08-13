## TESTING VIA BASH
import sys
sys.path.append("/mnt/c/dev/projects/python/python-sandbox")

from problems.preorder_binarytree import BinaryTreeNode, Tree

A = BinaryTreeNode("A")
B = BinaryTreeNode("B")
C = BinaryTreeNode("C")
D = BinaryTreeNode("D")
E = BinaryTreeNode("E")
F = BinaryTreeNode("F")
G = BinaryTreeNode("G")
H = BinaryTreeNode("G")

A.left = B
A.right = C
C.right = E
C.left = D
D.right = G
D.left = F
E.left = H

t = Tree()
t.root = A

t.preorderTraversal()