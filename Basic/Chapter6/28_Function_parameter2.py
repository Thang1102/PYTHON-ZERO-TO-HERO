def tong (*data):
	t = 0
	for item in data:
		t = t + item
	return t
ketqua = tong(10,20,30)
print("Ket qua tong : ", ketqua)

def tong2 (*data):
	kq = []
	for item in data:
		tong = 0
		for n in item:
			tong = tong + n
		kq.append(tong)
	return kq
ketqua2 = tong2([2,3,4],[-1,6,-9],[20.-19,10])
print("tong gia tri cua cac ket qua la: ", ketqua2)