#dieu kien 
x = 15
y = 50
#if statement
if x > y:
	print ('X: ' , x)
	print ('Y: ' , y)
	print('X lon hon Y') #Truong hop chua nhieu dong trong if
print('OK')

#if-else statement
if x > y :
	print ('X: ' , x)
	print ('Y: ' , y)
	print ("X lon hon Y")
else:
	print ('X: ' , x)
	print ('Y: ' , y)
	print ("X nho hon Y")
print ('OK')

#if-elif-else statement

diem = 4
if diem > 8:
	print('Excellent')
elif diem <= 8 and diem >= 6: #luu y dung dieu kien la and, or
	print('Good')
else:
	print('Bad')