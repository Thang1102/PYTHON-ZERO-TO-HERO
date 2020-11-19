class Person:
	def __init__ (self,age,name): #self là person
		self.name = name # tạo thuộc tính lớp 
		self.age = age   #

	def info ():
		print('Chào bạn tôi tên là : ', self.name, 'Tuổi tôi là: ', self.age)

asia = Person("Mai Thành Thắng", 22)

class Student:
	def __init__(self,grade):
		self.grade = grade

	def infoGrade (self):
		print("Lớp của tôi là: ", self.grade)

hsa = Student("6/5")
hsa.infoGrade()
##########
class Person2:
	def __init__ (self,age,name): #self là person
		self.name = name # tạo thuộc tính lớp 
		self.age = age   #

	def info2 (self):
		print('Chào bạn tôi tên là : ', self.name, 'Tuổi tôi là: ', self.age)
class Student2(Person2):
	def __init__(self,name,age,grade):
		Person2.__init__(self,name,age)
		self.grade = grade

	def infoGrade2 (self):
		print("Lớp của tôi là: ", self.grade)

hsb = Student2("21","Thang", "9/9")
hsb.infoGrade2()
hsb.info2()