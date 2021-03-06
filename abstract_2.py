from abc import ABCMeta, abstractmethod
## using @abstractmethod
class Polygon(metaclass=ABCMeta):
	@abstractmethod
	def sides(self):
		pass

class Triangle(Polygon):
	def sides(self):
		print('I have 3 sides')

class Pentagon(Polygon):
	def sides(self):
		print('I have 5 sides')

class Hexagon(Polygon):
	def sides(self):
		print('I have 6 sides!!!')

t = Triangle()
t.sides()
p = Pentagon()
p.sides()
h = Hexagon()
h.sides()