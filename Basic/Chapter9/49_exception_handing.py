#quan ly loi
a = 0
b = 100
x = 0 / 100
try:
	c = 100
	d = 0
	x = c/d
except:
	print("Lỗi: So B phai khac 0")

try:
	c = 100
	d = 0
	x = c/d
except ZeroDivisionError as error:
	print("Lỗi: ",error)