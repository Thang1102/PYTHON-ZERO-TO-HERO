#in ra khong co chu 'h'
for letter in 'python':
	if letter != 'h':
		print(letter) 

#Cach khac dung continue
for letter in 'python':
	if letter == 'h':
		continue
	print(letter)

#Cach dung break
for letter in 'python':
	if letter == 'h':
		break
	print(letter)

#Cach dung pass
for letter in 'python':
	if letter == 'h':
		pass
		print('pass qua roi')
	print(letter)