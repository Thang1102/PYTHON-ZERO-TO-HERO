#Cach 1
li = []
for i in range(10):
	li.append(i ** 2)
print(li)
#Cach 2 Cach viet tat

l = [i ** 2 for i in range(10)]
print(l)
####
leven = []
for i in l:
	if i % 2 == 0:
		leven.append(i)
print(leven)
#Cach 2 Cach viet tat
leven2 = [ i for i in l if i % 2 == 0 ]
print(leven2)

####
lodd = []
for i in l:
	if i % 2 != 0:
		lodd.append(i)
print(lodd)

#Cach 2 : Cach viet tat
lodd2 = [i for i in l if i % 2 != 0] 
print(lodd2)
####
la = [1,2,3]
lb = [4,5,6]
lc = []
for x in la:
	for y in lb:
		lc.append((x,y))# ghep tung phan tu la va lb
print(lc)
#Cach 2:
lc2 = [(x,y) for x in la for y in lb ]
print(lc2)