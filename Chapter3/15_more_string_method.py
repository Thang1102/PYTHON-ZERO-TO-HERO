name = 'Mai Thanh Thang'
print(name.find('Mai')) #tim chu Mai vị trí đầu
print(name.find('Linh')) #tim chu Linh (kho co tra lai -1)
chuoi = "Toi la thang toi la hoc vien kma"
print(chuoi.find('la')) #tim chu 'la' nó sẽ lấy luôn chữ đầu
print(chuoi.find('la',10)) # tìm chữ 'là' ở vị trí tiếp theo
print(chuoi.find('la',5,40)) # tìm chữ 'là' ở vị trí tiếp theo xem có k? nếu k -1
'tha' in chuoi #in ra fail vì chữ thang k co trong chuoi
print(chuoi.index("thang toi")) #xac định vị trí trong chuỗi
print(chuoi.replace("la","na")) # sửa nội dung trong chuỗi
s='linh'
s.isalnum() # tra ve true neu có ký tự 0-9,a-z, fail với trường hợp có ký tự đặc biệt xuất hiện trong chuỗi
s.isalpha() # tra về true nếu có kỹ tự a-z, fail với tất cả trường hợp khác
s.isdigit() # tra về true nếu có kỹ tự 0-9, fail với tất cả trường hợp khác
s.isspace() # kiểm tra khoảng chống