class MyError(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return self.value

try:
	raise (MyError(3*2))

except MyError as err:
	print('Exception Occured :- ', err.value)
