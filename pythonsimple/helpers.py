class HelperSample:
	
	@classmethod
	def Helper1(cls):
		print("Helper Test 1: Class %s" % cls)
		
	@staticmethod
	def Helper2():
		print("Helper Test 2")
		
	def Helper3(self):
		print("Helper Test 3")