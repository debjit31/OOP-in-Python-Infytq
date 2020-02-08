## Using property decorator for private attributes 
class Geeks:
	def __init__(self):
		self.__age = 0
	
	@property
	#getter
	def age(self): 
		print("getter method called") 
		return self.__age 

	@age.setter
	#setter
	def age(self, a):
		print('Setter Invoked!!')
		self.__age = a

	@age.deleter
	#deleter
	def age(self):
		print('Deleter Invoked')
		self.__age = 0
	

mark = Geeks()

mark.age = 19
print(mark.age)
del mark.age
print(mark.age)


