x = range(5)
print(x)
for i in range(5):
	print(i)
x1 =  range(0,5,1)
for i in x1:
	print(i)

def myRange(start,length,step):
	i = start
	while (i < length):
		print(i)
		i +=1
myRange(0,5,1)		

def myRange2(start,length,step):
	i = start
	while (i < length):
		yield i # tra chay tra chay
		#tao mot cai ham chua du lieu ko in ra
		i +=1
t = myRange2(0,5,1) # genertor {tao ham bao mat}
print(t)
def myRange3(start,length,step):
	i = start
	while (i < length):
		return i # tra chay 1 lan duy nhat
		#tao mot cai ham chua du lieu moi in ra
		i +=1
t2 = myRange3(0,5,1) # genertor {tao ham bao mat}
print(t2)
