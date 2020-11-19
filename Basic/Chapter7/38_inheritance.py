class Person:

	def name(self,ten):
		return("Tôi tên là : ", ten)
asian =  Person()
#asian.name("Mai Thắng")
print (asian.name("Mai Thắng"))
###########
class Student(Person): # kế thừa
	def age(self,tuoi):
		return ('Tuổi là', tuoi)
teo = Student()
print(teo.age(23))
print(teo.name("Tony teo"))