#ham("Tuan","Teo","Tun","Hoc Python")
#{"T": 4 , "u": 2,...} đếm chữ
def countChar(*data):
	dic = {}
	for item in data:
		for i in item:
			i = i.upper() #xep thanh hang
			if i in dic:
				dic[i] = dic[i] + 1 # dem xem ky tu giong nhau cong vao
			else:
				dic[i] = 1
	return dic
print(countChar("Tuan", "Teo", "Tun", "Hoc Python"))