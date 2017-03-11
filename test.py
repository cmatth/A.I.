import numpy

class Tester():
	def __init__(self, word):
		self.name = word

	def returnName(self):
		return self.name

t1 = Tester("doggy")
print t1.returnName()
