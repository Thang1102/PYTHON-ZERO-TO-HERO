class Car: #lop
	fuel = "Xăng" # thuoc tinh
	maxspeed = 150
polo = Car()  #tao doi tuong 
print(polo.fuel) # truy xuat lay du lieu tu lop

class Car2: #lop
	fuel = "Xăng" # thuoc tinh
	maxspeed2 = 150
	def  drive1(self):
		print("Xe chay toc do: ", self.maxspeed2)
mini = Car2()
mini.drive1() # lay du lieu bang ham

class Car3: #lop
	fuel = "Xăng" # thuoc tinh
	maxspeed = 150
	def drive (self,maxspeed):
		print("Xe chay toc do: ",maxspeed)
thang = Car3()
thang.drive(300) #thay thuoc tinh
