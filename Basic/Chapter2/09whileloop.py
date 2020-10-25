#vong lap while
n = 1
while (n < 10):
	print(n, "I love you")
	n += 1
#############
print('\n')
n1 = 1
while (n1 <= 100):
	print(n1, end = ' ') # in khong xuong dong khi co end 
	n1 = n1 + 1
# # in so chan den 100
print('\n')
n3 = 1
while (n3 <= 100):
	if n3 % 2 == 0:
		print(n3, end = ' ') # in khong xuong dong khi co end 
	n3 = n3 + 1
########### thêm  du lieu vao list
print('\n')
n4 = 1
A = []
while (n4 <=100):
	if n4 % 10 == 0:
		A.append(n4) # add cac gia tri phu hop vao list
	n4 = n4 + 1
print(A)