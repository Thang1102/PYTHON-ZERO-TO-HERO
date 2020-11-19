class Student :

	def info(self,name,age):
		print("Name : ", name ,"Age: ", age)
jackson = Student()
jackson.info("Robin",18)
###########
class Student2:
	def __init__(self,name,age): #contractor
		print("Name : ", name ,"Age: ", age)
teo = Student2("Tony teo",26) #constractor khi tao doi tuong in ra luon
########### trong init k dung return
class Student3:
	def __init__(self,name,age): #contractor
		print("Name : ", name ,"Age: ", age)
	def __str__(self):
		return('----------------------------')
thang = Student3("Mai Thành Thắng", 22)
print(thang) #tra về return kèm theo đối tượng
########Detractor
class Student4:
	def __init__(self,name,age): #contractor
		print("Name : ", name ,"Age: ", age)
	def __str__(self):
		return('----------------------------')
	def __del__(self):
		print('Destroyed')
teo = Student4("TOny Teo","26")
print(teo)
del teo