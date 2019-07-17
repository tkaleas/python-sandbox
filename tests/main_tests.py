import unittest

import pythonsimple

from pythonsimple import pythonsimple

class TestStringMethods(unittest.TestCase):

	#SAMPLE TESTS (from python doc for unittest)
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
            
    def test_main(self):
        pythonsimple.main()

if __name__ == '__main__':
    unittest.main()