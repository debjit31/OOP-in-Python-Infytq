# Python program showing a 
# use of property() function 

class Geeks: 
	def __init__(self):
	##__age is a private attribute  
		self.__age = 0
	
	
	def get_age(self): 
		print("getter method called") 
		return self.__age 
	

	def set_age(self, a): 
		print("setter method called") 
		self.__age = a 

	
	def del_age(self): 
		del self.__age 
	
	age = property(get_age, set_age, del_age) 

mark = Geeks() 
##print(mark._Geeks__age)
mark.age = 10
print(mark.age) 
