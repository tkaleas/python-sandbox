class HelperSample:
	
	def __init__(self, input = 5):
		self.data = input

	@classmethod
	def Helper1(cls):
		return ("Helper Test 1: Class %s" % cls)

	@staticmethod
	def Helper2():
		return "Helper Test 2"
	
	def Helper3(self):
		return ("Helper Test: Data %d" % self.data)