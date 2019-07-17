import unittest

import datastructures.linkedlist

from datastructures.linkedlist import LinkedList,LinkedListElement
from datastructures.stack import Stack

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

if __name__ == '__main__':
    unittest.main()