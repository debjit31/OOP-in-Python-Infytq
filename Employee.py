class Employee:

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first 
		self.last = last 
		self.pay = pay
		self.fullname = self.first + ' ' + self.last
		self.email = first+'.'+last+'@email.com'

	def display(self):
		print("FullName of Developer :- " , self.first , ' ' , self.last)
		print("Email :- " , self.email)
		print("Pay :- " , self.pay)
		print("Programming Language :- " + self.prog_lang)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	def __repr__(self):
	##unambiguous representation of the object
	## used for debugging
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self,pay)

	def __str__(self):
	## readable representation of a object 
	## used for display to end user
		pass


class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

	def __repr__(self):
	##unambiguous representation of the object
	## used for debugging
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self,pay)

	def __str__(self):
	## readable representation of a object 
	## used for display to end user
		pass

class Manager(Employee):

	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees == None:
			self.employees = []
		else:
			self.employees=employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def rem_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname)

	def __repr__(self):
	##unambiguous representation of the object
	## used for debugging
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self,pay)

	def __str__(self):
	## readable representation of a object 
	## used for display to end user
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self,pay)

dev2 = Developer('Test', 'Employee', 60000, 'Python')

dev1 = Developer('Corey', 'Schafer', 50000, 'Java')

mgr1 = Manager('Sue', 'Smith', 90000, [dev1])


print(int.__add__(1,2))
print(str.__add__('a', 'ab'))

# print(mgr1.email)
# mgr1.add_emp(dev2)
# mgr1.rem_emp(dev1)
# mgr1.print_emps()

# print(isinstance(Manager, Employee))
# print(issubclass(Manager, Developer))



# print('a' + 'b')
# print(1 + 2)

## dunder functions :- __init__ 


