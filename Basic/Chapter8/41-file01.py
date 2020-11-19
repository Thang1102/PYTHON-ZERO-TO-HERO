fp = open("data/list.txt","r") #đọc file
for line in fp :
	print(line, end " ")
fp.close()  #đong file sau đọc

##### dem dong trong file
fp = open("data/list.txt","r")
i = 0
for line in fp :
	i = i + 1
	print(line, end " ")
fp.close()
print()
print("Tông số dòng", i)