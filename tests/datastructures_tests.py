import unittest

import datastructures.linkedlist

from datastructures.linkedlist import LinkedList,LinkedListElement
from datastructures.stack import Stack
from datastructures.queue import Queue
from datastructures.binarytree import Node, BinaryTree, BST
from datastructures.graph import Graph

class TestLinkedListMethods(unittest.TestCase):

    def setUp(self):
        # Set up some Elements
        self.e1 = LinkedListElement(1)
        self.e2 = LinkedListElement(2)
        self.e3 = LinkedListElement(3)
        self.e4 = LinkedListElement(4)

        # Start setting up a LinkedList
        self.ll = LinkedList(self.e1)
        return 

    def tearDown(self):
        #Clear For Next Test
        self.e1 = self.e2 = self.e3 = self.e4 = None
        self.ll = None

    #TEST FUNCTION
    def test_append(self):
        #Setup
        self.ll.append(self.e2)
        self.ll.append(self.e3)
        self.assertEqual(self.ll.head.next.value,2)
        self.assertEqual(self.ll.head.next.next.value,3)

    def test_getPosition(self):
        #Setup
        self.ll.append(self.e2)
        self.ll.append(self.e3)
        self.assertEqual(self.ll.get_position(3).value,3)

    def test_insert(self):
        #Setup
        self.ll.append(self.e2)
        self.ll.append(self.e3)
        
        # Test insert
        self.ll.insert(self.e4,3)
        # Should print 4 now
        self.assertEqual(self.ll.get_position(3).value,4)

    def test_delete(self):
        #Setup
        self.ll.append(self.e2)
        self.ll.append(self.e4)
        self.ll.append(self.e3)
        
        # Test delete
        self.ll.delete(1)
        
        self.assertEqual(self.ll.get_position(1).value,2)
        self.assertEqual(self.ll.get_position(2).value,4)
        self.assertEqual(self.ll.get_position(3).value,3)

class TestStackMethods(unittest.TestCase):

    def setUp(self):
        # Set up some Elements
        self.e1 = LinkedListElement(1)
        self.e2 = LinkedListElement(2)
        self.e3 = LinkedListElement(3)
        self.e4 = LinkedListElement(4)

        # Start setting up a LinkedList
        self.stack = Stack(self.e1)
        return 

    def tearDown(self):
        #Clear For Next Test
        self.e1 = self.e2 = self.e3 = self.e4 = None
        self.stack = None
    
    def test_peek(self):
        self.assertEqual(self.stack.peek().value,1)

    def test_push(self):
        # Setup
        # Test stack functionality
        self.stack.push(self.e2)
        self.stack.push(self.e3)
        self.assertEqual(self.stack.peek().value,3)

    def test_pop(self):
       self.stack.push(self.e2)
       self.stack.push(self.e3)
       self.assertEqual(self.stack.pop().value, 3)
       self.assertEqual(self.stack.pop().value, 2)
       self.assertEqual(self.stack.pop().value, 1)
       self.assertEqual(self.stack.pop(), None)

class TestQueueMethods(unittest.TestCase):

    def setUp(self):
        # Setup
        self.q = Queue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        return 

    def tearDown(self):
        #Clear For Next Test
        self.q = None

    def test_peek(self):
        self.assertEqual(self.q.peek(), 1)
        pass

    def test_enqueue(self):
        self.q.enqueue(4)
        self.assertEqual(self.q.peek(),1)
        pass

    def test_deque(self):
        self.assertEqual(self.q.dequeue(),1)
        self.assertEqual(self.q.dequeue(),2)
        self.assertEqual(self.q.dequeue(),3)
        pass

    def test_total(self):
        self.assertEqual(self.q.dequeue(),1)
        self.q.enqueue(4)
        self.assertEqual(self.q.dequeue(),2)
        self.assertEqual(self.q.dequeue(),3)
        self.assertEqual(self.q.dequeue(),4)
        self.q.enqueue(5)
        self.assertEqual(self.q.peek(),5)
        pass

class TestBinaryTrees(unittest.TestCase):

    def setUp(self):
        # Set up tree
        self.tree = BinaryTree(1)
        self.tree.root.left = Node(2)
        self.tree.root.right = Node(3)
        self.tree.root.left.left = Node(4)
        self.tree.root.left.right = Node(5)

    def tearDown(self):
        pass

    def test_search(self):
        # Test search
        # Should be True
        self.assertTrue(self.tree.search(4))
        self.assertFalse(self.tree.search(6))
        pass

    def test_print_tree(self):
        self.assertEqual(self.tree.print_tree(),"1-2-4-5-3")
        pass

class TestBinarySearchTrees(unittest.TestCase):

    def setUp(self):
        # Set up tree
        self.tree = BST(4)

    def tearDown(self):
        pass

    def test_insert(self):
        self.tree.insert(2)
        self.assertEqual(self.tree.root.left.value,2)
        self.tree.insert(1)
        self.assertEqual(self.tree.root.left.left.value,1)
        self.tree.insert(3)
        self.assertEqual(self.tree.root.left.right.value,3)
        self.tree.insert(5)
        self.assertEqual(self.tree.root.right.value,5)

    def test_search(self):
        # Test search
        # Should be True
        self.tree.insert(2)
        self.tree.insert(1)
        self.tree.insert(3)
        self.tree.insert(5)
        self.assertTrue(self.tree.search(4))
        self.assertFalse(self.tree.search(6))

    def test_print_tree(self):
        # Insert elements
        self.tree.insert(2)
        self.tree.insert(1)
        self.tree.insert(3)
        self.tree.insert(5)
        self.assertEqual(self.tree.print_tree(),"4-2-1-3-5")
        pass

class TestGraphs(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.insert_edge(100, 1, 2)
        self.graph.insert_edge(101, 1, 3)
        self.graph.insert_edge(102, 1, 4)
        self.graph.insert_edge(103, 3, 4)
    
    def tearDown(self):
        pass

    def test_edge_list(self):
        myList = self.graph.get_edge_list()
        print(myList)
        self.assertEqual(str(myList),
        "[(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]")
        self.graph.nodes.clear()
        self.graph.edges.clear()

    def test_adj_list(self):
        self.assertEqual(str(self.graph.get_adjacency_list()),
        "[None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]")
        self.graph.nodes.clear()
        self.graph.edges.clear()
    
    def test_adj_matrix(self):
        self.assertEqual(str(self.graph.get_adjacency_matrix()),
        "[[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]")
        self.graph.nodes.clear()
        self.graph.edges.clear()

if __name__ == '__main__':
    unittest.main()