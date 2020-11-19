def tong (n1,n2,n3,*data,**lists):
	t1 = t2 = t3 = 0
	t1 = n1 + n2 + n3
	for item in data:
		t2 = t2 + item
	for k,v in lists.items():
		row = "{:20}{:10}".format(k,v)
		print(row)
		t3  = t3 + v
	t = [t1,t2,t3]
	return t
kq = tong(10,20,30,11,12,13,14,15,one = 100, two = 200, three = 300)
print ("-" * 30)
print(kq)
