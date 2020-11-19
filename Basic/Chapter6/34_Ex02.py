# range(5) => 0,1,2,3,4 range(0,5,1)
# range (0,5) => 0,1,2,3,4 range(0,5,1)
# range(0,6,2) => 0,2,4
def myRange (*thamso) :
	start = length = step = 0
	if (len(thamso) == 3):
		start = thamso[0]
		length = thamso[1]
		step = thamso [2]
	elif (len(thamso) == 2):
		start = thamso[0]
		length = thamso[1]
		step = 1
	else:
		start = 0
		length = thamso[0]
		step = 1
	i = start
	while (i < length):
		yield i
		i = i + step
A = myRange(5)
B = myRange(0,5)
C = myRange(0,6,2)
print (list(A))
print (list(B))
print (list(C))