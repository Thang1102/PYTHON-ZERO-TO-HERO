#in ra chuỗi
t = (1,2,3,4,5)
for n in t:
	print(n, end= ' ')
#Danh so phan tu
print('\n')
t1 = (1,3,5,7)
i = 0
for n in t1:
	print(i, end= ' ')
	i +=1
#in ra so lan phan tu
print('\n')
t2 = (4,1,6,9)
for n in t2:
	print("I love you ")
############## chuoi
print('\n')
l =[10,20,30,40,50]
for n in l:
	print(n, end= ' ')
print('\n')
############### dict
d={'Vu':27, 'Thi': 11, 'Linh' : 1998}
for key in d:
	print(key) #lay strings trong dict
for key in d:
	print(d[key]) #lay ra number trong dict
print('\n')
################# string
ss = 'Mai Thanh Thang'
for s in ss:
	if(s != ' '):# loai khoang trang
		print(s * 10) #in ra lap lai ky tu
