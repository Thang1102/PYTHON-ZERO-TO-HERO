fp = open('data/write.txt','w')
fp.write("Thang")
fp.write("\n")
fp.write("Linh")
fp.write("\n")
fp.write("Thang")
fp.write("\n")
fp.write("Linh")
fp.write("\n")
fp.write("Thang")
fp.write("\n")
fp.write("Linh")
fp.write("\n")
fp.write("Thang")
fp.write("\n")
fp.write("Linh")
print("Done")
#### doc tu mot file va ghi vao file khac
rFile = open("data/list.txt",'r')
wFile = open("data/list2.txt",'w')

for line in rFile:
	print(line, file=wFile,end = "")
print('DONE')