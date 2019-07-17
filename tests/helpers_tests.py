import unittest

import pythonsimple.helpers

from pythonsimple.helpers import HelperSample

#from helpers import HelperSample

class TestStringMethods(unittest.TestCase):

    #TEST FUNCTION
    def test_helper1(self):
        self.assertEqual(HelperSample.Helper1(),"Helper Test 1: Class pythonsimple.helpers.HelperSample")
    
    def test_helper2(self):
        self.assertEqual(HelperSample.Helper2(),"Helper Test 2")
    
    def test_helper3(self):
        hSample = HelperSample()
        self.assertEqual(hSample.Helper3(),"Helper Test: Data 5")
        hSample = HelperSample(100)
        self.assertEqual(hSample.Helper3(),"Helper Test: Data 100")

if __name__ == '__main__':
    unittest.main()