# chuoi = "{:10}{:10}".format("Apple",10000) #tao khoang cach cac ky tu
# print(chuoi)
# tong (nokia = 5000,iphone = 10000, motorola = 2000)
#nokia 5000
# iphone 10000
# motorola 2000
# --------------
# tong     ....
def phone (**data): #** la bieu thi 2 gia tri
	count = 0
	for name,price in data.items():
		row = "{:20}{:10}".format(name,price)
		print(row)
		count = count + price
	return count
total = phone(iphone = 10000, samsung = 5500, nokia = 1000)
print ("-" * 30)
chuoitall = "{:20}{:10}".format("Total :", total)
print(chuoitall)