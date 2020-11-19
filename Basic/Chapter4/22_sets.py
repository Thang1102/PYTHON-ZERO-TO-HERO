s = {1,2,3,4,5}
print(len(s))
a,b,c,d,e = s
for item in s:
	print(item) # in theo hàng lần lượt
s1 = set('aaaabbbbcccceeeeffffdddd')
print(s1) #sap xep theo a-z
#check xem trong s1 co trong s1 khong ?
print('c' in s1)
A = {1,2,3,4,5}
B = {8,4,7,5,3}
C = A,B # hop set A,B -> tuple
print(C)
C1 = A - B # loai bo phan tu trung nhau
print(C1)
C2 = A | B # Gop 2 set loai nhung phan tu giong set A
print (C2)
C3 = A & B # Lay gia tri  giong nhau giua A, B
print(C3)
C4 = A ^ B # lay gia tri khac nhau giua A, B
print (C4)