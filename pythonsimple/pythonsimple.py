#standard imports
import os
import os.path
import sys

#internal imports
import helpers

from helpers import HelperSample

def main():
	print("Hello World!")
	HelperSample.Helper1()
	HelperSample.Helper2()
	hSample = HelperSample();
	hSample.Helper3()
	
if __name__== "__main__":
  main()