__author__ = 'raymond'


class SignFunction:
	@staticmethod
	def evaluate(value):
		if value < 0:
			return -1
		elif value == 0:
			return 0
		else:
			return 1
