name = "mai thanh thang"
print(name.capitalize()) #Viet hoa chu cai dau
print(name.upper())#Viet in hoa tat
name1 = "vu thi linh"
print(name1.swapcase()) # Chuyển in hoa thành  in hoa, in thường 
name2 = "VU THI LINH"
print(name2.swapcase())
chuoi = "Python"
print(chuoi.ljust(10,"*")) #them vao chuoi bang tong so ky tu hien co ví dụ ở python=6 ký tự và thêm tiếp 4 dấu * bên phải
print(chuoi.rjust(10,"*")) #them vao chuoi bang tong so ky tu hien co ví dụ ở python=6 ký tự và thêm tiếp 4 dấu * bên trái
print(chuoi.center(10,"+")) #Thêm đều 2 bên
chuoi = "       ###      ^^ thang  ^^    @@@"
chuoi.lstrip() #bo khoang trang truoc chuoi
chuoi.rstrip() #bo khoang tran sau chuoi
chuoi.strip() #bo khoang trang 2 ben
chuoi.lstrip('#') #bo ky tu # truoc chuoi
chuoi.rstrip("@") #Bo ky tu @ sau chuoi
chuoi.strip('^') #bo cac ky tu ^ truoc va sau chuoi