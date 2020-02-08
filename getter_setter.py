class Employee:
	def __init__(self, name, pay, grade, eid):
		self.__name = name
		self.__pay = pay
		self.__grade = grade
		self.__eid = eid 
	@property
	def _name(self):
		print('Getter Method Invoked!!!!')
		return self.__name
	@property
	def _pay(self):
		print('Getter Method Invoked!!!!')
		return self.__pay
	@property
	def _grade(self):
		print('Getter Method Invoked!!!!')
		return self.__grade
	@property
	def _eid(self):
		print('Getter Method Invoked!!!!')
		return self.__eid
	@_name.setter
	def _name(self, n):
		print('Setter Method Invoked!!!')
		self.__name=n	
	@_pay.setter
	def _pay(self, p):
		print('Setter Method Invoked!!!')
		self.__pay = p
	@_grade.setter
	def _grade(self, g):
		print('Setter Method Invoked!!!')
		self.__grade=g
	@_eid.setter
	def _eid(self, id):
		print('Setter Method Invoked!!!')
		self.__eid = id



	
	
class Developer(Employee):
	def __init__(self, name, pay, grade, eid):
		super().__init__(name, pay, grade, eid)



		

class Driver:
	if __name__ == '__main__':
		d = Developer('Debjit', 60000, 'A', 123456)
		print(d._name, d._pay, d._grade)
		d._grade = 'A+'
		d._eid = 112233
		d._name = 'Carl'
		d._pay = 100000
		print(d._name, d._pay, d._grade)