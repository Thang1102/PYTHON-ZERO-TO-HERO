####GHI De
BUFFERSIZE = 25
rFile = open("data/list.txt","r")
wFile = open ("data/write.txt","w")

buffer = rFile.read(BUFFERSIZE)#doc het file list
i = 0
while (len(buffer)) : #cu moi lan dem 25 roi doc 1 lan
	i = i + 1
	wFile.write(buffer)
	print(i,"() byte",format(len(buffer))) 
	buffer = rFile.read(BUFFERSIZE)
print("DONE")
###Doc ghi doc ghi lien tuc