#standard imports
import os
import os.path
import sys

#internal imports
import helpers

#helpers is a template for internally imported modules
from helpers import HelperSample

def main():
	#Very Basic Program Testing HelperSample
	print("Hello World!")
	HelperSample.Helper1()
	HelperSample.Helper2()
	hSample = HelperSample()
	hSample.Helper3()
	
if __name__== "__main__":
  main()