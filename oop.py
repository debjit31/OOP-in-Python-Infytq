class Person:

	def __init__(self, name, pay, age):
		self.name = name
		self.pay = pay
		self.age = age

	def display(self):
		return (self.name, self.pay, self.age)

p = Person('Debjit', 50000, 20)
print(p.display())