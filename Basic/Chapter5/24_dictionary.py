std = {"hs1":"Thang","hs2":"Linh","hs3":"Loi"} # thu vien
print(std)
print(len(std)) #do dai thu vien
del std['hs3'] #xoa phan tu trong thu vien
#neu 1 phan tu cos nhieu trong thu vien chi lay duy nhat 1
print(std)
print(std.keys()) #Lay khoa thu vien
print(std.values()) #lay ra gia tri ung voi khoa
i = std.items()
print(i) # lay gia tri gop lai nhom ()
for item in i:
	print(item[1]) #in ra gia tri cua tung tri theo hang 
	diem = dict(A = 10, B = 7, C = 6)
	print(diem)
	print(list(diem)) # lay lit cac diem gia tri A,B,C,...
	result = {x:x ** 2 for x in range(10)} # in ra dict kieu 0:0, 1:!, 2:4....  