import unittest

import algorithms.binarysearch
import algorithms.sorting

from algorithms.binarysearch import binary_search, get_fib
from algorithms.sorting import bubble_sort, merge_sort, quicksort

class TestBasicAlgorithms(unittest.TestCase):

    def setUp(self):
        pass 

    def tearDown(self):
        pass

    #TEST FUNCTION
    def test_binarysearch(self):
        #Setup
        test_list = [1,3,9,11,15,19,29]
        test_val1 = 25
        test_val2 = 15
        self.assertEqual(binary_search(test_list, test_val1),-1)
        self.assertEqual(binary_search(test_list, test_val2),4)
        return

    def test_get_fib(self):
        self.assertEqual(get_fib(9),34)
        self.assertEqual(get_fib(11),89)
        self.assertEqual(get_fib(0),0)
        return

class TestSortingMethods(unittest.TestCase):
    
    #TEST FUNCTION
    def test_bubblesort(self):
        return
    
    def test_quicksort(self):
        test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
        sortedList = [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]
        self.assertListEqual(quicksort(test), sortedList)

    def test_mergesort(self):
        return

if __name__ == '__main__':
    unittest.main()