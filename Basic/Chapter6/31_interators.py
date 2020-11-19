l = [1,2,3,4,5,6]
for i in l:
	print(i)
l = "Mai Thắng"
for i in l:
	print(i)
l1 = [1,2,3,4,5,6]
I = iter(l1)# list_iterator
print(I.__next__()) # cắt chuỗi lần lượt
print(I.__next__())
print(I.__next__())
print(I.__next__())
l2 = "Mai Thắng"
I1 = iter(l2) # str_iterator
print(I1.__next__()) # cắt chuỗi lần lượt từng phần tử
print(I1.__next__())
