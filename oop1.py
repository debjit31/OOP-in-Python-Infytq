class Employee:

	def __init__(self, first, last, pay):
		self.first = first 
		self.last = last 
		self.pay = pay

	@property
	def fullname(self):
		return '{} {}'.format(self.first , self.last)

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first,self.last)

	## setter
	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print('Delete Name!!')
		self.first = None
		self.last = None
	


emp1 = Employee('Corey', 'Scahfer', 60000)

emp1.first = 'John'

emp1.fullname = 'Corey Scahfer'

print(emp1.email)
print(emp1.fullname)
print(emp1.first)

## deleter
del emp1.fullname


# print(emp1 + emp2)