d = {"name":"Thang","age":"22","website":"hocvienact.edu.vn"}
print(d)
print(len(d))
print(d['age'])
d['age'] = 23
print(d) # doi voi dict se sap xep du lieu
del d['age']
print(d)
print('age' in d) # check key k check value, trung key gop 2 key thanh 1
print('Thang' not in d)
d.clear() #xoa het list trong d
print(d)
d = {"hs1":"Thang","hs2":"Linh","hs3":"Loi","hs4":"Lien","hs6":"Ly"}
d.pop('hs3') #xoa hs3 trong dict
print(d)
d.popitem()# xoa random
print(d)