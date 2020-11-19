f = open("data/data.txt",encoding = "utf8")
fpos = f.tell() # doc lần lượt từng đoạn.
print("Đọc tới vị trí ",fpos)

line = f.readline()
print(line, end = '')

fpos = f.tell()
print("Đọc tới vị trí ",fpos)

line = f.readline()
print(line, end = '')

fpos = f.tell()
print("Đọc tới vị trí ",fpos)

line = f.readline()
print(line, end = '')

fpos = f.tell()
print("Đọc tới vị trí ",fpos)

line = f.readline()
print(line, end = '')

fpos = f.tell()
print("Đọc tới vị trí ",fpos)

line = f.readline()
print(line, end = '')

fpos = f.tell()
print("Đọc tới vị trí ",fpos)

line = f.readline()
print(line, end = '')

fpos = f.tell()
print("Đọc tới vị trí ",fpos)

f.seek(241) #doc tu vi tri 241
print('-' *50)
data = f.read()
print (len(data))
print(data)
